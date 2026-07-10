from __future__ import annotations

import argparse
import json
import os
import re
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUT = ROOT / "gold_data" / "final_dg_all.json"
OUT_DIR = ROOT / "gold_data" / "ai_distillation"
RULE_PATHS = [
    ROOT / "skill" / "dg-questionnaire-designer" / "SKILL.md",
    ROOT / "skill" / "dg-questionnaire-designer" / "references" / "research_rules.md",
    ROOT / "skill" / "dg-questionnaire-designer" / "references" / "generation_logic.md",
    ROOT / "skill" / "dg-question-wording-editor" / "SKILL.md",
    ROOT / "skill" / "dg-question-wording-editor" / "references" / "style_rules.md",
    ROOT / "skill" / "dg-question-wording-editor" / "references" / "rewrite_patterns.md",
]


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8-sig", errors="replace")


def read_json(path: Path) -> Any:
    return json.loads(read_text(path))


def clean(value: Any) -> str:
    if value is None:
        return ""
    return re.sub(r"\s+", " ", str(value)).strip()


def compact_text(text: str, max_chars: int) -> str:
    text = clean(text)
    if len(text) <= max_chars:
        return text
    head = text[: int(max_chars * 0.7)].rstrip()
    tail = text[-int(max_chars * 0.2) :].lstrip()
    return f"{head}\n...[omitted]...\n{tail}"


def as_int(value: Any, default: int = 0) -> int:
    if isinstance(value, int):
        return value
    if isinstance(value, dict) and "$numberLong" in value:
        try:
            return int(value["$numberLong"])
        except (TypeError, ValueError):
            return default
    try:
        return int(value)
    except (TypeError, ValueError):
        return default


def modules(project: dict[str, Any]) -> list[dict[str, Any]]:
    raw = project.get("modules")
    if not isinstance(raw, list):
        return []
    return sorted((m for m in raw if isinstance(m, dict)), key=lambda m: as_int(m.get("index")))


def questions(module: dict[str, Any]) -> list[dict[str, Any]]:
    raw = module.get("questions")
    if not isinstance(raw, list):
        return []
    return sorted((q for q in raw if isinstance(q, dict)), key=lambda q: as_int(q.get("index")))


def project_digest(project: dict[str, Any], max_questions_per_module: int = 6) -> dict[str, Any]:
    digest_modules = []
    total_questions = 0
    for module in modules(project):
        qs = questions(module)
        total_questions += len(qs)
        question_samples = []
        for question in qs[:max_questions_per_module]:
            question_samples.append(
                {
                    "type": clean(question.get("type")),
                    "sub_type": clean(question.get("sub_type")),
                    "require_image": bool(question.get("require_image")),
                    "require_video": bool(question.get("require_video")),
                    "title": compact_text(clean(question.get("title")), 360),
                    "bot_prompt": compact_text(clean(question.get("bot_prompt")), 220),
                }
            )
        digest_modules.append(
            {
                "title": clean(module.get("title")) or "(untitled)",
                "type": clean(module.get("type")),
                "question_count": len(qs),
                "question_samples": question_samples,
            }
        )

    return {
        "project_id": clean(project.get("id")),
        "name": compact_text(clean(project.get("name")), 120),
        "description": compact_text(clean(project.get("description")), 180),
        "status": clean(project.get("status")),
        "language": clean(project.get("language")),
        "module_count": len(digest_modules),
        "question_count": total_questions,
        "modules": digest_modules,
    }


def load_rule_context() -> str:
    chunks = []
    for path in RULE_PATHS:
        if path.exists():
            chunks.append(f"## {path.relative_to(ROOT)}\n\n{compact_text(read_text(path), 6000)}")
    return "\n\n---\n\n".join(chunks)


def build_messages(batch: list[dict[str, Any]], focus: str) -> list[dict[str, str]]:
    rule_context = load_rule_context()
    focus_instruction = {
        "designer": "只提炼 questionnaire designer 相关规则：研究逻辑、模块结构、模块顺序、任务设计、Diary vs IDI、品牌曝光、评估规则。",
        "wording": "只提炼 wording editor 相关规则：题面自然度、开放性、媒体请求、括号/例子、负担控制、品牌曝光措辞。",
        "both": "同时提炼 designer 和 wording 两类规则，但每条规则必须明确目标 skill。",
    }[focus]
    if focus == "wording":
        focus_instruction += (
            " 这次优先提炼语言风格和可复用改写手法，不要把模块结构、研究设计、任务负担控制当成主要结论。"
            " 重点观察：开场语怎么自然、动词怎么选、命令句如何软化、研究员话术如何改成受访者任务、"
            "例子和括号的长度、媒体请求的语气、敏感问题的委婉问法、评分/排序前后的承接语。"
            " 每条候选规则必须包含可直接写入 style/rewrite/rubric 的 wording 表述。"
        )

    system = f"""
你是一个资深消费者研究方法论专家，正在帮助团队从历史 final DG 数据中离线提炼可沉淀进 Codex skill 的规则。

重要原则：
- 不要复制历史题目原文。
- 不要把个案内容当成规则。
- 如果历史数据与现有规则冲突，以现有规则为主，只把冲突作为 review evidence。
- 只输出少量高价值候选规则。
- 每条候选规则必须能解释为什么值得进入 skill，或者为什么只适合作为负面提醒。
- {focus_instruction}

你会看到两类输入：
1. 当前已有 skill 规则摘要。
2. 一小批 final DG 项目 digest，每个项目只保留模块和少量题面样本。

请输出 JSON，不要输出 Markdown。
JSON 格式：
{{
  "batch_summary": "一句话概括这一批数据给你的启发",
  "candidates": [
    {{
      "target_skill": "dg-questionnaire-designer | dg-question-wording-editor",
      "target_file": "建议写入的 skill reference 文件",
      "candidate_type": "module_order | task_design | diary_idi | brand_exposure | wording_naturalness | media_burden | negative_pattern | eval_rule | other",
      "title": "短标题",
      "proposed_rule": "可直接进入 skill 的规则文本，中文，尽量短",
      "why_from_data": "你从这批数据观察到了什么，不要引用长原文",
      "existing_rule_relation": "extends_existing | clarifies_existing | conflicts_with_existing | new_candidate",
      "conflict_policy": "如果与现有规则冲突，应如何处理",
      "evidence_project_ids": ["项目 id，最多 5 个"],
      "risk": "low | medium | high"
    }}
  ]
}}

JSON 输出约束：
- 只输出一个 JSON object，不要包 Markdown code fence。
- 所有字段值都用短中文纯文本；不要在 JSON 字符串里写 Markdown 标题、表格、列表、Before/After 代码块或三反引号。
- `proposed_rule` 控制在 2-4 句，可直接写入 skill；如需示例，用中文书名号/引号「」包裹，不要使用英文双引号。
- 不要在字符串里使用未转义的英文双引号；需要强调词语时用「」。
- 如果想提供 rewrite 示例，只写成一句 “可改为：……” 的短句，不要写多行代码块。
""".strip()

    user = f"""
# 当前已有 skill 规则摘要

{rule_context}

# 本批 final DG digest

{json.dumps(batch, ensure_ascii=False, indent=2)}
""".strip()

    return [{"role": "system", "content": system}, {"role": "user", "content": user}]


def call_chat(messages: list[dict[str, str]], model: str) -> str:
    api_key = os.environ.get("CHATANYWHERE_API_KEY")
    if not api_key:
        raise RuntimeError("Missing CHATANYWHERE_API_KEY environment variable.")

    base_url = os.environ.get("CHATANYWHERE_BASE_URL", "https://api.chatanywhere.tech/v1").rstrip("/")
    url = f"{base_url}/chat/completions"
    payload = {"model": model, "messages": messages, "temperature": 0.1}
    request = urllib.request.Request(
        url=url,
        data=json.dumps(payload, ensure_ascii=False).encode("utf-8"),
        headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=240) as response:
            raw = response.read().decode("utf-8")
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"Chat completion HTTP {exc.code}: {body}") from exc
    data = json.loads(raw)
    try:
        return data["choices"][0]["message"]["content"]
    except (KeyError, IndexError, TypeError) as exc:
        raise RuntimeError(f"Unexpected response shape: {raw[:2000]}") from exc


def parse_json_response(text: str) -> dict[str, Any]:
    cleaned = text.strip()
    if cleaned.startswith("```"):
        cleaned = re.sub(r"^```(?:json)?", "", cleaned).strip()
        cleaned = re.sub(r"```$", "", cleaned).strip()
    return json.loads(cleaned)


def filter_candidates_for_focus(result: dict[str, Any], focus: str) -> dict[str, Any]:
    if focus == "both":
        return result

    expected_skill = {
        "designer": "dg-questionnaire-designer",
        "wording": "dg-question-wording-editor",
    }[focus]
    candidates = result.get("candidates", [])
    if not isinstance(candidates, list):
        result["candidates"] = []
        return result

    result["candidates"] = [
        candidate
        for candidate in candidates
        if isinstance(candidate, dict) and candidate.get("target_skill") == expected_skill
    ]
    return result


def chunked(items: list[dict[str, Any]], size: int) -> list[list[dict[str, Any]]]:
    return [items[index : index + size] for index in range(0, len(items), size)]


def write_markdown_summary(path: Path, results: list[dict[str, Any]]) -> None:
    lines = [
        "# AI Gold Rule Candidates",
        "",
        f"- Created at: {datetime.now(timezone.utc).isoformat()}",
        f"- Batches: {len(results)}",
        "",
        "These are AI-generated candidates. Human review is required before skill promotion.",
        "",
    ]
    counter = 0
    for batch_index, result in enumerate(results, start=1):
        lines.extend([f"## Batch {batch_index}", "", result.get("batch_summary", ""), ""])
        for candidate in result.get("candidates", []):
            counter += 1
            lines.extend(
                [
                    f"### {counter}. {candidate.get('title', 'Untitled')}",
                    "",
                    f"- Target skill: `{candidate.get('target_skill', '')}`",
                    f"- Target file: `{candidate.get('target_file', '')}`",
                    f"- Type: `{candidate.get('candidate_type', '')}`",
                    f"- Relation: `{candidate.get('existing_rule_relation', '')}`",
                    f"- Risk: `{candidate.get('risk', '')}`",
                    f"- Evidence projects: {', '.join(candidate.get('evidence_project_ids', []))}",
                    "",
                    "Proposed rule:",
                    "",
                    f"> {candidate.get('proposed_rule', '')}",
                    "",
                    "Why from data:",
                    "",
                    f"> {candidate.get('why_from_data', '')}",
                    "",
                    "Conflict policy:",
                    "",
                    f"> {candidate.get('conflict_policy', '')}",
                    "",
                ]
            )
    path.write_text("\n".join(lines), encoding="utf-8-sig")


def main() -> int:
    parser = argparse.ArgumentParser(description="Use an OpenAI-compatible model to distill skill rule candidates from compact final DG batches.")
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--out-dir", type=Path, default=OUT_DIR)
    parser.add_argument("--model", default=os.environ.get("CHATANYWHERE_MODEL", "claude-opus-4-6"))
    parser.add_argument("--focus", choices=["designer", "wording", "both"], default="both")
    parser.add_argument("--max-projects", type=int, default=24)
    parser.add_argument("--batch-size", type=int, default=6)
    parser.add_argument("--max-questions-per-module", type=int, default=6)
    parser.add_argument("--run", action="store_true", help="Actually call the configured chat completion API. Without this flag, only prompt previews are written.")
    args = parser.parse_args()

    input_path = args.input if args.input.is_absolute() else ROOT / args.input
    out_dir = args.out_dir if args.out_dir.is_absolute() else ROOT / args.out_dir
    data = read_json(input_path)
    if not isinstance(data, list):
        raise TypeError("Expected top-level JSON to be a list.")

    digests = [
        project_digest(item, max_questions_per_module=args.max_questions_per_module)
        for item in data
        if isinstance(item, dict) and modules(item)
    ]
    digests = digests[: args.max_projects]
    batches = chunked(digests, args.batch_size)
    out_dir.mkdir(parents=True, exist_ok=True)

    results: list[dict[str, Any]] = []
    for batch_index, batch in enumerate(batches, start=1):
        messages = build_messages(batch, args.focus)
        prompt_path = out_dir / f"batch_{batch_index:03d}_prompt.json"
        prompt_path.write_text(json.dumps(messages, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"Prompt preview: {prompt_path}")

        if not args.run:
            continue

        response_text = call_chat(messages, args.model)
        response_path = out_dir / f"batch_{batch_index:03d}_response.json"
        response_path.write_text(response_text, encoding="utf-8")
        result = filter_candidates_for_focus(parse_json_response(response_text), args.focus)
        results.append(result)
        print(f"Response: {response_path}")

    if args.run:
        merged_json_path = out_dir / "ai_rule_candidates.json"
        merged_md_path = out_dir / "ai_rule_candidates.md"
        merged_json_path.write_text(
            json.dumps(
                {
                    "source": str(input_path.relative_to(ROOT)),
                    "created_at": datetime.now(timezone.utc).isoformat(),
                    "model": args.model,
                    "focus": args.focus,
                    "human_review_required": True,
                    "batches": results,
                },
                ensure_ascii=False,
                indent=2,
            ),
            encoding="utf-8",
        )
        write_markdown_summary(merged_md_path, results)
        print(f"Merged JSON: {merged_json_path}")
        print(f"Merged Markdown: {merged_md_path}")
    else:
        print("Dry run only. Add --run to call the configured model API.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

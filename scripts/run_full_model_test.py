from __future__ import annotations

import argparse
import json
import os
import socket
import sys
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from prompt import ChatMessage, PromptBundle, build_generation_prompt, compact_text
from test_prompt_with_cases import case_dir_for_id, load_case_inputs, normalize_case_id, project_info_for_case


OUT_DIR = ROOT / "tests" / "model_tests"
WORDING_SKILL_DIR = ROOT / "skill" / "dg-question-wording-editor"
WORDING_AGENT_CONFIG_PATH = WORDING_SKILL_DIR / "agents" / "openai.yaml"
WORDING_REFERENCE_PATHS = [
    WORDING_SKILL_DIR / "SKILL.md",
    WORDING_SKILL_DIR / "references" / "style_rules.md",
    WORDING_SKILL_DIR / "references" / "rewrite_patterns.md",
    WORDING_SKILL_DIR / "references" / "module_tone_guides.md",
    WORDING_SKILL_DIR / "references" / "wording_eval_rubric.md",
]


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8-sig", errors="replace")


def load_default_system_prompt(path: Path) -> str:
    if not path.exists():
        return ""

    lines = read_text(path).splitlines()
    for index, line in enumerate(lines):
        stripped = line.strip()
        if not stripped.startswith("default_system_prompt:"):
            continue

        key_indent = len(line) - len(line.lstrip(" "))
        value = stripped.partition(":")[2].strip()
        if value and value not in {"|", ">"}:
            return value.strip("\"'")

        block_lines: list[str] = []
        block_indent: int | None = None
        for block_line in lines[index + 1 :]:
            if block_line.strip():
                current_indent = len(block_line) - len(block_line.lstrip(" "))
                if current_indent <= key_indent:
                    break
                if block_indent is None:
                    block_indent = current_indent
            if block_indent is None:
                block_lines.append("")
            else:
                block_lines.append(block_line[block_indent:])
        return "\n".join(block_lines).strip()

    return ""


def call_chatanywhere(messages: list[dict[str, str]], model: str, temperature: float, timeout: int) -> str:
    api_key = os.environ.get("CHATANYWHERE_API_KEY")
    if not api_key:
        raise RuntimeError("Missing CHATANYWHERE_API_KEY environment variable.")

    base_url = os.environ.get("CHATANYWHERE_BASE_URL", "https://api.chatanywhere.tech/v1").rstrip("/")
    url = f"{base_url}/chat/completions"
    payload = {"model": model, "messages": messages, "temperature": temperature}
    request = urllib.request.Request(
        url=url,
        data=json.dumps(payload, ensure_ascii=False).encode("utf-8"),
        headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
        method="POST",
    )

    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            raw = response.read().decode("utf-8")
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"ChatAnywhere HTTP {exc.code}: {body}") from exc
    except TimeoutError as exc:
        raise RuntimeError(
            f"ChatAnywhere request timed out after {timeout}s. "
            "Try a larger --timeout value, a faster model, or --wording-only if designer output already exists."
        ) from exc
    except socket.timeout as exc:
        raise RuntimeError(
            f"ChatAnywhere request timed out after {timeout}s. "
            "Try a larger --timeout value, a faster model, or --wording-only if designer output already exists."
        ) from exc

    data = json.loads(raw)
    try:
        return data["choices"][0]["message"]["content"]
    except (KeyError, IndexError, TypeError) as exc:
        raise RuntimeError(f"Unexpected response shape: {raw[:2000]}") from exc


def build_wording_prompt(designer_output: str) -> PromptBundle:
    references = []
    for path in WORDING_REFERENCE_PATHS:
        references.append(f"## {path.relative_to(ROOT)}\n\n{compact_text(read_text(path), 12000)}")

    default_system_prompt = load_default_system_prompt(WORDING_AGENT_CONFIG_PATH)
    default_system_section = (
        f"# Default system prompt from {WORDING_AGENT_CONFIG_PATH.relative_to(ROOT)}\n\n"
        f"{default_system_prompt}\n\n"
        if default_system_prompt
        else ""
    )

    system = f"""
{default_system_section}
你是 `dg-question-wording-editor`，负责把 questionnaire designer 产出的研究完整 DG 草稿改写成受访者可读、自然、开放、低负担的最终 DG wording。

你必须遵守：

1. 保留 designer 已确定的模块顺序、研究目的、观察点、任务时机、Diary vs IDI 分工、品牌/刺激物暴露顺序。
2. 不重新设计研究方案，除非发现明显研究风险；风险只放在简短的 remaining research questions。
3. 固定 About Me 开场若已出现，必须保持固定模板，不要擅自改写。
4. 删除或改写受访者题面中的研究员话术、内部逻辑、HTML 标签、占位符、过长括号、过硬命令句。
5. 媒体请求默认软化为可选支持；若 designer 标明强制或平台要求，保留要求但降低压迫感。
6. 输出完整 Markdown，不要输出 JSON。
7. 主交付是修订后的 DG wording，不要长篇解释。
8. 采用最小必要改写：如果 designer 的引导语、题目或结束语已经自然、具体、可回答，不要为了“润色”而改写。
9. 不要统一抹掉年轻化但自然的语气词、波浪号、轻松表达或项目合适的口语；只有在过度、做作、年龄不适配或影响清晰度时才调整。
10. 优先修复明确问题：researcher-facing 话术、checklist、过长括号、暴露研究目的、负担过重、结束语过度感谢或 AI 主持人腔。

# Wording skill references

{chr(10).join(references)}
""".strip()

    user = f"""
# Designer draft to rewrite

{compact_text(designer_output, 50000)}

# Task

请执行完整 wording pass，输出：

## Wording Pass Complete
- preserved research intent:
- major wording changes:
- remaining research questions for designer agent:

## Revised DG Wording

保留 designer 的主要结构和已经自然的受访者表达。只改写确实存在问题的引导语、题目、结束语和素材请求；不要全量重写。
""".strip()

    return PromptBundle(
        messages=[
            ChatMessage(role="system", content=system),
            ChatMessage(role="user", content=user),
        ]
    )


def write_prompt_preview(path: Path, bundle: PromptBundle) -> None:
    lines = []
    for index, message in enumerate(bundle.messages, start=1):
        lines.extend(
            [
                "---",
                "",
                f"## Message {index}: {message.role}",
                "",
                "```text",
                message.content,
                "```",
                "",
            ]
        )
    path.write_text("\n".join(lines), encoding="utf-8-sig")


def main() -> int:
    parser = argparse.ArgumentParser(description="Run a full DG model test: designer draft -> wording final.")
    parser.add_argument("--case", default="case_001", help="Case id, for example case_005 or 005.")
    parser.add_argument("--case-root", default=os.environ.get("DG_AGENT_CASE_ROOT", str(ROOT / "case_data")))
    parser.add_argument("--model", default=os.environ.get("CHATANYWHERE_MODEL", "claude-opus-4-6"))
    parser.add_argument("--dry-run", action="store_true", help="Write prompt previews without calling the model.")
    parser.add_argument("--timeout", type=int, default=int(os.environ.get("CHATANYWHERE_TIMEOUT", "600")), help="API request timeout in seconds.")
    parser.add_argument("--wording-only", action="store_true", help="Reuse an existing designer output and only run the wording editor.")
    args = parser.parse_args()

    case_id = normalize_case_id(args.case)
    case_root = Path(args.case_root)
    case_dir = case_dir_for_id(case_root, case_id)
    files = load_case_inputs(case_dir)
    project_info = project_info_for_case(case_id, case_dir)
    designer_bundle = build_generation_prompt(project_info=project_info, files=files)

    OUT_DIR.mkdir(exist_ok=True)
    designer_prompt_path = OUT_DIR / f"{case_id}_{args.model}_designer_prompt.md"
    write_prompt_preview(designer_prompt_path, designer_bundle)

    print(f"Model: {args.model}")
    print(f"Case: {case_id}")
    print(f"Case folder: {case_dir}")
    print(f"Selected cases: {', '.join(designer_bundle.selected_case_ids) or 'none'}")
    print(f"Input files: {len(files)}")
    print(f"Designer prompt: {designer_prompt_path}")
    print(f"Timeout: {args.timeout}s")

    if args.dry_run:
        designer_out_path = OUT_DIR / f"{case_id}_{args.model}_designer_output.md"
        if designer_out_path.exists():
            designer_output = read_text(designer_out_path)
            wording_bundle = build_wording_prompt(designer_output)
            wording_prompt_path = OUT_DIR / f"{case_id}_{args.model}_wording_prompt.md"
            write_prompt_preview(wording_prompt_path, wording_bundle)
            print(f"Wording prompt: {wording_prompt_path}")
        else:
            print(f"Wording prompt skipped: no existing designer output at {designer_out_path}")
        print("Dry run only. Add --run by omitting --dry-run to call the configured model API.")
        return 0

    designer_out_path = OUT_DIR / f"{case_id}_{args.model}_designer_output.md"
    if args.wording_only:
        if not designer_out_path.exists():
            raise FileNotFoundError(f"--wording-only requires existing designer output: {designer_out_path}")
        designer_output = read_text(designer_out_path)
        print(f"Designer output reused: {designer_out_path}")
    else:
        print("Calling designer...")
        designer_output = call_chatanywhere(designer_bundle.to_openai_messages(), args.model, temperature=0.2, timeout=args.timeout)
        designer_out_path.write_text(designer_output, encoding="utf-8-sig")
        print(f"Designer output: {designer_out_path}")

    wording_bundle = build_wording_prompt(designer_output)
    wording_prompt_path = OUT_DIR / f"{case_id}_{args.model}_wording_prompt.md"
    write_prompt_preview(wording_prompt_path, wording_bundle)
    print(f"Wording prompt: {wording_prompt_path}")

    print("Calling wording editor...")
    wording_output = call_chatanywhere(wording_bundle.to_openai_messages(), args.model, temperature=0.15, timeout=args.timeout)
    wording_out_path = OUT_DIR / f"{case_id}_{args.model}_full_output.md"
    wording_out_path.write_text(wording_output, encoding="utf-8-sig")
    print(f"Full output: {wording_out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

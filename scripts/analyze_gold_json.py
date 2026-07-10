from __future__ import annotations

import argparse
import json
import re
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUT = ROOT / "gold_data" / "final_dg_all.json"
OUT_DIR = ROOT / "gold_data" / "reports"


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8-sig"))


def scalar(value: Any) -> str:
    if value is None:
        return "None"
    if isinstance(value, dict):
        if "$date" in value:
            return str(value["$date"])
        if "$numberLong" in value:
            return str(value["$numberLong"])
        if "$oid" in value:
            return str(value["$oid"])
    return str(value)


def clean_text(value: Any) -> str:
    if value is None:
        return ""
    return re.sub(r"\s+", " ", str(value)).strip()


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


def iter_modules(project: dict[str, Any]) -> list[dict[str, Any]]:
    modules = project.get("modules")
    return modules if isinstance(modules, list) else []


def iter_questions(module: dict[str, Any]) -> list[dict[str, Any]]:
    questions = module.get("questions")
    return questions if isinstance(questions, list) else []


def top(counter: Counter[str], limit: int = 20) -> list[tuple[str, int]]:
    return counter.most_common(limit)


def sample(counter: dict[str, list[str]], key: str, limit: int = 5) -> list[str]:
    return counter.get(key, [])[:limit]


def add_sample(samples: dict[str, list[str]], key: str, value: str, limit: int = 8) -> None:
    value = clean_text(value)
    if not value:
        return
    bucket = samples.setdefault(key, [])
    if len(bucket) < limit and value not in bucket:
        bucket.append(value)


def classify_question(text: str, question: dict[str, Any]) -> set[str]:
    labels: set[str] = set()
    lowered = text.lower()
    if question.get("require_image") or "照片" in text or "拍照" in text:
        labels.add("image_request")
    if question.get("require_video") or "视频" in text or "录制" in text:
        labels.add("video_request")
    if "打分" in text or "评分" in text or scalar(question.get("type")) == "score":
        labels.add("score")
    if "排序" in text or "排名" in text or scalar(question.get("type")) == "sort":
        labels.add("sort")
    if "品牌" in text or "brand" in lowered:
        labels.add("brand_exposure")
    if "购买" in text or "购物" in text or "下单" in text:
        labels.add("shopping")
    if "使用" in text or "食用" in text or "喝" in text or "吃" in text:
        labels.add("usage")
    if "为什么" in text or "原因" in text or "感受" in text:
        labels.add("why_or_feeling")
    if "请问" in text:
        labels.add("polite_question")
    if "可以" in text and ("分享" in text or "说说" in text):
        labels.add("soft_open_prompt")
    return labels


def build_inventory(projects: list[dict[str, Any]]) -> dict[str, Any]:
    project_keys: Counter[str] = Counter()
    status: Counter[str] = Counter()
    language: Counter[str] = Counter()
    project_type: Counter[str] = Counter()
    module_type: Counter[str] = Counter()
    question_type: Counter[str] = Counter()
    question_subtype: Counter[str] = Counter()
    module_title: Counter[str] = Counter()
    first_module_title: Counter[str] = Counter()
    question_labels: Counter[str] = Counter()
    module_count_hist: Counter[str] = Counter()
    question_count_hist: Counter[str] = Counter()
    module_sequence: Counter[str] = Counter()
    samples: dict[str, list[str]] = {}

    total_modules = 0
    total_questions = 0
    empty_modules = 0
    empty_projects = 0
    projects_with_image = 0
    projects_with_video = 0

    for project in projects:
        project_keys.update(project.keys())
        status[scalar(project.get("status"))] += 1
        language[scalar(project.get("language"))] += 1
        project_type[scalar(project.get("project_type"))] += 1

        modules = sorted(iter_modules(project), key=lambda m: as_int(m.get("index")))
        total_modules += len(modules)
        module_count_hist[str(len(modules))] += 1
        if not modules:
            empty_projects += 1

        sequence_titles: list[str] = []
        project_has_image = False
        project_has_video = False
        project_question_count = 0

        for index, module in enumerate(modules):
            questions = sorted(iter_questions(module), key=lambda q: as_int(q.get("index")))
            module_name = clean_text(module.get("title")) or "(untitled)"
            sequence_titles.append(module_name)
            module_title[module_name] += 1
            module_type[scalar(module.get("type"))] += 1
            if index == 0:
                first_module_title[module_name] += 1
            if not questions:
                empty_modules += 1

            total_questions += len(questions)
            project_question_count += len(questions)

            add_sample(samples, f"module:{module_name}", module_name)
            for question in questions:
                q_text = clean_text(question.get("title"))
                q_type = scalar(question.get("type"))
                q_subtype = scalar(question.get("sub_type"))
                question_type[q_type] += 1
                question_subtype[q_subtype] += 1
                labels = classify_question(q_text, question)
                question_labels.update(labels)
                if question.get("require_image"):
                    project_has_image = True
                if question.get("require_video"):
                    project_has_video = True
                for label in labels:
                    add_sample(samples, f"question_label:{label}", q_text)
                if index == 0 and len(sample(samples, "opening_questions", 10)) < 10:
                    add_sample(samples, "opening_questions", q_text, limit=10)
                if q_type in {"start", "end", "halftime"}:
                    add_sample(samples, f"platform_question:{q_type}", q_text)

        if sequence_titles:
            module_sequence[" -> ".join(sequence_titles[:8])] += 1
        question_count_hist[str(project_question_count)] += 1
        if project_has_image:
            projects_with_image += 1
        if project_has_video:
            projects_with_video += 1

    return {
        "created_at": datetime.now(timezone.utc).isoformat(),
        "project_count": len(projects),
        "total_modules": total_modules,
        "total_questions": total_questions,
        "avg_modules_per_project": round(total_modules / max(len(projects), 1), 2),
        "avg_questions_per_project": round(total_questions / max(len(projects), 1), 2),
        "empty_projects": empty_projects,
        "empty_modules": empty_modules,
        "projects_with_image_request": projects_with_image,
        "projects_with_video_request": projects_with_video,
        "project_keys": top(project_keys, 50),
        "status": top(status),
        "language": top(language),
        "project_type": top(project_type),
        "module_type": top(module_type),
        "question_type": top(question_type),
        "question_subtype": top(question_subtype),
        "module_title": top(module_title, 40),
        "first_module_title": top(first_module_title, 20),
        "question_labels": top(question_labels, 20),
        "module_count_hist": top(module_count_hist, 30),
        "question_count_hist": top(question_count_hist, 50),
        "module_sequence": top(module_sequence, 25),
        "samples": samples,
    }


def build_designer_patterns(inventory: dict[str, Any]) -> dict[str, Any]:
    return {
        "purpose": "Patterns for dg-questionnaire-designer. Use for structure, order, task logic, and evaluation; do not copy respondent wording mechanically.",
        "source": "gold_data/final_dg_all.json",
        "created_at": inventory["created_at"],
        "project_count": inventory["project_count"],
        "priority_rule": "Use these patterns as empirical reference only. Existing research_rules.md, generation_logic.md, case cards, Brief, Proposal, and explicit client requirements take priority when there is any conflict.",
        "summary": {
            "avg_modules_per_project": inventory["avg_modules_per_project"],
            "avg_questions_per_project": inventory["avg_questions_per_project"],
            "projects_with_image_request": inventory["projects_with_image_request"],
            "projects_with_video_request": inventory["projects_with_video_request"],
        },
        "common_module_titles": inventory["module_title"][:30],
        "common_first_modules": inventory["first_module_title"][:15],
        "common_module_sequences": inventory["module_sequence"][:20],
        "question_type_distribution": inventory["question_type"],
        "detected_task_labels": inventory["question_labels"],
        "recommended_skill_updates": [
            "Use module sequence statistics as retrieval hints before drafting a DG structure.",
            "Use first-module statistics to protect broad person/life-context openings before category or brand exposure.",
            "Use image/video request rates and samples to keep Diary tasks answerable without excessive proof burden.",
            "Use platform question types such as start, halftime, and end as export/platform constraints, not as core research questions.",
            "Record conflicts between gold-data patterns and existing rules as eval notes instead of overriding current rules.",
        ],
    }


def build_wording_patterns(inventory: dict[str, Any]) -> dict[str, Any]:
    samples = inventory["samples"]
    return {
        "purpose": "Patterns for dg-question-wording-editor. Use for natural respondent-facing Chinese wording, tone, and burden control.",
        "source": "gold_data/final_dg_all.json",
        "created_at": inventory["created_at"],
        "project_count": inventory["project_count"],
        "priority_rule": "Use these samples as tone and naturalness references only. Existing style_rules.md, rewrite_patterns.md, fixed templates, designer handoff constraints, Brief, Proposal, and explicit client requirements take priority when there is any conflict.",
        "opening_question_samples": samples.get("opening_questions", []),
        "soft_open_prompt_samples": samples.get("question_label:soft_open_prompt", []),
        "media_request_samples": {
            "image": samples.get("question_label:image_request", []),
            "video": samples.get("question_label:video_request", []),
        },
        "brand_exposure_samples": samples.get("question_label:brand_exposure", []),
        "shopping_task_samples": samples.get("question_label:shopping", []),
        "usage_task_samples": samples.get("question_label:usage", []),
        "why_or_feeling_samples": samples.get("question_label:why_or_feeling", []),
        "recommended_skill_updates": [
            "Prefer soft open prompts that invite sharing over command-like checklist wording.",
            "Keep examples optional and short; use final-DG samples to learn tone, not to copy exact questions.",
            "Treat image and video wording as burden-control wording unless the platform requires mandatory upload.",
            "Check whether brand-related wording appears only after suitable behavior/context modules.",
            "Record conflicts between historical wording samples and current style rules as eval notes instead of overriding current rules.",
        ],
    }


def markdown_table(counter_items: list[tuple[str, int]], headers: tuple[str, str]) -> list[str]:
    lines = [f"| {headers[0]} | {headers[1]} |", "|---|---:|"]
    for key, count in counter_items:
        safe_key = key.replace("|", "\\|")
        lines.append(f"| {safe_key} | {count} |")
    return lines


def build_markdown_report(inventory: dict[str, Any], input_path: Path) -> str:
    lines: list[str] = [
        "# Gold DG JSON Inventory",
        "",
        f"- Source: `{input_path.relative_to(ROOT)}`",
        f"- Created at: {inventory['created_at']}",
        f"- Projects: {inventory['project_count']}",
        f"- Modules: {inventory['total_modules']}",
        f"- Questions: {inventory['total_questions']}",
        f"- Avg modules / project: {inventory['avg_modules_per_project']}",
        f"- Avg questions / project: {inventory['avg_questions_per_project']}",
        f"- Empty projects: {inventory['empty_projects']}",
        f"- Empty modules: {inventory['empty_modules']}",
        f"- Projects with image request: {inventory['projects_with_image_request']}",
        f"- Projects with video request: {inventory['projects_with_video_request']}",
        "",
        "## Project Fields",
        "",
    ]
    lines.extend(markdown_table(inventory["project_keys"], ("Field", "Count")))
    lines.extend(["", "## Status", ""])
    lines.extend(markdown_table(inventory["status"], ("Status", "Projects")))
    lines.extend(["", "## Language", ""])
    lines.extend(markdown_table(inventory["language"], ("Language", "Projects")))
    lines.extend(["", "## Project Type", ""])
    lines.extend(markdown_table(inventory["project_type"], ("Project type", "Projects")))
    lines.extend(["", "## Question Types", ""])
    lines.extend(markdown_table(inventory["question_type"], ("Question type", "Questions")))
    lines.extend(["", "## Common Module Titles", ""])
    lines.extend(markdown_table(inventory["module_title"][:30], ("Module title", "Modules")))
    lines.extend(["", "## Common First Modules", ""])
    lines.extend(markdown_table(inventory["first_module_title"][:20], ("First module", "Projects")))
    lines.extend(["", "## Common Module Sequences", ""])
    lines.extend(markdown_table(inventory["module_sequence"][:20], ("Sequence", "Projects")))
    lines.extend(["", "## Detected Question Labels", ""])
    lines.extend(markdown_table(inventory["question_labels"], ("Label", "Questions")))

    samples = inventory["samples"]
    sample_sections = [
        ("Opening Questions", samples.get("opening_questions", [])),
        ("Soft Open Prompts", samples.get("question_label:soft_open_prompt", [])),
        ("Image Requests", samples.get("question_label:image_request", [])),
        ("Video Requests", samples.get("question_label:video_request", [])),
        ("Brand Exposure", samples.get("question_label:brand_exposure", [])),
        ("Shopping Tasks", samples.get("question_label:shopping", [])),
        ("Usage Tasks", samples.get("question_label:usage", [])),
        ("Why Or Feeling", samples.get("question_label:why_or_feeling", [])),
    ]
    for title, rows in sample_sections:
        lines.extend(["", f"## {title}", ""])
        if rows:
            lines.extend(f"- {row}" for row in rows)
        else:
            lines.append("- No samples detected.")

    lines.extend(
        [
            "",
            "## Recommended Next Uses",
            "",
            "- Feed `designer_patterns.json` into `dg-questionnaire-designer` as structure and research-logic evidence.",
            "- Feed `wording_patterns.json` into `dg-question-wording-editor` as respondent-facing wording evidence.",
            "- Keep `final_dg_all.json` read-only and regenerate these reports whenever the database export changes.",
            "- Add a later evaluator that compares generated DG drafts against these gold modules and question labels.",
        ]
    )
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description="Analyze one database-exported JSON file containing many final DG projects.")
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--out-dir", type=Path, default=OUT_DIR)
    args = parser.parse_args()

    input_path = args.input if args.input.is_absolute() else ROOT / args.input
    out_dir = args.out_dir if args.out_dir.is_absolute() else ROOT / args.out_dir
    data = read_json(input_path)
    if not isinstance(data, list):
        raise TypeError("Expected the top-level JSON value to be a list of projects.")

    projects = [item for item in data if isinstance(item, dict)]
    inventory = build_inventory(projects)
    designer_patterns = build_designer_patterns(inventory)
    wording_patterns = build_wording_patterns(inventory)

    out_dir.mkdir(parents=True, exist_ok=True)
    inventory_path = out_dir / "gold_data_inventory.md"
    designer_path = out_dir / "designer_patterns.json"
    wording_path = out_dir / "wording_patterns.json"

    inventory_path.write_text(build_markdown_report(inventory, input_path), encoding="utf-8-sig")
    designer_path.write_text(json.dumps(designer_patterns, ensure_ascii=False, indent=2), encoding="utf-8")
    wording_path.write_text(json.dumps(wording_patterns, ensure_ascii=False, indent=2), encoding="utf-8")

    print(inventory_path)
    print(designer_path)
    print(wording_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

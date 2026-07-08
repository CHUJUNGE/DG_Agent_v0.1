from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
VERSION_PATH = ROOT / "skill" / "dg-questionnaire-designer" / "VERSION.json"
PROMPT_TEST_DIR = ROOT / "tests" / "prompt_tests"
MODEL_TEST_DIR = ROOT / "tests" / "model_tests"
OUT_DIR = ROOT / "tests" / "loop_reports"


GAP_PATTERNS: dict[str, list[str]] = {
    "too_rigid_or_checklist": ["死板", "checklist", "表格", "命令", "机械"],
    "too_many_examples_or_parentheses": ["括号", "解释", "例子", "为了引导而引导"],
    "respondent_burden": ["负担", "太多", "过重", "必须上传", "至少", "最多", "打分"],
    "bad_question_wording": ["语气", "题面", "不自然", "random", "specific"],
    "missing_or_wrong_research_logic": ["模块", "逻辑", "研究问题", "目的"],
    "needs_engineering_or_data": ["数据库", "后端", "算法", "训练", "标答"],
}


RULE_TARGETS: dict[str, str] = {
    "too_rigid_or_checklist": "references/research_rules.md",
    "too_many_examples_or_parentheses": "references/research_rules.md",
    "respondent_burden": "references/research_rules.md + references/eval_rubric.md",
    "bad_question_wording": "references/research_rules.md",
    "missing_or_wrong_research_logic": "references/generation_logic.md",
    "needs_engineering_or_data": "docs/data_training_iteration.md",
}


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8-sig", errors="replace")


def load_versions() -> dict[str, str]:
    if not VERSION_PATH.exists():
        return {}
    return json.loads(read_text(VERSION_PATH))


def find_latest_review(case_id: str) -> Path:
    candidates = sorted(
        MODEL_TEST_DIR.glob(f"{case_id}_*_review*.md"),
        key=lambda path: path.stat().st_mtime,
        reverse=True,
    )
    if not candidates:
        candidates = sorted(
            MODEL_TEST_DIR.glob(f"{case_id}_*.md"),
            key=lambda path: path.stat().st_mtime,
            reverse=True,
        )
    if not candidates:
        raise FileNotFoundError(f"No model test or review file found for {case_id} in {MODEL_TEST_DIR}")
    return candidates[0]


def extract_prompt_preview(case_id: str) -> tuple[str, list[str]]:
    path = PROMPT_TEST_DIR / f"{case_id}_prompt_preview.md"
    if not path.exists():
        return "not_found", []

    text = read_text(path)
    selected_match = re.search(r"- Selected cases:\s*(.+)", text)
    selected_cases = selected_match.group(1).strip() if selected_match else "unknown"

    input_files = []
    for match in re.finditer(r"^\s+-\s+(.+?)\s+\((.+?),\s+\d+\s+chars\)", text, re.MULTILINE):
        input_files.append(f"{match.group(1)} ({match.group(2)})")

    return selected_cases, input_files


def detect_gaps(text: str) -> tuple[Counter[str], dict[str, list[str]]]:
    counts: Counter[str] = Counter()
    evidence: dict[str, list[str]] = {}
    lines = []
    for raw_line in text.splitlines():
        line = raw_line.strip()
        if not line:
            continue
        if line.startswith("#") or line.startswith("|") or line.startswith("---"):
            continue
        lines.append(line)

    for gap_type, patterns in GAP_PATTERNS.items():
        for line in lines:
            if any(pattern.lower() in line.lower() for pattern in patterns):
                counts[gap_type] += 1
                evidence.setdefault(gap_type, [])
                if len(evidence[gap_type]) < 3:
                    evidence[gap_type].append(line[:220])

    return counts, evidence


def build_rule_candidates(counts: Counter[str], evidence: dict[str, list[str]]) -> list[str]:
    candidates: list[str] = []
    for gap_type, count in counts.most_common():
        target = RULE_TARGETS.get(gap_type, "references/research_rules.md")
        sample = evidence.get(gap_type, [""])[0]
        candidates.append(
            f"- `{gap_type}` ({count} hit): update `{target}`. Evidence: {sample}"
        )
    return candidates


def build_report(case_id: str, review_path: Path) -> str:
    versions = load_versions()
    selected_cases, input_files = extract_prompt_preview(case_id)
    review_text = read_text(review_path)
    counts, evidence = detect_gaps(review_text)
    rule_candidates = build_rule_candidates(counts, evidence)

    created_at = datetime.now(timezone.utc).isoformat()
    lines: list[str] = [
        f"# Demo Closed Loop Report - {case_id}",
        "",
        "## 1. Run Metadata",
        "",
        f"- Created at: {created_at}",
        f"- Review source: `{review_path.relative_to(ROOT)}`",
        f"- Selected case cards: {selected_cases}",
        f"- Input files: {', '.join(input_files) if input_files else 'not available in prompt preview'}",
        "",
        "## 2. Version Baseline",
        "",
    ]

    if versions:
        for key in [
            "skill_version",
            "generation_logic_version",
            "research_rules_version",
            "case_library_version",
            "fixed_template_version",
            "eval_rubric_version",
            "data_contracts_version",
            "status",
        ]:
            if key in versions:
                lines.append(f"- {key}: {versions[key]}")
    else:
        lines.append("- Version file not found.")

    lines.extend(
        [
            "",
            "## 3. Detected Review Gaps",
            "",
        ]
    )

    if counts:
        for gap_type, count in counts.most_common():
            lines.append(f"### {gap_type}")
            lines.append("")
            lines.append(f"- Hits: {count}")
            for item in evidence.get(gap_type, []):
                lines.append(f"- Evidence: {item}")
            lines.append("")
    else:
        lines.append("- No keyword-based gaps detected. Add manual annotations before promoting rules.")
        lines.append("")

    lines.extend(
        [
            "## 4. Rule / Skill Update Candidates",
            "",
        ]
    )
    lines.extend(rule_candidates or ["- No automatic rule candidate. Keep this run as eval evidence only."])

    lines.extend(
        [
            "",
            "## 5. Current Demo Loop",
            "",
            "1. Build prompt from project files, rules, generation logic, and selected case cards.",
            "2. Generate the DG draft with an OpenAI-compatible model.",
            "3. Record researcher review or model-review notes under `tests/model_tests/`.",
            "4. Build this loop report to classify gaps and propose rule / rubric / training updates.",
            "5. Promote only stable, reusable findings into skill references; keep one-off project details out of the skill.",
            "",
            "## 6. Not Solvable Inside This Local Demo",
            "",
            "- Company database connection: requires production credentials, project permissions, schema access, and data governance.",
            "- Company backend integration: requires API contracts, auth, file storage, job orchestration, and deployment environment.",
            "- Algorithm service integration: requires embedding/reranker/evaluator services and model registry access.",
            "- Gold-answer evaluation at scale: requires historical input materials paired with final DG gold answers from the database.",
            "- Model training or fine-tuning: requires curated training/eval datasets, approved training pipeline, model versioning, and regression gates.",
            "- Production monitoring: requires logs, user feedback capture, quality dashboards, and rollback/version controls.",
            "",
            "## 7. Production Loop Required Next",
            "",
            "Database historical inputs + final DG gold answers -> batch generation -> auto evaluation -> gap clustering -> skill/rule candidates + training samples -> regression gate -> new model/skill release.",
        ]
    )

    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description="Build a local demo closed-loop report from model review files.")
    parser.add_argument("--case", default="case_001", help="Case id, for example case_005 or 005.")
    parser.add_argument("--review-file", type=Path, help="Optional explicit review/model-output markdown file.")
    args = parser.parse_args()

    normalized_arg = args.case.strip().lower()
    case_id = normalized_arg if normalized_arg.startswith("case_") else f"case_{normalized_arg}"
    review_path = args.review_file or find_latest_review(case_id)
    if not review_path.is_absolute():
        review_path = ROOT / review_path
    if not review_path.exists():
        raise FileNotFoundError(review_path)

    report = build_report(case_id, review_path)
    OUT_DIR.mkdir(exist_ok=True)
    out_path = OUT_DIR / f"{case_id}_closed_loop_report.md"
    out_path.write_text(report, encoding="utf-8-sig")
    print(out_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

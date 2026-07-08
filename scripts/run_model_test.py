from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from prompt import ProjectInfo, build_generation_prompt
from test_prompt_with_cases import load_case_inputs


OUT_DIR = ROOT / "tests" / "model_tests"


def call_chatanywhere(messages: list[dict[str, str]], model: str) -> str:
    api_key = os.environ.get("CHATANYWHERE_API_KEY")
    if not api_key:
        raise RuntimeError("Missing CHATANYWHERE_API_KEY environment variable.")

    base_url = os.environ.get("CHATANYWHERE_BASE_URL", "https://api.chatanywhere.tech/v1").rstrip("/")
    url = f"{base_url}/chat/completions"

    payload = {
        "model": model,
        "messages": messages,
        "temperature": 0.2,
    }

    request = urllib.request.Request(
        url=url,
        data=json.dumps(payload, ensure_ascii=False).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        method="POST",
    )

    try:
        with urllib.request.urlopen(request, timeout=180) as response:
            raw = response.read().decode("utf-8")
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"ChatAnywhere HTTP {exc.code}: {body}") from exc

    data = json.loads(raw)
    try:
        return data["choices"][0]["message"]["content"]
    except (KeyError, IndexError, TypeError) as exc:
        raise RuntimeError(f"Unexpected response shape: {raw[:2000]}") from exc


def project_info_for_case(case_id: str) -> ProjectInfo:
    if case_id == "case_001":
        return ProjectInfo(
            category="口香糖",
            brand="益达 / 绿箭",
            target_audience="18-40 Urban Striver",
            extra_notes="请基于 Case_001 的输入材料生成题目设计；不要参考 Final Digital Diary DG。",
        )
    if case_id == "case_002":
        return ProjectInfo(
            category="巧克力 / 零食",
            brand="德芙 / Mars",
            target_audience="巧克力目标消费者",
            extra_notes="请基于 Case_002 的输入材料生成题目设计；不要参考 Final Digital Diary DG。",
        )
    raise ValueError(f"Unsupported case id: {case_id}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--case", default="case_001", choices=["case_001", "case_002"])
    parser.add_argument("--model", default=os.environ.get("CHATANYWHERE_MODEL", "gpt-5-mini"))
    args = parser.parse_args()

    case_root = Path(os.environ.get("DG_AGENT_CASE_ROOT", ROOT / "case_data"))
    case_dir = case_root / f"Case_{args.case[-3:]}"
    files = load_case_inputs(case_dir)
    bundle = build_generation_prompt(project_info=project_info_for_case(args.case), files=files)

    print(f"Calling model: {args.model}")
    print(f"Selected cases: {', '.join(bundle.selected_case_ids) or 'none'}")
    print(f"Input files: {len(files)}")

    content = call_chatanywhere(bundle.to_openai_messages(), args.model)

    OUT_DIR.mkdir(exist_ok=True)
    out_path = OUT_DIR / f"{args.case}_{args.model}_output.md"
    out_path.write_text(content, encoding="utf-8-sig")
    print(f"Saved: {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

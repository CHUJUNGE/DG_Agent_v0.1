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

from prompt import build_generation_prompt
from test_prompt_with_cases import case_dir_for_id, load_case_inputs, normalize_case_id, project_info_for_case


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


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--case", default="case_001", help="Case id, for example case_005 or 005.")
    parser.add_argument("--case-root", default=os.environ.get("DG_AGENT_CASE_ROOT", str(ROOT / "case_data")))
    parser.add_argument("--model", default=os.environ.get("CHATANYWHERE_MODEL", "claude-opus-4-6"))
    args = parser.parse_args()

    case_id = normalize_case_id(args.case)
    case_root = Path(args.case_root)
    case_dir = case_dir_for_id(case_root, case_id)
    files = load_case_inputs(case_dir)
    bundle = build_generation_prompt(project_info=project_info_for_case(case_id, case_dir), files=files)

    print(f"Calling model: {args.model}")
    print(f"Case: {case_id}")
    print(f"Case folder: {case_dir}")
    print(f"Selected cases: {', '.join(bundle.selected_case_ids) or 'none'}")
    print(f"Input files: {len(files)}")

    content = call_chatanywhere(bundle.to_openai_messages(), args.model)

    OUT_DIR.mkdir(exist_ok=True)
    out_path = OUT_DIR / f"{case_id}_{args.model}_output.md"
    out_path.write_text(content, encoding="utf-8-sig")
    print(f"Saved: {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

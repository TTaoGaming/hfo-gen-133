"""
dispatch_research.py -- CLI wrapper so Olrun can dispatch cross-substrate
research (Gemini / OpenAI / Claude / local Ollama) programmatically instead
of pasting into ChatGPT/Gemini Deep Research UIs.

Composes: GPT Researcher (research-loop framework, OSS/MIT) + LiteLLM proxy
(model routing, already running on this host) + a web-search API (Tavily/
Serper/Brave -- whichever key is present).

Usage:
    python tools/dispatch_research.py --query "..." --model ollama-local \
        --report-type research_report --out resources/research/out.md

    --model ollama-local  -> openai:huginn via the 4001 proxy (CONFIRMED LIVE)
    --model gemini        -> gemini/gemini-2.5-flash via a keyed proxy
                              (BLOCKED on this host -- see receipt, Windows
                              aiohttp/aiodns DNS resolution bug)
    --model openai         -> requires OPENAI_API_KEY (NOT present in
                              sigrun-secrets as of 2026-08-01, will error)
    --model claude          -> requires ANTHROPIC_API_KEY (NOT present as a
                              standalone API key; Claude Code session auth
                              is not usable here, will error)

Every dispatch appends one row to state/ssot/research_dispatches.jsonl --
this is the caller's receipt, not a chain-sealed row (sealing is operator-only).
"""
import argparse
import asyncio
import json
import time
import traceback
from datetime import datetime, timezone
from pathlib import Path

FORGE = Path(__file__).resolve().parents[1]
DISPATCH_LOG = FORGE / "state" / "ssot" / "research_dispatches.jsonl"

MODEL_ROUTES = {
    "ollama-local": {
        "OPENAI_BASE_URL": "http://127.0.0.1:4001",
        "OPENAI_API_KEY": "local-only-no-external-access",
        "FAST_LLM": "openai:huginn",
        "SMART_LLM": "openai:huginn",
        "STRATEGIC_LLM": "openai:huginn",
    },
    "gemini": {
        "OPENAI_BASE_URL": "http://127.0.0.1:4002",
        "OPENAI_API_KEY": "local-only-no-external-access",
        "FAST_LLM": "openai:nidhoggr-gemini-flash",
        "SMART_LLM": "openai:nidhoggr-gemini-pro",
        "STRATEGIC_LLM": "openai:nidhoggr-gemini-pro",
    },
    "openai": {
        "OPENAI_BASE_URL": "http://127.0.0.1:4001",
        "OPENAI_API_KEY": "local-only-no-external-access",
        "FAST_LLM": "openai:gpt-4o-mini",
        "SMART_LLM": "openai:gpt-4o",
        "STRATEGIC_LLM": "openai:gpt-4o",
    },
    "claude": {
        "OPENAI_BASE_URL": "http://127.0.0.1:4001",
        "OPENAI_API_KEY": "local-only-no-external-access",
        "FAST_LLM": "openai:claude-haiku",
        "SMART_LLM": "openai:claude-sonnet",
        "STRATEGIC_LLM": "openai:claude-sonnet",
    },
}


def append_dispatch_row(row: dict) -> None:
    DISPATCH_LOG.parent.mkdir(parents=True, exist_ok=True)
    with DISPATCH_LOG.open("a", encoding="utf-8", newline="\n") as f:
        f.write(json.dumps(row, sort_keys=True, separators=(",", ":")) + "\n")


async def run(query: str, model: str, report_type: str, out_path: Path) -> dict:
    import os

    if model not in MODEL_ROUTES:
        raise SystemExit(f"unknown --model {model!r}, choices: {list(MODEL_ROUTES)}")
    os.environ.update(MODEL_ROUTES[model])
    os.environ.setdefault("RETRIEVER", "tavily")

    from gpt_researcher import GPTResearcher

    t0 = time.time()
    researcher = GPTResearcher(query=query, report_type=report_type)
    result = {
        "query": query,
        "model": model,
        "report_type": report_type,
        "ts_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
    }
    try:
        await researcher.conduct_research()
        report = await researcher.write_report()
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(report, encoding="utf-8")
        result.update(
            status="SUCCESS",
            elapsed_s=round(time.time() - t0, 1),
            out_path=str(out_path),
            report_chars=len(report),
        )
    except Exception as e:
        result.update(
            status="FAIL",
            elapsed_s=round(time.time() - t0, 1),
            error=f"{type(e).__name__}: {e}",
            traceback=traceback.format_exc()[-4000:],
        )
    return result


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--query", required=True)
    ap.add_argument("--model", default="ollama-local", choices=list(MODEL_ROUTES))
    ap.add_argument("--report-type", default="research_report")
    ap.add_argument("--out", default=None, help="output markdown path")
    args = ap.parse_args()

    out_path = Path(args.out) if args.out else FORGE / "resources" / "research" / "dispatch_output.md"
    result = asyncio.run(run(args.query, args.model, args.report_type, out_path))
    append_dispatch_row(result)
    print(json.dumps(result, indent=2)[:2000])
    if result["status"] != "SUCCESS":
        raise SystemExit(1)


if __name__ == "__main__":
    main()

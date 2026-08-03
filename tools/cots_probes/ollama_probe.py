#!/usr/bin/env python3
"""Behavioral probe: direct HTTP call to Ollama's /api/generate.

Deliberately bypasses litellm entirely -- this probe must fail independently
of litellm_probe.py, so it uses a raw requests.post against the Ollama HTTP
API and asserts on the actual completion text in the JSON response.
"""
import sys

import requests

OLLAMA_BASE = "http://127.0.0.1:11434"


def main() -> int:
    r = requests.post(
        f"{OLLAMA_BASE}/api/generate",
        json={
            "model": "llama3.2:3b",
            "prompt": "What is 2+2? Answer with just the number.",
            "stream": False,
        },
        timeout=60,
    )
    r.raise_for_status()
    data = r.json()
    print(f"RAW_JSON_KEYS: {sorted(data.keys())}")

    has_error = bool(data.get("error"))
    completion = (data.get("response") or "").strip()
    print(f"RAW_RESPONSE: {completion!r}")
    print(f"HAS_ERROR_FIELD={has_error}")

    ok = (not has_error) and len(completion) > 0
    print(f"PROBE_PASS={ok}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())

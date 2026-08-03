#!/usr/bin/env python3
"""Behavioral probe: litellm.completion against local Ollama. Not a mock.

Invokes the real litellm completion API against the locally-running Ollama
server and asserts on the actual response TEXT content -- not merely that
the call returns without raising.
"""
import sys

import litellm


def main() -> int:
    r = litellm.completion(
        model="ollama/llama3.2:3b",
        api_base="http://127.0.0.1:11434",
        messages=[{"role": "user", "content": "What is 2+2? Answer with just the number."}],
    )
    content = r.choices[0].message.content or ""
    print(f"RAW_RESPONSE: {content!r}")
    ok = "4" in content
    print(f"PROBE_PASS={ok}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())

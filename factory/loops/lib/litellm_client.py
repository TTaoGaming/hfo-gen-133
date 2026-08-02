"""Tiny LiteLLM proxy client used by every loop that needs an LLM call.

Contract per HFO convention: loops NEVER direct-call OpenAI/Anthropic keys.
Every prompt goes through the LiteLLM proxy at LITELLM_PROXY_URL. The proxy
handles key rotation, budget caps, and per-model routing.

If LITELLM_PROXY_URL is not set, this module returns a deterministic
DRY_RUN response so operator can smoke-test runners without spend.

Env vars
--------
LITELLM_PROXY_URL     e.g. http://localhost:4000
LITELLM_API_KEY       optional bearer token for the proxy (never per-vendor)
LITELLM_DEFAULT_MODEL fallback if caller does not pass model=
"""

from __future__ import annotations

import json
import os
import time
import urllib.error
import urllib.request
from dataclasses import dataclass

try:
    from .slack_escalate import _autoload_dotenv
except ImportError:  # running as a bare script
    import sys as _sys
    from pathlib import Path as _Path
    _sys.path.insert(0, str(_Path(__file__).resolve().parent))
    from slack_escalate import _autoload_dotenv  # type: ignore


@dataclass
class LLMResult:
    ok: bool
    text: str
    model: str
    tokens_in: int | None
    tokens_out: int | None
    dry_run: bool
    error: str | None = None


def _endpoint() -> str | None:
    _autoload_dotenv()
    return os.environ.get("LITELLM_PROXY_URL")


def _model(explicit: str | None) -> str:
    return explicit or os.environ.get("LITELLM_DEFAULT_MODEL") or "gpt-4o-mini"


def _headers() -> dict:
    _autoload_dotenv()
    key = os.environ.get("LITELLM_API_KEY")
    h = {"Content-Type": "application/json"}
    if key:
        h["Authorization"] = f"Bearer {key}"
    return h


def _dry_run_response(prompt: str, model: str) -> LLMResult:
    stub = (
        f"[DRY_RUN model={model}] {prompt.strip()[:200]}"
        f"\n\n(No LITELLM_PROXY_URL configured — runner returned a stub.)"
    )
    return LLMResult(
        ok=True,
        text=stub,
        model=model,
        tokens_in=None,
        tokens_out=None,
        dry_run=True,
    )


def complete(
    prompt: str,
    model: str | None = None,
    system: str | None = None,
    max_tokens: int = 1024,
    temperature: float = 0.4,
    timeout: float = 60.0,
    retries: int = 2,
) -> LLMResult:
    """Send a single-shot completion via the LiteLLM proxy /v1/chat/completions."""
    endpoint = _endpoint()
    model_name = _model(model)
    if not endpoint:
        return _dry_run_response(prompt, model_name)

    messages = []
    if system:
        messages.append({"role": "system", "content": system})
    messages.append({"role": "user", "content": prompt})
    body = json.dumps(
        {
            "model": model_name,
            "messages": messages,
            "max_tokens": max_tokens,
            "temperature": temperature,
        }
    ).encode("utf-8")

    url = endpoint.rstrip("/") + "/v1/chat/completions"
    last_err = None
    for attempt in range(retries + 1):
        try:
            req = urllib.request.Request(url, data=body, headers=_headers(), method="POST")
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                data = json.loads(resp.read().decode("utf-8"))
                text = data["choices"][0]["message"]["content"]
                usage = data.get("usage", {}) or {}
                return LLMResult(
                    ok=True,
                    text=text,
                    model=data.get("model", model_name),
                    tokens_in=usage.get("prompt_tokens"),
                    tokens_out=usage.get("completion_tokens"),
                    dry_run=False,
                )
        except urllib.error.HTTPError as e:
            last_err = f"HTTP {e.code}: {e.reason}"
        except (urllib.error.URLError, TimeoutError, OSError) as e:
            last_err = str(e)
        time.sleep(min(30, 2 ** attempt))

    return LLMResult(
        ok=False,
        text="",
        model=model_name,
        tokens_in=None,
        tokens_out=None,
        dry_run=False,
        error=last_err,
    )


if __name__ == "__main__":  # pragma: no cover
    r = complete("Say hello in 5 words.", model="gpt-4o-mini")
    print(json.dumps({"ok": r.ok, "dry_run": r.dry_run, "text": r.text[:200], "err": r.error}))

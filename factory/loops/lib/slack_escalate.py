"""Post hot-reply pings + halt notices to Slack from any loop.

Reads SLACK_WEBHOOK_URL from the process env or from the repo-root .env
(does NOT read from CLI args — the URL contains a secret token).

Modeled on tools/slack_post.py so behavior is identical. This module adds:
- .env autoload so operator can run runners under a bare PowerShell
- an escalate(loop, action, detail, severity) convenience that formats
  a consistent HFO pattern for chain-row audit
"""

from __future__ import annotations

import json
import os
import sys
import urllib.error
import urllib.request
from pathlib import Path

FORGE_ROOT = Path(__file__).resolve().parents[3]
DOTENV = FORGE_ROOT / ".env"


def _autoload_dotenv() -> None:
    if not DOTENV.exists():
        return
    for raw in DOTENV.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        if "=" not in line:
            continue
        k, v = line.split("=", 1)
        k = k.strip()
        v = v.strip().strip("'\"")
        os.environ.setdefault(k, v)


def get_webhook_url() -> str | None:
    _autoload_dotenv()
    url = os.environ.get("SLACK_WEBHOOK_URL") or os.environ.get("SLACK_INCOMING_WEBHOOK")
    if not url or "{{" in url:
        return None
    return url


def post(text: str) -> tuple[bool, int | str | None]:
    url = get_webhook_url()
    if not url:
        return False, "no_webhook_configured"
    body = json.dumps({"text": text}).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=body,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            return True, resp.status
    except urllib.error.HTTPError as e:
        return False, e.code
    except (urllib.error.URLError, TimeoutError, OSError) as e:
        return False, str(e)


SEVERITY_EMOJI = {
    "info": ":information_source:",
    "hot_reply": ":fire:",
    "warn": ":warning:",
    "halt": ":octagonal_sign:",
}


def escalate(loop: str, action: str, detail: str, severity: str = "info") -> tuple[bool, int | str | None]:
    """Post a formatted HFO ping. Returns (posted?, status_or_reason)."""
    emoji = SEVERITY_EMOJI.get(severity, ":bell:")
    text = f"{emoji} `{loop}` — *{action}*\n{detail}"
    return post(text)


if __name__ == "__main__":  # pragma: no cover
    if len(sys.argv) > 1:
        text = " ".join(sys.argv[1:])
    else:
        text = "test from factory.loops.lib.slack_escalate"
    ok, status = post(text)
    print(json.dumps({"posted": ok, "status": status}))

#!/usr/bin/env python3
"""INSTANTLY-COLD-EMAIL-STAGER (EMERGENCY_FORGE 2026-08-03, worker D, HOT-D3).

Stages a cold-email draft in the JSON shape Instantly's campaign/lead API
expects (POST /api/v2/leads -- campaign + lead[] with personalization
fields). Checks .env for INSTANTLY_API_KEY; as of 2026-08-02 that key does
NOT exist in this forge's .env (only SLACK_WEBHOOK_URL is present, and it is
itself a placeholder). Without a real key this tool CANNOT send and does not
try -- it stages to outputs/staged_sends/email_drafts/ and marks
status=staged_no_key.

CLASS ENVELOPE: STAGE only. SEND is a STOP -- operator signs in the morning
queue. This tool makes no network call, ever.

    python tools/olrun/skills/instantly_email.py \
        --draft --to=probe-target@example.com --template=spatial_pilot_v1

Prints exactly one JSON object on stdout. clock_source=host_read.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DRAFTS_DIR = ROOT / "outputs" / "staged_sends" / "email_drafts"
ENV_PATH = ROOT / ".env"
PORTFOLIO_URL = "https://hfo-games.pages.dev"


def now_str() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def rel(p: Path) -> str:
    return str(p.relative_to(ROOT)).replace("\\", "/")


def has_real_instantly_key() -> bool:
    """True only if INSTANTLY_API_KEY is present in .env with a non-placeholder value."""
    if not ENV_PATH.exists():
        return False
    text = ENV_PATH.read_text(encoding="utf-8", errors="ignore")
    for line in text.splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if line.startswith("INSTANTLY_API_KEY"):
            _, _, val = line.partition("=")
            val = val.strip().strip('"').strip("'")
            if val and "{{" not in val and val.upper() != "NONE":
                return True
            return False
    return False


def build_body(to: str, template: str) -> tuple[str, str]:
    """Returns (subject, body) -- a real, specific cold email, not lorem ipsum."""
    if template == "spatial_pilot_v1":
        subject = "60-second test: browser game that reads your hand, no controller"
        body = (
            "Hi,\n\n"
            "I build small browser games that run on webcam hand-tracking instead of "
            "a mouse, keyboard, or gamepad -- point at a laptop camera and the hand "
            "itself is the input. Everything runs client-side, no install, no account, "
            "no data leaves the browser tab.\n\n"
            f"Live portfolio of playable builds: {PORTFOLIO_URL}\n\n"
            "I'm looking for 5-10 people willing to try one build for about a minute "
            "and tell me honestly whether the gesture recognition felt responsive or "
            "laggy on their hardware. No signup form, no pitch deck, just a link and "
            "a minute of your time -- I want the failure cases more than the praise.\n\n"
            "Would you be open to a quick look this week?\n\n"
            "Thanks,\nTommy / HFO"
        )
    else:
        subject = f"Quick look at a live browser-game portfolio ({template})"
        body = (
            f"Hi,\n\nSharing a small, self-contained browser game portfolio built for "
            f"quick play-testing: {PORTFOLIO_URL}. Each title is a single static page, "
            f"no install and no account required. If you have a minute, I'd value a "
            f"gut reaction to whichever one grabs you first -- what felt good, what "
            f"felt off. Not a sales pitch, just looking for honest signal before "
            f"investing more build time.\n\nThanks,\nTommy / HFO"
        )
    return subject, body


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--draft", action="store_true", help="stage a draft (this tool never sends)")
    ap.add_argument("--to", required=True)
    ap.add_argument("--template", required=True)
    args = ap.parse_args()

    has_key = has_real_instantly_key()
    status = "staged_with_key_not_sent" if has_key else "staged_no_key"
    subject, body = build_body(args.to, args.template)
    ts = datetime.now(timezone.utc)
    ts_str = ts.strftime("%Y-%m-%dT%H:%M:%SZ")

    safe_to = re.sub(r"[^a-zA-Z0-9_.-]+", "_", args.to)
    DRAFTS_DIR.mkdir(parents=True, exist_ok=True)
    draft_path = DRAFTS_DIR / f"{ts.strftime('%Y%m%dT%H%M%SZ')}_{safe_to}_{args.template}.json"

    # Shape approximates Instantly v2 "add leads to campaign" payload:
    # POST /api/v2/leads  {campaign, leads:[{email, personalization,...}]}
    instantly_shape = {
        "campaign": args.template,
        "leads": [
            {
                "email": args.to,
                "personalization": body,
                "custom_variables": {"subject": subject, "portfolio_url": PORTFOLIO_URL},
            }
        ],
        "skip_if_in_workspace": True,
        "subject": subject,
        "body": body,
        "status": status,
        "note": (
            "STAGED ONLY. INSTANTLY_API_KEY not found in .env as of this run -- "
            "see .env comment block; only SLACK_WEBHOOK_URL exists there and it is "
            "itself an unfilled placeholder. This tool never sends regardless of "
            "key presence -- SEND requires explicit operator sign-off."
            if not has_key
            else "STAGED ONLY. API key present in .env but this tool never sends -- "
            "SEND requires explicit operator sign-off in the morning queue."
        ),
        "ts_utc": ts_str,
    }
    draft_path.write_text(json.dumps(instantly_shape, indent=2), encoding="utf-8")

    payload = {
        "campaign": args.template,
        "to": args.to,
        "subject": subject,
        "body": body,
        "draft_path": rel(draft_path),
        "status": status,
        "has_instantly_api_key": has_key,
        "ts_utc": ts_str,
    }
    print(json.dumps(payload))
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""COLD-EMAIL REPLY TRIAGE (per Sigrún envelope ENV_COLD_EMAIL_001 §D.operator_touch).

Categorizes each reply into one of:
  price_or_date_named   -> escalate to operator via Slack #hfo-synthesis webhook
  question_answered     -> draft candidate reply into state/outreach/reply_drafts/
  negative              -> log + append to suppression (soft; do not re-contact)
  unsubscribe           -> auto-honor + append to suppression (hard)
  bounce                -> mark bad; remove from Instantly campaign
  other                 -> log; leave for operator review

Data source: Instantly `/api/v2/emails/replies` (poll every 30 min via
cron/scheduled task). Falls back to reading a stdin JSON payload for tests.

Usage:
  python tools/outreach/reply_triage.py --poll                 # live
  python tools/outreach/reply_triage.py --test-payloads        # runs synthetic tests
  echo '{...}' | python tools/outreach/reply_triage.py --stdin # single reply
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DRAFTS_DIR = ROOT / "state" / "outreach" / "reply_drafts"
SUPPRESSION_PATH = ROOT / "state" / "outreach" / "suppression.txt"
TRIAGE_LOG = ROOT / "state" / "outreach" / "reply_triage.jsonl"
ENV_PATH = ROOT / ".env"
INSTANTLY_BASE = "https://api.instantly.ai/api/v2"

# Regex patterns for categorization — deliberately conservative; miss > false-positive.
PRICE_RE = re.compile(r"\$\s?\d[\d,]*(?:\.\d{2})?|\b(\d[\d,]*)\s?(?:usd|dollars?|k)\b", re.I)
DATE_RE = re.compile(
    r"\b(?:mon|tue|wed|thu|fri|sat|sun)(?:day)?\b|"
    r"\b(?:jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)(?:uary|ruary|ch|il|e|y|ust|tember|ober|ember)?\s+\d{1,2}\b|"
    r"\bnext week\b|\bthis week\b|\btomorrow\b|\bmorning\b|\bafternoon\b|\d{1,2}:\d{2}\s?(am|pm)\b|"
    r"\b(?:calendar|calendly|cal\.com|book a time|schedule)\b",
    re.I,
)
NEG_RE = re.compile(r"\bnot interested\b|\bstop\b|\bremove me\b|\bplease do not\b|\bf\*+ off\b|\bfuck off\b|\bspam\b", re.I)
UNSUB_RE = re.compile(r"\bunsubscribe\b|\bopt.?out\b|\bremove.*(list|contact)\b", re.I)
BOUNCE_RE = re.compile(r"\b(mailer-daemon|postmaster|delivery status notification|undeliverable|550 5\.\d)\b", re.I)
QUESTION_RE = re.compile(r"\?")


def load_env() -> dict[str, str]:
    env: dict[str, str] = {}
    if not ENV_PATH.exists():
        return env
    for line in ENV_PATH.read_text(encoding="utf-8", errors="ignore").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, _, v = line.partition("=")
        v = v.strip().strip('"').strip("'")
        if v and "{{" not in v:
            env[k.strip()] = v
    return env


def categorize(reply: dict) -> str:
    """Reply schema: {from_email, subject, body, message_id, in_reply_to, received_utc}."""
    text = " ".join(str(reply.get(k, "")) for k in ("subject", "body")).lower()
    if BOUNCE_RE.search(text):
        return "bounce"
    if UNSUB_RE.search(text):
        return "unsubscribe"
    if NEG_RE.search(text):
        return "negative"
    if PRICE_RE.search(text) or DATE_RE.search(text):
        return "price_or_date_named"
    if QUESTION_RE.search(text):
        return "question_answered"
    return "other"


def append_suppression(email: str, reason: str) -> None:
    SUPPRESSION_PATH.parent.mkdir(parents=True, exist_ok=True)
    with SUPPRESSION_PATH.open("a", encoding="utf-8") as fh:
        fh.write(f"{email.lower()}  # {reason} @ {dt.datetime.now(dt.timezone.utc).isoformat()}\n")


def log_triage(record: dict) -> None:
    TRIAGE_LOG.parent.mkdir(parents=True, exist_ok=True)
    with TRIAGE_LOG.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(record) + "\n")


def slack_notify(webhook_url: str, message: str) -> int:
    payload = {"text": message}
    req = urllib.request.Request(
        webhook_url,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=8) as resp:
            return resp.status
    except urllib.error.HTTPError as e:
        return e.code
    except Exception:
        return 0


def draft_reply_candidate(reply: dict, env: dict) -> Path:
    DRAFTS_DIR.mkdir(parents=True, exist_ok=True)
    fname = re.sub(r"[^a-zA-Z0-9]+", "_", reply.get("from_email", "unknown"))
    ts = dt.datetime.now(dt.timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    path = DRAFTS_DIR / f"{ts}_{fname}.md"
    body = (
        f"# Reply-draft candidate (STAGED — operator must send)\n\n"
        f"- from: {reply.get('from_email')}\n"
        f"- their subject: {reply.get('subject')}\n"
        f"- their body:\n\n> {reply.get('body','').strip()[:1000]}\n\n"
        f"## Suggested reply\n\n"
        f"Thanks for the reply. Short answer: I do a fixed $350 diagnostic that maps\n"
        f"the failure, shows you the fix in writing, and you keep the write-up whether\n"
        f"we work together after or not. If it's a fit I can point at a scoped 1–2 week\n"
        f"sprint at $1.5–3k; if not I'll say so.\n\n"
        f"Worth 20 minutes? {env.get('BOOKING_LINK', '{{BOOKING_LINK}}')}\n\n"
        f"— {env.get('SENDER_NAME', '{{SENDER_NAME}}')}\n\n"
        f"---\n"
        f"⚠️ operator: review, edit if needed, send from your Instantly inbox thread.\n"
    )
    path.write_text(body, encoding="utf-8")
    return path


def handle(reply: dict, env: dict) -> dict:
    category = categorize(reply)
    from_email = reply.get("from_email", "")
    record: dict = {
        "ts": dt.datetime.now(dt.timezone.utc).isoformat(),
        "from_email": from_email,
        "category": category,
        "message_id": reply.get("message_id"),
    }
    if category in ("unsubscribe", "bounce"):
        append_suppression(from_email, category)
        record["action"] = "suppressed"
    elif category == "negative":
        append_suppression(from_email, "negative_reply")
        record["action"] = "suppressed_soft"
    elif category == "price_or_date_named":
        hook = env.get("SLACK_WEBHOOK_URL")
        if hook:
            status = slack_notify(
                hook,
                f":inbox_tray: cold-email reply from *{from_email}* — price or date named. "
                f"Subject: _{reply.get('subject','')}_\n"
                f"```\n{reply.get('body','').strip()[:800]}\n```",
            )
            record["slack_notify_status"] = status
            record["action"] = "escalated_slack"
        else:
            record["action"] = "would_escalate_no_slack_webhook"
    elif category == "question_answered":
        draft_path = draft_reply_candidate(reply, env)
        record["action"] = "reply_draft_staged"
        record["draft_path"] = str(draft_path.relative_to(ROOT))
    else:
        record["action"] = "logged_only"
    log_triage(record)
    return record


def poll_instantly(env: dict, since_iso: str | None) -> list[dict]:
    api_key = env.get("INSTANTLY_API_KEY")
    campaign_id = env.get("INSTANTLY_CAMPAIGN_ID")
    if not (api_key and campaign_id):
        return []
    params = f"?campaign_id={campaign_id}"
    if since_iso:
        params += f"&since={since_iso}"
    req = urllib.request.Request(
        f"{INSTANTLY_BASE}/emails/replies{params}",
        headers={"Authorization": f"Bearer {api_key}"},
    )
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            return data.get("replies", [])
    except Exception as e:
        print(f"poll error: {e}", file=sys.stderr)
        return []


def synthetic_test_payloads() -> list[tuple[dict, str]]:
    """(reply, expected_category)."""
    return [
        (
            {"from_email": "founder@example.com", "subject": "Re: Fix AI workflow", "body": "Yes send a quote, what's your rate for a 2-week engagement? $2000 range?"},
            "price_or_date_named",
        ),
        (
            {"from_email": "founder2@example.com", "subject": "Re: Fix AI workflow", "body": "How does the diagnostic differ from a paid audit? Timeline?"},
            "question_answered",
        ),
        (
            {"from_email": "grumpy@example.com", "subject": "Re: Fix AI workflow", "body": "Not interested, please stop emailing."},
            "negative",
        ),
        (
            {"from_email": "clean@example.com", "subject": "Re: Fix AI workflow", "body": "Please unsubscribe me from your list."},
            "unsubscribe",
        ),
        (
            {"from_email": "mailer-daemon@example.com", "subject": "Undeliverable: Fix AI workflow", "body": "Delivery Status Notification (Failure). 550 5.1.1 The email account does not exist."},
            "bounce",
        ),
        (
            {"from_email": "curious@example.com", "subject": "Re: Fix AI workflow", "body": "Interesting — I'll take a look."},
            "other",
        ),
        (
            {"from_email": "book@example.com", "subject": "Re: Fix AI workflow", "body": "Sure, calendar-wise Thursday morning works — send a Cal.com link."},
            "price_or_date_named",
        ),
    ]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--poll", action="store_true")
    ap.add_argument("--stdin", action="store_true")
    ap.add_argument("--test-payloads", action="store_true")
    ap.add_argument("--since", default=None)
    args = ap.parse_args()

    env = load_env()

    if args.test_payloads:
        passed = failed = 0
        for reply, expected in synthetic_test_payloads():
            got = categorize(reply)
            ok = got == expected
            if ok:
                passed += 1
            else:
                failed += 1
                print(f"FAIL: expected={expected} got={got} reply={reply['body'][:80]}")
        print(json.dumps({"test": "reply_triage", "passed": passed, "failed": failed, "total": passed + failed}))
        return 0 if failed == 0 else 1

    if args.stdin:
        reply = json.loads(sys.stdin.read())
        rec = handle(reply, env)
        print(json.dumps(rec))
        return 0

    if args.poll:
        replies = poll_instantly(env, args.since)
        handled = [handle(r, env) for r in replies]
        print(json.dumps({"polled": len(replies), "handled": len(handled)}))
        return 0

    ap.print_help()
    return 1


if __name__ == "__main__":
    raise SystemExit(main())

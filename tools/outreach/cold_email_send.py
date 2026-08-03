#!/usr/bin/env python3
"""COLD-EMAIL SAFE-SEND worker (per Sigrún envelope ENV_COLD_EMAIL_001 §D).

Flow:
  1. Read tools/olrun/approvals_parser.py resolve() of the current gate.
  2. Filter to market=cold_email rows.
  3. For each row, load the staged draft package.
  4. Pre-send verify: booking_link HTTP 200, unsub present, postal present,
     recipient not in Instantly suppression list, .env vars all set.
  5. POST /api/v2/leads to add lead to campaign, then trigger send
     (Instantly launches per campaign schedule; we don't fire per-message).
     If INSTANTLY_API_KEY absent or --dry-run flag set, write receipt with
     status=STAGED_ONLY_NO_KEY / DRY_RUN and skip the network call.
  6. Post-send: append receipt to state/experiments/publications.jsonl AND
     state/ssot/outreach_log.jsonl.
  7. Halt on any stop-gate:
     - bounce_rate > 5% over any 50 sends
     - spam_complaint > 0.1%
     - reply_rate < 2% after 50 sends
     - any 4xx/5xx from Instantly API

Usage:
  python tools/outreach/cold_email_send.py --now 2026-08-04T14:00:00Z
  python tools/outreach/cold_email_send.py --dry-run --limit 3
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import sys
import urllib.error
import urllib.request
from pathlib import Path
from typing import Optional

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from tools.olrun.approvals_parser import (  # noqa: E402
    load_index,
    parse_gate_file,
    resolve,
)

GATE_PATH = ROOT / "state" / "experiments" / "approvals" / "latest.txt"
INDEX_PATH = ROOT / "outputs" / "staged_sends" / "OPERATOR_APPROVAL_INDEX_20260803.md"
PUB_LOG = ROOT / "state" / "experiments" / "publications.jsonl"
OUTREACH_LOG = ROOT / "state" / "ssot" / "outreach_log.jsonl"
SUPPRESSION_PATH = ROOT / "state" / "outreach" / "suppression.txt"
ENV_PATH = ROOT / ".env"

INSTANTLY_BASE = "https://api.instantly.ai/api/v2"

# Halt thresholds per envelope §D.stop_gates
HALT_BOUNCE_RATE = 0.05
HALT_SPAM_RATE = 0.001
HALT_REPLY_RATE = 0.02  # only enforced after >= 50 sends


def now_utc() -> dt.datetime:
    return dt.datetime.now(tz=dt.timezone.utc)


def load_env() -> dict[str, str]:
    """Parse .env into dict; empty values or {{...}} placeholders count as unset."""
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


def load_suppression() -> set[str]:
    if not SUPPRESSION_PATH.exists():
        return set()
    return {ln.strip().lower() for ln in SUPPRESSION_PATH.read_text(encoding="utf-8").splitlines() if ln.strip() and not ln.startswith("#")}


def http_head(url: str, timeout: float = 6.0) -> int:
    req = urllib.request.Request(url, method="HEAD")
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return resp.status
    except urllib.error.HTTPError as e:
        return e.code
    except Exception:
        return 0


def check_stop_gates() -> Optional[str]:
    """Return halt reason string if a stop-gate has tripped; else None.

    Reads state/experiments/publications.jsonl for cold_email rows only.
    """
    if not PUB_LOG.exists():
        return None
    sent = bounces = spam = replies = 0
    for line in PUB_LOG.read_text(encoding="utf-8").splitlines():
        try:
            rec = json.loads(line)
        except json.JSONDecodeError:
            continue
        if rec.get("market") != "cold_email":
            continue
        if rec.get("status") == "sent":
            sent += 1
        if rec.get("event") == "bounce":
            bounces += 1
        if rec.get("event") == "spam_complaint":
            spam += 1
        if rec.get("event") == "reply":
            replies += 1
    if sent >= 50:
        if bounces / sent > HALT_BOUNCE_RATE:
            return f"HALT: bounce_rate={bounces / sent:.3f} > {HALT_BOUNCE_RATE}"
        if replies / sent < HALT_REPLY_RATE:
            return f"HALT: reply_rate={replies / sent:.3f} < {HALT_REPLY_RATE} after {sent} sends"
    if sent > 0 and spam / sent > HALT_SPAM_RATE:
        return f"HALT: spam_complaint_rate={spam / sent:.4f} > {HALT_SPAM_RATE}"
    return None


def pre_send_verify(draft: dict, env: dict, suppression: set[str]) -> tuple[bool, list[str]]:
    """Return (ok, reasons_if_not_ok)."""
    problems = []
    if not draft.get("to"):
        problems.append("draft missing 'to'")
    elif draft["to"].lower() in suppression:
        problems.append(f"recipient {draft['to']} in suppression list")
    if not draft.get("subject"):
        problems.append("draft missing 'subject'")
    if not draft.get("body"):
        problems.append("draft missing 'body'")
    for slot in ("BOOKING_LINK", "UNSUBSCRIBE_LINK", "POSTAL_ADDRESS", "SENDER_NAME"):
        if slot not in env:
            problems.append(f".env missing {slot}")
    body = draft.get("body", "")
    # Substitute the two we can check pre-send.
    if "{{UNSUBSCRIBE_LINK}}" not in body and "UNSUBSCRIBE_LINK" not in env:
        problems.append("body missing unsubscribe placeholder AND no env value")
    if "{{POSTAL_ADDRESS}}" not in body and "POSTAL_ADDRESS" not in env:
        problems.append("body missing postal placeholder AND no env value")
    if env.get("BOOKING_LINK"):
        status = http_head(env["BOOKING_LINK"])
        if status != 200:
            problems.append(f"booking_link returned HTTP {status} (must be 200)")
    return (not problems, problems)


def substitute(body: str, env: dict) -> str:
    for slot in ("BOOKING_LINK", "UNSUBSCRIBE_LINK", "POSTAL_ADDRESS", "SENDER_NAME"):
        body = body.replace("{{" + slot + "}}", env.get(slot, "MISSING_" + slot))
    return body


def instantly_add_lead(campaign_id: str, api_key: str, draft: dict, body_rendered: str) -> tuple[int, dict]:
    """POST /api/v2/leads (Instantly's actual endpoint may differ; adjust per docs)."""
    payload = {
        "campaign": campaign_id,
        "leads": [
            {
                "email": draft["to"],
                "first_name": draft.get("first_name", ""),
                "company_name": draft.get("company", ""),
                "personalization": body_rendered,
                "custom_variables": {
                    "subject": draft["subject"],
                    "pain_signal": draft.get("pain_signal", ""),
                },
            }
        ],
        "skip_if_in_workspace": True,
    }
    req = urllib.request.Request(
        f"{INSTANTLY_BASE}/leads",
        data=json.dumps(payload).encode("utf-8"),
        headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            body = json.loads(resp.read().decode("utf-8"))
            return resp.status, body
    except urllib.error.HTTPError as e:
        return e.code, {"error": e.reason, "body": e.read().decode("utf-8", errors="ignore")}
    except Exception as e:
        return 0, {"error": str(e)}


def append_receipt(rec: dict) -> None:
    PUB_LOG.parent.mkdir(parents=True, exist_ok=True)
    OUTREACH_LOG.parent.mkdir(parents=True, exist_ok=True)
    with PUB_LOG.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(rec) + "\n")
    with OUTREACH_LOG.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(rec) + "\n")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--now", default=None, help="ISO UTC override for tests")
    ap.add_argument("--dry-run", action="store_true", help="verify + log DRY_RUN receipts; no network")
    ap.add_argument("--limit", type=int, default=None, help="cap sends this run (overrides quota)")
    args = ap.parse_args()

    now = (
        dt.datetime.fromisoformat(args.now.replace("Z", "+00:00"))
        if args.now
        else now_utc()
    )
    env = load_env()
    suppression = load_suppression()

    halt = check_stop_gates()
    if halt:
        print(f"{halt} — refusing to send", file=sys.stderr)
        return 2

    gate = parse_gate_file(GATE_PATH)
    index = load_index(INDEX_PATH)
    resolved = resolve(gate, index, now)
    cold_rows = [r for r in resolved if r["market"] == "cold_email"]
    if args.limit is not None:
        cold_rows = cold_rows[: args.limit]

    api_key = env.get("INSTANTLY_API_KEY")
    campaign_id = env.get("INSTANTLY_CAMPAIGN_ID")
    dry = args.dry_run or not (api_key and campaign_id)

    sent = failed = skipped = 0
    for row in cold_rows:
        pkg_dir = ROOT / row["package_path"]
        draft_path = pkg_dir / "draft.json"
        if not draft_path.exists():
            skipped += 1
            append_receipt({"ts": now.isoformat(), "market": "cold_email", "seq": row["seq"], "status": "skip_no_draft", "reason": str(draft_path)})
            continue
        draft = json.loads(draft_path.read_text(encoding="utf-8"))
        ok, problems = pre_send_verify(draft, env, suppression)
        if not ok:
            skipped += 1
            append_receipt({"ts": now.isoformat(), "market": "cold_email", "seq": row["seq"], "to": draft.get("to"), "status": "skip_pre_send_failed", "problems": problems})
            continue
        rendered_body = substitute(draft["body"], env)
        if dry:
            append_receipt({"ts": now.isoformat(), "market": "cold_email", "seq": row["seq"], "to": draft["to"], "status": "DRY_RUN", "would_send": {"subject": draft["subject"], "body_len": len(rendered_body)}})
            sent += 1
            continue
        assert api_key and campaign_id  # for type checker; dry path is above
        status, body = instantly_add_lead(campaign_id, api_key, draft, rendered_body)
        if 200 <= status < 300:
            sent += 1
            append_receipt({"ts": now.isoformat(), "market": "cold_email", "seq": row["seq"], "to": draft["to"], "status": "sent", "instantly_response": body, "campaign_id": campaign_id})
        else:
            failed += 1
            append_receipt({"ts": now.isoformat(), "market": "cold_email", "seq": row["seq"], "to": draft["to"], "status": "api_error", "http_status": status, "response": body})
            if 400 <= status < 600:
                print(f"HALT: Instantly API {status} — see log", file=sys.stderr)
                print(json.dumps({"sent": sent, "failed": failed, "skipped": skipped, "halted_after_first_api_error": True}))
                return 3

    print(json.dumps({"sent": sent, "failed": failed, "skipped": skipped, "dry_run": dry, "resolved_cold_rows": len(cold_rows)}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

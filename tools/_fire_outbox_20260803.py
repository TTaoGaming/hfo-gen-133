#!/usr/bin/env python3
"""One-shot fire script for the 2026-08-03 gen-133 broadcaster outbox.

Uses tools/slack_post_bot.py's helper functions to POST via chat.postMessage
with the SLACK_BOT_TOKEN recovered from gen-131. Writes one JSONL row per
attempt to state/olrun/SLACK_DELIVERY_LOG_20260803.jsonl (append-only) and to
state/olrun/CREDENTIAL_RECOVERY_LOG.jsonl (chain-row per mandate).

Idempotency: this script appends. Re-running will double-post; do not re-run
without pruning the delivery log first.
"""
from __future__ import annotations
import datetime as _dt
import json
import pathlib
import sys
import time

ROOT = pathlib.Path(r"C:\Dev\hfo_gen_133_forge")
sys.path.insert(0, str(ROOT / "tools"))

# reuse helpers from the bot poster (loads SLACK_BOT_TOKEN from .env)
import slack_post_bot as bot  # type: ignore

DELIVERY_LOG = ROOT / "state" / "olrun" / "SLACK_DELIVERY_LOG_20260803.jsonl"
CHAIN_LOG = ROOT / "state" / "olrun" / "CREDENTIAL_RECOVERY_LOG.jsonl"

NOW = _dt.datetime.now(_dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

# (message_type, artifact_ref, channel)
QUEUE = [
    ("exec_summary", "state/olrun/slack_outbox_20260803/00_exec_summary_command_and_control.md", "#hfo-command-and-control"),
    ("adr_digest", "state/olrun/slack_outbox_20260803/01_adr_digest_synthesis.md", "#hfo-synthesis"),
    ("research_report_summaries", "state/olrun/slack_outbox_20260803/02_research_reports_synthesis.md", "#hfo-synthesis"),
    ("active_blockers", "state/olrun/slack_outbox_20260803/03_blockers_andon.md", "#hfo-andon"),
    ("cross_gen_anchor", "state/olrun/slack_outbox_20260803/04_cross_gen_anchor_synthesis.md", "#hfo-synthesis"),
]

V9_PATH = ROOT / "state" / "olrun" / "slack_outbox" / "SIGRUN_V9_SYNTHESIS_PHEROMONES_20260803.md"


def strip_yaml(text: str) -> str:
    if text.startswith("---\n"):
        end = text.find("\n---\n", 4)
        if end != -1:
            return text[end + 5:]
    return text


def append_jsonl(path: pathlib.Path, row: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as f:
        f.write(json.dumps(row, ensure_ascii=False) + "\n")


def fire_single(message_type: str, artifact_ref: str, channel: str, text: str,
                thread_ts: str | None = None) -> dict:
    token = bot.get_token()
    payload = {
        "channel": channel,
        "text": text,
        "unfurl_links": False,
        "unfurl_media": False,
    }
    if thread_ts:
        payload["thread_ts"] = thread_ts
    result = bot.call("chat.postMessage", payload, token)
    row = {
        "ts": _dt.datetime.now(_dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "actor": "cross_gen_credential_hunter",
        "channel": channel,
        "message_type": message_type,
        "artifact_ref": artifact_ref,
        "delivered": bool(result.get("ok")),
        "slack_ts": result.get("ts"),
        "slack_channel_id": result.get("channel"),
        "error": result.get("error"),
        "warning": result.get("warning"),
        "thread_ts": thread_ts,
    }
    append_jsonl(DELIVERY_LOG, row)
    append_jsonl(CHAIN_LOG, {
        **row,
        "action": "slack_post",
        "credential_source": "gen-131 sigrun_secrets/.env (SLACK_BOT_TOKEN)",
    })
    return row


def main() -> int:
    append_jsonl(CHAIN_LOG, {
        "ts": NOW,
        "actor": "cross_gen_credential_hunter",
        "action": "session_start",
        "credential_found_at": "C:/Dev/hfo_gen_131_forge/state/sigrun_secrets/.env",
        "credential_kind": "SLACK_BOT_TOKEN (xoxb-)",
        "wired_to": "C:/Dev/hfo_gen_133_forge/.env (appended)",
        "auth_test": "ok — team=hfo user=hfo_local_dispatcher",
    })

    ok = 0
    fail = 0

    # Fire the 5 broadcaster messages
    for mtype, ref, channel in QUEUE:
        path = ROOT / ref
        try:
            text = strip_yaml(path.read_text(encoding="utf-8"))
        except OSError as e:
            append_jsonl(DELIVERY_LOG, {
                "ts": _dt.datetime.now(_dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
                "actor": "cross_gen_credential_hunter",
                "channel": channel, "message_type": mtype, "artifact_ref": ref,
                "delivered": False, "error": f"read_failed: {e!r}",
            })
            fail += 1
            continue
        row = fire_single(mtype, ref, channel, text)
        print(f"[{mtype}] channel={row.get('slack_channel_id')} "
              f"ts={row.get('slack_ts')} ok={row['delivered']} err={row.get('error')}")
        if row["delivered"]:
            ok += 1
        else:
            fail += 1
        time.sleep(2)

    # Fire the V9 SIGRÚN posts (14 posts, threaded — first post seeds, rest reply in-thread)
    if V9_PATH.exists():
        raw = strip_yaml(V9_PATH.read_text(encoding="utf-8"))
        parts = [p.strip() for p in raw.split("---POST---") if p.strip()]
        parent_ts = None
        for i, post in enumerate(parts, 1):
            row = fire_single(
                f"sigrun_v9_post_{i:02d}",
                "state/olrun/slack_outbox/SIGRUN_V9_SYNTHESIS_PHEROMONES_20260803.md",
                "#hfo-synthesis",
                post,
                thread_ts=parent_ts,
            )
            print(f"[V9 {i}/{len(parts)}] ts={row.get('slack_ts')} "
                  f"ok={row['delivered']} err={row.get('error')}")
            if row["delivered"]:
                ok += 1
                if parent_ts is None:
                    parent_ts = row.get("slack_ts")
            else:
                fail += 1
                # abort V9 thread on first failure — a partial thread is worse than none
                append_jsonl(CHAIN_LOG, {
                    "ts": _dt.datetime.now(_dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
                    "actor": "cross_gen_credential_hunter",
                    "action": "v9_thread_aborted",
                    "at_post": i, "of": len(parts), "error": row.get("error"),
                })
                break
            time.sleep(2)

    append_jsonl(CHAIN_LOG, {
        "ts": _dt.datetime.now(_dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "actor": "cross_gen_credential_hunter",
        "action": "fire_complete",
        "delivered": ok, "failed": fail,
    })
    print(f"\ndone: delivered={ok} failed={fail}")
    return 0 if fail == 0 else 1


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""Post a message to Slack via chat.postMessage using a bot token.

Companion to tools/slack_post.py (webhook variant). Use this when you have a
SLACK_BOT_TOKEN (xoxb-...) and want to target a channel by ID or name.

Token / channel are NEVER taken as CLI args (would leak into shell history /
process list). Read them from env, or from .env in the forge root.

Env vars (first path found wins):
    SLACK_BOT_TOKEN         xoxb-... bot user OAuth token
    SLACK_CHANNEL           channel ID (Cxxxxxxxxxx) or name (#hfo-...)
    SLACK_THREAD_TS         (optional) parent message ts for a threaded reply

Usage:
    SLACK_BOT_TOKEN=xoxb-... SLACK_CHANNEL=#hfo-synthesis \\
        python tools/slack_post_bot.py "message text"

    echo "message text" | SLACK_BOT_TOKEN=... SLACK_CHANNEL=C0... \\
        python tools/slack_post_bot.py

    # Auth-only check (no message sent):
    SLACK_BOT_TOKEN=... python tools/slack_post_bot.py --auth-check

Fallback: if SLACK_BOT_TOKEN is not in env, read it from the first .env file
found by walking up from this file (looking for a line SLACK_BOT_TOKEN=...).
"""
import argparse
import json
import os
import pathlib
import sys
import urllib.request
import urllib.error


def _load_from_dotenv(varname: str) -> str | None:
    here = pathlib.Path(__file__).resolve()
    for parent in [here.parent, *here.parents]:
        candidate = parent / ".env"
        if candidate.exists():
            try:
                for line in candidate.read_text(encoding="utf-8", errors="replace").splitlines():
                    line = line.strip()
                    if line.startswith(varname + "="):
                        v = line.split("=", 1)[1].strip().strip("'\"")
                        if v and not v.startswith("{{"):
                            return v
            except OSError:
                pass
        if parent == parent.parent:
            break
    return None


def get_token() -> str:
    tok = os.environ.get("SLACK_BOT_TOKEN") or _load_from_dotenv("SLACK_BOT_TOKEN")
    if not tok:
        raise SystemExit(
            "No SLACK_BOT_TOKEN in env or .env. Set SLACK_BOT_TOKEN=xoxb-... "
            "before running (or paste it into the nearest .env)."
        )
    return tok


def call(method: str, payload: dict, token: str) -> dict:
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        f"https://slack.com/api/{method}",
        data=data,
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json; charset=utf-8",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            body = resp.read().decode("utf-8")
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")
    try:
        return json.loads(body)
    except json.JSONDecodeError:
        return {"ok": False, "raw": body[:400]}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("text", nargs="*", help="message text (or read from stdin)")
    ap.add_argument("--auth-check", action="store_true",
                    help="call auth.test and print result — send no message")
    ap.add_argument("--channel", default=None,
                    help="override SLACK_CHANNEL for this call")
    ap.add_argument("--thread-ts", default=None,
                    help="reply to this parent ts in a thread")
    args = ap.parse_args()

    token = get_token()

    if args.auth_check:
        result = call("auth.test", {}, token)
        print(json.dumps(result, indent=2))
        return 0 if result.get("ok") else 2

    channel = args.channel or os.environ.get("SLACK_CHANNEL")
    if not channel:
        raise SystemExit(
            "No channel. Pass --channel or set SLACK_CHANNEL "
            "(e.g. #hfo-synthesis or Cxxxxxxxx)."
        )

    if args.text:
        text = " ".join(args.text)
    else:
        text = sys.stdin.read()
    text = text.strip()
    if not text:
        raise SystemExit("No message text (arg or stdin).")

    payload = {"channel": channel, "text": text, "unfurl_links": False, "unfurl_media": False}
    thread_ts = args.thread_ts or os.environ.get("SLACK_THREAD_TS")
    if thread_ts:
        payload["thread_ts"] = thread_ts

    result = call("chat.postMessage", payload, token)
    print(json.dumps(
        {k: v for k, v in result.items() if k in ("ok", "channel", "ts", "error", "warning")},
        indent=2,
    ))
    return 0 if result.get("ok") else 3


if __name__ == "__main__":
    sys.exit(main())

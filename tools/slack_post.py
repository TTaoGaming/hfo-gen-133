#!/usr/bin/env python3
"""Post a message to Slack via an incoming webhook URL. Stdlib only.

Webhook URL is never taken as a CLI arg (would leak into shell history /
process list). Read it from an env var instead.

Usage:
    SLACK_WEBHOOK_URL=https://hooks.slack.com/services/... \
        python tools/slack_post.py "message text"

    echo "message text" | SLACK_WEBHOOK_URL=... python tools/slack_post.py

Env vars (first one found wins):
    SLACK_WEBHOOK_URL
    SLACK_INCOMING_WEBHOOK
"""
import json
import os
import sys
import urllib.request


def get_webhook_url() -> str:
    url = os.environ.get("SLACK_WEBHOOK_URL") or os.environ.get("SLACK_INCOMING_WEBHOOK")
    if not url:
        raise SystemExit(
            "No webhook configured. Set SLACK_WEBHOOK_URL (or SLACK_INCOMING_WEBHOOK) "
            "in the environment before running this script."
        )
    return url


def post(text: str, webhook_url: str) -> int:
    body = json.dumps({"text": text}).encode("utf-8")
    req = urllib.request.Request(
        webhook_url,
        data=body,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=10) as resp:
        return resp.status


def main() -> None:
    if len(sys.argv) > 1:
        text = " ".join(sys.argv[1:])
    else:
        text = sys.stdin.read().strip()
    if not text:
        raise SystemExit("No message text given (arg or stdin).")

    webhook_url = get_webhook_url()
    status = post(text, webhook_url)
    print(f"posted, status={status}")


if __name__ == "__main__":
    main()

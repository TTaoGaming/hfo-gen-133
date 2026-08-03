#!/usr/bin/env python3
"""Fire a staged Slack pheromone outbox, one post per message.

Dry-run by default. Sending is ENV-C (contact class) and requires --send.

    python tools/fire_outbox.py <outbox.md>            # validate + preview, sends nothing
    python tools/fire_outbox.py <outbox.md> --send     # actually post each block

Posts are separated by a line containing exactly ---POST---. Slack's practical
block limit is ~3000 chars; pheromone discipline here is 2000. Any post over the
limit fails validation and NOTHING is sent — a partial thread is worse than none.
"""
from __future__ import annotations

import argparse
import pathlib
import subprocess
import sys

LIMIT = 2000
DELIM = "---POST---"


def load(path: pathlib.Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    # drop YAML front matter if present
    if text.startswith("---\n"):
        end = text.find("\n---\n", 4)
        if end != -1:
            text = text[end + 5:]
    parts = [p.strip() for p in text.split(DELIM)]
    return [p for p in parts if p]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("outbox")
    ap.add_argument("--send", action="store_true", help="actually post (ENV-C)")
    args = ap.parse_args()

    path = pathlib.Path(args.outbox)
    posts = load(path)
    if not posts:
        print("no posts found — check the delimiter")
        return 1

    over = [(i, len(p)) for i, p in enumerate(posts, 1) if len(p) > LIMIT]
    print(f"{len(posts)} post(s); longest {max(len(p) for p in posts)} chars; limit {LIMIT}")
    if over:
        print("VALIDATION FAILED — posts over limit (nothing sent):")
        for i, n in over:
            print(f"  post {i}: {n} chars")
        return 1
    print("validation OK")

    if not args.send:
        for i, p in enumerate(posts, 1):
            print(f"\n--- [{i}/{len(posts)}] {len(p)} chars ---")
            print(p.splitlines()[0][:96])
        print("\nDRY RUN — nothing sent. Re-run with --send once SLACK_WEBHOOK_URL is real.")
        return 0

    root = pathlib.Path(__file__).resolve().parent.parent
    for i, p in enumerate(posts, 1):
        r = subprocess.run([sys.executable, "tools/slack_post.py"],
                           input=p.encode("utf-8"), capture_output=True, cwd=root)
        if r.returncode != 0:
            print(f"HALT at post {i}: {r.stderr.decode()[:200]}")
            return 1
        print(f"  sent {i}/{len(posts)}")
    print("outbox fired")
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""LOOP-D · DEMAND_SIGNAL_MINE — pull last-24h posts from Reddit + HN + IH,
extract pain patterns, classify via LiteLLM, score against MAP-Elite cells,
emit a daily digest.

AIH2O header
------------
AIH2O:
  version: gen-133
  loop: demand_signal_mine
  role: executor
  actor: factory_loop
  verifier: n_signals > 0 OR explicit zero-signal chain-row with reason
  clock_source: host_read
  chain: state/loop_receipts/demand_signal_mine_<UTCDATE>.jsonl
  signal_log: state/factory_targets/DEMAND_SIGNAL_LOG.jsonl
  daily_digest: state/factory_targets/DEMAND_DIGEST_<UTCDATE>.md

CLI
---
    python factory/loops/demand_signal_mine/run.py \\
        --subreddits subs.txt --patterns patterns.json --cells cells.json

Kill conditions
---------------
- Reddit rate-limit → exponential backoff 60s → 300s → 1800s then continue
- All sources fail → chain-row zero_signals + slack warn
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

_HERE = Path(__file__).resolve()
_FORGE = _HERE.parents[3]
sys.path.insert(0, str(_FORGE))
from factory.loops.lib import chain_row, litellm_client, slack_escalate  # noqa: E402


LOOP = "demand_signal_mine"
SIGNAL_LOG = _FORGE / "state" / "factory_targets" / "DEMAND_SIGNAL_LOG.jsonl"
DIGEST_DIR = _FORGE / "state" / "factory_targets"

USER_AGENT = "hfo-gen133-factory-loop/0.1"
REDDIT_JSON = "https://www.reddit.com/r/{sub}/new.json?limit=100"
HN_NEW_JSON = "https://hacker-news.firebaseio.com/v0/newstories.json"
HN_ITEM_JSON = "https://hacker-news.firebaseio.com/v0/item/{id}.json"


def _utc() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _utc_today() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%d")


def _fetch_json(url: str, retries: int = 3) -> tuple[bool, dict | list | None, str]:
    """Fetch with exponential backoff on 429/5xx."""
    backoffs = [60, 300, 1800]  # 1min → 5min → 30min
    for attempt in range(retries + 1):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
            with urllib.request.urlopen(req, timeout=30) as resp:
                return True, json.loads(resp.read().decode("utf-8")), ""
        except urllib.error.HTTPError as e:
            if e.code == 429 and attempt < retries:
                wait = backoffs[min(attempt, len(backoffs) - 1)]
                time.sleep(wait)
                continue
            return False, None, f"HTTP {e.code}"
        except (urllib.error.URLError, TimeoutError, OSError) as e:
            if attempt < retries:
                time.sleep(min(30, 5 * (attempt + 1)))
                continue
            return False, None, str(e)
    return False, None, "exhausted retries"


def fetch_reddit(sub: str) -> list[dict]:
    ok, data, err = _fetch_json(REDDIT_JSON.format(sub=sub))
    if not ok or not isinstance(data, dict):
        return []
    posts = []
    now = time.time()
    for child in data.get("data", {}).get("children", []):
        d = child.get("data", {})
        created = d.get("created_utc", 0)
        if now - created > 24 * 3600:
            continue
        posts.append(
            {
                "source": f"reddit:{sub}",
                "id": d.get("id"),
                "title": d.get("title") or "",
                "text": d.get("selftext") or "",
                "url": "https://www.reddit.com" + d.get("permalink", ""),
                "score": d.get("score", 0),
                "num_comments": d.get("num_comments", 0),
                "created_utc": created,
            }
        )
    return posts


def fetch_hn_new(limit: int = 100) -> list[dict]:
    ok, ids, _ = _fetch_json(HN_NEW_JSON)
    if not ok or not isinstance(ids, list):
        return []
    out = []
    for hid in ids[:limit]:
        ok2, item, _ = _fetch_json(HN_ITEM_JSON.format(id=hid))
        if not ok2 or not isinstance(item, dict):
            continue
        # 24h filter
        if time.time() - item.get("time", 0) > 24 * 3600:
            continue
        out.append(
            {
                "source": "hn:new",
                "id": item.get("id"),
                "title": item.get("title") or "",
                "text": item.get("text") or "",
                "url": item.get("url") or f"https://news.ycombinator.com/item?id={item.get('id')}",
                "score": item.get("score", 0),
                "num_comments": item.get("descendants", 0),
                "created_utc": item.get("time"),
            }
        )
        # be nice
        time.sleep(0.05)
    return out


def extract_pain_pattern(post: dict, patterns: dict) -> list[str]:
    """Regex-based first pass. patterns = {label: regex}."""
    hits = []
    body = (post.get("title", "") + " " + post.get("text", "")).lower()
    for label, rx in patterns.items():
        try:
            if re.search(rx, body, flags=re.I):
                hits.append(label)
        except re.error:
            continue
    return hits


def score_against_cells(post: dict, hits: list[str], cells: dict) -> tuple[str | None, float]:
    """cells = {"axis1_axis2_axis3": {"terms":[...], "weight":1.0}, ...}
    Pick the highest-scoring cell for this post. Returns (cell_id, score)."""
    body = (post.get("title", "") + " " + post.get("text", "")).lower()
    best_cell = None
    best_score = 0.0
    for cell_id, meta in cells.items():
        terms = meta.get("terms", []) if isinstance(meta, dict) else meta
        weight = float(meta.get("weight", 1.0)) if isinstance(meta, dict) else 1.0
        score = sum(1 for t in terms if t.lower() in body)
        score *= weight
        # Bonus for pattern hits
        score += 0.5 * len(hits)
        if score > best_score:
            best_score = score
            best_cell = cell_id
    return best_cell, best_score


def classify_with_llm(post: dict, hits: list[str]) -> str:
    """Cheap classification pass — returns a 1-line category string.
    Uses LiteLLM proxy or falls through to DRY_RUN stub."""
    prompt = (
        "One-line pain-category label for this social post. "
        "Format: '<icp>|<pain>|<affordability_signal 0-3>'. "
        "Nothing else.\n\n"
        f"TITLE: {post.get('title','')[:200]}\n"
        f"BODY: {post.get('text','')[:600]}\n"
        f"REGEX_HITS: {','.join(hits) or 'none'}"
    )
    r = litellm_client.complete(prompt, max_tokens=64, temperature=0.2)
    if not r.ok:
        return f"UNKNOWN|{','.join(hits) or 'no_pattern'}|0"
    return r.text.strip().splitlines()[0][:200]


def append_signal(sig: dict) -> None:
    SIGNAL_LOG.parent.mkdir(parents=True, exist_ok=True)
    with SIGNAL_LOG.open("a", encoding="utf-8", newline="\n") as fh:
        fh.write(json.dumps(sig, ensure_ascii=False, sort_keys=True) + "\n")


def build_digest(signals: list[dict], cell_coverage: dict[str, int]) -> Path:
    day = _utc_today()
    out = DIGEST_DIR / f"DEMAND_DIGEST_{day}.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    top = sorted(signals, key=lambda s: s.get("cell_score", 0), reverse=True)[:10]
    lines = [f"# Demand Digest — {day}\n\n"]
    lines.append(f"**Signals collected:** {len(signals)}\n\n")
    lines.append("## Top 10 by cell score\n\n")
    for i, s in enumerate(top, 1):
        lines.append(
            f"{i}. **{s.get('cell') or '(no cell)'}** · score={s.get('cell_score'):.2f}\n"
            f"   - {s['source']} · [{s['title'][:120]}]({s['url']})\n"
            f"   - hits: {', '.join(s.get('pattern_hits', []) or ['none'])}\n"
            f"   - classify: `{s.get('llm_label','')}`\n\n"
        )
    lines.append("## Cell coverage (last 24h)\n\n")
    for cell, count in sorted(cell_coverage.items(), key=lambda kv: kv[1], reverse=True):
        lines.append(f"- `{cell}` — {count}\n")
    out.write_text("".join(lines), encoding="utf-8")
    return out


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--subreddits", type=Path, required=True, help="txt file, one sub per line")
    p.add_argument("--patterns", type=Path, required=True, help="JSON {label: regex}")
    p.add_argument("--cells", type=Path, required=True, help="JSON {cell_id: {terms:[], weight:float}}")
    p.add_argument("--include-hn", action="store_true", default=True)
    p.add_argument("--dry-run", action="store_true", help="skip LLM classification")
    args = p.parse_args(argv)

    subs = [s.strip() for s in args.subreddits.read_text(encoding="utf-8").splitlines() if s.strip() and not s.startswith("#")]
    patterns = json.loads(args.patterns.read_text(encoding="utf-8"))
    cells = json.loads(args.cells.read_text(encoding="utf-8"))

    chain_row.append_row(
        LOOP,
        action="start_scan",
        verifier_result=f"subs={len(subs)} patterns={len(patterns)} cells={len(cells)}",
        claim_status="proposed",
        remaining_risk=["rate_limit", "source_down"],
        next_safe_action="fetch",
        honest_flaw="none",
        extra={"subs": subs},
    )

    all_posts: list[dict] = []
    for sub in subs:
        posts = fetch_reddit(sub)
        all_posts.extend(posts)
        time.sleep(1.5)  # be nice to reddit
    if args.include_hn:
        all_posts.extend(fetch_hn_new(limit=100))

    signals: list[dict] = []
    cell_coverage: dict[str, int] = {}
    for post in all_posts:
        hits = extract_pain_pattern(post, patterns)
        cell, score = score_against_cells(post, hits, cells)
        if score <= 0 and not hits:
            continue
        label = "" if args.dry_run else classify_with_llm(post, hits)
        sig = {
            "ts_utc": _utc(),
            **{k: post.get(k) for k in ("source", "id", "title", "url", "score", "num_comments")},
            "pattern_hits": hits,
            "cell": cell,
            "cell_score": score,
            "llm_label": label,
        }
        append_signal(sig)
        signals.append(sig)
        if cell:
            cell_coverage[cell] = cell_coverage.get(cell, 0) + 1

    digest = build_digest(signals, cell_coverage)

    chain_row.append_row(
        LOOP,
        action="finish_scan",
        verifier_result=f"{len(signals)} signals from {len(all_posts)} posts; digest={digest.name}",
        claim_status="wired_with_receipts" if signals else "partial",
        remaining_risk=["stale_patterns_may_miss_new_pain"] if signals else ["all_sources_may_have_failed"],
        next_safe_action="operator_review_digest",
        honest_flaw="none" if signals else "zero signals — check patterns.json or source availability",
        extra={"n_signals": len(signals), "n_posts": len(all_posts), "digest": str(digest.relative_to(_FORGE)), "cell_coverage": cell_coverage},
    )

    if not signals:
        slack_escalate.escalate(LOOP, "ZERO signals in daily mine", f"scanned {len(all_posts)} posts, no matches", severity="warn")
    print(json.dumps({"n_posts": len(all_posts), "n_signals": len(signals), "digest": str(digest)}, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())

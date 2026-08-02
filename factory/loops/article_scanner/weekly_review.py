#!/usr/bin/env python3
"""LOOP-A · ARTICLE_SCANNER — weekly review generator.

Reads the last 7 days of state/factory_targets/article_signals.jsonl,
ranks by composite score, writes ARTICLE_WEEK_<yyyymmdd>.md with
`pick` / `skip` / `note` columns for operator triage.

Operator edits the file in place (flip `pick` to `x`). A separate
downstream step (out of scope here) reads picks and feeds them into
MAP-Elites cell scoring for next build cadence.

AIH2O
-----
AIH2O:
  version: gen-133
  loop: article_scanner
  role: reviewer
  actor: factory_loop
  verifier: n_rows > 0 OR explicit empty-week chain-row with reason
  clock_source: host_read
  chain: state/loop_receipts/article_scanner_<UTCDATE>.jsonl
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

_HERE = Path(__file__).resolve()
_FORGE = _HERE.parents[3]
sys.path.insert(0, str(_FORGE))
from factory.loops.lib import chain_row  # noqa: E402

LOOP = "article_scanner"
SIGNAL_LOG = _FORGE / "state" / "factory_targets" / "article_signals.jsonl"
DIGEST_DIR = _FORGE / "state" / "factory_targets"


def _utc_today() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%d")


def _iter_signals():
    if not SIGNAL_LOG.exists():
        return
    with SIGNAL_LOG.open("r", encoding="utf-8", errors="replace") as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            try:
                yield json.loads(line)
            except Exception:
                continue


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--days", type=int, default=7)
    p.add_argument("--top", type=int, default=20)
    args = p.parse_args(argv)

    cutoff = datetime.now(timezone.utc) - timedelta(days=args.days)
    rows = []
    for r in _iter_signals():
        try:
            ts = datetime.strptime(r.get("ts_utc", ""), "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)
        except Exception:
            continue
        if ts < cutoff:
            continue
        rows.append(r)

    rows.sort(key=lambda x: float(x.get("composite", 0)), reverse=True)
    top = rows[:args.top]

    day = _utc_today()
    out = DIGEST_DIR / f"ARTICLE_WEEK_{day}.md"
    out.parent.mkdir(parents=True, exist_ok=True)

    header = (
        f"# Article Week — {day} ({args.days}d window)\n\n"
        f"Signals in window: **{len(rows)}** — showing top **{len(top)}** by composite.\n\n"
        "Operator: flip `pick` to `x` to send to MAP-Elites cell scoring.\n"
        "Add a short `note` if the pick needs context.\n\n"
        "| # | pick | axis | source | title | score | hfo_action | note |\n"
        "|---|:----:|------|--------|-------|:-----:|------------|------|\n"
    )
    lines = [header]
    for i, r in enumerate(top, 1):
        title_cell = f"[{(r.get('title') or '(untitled)')[:100].replace('|', '/')}]({r.get('url','')})"
        action = (r.get("hfo_action") or "").replace("|", "/")[:120]
        lines.append(
            f"| {i} | [ ] | `{r.get('axis','?')}` | `{r.get('source_id','?')}` | "
            f"{title_cell} | {float(r.get('composite',0)):.3f} | {action} | |\n"
        )

    lines.append("\n---\n\n## How this gets consumed\n\n"
                 "1. Operator opens this file, flips `[ ]` to `[x]` on desired rows.\n"
                 "2. `git add` + `git commit` — the file itself is the pick receipt.\n"
                 "3. Downstream: `factory/loops/article_scanner/harvest_picks.py`\n"
                 "   (planned) reads the ticked rows and appends to MAP-Elites\n"
                 "   cell scoring inputs. Until that harvester exists, the picks\n"
                 "   are still auditable in git history.\n")
    out.write_text("".join(lines), encoding="utf-8")

    chain_row.append_row(
        LOOP,
        action="weekly_review",
        verifier_result=f"{len(rows)} signals in {args.days}d window; wrote {out.name}",
        claim_status="wired_with_receipts" if rows else "partial",
        remaining_risk=[] if rows else ["no_week_signals"],
        next_safe_action="operator_pick_skip",
        honest_flaw="none" if rows else "week window had zero signals",
        extra={"n_rows": len(rows), "n_top": len(top), "review_path": str(out.relative_to(_FORGE))},
    )
    print(json.dumps({"n_rows": len(rows), "n_top": len(top), "path": str(out)}, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())

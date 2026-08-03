#!/usr/bin/env python3
"""Port a sample of gen-130's already-bitemporal-shaped memory_events into
sigrun_memory (Postgres/pgvector) -- OPTIONAL stretch goal, EMERGENCY_FORGE
worker_C, run only after HOT-7/HOT-8 are green.

Source: C:\\Dev\\hfo_dev_2026_5_30\\hfo_gen_130_forge\\state\\memory\\
hfo_bitemporal_memory.sqlite -> table memory_events (4077 rows, read-only
heritage forge, never written to).

IMPORTANT: every ported row is written with sigrun_approved=FALSE. These are
raw heritage summaries ingested by a prior generation's pipeline -- exactly
the kind of unreceipted prose-derived claim this system exists to keep OUT
of curated rehydration until a human or Sigrun explicitly reviews and calls
approve(id). Porting them pre-approved would reintroduce the defect this
whole module was built to cure.

Usage:
    python tools/memory/port_gen130_sample.py --limit 100
"""
from __future__ import annotations

import argparse
import sqlite3
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import bitemporal as bt  # noqa: E402

SRC_DB = (
    Path("C:/Dev/hfo_dev_2026_5_30/hfo_gen_130_forge/state/memory/"
         "hfo_bitemporal_memory.sqlite")
)


def _parse_ts(s: str | None) -> datetime | None:
    if not s:
        return None
    s = s.replace("Z", "+00:00")
    try:
        dt = datetime.fromisoformat(s)
    except ValueError:
        return None
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=100)
    args = ap.parse_args()

    if not SRC_DB.exists():
        print(f"SOURCE_NOT_FOUND: {SRC_DB}", file=sys.stderr)
        return 1

    con = sqlite3.connect(str(SRC_DB))
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    # Stride sample for diversity across medallion tiers rather than the
    # first N rows in insertion order.
    cur.execute("SELECT count(*) FROM memory_events")
    total = cur.fetchone()[0]
    stride = max(1, total // args.limit)
    cur.execute(
        "SELECT * FROM memory_events "
        "WHERE (ROWID - 1) % ? = 0 "
        "ORDER BY ROWID LIMIT ?",
        (stride, args.limit),
    )
    rows = cur.fetchall()
    con.close()

    bt.ensure_schema()

    written = 0
    skipped = 0
    for r in rows:
        valid_from = _parse_ts(r["valid_time_start_utc"])
        if valid_from is None:
            skipped += 1
            continue
        valid_to = _parse_ts(r["valid_time_end_utc"]) or "infinity"
        subject = r["source_path"] or r["event_id"]
        predicate = "summarized_as"
        object_ = (r["summary"] or "")[:2000]
        if not object_:
            skipped += 1
            continue
        source_pointer = (
            f"gen130:state/memory/hfo_bitemporal_memory.sqlite:"
            f"memory_events:{r['event_id']}"
        )
        try:
            bt.write(
                subject, predicate, object_,
                valid_from=valid_from, valid_to=valid_to,
                source_pointer=source_pointer,
                confidence=0.5,  # ported heritage claim, not independently verified
                claim_status=r["claim_status"] or "proposed",
                sigrun_approved=False,  # NEVER pre-approve a ported heritage row
            )
            written += 1
        except Exception as e:
            print(f"SKIP {r['event_id']}: {type(e).__name__}: {e}", file=sys.stderr)
            skipped += 1

    print(f"PORTED written={written} skipped={skipped} source_total={total} stride={stride}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

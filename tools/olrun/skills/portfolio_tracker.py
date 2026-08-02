#!/usr/bin/env python3
"""PORTFOLIO-TRACKER (EMERGENCY_FORGE 2026-08-03, worker D, HOT-D8).

Append-only concurrent-experiment ledger at state/experiments/portfolio.jsonl.
This is the direct fix for the operator's stated pain point: the swarm runs
concurrent experiments with no kill criteria. The schema refuses to let an
experiment exist without a hypothesis, an external_signal_threshold, and a
kill_at_utc -- `--op=start` hard-fails without all three.

Every row (start/update/kill/promote) carries the FULL schema by carrying
forward the immutable fields (name, hypothesis, seed_utc,
external_signal_threshold, kill_at_utc) from the experiment's most recent
row, so no row is ever partial -- a reader can take any single row and know
the full state of the experiment at that point in time.

    python tools/olrun/skills/portfolio_tracker.py --experiment=NAME --op=start \
        --hypothesis="..." --threshold="..." --kill-at="2026-08-10T00:00:00Z"
    python tools/olrun/skills/portfolio_tracker.py --experiment=NAME --op=update \
        --signal="..." --next-action="..."
    python tools/olrun/skills/portfolio_tracker.py --experiment=NAME --op=kill \
        --signal="..."

Prints exactly one JSON object on stdout (a row summary; the ledger row on
disk is the actual evidence, not this stdout line). clock_source=host_read.
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
LEDGER = ROOT / "state" / "experiments" / "portfolio.jsonl"

SCHEMA_FIELDS = [
    "name", "hypothesis", "seed_utc", "external_signal_threshold",
    "current_signal", "next_action", "kill_at_utc",
]


def now_str() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def rel(p: Path) -> str:
    return str(p.relative_to(ROOT)).replace("\\", "/")


def load_rows() -> list[dict]:
    if not LEDGER.exists():
        return []
    rows = []
    for line in LEDGER.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            rows.append(json.loads(line))
        except json.JSONDecodeError:
            continue
    return rows


def last_row_for(rows: list[dict], name: str) -> dict | None:
    for r in reversed(rows):
        if r.get("name") == name:
            return r
    return None


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--experiment", required=True, help="experiment name (stable id across ops)")
    ap.add_argument("--op", required=True, choices=["start", "update", "kill", "promote"])
    ap.add_argument("--hypothesis")
    ap.add_argument("--threshold", help="external_signal_threshold, e.g. '1 external reply'")
    ap.add_argument("--kill-at", help="ISO-8601 UTC deadline, required at --op=start")
    ap.add_argument("--signal", help="current_signal observation")
    ap.add_argument("--next-action")
    args = ap.parse_args()

    rows = load_rows()
    prev = last_row_for(rows, args.experiment)

    if args.op == "start":
        if prev is not None:
            print(
                f"refuse: experiment {args.experiment!r} already has a row "
                f"(op={prev.get('op')} at {prev.get('written_ts_utc')}) -- use "
                f"--op=update/kill/promote, not a second start",
                file=sys.stderr,
            )
            return 1
        missing = [
            flag for flag, val in (
                ("--hypothesis", args.hypothesis),
                ("--threshold", args.threshold),
                ("--kill-at", args.kill_at),
            ) if not val
        ]
        if missing:
            print(
                "refuse to start without " + ", ".join(missing) + " -- "
                "no experiment may exist without a hypothesis, an "
                "external_signal_threshold, and a kill_at_utc (operator's "
                "stated pain point: concurrent experiments run without kill "
                "criteria)",
                file=sys.stderr,
            )
            return 1
        ts = now_str()
        row = {
            "name": args.experiment,
            "hypothesis": args.hypothesis,
            "seed_utc": ts,
            "external_signal_threshold": args.threshold,
            "current_signal": "none yet",
            "next_action": "await first external signal",
            "kill_at_utc": args.kill_at,
            "op": "start",
            "written_ts_utc": ts,
        }
    else:
        if prev is None:
            print(
                f"refuse: no prior row for experiment {args.experiment!r} -- "
                f"must --op=start before {args.op}",
                file=sys.stderr,
            )
            return 1
        row = {k: prev.get(k) for k in SCHEMA_FIELDS}
        row["op"] = args.op
        if args.op == "update":
            if args.signal:
                row["current_signal"] = args.signal
            if args.next_action:
                row["next_action"] = args.next_action
        elif args.op == "kill":
            if args.signal:
                row["current_signal"] = args.signal
            row["next_action"] = args.next_action or f"KILLED -- signal={row['current_signal']}"
        elif args.op == "promote":
            if args.signal:
                row["current_signal"] = args.signal
            row["next_action"] = args.next_action or "PROMOTED -- graduated out of experiment tracking"
        row["written_ts_utc"] = now_str()

    missing_schema = [k for k in SCHEMA_FIELDS if k not in row or row[k] in (None, "")]
    if missing_schema:
        print(f"internal error: row missing schema fields {missing_schema}", file=sys.stderr)
        return 1

    LEDGER.parent.mkdir(parents=True, exist_ok=True)
    with LEDGER.open("a", encoding="utf-8") as f:
        f.write(json.dumps(row) + "\n")

    payload = {
        "name": row["name"],
        "op": row["op"],
        "ledger_path": rel(LEDGER),
        "current_signal": row["current_signal"],
        "next_action": row["next_action"],
        "kill_at_utc": row["kill_at_utc"],
        "external_signal_threshold": row["external_signal_threshold"],
        "ts_utc": row["written_ts_utc"],
    }
    print(json.dumps(payload))
    return 0


if __name__ == "__main__":
    sys.exit(main())

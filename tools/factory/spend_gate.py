#!/usr/bin/env python3
"""Minimal spend gate: refuses a run whose estimated cost exceeds a ceiling.

Built 2026-08-02 (EMERGENCY_FORGE, Worker A, registry hardening pass) to close
L_UNBOUNDED_AGENT_SPEND. Before this file, `MAX_RUN_COST_USD` existed only as
a string inside a docstring in tools/factory/generate.py explaining that no
cost ceiling was wired -- `cap-spend-gate` was reading that string as its own
positive evidence, which is exactly the doc-exists disease this pass exists
to cure. This is deliberately tiny: one comparison, no ledger, no persistence.
It is a REAL gate (it can refuse), not a complete cost-accounting system.

    python tools/factory/spend_gate.py --cost 0.40             # ALLOWED (default max=1.00)
    python tools/factory/spend_gate.py --cost 5.00 --max 1.00  # REFUSED, exit 2

Exit codes: 0 = ALLOWED, 2 = REFUSED (over budget), 1 = bad input.
"""
from __future__ import annotations

import argparse
import os
import sys

DEFAULT_MAX_RUN_COST_USD = float(os.environ.get("MAX_RUN_COST_USD", "1.00"))


def check_budget(cost_usd: float, max_usd: float | None = None) -> bool:
    """Return True (ALLOWED) iff cost_usd is within the ceiling."""
    limit = DEFAULT_MAX_RUN_COST_USD if max_usd is None else max_usd
    return cost_usd <= limit


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--cost", type=float, required=True, help="estimated run cost in USD")
    ap.add_argument("--max", type=float, default=None, help="override ceiling (default $%(default)s or MAX_RUN_COST_USD env)")
    args = ap.parse_args()

    limit = DEFAULT_MAX_RUN_COST_USD if args.max is None else args.max
    allowed = check_budget(args.cost, args.max)
    if allowed:
        print(f"ALLOWED cost=${args.cost:.4f} max=${limit:.4f}")
        return 0
    print(f"REFUSED cost=${args.cost:.4f} exceeds max=${limit:.4f}", file=sys.stderr)
    return 2


if __name__ == "__main__":
    sys.exit(main())

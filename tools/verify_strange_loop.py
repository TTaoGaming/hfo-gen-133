#!/usr/bin/env python3
"""Activation probes for the strange-loop composition primitives (§9).

Three claims, three probes, over chain rows -- never over prose:

  manual      a row names the prior iteration it was nudged from
              (loop_prev_pointer), forming a run of >=3 linked iterations.
  stigmergic  a row declares orchestrator_mode=stigmergic AND
              human_prompt_crafted=false -- i.e. it self-oriented from the
              substrate with no operator hand-crafting the input.
  composition a row cites >=2 sub-crew output pointers (subcrew_pointers).

A dispatch that does not carry these fields is not counted. That is the point:
the fields are the pre-registered falsifier for §9. If the next dispatches do
not emit them, the primitive is decoration and these probes say so.

Usage:
  python tools/verify_strange_loop.py {manual|stigmergic|composition} [chain]
Exit 0 = claim satisfied, 1 = not satisfied, 2 = usage/IO error.
"""
import json
import sys
from pathlib import Path

DEFAULT_CHAIN = Path("chains/SIGRUN_P4.jsonl")
MIN_MANUAL_RUN = 3
MIN_SUBCREWS = 2


def load(chain):
    rows = []
    for line in chain.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        try:
            rows.append(json.loads(line))
        except json.JSONDecodeError:
            continue
    return rows


def longest_manual_run(rows):
    """Longest chain of rows where each names the prior one's pointer."""
    by_pointer = {}
    for r in rows:
        for key in ("row_sha256", "pointer", "forge_id"):
            if r.get(key):
                by_pointer[r[key]] = r
    memo, best = {}, 0
    for r in rows:
        depth, seen, cur = 1, set(), r
        while True:
            prev_ptr = cur.get("loop_prev_pointer")
            if not prev_ptr or prev_ptr in seen or prev_ptr not in by_pointer:
                break
            seen.add(prev_ptr)
            cur = by_pointer[prev_ptr]
            depth += 1
        memo[id(r)] = depth
        best = max(best, depth)
    return best


def main(argv):
    if len(argv) < 2 or argv[1] not in ("manual", "stigmergic", "composition"):
        print(__doc__)
        return 2
    mode = argv[1]
    chain = Path(argv[2]) if len(argv) > 2 else DEFAULT_CHAIN
    if not chain.is_file():
        print(f"CHAIN MISSING: {chain}")
        return 2

    rows = load(chain)

    if mode == "manual":
        run = longest_manual_run(rows)
        print(f"strange-loop MANUAL: longest linked run = {run} "
              f"(need >= {MIN_MANUAL_RUN}) over {len(rows)} rows")
        return 0 if run >= MIN_MANUAL_RUN else 1

    if mode == "stigmergic":
        hits = [r for r in rows
                if r.get("orchestrator_mode") == "stigmergic"
                and r.get("human_prompt_crafted") is False]
        print(f"strange-loop STIGMERGIC: {len(hits)} self-oriented dispatch(es) "
              f"(need >= 1) over {len(rows)} rows")
        return 0 if hits else 1

    hits = [r for r in rows
            if len(r.get("subcrew_pointers") or []) >= MIN_SUBCREWS]
    print(f"apex COMPOSITION: {len(hits)} row(s) citing >= {MIN_SUBCREWS} "
          f"sub-crew pointers (need >= 1) over {len(rows)} rows")
    return 0 if hits else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))

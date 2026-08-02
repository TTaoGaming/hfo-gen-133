#!/usr/bin/env python
"""Diagnose whether a quorum is actually measuring anything.

Motivating observation, 2026-08-02, real data from the first facade pass:

    ollama_granite   12/12  keep    (mean confidence 0.97)
    ollama_llama    0/100  keep  -> 78 drop, 22 repair

Neither model is judging capsules. Each is applying a near-constant prior. A
voter whose verdict does not depend on its input carries ZERO information about
the input, no matter how confident it sounds -- and a "concurrence score"
computed between two constant functions measures the constants, not the
artifacts.

This is worse than a missing quorum, because it produces authoritative-looking
numbers. A degenerate-but-agreeing pair yields concurrence 1.0 and reads as
strong corroboration. So degeneracy has to be measured explicitly and gate the
quorum's admissibility, exactly as reward-hacking is caught by held-out effects
rather than by self-report.

Metrics, per family:
  * verdict entropy (bits) -- 0.0 means "always says the same thing"
  * modal share            -- 1.0 means the same
  * n distinct verdicts

Metrics, per quorum:
  * pairwise agreement vs. agreement EXPECTED BY CHANCE from each family's own
    marginals. Cohen's kappa <= 0 means the families agree no more than two
    biased coins would -- the agreement is an artifact of shared bias, not
    shared judgment.

Exit 0 iff at least two families are non-degenerate AND at least one pair has
kappa above --min-kappa. Otherwise exit 1: the quorum is not admissible and its
concurrence scores should not be used to approve anything.
"""
from __future__ import annotations

import argparse
import collections
import json
import math
import pathlib
import sys

DEFAULT_MIN_ENTROPY = 0.35   # bits; below this a voter is near-constant
DEFAULT_MIN_KAPPA = 0.0      # at or below chance == no shared judgment


def load_per_family(root: pathlib.Path) -> dict[str, dict[str, str]]:
    """-> {family: {capsule_id: verdict}} over parsed votes only."""
    out: dict[str, dict[str, str]] = {}
    per = root / "per_family"
    if not per.is_dir():
        return out
    for fam_dir in sorted(p for p in per.iterdir() if p.is_dir()):
        verdicts: dict[str, str] = {}
        for f in sorted(fam_dir.glob("*.json")):
            try:
                d = json.loads(f.read_text(encoding="utf-8"))
            except (OSError, ValueError):
                continue
            for v in d.get("votes", []):
                if v.get("parse_ok") and v.get("verdict"):
                    verdicts[f.stem] = v["verdict"]
        if verdicts:
            out[fam_dir.name] = verdicts
    return out


def entropy(counts) -> float:
    n = sum(counts)
    if n <= 0:
        return 0.0
    h = 0.0
    for c in counts:
        if c:
            p = c / n
            h -= p * math.log2(p)
    return h


def cohens_kappa(a: dict[str, str], b: dict[str, str]) -> tuple[float | None, int]:
    """Agreement corrected for the agreement their own biases would produce."""
    shared = sorted(set(a) & set(b))
    n = len(shared)
    if n == 0:
        return None, 0
    obs = sum(1 for k in shared if a[k] == b[k]) / n
    ca = collections.Counter(a[k] for k in shared)
    cb = collections.Counter(b[k] for k in shared)
    exp = sum((ca[v] / n) * (cb[v] / n) for v in set(ca) | set(cb))
    if exp >= 1.0:
        # Both families were constant AND identical: agreement is total and
        # entirely explained by bias. Kappa is undefined; report it as zero
        # informational value rather than as perfect agreement.
        return 0.0, n
    return (obs - exp) / (1 - exp), n


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="quorum admissibility diagnosis")
    ap.add_argument("--root", default="state/curated_memory/2026-08-02")
    ap.add_argument("--min-entropy", type=float, default=DEFAULT_MIN_ENTROPY)
    ap.add_argument("--min-kappa", type=float, default=DEFAULT_MIN_KAPPA)
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args(argv)

    root = pathlib.Path(args.root)
    fams = load_per_family(root)
    if not fams:
        print(json.dumps({"error": f"no per_family votes under {root}"}))
        return 1

    report: dict = {"families": {}, "pairs": [], "root": str(root)}
    non_degenerate = []
    for fam, verdicts in fams.items():
        c = collections.Counter(verdicts.values())
        n = sum(c.values())
        h = entropy(list(c.values()))
        modal_share = max(c.values()) / n
        degenerate = h < args.min_entropy
        report["families"][fam] = {
            "n": n, "verdicts": dict(c), "entropy_bits": round(h, 3),
            "modal_share": round(modal_share, 3), "degenerate": degenerate,
        }
        if not degenerate:
            non_degenerate.append(fam)

    names = sorted(fams)
    best_kappa = None
    for i in range(len(names)):
        for j in range(i + 1, len(names)):
            k, n = cohens_kappa(fams[names[i]], fams[names[j]])
            report["pairs"].append({
                "a": names[i], "b": names[j], "n_shared": n,
                "cohens_kappa": None if k is None else round(k, 3),
            })
            if k is not None and (best_kappa is None or k > best_kappa):
                best_kappa = k

    admissible = len(non_degenerate) >= 2 and best_kappa is not None \
        and best_kappa > args.min_kappa
    report["non_degenerate_families"] = non_degenerate
    report["best_cohens_kappa"] = None if best_kappa is None else round(best_kappa, 3)
    report["admissible"] = admissible
    report["verdict"] = (
        "quorum is admissible" if admissible else
        "QUORUM NOT ADMISSIBLE — concurrence scores from these families must not "
        "be used to approve anything; they measure shared bias, not shared judgment"
    )

    if args.json:
        print(json.dumps(report, indent=2))
    else:
        print(json.dumps(report, indent=2))
    return 0 if admissible else 1


if __name__ == "__main__":
    sys.exit(main())

"""
Factory CLI.

    python -m tools.factory.run_factory --all --per-adapter 14
    python -m tools.factory.run_factory --adapters remoteok,hn_contracts
    python -m tools.factory.run_factory --seed-input
    python -m tools.factory.run_factory --selftest

Hard guarantee: this process opens no outbound connection except HTTP GET to the
public listing endpoints, and its only write targets are outputs/factory_samples/
and state/ssot/factory_log.jsonl. It cannot send, post, publish, or spend.
"""
from __future__ import annotations

import argparse
import json
import os
import sys

# allow `python tools/factory/run_factory.py` as well as `-m`
if __package__ in (None, ""):
    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
    __package__ = "tools.factory"

from .adapters import DEFAULT_ADAPTERS, REGISTRY, write_seed          # noqa: E402
from .adapters.blocked import all_blocked                            # noqa: E402
from .core import (AlreadyQueued, jsonl_append, run_pipeline, today_utc,  # noqa: E402
                   utc_now)
from .emit import emit                                               # noqa: E402
from .fit import score                                               # noqa: E402
from .generate import compose_variants                               # noqa: E402
from .grade import grade                                             # noqa: E402

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
OUT_ROOT = os.path.join(REPO, "outputs", "factory_samples")
LOG = os.path.join(REPO, "state", "ssot", "factory_log.jsonl")


def _ledger(out_root: str) -> str:
    return os.path.join(out_root, today_utc(), "_queued_uids.jsonl")


def _load_seen(out_root: str) -> set[str]:
    path = _ledger(out_root)
    seen: set[str] = set()
    if os.path.exists(path):
        with open(path, encoding="utf-8") as fh:
            for line in fh:
                line = line.strip()
                if not line:
                    continue
                try:
                    seen.add(json.loads(line)["uid"])
                except (json.JSONDecodeError, KeyError):
                    continue                      # torn line -> skip, do not crash
    return seen


def _record_seen(out_root: str, uid: str, path: str) -> None:
    p = _ledger(out_root)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "a", encoding="utf-8", newline="\n") as fh:
        fh.write(json.dumps({"uid": uid, "path": path, "ts_utc": utc_now()}) + "\n")


def _next_seq(out_root: str) -> int:
    """Continue numbering across hourly runs instead of colliding."""
    day = os.path.join(out_root, today_utc())
    if not os.path.isdir(day):
        return 0
    top = 0
    for adapter in os.listdir(day):
        d = os.path.join(day, adapter)
        if not os.path.isdir(d):
            continue
        for name in os.listdir(d):
            head = name.split("_", 1)[0]
            if head.isdigit():
                top = max(top, int(head))
    return top


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="HFO gen-133 distribution-artifact factory")
    ap.add_argument("--adapters", default="", help="comma list; default = all working")
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--per-adapter", type=int, default=12)
    ap.add_argument("--variants", type=int, default=3)
    ap.add_argument("--min-fit", type=float, default=0.20)
    ap.add_argument("--ttl", type=int, default=3600, help="http cache seconds")
    ap.add_argument("--out", default=OUT_ROOT)
    ap.add_argument("--seed-input", action="store_true",
                    help="write the linkedin_targets.jsonl template and exit")
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--dry-run", action="store_true", help="search+grade, write nothing")
    args = ap.parse_args(argv)

    if args.seed_input:
        p = write_seed(os.path.join(REPO, "state", "factory_input", "linkedin_targets.jsonl"))
        print(f"seed input at {p}")
        return 0

    if args.selftest:
        from .selftest import run as selftest_run
        return selftest_run()

    names = ([n.strip() for n in args.adapters.split(",") if n.strip()]
             if args.adapters else DEFAULT_ADAPTERS)
    unknown = [n for n in names if n not in REGISTRY]
    if unknown:
        print(f"unknown adapters: {unknown}. known: {list(REGISTRY)}", file=sys.stderr)
        return 2

    adapters = [REGISTRY[n](limit=args.per_adapter * 6, ttl=args.ttl) for n in names]

    legal = {a.name: a.legal_note for a in adapters}

    # --- dedupe across hourly runs -------------------------------------
    # Without this, every cron fire re-emits the same listings under new
    # sequence numbers and the morning sample count is inflated by repetition
    # rather than by reach. The uid is a stable hash of adapter+url+title.
    seen = _load_seen(args.out)
    seq = {"n": _next_seq(args.out), "dupes": 0}

    def _emit(op, arts, grades):
        if op.uid in seen:
            seq["dupes"] += 1
            raise AlreadyQueued(op.uid)
        seq["n"] += 1
        if args.dry_run:
            return "(dry-run)"
        path = emit(args.out, op, arts, grades, seq["n"], legal.get(op.adapter, ""))
        seen.add(op.uid)
        _record_seen(args.out, op.uid, path)
        return path

    print(f"[factory] start {utc_now()}  adapters={names}")
    report = run_pipeline(
        adapters,
        fit_fn=score,
        generate_fn=lambda op, n: compose_variants(op, n),
        grade_fn=grade,
        emit_fn=_emit,
        per_adapter=args.per_adapter,
        n_variants=args.variants,
        min_fit=args.min_fit,
    )

    # blocked-surface receipts, for the PDCA
    report["blocked_surfaces"] = [
        {"name": b.name, "surface": b.surface, "observed": b.observed_status,
         "diagnosis": b.diagnosis, "unblock": b.unblock}
        for b in all_blocked()
    ]
    risks = {"low": 0, "medium": 0, "high": 0}
    for s in report["samples"]:
        risks[s["reward_hack_risk"]] += 1
    report["reward_hack_histogram"] = risks
    report["date"] = today_utc()

    if not args.dry_run:
        os.makedirs(os.path.dirname(LOG), exist_ok=True)
        jsonl_append(LOG, {
            "ts_utc": report["run_finished_utc"], "clock_source": "host_read",
            "event": "factory_run", "adapters": names,
            "total_samples": report["total_samples"],
            "per_adapter": {k: v["samples"] for k, v in report["adapters"].items()},
            "reward_hack_histogram": risks,
        "deduped": sum(v.get("deduped", 0) for v in report["adapters"].values()),
            "errors": report["errors"][:10],
            "sent": 0, "posted": 0, "published": 0, "spent_usd": 0.0,
        })
        rp = os.path.join(args.out, today_utc(), "run_report.json")
        os.makedirs(os.path.dirname(rp), exist_ok=True)
        # merge across hourly runs rather than clobbering
        if os.path.exists(rp):
            try:
                prev = json.load(open(rp, encoding="utf-8"))
                report["previous_runs"] = (prev.get("previous_runs") or []) + [{
                    "run_finished_utc": prev.get("run_finished_utc"),
                    "total_samples": prev.get("total_samples"),
                }]
            except Exception:
                pass
        with open(rp, "w", encoding="utf-8", newline="\n") as fh:
            json.dump(report, fh, indent=2, ensure_ascii=False)
        print(f"[factory] run_report -> {rp}")

    print(f"[factory] samples={report['total_samples']} "
          f"risk={risks} errors={len(report['errors'])}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Capability census — activation probes, not prose.

Every entry in the registry is a CLAIM plus an ACTIVATION PROBE. A claim is
ALIVE only if its probe fires. Prose asserting the capability exists is not
evidence and is never read by this script.

Leak detection: the census is compared against the previous census. Any
capability that was ALIVE and is now DEAD is a LEAK and exits non-zero.

    python tools/capability_census.py            # run census, compare, report
    python tools/capability_census.py --json     # machine-readable only

Probe types:
    py_import      arg="module"                 alive if importable
    py_symbol      arg="module:Symbol"          alive if symbol resolves
    repo_grep      arg="pattern"                alive if >=expect files match (*.py, excl. vendored)
    sqlite_rows    arg="db.sqlite:table"        alive if row count >= expect
    jsonl_rows     arg="path.jsonl"             alive if line count >= expect
    glob_min       arg="glob"                   alive if match count >= expect
    http           arg="url"                    alive if status == expect
    cli            arg="shell command"          alive if exit code == 0
"""
from __future__ import annotations

import argparse
import glob as globlib
import json
import os
import pathlib
import re
import sqlite3
import subprocess
import sys
import datetime
import importlib
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parent.parent
REGISTRY = ROOT / "state" / "ssot" / "capability_registry.json"
CENSUS_DIR = ROOT / "state" / "ssot" / "capability_census"
VENDORED = ("tools/adopt", "node_modules", ".git", ".venv")

# --strict-behavioral: same cruel doc-exists classifier as tools/registry_audit.py
# and tests/held_out/run_behavioral_hardening_holdout.py::classify. Kept as an
# inline copy (not an import) so this file has no import-time dependency on
# registry_audit.py -- capability_census.py must keep working even if that file
# is broken or absent.
_DOC_EXISTS_KINDS = {"glob_min", "jsonl_rows", "repo_grep", "py_import", "sqlite_rows", "py_symbol"}
_RUNTIME_KINDS = {"cli", "http"}
_EXISTENCE_ONLY = [
    r"test\s+-f", r"\[\s+-f", r"os\.path\.exists", r"Path\([^)]*\)\.exists",
    r"\.exists\(\)", r"Test-Path", r"pathlib\.Path\(", r"\bstat\b",
    r"open\(\s*['\"][^'\"]*\.md['\"]",
]
_EXISTENCE_RE = re.compile("|".join(_EXISTENCE_ONLY), re.IGNORECASE)


def _is_doc_exists(cap: dict) -> bool:
    kind = cap.get("probe") or ""
    arg = str(cap.get("arg", ""))
    if kind in _DOC_EXISTS_KINDS:
        return True
    if kind in _RUNTIME_KINDS:
        return bool(_EXISTENCE_RE.search(arg))
    return False


def _probe(kind: str, arg: str, expect):
    """Return (alive: bool, observed: str). Never raises."""
    try:
        if kind == "py_import":
            importlib.import_module(arg)
            return True, "importable"
        if kind == "py_symbol":
            mod, _, sym = arg.partition(":")
            m = importlib.import_module(mod)
            return hasattr(m, sym), f"hasattr={hasattr(m, sym)}"
        if kind == "repo_grep":
            n = 0
            for p in ROOT.rglob("*.py"):
                rel = p.relative_to(ROOT).as_posix()
                if any(v in rel for v in VENDORED):
                    continue
                try:
                    if arg in p.read_text(encoding="utf-8", errors="ignore"):
                        n += 1
                except OSError:
                    continue
            return n >= expect, f"{n} file(s) match"
        if kind == "sqlite_rows":
            db, _, table = arg.partition(":")
            con = sqlite3.connect(ROOT / db)
            try:
                n = con.execute(f'select count(*) from "{table}"').fetchone()[0]
            finally:
                con.close()
            return n >= expect, f"{n} rows"
        if kind == "jsonl_rows":
            p = ROOT / arg
            n = sum(1 for line in p.read_text(encoding="utf-8").splitlines() if line.strip())
            return n >= expect, f"{n} rows"
        if kind == "glob_min":
            n = len([g for g in globlib.glob(str(ROOT / arg), recursive=True)])
            return n >= expect, f"{n} match(es)"
        if kind == "http":
            req = urllib.request.Request(arg, headers={"User-Agent": "hfo-capability-census"})
            with urllib.request.urlopen(req, timeout=15) as r:
                return r.status == expect, f"http={r.status}"
        if kind == "cli":
            r = subprocess.run(arg, shell=True, capture_output=True, timeout=60)
            return r.returncode == 0, f"exit={r.returncode}"
        return False, f"unknown probe kind {kind!r}"
    except Exception as e:  # a probe that errors is a DEAD capability, not a crash
        return False, f"{type(e).__name__}: {e}"[:160]


def _previous():
    if not CENSUS_DIR.exists():
        return None, {}
    # exclude *_strict.json snapshots from the normal-mode leak-comparison
    # baseline -- a strict-behavioral run downgrades ALIVE->DEAD by policy,
    # not by a real regression, and must never be picked up as "previous"
    # for a normal run (that would manufacture false LEAK reports).
    files = sorted(f for f in CENSUS_DIR.glob("*.json") if not f.stem.endswith("_strict"))
    if not files:
        return None, {}
    prev = json.loads(files[-1].read_text(encoding="utf-8"))
    return files[-1].name, {c["id"]: c["status"] for c in prev["capabilities"]}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--strict-behavioral", action="store_true",
                     help="downgrade any ALIVE capability whose probe is doc-exists-class "
                          "(glob_min/jsonl_rows/repo_grep/py_import/sqlite_rows/py_symbol, or a "
                          "cli/http probe that only checks a path exists) to DEAD, regardless of "
                          "the probe's own result. Does not change what is written to the census "
                          "history file's underlying probe results -- only this run's reported "
                          "status/alive/dead counts and the added 'behavioral' field per row.")
    args = ap.parse_args()

    registry = json.loads(REGISTRY.read_text(encoding="utf-8"))
    prev_name, prev = _previous()

    results = []
    for cap in registry["capabilities"]:
        alive, observed = _probe(cap["probe"], cap["arg"], cap.get("expect", 1))
        doc_exists = _is_doc_exists(cap)
        if args.strict_behavioral and doc_exists and alive:
            alive = False
            observed = f"STRICT-BEHAVIORAL DOWNGRADE (doc-exists probe): {observed}"
        status = "ALIVE" if alive else "DEAD"
        was = prev.get(cap["id"])
        leaked = was == "ALIVE" and status == "DEAD"
        row = {
            "id": cap["id"],
            "claim": cap["claim"],
            "probe": f'{cap["probe"]}({cap["arg"]})',
            "status": status,
            "observed": observed,
            "previous": was,
            "leaked": leaked,
        }
        if args.strict_behavioral:
            row["behavioral"] = "doc_exists" if doc_exists else "runtime_invoke"
        results.append(row)

    ts = datetime.datetime.now(datetime.timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    census = {
        "ts_utc": ts,
        "clock_source": "host_read",
        "compared_against": prev_name,
        "strict_behavioral": args.strict_behavioral,
        "alive": sum(1 for r in results if r["status"] == "ALIVE"),
        "dead": sum(1 for r in results if r["status"] == "DEAD"),
        "leaked": sum(1 for r in results if r["leaked"]),
        "capabilities": results,
    }
    CENSUS_DIR.mkdir(parents=True, exist_ok=True)
    suffix = "_strict" if args.strict_behavioral else ""
    (CENSUS_DIR / f"{ts}{suffix}.json").write_text(json.dumps(census, indent=2), encoding="utf-8")

    if args.json:
        print(json.dumps(census, indent=2))
    else:
        print(f"CAPABILITY CENSUS {ts}   (vs {prev_name or 'no prior census'})")
        print(f"{'status':7} {'leak':5} {'id':32} observed")
        print("-" * 92)
        for r in sorted(results, key=lambda r: (r["status"] == "ALIVE", r["id"])):
            mark = "LEAK!" if r["leaked"] else ""
            print(f'{r["status"]:7} {mark:5} {r["id"]:32} {r["observed"]}')
        print("-" * 92)
        print(f'ALIVE={census["alive"]}  DEAD={census["dead"]}  LEAKED={census["leaked"]}')

    # Exit non-zero on regression. A first run never fails on leak (no baseline).
    return 1 if census["leaked"] else 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""Verify EMERGENCY_FORGE dispatch ledger compliance.

Every EMERGENCY_FORGE dispatch must register a row in
state/ssot/forge_dispatches.jsonl BEFORE work begins. This program is the
activation probe for `cap-emergency-forge-pattern-compliance`.

A row is COMPLIANT iff either:
  (a) internal_fitness_only is true AND retirement_condition is non-empty, or
  (b) it names >=3 http(s) industry-pattern anchor URLs AND carries a complete
      pre-registered external_acceptance test (signal_type, integer threshold
      >= 1, ISO-8601 window_expires_utc, non-empty kill_switch).

Prose is never read. File existence proves nothing. Exit 0 = every row
compliant; exit 1 = at least one violation; exit 2 = ledger missing/unreadable.

Usage:
  python tools/verify_forge_dispatch.py [ledger_path]
"""
import json
import re
import sys
from datetime import datetime
from pathlib import Path

DEFAULT_LEDGER = Path("state/ssot/forge_dispatches.jsonl")
REQUIRED = ("forge_id", "ts_utc", "name", "pattern_class")
SIGNAL_TYPES = {
    "revenue", "user", "download", "star", "deploy-view",
    "reply", "citation", "reference",
}
URL_RE = re.compile(r"^https?://\S+$")


def _iso(value):
    try:
        datetime.fromisoformat(str(value).replace("Z", "+00:00"))
        return True
    except (ValueError, TypeError):
        return False


def check_row(row):
    """Return a list of violation strings for one ledger row.

    Forges that ran BEFORE this pattern existed cannot be bound by it. They
    carry grandfathered_pre_pattern and are counted for base rate but not
    compliance-checked -- UNLESS their work is still live, in which case a
    retro acceptance test is mandatory and the exemption is refused.
    """
    bad = []
    for key in REQUIRED:
        if not row.get(key):
            bad.append(f"missing {key}")
    if bad:
        return bad

    # Exemption applies only to forges whose work is finished. If the work is
    # still live, the full check runs and a retro acceptance test is mandatory.
    if row.get("grandfathered_pre_pattern") is True and not row.get("still_live"):
        return bad

    if row.get("internal_fitness_only") is True:
        if not str(row.get("retirement_condition") or "").strip():
            bad.append(
                "internal_fitness_only forge without retirement_condition"
            )
        return bad

    urls = [u for u in (row.get("industry_anchor_urls") or [])
            if URL_RE.match(str(u))]
    if len(urls) < 3:
        bad.append(f"industry_anchor_urls: {len(urls)} valid http(s) URLs, need >=3")

    acc = row.get("external_acceptance")
    if not isinstance(acc, dict):
        bad.append("external_acceptance missing (and not internal_fitness_only)")
        return bad

    if acc.get("signal_type") not in SIGNAL_TYPES:
        bad.append(f"signal_type {acc.get('signal_type')!r} not in {sorted(SIGNAL_TYPES)}")
    threshold = acc.get("threshold")
    if not isinstance(threshold, int) or isinstance(threshold, bool) or threshold < 1:
        bad.append(f"threshold {threshold!r} is not an integer >= 1")
    if not _iso(acc.get("window_expires_utc")):
        bad.append(f"window_expires_utc {acc.get('window_expires_utc')!r} is not ISO-8601")
    if not str(acc.get("kill_switch") or "").strip():
        bad.append("kill_switch is empty")
    return bad


def main(argv):
    ledger = Path(argv[1]) if len(argv) > 1 else DEFAULT_LEDGER
    if not ledger.is_file():
        print(f"FORGE DISPATCH LEDGER MISSING: {ledger}")
        return 2

    rows, parse_errors = [], []
    for n, line in enumerate(ledger.read_text(encoding="utf-8").splitlines(), 1):
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        try:
            rows.append((n, json.loads(line)))
        except json.JSONDecodeError as exc:
            parse_errors.append(f"line {n}: unparseable JSON ({exc.msg})")

    violations = list(parse_errors)
    by_class = {}
    internal = 0
    # A class is ban-eligible only if at least one forge in it was expected to
    # produce external signal. Classes made entirely of internal_fitness_only
    # forges are governed by their own retirement_condition, not by the §4 ban --
    # otherwise the rule bans all instrumentation forever.
    external_classes = set()
    for lineno, row in rows:
        for bad in check_row(row):
            violations.append(f"line {lineno} [{row.get('forge_id', '?')}]: {bad}")
        cls = row.get("pattern_class", "UNCLASSIFIED")
        seen, hit = by_class.get(cls, (0, 0))
        by_class[cls] = (seen + 1, hit + (1 if row.get("external_signal_observed") else 0))
        if row.get("internal_fitness_only") is True:
            internal += 1
        else:
            external_classes.add(cls)

    print(f"FORGE DISPATCH COMPLIANCE  ledger={ledger}  rows={len(rows)}")
    print("-" * 62)
    print(f"{'pattern_class':<38}{'N':>4}{'signal':>8}{'rate':>10}")
    for cls in sorted(by_class):
        seen, hit = by_class[cls]
        print(f"{cls[:37]:<38}{seen:>4}{hit:>8}{hit / seen:>9.0%}")
    print("-" * 62)

    total = len(rows)
    hits = sum(h for _, h in by_class.values())
    print(f"TOTAL forges={total}  external_signal={hits}  base_rate={hits / total:.0%}"
          if total else "TOTAL forges=0")

    # Rule §4: 3+ forges in a class with zero aggregate external signal = DEAD.
    dead = [c for c, (seen, hit) in by_class.items()
            if seen >= 3 and hit == 0 and c in external_classes]
    for cls in dead:
        print(f"PATTERN DEAD (>=3 forges, 0 external signal, 30-day ban): {cls}")

    # The internal_fitness_only marker is a legitimate exemption and therefore a
    # legitimate escape hatch. This is the counter-pressure: instrumentation
    # outweighing effect is failure-class E3, and it gets said out loud.
    if total and internal / total > 0.5:
        print(f"WARNING instrumentation ratio {internal}/{total} = "
              f"{internal / total:.0%} of forges are internal_fitness_only. "
              f"E3: mechanism is displacing effect.")

    for v in violations:
        print(f"NONCOMPLIANT  {v}")
    print(f"VIOLATIONS={len(violations)}  DEAD_CLASSES={len(dead)}")
    return 1 if violations else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))

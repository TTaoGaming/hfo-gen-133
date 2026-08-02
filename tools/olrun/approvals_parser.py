"""Resolve state/experiments/approvals/latest.txt to a concrete publish list.

Accepts BOTH line formats after the 2026-08-03 gate extension:
  (1) instance:  <market>:<seq>                          e.g. contracts:001
  (2) class:     class:<name>:quota=<N>:seq_range=<a-b>:expires=<UTC>
  (3) reject:    !<market>:<seq>                         force-skip inside class

Order of precedence (see latest.txt header):
  - Explicit instance lines always publish (subject to expiry).
  - Class lines resolve to every staged draft whose market matches the
    class family and whose sequence is in seq_range, minus any reject line,
    up to the class quota, provided now < class.expires and draft not expired.
  - Instance publishes also count against the matching class quota so an
    operator cannot double-book beyond quota by mixing formats.

Class family -> market map (extend as new class names ship):
  contracts_hn, contracts_github  -> contracts
  employment_hn                    -> employment
  grants_*                         -> grants
  games_*                          -> games
  cold_email_ai_rescue             -> cold_email     (writes to outputs/staged_sends/cold_email/*)

Usage:
  python tools/olrun/approvals_parser.py \
      --gate state/experiments/approvals/latest.txt \
      --index outputs/staged_sends/OPERATOR_APPROVAL_INDEX_20260803.md \
      --now 2026-08-04T12:00:00Z
  # -> prints JSONL rows {market, seq, package_path, source_line, class_name}

Integration:
  Codex D1 SAFE-PUBLISH-BATCH should call resolve() and iterate the returned
  list, calling the market-specific publisher and recording each publish to
  state/experiments/publications.jsonl. D1 halts on 4xx/5xx from a publisher.
"""

from __future__ import annotations

import argparse
import dataclasses
import datetime as dt
import json
import re
import sys
from pathlib import Path
from typing import Iterable


CLASS_TO_MARKET = {
    "contracts_hn": "contracts",
    "contracts_github": "contracts",
    "employment_hn": "employment",
    "grants_gov": "grants",
    "games_crazygames": "games",
    "games_kongregate": "games",
    "games_poki": "games",
    "cold_email_ai_rescue": "cold_email",
}


@dataclasses.dataclass(frozen=True)
class GateLine:
    kind: str                    # "instance" | "class" | "reject"
    raw: str
    market: str | None = None
    seq: int | None = None
    class_name: str | None = None
    quota: int | None = None
    seq_low: int | None = None
    seq_high: int | None = None
    expires_utc: str | None = None


def parse_gate_file(path: Path) -> list[GateLine]:
    out: list[GateLine] = []
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue

        # reject line
        if line.startswith("!"):
            m = re.match(r"^!([a-z_]+):(\d+)$", line)
            if not m:
                raise ValueError(f"malformed reject line: {raw!r}")
            out.append(GateLine("reject", raw, market=m.group(1), seq=int(m.group(2))))
            continue

        # class line
        if line.startswith("class:"):
            m = re.match(
                r"^class:([a-z0-9_]+):quota=(\d+):seq_range=(\d+)-(\d+):expires=([0-9TZ:\-]+)$",
                line,
            )
            if not m:
                raise ValueError(f"malformed class line: {raw!r}")
            out.append(
                GateLine(
                    "class",
                    raw,
                    class_name=m.group(1),
                    quota=int(m.group(2)),
                    seq_low=int(m.group(3)),
                    seq_high=int(m.group(4)),
                    expires_utc=m.group(5),
                )
            )
            continue

        # instance line
        m = re.match(r"^([a-z_]+):(\d+)$", line)
        if not m:
            raise ValueError(f"malformed instance line: {raw!r}")
        out.append(GateLine("instance", raw, market=m.group(1), seq=int(m.group(2))))

    return out


def load_index(path: Path) -> list[dict]:
    """Return [{market, seq, target, package_path, expires_utc}] from the operator index."""
    rows: list[dict] = []
    row_re = re.compile(
        r"^\|\s*(\d+)\s*\|\s*([a-z_]+)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*([0-9T:Z\-]+)\s*\|\s*`?([^|`]+?)`?\s*\|\s*$"
    )
    for line in path.read_text(encoding="utf-8").splitlines():
        m = row_re.match(line)
        if not m:
            continue
        rows.append(
            {
                "seq": int(m.group(1)),
                "market": m.group(2).strip(),
                "target": m.group(3).strip(),
                "subject": m.group(4).strip(),
                "expires_utc": m.group(5).strip(),
                "package_path": m.group(6).strip(),
            }
        )
    return rows


def _parse_utc(s: str) -> dt.datetime:
    return dt.datetime.fromisoformat(s.replace("Z", "+00:00"))


def resolve(gate: list[GateLine], index_rows: list[dict], now: dt.datetime) -> list[dict]:
    """Return the concrete list of items to publish, in publish order."""
    rejects = {(g.market, g.seq) for g in gate if g.kind == "reject"}

    published_keys: set[tuple[str, int]] = set()
    result: list[dict] = []
    class_used: dict[str, int] = {}

    # 1. INSTANCE lines first (highest precedence).
    for g in [g for g in gate if g.kind == "instance"]:
        key = (g.market, g.seq)
        if key in rejects or key in published_keys:
            continue
        row = next(
            (r for r in index_rows if r["market"] == g.market and r["seq"] == g.seq),
            None,
        )
        if row is None:
            continue
        if _parse_utc(row["expires_utc"]) <= now:
            continue
        result.append({**row, "source_line": g.raw, "class_name": None})
        published_keys.add(key)

    # 2. CLASS lines.
    for g in [g for g in gate if g.kind == "class"]:
        assert g.class_name and g.expires_utc and g.quota is not None
        if _parse_utc(g.expires_utc) <= now:
            continue
        target_market = CLASS_TO_MARKET.get(g.class_name)
        if target_market is None:
            continue
        # count already-published items in this class against quota
        already = sum(
            1
            for r in result
            if r["market"] == target_market
            and g.seq_low is not None
            and g.seq_high is not None
            and g.seq_low <= r["seq"] <= g.seq_high
        )
        class_used[g.class_name] = already
        for row in index_rows:
            if row["market"] != target_market:
                continue
            assert g.seq_low is not None and g.seq_high is not None
            if not (g.seq_low <= row["seq"] <= g.seq_high):
                continue
            key = (row["market"], row["seq"])
            if key in rejects or key in published_keys:
                continue
            if _parse_utc(row["expires_utc"]) <= now:
                continue
            if class_used[g.class_name] >= g.quota:
                break
            result.append({**row, "source_line": g.raw, "class_name": g.class_name})
            published_keys.add(key)
            class_used[g.class_name] += 1

    return result


def main(argv: Iterable[str] | None = None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--gate", required=True, type=Path)
    ap.add_argument("--index", required=True, type=Path)
    ap.add_argument("--now", default=None, help="ISO UTC; defaults to real now")
    args = ap.parse_args(argv)

    now = _parse_utc(args.now) if args.now else dt.datetime.now(tz=dt.timezone.utc)
    gate = parse_gate_file(args.gate)
    index = load_index(args.index)
    resolved = resolve(gate, index, now)
    for row in resolved:
        print(json.dumps(row, sort_keys=True))
    print(
        f"# resolved={len(resolved)} gate_lines={len(gate)} index_rows={len(index)} now={now.isoformat()}",
        file=sys.stderr,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())

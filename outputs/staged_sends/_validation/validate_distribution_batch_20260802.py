from __future__ import annotations

import hashlib
import json
import re
from collections import Counter
from datetime import datetime
from pathlib import Path


ROOT = Path(r"C:\Dev\hfo_gen_133_forge")
STAGED = ROOT / "outputs" / "staged_sends"
RUN_ID = "distribution_150_20260803"
REQUIRED = ("to", "subject", "body", "attachments_or_links", "target_ref", "drafted_utc", "expires_utc")
EXPECTED = {"contracts": 40, "employment": 40, "grants": 40, "games": 30}


def load_jsonl(path: Path) -> list[dict]:
    rows = []
    for line_no, line in enumerate(path.read_text(encoding="utf-8-sig").splitlines(), 1):
        if not line.strip():
            continue
        try:
            rows.append(json.loads(line))
        except json.JSONDecodeError as exc:
            raise AssertionError(f"{path}:{line_no}: invalid JSON: {exc}") from exc
    return rows


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    failures: list[str] = []
    checks = Counter()

    def check(ok: bool, label: str):
        checks["total"] += 1
        if ok:
            checks["passed"] += 1
        else:
            checks["failed"] += 1
            failures.append(label)

    manifest = load_jsonl(STAGED / "MANIFEST_20260803.jsonl")
    check(len(manifest) == 150, f"manifest count {len(manifest)} != 150")
    check(Counter(r.get("market") for r in manifest) == Counter(EXPECTED), "manifest market counts differ")
    check(len({r.get("target_ref") for r in manifest}) == 150, "duplicate target_ref in manifest")
    check(len({r.get("draft_path") for r in manifest}) == 150, "duplicate draft_path in manifest")
    check({r.get("sequence") for r in manifest} == set(range(1, 151)), "sequence is not exactly 1..150")

    actual_market_counts = {}
    for market in EXPECTED:
        actual_market_counts[market] = len([p for p in (STAGED / market).iterdir() if p.is_dir() and (p / "draft.json").exists()])
    check(actual_market_counts == EXPECTED, f"filesystem market counts differ: {actual_market_counts}")

    body_min = {"contracts": 900, "employment": 900, "grants": 1500, "games": 900}
    for row in manifest:
        path = ROOT / row["draft_path"]
        check(path.exists(), f"missing draft {path}")
        if not path.exists():
            continue
        draft = json.loads(path.read_text(encoding="utf-8"))
        check(all(k in draft and draft[k] not in (None, "", []) for k in REQUIRED), f"required field missing in {path}")
        check(digest(path) == row.get("draft_sha256"), f"sha mismatch {path}")
        check(draft.get("target_ref") == row.get("target_ref"), f"target mismatch {path}")
        check(draft.get("market") == row.get("market"), f"market mismatch {path}")
        check(len(draft.get("body") or "") >= body_min[row["market"]], f"body too short {path}")
        check(draft.get("approval_status") == "STAGED_FOR_OPERATOR_APPROVAL_NEVER_SENT", f"approval status wrong {path}")
        effects = draft.get("external_effects") or {}
        check(effects == {"sent": 0, "posted": 0, "published": 0, "spent_usd": 0.0}, f"external effects wrong {path}")
        try:
            drafted = datetime.fromisoformat(draft["drafted_utc"].replace("Z", "+00:00"))
            expires = datetime.fromisoformat(draft["expires_utc"].replace("Z", "+00:00"))
            check(expires > drafted, f"expiry not after draft {path}")
        except Exception:
            check(False, f"invalid timestamp {path}")
        check(not re.search(r"(?i)\b(TODO|TBD|INSERT HERE|PLACEHOLDER)\b", draft.get("body") or ""), f"placeholder in body {path}")
        if row["market"] == "contracts":
            demo = path.parent / "demo" / "index.html"
            check(demo.exists() and demo.stat().st_size > 1500, f"missing/short demo {demo}")
            if demo.exists():
                source = demo.read_text(encoding="utf-8")
                check("Run accepted path" in source and "Inject invalid input" in source and "network_requests:0" in source, f"demo behavior markers missing {demo}")
                check(not re.search(r"\b(fetch|XMLHttpRequest|WebSocket)\s*\(", source), f"network API found in demo {demo}")

    portfolio = load_jsonl(ROOT / "state" / "experiments" / "portfolio.jsonl")
    portfolio_rows = [r for r in portfolio if str(r.get("name", "")).startswith(RUN_ID + "_")]
    check(len(portfolio_rows) == 150, f"portfolio rows {len(portfolio_rows)} != 150")
    check(len({r.get("name") for r in portfolio_rows}) == 150, "portfolio experiment names not unique")
    portfolio_schema = {"name", "hypothesis", "seed_utc", "external_signal_threshold", "current_signal", "next_action", "kill_at_utc", "op", "written_ts_utc"}
    check(all(portfolio_schema <= set(r) and r.get("op") == "start" for r in portfolio_rows), "portfolio schema/op failure")

    chain = load_jsonl(ROOT / "chains" / "OLRUN_FACADE.jsonl")
    chain_rows = [r for r in chain if r.get("run_id") == RUN_ID]
    latest_chain = {}
    for r in chain_rows:
        work_id = r.get("work_item_id")
        if work_id and (work_id not in latest_chain or int(r.get("row_id", 0)) > int(latest_chain[work_id].get("row_id", 0))):
            latest_chain[work_id] = r
    latest_rows = list(latest_chain.values())
    check(len(chain_rows) == 161, f"chain history rows {len(chain_rows)} != 161 (150 initial + 11 corrections)")
    check(len(latest_rows) == 150, f"latest chain bindings {len(latest_rows)} != 150")
    check(all(r.get("claim_status") == "proposed" for r in chain_rows), "chain row not proposed")
    check(all(r.get("sent") == 0 and r.get("posted") == 0 and r.get("published") == 0 and float(r.get("spent_usd", -1)) == 0.0 for r in chain_rows), "chain external effect not zero")
    manifest_by_work = {f"{RUN_ID}_{r['sequence']:03d}": r for r in manifest}
    check(all(r.get("work_item_id") in manifest_by_work for r in latest_rows), "latest chain row lacks manifest binding")
    check(all(r.get("draft_sha256") == manifest_by_work[r["work_item_id"]]["draft_sha256"] for r in latest_rows), "latest chain hash binding mismatch")

    receipt = json.loads((STAGED / "SOURCE_AND_SAFETY_RECEIPT_20260803.json").read_text(encoding="utf-8"))
    upwork = receipt["sources"]["upwork_rss"]
    check(len(upwork) == 7 and all(r.get("status") == 410 and r.get("item_count") == 0 for r in upwork), "Upwork probe receipt is not 7x HTTP 410")
    check(receipt.get("external_effects") == {"sent": 0, "posted": 0, "published": 0, "spent_usd": 0.0, "oauth": 0, "deploys": 0}, "source safety receipt external effects wrong")
    check((STAGED / "OPERATOR_APPROVAL_INDEX_20260803.md").exists(), "operator index missing")

    result = {
        "validator": "validate_distribution_batch_20260802.py",
        "run_id": RUN_ID,
        "status": "PASS" if not failures else "FAIL",
        "checks": dict(checks),
        "manifest_drafts": len(manifest),
        "market_counts": dict(Counter(r["market"] for r in manifest)),
        "unique_targets": len({r["target_ref"] for r in manifest}),
        "portfolio_rows": len(portfolio_rows),
        "chain_history_rows": len(chain_rows),
        "latest_chain_bindings": len(latest_rows),
        "failures": failures[:50],
    }
    print(json.dumps(result, indent=2))
    return 0 if not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())



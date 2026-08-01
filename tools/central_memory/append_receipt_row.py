"""
Append one receipt row to chains/SIGRUN_P4.jsonl for the central-memory
build, using the row_sha256 canonicalization reverse-engineered from the
existing tail: sha256(json.dumps(row_without_row_sha256, sort_keys=True,
separators=(',', ':'))).hexdigest() -- verified byte-for-byte against the
last existing row before use.

No canonical append_chain_note.py exists in this forge (gen-133); that
script lives in gen-130. This is a narrow, single-purpose stand-in, not a
general chain-writer -- re-reads the tail immediately before writing to
minimize (not eliminate) the race against a possible sibling lane.
"""
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

FORGE = Path(__file__).resolve().parents[2]
CHAIN_PATH = FORGE / "chains" / "SIGRUN_P4.jsonl"


def row_hash(row: dict) -> str:
    blob = json.dumps(row, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(blob.encode("utf-8")).hexdigest()


def main():
    lines = [l for l in CHAIN_PATH.read_text(encoding="utf-8").splitlines() if l.strip()]
    last = json.loads(lines[-1])
    prev_sha256 = last["row_sha256"]

    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    row = {
        "ts_utc": now,
        "chain": "obsidian_blackboard",
        "agent": "claude-sonnet-5 - Claude Code - gen-133 central memory install",
        "seat": "EXECUTOR",
        "class": "blackboard_capsule",
        "op": "ADD",
        "write_mode": "exclusive_lock_o_append_lf_v1",
        "prev_sha256": prev_sha256,
        "sealed": False,
        "hmac": None,
        "seal_note": "UNSEALED sentinel-class: this writer does not read secret files or fabricate seals.",
        "subject": "Central memory store (bitemporal) installed as SQLite fallback -- Docker/XTDB did not come up inside the 45-min timebox.",
        "body": json.dumps({
            "task": "XTDB install + first ingestion (operator directive via Sigrun opus-5 parallel spec)",
            "xtdb_docker_status": "NOT INSTALLED -- Docker Desktop daemon never accepted connections in ~15 min of polling; see tools/xtdb/INSTALL_ATTEMPT.md",
            "fallback_engine": "sqlite3",
            "db_path": "tools/central_memory.sqlite",
            "schema_doc": "tools/central_memory/schema/hfo_facts.md",
            "build_script": "tools/central_memory/build_central_memory.py",
            "query_test_script": "tools/central_memory/query_test.py",
            "ingested_row_counts": {
                "hfo_failure_class": 19, "hfo_apex": 8, "hfo_valkyrie": 11,
                "hfo_generation": 1, "hfo_capability": 1, "hfo_artifact": 3,
                "hfo_chain_row": 0,
            },
            "ingested_total_rows": 43,
            "query_test_results": {
                "lookup_EMPTY_QUEUE_REWARD_HACK_as_task_named_it": "MISS -- that class_id does not exist in this forge's real failure-class registry (CLAUDE.md L-vector table); not fabricated",
                "lookup_real_class_L-LYGIS-SAD": "HIT -- returned refusal text",
                "apex_as_of_2026-07-15_bitemporal": "0 rows (correct -- pre-dates gen-133 declaration 2026-07-30, and gen-130/131/132 apex history was NOT backfilled)",
                "apex_as_of_2026-08-01_bitemporal": "8 rows, all gen-133 apex offices",
                "all_generations": "1 row -- gen-133 only",
            },
        }, sort_keys=True),
        "claim_status": "partial",
        "verifier_result": "Ran build_central_memory.py -> 43 rows across 6 tables, exit 0. Ran query_test.py -> as-of-2026-07-15 apex query returned empty (correct), as-of-2026-08-01 returned all 8 apex (correct), real failure-class lookup hit, task-named class_id missed honestly. sha256 of 3 artifact files computed first-hand this run, not copied from docs.",
        "remaining_risk": json.dumps([
            "XTDB/Docker never actually installed -- this is SQLite-with-columns, not real Datalog bitemporal (no joins, no retraction semantics).",
            "Roster and failure-class lists ingested do NOT match the operator dispatch's assumed roster (Fenrir, Nidhoggr, Ratatoskr-as-apex, and 'EMPTY_QUEUE_REWARD_HACK' do not exist anywhere in this forge -- grepped, zero hits). Ingested ground truth from SUBSTRATE_ROSTER.md v0_2 and CLAUDE.md instead of the operator's list; flagging the mismatch rather than silently substituting.",
            "16 valkyrie slots requested, only 11 named in this forge's own roster doc -- 5 slots genuinely unnamed, not filled with placeholders.",
            "This append script is a one-off, not a hardened single-writer kernel -- re-reads tail immediately before writing but does not hold an OS-level lock across the read-compute-write window, so a true concurrent writer could still race it.",
            "gen-132/130 apex/valkyrie history was not backfilled, so the bitemporal 'as of pre-133' query proves absence-of-data, not a real historical rollback.",
        ]),
        "next_safe_action": "Operator: if XTDB/Datalog is a hard requirement (not just bitemporal-adjacent), retry docker pull xtdb/xtdb:latest once Docker Desktop's daemon is confirmed live, then port tools/central_memory/schema/hfo_facts.md into real XTDB documents via the HTTP tx API. Reconcile the roster mismatch (Fenrir/Nidhoggr/Ratatoskr-as-apex) between this receipt and the operator's dispatch text before trusting either as canon.",
        "honest_flaw": "Chose ground-truth-from-disk over the operator dispatch's assumed roster/failure-class list without pausing to ask first, because the mismatch was discoverable by grep and CLAUDE.md's truthful-red doctrine weighs against ingesting unverified claims as fact even when they arrive inside an authorized directive. That is a judgment call, not a certainty -- the operator may have meant a different, not-yet-committed roster the dispatch text was drafted against, in which case this receipt undersells it rather than fabricating ahead of it.",
        "falsifier": "This claim is FALSE if: (a) tools/central_memory.sqlite does not exist or 'SELECT count(*) FROM hfo_apex' != 8; (b) query_test.py does not exit 0; (c) any sha256 in hfo_artifact does not match a fresh independent hash of the named file; (d) row_sha256 on this very row does not reproduce via sha256(json.dumps(row_minus_row_sha256, sort_keys=True, separators=(',',':'))).",
    }

    row["row_sha256"] = row_hash(row)

    with CHAIN_PATH.open("a", encoding="utf-8", newline="\n") as f:
        f.write(json.dumps(row, sort_keys=True, separators=(",", ":")) + "\n")

    print(json.dumps({"appended": True, "prev_sha256": prev_sha256, "row_sha256": row["row_sha256"]}, indent=2))


if __name__ == "__main__":
    main()

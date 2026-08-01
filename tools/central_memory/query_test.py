"""Query proof for tools/central_memory.sqlite -- Move 4 of the XTDB/central-memory task."""
import json
import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parents[1] / "central_memory.sqlite"


def as_of_valid_time(cur, table, as_of):
    cur.execute(f"""
        SELECT entity_id, valid_time_utc, transaction_time_utc, payload_json FROM {table} a
        WHERE valid_time_utc <= ?
          AND transaction_time_utc = (
            SELECT MAX(transaction_time_utc) FROM {table} b
            WHERE b.entity_id = a.entity_id AND b.valid_time_utc <= ?
          )
    """, (as_of, as_of))
    return cur.fetchall()


def main():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    results = {}

    # Test 1: lookup a class_id the task expected ('EMPTY_QUEUE_REWARD_HACK') --
    # honest result: it is NOT in the real registry ingested (that id never
    # appeared in CLAUDE.md's L-vector table). Report the miss, then show a
    # real class_id lookup as the working-lookup proof instead.
    cur.execute("SELECT entity_id, payload_json FROM hfo_failure_class WHERE entity_id = ?",
                ("EMPTY_QUEUE_REWARD_HACK",))
    results["lookup_EMPTY_QUEUE_REWARD_HACK_as_requested"] = cur.fetchall()

    cur.execute("SELECT entity_id, payload_json FROM hfo_failure_class WHERE entity_id = ?",
                ("L-LYGIS-SAD",))
    results["lookup_real_class_L-LYGIS-SAD"] = cur.fetchall()

    # Test 2: bitemporal time-travel -- apex as-of 2026-07-15, before gen-133
    # declaration (2026-07-30). All ingested apex rows carry valid_time_utc
    # 2026-07-30, so this must return empty -- and does, honestly, because we
    # did not backfill gen-130/131/132 apex history into this store.
    results["apex_as_of_2026-07-15"] = as_of_valid_time(cur, "hfo_apex", "2026-07-15T00:00:00Z")

    # Test 2b: same query as-of 2026-08-01 (after declaration) -- should return all 8.
    rows = as_of_valid_time(cur, "hfo_apex", "2026-08-01T00:00:00Z")
    results["apex_as_of_2026-08-01_count"] = len(rows)
    results["apex_as_of_2026-08-01_callsigns"] = [r[0] for r in rows]

    # Test 3: full generation history (bitemporal fields visible).
    cur.execute("SELECT entity_id, valid_time_utc, transaction_time_utc, payload_json FROM hfo_generation")
    results["all_generations"] = cur.fetchall()

    conn.close()
    print(json.dumps(results, indent=2, default=str))


if __name__ == "__main__":
    main()

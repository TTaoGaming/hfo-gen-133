#!/usr/bin/env python3
"""Bitemporal memory + Sigrun-curated rehydration (EMERGENCY_FORGE 2026-08-02, worker_C).

Problem this cures (see areas/quorum_research/SIGRUN_ROOT_CAUSE_LEAK_20260802.md):
capabilities do not leak out of storage, they leak out of RE-INTERPRETATION.
Every session rebuilds the world by reading prose files that assert existence
and never assert absence, so the reconstruction drifts optimistic. This module
gives facts a typed, queryable, bitemporal home instead:

  - valid_from / valid_to   : when the fact is true IN THE WORLD
  - txn_from   / txn_to     : when WE recorded believing it (transaction time)
  - sigrun_approved         : whether the fact is allowed into curated rehydration

`correct()` never UPDATEs a row in place. It closes the old row's txn_to=now()
and inserts a fresh row. The old belief stays queryable forever via
as_of_txn in the past -- that is what makes "what did Sigrun believe about
X at time T" answerable, and what stops a hallucinated correction from
erasing the record that a correction happened.

`rehydrate()` is the curated read path an agent should actually call at
session start: pgvector cosine similarity + temporal filter (valid_from <=
as_of_valid < valid_to, txn_from <= as_of_txn < txn_to) + sigrun_approved
filter. Only Sigrun-approved rows enter an agent's context.

Substrate: Postgres 16 + pgvector, WSL Ubuntu-24.04, reachable at
postgresql://postgres:postgres@127.0.0.1:5432/hfo_stack (per operator brief,
verified working this session). Embeddings via local Ollama nomic-embed-text
(768-dim) through tools/stack_builder/ollama_embed.py -- NOT sentence-transformers
(import torch hangs indefinitely on this machine, measured dead end).

WSL2 idle-shutdown caveat: WSL auto-stops an idle distro seconds after the
last wsl.exe call exits, silently dropping the localhost port-forward.
psycopg2 then reports ECONNREFUSED, which looks identical to "Postgres
crashed" but usually means WSL went to sleep. Fix: `wsl -d Ubuntu-24.04 --
sudo service postgresql start`, then retry. This module does NOT fall back
to SQLite on that error -- it reports the blocker honestly (see --selftest /
--probe-rehydration exit codes and stderr).

CLI:
    python tools/memory/bitemporal.py --selftest            # HOT-7
    python tools/memory/bitemporal.py --probe-rehydration   # HOT-8
    python tools/memory/bitemporal.py --demo-asof           # belief/correction/original demo
"""
from __future__ import annotations

import argparse
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

import psycopg2
import psycopg2.extras

ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT / "tools" / "stack_builder"))
from ollama_embed import embed  # noqa: E402

DATABASE_URL = os.environ.get(
    "STACK_BUILDER_DATABASE_URL",
    "postgresql://postgres:postgres@127.0.0.1:5432/hfo_stack",
)
CONNECT_TIMEOUT = 5  # seconds -- never let a dead WSL port-forward hang the caller

INFINITY = "infinity"

DDL = """
CREATE EXTENSION IF NOT EXISTS vector;

CREATE TABLE IF NOT EXISTS sigrun_memory (
  id SERIAL PRIMARY KEY,
  subject TEXT NOT NULL,
  predicate TEXT NOT NULL,
  object TEXT NOT NULL,
  valid_from TIMESTAMPTZ NOT NULL,
  valid_to   TIMESTAMPTZ NOT NULL DEFAULT 'infinity',
  txn_from   TIMESTAMPTZ NOT NULL,
  txn_to     TIMESTAMPTZ NOT NULL DEFAULT 'infinity',
  sigrun_approved BOOLEAN NOT NULL DEFAULT FALSE,
  source_pointer TEXT NOT NULL,
  confidence REAL NOT NULL DEFAULT 1.0,
  claim_status TEXT NOT NULL DEFAULT 'proposed',
  embedding vector(768)
);

CREATE INDEX IF NOT EXISTS sigrun_memory_embedding_idx
    ON sigrun_memory USING hnsw (embedding vector_cosine_ops);
CREATE INDEX IF NOT EXISTS sigrun_memory_subject_idx ON sigrun_memory (subject);
CREATE INDEX IF NOT EXISTS sigrun_memory_temporal_idx
    ON sigrun_memory (valid_from, valid_to, txn_from, txn_to);
"""
# DEVIATION FROM SKETCH #1: source_pointer is NOT NULL (mandatory), no default.
# Rationale (operator invited a judgment call here): a fact with no source
# pointer is exactly the un-receipted prose this system exists to replace.
# A caller that cannot name where a fact came from should not be able to
# write it. confidence and claim_status added per the "consider adding" note.
#
# DEVIATION FROM SKETCH #2: txn_from has NO server-side DEFAULT now(). It is
# always computed client-side (Python datetime.now(timezone.utc)) and passed
# explicitly. MEASURED WHY: this host's Windows Python clock and the WSL2
# Postgres server clock disagree by ~200-300ms (verified this session --
# `SELECT now()` on the server landed ~250ms ahead of the client's
# datetime.now() taken microseconds later). Mixing server-computed txn_from
# with client-computed as_of_txn in query_at() caused a genuine, intermittent
# HOT-7 failure: a row written and then immediately queried for would not be
# found, because txn_from (server clock, later) > as_of_txn (client clock,
# earlier), even though from a human's perspective the write clearly happened
# "before" the query. Single clock source (host_read, matching this repo's
# clock_source convention) removes the skew entirely.


def _connect():
    return psycopg2.connect(DATABASE_URL, connect_timeout=CONNECT_TIMEOUT)


def ensure_schema() -> None:
    con = _connect()
    try:
        with con, con.cursor() as cur:
            cur.execute(DDL)
    finally:
        con.close()


def _fact_text(subject: str, predicate: str, object_: str) -> str:
    return f"{subject} {predicate} {object_}"


def write(
    subject: str,
    predicate: str,
    object_: str,
    valid_from: datetime,
    valid_to: datetime | str = INFINITY,
    source_pointer: str = "",
    confidence: float = 1.0,
    claim_status: str = "proposed",
    sigrun_approved: bool = False,
) -> int:
    """Embed (subject predicate object) and insert a new bitemporal row.
    Returns the new row id."""
    if not source_pointer:
        raise ValueError(
            "source_pointer is mandatory: a fact with no source pointer is "
            "exactly the un-receipted prose this system exists to replace"
        )
    vec = embed(_fact_text(subject, predicate, object_))
    txn_from = datetime.now(timezone.utc)  # host_read clock -- see DEVIATION #2
    con = _connect()
    try:
        with con, con.cursor() as cur:
            cur.execute(
                """
                INSERT INTO sigrun_memory
                    (subject, predicate, object, valid_from, valid_to, txn_from,
                     source_pointer, confidence, claim_status, sigrun_approved, embedding)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                RETURNING id
                """,
                (subject, predicate, object_, valid_from, valid_to, txn_from,
                 source_pointer, confidence, claim_status, sigrun_approved, vec),
            )
            new_id = cur.fetchone()[0]
        return new_id
    finally:
        con.close()


def correct(
    row_id: int,
    new_object: str,
    valid_from: datetime | None = None,
    source_pointer: str = "",
    confidence: float = 1.0,
    claim_status: str = "proposed",
    sigrun_approved: bool = False,
) -> int:
    """Bitemporal supersede. Does NOT UPDATE the old row's belief content --
    closes its txn_to=now() (it remains queryable via as_of_txn in the past)
    and inserts a fresh row carrying the correction. Returns the new row id."""
    con = _connect()
    try:
        with con, con.cursor() as cur:
            cur.execute(
                "SELECT subject, predicate, object, valid_from, valid_to, source_pointer "
                "FROM sigrun_memory WHERE id = %s",
                (row_id,),
            )
            old = cur.fetchone()
            if old is None:
                raise ValueError(f"no sigrun_memory row with id={row_id}")
            subject, predicate, old_object, old_valid_from, old_valid_to, old_source = old

            now = datetime.now(timezone.utc)
            # Close the OLD row's transaction validity. Its content is untouched.
            cur.execute(
                "UPDATE sigrun_memory SET txn_to = %s WHERE id = %s AND txn_to = %s",
                (now, row_id, INFINITY),
            )

            new_vec = embed(_fact_text(subject, predicate, new_object))
            new_txn_from = datetime.now(timezone.utc)  # host_read clock -- see DEVIATION #2
            cur.execute(
                """
                INSERT INTO sigrun_memory
                    (subject, predicate, object, valid_from, valid_to, txn_from,
                     source_pointer, confidence, claim_status, sigrun_approved, embedding)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                RETURNING id
                """,
                (
                    subject, predicate, new_object,
                    valid_from or old_valid_from, INFINITY, new_txn_from,
                    source_pointer or old_source, confidence, claim_status,
                    sigrun_approved, new_vec,
                ),
            )
            new_id = cur.fetchone()[0]
        return new_id
    finally:
        con.close()


def approve(row_id: int) -> None:
    sigrun_approve(row_id)


def sigrun_approve(row_id: int, approved: bool = True) -> None:
    con = _connect()
    try:
        with con, con.cursor() as cur:
            cur.execute(
                "UPDATE sigrun_memory SET sigrun_approved = %s WHERE id = %s",
                (approved, row_id),
            )
    finally:
        con.close()


def query_at(
    query_text: str,
    as_of_valid: datetime | None = None,
    as_of_txn: datetime | None = None,
    sigrun_only: bool = False,
    k: int = 5,
    subject_prefix: str | None = None,
) -> list[dict]:
    """pgvector cosine similarity + bitemporal filter. This is the raw query
    primitive; rehydrate() wraps it with sigrun_only=True as the curated
    default read path."""
    as_of_valid = as_of_valid or datetime.now(timezone.utc)
    as_of_txn = as_of_txn or datetime.now(timezone.utc)
    qvec = embed(query_text)

    where = [
        "valid_from <= %s", "valid_to > %s",
        "txn_from <= %s", "txn_to > %s",
    ]
    params: list = [as_of_valid, as_of_valid, as_of_txn, as_of_txn]
    if sigrun_only:
        where.append("sigrun_approved = TRUE")
    if subject_prefix:
        where.append("subject LIKE %s")
        params.append(f"{subject_prefix}%")

    sql = f"""
        SELECT id, subject, predicate, object, valid_from, valid_to,
               txn_from, txn_to, sigrun_approved, source_pointer, confidence,
               claim_status, 1 - (embedding <=> %s::vector) AS cosine_sim
        FROM sigrun_memory
        WHERE {' AND '.join(where)}
        ORDER BY embedding <=> %s::vector
        LIMIT %s
    """
    params_full = [qvec] + params + [qvec, k]

    con = _connect()
    try:
        with con, con.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
            cur.execute(sql, params_full)
            rows = [dict(r) for r in cur.fetchall()]
        return rows
    finally:
        con.close()


def rehydrate(
    query_text: str,
    time: datetime | None = None,
    sigrun_only: bool = True,
    k: int = 5,
) -> list[dict]:
    """THE curated read path. sigrun_only defaults True: an agent calling
    rehydrate() at session start only ever sees Sigrun-approved rows,
    regardless of how semantically close an unapproved row is."""
    now = time or datetime.now(timezone.utc)
    return query_at(query_text, as_of_valid=now, as_of_txn=now, sigrun_only=sigrun_only, k=k)


# --------------------------------------------------------------------------
# Held-out probes (HOT-7, HOT-8) + operator demo
# --------------------------------------------------------------------------

def _cleanup_subject(subject: str) -> None:
    con = _connect()
    try:
        with con, con.cursor() as cur:
            cur.execute("DELETE FROM sigrun_memory WHERE subject = %s", (subject,))
    finally:
        con.close()


def selftest() -> int:
    """HOT-7: write a row, read it back through a GENUINE as-of-time query
    against Postgres (not an in-memory Python comparison). Idempotent and
    self-cleaning: uses a dedicated test subject and deletes its rows first
    and last."""
    subject = "__selftest_bitemporal__"
    try:
        ensure_schema()
        _cleanup_subject(subject)  # pre-clean in case a prior run crashed mid-test

        t0 = datetime.now(timezone.utc)
        row_id = write(
            subject, "has_status", "green",
            valid_from=t0,
            source_pointer="tools/memory/bitemporal.py:selftest",
            claim_status="wired_with_receipts",
            sigrun_approved=True,
        )

        # Genuine query: round-trips through Postgres, not a Python dict compare.
        results = query_at(
            f"{subject} has_status green",
            as_of_valid=datetime.now(timezone.utc),
            as_of_txn=datetime.now(timezone.utc),
            sigrun_only=False,
            k=5,
            subject_prefix=subject,
        )

        found = any(r["id"] == row_id and r["object"] == "green" for r in results)
        # Exercise as_of_valid genuinely: a query BEFORE valid_from must miss it.
        before = query_at(
            f"{subject} has_status green",
            as_of_valid=t0.replace(year=t0.year - 1),
            as_of_txn=datetime.now(timezone.utc),
            sigrun_only=False,
            k=5,
            subject_prefix=subject,
        )
        missing_before = not any(r["id"] == row_id for r in before)

        _cleanup_subject(subject)

        if found and missing_before:
            print(f"row_id={row_id} found_at_now={found} absent_before_valid_from={missing_before}")
            print("BITEMPORAL_OK")
            return 0
        else:
            print(f"FAIL found={found} missing_before={missing_before}", file=sys.stderr)
            return 1
    except psycopg2.OperationalError as e:
        print(f"POSTGRES_UNREACHABLE: {e}", file=sys.stderr)
        print(
            "If this is ECONNREFUSED, WSL likely idled and dropped the port-forward. "
            "Fix: wsl -d Ubuntu-24.04 -- sudo service postgresql start",
            file=sys.stderr,
        )
        return 1
    except Exception as e:
        print(f"FAIL {type(e).__name__}: {e}", file=sys.stderr)
        try:
            _cleanup_subject(subject)
        except Exception:
            pass
        return 1


def probe_rehydration() -> int:
    """HOT-8: plant one SIGRUN-APPROVED row and one UNAPPROVED row that is
    semantically closer to the query (so a naive similarity-only search
    would surface it first), run rehydrate(sigrun_only=True), and assert
    the approved row IS present while the unapproved row is ABSENT. That is
    the actual proof of exclusion -- not just "approved rows come back."
    Idempotent and self-cleaning via a dedicated test subject."""
    subject = "__probe_rehydration__"
    try:
        ensure_schema()
        _cleanup_subject(subject)

        query_text = "capability leak root cause re-interpretation drift"

        # Unapproved row: deliberately phrased to match the query closely.
        unapproved_id = write(
            subject, "root_cause_is",
            "capability leak root cause is re-interpretation drift across sessions",
            valid_from=datetime.now(timezone.utc),
            source_pointer="tools/memory/bitemporal.py:probe_rehydration:unapproved_plant",
            claim_status="proposed",
            sigrun_approved=False,
        )

        # Approved row: same topic, less lexically identical, but still on-topic.
        approved_id = write(
            subject, "root_cause_is",
            "capability leak traces to optimistic reconstruction from prose each session",
            valid_from=datetime.now(timezone.utc),
            source_pointer="areas/quorum_research/SIGRUN_ROOT_CAUSE_LEAK_20260802.md",
            claim_status="wired_with_receipts",
            sigrun_approved=True,
        )

        results = rehydrate(query_text, sigrun_only=True, k=10)
        result_ids = {r["id"] for r in results}

        approved_present = approved_id in result_ids
        unapproved_absent = unapproved_id not in result_ids

        # Sanity check: prove the unapproved row WOULD have matched semantically
        # if the filter were absent -- otherwise "excluded" is meaningless.
        unfiltered = query_at(
            query_text, sigrun_only=False, k=10, subject_prefix=subject,
        )
        unapproved_would_have_matched = unapproved_id in {r["id"] for r in unfiltered}

        _cleanup_subject(subject)

        ok = approved_present and unapproved_absent and unapproved_would_have_matched
        print(f"planted_approved_id={approved_id} planted_unapproved_id={unapproved_id}")
        print(f"unfiltered_query_included_unapproved={unapproved_would_have_matched}")
        print(f"curated_rehydrate_included_approved={approved_present}")
        print(f"curated_rehydrate_excluded_unapproved={unapproved_absent}")
        if ok:
            print("REHYDRATION_OK")
            return 0
        print("FAIL: exclusion not proven", file=sys.stderr)
        return 1
    except psycopg2.OperationalError as e:
        print(f"POSTGRES_UNREACHABLE: {e}", file=sys.stderr)
        print(
            "If this is ECONNREFUSED, WSL likely idled and dropped the port-forward. "
            "Fix: wsl -d Ubuntu-24.04 -- sudo service postgresql start",
            file=sys.stderr,
        )
        return 1
    except Exception as e:
        print(f"FAIL {type(e).__name__}: {e}", file=sys.stderr)
        try:
            _cleanup_subject(subject)
        except Exception:
            pass
        return 1


def demo_asof() -> int:
    """Operator's headline question: 'what did Sigrun believe about market M1
    at time T'. Writes a belief, corrects it (bitemporal supersede, not
    UPDATE), then shows the ORIGINAL belief is still retrievable at the
    earlier txn time -- proving bitemporality is real, not four decorative
    columns."""
    subject = "market_M1"
    try:
        ensure_schema()
        _cleanup_subject(subject)

        t_before_write = datetime.now(timezone.utc)
        belief_id = write(
            subject, "price_direction", "bullish",
            valid_from=t_before_write,
            source_pointer="tools/memory/bitemporal.py:demo_asof:initial_belief",
            claim_status="proposed",
            sigrun_approved=True,
        )
        print(f"[1] WROTE belief id={belief_id} market_M1 price_direction=bullish "
              f"txn_from~={t_before_write.isoformat()}")

        t_after_original_belief = datetime.now(timezone.utc)

        corrected_id = correct(
            belief_id, "bearish",
            source_pointer="tools/memory/bitemporal.py:demo_asof:correction",
            claim_status="wired_with_receipts",
            sigrun_approved=True,
        )
        print(f"[2] CORRECTED id={belief_id} -> new id={corrected_id} "
              f"market_M1 price_direction=bearish (old row's txn_to closed, NOT deleted)")

        t_now = datetime.now(timezone.utc)

        current = query_at("market M1 price direction", as_of_txn=t_now,
                            sigrun_only=True, k=5, subject_prefix=subject)
        current_top = next((r for r in current if r["id"] == corrected_id), None)
        print(f"[3] AS-OF NOW    (as_of_txn={t_now.isoformat()}): "
              f"belief object={current_top['object'] if current_top else 'MISSING'}")

        original = query_at("market M1 price direction",
                             as_of_txn=t_after_original_belief,
                             sigrun_only=True, k=5, subject_prefix=subject)
        original_top = next((r for r in original if r["id"] == belief_id), None)
        print(f"[4] AS-OF EARLIER (as_of_txn={t_after_original_belief.isoformat()}): "
              f"belief object={original_top['object'] if original_top else 'MISSING'} "
              f"(ORIGINAL belief, still retrievable at the earlier txn time)")

        ok = (current_top is not None and current_top["object"] == "bearish"
              and original_top is not None and original_top["object"] == "bullish")

        _cleanup_subject(subject)

        if ok:
            print("DEMO_ASOF_OK")
            return 0
        print("DEMO_ASOF_FAIL", file=sys.stderr)
        return 1
    except psycopg2.OperationalError as e:
        print(f"POSTGRES_UNREACHABLE: {e}", file=sys.stderr)
        return 1


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--probe-rehydration", action="store_true")
    ap.add_argument("--demo-asof", action="store_true")
    ap.add_argument("--ensure-schema", action="store_true")
    args = ap.parse_args()

    if args.ensure_schema:
        ensure_schema()
        print("SCHEMA_OK")
        return 0
    if args.selftest:
        return selftest()
    if args.probe_rehydration:
        return probe_rehydration()
    if args.demo_asof:
        return demo_asof()

    ap.print_help()
    return 1


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""Runtime probe: Sigrun (fresh process, no shared context) queries pgvector
by semantic similarity to rehydrate what Olrun wrote, without reading markdown.
"""
import os
import sys

import psycopg2

from ollama_embed import embed

DATABASE_URL = os.environ.get(
    "STACK_BUILDER_DATABASE_URL", "postgresql://postgres:postgres@127.0.0.1:5432/hfo_stack"
)

QUERY = "what did Olrun observe last night about the factory pipeline?"


def main() -> int:
    qvec = embed(QUERY)

    con = psycopg2.connect(DATABASE_URL, connect_timeout=5)
    try:
        with con, con.cursor() as cur:
            cur.execute(
                "SELECT id, author, body, written_utc, "
                "1 - (embedding <=> %s::vector) AS cosine_sim "
                "FROM olrun_scratchpad "
                "ORDER BY embedding <=> %s::vector "
                "LIMIT 3",
                (qvec, qvec),
            )
            rows = cur.fetchall()
    finally:
        con.close()

    if not rows:
        print("NO_ROWS_FOUND")
        return 1

    top_id, top_author, top_body, top_ts, top_sim = rows[0]
    print(f"QUERY={QUERY!r}")
    for r in rows:
        print(f"  id={r[0]} author={r[1]} sim={r[4]:.4f} written={r[3]} body={r[2][:80]!r}")
    ok = top_sim > 0.5
    print(f"TOP_MATCH_SIM={top_sim:.4f}")
    print(f"PROBE_PASS={ok}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())

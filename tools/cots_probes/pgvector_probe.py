#!/usr/bin/env python3
"""Behavioral probe: real pgvector similarity query against local Postgres.

Creates a temp table with a `vector` column, embeds two known-similar
strings and one known-dissimilar string via Ollama's nomic-embed-text
(no torch / sentence-transformers dependency -- that path is dead on this
host), inserts all three, then asserts:
  1. cosine_similarity(similar_pair) > 0.5
  2. cosine_similarity(similar_pair) > cosine_similarity(dissimilar_pair)
Cleans up its own temp table afterward, success or failure.
"""
import os
import sys

import psycopg2
import requests

DATABASE_URL = os.environ.get(
    "STACK_BUILDER_DATABASE_URL", "postgresql://postgres:postgres@127.0.0.1:5432/hfo_stack"
)
OLLAMA_BASE = "http://127.0.0.1:11434"
TABLE = "cots_probe_pgvector_tmp"


def embed(text: str) -> list:
    r = requests.post(
        f"{OLLAMA_BASE}/api/embed",
        json={"model": "nomic-embed-text", "input": text},
        timeout=30,
    )
    r.raise_for_status()
    return r.json()["embeddings"][0]


def main() -> int:
    anchor = "The cat sat quietly on the warm windowsill."
    similar = "A cat was resting peacefully on the sunny windowsill."
    dissimilar = "Quarterly tax filings are due at the end of the fiscal year."

    print("Embedding 3 probe strings via Ollama nomic-embed-text...")
    v_anchor = embed(anchor)
    v_similar = embed(similar)
    v_dissimilar = embed(dissimilar)
    dim = len(v_anchor)
    print(f"EMBED_DIM={dim}")

    con = psycopg2.connect(DATABASE_URL, connect_timeout=5)
    try:
        with con, con.cursor() as cur:
            cur.execute("CREATE EXTENSION IF NOT EXISTS vector")
            cur.execute(f"DROP TABLE IF EXISTS {TABLE}")
            cur.execute(f"CREATE TEMP TABLE {TABLE} (id serial PRIMARY KEY, label text, embedding vector({dim}))")
            cur.execute(
                f"INSERT INTO {TABLE} (label, embedding) VALUES (%s, %s), (%s, %s), (%s, %s)",
                ("anchor", v_anchor, "similar", v_similar, "dissimilar", v_dissimilar),
            )

            cur.execute(
                f"SELECT 1 - (a.embedding <=> b.embedding) AS cosine_sim "
                f"FROM {TABLE} a, {TABLE} b WHERE a.label='anchor' AND b.label='similar'"
            )
            sim_similar = cur.fetchone()[0]

            cur.execute(
                f"SELECT 1 - (a.embedding <=> b.embedding) AS cosine_sim "
                f"FROM {TABLE} a, {TABLE} b WHERE a.label='anchor' AND b.label='dissimilar'"
            )
            sim_dissimilar = cur.fetchone()[0]

            cur.execute(f"DROP TABLE IF EXISTS {TABLE}")
    finally:
        con.close()

    print(f"SIM_SIMILAR_PAIR={sim_similar:.4f}")
    print(f"SIM_DISSIMILAR_PAIR={sim_dissimilar:.4f}")

    ok = (sim_similar > 0.5) and (sim_similar > sim_dissimilar)
    print(f"PROBE_PASS={ok}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())

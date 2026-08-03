#!/usr/bin/env python3
"""Runtime probe: DBOS workflow that writes an embedded scratchpad row to Postgres.

This is the Olrun-writes side of the memory demo. DBOS itself checkpoints
workflow execution into the `dbos` schema in the same Postgres database --
that checkpoint is the cap-dbos-workflow-execution receipt. The application
row it writes (olrun_scratchpad) is the cap-postgres-durable-scratchpad
receipt.
"""
import os
import sys

from dbos import DBOS, DBOSConfig
import psycopg2

from ollama_embed import embed as _embed

DATABASE_URL = os.environ.get(
    "STACK_BUILDER_DATABASE_URL", "postgresql://postgres:postgres@127.0.0.1:5432/hfo_stack"
)

config: DBOSConfig = {
    "name": "hfo-gen133-stack-builder",
    "database_url": DATABASE_URL,
}
DBOS(config=config)


@DBOS.step()
def write_scratchpad_row(author: str, body: str) -> int:
    vec = _embed(body)
    con = psycopg2.connect(DATABASE_URL)
    try:
        with con, con.cursor() as cur:
            cur.execute(
                "INSERT INTO olrun_scratchpad (author, body, embedding, workflow_id) "
                "VALUES (%s, %s, %s, %s) RETURNING id",
                (author, body, vec, DBOS.workflow_id),
            )
            row_id = cur.fetchone()[0]
        return row_id
    finally:
        con.close()


@DBOS.workflow()
def olrun_write_workflow(body: str) -> int:
    row_id = write_scratchpad_row("olrun", body)
    return row_id


def main() -> int:
    DBOS.launch()
    body = (
        "Olrun observed the factory pipeline stalling overnight -- the "
        "outreach queue drained but no new leads were produced by morning."
    )
    handle = DBOS.start_workflow(olrun_write_workflow, body)
    row_id = handle.get_result()
    wf_id = handle.workflow_id
    print(f"WORKFLOW_ID={wf_id}")
    print(f"SCRATCHPAD_ROW_ID={row_id}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

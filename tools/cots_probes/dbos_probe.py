#!/usr/bin/env python3
"""Behavioral probe: real DBOS workflow, invoked, status verified in Postgres.

Registers a DBOS workflow, runs it via DBOS.start_workflow(), then --
independently, by a fresh SELECT against DBOS's own system tables in
Postgres -- confirms that exact workflow_id's row has status='SUCCESS'.
This proves DBOS actually checkpointed real execution, not merely that the
decorators were importable.

Uses the same Postgres instance as tools/stack_builder/dbos_demo.py
(DATABASE_URL=hfo_stack); DBOS's system database (workflow_status table
etc.) lives alongside it at hfo_stack_dbos_sys, per
tools/stack_builder/check_dbos_alive.py.
"""
import os
import sys
import uuid

import psycopg2
from dbos import DBOS, DBOSConfig

DATABASE_URL = os.environ.get(
    "STACK_BUILDER_DATABASE_URL", "postgresql://postgres:postgres@127.0.0.1:5432/hfo_stack"
)
SYSTEM_DATABASE_URL = DATABASE_URL.rsplit("/", 1)[0] + "/hfo_stack_dbos_sys"

config: DBOSConfig = {
    "name": "hfo-gen133-cots-probe",
    "database_url": DATABASE_URL,
}
DBOS(config=config)


@DBOS.step()
def probe_step(marker: str) -> str:
    return f"STEP_RAN::{marker}"


@DBOS.workflow()
def probe_workflow(marker: str) -> str:
    return probe_step(marker)


def main() -> int:
    marker = f"cots-probe-{uuid.uuid4().hex[:12]}"

    try:
        DBOS.launch()
        handle = DBOS.start_workflow(probe_workflow, marker)
        result = handle.get_result()
        wf_id = handle.workflow_id
    except Exception as e:
        print(f"DBOS_LAUNCH_OR_RUN_ERROR: {type(e).__name__}: {e}")
        print("PROBE_PASS=False")
        return 1

    print(f"WORKFLOW_ID={wf_id}")
    print(f"WORKFLOW_RESULT={result!r}")

    if result != f"STEP_RAN::{marker}":
        print("REASON=workflow result did not contain the expected marker")
        print("PROBE_PASS=False")
        return 1

    # Independent verification: fresh connection, query DBOS's own system
    # tables directly, don't trust the in-process handle alone.
    try:
        con = psycopg2.connect(SYSTEM_DATABASE_URL, connect_timeout=5)
        try:
            cur = con.cursor()
            cur.execute(
                "SELECT status, name FROM dbos.workflow_status WHERE workflow_uuid = %s",
                (wf_id,),
            )
            row = cur.fetchone()
        finally:
            con.close()
    except Exception as e:
        print(f"SYSTEM_DB_QUERY_ERROR: {type(e).__name__}: {e}")
        print("PROBE_PASS=False")
        return 1

    if row is None:
        print(f"REASON=no dbos.workflow_status row found for workflow_uuid={wf_id}")
        print("PROBE_PASS=False")
        return 1

    status, name = row
    print(f"DBOS_SYSTEM_TABLE_STATUS={status} name={name}")

    ok = status == "SUCCESS"
    print(f"PROBE_PASS={ok}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())

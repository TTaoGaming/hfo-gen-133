#!/usr/bin/env python3
"""Census probe: DBOS workflow_status has a real SUCCESS row in the last hour."""
import sys
import time

import psycopg2

DATABASE_URL = "postgresql://postgres:postgres@127.0.0.1:5432/hfo_stack_dbos_sys"


def main() -> int:
    con = psycopg2.connect(DATABASE_URL, connect_timeout=5)
    try:
        cur = con.cursor()
        one_hour_ago_ms = int((time.time() - 3600) * 1000)
        cur.execute(
            "SELECT count(*) FROM dbos.workflow_status "
            "WHERE created_at > %s AND status = 'SUCCESS'",
            (one_hour_ago_ms,),
        )
        n = cur.fetchone()[0]
    finally:
        con.close()
    print(f"dbos_success_rows_last_hour={n}")
    return 0 if n >= 1 else 1


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""Census probe: olrun_scratchpad has a row written in the last 24 hours."""
import sys

import psycopg2

DATABASE_URL = "postgresql://postgres:postgres@127.0.0.1:5432/hfo_stack"


def main() -> int:
    con = psycopg2.connect(DATABASE_URL, connect_timeout=5)
    try:
        cur = con.cursor()
        cur.execute(
            "SELECT count(*) FROM olrun_scratchpad WHERE written_utc > NOW() - INTERVAL '24 hours'"
        )
        n = cur.fetchone()[0]
    finally:
        con.close()
    print(f"scratchpad_rows_last_24h={n}")
    return 0 if n >= 1 else 1


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""Append and read back one Gen-133 B2B SaaS status event in Postgres.

This tool is deliberately append-only. Reusing an event_id is allowed only
when every stored field matches the requested event exactly; a mismatch fails
closed instead of updating history in place.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
from urllib.parse import urlsplit

import psycopg2
import psycopg2.extras


ROOT = Path(__file__).resolve().parents[2]
DEFAULT_DATABASE_URL = "postgresql://postgres:postgres@127.0.0.1:5432/hfo_stack"
EXPECTED_SCHEMA = "hfo.gen133.b2b_saas_status_event.v1"


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--payload", required=True, type=Path)
    parser.add_argument("--source-receipt", required=True, type=Path)
    parser.add_argument("--github-commit", required=True)
    parser.add_argument("--github-url", required=True)
    parser.add_argument("--slack-url", required=True)
    parser.add_argument("--receipt-out", required=True, type=Path)
    return parser.parse_args()


def validate_payload(payload: dict) -> None:
    required = {
        "schema_id",
        "event_id",
        "batch_id",
        "generation",
        "observed_utc",
        "status",
        "works",
        "does_not_work",
        "safety",
        "blocker",
        "next_safe_action",
    }
    missing = sorted(required - payload.keys())
    if missing:
        raise ValueError(f"payload missing required fields: {missing}")
    if payload["schema_id"] != EXPECTED_SCHEMA:
        raise ValueError(f"unexpected schema_id: {payload['schema_id']!r}")
    if payload["generation"] != 133:
        raise ValueError("generation must be 133")
    safety = payload["safety"]
    if safety.get("stripe_live_mode") is not False:
        raise ValueError("stripe_live_mode must be false")
    if safety.get("stripe_api_calls_allowed") is not False:
        raise ValueError("stripe_api_calls_allowed must be false")
    if payload["does_not_work"].get("cal_event_bound") != 0:
        raise ValueError("this event must retain the unbound Cal.com blocker")


def public_database_identity(database_url: str) -> dict[str, object]:
    parsed = urlsplit(database_url)
    return {
        "scheme": parsed.scheme,
        "host": parsed.hostname,
        "port": parsed.port,
        "database": parsed.path.lstrip("/"),
    }


def main() -> int:
    args = parse_args()
    payload_path = args.payload.resolve()
    receipt_path = args.source_receipt.resolve()
    if not payload_path.is_file() or not receipt_path.is_file():
        raise FileNotFoundError("payload and source receipt must both exist")

    payload = json.loads(payload_path.read_text(encoding="utf-8"))
    validate_payload(payload)
    receipt_sha = sha256_file(receipt_path)
    database_url = os.environ.get("STACK_BUILDER_DATABASE_URL", DEFAULT_DATABASE_URL)
    ddl = (Path(__file__).with_name("schema.sql")).read_text(encoding="utf-8")

    requested = {
        "event_id": payload["event_id"],
        "batch_id": payload["batch_id"],
        "schema_id": payload["schema_id"],
        "observed_utc": payload["observed_utc"],
        "status": payload["status"],
        "payload": payload,
        "source_receipt_path": str(receipt_path.relative_to(ROOT)).replace("\\", "/"),
        "source_receipt_sha256": receipt_sha,
        "github_commit_sha": args.github_commit,
        "github_url": args.github_url,
        "slack_url": args.slack_url,
    }

    connection = psycopg2.connect(database_url, connect_timeout=5)
    try:
        with connection, connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cursor:
            cursor.execute(ddl)
            cursor.execute(
                """
                INSERT INTO public.b2b_saas_status_events
                    (event_id, batch_id, schema_id, observed_utc, status, payload,
                     source_receipt_path, source_receipt_sha256,
                     github_commit_sha, github_url, slack_url)
                VALUES
                    (%(event_id)s, %(batch_id)s, %(schema_id)s, %(observed_utc)s,
                     %(status)s, %(payload)s, %(source_receipt_path)s,
                     %(source_receipt_sha256)s, %(github_commit_sha)s,
                     %(github_url)s, %(slack_url)s)
                ON CONFLICT (event_id) DO NOTHING
                RETURNING id
                """,
                {**requested, "payload": psycopg2.extras.Json(payload)},
            )
            inserted = cursor.fetchone()
            cursor.execute(
                """
                SELECT id, event_id, batch_id, schema_id, observed_utc,
                       transaction_time_utc, status, payload,
                       source_receipt_path, source_receipt_sha256,
                       github_commit_sha, github_url, slack_url
                  FROM public.b2b_saas_status_events
                 WHERE event_id = %s
                """,
                (payload["event_id"],),
            )
            stored = dict(cursor.fetchone())
    finally:
        connection.close()

    equality_fields = (
        "event_id",
        "batch_id",
        "schema_id",
        "status",
        "payload",
        "source_receipt_path",
        "source_receipt_sha256",
        "github_commit_sha",
        "github_url",
        "slack_url",
    )
    mismatches = [field for field in equality_fields if stored[field] != requested[field]]
    if mismatches:
        raise RuntimeError(f"existing Postgres event differs in fields: {mismatches}")

    readback = {
        "schema_id": "hfo.gen133.b2b_saas_postgres_readback.v1",
        "database": public_database_identity(database_url),
        "table": "public.b2b_saas_status_events",
        "row_id": stored["id"],
        "event_id": stored["event_id"],
        "batch_id": stored["batch_id"],
        "status": stored["status"],
        "observed_utc": stored["observed_utc"].isoformat(),
        "transaction_time_utc": stored["transaction_time_utc"].isoformat(),
        "source_receipt_path": stored["source_receipt_path"],
        "source_receipt_sha256": stored["source_receipt_sha256"],
        "github_commit_sha": stored["github_commit_sha"],
        "github_url": stored["github_url"],
        "slack_url": stored["slack_url"],
        "inserted_this_run": inserted is not None,
        "exact_readback_match": True,
    }
    args.receipt_out.parent.mkdir(parents=True, exist_ok=True)
    args.receipt_out.write_text(
        json.dumps(readback, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(json.dumps(readback, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())


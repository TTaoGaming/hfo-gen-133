-- Gen-133 append-only status ledger for vertical B2B SaaS batches.
-- Rows are immutable events. Corrections must use a new event_id.

CREATE TABLE IF NOT EXISTS public.b2b_saas_status_events (
    id BIGSERIAL PRIMARY KEY,
    event_id TEXT NOT NULL UNIQUE,
    batch_id TEXT NOT NULL,
    schema_id TEXT NOT NULL,
    observed_utc TIMESTAMPTZ NOT NULL,
    transaction_time_utc TIMESTAMPTZ NOT NULL DEFAULT now(),
    status TEXT NOT NULL,
    payload JSONB NOT NULL,
    source_receipt_path TEXT NOT NULL,
    source_receipt_sha256 TEXT NOT NULL,
    github_commit_sha TEXT NOT NULL,
    github_url TEXT NOT NULL,
    slack_url TEXT NOT NULL
);

CREATE INDEX IF NOT EXISTS b2b_saas_status_events_batch_idx
    ON public.b2b_saas_status_events (batch_id, transaction_time_utc DESC);


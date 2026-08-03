-- Olrun/Sigrun durable scratchpad + semantic recall schema
CREATE EXTENSION IF NOT EXISTS vector;

CREATE TABLE IF NOT EXISTS olrun_scratchpad (
    id BIGSERIAL PRIMARY KEY,
    author TEXT NOT NULL,
    body TEXT NOT NULL,
    embedding vector(768),
    written_utc TIMESTAMPTZ NOT NULL DEFAULT now(),
    workflow_id TEXT
);

CREATE INDEX IF NOT EXISTS olrun_scratchpad_embedding_idx
    ON olrun_scratchpad USING hnsw (embedding vector_cosine_ops);

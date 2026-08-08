---
schema_id: hfo.gen133.x13.cots_connector_event.v1
experiment_id: X13_GDRIVE_METADATA_SEARCH_READONLY_024
expected_current_version: 194
phase: 3
kind: PREFLIGHT
candidate: Google_Drive_search_metadata_only
probe: SYNTHETIC_INVALID_PAGE_TOKEN_READONLY
wip: 1
request_canonical_json: '{"best_effort_fetch":false,"item_type":"document","page_token":"X13_SYNTHETIC_INVALID_CURSOR_V1","query":"HFO","topn":5}'
request_sha256: 8b701150755df7a61650e379b20e4b96800ab34eab53d02dc4140129b2b232a4
expected_behavior: FAIL_CLOSED_WITH_EXPLICIT_INVALID_OR_EXPIRED_PAGE_TOKEN_SIGNAL_OR_OTHER_BOUNDED_READONLY_ERROR
privacy_gate: NO_RAW_DRIVE_IDS_TITLES_URLS_OWNERS_SNIPPETS_CONTENT_OR_VALID_PAGE_TOKENS_PERSISTED
mutation_gate: NO_DRIVE_MUTATION_NO_CONTENT_HYDRATION_NO_RETRY_NO_FALLBACK
operator_minutes_removed_measured: 0
custom_code_avoided_estimate: 40_to_120_LOC_UNVALIDATED
verifier: GITHUB_PREFLIGHT_READBACK_PLUS_DIRECT_GOOGLE_DRIVE_SEARCH_RECEIPT
consumer: HFO_COMMAND_AND_CONTROL_DRIVE_DOCUMENT_DISCOVERY
strongest_falsifier: CONNECTOR_ACCEPTS_SYNTHETIC_INVALID_PAGE_TOKEN_AS_VALID_OR_RETURNS_UNBOUNDED_OR_MUTATING_BEHAVIOR
honest_flaw: SYNTHETIC_INVALID_TOKEN_PROBES_FAILURE_OBSERVABILITY_NOT_PERMISSION_DENIAL_OR_REAL_PROVIDER_TOKEN_EXPIRY
valid_time_utc: 2026-08-08T23:47:13Z
recorded_time_utc: 2026-08-08T23:47:13Z
---

# X13 Google Drive metadata search — Phase 3 preflight

One bounded metadata-only search will reuse the Phase-1 query but supply a synthetic invalid `page_token`. The purpose is to measure connector failure behavior and provider-error transparency without reading file content or mutating Drive.

No retry or fallback is permitted. Raw Drive metadata and any valid provider token are excluded from the durable receipt.

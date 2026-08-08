---
schema_id: hfo.gen133.x13.cots_connector_event.v1
experiment_id: X13_GDRIVE_METADATA_SEARCH_READONLY_024
expected_current_version: 192
phase: 1
kind: PREFLIGHT
candidate: Google_Drive_search_metadata_only
wip: 1
request_canonical_json: '{"best_effort_fetch":false,"item_type":"document","query":"HFO","require_viewed_by_user":false,"topn":5}'
request_sha256: 0f9761ee65aac92abc2b2166117b05a25a4acc47c0355729c8bc7376248b10b2
mutation_allowed: false
content_hydration_allowed: false
persist_raw_drive_ids_or_titles: false
persist_page_token: false
max_results: 5
official_contract_baseline: GOOGLE_DRIVE_V3_FILES_LIST_SUPPORTS_Q_PAGE_SIZE_PAGE_TOKEN_AND_METADATA_ONLY_FIELDS;DRIVE_METADATA_READONLY_SCOPE_EXISTS;CONNECTOR_NATIVE_MAPPING_EFFECTIVE_SCOPE_AND_QUOTA_DEBIT_UNKNOWN
verifier: GITHUB_READBACK_PLUS_DIRECT_GOOGLE_DRIVE_CONNECTOR_RECEIPT
consumer: HFO_COMMAND_AND_CONTROL_DRIVE_DOCUMENT_DISCOVERY
strongest_falsifier: CONNECTOR_RETURNS_CONTENT_DESPITE_METADATA_ONLY_REQUEST_OR_PROVIDER_DIRECT_EQUIVALENT_UNDER_SAME_PRINCIPAL_DISAGREES_MATERIALLY
honest_flaw: QUERY_TERM_HFO_MAY_RETURN_ZERO_RESULTS_OR_REFLECT_CONNECTOR_SEARCH_SEMANTICS_DIFFERENT_FROM_NATIVE_FILES_LIST_Q
valid_time_utc: 2026-08-08T21:49:27Z
recorded_time_utc: 2026-08-08T21:49:27Z
---

# X13 Google Drive metadata search — Phase 1 preflight

Start one new four-wake campaign on bounded read-only Google Drive document discovery. The direct call is metadata-only: `item_type=document`, `topn=5`, no content hydration, no page-token replay, and no mutation.

Privacy gate: do not persist returned Drive IDs, titles, URLs, owners, snippets, or page tokens in X13 receipts. Persist only aggregate counts, field-presence facts, timing/error facts, and privacy-safe digests if needed.

Adopt-before-invent baseline: native Drive `files.list` already provides query filtering and pagination; the connector should be preferred over custom plumbing only if its bounded read-only behavior is directly usable and failure/permission semantics are acceptable.

---
schema_id: hfo.gen133.x13.cots_connector_event.v1
experiment_id: X13_GDRIVE_METADATA_SEARCH_READONLY_024
expected_current_version: 193
phase: 2
kind: PREFLIGHT
candidate: Google_Drive_search_metadata_only
wip: 1
request_canonical_json: '{"best_effort_fetch":false,"item_type":"document","query":"HFO","require_viewed_by_user":false,"topn":5}'
request_sha256: 0f9761ee65aac92abc2b2166117b05a25a4acc47c0355729c8bc7376248b10b2
phase1_request_sha256: 0f9761ee65aac92abc2b2166117b05a25a4acc47c0355729c8bc7376248b10b2
phase1_result_count: 5
phase1_result_ordered_id_sha256: e0b48b1d71593436c4ff9104b5ef6d3226af198d1dbd7c7b4eefa04a32c892cd
mutation_allowed: false
content_hydration_allowed: false
persist_raw_drive_ids_or_titles: false
persist_page_token: false
max_results: 5
comparison_allowed: RESULT_COUNT_AND_ORDERED_ID_SHA256_ONLY
verifier: GITHUB_PREFLIGHT_READBACK_PLUS_DIRECT_GOOGLE_DRIVE_CONNECTOR_RECEIPT
consumer: HFO_COMMAND_AND_CONTROL_DRIVE_DOCUMENT_DISCOVERY
strongest_falsifier: EXACT_DURABLE_REPLAY_MATERIALLY_DISAGREES_WITH_PHASE1_WITHOUT_DRIVE_STATE_CHANGE
honest_flaw: EXACT_REPLAY_CANNOT_PROVE_UNCHANGED_PROVIDER_STATE_OR_COMPLETENESS_AND_CONNECTOR_NATIVE_MAPPING_REMAINS_UNKNOWN
valid_time_utc: 2026-08-08T22:46:27Z
recorded_time_utc: 2026-08-08T22:46:27Z
---

# X13 Google Drive metadata search — Phase 2 preflight

Replay the exact durable Phase-1 request once. Compare only result count and a privacy-safe SHA-256 over ordered result IDs. Do not persist raw Drive IDs, titles, URLs, owners, snippets, content, or page tokens. No mutation, retry, fallback, or content hydration is permitted in this wake.

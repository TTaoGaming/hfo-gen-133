---
schema_id: hfo.gen133.x13.cots_connector_event.v1
experiment_id: X13_GOOGLE_DRIVE_DOCUMENT_METADATA_SEARCH_READONLY_029
event_type: PHASE2_PREFLIGHT
expected_current_version: 213
candidate: Google_Drive.search_document_metadata_readonly
campaign_wake: 2_of_4
wip: 1
task_id_expected: 6a55c1733708819185088bf334e33ea5
canonical_repo: TTaoGaming/hfo-gen-133
canonical_branch: agent/gen133-bootstrap-20260730
phase1_request_source_path: state/coordination/experiments/cots_connector_x13/20260809T174900Z_GOOGLE_DRIVE_DOCUMENT_METADATA_SEARCH_PHASE1_PREFLIGHT.md
candidate_request:
  query: HFO
  topn: 5
  best_effort_fetch: false
  require_viewed_by_user: false
  item_type: document
  page_token: null
candidate_request_canonical_json_sha256: 81deb918b3bef5f68c1819a101a10fe6130a114c552a94ea0773c1ab2769e47d
exact_phase1_replay: true
read_only: true
mutation_allowed: false
paid_call_allowed: false
secret_persistence_allowed: false
second_page_allowed: false
file_content_fetch_allowed: false
operator_minutes_removed_measured: 0
custom_code_avoided_realized_by_this_candidate: 0
custom_code_avoided_estimate: 30_to_100_LOC_UNVALIDATED
credentials: CONNECTOR_MANAGED_EFFECTIVE_SCOPE_AND_PRINCIPAL_UNKNOWN
durability: PENDING_DIRECT_RECEIPT
observability: PENDING_DIRECT_RECEIPT
portability: PHASE1_MEDIUM_HIGH_WITH_DOCUMENT_TAXONOMY_GATE
failure_behavior: UNPROBED
paid_cost_usd_observed: UNKNOWN_NO_PHASE2_CALL_YET
verifier: GIT_DURABLE_READBACK_PLUS_DIRECT_DRIVE_RECEIPT
consumer: HFO_BOUNDED_DRIVE_DISCOVERY_FOR_OPERATOR_CONTROL_LOOPS
strongest_falsifier: PHASE2_REPLAY_HYDRATES_CONTENT_OR_CANNOT_REPRODUCE_BOUNDED_METADATA_BEHAVIOR;CONSUMER_REQUIRES_GOOGLE_DOCS_ONLY_MIME_SEMANTICS
honest_flaw: PHASE2_REPLAY_CAN_ESTABLISH_REPEATABILITY_ONLY;IT_CANNOT_PROVE_COMPLETENESS_PERMISSION_SCOPE_RATE_LIMIT_QUOTA_DEBIT_OR_NATIVE_QUERY_EQUIVALENCE
valid_time_utc: 2026-08-09T18:47:00Z
recorded_time_utc: 2026-08-09T18:47:00Z
---

# X13 Phase 2 preflight — Google Drive document metadata search

Replay the exact Phase-1 bounded request once. Do not fetch a second page or file contents. Persist only aggregate measurements and privacy-safe digests; never persist raw file names, IDs, URLs, parent IDs, content, or page tokens.

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
candidate_request:
  query: HFO
  topn: 5
  best_effort_fetch: false
  require_viewed_by_user: false
  item_type: document
  page_token: null
canonical_request_json_sorted_compact: '{"best_effort_fetch":false,"item_type":"document","page_token":null,"query":"HFO","require_viewed_by_user":false,"topn":5}'
candidate_request_sha256: 81deb918b3bef5f68c1819a101a10fe6130a114c552a94ea0773c1ab2769e47d
phase1_ordered_result_id_digest_sha256: 9e7528559ea056b1cb10633c493a81e0070a9d6909567f18ed2b1e2e5d928bf7
read_only: true
mutation_allowed: false
paid_call_allowed: false
secret_persistence_allowed: false
operator_minutes_removed_measured: 0
custom_code_avoided_realized_by_this_candidate: 0
custom_code_avoided_estimate: 30_to_100_LOC_UNVALIDATED
credentials: CONNECTOR_MANAGED_EFFECTIVE_SCOPE_AND_PRINCIPAL_UNKNOWN
durability: GIT_PREFLIGHT_PENDING_DIRECT_RECEIPT
observability: PHASE2_EXACT_REPLAY_PENDING
portability: MEDIUM_HIGH_WITH_DOCUMENT_TAXONOMY_VARIANCE_GATE
failure_behavior: UNPROBED
paid_cost_usd_observed: 0_NO_CHARGE_SURFACED_NOT_BILLING_PROOF
verifier: GIT_DURABLE_READBACK_PLUS_DIRECT_DRIVE_RECEIPT
consumer: HFO_BOUNDED_DRIVE_DISCOVERY_FOR_OPERATOR_CONTROL_LOOPS
strongest_falsifier: EXACT_REPLAY_HYDRATES_FILE_CONTENT_OR_CANNOT_REPRODUCE_BOUNDED_METADATA_BEHAVIOR
honest_flaw: PHASE2_REPLAY_ONLY;NO_PERMISSION_FAILURE_VALID_PAGINATION_SCOPE_RATE_LIMIT_QUOTA_DEBIT_LATENCY_OR_COMPLETENESS_EVIDENCE
valid_time_utc: 2026-08-09T18:49:00Z
recorded_time_utc: 2026-08-09T18:49:00Z
---

# X13 Phase 2 preflight — Google Drive document metadata exact replay

Recompute and freeze the Phase-1 request, then invoke it exactly once. Compare result count, privacy-safe ordered-ID digest, next-page-token presence, content-hydration behavior, and document-taxonomy variance. Do not fetch a second page or file contents. Do not persist raw file names, IDs, URLs, parent IDs, snippets, content, or page tokens.

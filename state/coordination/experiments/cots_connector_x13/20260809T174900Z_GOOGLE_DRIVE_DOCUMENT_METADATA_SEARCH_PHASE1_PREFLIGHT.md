---
schema_id: hfo.gen133.x13.cots_connector_event.v1
experiment_id: X13_GOOGLE_DRIVE_DOCUMENT_METADATA_SEARCH_READONLY_029
event_type: PHASE1_PREFLIGHT
expected_current_version: 212
candidate: Google_Drive.search_document_metadata_readonly
campaign_wake: 1_of_4
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
read_only: true
mutation_allowed: false
paid_call_allowed: false
secret_persistence_allowed: false
operator_minutes_removed_measured: 0
custom_code_avoided_realized_by_this_candidate: 0
custom_code_avoided_estimate: 30_to_100_LOC_UNVALIDATED
credentials: CONNECTOR_MANAGED_EFFECTIVE_SCOPE_AND_PRINCIPAL_UNKNOWN
durability: PENDING_DIRECT_RECEIPT
observability: PENDING_DIRECT_RECEIPT
portability: PENDING_DIRECT_RECEIPT
failure_behavior: UNPROBED
paid_cost_usd_observed: UNKNOWN_NO_CALL_YET
verifier: GIT_DURABLE_READBACK_PLUS_DIRECT_DRIVE_RECEIPT
consumer: HFO_BOUNDED_DRIVE_DISCOVERY_FOR_OPERATOR_CONTROL_LOOPS
strongest_falsifier: CONNECTOR_HYDRATES_FILE_CONTENT_DESPITE_EXPLICIT_DOCUMENT_METADATA_MODE_OR_CANNOT_BOUND_ONE_PROVIDER_PAGE
honest_flaw: PHASE1_ONLY;NO_PERMISSION_FAILURE_PAGINATION_SCOPE_RATE_LIMIT_QUOTA_OR_COMPLETENESS_EVIDENCE_YET
official_contract_baseline: Google Drive API v3 files.list is GET /drive/v3/files; q filters file results; pageToken continues a prior list request; files.list supports fields selection; a populated nextPageToken means another page may exist. Connector contract additionally states that explicit item_type=document performs exactly one metadata-only provider page and never fetches file contents.
valid_time_utc: 2026-08-09T17:49:00Z
recorded_time_utc: 2026-08-09T17:49:00Z
---

# X13 Phase 1 preflight — Google Drive document metadata search

One bounded read-only call only. Search keyword `HFO`, `topn=5`, explicit `item_type=document`, `best_effort_fetch=false`. Do not fetch a second page, file contents, or mutate Drive state. Persist only aggregate measurements and privacy-safe digests; do not persist raw file names, IDs, URLs, snippets, content, or page tokens.

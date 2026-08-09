---
schema_id: hfo.gen133.x13.cots_connector_current.v1
experiment_id: X13_GOOGLE_DRIVE_DOCUMENT_METADATA_SEARCH_READONLY_029
version: 213
prior_version: 212
candidate: Google_Drive.search_document_metadata_readonly
campaign_wake: 1_of_4
campaign_status: ACTIVE_PHASE1
phase_1_status: PHASE1_ACCEPTED_WITH_GATES_ANDON
phase_2_status: NOT_RUN
phase_3_status: NOT_RUN
phase_4_status: NOT_RUN
phase_4_decision: NONE
operational_decision: PENDING
wip: 1
last_event_commit: c20373bdc86fc233da1d71288f064e5eb7047eb5
last_event_path: state/coordination/experiments/cots_connector_x13/20260809T175000Z_GOOGLE_DRIVE_DOCUMENT_METADATA_SEARCH_PHASE1_RESULT.md
last_event_blob_sha: 4b1611cd8539b645745b6fa927e7c89f83a1ec00
last_event_readback: true
phase1_preflight_commit: 0e02d523c96f2ae8c9ade5f7dffbae4fdf77be73
phase1_preflight_blob_sha: a55afb4d686d224f05793dedef174414a12b2ebf
phase1_result_commit: c20373bdc86fc233da1d71288f064e5eb7047eb5
phase1_result_blob_sha: 4b1611cd8539b645745b6fa927e7c89f83a1ec00
phase1_result_readback: true
candidate_invocations_total: 1
usable_candidate_results: 1
expected_failure_probes_total: 0
connector_errors_total: 0
retries_total: 0
fallbacks_total: 0
candidate_mutations_total: 0
result_count_phase1: 5
ordered_result_id_digest_phase1_sha256: 9e7528559ea056b1cb10633c493a81e0070a9d6909567f18ed2b1e2e5d928bf7
next_page_token_phase1_observed: false
file_content_hydration_phase1_observed: false
operator_minutes_removed_measured: 0
custom_code_avoided_estimate: 30_to_100_LOC_UNVALIDATED
custom_code_avoided_realized_by_this_candidate: 0
paid_cost_usd_observed: 0_NO_CHARGE_SURFACED_NOT_BILLING_PROOF
credentials: CONNECTOR_MANAGED_EFFECTIVE_SCOPE_AND_PRINCIPAL_UNKNOWN
durability: PHASE1_GIT_PREFLIGHT_AND_RESULT_READ_BACK_ON_CANONICAL_BRANCH
observability: ONE_BOUNDED_SUCCESS;5_RESULTS;ORDERED_ID_DIGEST;NO_CONTENT_HYDRATION;NO_NATIVE_REQUEST_ID_RATE_HEADERS_SCOPE_QUOTA_DEBIT_OR_LATENCY_SURFACED
portability: MEDIUM_HIGH_TO_DRIVE_FILES_LIST_QUERY_AND_PAGINATION_CONCEPTS_BUT_CONNECTOR_DOCUMENT_TAXONOMY_IS_BROADER_THAN_GOOGLE_DOCS_MIME_SEMANTICS
failure_behavior: UNPROBED
verifier: GIT_DURABLE_READBACK_PLUS_DIRECT_DRIVE_RECEIPT
consumer: HFO_BOUNDED_DRIVE_DISCOVERY_FOR_OPERATOR_CONTROL_LOOPS
adoption_credit: 0
fitness_credit: 0
mandatory_gate: READ_ONLY;ITEM_TYPE_DOCUMENT;BEST_EFFORT_FETCH_FALSE;TOPN_5;NO_SECOND_PAGE;DO_NOT_PERSIST_RAW_NAMES_IDS_URLS_PARENT_IDS_OR_PAGE_TOKENS;DOCUMENT_ITEM_TYPE_NOT_GOOGLE_DOCS_ONLY;NO_COMPLETENESS_SCOPE_RATE_LIMIT_OR_QUOTA_ASSUMPTIONS
strongest_falsifier: PHASE2_REPLAY_HYDRATES_CONTENT_OR_CANNOT_REPRODUCE_BOUNDED_METADATA_BEHAVIOR;CONSUMER_REQUIRES_GOOGLE_DOCS_ONLY_MIME_SEMANTICS
honest_flaw: DOCUMENT_ITEM_TYPE_INCLUDED_A_SPREADSHEET_RESOURCE;NO_PERMISSION_FAILURE_VALID_PAGINATION_SCOPE_RATE_LIMIT_QUOTA_DEBIT_LATENCY_OR_COMPLETENESS_EVIDENCE
next_phase: PHASE2_EXACT_REPLAY_ONCE_NO_SECOND_PAGE_NO_CONTENT_FETCH
valid_time_utc: 2026-08-09T17:50:30Z
recorded_time_utc: 2026-08-09T17:50:30Z
---

# X13 CURRENT v213

`X13_GOOGLE_DRIVE_DOCUMENT_METADATA_SEARCH_READONLY_029` is active at wake 1 of 4 with **PHASE1_ACCEPTED_WITH_GATES_ANDON**.

One bounded read-only Drive search using `query=HFO`, `topn=5`, explicit `item_type=document`, and `best_effort_fetch=false` returned five metadata results with no observed file-content hydration, retry, fallback, connector error, or Drive mutation. Persisted state contains only aggregate measurements and a privacy-safe ordered-ID digest.

Measured variance/Andon: connector `document` mode included at least one spreadsheet resource, so it must not be treated as equivalent to a Google Docs MIME-type filter. No direct receipt established completeness, valid pagination, OAuth principal/scope, rate-limit behavior, native method mapping, quota debit, billing, or latency.

Measured operator savings remain `0`; realized custom-code avoidance remains `0`; the `30–100 LOC` estimate remains unvalidated. Adoption and fitness credit remain `0 / 0`.

Next wake: Phase 2 exact replay once with the same bounded request. Do not fetch page 2 or file contents. WIP remains 1.

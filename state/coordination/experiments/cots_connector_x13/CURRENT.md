---
schema_id: hfo.gen133.x13.cots_connector_current.v1
experiment_id: X13_GITHUB_BRANCH_SEARCH_READONLY_025
version: 197
prior_version: 196
previous_experiment_id: X13_GDRIVE_METADATA_SEARCH_READONLY_024
candidate: GitHub_search_branches_readonly
campaign_wake: 1_of_4
campaign_status: ACTIVE
phase_1_status: PHASE1_ACCEPTED_WITH_GATES
phase_2_status: NOT_RUN
phase_3_status: NOT_RUN
phase_4_status: NOT_RUN
phase_4_decision: UNKNOWN
operational_decision: EVALUATING_BOUNDED_BRANCH_DISCOVERY
wip: 1
last_event_commit: c07766d6e68cafb893e4a121421a14b414057ef5
last_event_path: state/coordination/experiments/cots_connector_x13/20260809T014920Z_GITHUB_BRANCH_SEARCH_PHASE1_RESULT.md
last_event_blob_sha: f82cd8ecde49310ff04aa2a6f97d06f6e65cc0a6
last_event_readback: true
phase1_preflight_commit: cccb70a282df95a54600a27d046e28f1c8f35737
phase1_preflight_blob_sha: a3c5e334c14b04337214d39780ecf5d9ac76dcb5
phase1_preflight_readback: true
candidate_invocations_total: 1
usable_candidate_results: 1
result_count_last_success: 1
exact_query_match_observed: true
opaque_cursor_observed: true
connector_errors_total: 0
retries_total: 0
fallbacks_total: 0
candidate_mutations_total: 0
external_call_time_ms_last: 299
operator_minutes_removed_measured: 0
custom_code_avoided_estimate: 20_to_60_LOC_UNVALIDATED
custom_code_avoided_realized_by_this_candidate: 0
paid_cost_usd_observed: 0_NO_CHARGE_SURFACED_NOT_BILLING_PROOF
direct_cost_or_quota_evidence: NO_RATE_LIMIT_HEADERS_QUOTA_DEBIT_OR_BILLING_METADATA_EXPOSED;OFFICIAL_GITHUB_REST_LIMITS_DEPEND_ON_AUTH_PRINCIPAL_AND_TOKEN_TYPE
credentials: GITHUB_CONNECTOR_MANAGED_EFFECTIVE_TOKEN_TYPE_PRINCIPAL_AND_PERMISSIONS_UNKNOWN;SUCCESS_PROVES_ACCESS_TO_NAMED_REPOSITORY_BRANCH_METADATA_FOR_THIS_CALL_ONLY
durability: GIT_PHASE1_PREFLIGHT_AND_RESULT_DURABLE_AND_READ_BACK
observability: ONE_EXACT_BRANCH_MATCH_PLUS_OPAQUE_CURSOR_AND_299MS_WRAPPER_EXTERNAL_CALL_TIME;NO_NATIVE_ENDPOINT_HTTP_STATUS_REQUEST_ID_RATE_HEADERS_TOKEN_SCOPE_OR_QUOTA_DEBIT_EXPOSED
portability: MEDIUM_NATIVE_LIST_BRANCHES_STANDARD_BUT_CONNECTOR_QUERY_FILTER_AND_OPAQUE_CURSOR_WRAPPER_SPECIFIC
failure_behavior: NOT_YET_PROBED
verifier: GITHUB_PHASE1_PREFLIGHT_AND_RESULT_READBACK_PLUS_DIRECT_SEARCH_BRANCHES_RECEIPT_PLUS_CANONICAL_REF_FETCH
consumer: HFO_CANONICAL_BRANCH_DISCOVERY_AND_PREFLIGHT_VALIDATION
adoption_credit: 0
fitness_credit: 0
mandatory_gate: READ_ONLY;BOUNDED_PAGE_SIZE;NO_BRANCH_MUTATION;NO_COMPLETENESS_INFERENCE_FROM_ONE_MATCH_OR_OPAQUE_CURSOR;DO_NOT_ASSUME_WRAPPER_QUERY_CURSOR_EQUAL_NATIVE_LIST_BRANCHES_SEMANTICS
strongest_falsifier: PROVIDER_DIRECT_BRANCH_LIST_UNDER_THE_SAME_EFFECTIVE_PRINCIPAL_FAILS_TO_INCLUDE_THE_MATCHED_BRANCH_OR_WRAPPER_SEARCH_OMITS_A_KNOWN_MATCH_UNDER_STABLE_STATE
honest_flaw: ONE_SUCCESS_ONLY;NO_REPLAY_FAILURE_PERMISSION_RATE_LIMIT_OR_PAGINATION_PROBE;OPAQUE_CURSOR_SEMANTICS_AND_NATIVE_ENDPOINT_MAPPING_UNKNOWN;EFFECTIVE_AUTH_PRINCIPAL_AND_RATE_DEBIT_UNKNOWN
next_phase: PHASE2_EXACT_REPLAY_ONCE_COMPARE_RESULT_COUNT_EXACT_MATCH_AND_CURSOR_PRESENCE_ONLY
valid_time_utc: 2026-08-09T01:49:30Z
recorded_time_utc: 2026-08-09T01:49:30Z
---

# X13 CURRENT v197

`X13_GITHUB_BRANCH_SEARCH_READONLY_025` is active at wake 1 of 4 with **PHASE1_ACCEPTED_WITH_GATES**.

One bounded read-only `search_branches` call returned exactly one exact match for the canonical branch `agent/gen133-bootstrap-20260730`, with an opaque cursor and 299 ms observed wrapper external-call time. No connector error, retry, fallback, or repository mutation was observed.

The official GitHub REST baseline and the connector contract are not treated as equivalent. Native `List branches` uses bounded `per_page` plus integer `page` pagination and requires Contents read permission for fine-grained access to private resources; the connector exposes query filtering and an opaque cursor. Native endpoint mapping, filtering semantics, cursor semantics, effective token/principal, and actual rate debit remain unknown.

Mandatory gates: read only, bounded page size, no branch mutation, no completeness inference from one match or cursor presence, and no assumption that connector query/cursor semantics equal the native REST contract.

Measured operator savings remain `0`; realized custom-code avoidance remains `0`; estimated avoidance is `20–60 LOC` unvalidated; adoption/fitness credit remains `0 / 0`.

Next wake: Phase 2 exact replay once and compare only result count, exact-match presence, and cursor presence. No branch mutation.

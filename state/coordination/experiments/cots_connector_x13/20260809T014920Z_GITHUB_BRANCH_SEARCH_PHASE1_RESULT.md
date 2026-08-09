---
schema_id: hfo.gen133.x13.cots_connector_event.v1
experiment_id: X13_GITHUB_BRANCH_SEARCH_READONLY_025
event_type: PHASE1_RESULT
expected_current_version: 196
candidate: GitHub_search_branches_readonly
campaign_wake: 1_of_4
phase_status: PHASE1_ACCEPTED_WITH_GATES
wip: 1
preflight_commit: cccb70a282df95a54600a27d046e28f1c8f35737
preflight_blob_sha: a3c5e334c14b04337214d39780ecf5d9ac76dcb5
preflight_readback: true
request_sha256_verified: true
candidate_invocations_total: 1
usable_candidate_results: 1
result_count: 1
exact_query_match_observed: true
matched_branch: agent/gen133-bootstrap-20260730
opaque_cursor_observed: true
connector_errors_total: 0
retries_total: 0
fallbacks_total: 0
candidate_mutations_total: 0
external_call_time_ms_observed: 299
operator_minutes_removed_measured: 0
custom_code_avoided_estimate: 20_to_60_LOC_UNVALIDATED
custom_code_avoided_realized_by_this_candidate: 0
paid_cost_usd_observed: 0_NO_CHARGE_SURFACED_NOT_BILLING_PROOF
direct_cost_or_quota_evidence: NO_RATE_LIMIT_HEADERS_QUOTA_DEBIT_OR_BILLING_METADATA_EXPOSED;OFFICIAL_GITHUB_REST_LIMITS_DEPEND_ON_AUTH_PRINCIPAL_AND_TOKEN_TYPE
credentials: GITHUB_CONNECTOR_MANAGED;EFFECTIVE_TOKEN_TYPE_PRINCIPAL_AND_PERMISSIONS_NOT_EXPOSED;SUCCESS_PROVES_ACCESS_TO_THE_NAMED_REPOSITORY_BRANCH_METADATA_FOR_THIS_CALL_ONLY
durability: GIT_PREFLIGHT_AND_RESULT_EVENTS_DURABLE;PREFLIGHT_READ_BACK_BEFORE_CANDIDATE_USE
observability: CONNECTOR_RETURNED_ONE_BRANCH_NAME_PLUS_OPAQUE_CURSOR_AND_WRAPPER_CALL_LATENCY;NO_NATIVE_ENDPOINT_HTTP_STATUS_REQUEST_ID_RATE_HEADERS_OR_TOKEN_SCOPE_EXPOSED
portability: MEDIUM_NATIVE_GITHUB_BRANCH_LISTING_IS_STANDARD_BUT_CONNECTOR_QUERY_FILTER_AND_OPAQUE_CURSOR_DIFFER_FROM_NATIVE_PAGE_NUMBER_PER_PAGE_CONTRACT
failure_behavior: NOT_YET_PROBED
verifier: GITHUB_PREFLIGHT_READBACK_PLUS_DIRECT_SEARCH_BRANCHES_RECEIPT_PLUS_CANONICAL_BRANCH_FETCHES_ON_SAME_REF
consumer: HFO_CANONICAL_BRANCH_DISCOVERY_AND_PREFLIGHT_VALIDATION
adoption_credit: 0
fitness_credit: 0
mandatory_gate: READ_ONLY;BOUNDED_PAGE_SIZE;NO_BRANCH_MUTATION;NO_COMPLETENESS_INFERENCE_FROM_ONE_MATCH_OR_OPAQUE_CURSOR;DO_NOT_ASSUME_WRAPPER_QUERY_CURSOR_EQUAL_NATIVE_LIST_BRANCHES_SEMANTICS
strongest_falsifier: PROVIDER_DIRECT_BRANCH_LIST_UNDER_THE_SAME_EFFECTIVE_PRINCIPAL_FAILS_TO_INCLUDE_THE_MATCHED_BRANCH_OR_WRAPPER_SEARCH_OMITS_A_KNOWN_MATCH_UNDER_STABLE_STATE
honest_flaw: ONE_SUCCESS_ONLY;NO_REPLAY_FAILURE_PERMISSION_RATE_LIMIT_OR_PAGINATION_PROBE;OPAQUE_CURSOR_SEMANTICS_AND_NATIVE_ENDPOINT_MAPPING_UNKNOWN;EFFECTIVE_AUTH_PRINCIPAL_AND_RATE_DEBIT_UNKNOWN
valid_time_utc: 2026-08-09T01:49:20Z
recorded_time_utc: 2026-08-09T01:49:20Z
---

# X13 GitHub Branch Search Phase 1 Result

A single bounded read-only `search_branches` call against `TTaoGaming/hfo-gen-133` returned exactly one branch, `agent/gen133-bootstrap-20260730`, matching the exact query. The connector also returned an opaque cursor and reported 299 ms external-call time. No connector error, retry, fallback, or repository mutation was observed.

Official GitHub REST baseline differs from this wrapper: native `GET /repos/{owner}/{repo}/branches` lists branches with `per_page` (max 100) and integer `page` pagination; fine-grained access to private resources requires repository Contents read permission. The connector instead exposes a query string and opaque cursor, so native mapping, filtering semantics, and cursor semantics remain unverified.

No actual rate-limit debit, rate headers, billing metadata, token type, principal, or effective permission set was exposed. GitHub documents REST limits as authentication-dependent, so no quota number is attributed to this connector call without direct evidence.

Phase 1 gate: treat this only as bounded branch-name discovery. Do not infer repository-wide completeness or native pagination equivalence.

Primary sources: GitHub Docs `REST API endpoints for branches` and `Rate limits for the REST API`, current API version documentation.

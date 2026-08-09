---
schema_id: hfo.gen133.x13.cots_connector_event.v1
experiment_id: X13_GITHUB_RECENT_PRS_READONLY_027
event: PHASE1_RESULT
expected_task_id: 6a55c1733708819185088bf334e33ea5
expected_current_version: 204
candidate: GitHub_get_users_recent_prs_in_repo_readonly
wip: 1
phase_status: PHASE1_ACCEPTED_WITH_GATES
preflight_commit: a5aa6f19f4afada4840090c3751f4e2058c3d961
preflight_blob_sha: 23ea60f33c0a177491cc1a7130957bfe567ae3e8
preflight_readback: true
request_sha256_verified: true
candidate_invocations_total: 1
result_count: 5
ordered_pr_number_sha256: 891dfafb35f12d4125a542bd7ae3d2241bcf7e231cd7f4c4dfac64bf8d947e8f
state_open_count: 5
draft_true_count: 5
merged_true_count: 0
diff_fields_requested: false
comments_requested: false
body_text_returned_despite_minimal_request: true
connector_errors_total: 0
retries_total: 0
fallbacks_total: 0
candidate_mutations_total: 0
external_call_time_ms: 1618
operator_minutes_removed_measured: 0
custom_code_avoided_estimate: 40_to_100_LOC_UNVALIDATED
custom_code_avoided_realized_by_this_candidate: 0
paid_cost_usd_observed: 0_NO_CHARGE_SURFACED_NOT_BILLING_PROOF
direct_cost_or_quota_evidence: NO_RATE_LIMIT_HEADERS_SEARCH_RESOURCE_DEBIT_BILLING_METADATA_OR_REQUEST_ID_EXPOSED
credentials: CONNECTOR_MANAGED;RESULTS_WERE_USER_SCOPED_AND_ALL_RETURNED_PRS_WERE_AUTHORED_BY_TTAOGAMING_BUT_EFFECTIVE_TOKEN_TYPE_PERMISSIONS_AND_RATE_LIMIT_IDENTITY_REMAIN_UNKNOWN
durability: GIT_PREFLIGHT_AND_PHASE1_RESULT_DURABLE_ON_CANONICAL_BRANCH_WITH_PREFLIGHT_READBACK
observability: WRAPPER_EXPOSED_PR_METADATA_AND_EXTERNAL_CALL_TIME;ALSO_RETURNED_FULL_BODY_TEXT_WITHOUT_A_BODY_SUPPRESSION_PARAMETER;NO_NATIVE_ENDPOINT_QUERY_RATE_HEADERS_REQUEST_ID_OR_QUOTA_DEBIT
portability: MEDIUM;CONNECTOR_DESCRIPTION_SAYS_UNDERLYING_GITHUB_SEARCH_ENDPOINT_AND_NATIVE_GITHUB_SUPPORTS_GET_SEARCH_ISSUES_WITH_IS_PR_FILTERS_BUT_EXACT_QUERY_SORT_PAGINATION_AND_AUTHENTICATED_USER_BINDING_ARE_NOT_EXPOSED
failure_behavior: NOT_PROBED_IN_PHASE1
verifier: GITHUB_PREFLIGHT_READBACK_PLUS_DIRECT_GITHUB_CONNECTOR_RECEIPT_PLUS_PHASE1_RESULT_READBACK_PENDING
consumer: HFO_BOUNDED_PULL_REQUEST_INTAKE_AND_OPERATOR_REVIEW_PRECHECK
adoption_credit: 0
fitness_credit: 0
mandatory_gate: READ_ONLY;REPOSITORY_SCOPED;BOUNDED_LIMIT;NO_DIFF;NO_COMMENTS;DO_NOT_PERSIST_PR_BODY_TEXT_IN_X13_RECEIPTS;NO_COMPLETENESS_ORDERING_OR_NATIVE_QUERY_INFERENCE
strongest_falsifier: DOWNSTREAM_USE_REQUIRES_FIELD_MINIMIZATION_NO_BODY_DISCLOSURE_AUTHORITATIVE_COMPLETENESS_STABLE_SORT_OR_EXPLICIT_RATE_LIMIT_CONTROL
honest_flaw: CONNECTOR_RETURNED_FULL_PR_BODY_TEXT_EVEN_WITH_DIFF_AND_COMMENTS_DISABLED;THIS_INCREASES_DATA_EXPOSURE_AND_MEANS_THE_TOOL_IS_NOT_A_METADATA_ONLY_SURFACE
valid_time_utc: 2026-08-09T09:51:00Z
recorded_time_utc: 2026-08-09T09:51:00Z
---

# X13 GitHub recent PRs — Phase 1 result

One exact preflighted read-only call returned five recent pull requests for `TTaoGaming/hfo-gen-133`; all five were open drafts and none was merged. X13 persisted only aggregate state plus an ordered PR-number digest, not PR body/comment text.

Measured wrapper time was 1618 ms with zero observed connector errors, retries, fallbacks, or mutations. The connector did not surface GitHub rate-limit headers, request ID, native query, token type, permissions, quota debit, or billing metadata.

Material gate: despite `include_diff=false` and `include_comments=false`, the connector returned each PR's full `body`. Therefore this capability is not metadata-only and should not be used where field minimization or body non-disclosure is a hard requirement.

Official contract context: GitHub supports pull-request filtering through issue/PR search (`is:pr`) and exposes `GET /search/issues`; search has a separate rate-limit resource. This is portability context only; the connector's exact native query, sort, pagination, and authenticated-user binding were not exposed.

Phase 1 disposition: **PHASE1_ACCEPTED_WITH_GATES** for bounded repository-scoped PR intake only. Phase 2 should replay the exact request once and compare count, ordered PR-number digest, and state/draft aggregates while treating repository drift as possible.

---
schema_id: hfo.gen133.x13.cots_connector_event.v1
experiment_id: X13_GITHUB_COMPARE_COMMITS_READONLY_001
event_type: PHASE1_OFFICIAL_CONTRACT_AND_DIRECT_BASELINE
phase: 1_of_4
disposition: PHASE1_ACCEPTED_WITH_GATES
carrier_task_id: 6a55c1733708819185088bf334e33ea5
carrier_task_id_match: true
wip: 1
canonical_repository: TTaoGaming/hfo-gen-133
canonical_branch: agent/gen133-bootstrap-20260730
prior_current_version: 80
candidate: GitHub_compare_commits_bounded_readonly_diff_metadata_surface
effect_ceiling: BOUNDED_READONLY_COMPARE_NO_FILE_FETCH_WRITE_BRANCH_PR_COMMENT_MERGE_OR_PUBLICATION
official_contract:
  endpoint: GET_/repos/{owner}/{repo}/compare/{basehead}
  official_documentation: https://docs.github.com/en/rest/commits/commits#compare-two-commits
  accepted_inputs: SAME_REPOSITORY_REFS_TAGS_OR_COMMIT_SHAS_AND_SAME_NETWORK_FORK_REFS
  minimum_fine_grained_permission_for_private_repository: CONTENTS_READ
  public_repository_authentication: OPTIONAL_PER_OFFICIAL_CONTRACT
  documented_success_status: 200
  documented_failure_statuses:
    - 404
    - 500
    - 503
  documented_unpaginated_commit_limit: 250
  documented_changed_file_limit_on_first_page: 300
  documented_order: COMMITS_CHRONOLOGICAL
  official_rate_limit_reference: https://docs.github.com/en/rest/using-the-rest-api/rate-limits-for-the-rest-api
probe:
  repository: TTaoGaming/hfo-gen-133
  base_ref_type: FULL_COMMIT_SHA
  head_ref_type: FULL_COMMIT_SHA
  relation: SAME_SHA
  base_sha: 8b8d3f3e2510159d81b866165b85ef706a559ee3
  head_sha: 8b8d3f3e2510159d81b866165b85ef706a559ee3
  bounded_reason: SAME_CONTENT_ADDRESSED_REF_FOR_ZERO_DIFF_BASELINE
measurements:
  candidate_invocations: 1
  completed_connector_responses: 1
  connector_error_count: 0
  status: identical
  ahead_by: 0
  behind_by: 0
  total_commits: 0
  files_returned_count: 0
  base_commit_sha_matches_requested: true
  merge_base_commit_sha_matches_requested: true
  too_large_field: null
  connector_reported_external_call_time_ms: 677
  carrier_retry_count: 0
  fallback_count: 0
  mutation_count: 0
  file_content_fetch_count: 0
  paid_cost_usd_observed: 0_NO_CHARGE_SURFACED
  actual_upstream_request_count: UNKNOWN
  actual_quota_consumed: UNKNOWN
  operator_minutes_removed_measured: 0
  consumer_ack: NOT_OBSERVED
custom_code_avoided_estimate:
  authenticated_compare_request_and_compact_relation_normalization: 15_to_50_LOC_UNVALIDATED
  required_hfo_gates_not_avoided: REF_PINNING_PERMISSION_VERIFICATION_PAGINATION_TRUNCATION_RAW_PARITY_RATE_LIMIT_TELEMETRY_RETRY_POLICY_AND_CONSUMER_WORKFLOW
credentials:
  connector_reached_positive_compare_path: true
  operator_supplied_credentials_this_wake: 0
  authenticated_principal: UNKNOWN
  effective_permission: UNKNOWN_NOT_PROVEN_CONTENTS_READ_ONLY
  credential_storage_and_custody: CONNECTOR_MANAGED_UNINSPECTED
  least_privilege_closed: false
durability:
  source_commit_objects: GITHUB_HOSTED_CONTENT_ADDRESSED_OBJECTS
  comparison_response: EPHEMERAL_CONNECTOR_RESULT
  durable_receipt: THIS_GIT_EVENT_AND_CURRENT_POINTER
observability:
  exposed: STATUS_AHEAD_BEHIND_TOTAL_COMMITS_BASE_SHA_MERGE_BASE_SHA_FILES_AND_EXTERNAL_CALL_TIME
  not_exposed: RAW_HTTP_STATUS_HEADERS_REQUEST_ID_RATE_LIMIT_RESOURCE_REMAINING_RESET_EFFECTIVE_IDENTITY_UPSTREAM_ATTEMPTS_OR_RETRIES
portability:
  git_commit_graph_semantics: PARTIALLY_PORTABLE
  wrapper_response_shape: GITHUB_CONNECTOR_SPECIFIC
  cross_provider_parity: NOT_TESTED
failure_behavior:
  phase_1_failure_probe: NOT_RUN
  documented_statuses_only: 404_500_503
  connector_normalization: UNVERIFIED
admitted_interpretation: CONNECTOR_RETURNED_AN_IDENTICAL_ZERO_DIFF_RELATION_FOR_ONE_CONTENT_ADDRESSED_SAME_SHA_COMPARISON
not_admitted:
  - CHANGED_FILE_DIFF_CORRECTNESS
  - BRANCH_OR_TAG_RESOLUTION_STABILITY
  - PAGINATION_COMPLETENESS_OR_TRUNCATION_SIGNAL
  - RENAMED_BINARY_OR_LARGE_DIFF_BEHAVIOR
  - PRIVATE_REPOSITORY_LEAST_PRIVILEGE
  - RAW_PROVIDER_PARITY
  - ACTUAL_QUOTA_USE_OR_ZERO_HIDDEN_RETRIES
mandatory_gates:
  - PREFER_FULL_COMMIT_SHAS_FOR_BINDING_DECISIONS
  - TREAT_BRANCHES_AND_TAGS_AS_MUTABLE_OBSERVATIONS
  - BOUND_EXPECTED_COMMIT_AND_FILE_CARDINALITY_BEFORE_USE
  - DO_NOT_TREAT_FILES_ARRAY_AS COMPLETE_FOR_LARGE_COMPARISONS_WITHOUT PAGINATION_OR_INDEPENDENT_GIT_VERIFICATION
  - DO_NOT_CLAIM_LEAST_PRIVILEGE_RAW_PARITY_QUOTA_USE_OR_ZERO_HIDDEN_RETRIES
  - REQUIRE_NAMED_CONSUMER_ACK_AND_MEASURED_OUTCOME_BEFORE_OPERATIONAL_ADOPTION_OR_FITNESS_CREDIT
strongest_falsifier: SAME_PRINCIPAL_RAW_GITHUB_COMPARE_FOR_THE_SAME_FULL_SHA_PAIR_RETURNS_NONIDENTICAL_RELATION_DIFFERENT_BASE_OR_MERGE_BASE_SHA_OR MATERIAL_RESPONSE_VARIANCE
verifier: DISTINCT_AUTHORIZED_RAW_GITHUB_REST_COMPARE_CALL_WITH_SAME_SHA_PAIR_CAPTURING_REQUEST_DIGEST_API_VERSION_RAW_STATUS_HEADERS_REQUEST_ID_RATE_LIMIT_FIELDS_AND_RESPONSE_BODY
consumer:
  immediate_catalog_consumer: HFO_COTS_CAPABILITY_INVENTORY
  future_operational_consumer: MUST_BE_NAMED_IN_NEW_WORKITEM
honest_flaw: ONE_SAME_SHA_ZERO_DIFF_SUCCESS PROVES_ONLY_THE_CONNECTOR_VISIBLE_IDENTICAL_PATH; CHANGED_DIFF_STATS_BRANCH_RESOLUTION_PAGINATION_TRUNCATION_BINARY_RENAME_LARGE_COMPARISON_PERMISSION_FAILURE_RAW_HTTP_QUOTA_HIDDEN_RETRIES_CONSUMER_VALUE_AND_OPERATOR_TIME_REDUCTION_REMAIN_UNVERIFIED
next_wake:
  phase: 2_of_4
  planned_probe: ONE_BOUNDED_CONTENT_ADDRESSED_ADJACENT_COMMIT_COMPARISON_EXPECTED_TO_RETURN_A_SMALL_NONZERO_FILE_SET_WITHOUT_FILE_FETCH_RETRY_OR_MUTATION
valid_time_utc: 2026-08-04T05:48:00Z
recorded_time_utc: 2026-08-04T05:48:00Z
---

# X13 GitHub compare-commits phase 1

A single read-only comparison used the same full commit SHA for both base and head. The connector returned `status=identical`, zero ahead/behind counts, zero commits, zero files, matching base and merge-base SHAs, no connector-visible error, and 677 ms external-call time. This establishes only the bounded identical-path response shape. It does not validate changed-file correctness, mutable-ref resolution, pagination, truncation, permissions, raw API parity, quota use, hidden retries, consumer value, or operator-time reduction.

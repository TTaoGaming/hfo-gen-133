---
schema_id: hfo.gen133.x13.cots_connector_event.v1
experiment_id: X13_GITHUB_COMPARE_COMMITS_READONLY_001
event_id: X13_GITHUB_COMPARE_COMMITS_PHASE4_ADOPT_WITH_GATES_20260804T084800Z
event_type: PHASE4_DECISION
phase: 4_of_4
phase_4_decision: ADOPT_WITH_GATES
disposition: ADOPT_WITH_GATES_CATALOG_ONLY_NONOPERATIONAL
campaign_status: CLOSED
carrier_task_id: 6a55c1733708819185088bf334e33ea5
carrier_task_id_match: true
wip: 1
canonical_repository: TTaoGaming/hfo-gen-133
canonical_branch: agent/gen133-bootstrap-20260730
prior_current_version: 83
candidate: GitHub_compare_commits_bounded_readonly_diff_metadata_surface
effect_ceiling: CATALOG_ONLY_BOUNDED_READONLY_COMPARE
phase_4_additional_candidate_calls: 0
source_events:
  phase_1:
    path: state/coordination/experiments/cots_connector_x13/20260804T054800Z_GITHUB_COMPARE_COMMITS_PHASE1_BASELINE.md
    blob_sha: 8df5caaac7e6adf684efb3439d4a1bf5a8fcaf78
  phase_2:
    path: state/coordination/experiments/cots_connector_x13/20260804T064800Z_GITHUB_COMPARE_COMMITS_PHASE2_MICROUSE.md
    blob_sha: 18745f32e2a2fb5efe8549e650e0aa1fdc7ee3cc
  phase_3:
    path: state/coordination/experiments/cots_connector_x13/20260804T074800Z_GITHUB_COMPARE_COMMITS_PHASE3_FAILURE_PROBE.md
    blob_sha: aae94e611c6511baa2fa82f2a607ae50f775f2b7
campaign_measurements:
  compare_reads: 3
  completed_success_responses: 2
  connector_visible_errors: 1
  identical_zero_diff_results: 1
  small_nonzero_diff_results: 1
  synthetic_unknown_sha_failure_probes: 1
  phase_2_status: ahead
  phase_2_ahead_by: 1
  phase_2_behind_by: 0
  phase_2_total_commits: 1
  phase_2_files_returned: 1
  phase_2_file_stats_returned: true
  phase_3_error: 404_NOT_FOUND
  phase_3_compare_content_returned: false
  successful_call_external_time_ms_total: 2217
  phase_3_latency_ms: NOT_EXPOSED
  retries: 0
  fallbacks: 0
  candidate_mutations: 0
  file_hydration_calls: 0
  operator_minutes_removed_measured: 0
  operator_minutes_removed_estimate: 1_to_3_UNVALIDATED
  custom_code_avoided_estimate: 15_to_50_LOC_UNVALIDATED
credentials:
  operator_supplied_across_campaign: 0
  authenticated_principal: UNKNOWN
  effective_permission: UNKNOWN
  connector_managed: true
  least_privilege_proven: false
durability:
  compared_commit_inputs: GITHUB_HOSTED_CONTENT_ADDRESSED_OBJECTS_WHEN_FULL_SHAS_ARE_USED
  connector_results: EPHEMERAL_NORMALIZED_RESPONSES
  durable_receipts: FOUR_IMMUTABLE_GIT_EVENTS_PLUS_CURRENT_POINTER
observability:
  exposed:
    - STATUS_AHEAD_BEHIND_AND_TOTAL_COMMIT_COUNTS
    - BASE_AND_MERGE_BASE_SHA_BINDINGS_ON_SUCCESS
    - PER_FILE_PATH_STATUS_AND_CHANGE_COUNTS_FOR_SMALL_RESULT
    - CONNECTOR_VISIBLE_404_WITH_NO_COMPARE_CONTENT
    - EXTERNAL_CALL_TIME_ON_SUCCESS_RESPONSES
  not_exposed:
    - AUTHENTICATED_IDENTITY_AND_EFFECTIVE_SCOPE
    - RAW_HTTP_STATUS_HEADERS_AND_REQUEST_ID
    - RATE_LIMIT_REMAINING_RESET_AND_RESOURCE
    - ACTUAL_UPSTREAM_REQUEST_AND_RETRY_COUNT
    - RAW_RESPONSE_BYTES_OR_DIGEST
    - COMPLETE_COMMIT_LIST_PATCH_AND_TRUNCATION_PROOF
portability:
  git_commit_graph_relation_semantics: PARTIALLY_PORTABLE
  normalized_wrapper_shape: GITHUB_CONNECTOR_SPECIFIC
  cross_provider_parity: NOT_TESTED
failure_behavior:
  observed: OUTER_404_WITHOUT_COMPARE_METADATA_OR_CONTENT
  admitted: FAIL_CLOSED_FOR_ONE_SYNTHETIC_UNKNOWN_SHA_PROBE
  ambiguity: UNKNOWN_REF_VS_INACCESSIBLE_OBJECT_OR_REPOSITORY_VS_PERMISSION_OR_WRAPPER_NORMALIZATION
  automatic_retry_policy: FORBIDDEN_WITHOUT_CHANGED_INPUT_IDENTITY_PERMISSION_OR_NEW_EVIDENCE
direct_cost_and_quota_evidence:
  paid_cost_usd_observed: 0_NO_CHARGE_SURFACED
  actual_quota_consumed: UNKNOWN
  rate_limit_headers_exposed: false
  provider_billing_or_quota_receipt: ABSENT
verifier:
  required: DISTINCT_AUTHORIZED_RAW_GITHUB_REST_COMPARE_WITNESS_FOR_THE_SAME_INPUTS_AND_PRINCIPAL_CLASS_WITH_API_VERSION_RAW_STATUS_SAFE_BODY_DIGEST_REQUEST_ID_RATE_LIMIT_FIELDS_AND_RETRY_COUNT
  completed: false
  advisory_reducer_receipt:
    result: REVISE
    path: state/coordination/receipts/chatgpt_runtime/seat-03/20260804T080900Z_X13_GITHUB_COMPARE_PHASE3_RETURN_BINDINGS_REVISE.yaml
    blob_sha: cbe14efaf7680cccc9bf09c185310403a5d93d8b
    binding_weight: 0
    admitted_use: CONFIRMS_DURABLE_EVENT_READBACK_AND_MISSING_RAW_WITNESS_TERMINAL_BINDINGS_AND_CONSUMER_ACK
    not_admitted: RAW_PROVIDER_PARITY_OR_STOOD_VERDICT
consumer:
  named_catalog_consumer: HFO_COTS_CAPABILITY_INVENTORY
  operational_consumer: NOT_NAMED
  consumer_ack: NOT_OBSERVED
  adoption_credit: 0
  fitness_credit: 0
strongest_falsifier: SAME_PRINCIPAL_RAW_GITHUB_COMPARE_DISAGREES_ON_PHASE2_STATUS_BINDINGS_FILE_PATH_OR_STATS_OR_RETURNS_VALID_COMPARE_METADATA_OR_NON_404_FOR_THE_PHASE3_INPUTS
mandatory_gates:
  - USE_FULL_COMMIT_SHAS_FOR_CONTENT_ADDRESSED_BINDING_DECISIONS
  - VERIFY_RETURNED_BASE_AND_MERGE_BASE_BINDINGS_ON_EVERY_SUCCESS
  - TREAT_BRANCH_AND_TAG_COMPARISONS_AS_MUTABLE_OBSERVATIONS_ONLY
  - BOUND_EXPECTED_COMMIT_AND_FILE_CARDINALITY_AND_INDEPENDENTLY_VERIFY_LARGE_OR_HIGH_ASSURANCE_COMPARISONS
  - FAIL_CLOSED_WHEN_COMPARE_METADATA_IS_ABSENT
  - TREAT_404_AS_AMBIGUOUS_AND_DO_NOT_AUTOMATICALLY_RETRY_WITHOUT_CHANGED_EVIDENCE
  - DO_NOT_CLAIM_LEAST_PRIVILEGE_RAW_PROVIDER_PARITY_ACTUAL_QUOTA_USE_OR_ZERO_HIDDEN_RETRIES
  - DO_NOT_USE_CONNECTOR_RESULTS_AS_TERMINAL_PRODUCER_EVIDENCE_WITHOUT_CLAIM_REQUEST_AND_RETURN_DIGEST_BINDINGS
  - REQUIRE_DISTINCT_RAW_WITNESS_NAMED_OPERATIONAL_CONSUMER_ACK_AND_MEASURED_OPERATOR_OUTCOME_BEFORE_OPERATIONAL_OR_FITNESS_CREDIT
adopted_boundary:
  allowed: BOUNDED_READONLY_CATALOG_DISCOVERY_AND_LOW_ASSURANCE_SMALL_FULL_SHA_RELATION_CHECKS
  forbidden:
    - MERGE_OR_RELEASE_GATING_WITHOUT_INDEPENDENT_VERIFICATION
    - LARGE_OR_UNBOUNDED_COMPARISON_COMPLETENESS_CLAIMS
    - PERMISSION_OR_EXISTENCE_INFERENCE_FROM_404
    - MUTATION_FILE_HYDRATION_PUBLICATION_OR_AUTOMATIC_RETRY
    - OPERATIONAL_ADOPTION_OR_FITNESS_CREDIT
honest_flaw: THE_CAMPAIGN_EXERCISED_ONLY_SAME_SHA_ONE_ADJACENT_SINGLE_FILE_DIFF_AND_ONE_SYNTHETIC_404; PRINCIPAL_SCOPE_RAW_PARITY_PAGINATION_TRUNCATION_RENAMES_BINARY_DIFFS_LARGE_COMPARISONS_RATE_LIMITS_HIDDEN_RETRIES_PERMISSION_VARIANCE_CONSUMER_VALUE_AND_ACTUAL_TIME_SAVINGS_REMAIN_UNVERIFIED
next_campaign:
  candidate: Slack_bounded_readonly_message_search_metadata_surface
  next_phase: 1_of_4
  action_this_wake: NONE
review_expiry_utc: 2026-08-11T08:48:00Z
valid_time_utc: 2026-08-04T08:48:00Z
recorded_time_utc: 2026-08-04T08:48:00Z
---

# X13 GitHub compare-commits phase 4 decision

Decision: `ADOPT_WITH_GATES` for catalog-only, nonoperational use. The connector produced one content-addressed identical result, one small adjacent one-file result with returned bindings and file counts, and one fail-closed `404` without compare content. It avoided a small amount of request and normalization code, but removed zero measured operator minutes and has no consumer acknowledgment, raw-provider witness, identity or scope proof, quota telemetry, or completeness evidence. It must not gate merges, releases, or high-assurance decisions without independent verification.

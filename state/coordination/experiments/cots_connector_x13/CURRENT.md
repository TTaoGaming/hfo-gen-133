---
schema_id: hfo.gen133.x13.cots_connector_current.v1
experiment_id: X13_GITHUB_ACTIONS_WORKFLOW_RUN_STATUS_READONLY_001
version: 50
prior_version: 49
candidate: GitHub_Actions_bounded_workflow_run_status_readonly_surface
candidate_contract_reference: official_GitHub_Actions_workflow_runs_REST_contract_rate_limits_and_direct_connector_receipts
campaign_wake: 2_of_4
campaign_status: IN_PROGRESS
phase_1_completed: true
phase_2_completed: true
phase_3_completed: false
phase_4_completed: false
phase_4_decision: PENDING
last_event:
  commit: 7df61934a9b2795fa48e1fdd304511e0a63b4344
  path: state/coordination/experiments/cots_connector_x13/20260802T225015Z_GITHUB_ACTIONS_WORKFLOW_RUN_STATUS_PHASE2_POSITIVE_FAILURE.md
  blob_sha: 6ca9bd5b5d19629a857868838add7236e4a6c6a0
  exact_readback_completed: true
prior_current_commit: 3ba4fc33704e8c19c3fbfe1e9b8e3fdf54ad3bd4
prior_current_blob_sha: f9e5a1247d4bb28fea4e5a421f7e5bb83b724634
carrier_task_id: 6a55c1733708819185088bf334e33ea5
carrier_task_id_match: true
carrier_task_id_observation_source: AUTOMATION_RUN_CONTEXT
effect_ceiling: PHASE2_SOURCE_DISCOVERY_ONE_BOUNDED_POSITIVE_READONLY_COMMIT_WORKFLOW_RUN_STATUS_RECEIPT_GIT_EVENT_CURRENT_ADVANCE_READBACK_AND_ONE_SHORT_REDACTED_SLACK_FACT
adoption_credit: 2
adoption_credit_basis:
  - OFFICIAL_PRIMARY_WORKFLOW_RUNS_AND_RATE_LIMIT_CONTRACT
  - PHASE1_BOUNDED_EMPTY_RESULT_SCOPE_BASELINE
  - PHASE2_SOURCE_BOUND_POSITIVE_WORKFLOW_RUN_PAYLOAD
  - EXPLICIT_TRANSPORT_SUCCESS_VS_WORKFLOW_FAILURE_SEPARATION
fitness_credit: 0_PENDING_SOURCE_BOUND_CONSUMER_ACK_AND_MEASURED_OPERATOR_OUTCOME
consumer_ack: NOT_OBSERVED
same_provider_binding_weight: 1_CORROBORATIVE_NOT_INDEPENDENT
independent_verification_closed: false
operator_relay_minutes: 0
operator_minutes_removed_measured: 0
operator_minutes_removed_estimate_per_known_commit_status_check: 1_to_3_UNVALIDATED
custom_code_avoided_estimate:
  authenticated_commit_lookup_and_normalized_run_status_extraction: 35_to_110_LOC_UNVALIDATED
custom_policy_not_avoided:
  - ACCOUNT_IDENTITY_CREDENTIAL_TYPE_AND_AUTHORITY
  - ACTIONS_READ_PERMISSION_AND_LEAST_PRIVILEGE_VERIFICATION
  - EVENT_BRANCH_COMMIT_ATTEMPT_AND_LATEST_RUN_SCOPE_POLICY
  - EMPTY_RESULT_AND_COMPLETENESS_SEMANTICS
  - PAGINATION_ORDERING_AND_MULTIPLE_RUN_SELECTION
  - RATE_LIMIT_RETRY_AND_BACKOFF
  - WEBHOOK_OR_POLLING_DURABILITY_POLICY
  - INDEPENDENT_VERIFICATION
credentials:
  connector_reached_github_without_error: true
  operator_supplied_credentials: 0
  authenticated_user_or_app_identity: UNKNOWN
  credential_type: UNKNOWN
  repository_visibility: UNKNOWN
  live_actions_permission: UNKNOWN
  oauth_pat_app_scope: UNKNOWN
  delegated_or_direct_authority: UNKNOWN
  credential_custody: UNKNOWN
  least_privilege_closed: false
paid_cost_usd_observed: 0_NO_CHARGE_SURFACED
campaign_candidate_invocations:
  phase_1_commit_workflow_runs_queries: 1
  phase_2_source_discovery_reads_total: 13
  phase_2_commit_workflow_runs_queries: 4
  phase_2_positive_run_payloads: 1
  phase_3_failure_permission_portability_probe: 0
  phase_4_decision_only: 0
actual_upstream_request_count: UNKNOWN_AT_LEAST_14_READONLY_CONNECTOR_CALLS_ACROSS_PHASES_1_AND_2
actual_quota_units_consumed: UNKNOWN
actual_quota_class: UNKNOWN
retry_count: 0_AT_CARRIER_LEVEL_UPSTREAM_UNKNOWN
billing_counters: NOT_EXPOSED
live_request_id_retry_after_rate_limit_or_quota_headers: NOT_EXPOSED
direct_phase_1_receipt:
  repository: TTaoGaming/hfo-gen-133
  commit_sha: 5ddb21762d27a4349c0707cc163b58352d36481d
  commit_role: CURRENT_V48_UPDATE_COMMIT
  connector_action: fetch_commit_workflow_runs
  wrapper_documented_event_filter: pull_request
  wrapper_documented_page_scope: first_page_only
  connector_error: null
  returned_workflow_run_count: 0
  external_call_time_ms: 386
  write_side_effect: false
  carrier_retries: 0
  interpretation: NO_MATCH_IN_WRAPPER_SCOPE_NOT_PROOF_OF_NO_WORKFLOW_RUNS
direct_phase_2_source_binding:
  repository: TTaoGaming/hive-fleet-obsidian-gen-132
  pull_request_number: 20
  pull_request_title: test_gen132_roundtrip_held_out_branch_push_PR_CI_gate_probe
  pull_request_state: open
  pull_request_draft: false
  pull_request_merged: false
  head_branch: agent/olrun-git-exemplar-selftest
  head_commit_sha: abcf741c0d6cd654f3fdcc02d331245861406931
  binding_limit: PR_METADATA_AND_PROSE_ARE_SOURCE_CONTEXT_NOT_INDEPENDENT_RUN_VERIFICATION
direct_phase_2_receipt:
  connector_action: fetch_commit_workflow_runs
  repository: TTaoGaming/hive-fleet-obsidian-gen-132
  commit_sha: abcf741c0d6cd654f3fdcc02d331245861406931
  wrapper_documented_event_filter: pull_request
  wrapper_documented_page_scope: first_page_only
  connector_error: null
  returned_workflow_run_count: 1
  run_id: 30493905584
  workflow_name: HFO_Conformance_Gate
  workflow_id: 321534087
  run_number: 1551
  status: completed
  conclusion: failure
  jobs_url_present_not_dereferenced: true
  logs_url_present_not_dereferenced: true
  external_call_time_ms: 516
  write_side_effect: false
  carrier_retries: 0
  interpretation: POSITIVE_STATUS_PAYLOAD_WORKFLOW_COMPLETED_WITH_FAILURE_WHILE_CONNECTOR_CALL_SUCCEEDED
official_contract_checked_2026_08_02:
  workflow_runs: https://docs.github.com/en/rest/actions/workflow-runs?apiVersion=2026-03-10
  rate_limits: https://docs.github.com/en/rest/using-the-rest-api/rate-limits-for-the-rest-api
  best_practices: https://docs.github.com/en/rest/using-the-rest-api/best-practices-for-using-the-rest-api
  endpoint: GET_/repos/{owner}/{repo}/actions/runs
  supported_filters:
    - actor
    - branch
    - event
    - status_or_conclusion
    - created
    - exclude_pull_requests
    - check_suite_id
    - head_sha
  documented_status_or_conclusion_values_observed_here:
    - completed
    - failure
  per_page_max: 100
  filtered_search_result_cap: 1000
  fine_grained_permission: ACTIONS_READ
  public_resource_unauthenticated_use_possible: true
  private_repository_classic_token_scope: repo
  general_authenticated_primary_limit_requests_per_hour: 5000_COMMON_CASE
  github_app_installation_minimum_requests_per_hour: 5000_WITH_SCALING_AND_ENTERPRISE_VARIANCE
  github_token_requests_per_hour_per_repository: 1000_NON_ENTERPRISE_CLOUD
  most_REST_GET_secondary_points: 1
  rate_limit_headers_expected_on_raw_response: true
  webhook_preferred_over_polling: true
failure_semantics:
  phase_1_bounded_commit_query: DIRECTLY_OBSERVED_SUCCESS_WITH_EMPTY_ARRAY
  phase_2_positive_run_payload: DIRECTLY_OBSERVED
  workflow_level_failure_as_data: DIRECTLY_OBSERVED_STATUS_COMPLETED_CONCLUSION_FAILURE
  connector_transport_error_on_positive_call: NOT_OBSERVED
  empty_result_completeness: NOT_PROVEN
  event_scope_variance: CONNECTOR_CONTRACT_FORCES_PULL_REQUEST
  first_page_only: CONNECTOR_CONTRACT_DOCUMENTED
  branch_wide_status: NOT_TESTED
  run_identity_status_conclusion_normalization: OBSERVED_FOR_ONE_RECORD
  run_attempt_semantics: NOT_EXPOSED_NOT_TESTED
  ordering_and_latest_run_selection: NOT_TESTED
  pagination: NOT_TESTED
  permission_denial: NOT_TESTED
  authentication_failure: NOT_TESTED
  not_found_masking: NOT_TESTED
  malformed_commit_input: NOT_TESTED
  quota_or_rate_limit: NOT_TESTED
  transient_server_failure: NOT_TESTED
  independent_raw_or_UI_readback: NOT_TESTED
durability: EPHEMERAL_POINT_IN_TIME_QUERY_OVER_MUTABLE_WORKFLOW_RUN_AND_RERUN_STATE_NOT_A_DURABLE_EVENT_STREAM_OR_LATEST_STATUS_GUARANTEE
observability: MEDIUM_LOW_NORMALIZED_RUN_ID_WORKFLOW_ID_NAME_RUN_NUMBER_STATUS_CONCLUSION_URL_PRESENCE_AND_CONNECTOR_TIME_VISIBLE_RAW_HTTP_EVENT_HEAD_SHA_BRANCH_ACTOR_TIMESTAMPS_ATTEMPT_PAGINATION_REQUEST_ID_RATE_LIMITS_AND_UPSTREAM_RETRIES_HIDDEN
portability: MEDIUM_LOW_COMMIT_SHA_AND_PASS_FAIL_CONCEPTS_PORTABLE_GITHUB_RUN_WORKFLOW_EVENT_CONCLUSION_AND_WRAPPER_SEMANTICS_PROVIDER_SPECIFIC
admitted_scope:
  - BOUNDED_READ_ONLY_COMMIT_SCOPED_WORKFLOW_RUN_LOOKUP
  - EXPLICIT_INTERPRETATION_OF_EMPTY_RESULT_AS_WRAPPER_SCOPED_NO_MATCH
  - TIMESTAMPED_STATUS_OBSERVATION_ONLY
  - NORMALIZED_RUN_ID_WORKFLOW_ID_NAME_RUN_NUMBER_STATUS_AND_CONCLUSION_FOR_ONE_OBSERVED_POSITIVE_RECORD
  - EXPLICIT_SEPARATION_OF_CONNECTOR_CALL_SUCCESS_FROM_WORKFLOW_CONCLUSION
excluded_scope:
  - WORKFLOW_DISPATCH
  - RERUN_OR_RETRY
  - CANCELLATION
  - ARTIFACT_DOWNLOAD
  - LOG_DOWNLOAD
  - JOB_OR_STEP_HYDRATION
  - SECRET_OR_ENVIRONMENT_ACCESS
  - WORKFLOW_FILE_OR_BRANCH_MUTATION
  - MERGE_OR_REPOSITORY_SETTING_MUTATION
  - LATEST_ATTEMPT_OR_COMPLETE_HISTORY_CLAIMS
  - REPOSITORY_WIDE_OR_BRANCH_WIDE_HEALTH_CLAIMS
mandatory_gates:
  - TREAT_CONNECTOR_CALL_SUCCESS_AND_WORKFLOW_RUN_SUCCESS_AS_SEPARATE_STATES
  - INTERPRET_STATUS_COMPLETED_PLUS_CONCLUSION_FAILURE_AS_FINISHED_FAILING_WORKFLOW_NOT_TRANSPORT_FAILURE_AND_NOT_PASS
  - BIND_EVERY_STATUS_OBSERVATION_TO_EXACT_REPOSITORY_COMMIT_OBSERVATION_TIME_AND_RUN_ID
  - TREAT_EMPTY_ARRAY_AS_NO_MATCH_IN_PULL_REQUEST_FIRST_PAGE_WRAPPER_SCOPE_NOT_NO_WORKFLOW_RUNS
  - DO_NOT_INFER_LATEST_ATTEMPT_ONLY_ATTEMPT_COMPLETE_HISTORY_BRANCH_WIDE_REPOSITORY_WIDE_OR_ALL_EVENT_CI_STATE
  - DO_NOT_TREAT_PR_PROSE_AS_VALIDATED_BY_RUN_EXISTENCE
  - DO_NOT_INFER_IDENTITY_CREDENTIAL_TYPE_SCOPE_REPOSITORY_VISIBILITY_ACTIONS_PERMISSION_RATE_LIMIT_BILLING_OR_WRITE_AUTHORITY_FROM_SUCCESS
  - KEEP_JOB_STEP_LOG_ARTIFACT_DISPATCH_RERUN_CANCEL_SECRET_WORKFLOW_BRANCH_MERGE_AND_SETTINGS_EFFECTS_EXCLUDED
  - USE_EXACT_KNOWN_REPOSITORY_AND_COMMIT_FOR_NORMAL_CHECKS_AVOID_BROAD_PR_SEARCH_AS_ROUTINE_MONITORING
  - USE_BOUNDED_POLLING_WITH_RATE_LIMIT_HANDLING_OR_PREFER_WEBHOOKS_FOR_DURABLE_HIGH_FREQUENCY_PROPAGATION
  - SEPARATE_EMPTY_RESULT_CLIENT_INPUT_AUTHENTICATION_AUTHORIZATION_NOT_FOUND_RATE_LIMIT_TRANSIENT_AND_WORKFLOW_FAILURE_STATES
verifier: SOURCE_BOUND_RAW_GITHUB_WORKFLOW_RUNS_ENDPOINT_OR_ACTIONS_UI_FOR_REPOSITORY_TTaoGaming_HIVE_FLEET_OBSIDIAN_GEN_132_COMMIT_ABCF741C0D6CD654F3FDCC02D331245861406931_RUN_30493905584_WITH_EXPLICIT_EVENT_AND_PAGE_POLICY
consumer:
  - HFO_CI_RELEASE_GATES
  - HFO_BRANCH_HEALTH_SUMMARIES
  - HFO_AGENT_COMPLETION_VERIFICATION
strongest_falsifier: RAW_ENDPOINT_OR_ACTIONS_UI_SHOWS_DIFFERENT_RUN_ID_STATUS_OR_CONCLUSION_FOR_THE_SAME_SOURCE_BINDING_OR_SHOWS_NEWER_ADDITIONAL_RELEVANT_ATTEMPTS_OMITTED_BY_FORCED_EVENT_FILTER_FIRST_PAGE_OR_NORMALIZATION
honest_flaw: ONE_POSITIVE_FAILURE_RECORD_NOT_INDEPENDENTLY_READ_BACK_JOBS_LOGS_EVENT_BRANCH_ACTOR_TIMESTAMPS_ATTEMPT_HEAD_SHA_ECHO_PAGINATION_RATE_LIMITS_AND_FAILURE_CAUSE_HIDDEN_DISCOVERY_REQUIRED_13_READONLY_CALLS_CONSUMER_ACK_ABSENT
phase_1_result:
  disposition: PHASE1_ACCEPTED_WITH_EVENT_SCOPE_AND_EMPTY_RESULT_GATES
phase_2_result:
  disposition: PHASE2_ACCEPTED_WITH_POSITIVE_FAILURE_STATUS_AND_SCOPE_GATES
next_wake:
  phase: 3_of_4
  proposed_action: ONE_PRIVACY_SAFE_READONLY_MALFORMED_COMMIT_INPUT_PROBE_AGAINST_THE_SAME_PUBLIC_REPOSITORY_WITH_NO_RETRY_OR_MUTATION
  acceptance_question: DOES_CONNECTOR_FAIL_CLOSED_WITH_DISTINGUISHABLE_CLIENT_INPUT_ERROR_OR_SILENTLY_NORMALIZE_INVALID_INPUT_TO_EMPTY_RESULT
  exclusions:
    - CREDENTIAL_OR_PERMISSION_MUTATION
    - WORKFLOW_DISPATCH
    - RERUN
    - CANCEL
    - JOB_STEP_ARTIFACT_OR_LOG_DOWNLOAD
    - SECRET_READ
    - WORKFLOW_BRANCH_MERGE_OR_REPOSITORY_SETTING_MUTATION
review_expiry_utc: 2026-08-09T22:50:15Z
valid_time_utc: 2026-08-02T22:50:15Z
transaction_time_utc: SEE_GIT_COMMIT_METADATA
sealed: true
prior_campaign:
  experiment_id: X13_GOOGLE_DRIVE_BOUNDED_METADATA_SEARCH_READONLY_001
  final_version: 48
  decision: ADOPT_WITH_GATES
prior_prior_campaign:
  experiment_id: X13_GMAIL_BOUNDED_METADATA_SEARCH_READONLY_001
  final_version: 44
  decision: ADOPT_WITH_GATES
---

# X13 current campaign

GitHub Actions bounded commit workflow-run status completed phase **2/4** with disposition **`PHASE2_ACCEPTED_WITH_POSITIVE_FAILURE_STATUS_AND_SCOPE_GATES`**.

A source-bound read against Gen-132 PR #20 head `abcf741c0d6cd654f3fdcc02d331245861406931` returned one `HFO Conformance Gate` record: run `30493905584`, `status=completed`, `conclusion=failure`, with no connector error in 516 ms. This proves the connector can return a positive normalized status payload and correctly keeps workflow failure as data distinct from connector-call success.

Measured operator relief remains `0`; surfaced cost was `$0`; fitness credit remains `0`. The result does not prove latest-attempt selection, completeness, failure cause, independent fidelity, or general repository health.

Next wake performs one malformed-commit read-only failure probe. No workflow, job, artifact, log, branch, merge, secret, credential, repository setting, or scheduled task will be mutated.
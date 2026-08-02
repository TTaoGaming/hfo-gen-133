---
schema_id: hfo.gen133.x13.cots_connector_current.v1
experiment_id: X13_GITHUB_ACTIONS_WORKFLOW_RUN_STATUS_READONLY_001
version: 49
prior_version: 48
candidate: GitHub_Actions_bounded_workflow_run_status_readonly_surface
candidate_contract_reference: official_GitHub_Actions_workflow_runs_REST_contract_rate_limits_and_direct_connector_receipt
campaign_wake: 1_of_4
campaign_status: IN_PROGRESS
phase_1_completed: true
phase_2_completed: false
phase_3_completed: false
phase_4_completed: false
phase_4_decision: PENDING
last_event:
  commit: 89228eb6d38f28ee2af0692ea7e4b8eaa15c1382
  path: state/coordination/experiments/cots_connector_x13/20260802T214851Z_GITHUB_ACTIONS_WORKFLOW_RUN_STATUS_PHASE1_BASELINE.md
  blob_sha: 4a53da46d5c6f5d24f3413208cad73810eb98592
  exact_readback_completed: true
prior_current_commit: 5ddb21762d27a4349c0707cc163b58352d36481d
prior_current_blob_sha: f78f28dc896603c9396bcc61c68f5f8b83cb3fc2
carrier_task_id: 6a55c1733708819185088bf334e33ea5
carrier_task_id_match: true
carrier_task_id_observation_source: AUTOMATION_RUN_CONTEXT
effect_ceiling: PHASE1_OFFICIAL_CONTRACT_ONE_BOUNDED_READONLY_COMMIT_WORKFLOW_RUN_QUERY_GIT_EVENT_CURRENT_ADVANCE_READBACK_AND_ONE_SHORT_REDACTED_SLACK_ANDON
adoption_credit: 1
adoption_credit_basis:
  - OFFICIAL_PRIMARY_WORKFLOW_RUNS_AND_RATE_LIMIT_CONTRACT
  - ONE_BOUNDED_COMMIT_SCOPED_READONLY_CONNECTOR_QUERY
  - EXPLICIT_EMPTY_RESULT_SCOPE_GATE
fitness_credit: 0_PENDING_POSITIVE_RUN_RECEIPT_SOURCE_BOUND_CONSUMER_ACK_AND_MEASURED_OPERATOR_OUTCOME
consumer_ack: NOT_OBSERVED
same_provider_binding_weight: 0
independent_verification_closed: false
operator_relay_minutes: 0
operator_minutes_removed_measured: 0
operator_minutes_removed_estimate_per_status_check: 1_to_3_UNVALIDATED
custom_code_avoided_estimate:
  authenticated_commit_filtered_listing_and_normalization: 25_to_80_LOC_UNVALIDATED
custom_policy_not_avoided:
  - ACCOUNT_IDENTITY_CREDENTIAL_TYPE_AND_AUTHORITY
  - ACTIONS_READ_PERMISSION_AND_LEAST_PRIVILEGE_VERIFICATION
  - EVENT_BRANCH_COMMIT_AND_ATTEMPT_SCOPE_POLICY
  - EMPTY_RESULT_AND_COMPLETENESS_SEMANTICS
  - PAGINATION_AND_ORDERING
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
  phase_1_commit_workflow_runs_query: 1
  phase_2_positive_micro_use: 0
  phase_3_failure_permission_portability_probe: 0
  phase_4_decision_only: 0
actual_upstream_request_count: UNKNOWN_AT_LEAST_ONE_CONNECTOR_EXTERNAL_CALL
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
official_contract_checked_2026_08_02:
  workflow_runs: https://docs.github.com/en/rest/actions/workflow-runs?apiVersion=2026-03-10
  rate_limits: https://docs.github.com/en/rest/using-the-rest-api/rate-limits-for-the-rest-api
  best_practices: https://docs.github.com/en/rest/using-the-rest-api/best-practices-for-using-the-rest-api
  endpoint: GET_/repos/{owner}/{repo}/actions/runs
  supported_filters:
    - actor
    - branch
    - event
    - status
    - created
    - exclude_pull_requests
    - check_suite_id
    - head_sha
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
  bounded_commit_query: DIRECTLY_OBSERVED_SUCCESS_WITH_EMPTY_ARRAY
  positive_run_payload: NOT_OBSERVED
  empty_result_completeness: NOT_PROVEN
  event_scope_variance: CONNECTOR_CONTRACT_FORCES_PULL_REQUEST
  first_page_only: CONNECTOR_CONTRACT_DOCUMENTED
  branch_wide_status: NOT_TESTED
  run_status_and_conclusion_fidelity: NOT_TESTED
  rerun_attempt_semantics: NOT_TESTED
  pagination: NOT_TESTED
  permission_denial: NOT_TESTED
  authentication_failure: NOT_TESTED
  not_found_masking: NOT_TESTED
  quota_or_rate_limit: NOT_TESTED
  transient_server_failure: NOT_TESTED
  independent_raw_or_UI_readback: NOT_TESTED
durability: EPHEMERAL_POINT_IN_TIME_QUERY_OVER_MUTABLE_WORKFLOW_RUN_AND_ATTEMPT_STATE_NOT_A_DURABLE_EVENT_STREAM
observability: LOW_EMPTY_NORMALIZED_ARRAY_AND_CONNECTOR_TIME_VISIBLE_RAW_HTTP_URL_STATUS_HEADERS_REQUEST_ID_FILTERS_PAGINATION_RATE_LIMITS_AND_UPSTREAM_RETRIES_HIDDEN
portability: MEDIUM_LOW_COMMIT_SHA_IS_PORTABLE_BUT_GITHUB_ACTIONS_EVENT_STATUS_CONCLUSION_RUN_ATTEMPT_AND_WRAPPER_FILTERS_ARE_PROVIDER_SPECIFIC
admitted_scope:
  - BOUNDED_READ_ONLY_COMMIT_SCOPED_WORKFLOW_RUN_LOOKUP
  - EXPLICIT_INTERPRETATION_OF_EMPTY_RESULT_AS_WRAPPER_SCOPED_NO_MATCH
  - TIMESTAMPED_STATUS_OBSERVATION_ONLY
excluded_scope:
  - WORKFLOW_DISPATCH
  - RERUN_OR_RETRY
  - CANCELLATION
  - ARTIFACT_DOWNLOAD
  - LOG_DOWNLOAD
  - JOB_OR_STEP_HYDRATION_UNTIL_SEPARATELY_ADMITTED
  - SECRET_OR_ENVIRONMENT_ACCESS
  - WORKFLOW_FILE_OR_BRANCH_MUTATION
  - REPOSITORY_WIDE_OR_BRANCH_WIDE_HEALTH_CLAIMS
mandatory_gates:
  - TREAT_EMPTY_ARRAY_AS_NO_MATCH_IN_PULL_REQUEST_FIRST_PAGE_WRAPPER_SCOPE_NOT_NO_WORKFLOW_RUNS
  - RECORD_EXACT_COMMIT_SHA_AND_OBSERVATION_TIME
  - DO_NOT_INFER_BRANCH_WIDE_REPOSITORY_WIDE_OR_ALL_EVENT_CI_STATE
  - REQUIRE_POSITIVE_RUN_RECEIPT_BEFORE_ADMITTING_STATUS_CONCLUSION_ATTEMPT_EVENT_WORKFLOW_OR_TIMESTAMP_FIELD_FIDELITY
  - DO_NOT_INFER_IDENTITY_CREDENTIAL_TYPE_SCOPE_REPOSITORY_VISIBILITY_ACTIONS_PERMISSION_RATE_LIMIT_BILLING_OR_WRITE_AUTHORITY_FROM_SUCCESS
  - KEEP_DISPATCH_RERUN_CANCEL_ARTIFACT_LOG_SECRET_WORKFLOW_AND_BRANCH_MUTATIONS_EXCLUDED
  - USE_BOUNDED_POLLING_WITH_RATE_LIMIT_HANDLING_OR_PREFER_WEBHOOKS_FOR_DURABLE_HIGH_FREQUENCY_PROPAGATION
  - SEPARATE_EMPTY_RESULT_AUTHENTICATION_AUTHORIZATION_NOT_FOUND_RATE_LIMIT_AND_TRANSIENT_FAILURES
verifier: SOURCE_BOUND_RAW_GITHUB_WORKFLOW_RUNS_ENDPOINT_WITH_EXPLICIT_HEAD_SHA_EVENT_AND_PAGE_POLICY_OR_GITHUB_ACTIONS_CHECKS_UI_FOR_THE_SAME_COMMIT
consumer:
  - HFO_CI_RELEASE_GATES
  - HFO_BRANCH_HEALTH_SUMMARIES
  - HFO_AGENT_COMPLETION_VERIFICATION
strongest_falsifier: RAW_ENDPOINT_OR_GITHUB_UI_SHOWS_ONE_OR_MORE_RUNS_FOR_THE_SAME_COMMIT_WHILE_CONNECTOR_RETURNS_EMPTY_DUE_TO_FORCED_PULL_REQUEST_FILTER_FIRST_PAGE_TRUNCATION_NORMALIZATION_OR_PERMISSION_VARIANCE
honest_flaw: NO_POSITIVE_RUN_PAYLOAD_STATUS_CONCLUSION_ORDERING_ATTEMPT_PAGINATION_EVENT_VARIANCE_401_403_404_429_5XX_RATE_LIMIT_HEADERS_INDEPENDENT_READBACK_OR_CONSUMER_ACK_TARGET_COMMIT_MAY_HAVE_NO_PULL_REQUEST_TRIGGERED_RUN
phase_1_result:
  disposition: PHASE1_ACCEPTED_WITH_EVENT_SCOPE_AND_EMPTY_RESULT_GATES
next_wake:
  phase: 2_of_4
  proposed_action: LOCATE_ONE_SOURCE_BOUND_COMMIT_KNOWN_TO_HAVE_A_PULL_REQUEST_TRIGGERED_WORKFLOW_RUN_AND_PERFORM_ONE_BOUNDED_READ_ONLY_POSITIVE_STATUS_QUERY
  fallback_if_no_positive_candidate: RECORD_UNKNOWN_WITHOUT_CREATING_OR_DISPATCHING_WORKFLOW_ACTIVITY
  exclusions:
    - WORKFLOW_DISPATCH
    - RERUN
    - CANCEL
    - ARTIFACT_OR_LOG_DOWNLOAD
    - SECRET_READ
    - WORKFLOW_OR_BRANCH_MUTATION
review_expiry_utc: 2026-08-09T21:48:51Z
valid_time_utc: 2026-08-02T21:48:51Z
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

GitHub Actions bounded commit workflow-run status completed phase **1/4** with disposition **`PHASE1_ACCEPTED_WITH_EVENT_SCOPE_AND_EMPTY_RESULT_GATES`**.

A read-only query against the CURRENT v48 commit returned zero runs with no connector error in 386 ms. The connector wrapper is documented to force `pull_request` event filtering and return only the first page, so the result means only **no match in that wrapper scope**; it is not proof that the commit has no Actions runs or checks.

Measured operator relief remains `0`; surfaced cost was `$0`; fitness credit remains `0`. A positive run payload is required before field fidelity or general CI-status usefulness can be admitted.

Next wake seeks one existing source-bound commit with a pull-request-triggered run for a positive read-only micro-use. No workflow activity will be created or mutated.
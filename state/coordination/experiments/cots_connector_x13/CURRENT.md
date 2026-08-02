---
schema_id: hfo.gen133.x13.cots_connector_current.v1
experiment_id: X13_GITHUB_CONTENTS_CONNECTOR_001
version: 32
prior_version: 31
candidate: GitHub_contents_API_branch_scoped_file_create_update_fetch_and_readback_connector
candidate_contract_reference: official_GitHub_repository_contents_and_REST_rate_limit_contract_plus_direct_connector_receipts
campaign_wake: 4_of_4
campaign_status: COMPLETE
phase_1_completed: true
phase_2_completed: true
phase_3_completed: true
phase_4_completed: true
phase_4_decision: ADOPT_WITH_GATES
decision_event:
  commit: 1c921066a994009f3ae76654cdec7a3fd8c1004c
  path: state/coordination/experiments/cots_connector_x13/20260802T044800Z_GITHUB_CONTENTS_PHASE4_DECISION_ADOPT_WITH_GATES.md
  blob_sha: 742e6230ee3fa1894b802517c0d076129c90bd8e
  exact_readback_completed: true
last_event:
  commit: 6e6f8f669353445f78d7b6e030c20bc6d89558d4
  path: state/coordination/experiments/cots_connector_x13/20260802T044900Z_GITHUB_CONTENTS_PHASE4_VERIFIER_RECONCILIATION.md
  blob_sha: ef0ed01fd35f7ba5d034434a12116527cc5ac4db
  exact_readback_completed: true
prior_current_commit: 3501ce8a820add8da1b625ad7089f98f269b8c3a
prior_current_blob_sha: 9da60e1775155d07af5bf3ef84edffc3b5c6ac37
carrier_task_id: 6a55c1733708819185088bf334e33ea5
carrier_task_id_match: true
carrier_task_id_observation_source: AUTOMATION_RUN_CONTEXT
effect_ceiling: GIT_FIRST_PHASE4_DECISION_AND_CURRENT_ADVANCE_PLUS_SANITIZED_SLACK_DECISION_RECEIPT_ONLY_NO_MERGE_DELETE_FORCE_PUSH_BRANCH_CREATE_WORKFLOW_EDIT_OR_PRODUCTION_EFFECT
adoption_credit: 4
adoption_credit_basis:
  - OFFICIAL_PRIMARY_CONTRACT
  - ONE_BRANCH_SCOPED_EXISTING_FILE_FETCH
  - ONE_UNIQUELY_NAMED_SMALL_UTF8_FILE_CREATE
  - EXACT_BRANCH_PATH_BODY_AND_BLOB_READBACK
  - ONE_SYNTHETIC_NONCURRENT_BLOB_SHA_UPDATE_REJECTED_AS_409
  - ORIGINAL_BODY_AND_BLOB_PRESERVED_AFTER_FAILED_UPDATE
  - PHASE4_DECISION_EVENT_EXACT_READBACK
  - X14_VERIFIER_STATE_RECONCILED_WITHOUT_PROMOTING_BINDING_WEIGHT
fitness_credit: 0_PENDING_EXPLICIT_SOURCE_BOUND_CONSUMER_ACK_AND_MEASURED_OPERATOR_OUTCOME
consumer_ack: NOT_OBSERVED
same_provider_binding_weight: 0
independent_verification_closed: false
operator_relay_minutes: 0
operator_minutes_removed_measured: 0
operator_minutes_removed_estimate_per_bounded_event_and_readback: 1_to_4_UNVALIDATED
custom_code_avoided_estimate:
  authenticated_branch_path_fetch_and_decode: 25_to_70_LOC_UNVALIDATED
  authenticated_create_update_and_base64_request_handling: 40_to_100_LOC_UNVALIDATED
  blob_SHA_optimistic_update_plumbing: 20_to_60_LOC_UNVALIDATED
  conflict_detection_and_normalization: 10_to_30_LOC_UNVALIDATED
  additive_total: NOT_CLAIMED_BECAUSE_FUNCTIONS_OVERLAP
custom_policy_not_avoided:
  - EXPLICIT_REF_SELECTION
  - VERSION_COMPARE_AND_SWAP
  - SERIAL_WRITE_ORDER
  - REFRESH_AND_RECONCILE_BEFORE_RETRY
  - MULTI_COMMIT_RECONCILIATION
  - ERROR_SANITIZATION
  - SECRET_AND_PRIVATE_CONTENT_EXCLUSION
  - CONSUMER_ACK
  - INDEPENDENT_VERIFICATION
credentials:
  connector_authenticated_or_repository_reachable: true
  operator_supplied_credentials: 0
  live_identity: UNKNOWN
  live_token_type: UNKNOWN
  live_permission_set: UNKNOWN
  credential_custody: UNKNOWN
paid_cost_usd_observed: 0_NO_CHARGE_SURFACED
campaign_candidate_invocations_phases_1_to_3: 5
campaign_bookkeeping_invocations_phases_1_to_3: 4
phase_4_new_candidate_invocations: 0
phase_4_decision_event_create_invocations: 1
phase_4_decision_event_readback_invocations: 1
phase_4_verifier_state_read_invocations: 1
phase_4_verifier_reconciliation_event_create_invocations: 1
phase_4_verifier_reconciliation_event_readback_invocations: 1
actual_upstream_request_count_and_secondary_points: UNKNOWN
actual_quota_class: UNKNOWN
billing_counters: NOT_EXPOSED
live_HTTP_status_headers_request_id_ETag_LastModified_or_rate_limit_headers: NOT_EXPOSED
official_contract_checked_2026_08_02:
  contents_api: https://docs.github.com/en/rest/repos/contents?apiVersion=2022-11-28#create-or-update-file-contents
  rate_limits: https://docs.github.com/en/rest/using-the-rest-api/rate-limits-for-the-rest-api
  get_content_ref: COMMIT_BRANCH_OR_TAG_DEFAULTS_TO_DEFAULT_BRANCH_IF_OMITTED
  create_update_encoding: BASE64_CONTENT
  update_precondition: CURRENT_BLOB_SHA_REQUIRED
  branch_default: DEFAULT_BRANCH_IF_OMITTED
  write_permission: CONTENTS_WRITE_WITH_ADDITIONAL_WORKFLOW_PERMISSION_FOR_WORKFLOW_FILES
  concurrency_warning: SERIALIZE_CREATE_UPDATE_AND_DELETE_TO_AVOID_CONFLICT
  documented_create_update_statuses:
    - 200
    - 201
    - 404
    - 409
    - 422
  public_unauthenticated_primary_limit_per_hour: 60
  authenticated_user_primary_limit_per_hour: 5000
  secondary_limits_exist_and_are_not_fully_static: true
  rate_limit_headers_preferred_but_hidden_by_connector: true
phase_receipts:
  phase_1:
    event_commit: 08af876e6175f2c5ca0d71258c9294a6dd95c10a
    event_path: state/coordination/experiments/cots_connector_x13/20260802T014800Z_GITHUB_CONTENTS_PHASE1_BASELINE.md
    event_blob_sha: 64a4a3289546cb451b58ff47b46ff45be6d31ef6
    result: EXPLICIT_REF_EXISTING_FILE_FETCH_AND_BASELINE_ACCEPTED
  phase_2:
    event_commit: 4858b38f0fa7fad9a73ca8be5d3a7c36abc99bc1
    event_path: state/coordination/experiments/cots_connector_x13/20260802T024800Z_GITHUB_CONTENTS_PHASE2_MICRO_ARTIFACT.md
    event_blob_sha: 538800f2b63a130014f5c6f88ab41c8f1385fc75
    result: UNIQUE_SMALL_UTF8_CREATE_AND_EXACT_BODY_BLOB_READBACK_ACCEPTED
  phase_3:
    event_commit: 6e595c86bb922b31672fd17f9b93a5448b090a28
    event_path: state/coordination/experiments/cots_connector_x13/20260802T034800Z_GITHUB_CONTENTS_PHASE3_STALE_SHA_CONFLICT.md
    event_blob_sha: fd6079b8781777e7ffa682864ac135313a39005a
    result: SYNTHETIC_NONCURRENT_SHA_REJECTED_AS_409_ORIGINAL_BODY_AND_BLOB_PRESERVED
  phase_4:
    decision: ADOPT_WITH_GATES
    decision_event_commit: 1c921066a994009f3ae76654cdec7a3fd8c1004c
    decision_event_blob_sha: 742e6230ee3fa1894b802517c0d076129c90bd8e
    verifier_reconciliation_commit: 6e6f8f669353445f78d7b6e030c20bc6d89558d4
    verifier_reconciliation_blob_sha: ef0ed01fd35f7ba5d034434a12116527cc5ac4db
failure_semantics:
  omitted_ref: MAY_READ_DEFAULT_BRANCH_AND_IS_NOT_ALLOWED_FOR_CANONICAL_STATE
  stale_update_SHA: DIRECTLY_PROBED_AND_REJECTED_AS_409_WITH_ORIGINAL_BODY_AND_BLOB_PRESERVED
  stale_update_recovery: REFRESH_CURRENT_BLOB_SHA_RECONCILE_EXPECTED_BODY_AND_VERSION_THEN_DECIDE_OR_ABORT
  blind_retry_after_409: PROHIBITED
  event_plus_CURRENT_update: TWO_COMMITS_NOT_ATOMIC_MULTI_FILE_TRANSACTION
  same_connector_readback: STRUCTURAL_RECONCILIATION_NOT_INDEPENDENT_VERIFICATION
  rate_limit_403_429: NOT_TESTED
  permission_403_404: NOT_TESTED
  validation_422: NOT_TESTED
  true_concurrent_writers: NOT_TESTED
durability: GIT_OBJECT_AND_BRANCH_HISTORY_ONLY_NO_WORKFLOW_REPLAY_RESUME_TRANSACTION_LEASE_IDEMPOTENCY_OR_EXACTLY_ONCE_CLAIM
observability: MEDIUM_FOR_REPOSITORY_PATH_REF_BODY_BLOB_SHA_DISPLAY_URL_COMMIT_SHA_CREATE_LATENCY_AND_CONFLICT_STATUS_BUT_LOW_FOR_HTTP_HEADERS_REQUEST_ID_CACHE_RETRIES_IDENTITY_PERMISSION_AND_QUOTA
portability: MEDIUM_FOR_REPOSITORY_PATH_REF_BODY_BLOB_AND_COMPARE_AND_SWAP_CONCEPTS_LOW_TO_MEDIUM_FOR_GITHUB_CONTENTS_API_BASE64_PERMISSION_NAMES_STATUS_NORMALIZATION_AND_WRAPPER_SHAPE
admitted_scope:
  - ONE_EXISTING_BRANCH
  - SMALL_UTF8_EXPERIMENT_AND_COORDINATION_TEXT_FILES
  - EXPLICIT_REF
  - SERIAL_CREATE_UPDATE_FETCH_READBACK
  - CURRENT_BLOB_SHA_COMPARE_AND_SWAP
  - GIT_FIRST_STATE_AND_IMMUTABLE_EVENTS
excluded_scope:
  - MERGE
  - DELETE
  - FORCE_PUSH
  - BRANCH_CREATION
  - WORKFLOW_FILE_EDIT
  - PRODUCTION_DEPLOYMENT
  - SECRET_BEARING_CONTENT
  - LARGE_BINARY_OR_GENERAL_ARTIFACT_TRANSPORT
  - EXACTLY_ONCE_OR_DURABLE_WORKFLOW_CLAIMS
mandatory_gates:
  - ALWAYS_PASS_EXPLICIT_BRANCH_OR_COMMIT_REF
  - REQUIRE_CURRENT_BLOB_SHA_BEFORE_UPDATE
  - SERIALIZE_WRITES_TO_THE_SAME_PATH
  - ON_409_DO_NOT_BLIND_RETRY
  - ON_409_REFRESH_CURRENT_BLOB_SHA_AND_RECONCILE_EXPECTED_BODY_AND_VERSION_BEFORE_DECIDING_OR_ABORTING
  - TREAT_EVENT_CREATE_AND_POINTER_UPDATE_AS_TWO_COMMITS_NOT_ATOMIC
  - READ_BACK_EXACT_EVENT_AND_CURRENT_AND_COMPARE_VERSION_PATH_BODY_AND_BLOB_SHA
  - DO_NOT_CLAIM_INDEPENDENT_VERIFICATION_FROM_SAME_CONNECTOR_READBACK
  - REQUIRE_DIRECT_S04_EXACT_CANDIDATE_REVIEW_OR_DISTINCT_COMMIT_PINNED_READER_FOR_BINDING_VERIFICATION
  - SANITIZE_ERROR_RECEIPTS_IF_PATHS_CONTENT_OR_IDENTIFIERS_ARE_PRIVATE
  - NO_MERGE_DELETE_FORCE_PUSH_BRANCH_CREATE_WORKFLOW_EDIT_OR_PRODUCTION_EFFECT
  - KEEP_ARTIFACTS_SMALL_UTF8_TEXT_ONLY
  - NO_LIVE_QUOTA_COST_OR_LEAST_PRIVILEGE_CLAIM_WITHOUT_DIRECT_EVIDENCE
  - NO_SECRET_BEARING_CONTENT
  - NO_OPERATOR_TIME_REMOVED_OR_FITNESS_CREDIT_WITHOUT_SOURCE_BOUND_CONSUMER_ACK
verifier_state:
  source: state/coordination/experiments/false_green_x14/CURRENT.yaml
  returned_version: 29
  returned_blob_sha: bb1b0684cb3f5ece92653d323f58f1590d3ccced
  campaign_decision: HOLD
  direct_s04_exact_mutant_verdicts_campaign_7: 0
  distinct_provider_verdicts: 0
  evidence_class: SAME_PROVIDER_NONBINDING
  binding_weight: 0
  interpretation: CLAIM_CEILING_SIGNAL_NOT_INDEPENDENT_ACCEPT_OR_REJECT_VERDICT
verifier: DIRECT_S04_EXACT_CANDIDATE_REVIEW_OR_DISTINCT_NONCARRIER_COMMIT_PINNED_READER
consumer:
  - GIT_FIRST_STATE_WRITERS_AND_READERS
  - X13_FUTURE_COTS_CAMPAIGNS
strongest_falsifier: A_FAILED_STALE_SHA_PROBE_CREATED_A_COMMIT_OR_CHANGED_CONTENT_OR_A_DISTINCT_COMMIT_PINNED_CLIENT_DISAGREES_WITH_THE_REPORTED_BODY_BLOB_OR_BRANCH_REF_OR_THE_CONNECTOR_IGNORES_AN_EXPLICIT_REF
honest_flaw: PHASE3_USED_A_DELIBERATELY_IMPOSSIBLE_ALL_ZERO_SHA_NOT_A_NATURALLY_STALE_PRIOR_BLOB_AND_ALL_BODY_AND_BLOB_RECONCILIATION_USED_THE_SAME_CONNECTOR_WITHOUT_PERMISSION_RATE_LIMIT_DEFAULT_BRANCH_TRUE_CONCURRENCY_OR_CROSS_CLIENT_VARIANCE_TESTS
next_campaign:
  experiment_id: X13_SLACK_NATIVE_MESSAGE_RECEIPT_001
  candidate: Slack_native_message_send_and_thread_receipt_surface
  phase: 1_of_4
  status: PLANNED
  effect_ceiling: OFFICIAL_CONTRACT_AND_READ_ONLY_BASELINE_OR_ONE_HARMLESS_MEASURED_FACT_POST_ONLY
review_expiry_utc: 2026-08-09T04:48:00Z
valid_time_utc: 2026-08-02T04:48:00Z
transaction_time_utc: SEE_GIT_COMMIT_METADATA
sealed: true
prior_campaign:
  experiment_id: X13_GOOGLE_CONTACTS_READONLY_CONNECTOR_001
  final_version: 28
  decision: ADOPT_WITH_GATES
  decision_commit: dff26eeef9989f0c9af9ee88c20c845df2388d49
prior_prior_campaign:
  experiment_id: X13_GOOGLE_DRIVE_READONLY_CONNECTOR_001
  final_version: 24
  decision: ADOPT_WITH_GATES
  decision_commit: c0f93c82fbae71f4bc301f62929d0bd072ee052f
---

# X13 current campaign

GitHub Contents branch-scoped small-text state handling completed at phase **4/4** with decision **ADOPT_WITH_GATES**.

The bounded evidence is one explicit-ref read, one uniquely named UTF-8 create with exact body/blob readback, and one synthetic noncurrent-SHA update rejected as HTTP 409 with the original body and blob preserved. The connector avoids authentication, Base64, request-shaping, and optimistic-concurrency plumbing, but it does not remove branch selection, compare-and-swap policy, serial writes, two-commit reconciliation, error sanitization, secret exclusion, ConsumerAck, or independent verification.

X14 currently reports HOLD for its mutation campaign because no direct S04 exact-mutant verdict or distinct-provider verdict exists. This leaves binding weight and fitness credit at zero and blocks any production-ready, portable, ungated, independently verified, or measured-operator-relief claim.

Next campaign: Slack native message and thread receipt surface, phase 1/4.

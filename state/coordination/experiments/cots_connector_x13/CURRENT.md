---
schema_id: hfo.gen133.x13.cots_connector_current.v1
experiment_id: X13_GITHUB_CONTENTS_CONNECTOR_001
version: 29
prior_version: 28
candidate: GitHub_contents_API_branch_scoped_file_create_update_fetch_and_readback_connector
candidate_contract_reference: official_GitHub_repository_contents_and_REST_rate_limit_contract_plus_direct_connector_receipts
campaign_wake: 1_of_4
campaign_status: ACTIVE
phase_1_completed: true
phase_2_completed: false
phase_3_completed: false
phase_4_completed: false
phase_4_decision: PENDING
last_event_commit: 08af876e6175f2c5ca0d71258c9294a6dd95c10a
last_event_path: state/coordination/experiments/cots_connector_x13/20260802T014800Z_GITHUB_CONTENTS_PHASE1_BASELINE.md
last_event_blob_sha: 64a4a3289546cb451b58ff47b46ff45be6d31ef6
prior_current_commit: b6493aac6386b72ddfaf97fc104c2ef8b9904d84
prior_current_blob_sha: 24fa0c71d82268d4908a2d52c2c4b6f861d2eb0b
carrier_task_id: 6a55c1733708819185088bf334e33ea5
carrier_task_id_match: true
carrier_task_id_observation_source: AUTOMATION_RUN_CONTEXT
effect_ceiling: HARMLESS_BRANCH_SCOPED_TEXT_EVENT_AND_READBACK_ONLY_NO_MERGE_DELETE_FORCE_PUSH_BRANCH_CREATION_WORKFLOW_EDIT_OR_PRODUCTION_CHANGE
adoption_credit: 1
adoption_credit_basis:
  - OFFICIAL_PRIMARY_CONTRACT
  - ONE_BRANCH_SCOPED_EXISTING_FILE_FETCH
  - ONE_IMMUTABLE_EVENT_CREATE_AND_READBACK_AS_BOOKKEEPING_NOT_INDEPENDENT_VERIFICATION
fitness_credit: 0_PENDING_EXPLICIT_SOURCE_BOUND_CONSUMER_ACK_AND_MEASURED_OPERATOR_OUTCOME
consumer_ack: NOT_OBSERVED
same_provider_binding_weight: 0
independent_verification_closed: false
operator_relay_minutes: 0
operator_minutes_removed_measured: 0
operator_minutes_removed_estimate_per_bounded_event_and_readback: 1_to_4_UNVALIDATED
custom_code_avoided_estimate:
  authenticated_branch_path_fetch_and_decode: 25_to_70_LOC_UNVALIDATED
  authenticated_create_update_and_Base64_request_handling: 40_to_100_LOC_UNVALIDATED
  blob_SHA_optimistic_update_plumbing: 20_to_60_LOC_UNVALIDATED
  additive_total: NOT_CLAIMED_BECAUSE_FUNCTIONS_OVERLAP
custom_policy_not_avoided:
  - EXPLICIT_REF_SELECTION
  - VERSION_COMPARE_AND_SWAP
  - SERIAL_WRITE_ORDER
  - MULTI_COMMIT_RECONCILIATION
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
phase_1_candidate_read_invocations: 1
phase_1_bookkeeping_create_invocations: 1
phase_1_bookkeeping_readback_invocations: 1
live_HTTP_status_headers_request_id_ETag_LastModified_or_rate_limit_headers: NOT_EXPOSED
actual_upstream_request_count_and_secondary_points: UNKNOWN
actual_quota_class: UNKNOWN
billing_counters: NOT_EXPOSED
phase_1_receipt:
  action: GitHub.fetch_file
  repository: TTaoGaming/hfo-gen-133
  path: state/coordination/experiments/cots_connector_x13/CURRENT.md
  requested_ref: agent/gen133-bootstrap-20260730
  encoding: utf-8
  result: SUCCESS_FILE_CONTENT
  returned_state_version: 28
  returned_blob_sha: 24fa0c71d82268d4908a2d52c2c4b6f861d2eb0b
  branch_qualified_display_url_returned: true
  file_body_returned: true
  response_headers_or_latency_exposed: false
phase_1_event_write_receipt:
  action: GitHub.create_file
  event_commit: 08af876e6175f2c5ca0d71258c9294a6dd95c10a
  event_blob_sha_after_readback: 64a4a3289546cb451b58ff47b46ff45be6d31ef6
  external_call_time_ms_create_exposed_by_connector: 754
  readback_body_and_blob_match_expected: true
official_contract_checked_2026_08_02:
  get_content_ref: COMMIT_BRANCH_OR_TAG_DEFAULTS_TO_DEFAULT_BRANCH_IF_OMITTED
  get_content_permission: CONTENTS_READ_FOR_NONPUBLIC_ACCESS
  get_content_size_support: FULL_TO_1MB_RAW_OR_OBJECT_1_TO_100MB_UNSUPPORTED_OVER_100MB
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
  rate_limit_headers_preferred_but_hidden_by_connector: true
failure_semantics:
  omitted_ref: MAY_READ_DEFAULT_BRANCH_AND_IS_NOT_ALLOWED_FOR_CANONICAL_STATE
  stale_update_SHA: EXPECT_CONFLICT_OR_VALIDATION_FAILURE_NOT_YET_PROBED
  event_plus_CURRENT_update: TWO_COMMITS_NOT_ATOMIC_MULTI_FILE_TRANSACTION
  same_connector_readback: STRUCTURAL_RECONCILIATION_NOT_INDEPENDENT_VERIFICATION
  rate_limit_403_429: NOT_TESTED
  permission_403_404: NOT_TESTED
  validation_409_422: NOT_TESTED
durability: GIT_OBJECT_AND_BRANCH_HISTORY_ONLY_NO_WORKFLOW_REPLAY_RESUME_TRANSACTION_LEASE_IDEMPOTENCY_OR_EXACTLY_ONCE_CLAIM
observability: MEDIUM_FOR_REPOSITORY_PATH_REF_BODY_BLOB_SHA_DISPLAY_URL_COMMIT_SHA_AND_CREATE_LATENCY_BUT_LOW_FOR_HTTP_HEADERS_REQUEST_ID_CACHE_RETRIES_IDENTITY_PERMISSION_AND_QUOTA
portability: MEDIUM_FOR_REPOSITORY_PATH_REF_BODY_BLOB_AND_COMPARE_AND_SWAP_CONCEPTS_LOW_TO_MEDIUM_FOR_GITHUB_CONTENTS_API_BASE64_PERMISSION_NAMES_STATUS_NORMALIZATION_AND_WRAPPER_SHAPE
admitted_scope:
  - ONE_EXISTING_BRANCH
  - ONE_SMALL_TEXT_FILE
  - EXPLICIT_REF
  - SERIAL_CREATE_UPDATE_FETCH_READBACK
  - EXPERIMENT_STATE_ONLY
mandatory_gates:
  - ALWAYS_PASS_EXPLICIT_BRANCH_OR_COMMIT_REF
  - REQUIRE_CURRENT_BLOB_SHA_BEFORE_UPDATE
  - SERIALIZE_WRITES_TO_THE_SAME_PATH
  - TREAT_EVENT_CREATE_AND_POINTER_UPDATE_AS_TWO_COMMITS_NOT_ATOMIC
  - READ_BACK_EXACT_EVENT_AND_CURRENT_AND_COMPARE_VERSION_PATH_AND_BLOB_SHA
  - DO_NOT_CLAIM_INDEPENDENT_VERIFICATION_FROM_SAME_CONNECTOR_READBACK
  - NO_MERGE_DELETE_FORCE_PUSH_BRANCH_CREATE_WORKFLOW_EDIT_OR_PRODUCTION_EFFECT
  - KEEP_ARTIFACTS_SMALL_TEXT_ONLY
  - NO_LIVE_QUOTA_COST_OR_LEAST_PRIVILEGE_CLAIM_WITHOUT_DIRECT_EVIDENCE
  - NO_SECRET_BEARING_CONTENT
verifier: S04_STRUCTURAL_PREFLIGHT_THEN_DISTINCT_NON_CARRIER_OR_COMMIT_PINNED_CLIENT_REVIEW
consumer:
  - X13_PHASE2
  - GIT_FIRST_STATE_READERS
strongest_falsifier: A_COMMIT_PINNED_INDEPENDENT_READ_DISAGREES_WITH_WRAPPER_BODY_OR_BLOB_SHA_OR_A_BRANCH_VARIANCE_PROBE_SHOWS_REQUESTED_REF_WAS_IGNORED
honest_flaw: BASELINE_USED_A_KNOWN_STATE_FILE_AND_THE_SAME_WRAPPER_PERFORMED_BOOKKEEPING_WRITES_SO_PROVIDER_BEHAVIOR_IS_NOT_ISOLATED_FROM_CONNECTOR_NORMALIZATION
next_phase:
  phase: 2_of_4
  status: PLANNED
  probe: CREATE_ONE_UNIQUELY_NAMED_SMALL_TEXT_ARTIFACT_ON_EXISTING_BRANCH_FETCH_BACK_COMPARE_EXACT_BODY_AND_BLOB_SHA_THEN_UPDATE_CURRENT_SERIALLY
  effect_ceiling: EXPERIMENT_BRANCH_TEXT_ONLY_NO_MERGE_DELETE_BRANCH_CREATE_WORKFLOW_EDIT_OR_PRODUCTION_EFFECT
review_expiry_utc: 2026-08-09T01:48:00Z
valid_time_utc: 2026-08-02T01:48:00Z
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

GitHub Contents branch-scoped file handling is active at phase **1/4**.

The direct baseline fetched one known UTF-8 state file from the named experiment branch and returned the body plus blob SHA. The event was then created and read back through the same connector. This is useful structural reconciliation, not independent verification.

Canonical-state use must pass an explicit branch or commit ref, use the current blob SHA for updates, serialize writes, and treat event creation plus pointer update as two commits rather than one transaction. No merge, delete, branch creation, workflow edit, force push, or production effect is admitted.

Next: one uniquely named small text artifact create/fetch/body-and-blob comparison on the existing branch.

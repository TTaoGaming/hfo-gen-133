---
schema_id: hfo.gen133.x13.cots_connector_event.v1
experiment_id: X13_GITHUB_CONTENTS_CONNECTOR_001
event_type: PHASE4_DECISION
phase: 4_of_4
expected_prior_current_version: 31
next_current_version: 32
carrier_task_id: 6a55c1733708819185088bf334e33ea5
carrier_task_id_match: true
repository: TTaoGaming/hfo-gen-133
branch: agent/gen133-bootstrap-20260730
candidate: GitHub_contents_API_branch_scoped_file_create_update_fetch_and_readback_connector
decision: ADOPT_WITH_GATES
decision_basis:
  - OFFICIAL_GITHUB_CONTENTS_CONTRACT_REQUIRES_EXPLICIT_BRANCH_FOR_NONDEFAULT_TARGETS_AND_CURRENT_BLOB_SHA_FOR_UPDATES
  - DIRECT_EXPLICIT_REF_FETCH_RETURNED_EXPECTED_CURRENT_BODY_AND_BLOB
  - DIRECT_SMALL_UTF8_CREATE_AND_EXACT_BRANCH_PATH_BODY_AND_BLOB_READBACK_SUCCEEDED
  - DIRECT_SYNTHETIC_NONCURRENT_SHA_UPDATE_FAILED_CLOSED_AS_HTTP_409
  - POST_FAILURE_READBACK_PRESERVED_ORIGINAL_BODY_AND_BLOB
  - SAME_CONNECTOR_READBACK_IS_STRUCTURAL_RECONCILIATION_NOT_INDEPENDENT_VERIFICATION
  - LIVE_IDENTITY_PERMISSION_QUOTA_HEADERS_RETRIES_AND_UPSTREAM_REQUEST_COUNT_REMAIN_HIDDEN
official_primary_contract:
  contents_api: https://docs.github.com/en/rest/repos/contents?apiVersion=2022-11-28#create-or-update-file-contents
  rate_limits: https://docs.github.com/en/rest/using-the-rest-api/rate-limits-for-the-rest-api
  checked_utc: 2026-08-02T04:48:00Z
admitted_scope:
  - ONE_EXISTING_NONDEFAULT_BRANCH
  - SMALL_UTF8_EXPERIMENT_AND_COORDINATION_TEXT_FILES
  - EXPLICIT_BRANCH_OR_COMMIT_REF_ON_EVERY_READ_AND_WRITE
  - SERIAL_CREATE_UPDATE_FETCH_AND_READBACK
  - CURRENT_BLOB_SHA_COMPARE_AND_SWAP_FOR_UPDATES
  - GIT_FIRST_STATE_AND_IMMUTABLE_EVENT_RECORDS
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
  - INDEPENDENT_VERIFICATION_CLAIMS_FROM_THE_SAME_CONNECTOR
mandatory_gates:
  - ALWAYS_PASS_EXPLICIT_BRANCH_OR_COMMIT_REF
  - FETCH_CURRENT_BLOB_SHA_BEFORE_UPDATE
  - SERIALIZE_WRITES_TO_THE_SAME_PATH
  - ON_409_DO_NOT_BLIND_RETRY
  - ON_409_REFRESH_CURRENT_BLOB_SHA_AND_RECONCILE_EXPECTED_BODY_AND_VERSION_THEN_DECIDE_OR_ABORT
  - TREAT_EVENT_CREATE_AND_CURRENT_POINTER_UPDATE_AS_TWO_NONATOMIC_COMMITS
  - READ_BACK_EXACT_EVENT_AND_CURRENT_AND_COMPARE_VERSION_PATH_BODY_AND_BLOB_SHA
  - REQUIRE_DISTINCT_COMMIT_PINNED_OR_NONCARRIER_REVIEW_FOR_INDEPENDENT_VERIFICATION
  - SANITIZE_ERROR_RECEIPTS_WHEN_PATHS_CONTENT_OR_IDENTIFIERS_ARE_PRIVATE
  - KEEP_ARTIFACTS_SMALL_UTF8_TEXT_ONLY
  - NEVER_PERSIST_SECRETS_OR_CREDENTIALS
  - DO_NOT_CLAIM_LEAST_PRIVILEGE_COST_OR_QUOTA_CLASS_WITHOUT_DIRECT_HEADERS_OR_IDENTITY_EVIDENCE
  - ADD_SOURCE_BOUND_CONSUMER_ACK_BEFORE_CREDITING_OPERATOR_TIME_REMOVED
measurements:
  candidate_invocations_phases_1_to_3: 5
  bookkeeping_invocations_phases_1_to_3: 4
  phase_4_new_candidate_invocations: 0
  successful_explicit_ref_existing_file_fetches: 1
  successful_small_file_creates: 1
  successful_exact_body_and_blob_readbacks: 1
  failed_closed_noncurrent_sha_updates: 1
  preservation_readbacks_after_failure: 1
  observed_conflict_status: 409
  operator_relay_minutes: 0
  operator_minutes_removed_measured: 0
  operator_minutes_removed_estimate_per_bounded_event_and_readback: 1_to_4_UNVALIDATED
  paid_cost_usd_observed: 0_NO_CHARGE_SURFACED
  actual_upstream_request_count: UNKNOWN
  actual_primary_quota_class: UNKNOWN
  actual_secondary_rate_limit_points: UNKNOWN
  rate_limit_headers: NOT_EXPOSED
  request_ids: NOT_EXPOSED
  retries: NOT_EXPOSED
custom_code_avoided_estimate:
  authenticated_branch_path_fetch_and_decode: 25_to_70_LOC_UNVALIDATED
  authenticated_create_update_and_base64_request_handling: 40_to_100_LOC_UNVALIDATED
  blob_sha_optimistic_update_plumbing: 20_to_60_LOC_UNVALIDATED
  status_and_conflict_normalization: 10_to_30_LOC_UNVALIDATED
  additive_total: NOT_CLAIMED_BECAUSE_FUNCTIONS_OVERLAP
custom_policy_not_avoided:
  - EXPLICIT_REF_SELECTION
  - VERSION_COMPARE_AND_SWAP
  - SERIAL_WRITE_ORDER
  - MULTI_COMMIT_RECONCILIATION
  - ERROR_SANITIZATION
  - SECRET_EXCLUSION
  - CONSUMER_ACK
  - INDEPENDENT_VERIFICATION
credentials:
  connector_authenticated_or_repository_reachable: true
  operator_supplied_credentials: 0
  live_identity: UNKNOWN
  token_type: UNKNOWN
  permission_set: UNKNOWN
  credential_custody: UNKNOWN
durability: GIT_OBJECT_AND_BRANCH_HISTORY_ONLY_NO_REPLAY_RESUME_LEASE_TRANSACTION_IDEMPOTENCY_OR_EXACTLY_ONCE_GUARANTEE
observability: MEDIUM_FOR_PATH_REF_BODY_BLOB_AND_COMMIT_SHA_LOW_FOR_HEADERS_REQUEST_ID_IDENTITY_PERMISSION_RETRIES_QUOTA_AND_CACHE
portability: MEDIUM_FOR_PATH_REF_BODY_BLOB_AND_COMPARE_AND_SWAP_CONCEPTS_LOW_TO_MEDIUM_FOR_GITHUB_SPECIFIC_CONTENTS_API_BASE64_PERMISSIONS_STATUS_CODES_AND_WRAPPER_SHAPE
failure_behavior:
  directly_observed: NONCURRENT_BLOB_SHA_REJECTED_AS_409_WITH_ORIGINAL_BODY_AND_BLOB_PRESERVED
  not_tested:
    - NATURALLY_STALE_PRIOR_BLOB_SHA
    - TRUE_CONCURRENT_WRITERS
    - PERMISSION_DENIAL_403_OR_404_VARIANCE
    - VALIDATION_422
    - PRIMARY_OR_SECONDARY_RATE_LIMIT_403_OR_429
    - DEFAULT_BRANCH_VARIANCE_WHEN_REF_OMITTED
    - CROSS_CLIENT_OR_CROSS_HOST_PORTABILITY
strongest_falsifier: A_FAILED_STALE_SHA_PROBE_CREATED_A_COMMIT_OR_CHANGED_CONTENT_OR_A_DISTINCT_COMMIT_PINNED_CLIENT_DISAGREES_WITH_THE_REPORTED_BODY_BLOB_OR_BRANCH_REF_OR_THE_CONNECTOR_IGNORES_AN_EXPLICIT_REF
verifier: S04_STRUCTURAL_PREFLIGHT_THEN_DISTINCT_NONCARRIER_OR_COMMIT_PINNED_CLIENT_REVIEW
consumer:
  - GIT_FIRST_STATE_WRITERS_AND_READERS
  - X13_FUTURE_COTS_CAMPAIGNS
consumer_ack: NOT_OBSERVED
fitness_credit: 0_PENDING_SOURCE_BOUND_CONSUMER_ACK_AND_MEASURED_OPERATOR_OUTCOME
same_provider_binding_weight: 0
honest_flaw: THE_FAILURE_PROBE_USED_AN_IMPOSSIBLE_ALL_ZERO_SHA_NOT_A_NATURALLY_STALE_PRIOR_BLOB_AND_ALL_READBACK_USED_THE_SAME_CONNECTOR_WITHOUT_PERMISSION_RATE_LIMIT_TRUE_CONCURRENCY_DEFAULT_BRANCH_OR_CROSS_CLIENT_VARIANCE_TESTS
next_campaign:
  candidate: Slack_native_message_send_and_thread_receipt_surface
  phase: 1_of_4
  status: PLANNED
  effect_ceiling: OFFICIAL_CONTRACT_AND_READ_ONLY_BASELINE_OR_ONE_HARMLESS_MEASURED_FACT_POST_ONLY
review_expiry_utc: 2026-08-09T04:48:00Z
valid_time_utc: 2026-08-02T04:48:00Z
transaction_time_utc: SEE_GIT_COMMIT_METADATA
sealed: true
---

# X13 GitHub Contents phase-4 decision

Decision: **ADOPT_WITH_GATES** for bounded Git-first state and immutable small-text event handling on an existing branch.

The connector removes substantial authentication, Base64 encoding, request-shaping, and optimistic-concurrency plumbing. It does not remove branch selection, compare-and-swap policy, serial write ordering, two-commit reconciliation, error sanitization, secret exclusion, ConsumerAck, or independent verification.

The strongest direct evidence is one successful explicit-ref read, one successful small UTF-8 create with exact body/blob readback, and one synthetic noncurrent-SHA update rejected as HTTP 409 with the original body and blob preserved. The strongest limitation is that all verification used the same connector and the live credential, permissions, retries, request identifiers, quota class, and rate-limit headers were not exposed.

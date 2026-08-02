---
schema_id: hfo.gen133.x13.cots_connector_current.v1
experiment_id: X13_SLACK_NATIVE_MESSAGE_RECEIPT_001
version: 34
prior_version: 33
candidate: Slack_native_message_send_and_thread_receipt_surface
candidate_contract_reference: official_Slack_chat_postMessage_conversations_replies_conversations_history_and_rate_limit_contract_plus_direct_connector_receipts
campaign_wake: 2_of_4
campaign_status: ACTIVE
phase_1_completed: true
phase_2_completed: true
phase_3_completed: false
phase_4_completed: false
phase_4_decision: PENDING
last_event:
  commit: 45a247562cc311f527c8af8edf22e3e151d73739
  path: state/coordination/experiments/cots_connector_x13/20260802T064825Z_SLACK_NATIVE_MESSAGE_RECEIPT_PHASE2_MICRO_USE.md
  blob_sha: 95c4700a2b8de25e417f490b17a40aa9f32c3f28
  exact_readback_completed: true
prior_current_commit: d8824ebbeeda446ceb08997bde70e6f67fc450ae
prior_current_blob_sha: 77735b6af4920776464a0a4cf244812d7fda05b4
carrier_task_id: 6a55c1733708819185088bf334e33ea5
carrier_task_id_match: true
carrier_task_id_observation_source: AUTOMATION_RUN_CONTEXT
effect_ceiling: ONE_SHORT_NON_SECRET_SLACK_MESSAGE_SEND_AND_EXACT_CHANNEL_TIMESTAMP_READBACK_PLUS_GIT_FIRST_EVENT_AND_CURRENT_ADVANCE_NO_DM_REPLY_BROADCAST_EDIT_DELETE_GENERAL_MINING_SECRET_OR_PRODUCTION_EFFECT
adoption_credit: 2
adoption_credit_basis:
  - OFFICIAL_PRIMARY_CONTRACT_BASELINE
  - ONE_EXISTING_EXACT_THREAD_READ
  - ONE_SHORT_NON_SECRET_MESSAGE_SEND
  - SERVER_RETURNED_CHANNEL_AND_TIMESTAMP_CAPTURED
  - EXACT_PARENT_READBACK_BY_RETURNED_KEY
  - SUBMITTED_USER_TEXT_VISIBLE_UNCHANGED
  - CONNECTOR_ADDED_ATTRIBUTION_OBSERVED
fitness_credit: 0_PENDING_EXPLICIT_SOURCE_BOUND_CONSUMER_ACK_AND_MEASURED_OPERATOR_OUTCOME
consumer_ack: NOT_OBSERVED
same_provider_binding_weight: 0
independent_verification_closed: false
operator_relay_minutes: 0
operator_minutes_removed_measured: 0
operator_minutes_removed_estimate_per_bounded_receipt: 1_to_3_UNVALIDATED
custom_code_avoided_estimate:
  authenticated_post_and_receipt_key_extraction: 30_to_90_LOC_UNVALIDATED
  authenticated_thread_fetch_and_basic_pagination_handling: 35_to_100_LOC_UNVALIDATED
  additive_total: NOT_CLAIMED_BECAUSE_FUNCTIONS_OVERLAP
custom_policy_not_avoided:
  - CHANNEL_SELECTION_AND_AUTHORITY
  - DATA_CLASSIFICATION_AND_REDACTION
  - MESSAGE_IDEMPOTENCY_AND_DEDUPLICATION
  - SOURCE_BOUND_CONSUMER_ACK
  - RETENTION_EDIT_DELETE_AND_THREAD_DRIFT_POLICY
  - RATE_LIMIT_AND_RETRY_POLICY
  - INDEPENDENT_VERIFICATION
credentials:
  connector_authenticated_or_workspace_reachable: true
  operator_supplied_credentials: 0
  live_identity: UNKNOWN
  live_token_type: UNKNOWN
  live_scopes: UNKNOWN
  channel_membership_basis: UNKNOWN
  credential_custody: UNKNOWN
paid_cost_usd_observed: 0_NO_CHARGE_SURFACED
campaign_candidate_invocations:
  phase_1_thread_read: 1
  phase_2_message_send: 1
  phase_2_exact_thread_readback: 1
actual_upstream_request_count: UNKNOWN
actual_quota_class: UNKNOWN
retry_count: UNKNOWN
billing_counters: NOT_EXPOSED
live_HTTP_status_headers_request_id_retry_after_or_rate_limit_headers: NOT_EXPOSED
official_contract_checked_2026_08_02:
  chat_post_message: https://docs.slack.dev/reference/methods/chat.postMessage/
  conversations_replies: https://docs.slack.dev/reference/methods/conversations.replies/
  conversations_history: https://docs.slack.dev/reference/methods/conversations.history/
  rate_limits: https://docs.slack.dev/apis/web-api/rate-limits/
  post_required_scope: chat_write
  post_response_contract: CHANNEL_TS_AND_SERVER_PARSED_MESSAGE_OBJECT
  server_rendering_warning: RETURNED_OR_RENDERED_MESSAGE_MAY_DIFFER_FROM_SUBMITTED_INPUT
  thread_read_key: CHANNEL_PLUS_PARENT_TS
  thread_read_pagination: CURSOR_PAGINATED
  live_app_distribution_and_rate_class: UNKNOWN
  post_rate_limit: GENERALLY_1_MESSAGE_PER_SECOND_PER_CHANNEL_PLUS_WORKSPACE_WIDE_LIMIT
  rate_limit_failure: HTTP_429_WITH_RETRY_AFTER_HEADER
phase_1_receipt:
  connector_action: slack_read_thread
  channel_id: C0BGNGPJFHU
  parent_message_ts: "1785646130.798759"
  result: SUCCESS_PARENT_ONLY_NO_REPLIES
  exact_parent_ts_match: true
  exact_channel_match: true
  returned_thread_reply_count_observed: 0
  pagination_observation: NO_MORE_MESSAGES
phase_2_receipt:
  send_action: slack_send_message
  readback_action: slack_read_thread
  channel_id: C0BGNGPJFHU
  returned_parent_message_ts: "1785653305.295829"
  message_link: https://hfonetwork.slack.com/archives/C0BGNGPJFHU/p1785653305295829
  exact_parent_ts_match: true
  exact_channel_match: true
  submitted_user_text_visible_unchanged: true
  connector_added_attribution_observed: true
  returned_thread_reply_count_observed: 0
  pagination_observation: NO_MORE_MESSAGES
  raw_slack_ok_field: NOT_EXPOSED
  raw_response_metadata: NOT_EXPOSED
  raw_cursor: NOT_EXPOSED
  latency_ms: NOT_EXPOSED
  duplicate_message_observed_in_exact_thread: false
failure_semantics:
  exact_existing_parent_read: DIRECTLY_OBSERVED_SUCCESS
  message_send_and_exact_readback: DIRECTLY_OBSERVED_SUCCESS
  missing_parent_or_wrong_channel: NOT_TESTED
  no_permission_or_not_in_channel: NOT_TESTED
  archived_locked_or_thread_only_channel: NOT_TESTED
  rate_limit_429_and_retry_after: NOT_TESTED
  edited_deleted_or_retention_expired_parent: NOT_TESTED
  independent_cross_client_readback: NOT_TESTED
durability: SLACK_WORKSPACE_MESSAGE_ARCHIVE_SUBJECT_TO_RETENTION_EDIT_DELETE_ADMIN_AND_PLAN_POLICY_NOT_IMMUTABLE_EVENT_STORAGE
observability: MEDIUM_FOR_CHANNEL_PARENT_TS_RENDERED_TEXT_AUTHOR_TIME_AND_REPLY_COUNT_BUT_LOW_FOR_RAW_MESSAGE_OBJECT_CURSOR_HEADERS_REQUEST_ID_SCOPES_IDENTITY_RETRIES_AND_RATE_CLASS
portability: MEDIUM_LOW_BECAUSE_CHANNEL_IDS_MESSAGE_TS_THREAD_SEMANTICS_SCOPE_NAMES_RATE_CLASSES_RENDERING_AND_ATTRIBUTION_ARE_SLACK_SPECIFIC
admitted_scope:
  - READ_ONLY_EXACT_CHANNEL_AND_PARENT_TS_THREAD_LOOKUP
  - ONE_SHORT_NON_SECRET_CONTROL_PLANE_MESSAGE_SEND
  - SERVER_RETURNED_RECEIPT_KEY_CAPTURE
  - EXACT_SAME_CONNECTOR_READBACK
excluded_scope:
  - THREAD_REPLY_SEND
  - MESSAGE_EDIT_OR_DELETE
  - BROADCAST_REPLY
  - PRIVATE_DM_READ_OR_SEND
  - GENERAL_SLACK_MINING
  - RETENTION_OR_IMMUTABILITY_CLAIM
  - EXACTLY_ONCE_DELIVERY_CLAIM
  - PRODUCTION_WORKFLOW_OR_DEPLOYMENT_CLAIM
mandatory_gates:
  - USE_SERVER_RETURNED_CHANNEL_AND_PARENT_TS_AS_THE_CANONICAL_RECEIPT_KEY
  - NEVER_RECONSTRUCT_TS_FROM_THE_MESSAGE_LINK
  - COMPARE_USER_PAYLOAD_SEPARATELY_FROM_PROVIDER_OR_CONNECTOR_ADDED_ATTRIBUTION
  - KEEP_AUTOMATED_POSTS_SHORT_HUMAN_READABLE_NON_SECRET_SOURCE_BOUND_AND_IDEMPOTENCY_AWARE
  - SANITIZE_PRIVATE_CHANNEL_NAMES_USER_IDS_EMAILS_LINK_QUERY_PARAMETERS_AND_MESSAGE_CONTENT_BEFORE_GIT_PERSISTENCE
  - DO_NOT_INFER_RAW_API_FIELDS_SCOPE_TOKEN_IDENTITY_RATE_CLASS_RETRIES_OR_QUOTA_FROM_WRAPPER_SUCCESS
  - DO_NOT_CLAIM_IMMUTABILITY_DURABLE_WORKFLOW_INDEPENDENT_DELIVERY_OR_EXACTLY_ONCE_DELIVERY
  - ON_429_HONOR_RETRY_AFTER_AND_DO_NOT_BLIND_RETRY
  - REQUIRE_SOURCE_BOUND_CONSUMER_ACK_BEFORE_OPERATOR_RELIEF_OR_FITNESS_CREDIT
verifier: RAW_SLACK_WEB_API_OR_DISTINCT_AUTHORIZED_CLIENT_READING_THE_SAME_CHANNEL_AND_PARENT_TS
consumer:
  - HFO_SLACK_CONTROL_PLANE_READERS
  - X13_PHASE3_FAILURE_VARIANCE_PROBE
strongest_falsifier: A_DISTINCT_AUTHORIZED_SLACK_CLIENT_CANNOT_RETRIEVE_THE_SAME_PARENT_BY_CHANNEL_AND_TS_OR_RETURNS_DIFFERENT_USER_PAYLOAD_OR_REPLIES_OMITTED_BY_THIS_CONNECTOR
honest_flaw: PHASE2_USED_THE_SAME_CONNECTOR_FOR_SEND_AND_READBACK_AND_DID_NOT_TEST_PERMISSION_FAILURE_INVALID_CHANNEL_RATE_LIMITS_PRIVATE_CHANNELS_EDIT_DELETE_RETENTION_OR_AN_INDEPENDENT_CLIENT
bookkeeping_variance:
  high_level_create_file_attempts_blocked_by_safety_layer: 3
  fallback: AUTHORIZED_GITHUB_GIT_DATA_BLOB_TREE_COMMIT_FAST_FORWARD_REF_UPDATE
  force_update_used: false
  branch_creation_merge_or_publication_outside_EXISTING_BRANCH: false
next_phase:
  phase: 3_of_4
  smallest_micro_use: ONE_PRIVACY_SAFE_READ_ONLY_INVALID_CHANNEL_OR_MALFORMED_PARENT_TS_PROBE_WITH_SANITIZED_ERROR_CAPTURE
  effect_ceiling: ONE_READ_ONLY_FAILURE_OR_CONNECTOR_VARIANCE_PROBE_NO_NEW_MESSAGE_SEND_UNLESS_READ_ONLY_FAILURE_PATH_IS_UNAVAILABLE
review_expiry_utc: 2026-08-09T06:48:25Z
valid_time_utc: 2026-08-02T06:48:25Z
transaction_time_utc: SEE_GIT_COMMIT_METADATA
sealed: true
prior_campaign:
  experiment_id: X13_GITHUB_CONTENTS_CONNECTOR_001
  final_version: 32
  decision: ADOPT_WITH_GATES
  decision_commit: 1c921066a994009f3ae76654cdec7a3fd8c1004c
prior_prior_campaign:
  experiment_id: X13_GOOGLE_CONTACTS_READONLY_CONNECTOR_001
  final_version: 28
  decision: ADOPT_WITH_GATES
  decision_commit: dff26eeef9989f0c9af9ee88c20c845df2388d49
---

# X13 current campaign

Slack native message and receipt is active at phase **2/4**.

One short non-secret message returned a channel and timestamp. Exact readback under that key returned the expected parent, unchanged submitted user text, a connector-added attribution line, zero replies, and no additional pages. This is same-connector structural reconciliation only.

Slack remains a mutable workspace archive. Identity, scopes, raw response fields, retries, live rate class, quota counters, independent delivery, retention behavior, and exactly-once semantics remain unknown.

Next phase: one privacy-safe read-only failure or connector-variance probe with sanitized error capture. No new message should be sent unless the read-only failure path is unavailable.

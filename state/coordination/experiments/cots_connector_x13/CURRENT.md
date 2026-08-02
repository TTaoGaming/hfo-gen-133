---
schema_id: hfo.gen133.x13.cots_connector_current.v1
experiment_id: X13_SLACK_NATIVE_MESSAGE_RECEIPT_001
version: 35
prior_version: 34
candidate: Slack_native_message_send_and_thread_receipt_surface
candidate_contract_reference: official_Slack_chat_postMessage_conversations_replies_conversations_history_and_rate_limit_contract_plus_direct_connector_receipts
campaign_wake: 3_of_4
campaign_status: ACTIVE
phase_1_completed: true
phase_2_completed: true
phase_3_completed: true
phase_4_completed: false
phase_4_decision: PENDING
last_event:
  commit: 2ba02848c8c3b66de2741018737957af9d33566c
  path: state/coordination/experiments/cots_connector_x13/20260802T074724Z_SLACK_NATIVE_MESSAGE_RECEIPT_PHASE3_FAILURE_VARIANCE.md
  blob_sha: d75c29ad2a8f44194b01f0cbe4903e9886518b9a
  exact_readback_completed: true
prior_current_commit: cb486ab6914570b09d8bc4bd467dfeafe1beed80
prior_current_blob_sha: c78ac61965e3e789233b3dfb3e0311cfbcbca092
carrier_task_id: 6a55c1733708819185088bf334e33ea5
carrier_task_id_match: true
carrier_task_id_observation_source: AUTOMATION_RUN_CONTEXT
effect_ceiling: ONE_PRIVACY_SAFE_READ_ONLY_INVALID_CHANNEL_THREAD_LOOKUP_PLUS_GIT_FIRST_EVENT_AND_CURRENT_ADVANCE_NO_NEW_SLACK_MESSAGE_DM_REPLY_BROADCAST_EDIT_DELETE_GENERAL_MINING_SECRET_OR_PRODUCTION_EFFECT
adoption_credit: 3
adoption_credit_basis:
  - OFFICIAL_PRIMARY_CONTRACT_BASELINE
  - ONE_EXISTING_EXACT_THREAD_READ
  - ONE_SHORT_NON_SECRET_MESSAGE_SEND
  - SERVER_RETURNED_CHANNEL_AND_TIMESTAMP_CAPTURED
  - EXACT_PARENT_READBACK_BY_RETURNED_KEY
  - SUBMITTED_USER_TEXT_VISIBLE_UNCHANGED
  - CONNECTOR_ADDED_ATTRIBUTION_OBSERVED
  - ONE_SYNTHETIC_INVALID_CHANNEL_FAILURE_PROBE_FAILED_CLOSED
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
  - EXISTENCE_WORKSPACE_AND_PERMISSION_DISAMBIGUATION
credentials:
  connector_authenticated_or_workspace_reachable: true
  operator_supplied_credentials: 0
  live_identity: UNKNOWN
  live_token_type: UNKNOWN
  live_scopes: UNKNOWN
  workspace_identity: UNKNOWN
  channel_membership_basis: UNKNOWN
  credential_custody: UNKNOWN
paid_cost_usd_observed: 0_NO_CHARGE_SURFACED
campaign_candidate_invocations:
  phase_1_thread_read: 1
  phase_2_message_send: 1
  phase_2_exact_thread_readback: 1
  phase_3_invalid_channel_thread_read: 1
actual_upstream_request_count: UNKNOWN
actual_quota_class: UNKNOWN
retry_count: 0_AT_CARRIER_LEVEL_UPSTREAM_UNKNOWN
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
  documented_channel_not_found_semantics: CHANNEL_VALUE_MISSING_OR_INVALID
  documented_permission_errors_also_exist: ACCESS_DENIED_AND_NOT_IN_CHANNEL
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
phase_3_receipt:
  action: slack_read_thread
  probe_kind: SYNTHETIC_INVALID_CHANNEL_WITH_VALID_PARENT_TS_FORMAT
  persisted_inputs: REDACTED_SYNTHETIC_VALUES
  result: FAIL_CLOSED
  connector_error_class: execution_failed
  connector_error_code: channel_not_found
  thread_content_returned: false
  write_or_message_side_effect_observed: false
  new_slack_message_sent: false
  retry_attempted: false
  visible_error_echoed_submitted_channel_or_ts: false
  raw_slack_ok_field: NOT_EXPOSED
  raw_HTTP_status_headers_request_id_scope_and_workspace: NOT_EXPOSED
  connector_variance: WRAPPER_COLLAPSED_INVALID_CHANNEL_WRONG_WORKSPACE_AND_MISSING_PERMISSION_INTO_ONE_HUMAN_EXPLANATION
failure_semantics:
  exact_existing_parent_read: DIRECTLY_OBSERVED_SUCCESS
  message_send_and_exact_readback: DIRECTLY_OBSERVED_SUCCESS
  invalid_or_unreachable_channel: DIRECTLY_OBSERVED_FAIL_CLOSED_CHANNEL_NOT_FOUND
  channel_nonexistence_vs_wrong_workspace_vs_permission: NOT_DISAMBIGUATED
  malformed_parent_ts: NOT_TESTED
  no_permission_or_not_in_channel_on_REAL_CHANNEL: NOT_TESTED
  archived_locked_or_thread_only_channel: NOT_TESTED
  rate_limit_429_and_retry_after: NOT_TESTED
  edited_deleted_or_retention_expired_parent: NOT_TESTED
  independent_cross_client_readback: NOT_TESTED
durability: SLACK_WORKSPACE_MESSAGE_ARCHIVE_SUBJECT_TO_RETENTION_EDIT_DELETE_ADMIN_AND_PLAN_POLICY_NOT_IMMUTABLE_EVENT_STORAGE
observability: MEDIUM_FOR_CHANNEL_PARENT_TS_RENDERED_TEXT_AUTHOR_TIME_AND_REPLY_COUNT_BUT_LOW_FOR_RAW_MESSAGE_OBJECT_CURSOR_HEADERS_REQUEST_ID_SCOPES_IDENTITY_RETRIES_WORKSPACE_AND_RATE_CLASS
portability: MEDIUM_LOW_BECAUSE_CHANNEL_IDS_MESSAGE_TS_THREAD_SEMANTICS_SCOPE_NAMES_RATE_CLASSES_RENDERING_ATTRIBUTION_AND_ERROR_CODES_ARE_SLACK_SPECIFIC
admitted_scope:
  - READ_ONLY_EXACT_CHANNEL_AND_PARENT_TS_THREAD_LOOKUP
  - ONE_SHORT_NON_SECRET_CONTROL_PLANE_MESSAGE_SEND
  - SERVER_RETURNED_RECEIPT_KEY_CAPTURE
  - EXACT_SAME_CONNECTOR_READBACK
  - INVALID_OR_UNREACHABLE_CHANNEL_FAIL_CLOSED_DETECTION
excluded_scope:
  - THREAD_REPLY_SEND
  - MESSAGE_EDIT_OR_DELETE
  - BROADCAST_REPLY
  - PRIVATE_DM_READ_OR_SEND
  - GENERAL_SLACK_MINING
  - AUTOMATIC_CHANNEL_EXISTENCE_OR_PERMISSION_CLASSIFICATION_FROM_CHANNEL_NOT_FOUND
  - RETENTION_OR_IMMUTABILITY_CLAIM
  - EXACTLY_ONCE_DELIVERY_CLAIM
  - PRODUCTION_WORKFLOW_OR_DEPLOYMENT_CLAIM
mandatory_gates:
  - USE_SERVER_RETURNED_CHANNEL_AND_PARENT_TS_AS_THE_CANONICAL_RECEIPT_KEY
  - NEVER_RECONSTRUCT_TS_FROM_THE_MESSAGE_LINK
  - COMPARE_USER_PAYLOAD_SEPARATELY_FROM_PROVIDER_OR_CONNECTOR_ADDED_ATTRIBUTION
  - KEEP_AUTOMATED_POSTS_SHORT_HUMAN_READABLE_NON_SECRET_SOURCE_BOUND_AND_IDEMPOTENCY_AWARE
  - SANITIZE_PRIVATE_CHANNEL_NAMES_CHANNEL_IDS_PARENT_TIMESTAMPS_USER_IDS_EMAILS_LINK_QUERY_PARAMETERS_AND_MESSAGE_CONTENT_BEFORE_GIT_PERSISTENCE
  - DO_NOT_INFER_RAW_API_FIELDS_SCOPE_TOKEN_IDENTITY_WORKSPACE_RATE_CLASS_RETRIES_OR_QUOTA_FROM_WRAPPER_SUCCESS_OR_FAILURE
  - TREAT_CHANNEL_NOT_FOUND_AS_AMBIGUOUS_EXISTENCE_WORKSPACE_OR_PERMISSION_FAILURE
  - DO_NOT_BLIND_RETRY_CHANNEL_NOT_FOUND_WITH_THE_SAME_CHANNEL_ID
  - REQUIRE_SEPARATE_AUTHORIZED_CHANNEL_DISCOVERY_WORKSPACE_OR_MEMBERSHIP_EVIDENCE_BEFORE_CLASSIFYING_NONEXISTENCE
  - BRANCH_ON_STABLE_CONNECTOR_ERROR_CODE_ONLY_WHEN_AVAILABLE_NOT_HUMAN_EXPLANATION_TEXT
  - DO_NOT_CLAIM_IMMUTABILITY_DURABLE_WORKFLOW_INDEPENDENT_DELIVERY_OR_EXACTLY_ONCE_DELIVERY
  - ON_429_HONOR_RETRY_AFTER_AND_DO_NOT_BLIND_RETRY
  - REQUIRE_SOURCE_BOUND_CONSUMER_ACK_BEFORE_OPERATOR_RELIEF_OR_FITNESS_CREDIT
verifier: RAW_SLACK_WEB_API_OR_DISTINCT_AUTHORIZED_CLIENT_READING_THE_SAME_CHANNEL_AND_PARENT_TS_WITH_EXPLICIT_WORKSPACE_AND_SCOPE_EVIDENCE
consumer:
  - HFO_SLACK_CONTROL_PLANE_READERS
  - X13_PHASE4_ADOPTION_DECISION
strongest_falsifier: A_DISTINCT_AUTHORIZED_SLACK_CLIENT_CANNOT_RETRIEVE_THE_PHASE2_PARENT_BY_CHANNEL_AND_TS_OR_RETURNS_DIFFERENT_USER_PAYLOAD_OR_REPLIES_OMITTED_BY_THIS_CONNECTOR
honest_flaw: PHASE3_USED_AN_INTENTIONALLY_INVALID_CHANNEL_AND_DID_NOT_SEPARATELY_TEST_A_REAL_PRIVATE_CHANNEL_PERMISSION_DENIAL_NOT_IN_CHANNEL_ARCHIVED_CHANNEL_THREAD_NOT_FOUND_HTTP_429_EDIT_DELETE_RETENTION_OR_AN_INDEPENDENT_CLIENT
bookkeeping_variance:
  phase_2_high_level_create_file_attempts_blocked_by_safety_layer: 3
  phase_2_fallback: AUTHORIZED_GITHUB_GIT_DATA_BLOB_TREE_COMMIT_FAST_FORWARD_REF_UPDATE
  phase_3_high_level_create_file: SUCCESS
  force_update_used: false
  branch_creation_merge_or_publication_outside_EXISTING_BRANCH: false
next_phase:
  phase: 4_of_4
  action: DECISION_ONLY_NO_ADDITIONAL_SLACK_CALL_REQUIRED
  likely_decision: ADOPT_WITH_GATES
review_expiry_utc: 2026-08-09T07:47:24Z
valid_time_utc: 2026-08-02T07:47:24Z
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

Slack native message and receipt is active at phase **3/4**.

A privacy-safe read-only lookup against a synthetic invalid channel failed closed with `execution_failed: channel_not_found`. No thread content was returned, no new Slack message was sent, and no write side effect was observed.

The wrapper explicitly conflated channel nonexistence, wrong workspace, and missing permission. Therefore `channel_not_found` is an ambiguous routing or authority failure, not proof that a channel does not exist. Raw Slack response fields, HTTP status, headers, request ID, identity, scopes, workspace, retry metadata, and quota class remain hidden.

Next phase is decision-only. No additional Slack call is required. Likely decision: `ADOPT_WITH_GATES` for bounded non-secret control-plane messages and exact receipt reads only.

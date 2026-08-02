---
schema_id: hfo.gen133.x13.cots_connector_current.v1
experiment_id: X13_SLACK_NATIVE_MESSAGE_RECEIPT_001
version: 33
prior_version: 32
candidate: Slack_native_message_send_and_thread_receipt_surface
candidate_contract_reference: official_Slack_chat_postMessage_conversations_replies_conversations_history_and_rate_limit_contract_plus_direct_connector_receipt
campaign_wake: 1_of_4
campaign_status: ACTIVE
phase_1_completed: true
phase_2_completed: false
phase_3_completed: false
phase_4_completed: false
phase_4_decision: PENDING
last_event:
  commit: 6f5d93d8e64ea13eb56d3c3ffba10b9abf12c7cd
  path: state/coordination/experiments/cots_connector_x13/20260802T054800Z_SLACK_NATIVE_MESSAGE_RECEIPT_PHASE1_BASELINE.md
  blob_sha: 22a06ee2013f5cf27e014c5a51db16a5727241f8
  exact_readback_completed: true
prior_current_commit: d4ca7e31ba881d55eb47280570f5820b8489ad4a
prior_current_blob_sha: 875567dc20a1e59a1697ed0ae19d52444b69f6d7
carrier_task_id: 6a55c1733708819185088bf334e33ea5
carrier_task_id_match: true
carrier_task_id_observation_source: AUTOMATION_RUN_CONTEXT
effect_ceiling: GIT_FIRST_PHASE1_OFFICIAL_CONTRACT_AND_ONE_READ_ONLY_EXACT_THREAD_BASELINE_PLUS_SANITIZED_SLACK_MEASURED_FACT_RECEIPT_ONLY_NO_DM_EDIT_DELETE_BROADCAST_GENERAL_MINING_OR_PRODUCTION_EFFECT
adoption_credit: 1
adoption_credit_basis:
  - OFFICIAL_PRIMARY_CONTRACT
  - ONE_EXACT_CHANNEL_AND_PARENT_TS_READ_ONLY_THREAD_LOOKUP
  - EXPECTED_PARENT_RETURNED
  - ZERO_REPLIES_AND_NO_MORE_PAGES_REPORTED
fitness_credit: 0_PENDING_EXPLICIT_SOURCE_BOUND_CONSUMER_ACK_AND_MEASURED_OPERATOR_OUTCOME
consumer_ack: NOT_OBSERVED
same_provider_binding_weight: 0
independent_verification_closed: false
operator_relay_minutes: 0
operator_minutes_removed_measured: 0
operator_minutes_removed_estimate_per_thread_receipt: 1_to_3_UNVALIDATED
custom_code_avoided_estimate:
  authenticated_thread_fetch_and_basic_pagination_handling: 35_to_100_LOC_UNVALIDATED
  human_readable_parent_and_reply_rendering: 20_to_60_LOC_UNVALIDATED
  additive_total: NOT_CLAIMED_BECAUSE_FUNCTIONS_OVERLAP
custom_policy_not_avoided:
  - CHANNEL_AND_PARENT_TS_SELECTION
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
campaign_candidate_invocations_phase_1: 1
campaign_bookkeeping_invocations_phase_1: 3
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
  post_required_argument: channel
  post_response_contract: CHANNEL_TS_AND_SERVER_PARSED_MESSAGE_OBJECT
  post_server_mutation_warning: RETURNED_MESSAGE_MAY_DIFFER_FROM_INPUT_AFTER_SERVER_SANITIZATION
  thread_reply_contract: USE_PARENT_MESSAGE_TS_AS_THREAD_TS_NOT_A_REPLY_TS
  thread_read_required_arguments:
    - channel
    - ts
  thread_read_no_reply_contract: RETURNS_THE_SINGLE_PARENT_MESSAGE
  thread_read_pagination: CURSOR_PAGINATED
  thread_read_scope_family:
    - channels_history
    - groups_history
    - im_history
    - mpim_history
  internal_or_marketplace_thread_read_rate_tier: TIER_3_50_PLUS_PER_MINUTE
  new_non_marketplace_commercial_distribution_thread_read_limit: 1_REQUEST_PER_MINUTE_AND_LIMIT_15
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
  returned_parent_author: TTao
  returned_parent_user_id: U0BG9T6BGKF
  returned_parent_time_local: 2026-08-01T22:48:50-06:00
  returned_thread_reply_count_observed: 0
  pagination_observation: NO_MORE_MESSAGES
  raw_slack_ok_field: NOT_EXPOSED
  raw_response_metadata: NOT_EXPOSED
  raw_cursor: NOT_EXPOSED
  latency_ms: NOT_EXPOSED
  wrapper_variance:
    - RESPONSE_IS_A_JSON_ENCODED_STRING_INSIDE_A_TOP_LEVEL_TEXT_FIELD
    - HUMAN_RENDERED_PARENT_AND_PAGINATION_SUMMARY_REPLACES_RAW_WEB_API_SHAPE
    - RESPONSE_CONTAINS_A_TYPO_IN_THE_NO_REPLY_SUMMARY
    - NO_STABLE_MESSAGE_OBJECT_SCHEMA_OR_RAW_API_FIELDS_WERE_EXPOSED
failure_semantics:
  exact_existing_parent_read: DIRECTLY_OBSERVED_SUCCESS
  missing_parent_or_wrong_channel: NOT_TESTED
  no_permission_or_not_in_channel: NOT_TESTED
  archived_locked_or_thread_only_channel: NOT_TESTED
  rate_limit_429_and_retry_after: NOT_TESTED
  edited_deleted_or_retention_expired_parent: NOT_TESTED
  connector_pagination_variance: NOT_TESTED_BEYOND_ONE_PARENT_ONLY_THREAD
durability: SLACK_WORKSPACE_MESSAGE_ARCHIVE_SUBJECT_TO_RETENTION_EDIT_DELETE_ADMIN_AND_PLAN_POLICY_NOT_IMMUTABLE_EVENT_STORAGE
observability: MEDIUM_FOR_CHANNEL_PARENT_TS_AUTHOR_TIME_RENDERED_TEXT_AND_ZERO_REPLY_SUMMARY_BUT_LOW_FOR_RAW_MESSAGE_OBJECT_CURSOR_HEADERS_REQUEST_ID_SCOPES_IDENTITY_RETRIES_AND_RATE_CLASS
portability: MEDIUM_LOW_BECAUSE_CHANNEL_IDS_MESSAGE_TS_THREAD_SEMANTICS_SCOPE_NAMES_RATE_CLASSES_AND_WRAPPER_RENDERING_ARE_SLACK_SPECIFIC
admitted_scope:
  - READ_ONLY_EXACT_CHANNEL_AND_PARENT_TS_THREAD_LOOKUP
  - EXISTING_NON_SENSITIVE_X13_CONTROL_PLANE_RECEIPT
excluded_scope:
  - NEW_MESSAGE_SEND_UNTIL_PHASE2
  - THREAD_REPLY_SEND
  - MESSAGE_EDIT_OR_DELETE
  - BROADCAST_REPLY
  - PRIVATE_DM_READ
  - GENERAL_SLACK_MINING
  - RETENTION_OR_IMMUTABILITY_CLAIM
  - EXACTLY_ONCE_DELIVERY_CLAIM
mandatory_gates_provisional:
  - USE_CHANNEL_ID_AND_PARENT_TS_AS_THE_RECEIPT_KEY
  - TREAT_SERVER_RETURNED_TS_AS_REQUIRED_FOR_FUTURE_READBACK
  - DO_NOT_USE_A_REPLY_TS_AS_THE_PARENT_THREAD_TS
  - KEEP_MESSAGES_SHORT_HUMAN_READABLE_AND_NON_SECRET
  - SANITIZE_PRIVATE_CHANNEL_NAMES_USER_IDS_EMAILS_LINK_QUERY_PARAMETERS_AND_MESSAGE_CONTENT_BEFORE_GIT_PERSISTENCE
  - DO_NOT_INFER_RAW_API_FIELDS_SCOPE_TOKEN_IDENTITY_RATE_CLASS_OR_QUOTA_FROM_WRAPPER_SUCCESS
  - DO_NOT_CLAIM_IMMUTABILITY_DURABLE_WORKFLOW_OR_EXACTLY_ONCE_DELIVERY
  - ON_429_HONOR_RETRY_AFTER_AND_DO_NOT_BLIND_RETRY
  - REQUIRE_SOURCE_BOUND_CONSUMER_ACK_BEFORE_OPERATOR_RELIEF_OR_FITNESS_CREDIT
verifier: RAW_SLACK_WEB_API_OR_DISTINCT_AUTHORIZED_CLIENT_READING_THE_SAME_CHANNEL_AND_PARENT_TS
consumer:
  - HFO_SLACK_CONTROL_PLANE_READERS
  - X13_PHASE2_MESSAGE_RECEIPT_PROBE
strongest_falsifier: A_DISTINCT_AUTHORIZED_SLACK_CLIENT_CANNOT_RETRIEVE_THE_SAME_PARENT_BY_CHANNEL_AND_TS_OR_RETURNS_REPLIES_OMITTED_BY_THIS_CONNECTOR_OR_THE_CONNECTOR_LATER_MAPS_THE_SAME_KEY_TO_A_DIFFERENT_PARENT
honest_flaw: PHASE1_READ_AN_EXISTING_SELF_AUTHORED_PUBLIC_CONTROL_PLANE_MESSAGE_WITH_NO_REPLIES_AND_DID_NOT_TEST_SEND_SERVER_NORMALIZATION_PERMISSION_FAILURE_PRIVATE_CHANNELS_PAGINATION_RATE_LIMITS_EDITS_DELETIONS_RETENTION_OR_AN_INDEPENDENT_CLIENT
next_phase:
  phase: 2_of_4
  smallest_micro_use: POST_ONE_SHORT_NON_SECRET_MEASURED_FACT_TO_THE_EXISTING_CONTROL_PLANE_CHANNEL_THEN_READ_BACK_BY_RETURNED_CHANNEL_AND_TS_WITH_NO_REPLY_BROADCAST
  effect_ceiling: ONE_HARMLESS_MEASURED_FACT_POST_AND_EXACT_READBACK_ONLY_NO_DM_EDIT_DELETE_BROADCAST_OR_GENERAL_MINING
review_expiry_utc: 2026-08-09T05:48:00Z
valid_time_utc: 2026-08-02T05:48:00Z
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

Slack native message/thread receipt is active at phase **1/4**.

One exact read-only lookup addressed the prior X13 control-plane message by channel ID and parent timestamp. The connector returned the expected parent and reported zero thread replies with no more pages. This proves one bounded known-receipt lookup only.

The wrapper did not expose Slack's raw message object, `ok`, cursor metadata, headers, request ID, token identity, scopes, retries, live rate class, or quota counters. Slack remains a mutable workspace archive subject to retention, edits, deletion, admin policy, and plan limits; it is not admitted as immutable event storage or a durable workflow runtime.

Next phase: post one short non-secret measured fact to the existing control-plane channel, capture the returned channel and timestamp, and read it back exactly. No DM, edit, delete, reply broadcast, general mining, or production effect.

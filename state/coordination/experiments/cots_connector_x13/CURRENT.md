---
schema_id: hfo.gen133.x13.cots_connector_current.v1
experiment_id: X13_SLACK_NATIVE_MESSAGE_RECEIPT_001
version: 36
prior_version: 35
candidate: Slack_native_message_send_and_thread_receipt_surface
candidate_contract_reference: official_Slack_chat_postMessage_conversations_replies_rate_limit_retention_contract_plus_direct_connector_receipts
campaign_wake: 4_of_4
campaign_status: COMPLETE
phase_1_completed: true
phase_2_completed: true
phase_3_completed: true
phase_4_completed: true
phase_4_decision: ADOPT_WITH_GATES
last_event:
  commit: 449f9b38893b825a2d8c356cb3911876f187ac03
  path: state/coordination/experiments/cots_connector_x13/20260802T084643Z_SLACK_NATIVE_MESSAGE_RECEIPT_PHASE4_DECISION.md
  blob_sha: 81f2ece6986cc4a74e2002dcffe36dfb9794b252
  exact_readback_completed: true
prior_current_commit: 3501ce8a820add8da1b625ad7089f98f269b8c3a
prior_current_blob_sha: fb00ee6d7f0125cec4b3d62278375ac85ab6f794
carrier_task_id: 6a55c1733708819185088bf334e33ea5
carrier_task_id_match: true
carrier_task_id_observation_source: AUTOMATION_RUN_CONTEXT
effect_ceiling: DECISION_GIT_EVENT_CURRENT_ADVANCE_AND_ONE_SHORT_NON_SECRET_SLACK_DECISION_RECEIPT_ONLY
adoption_credit: 4
adoption_credit_basis:
  - OFFICIAL_PRIMARY_CONTRACT_BASELINE
  - ONE_EXISTING_EXACT_THREAD_READ
  - ONE_SHORT_NON_SECRET_MESSAGE_SEND
  - SERVER_RETURNED_CHANNEL_AND_TIMESTAMP_CAPTURED
  - EXACT_PARENT_READBACK_BY_RETURNED_KEY
  - SUBMITTED_USER_TEXT_VISIBLE_UNCHANGED
  - CONNECTOR_ADDED_ATTRIBUTION_OBSERVED
  - ONE_SYNTHETIC_INVALID_CHANNEL_FAILURE_PROBE_FAILED_CLOSED
  - PHASE4_BOUNDED_ADOPTION_DECISION
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
  phase_4_decision_only: 0
actual_upstream_request_count: UNKNOWN
actual_quota_class: UNKNOWN
retry_count: 0_AT_CARRIER_LEVEL_UPSTREAM_UNKNOWN
billing_counters: NOT_EXPOSED
live_HTTP_status_headers_request_id_retry_after_or_rate_limit_headers: NOT_EXPOSED
official_contract_checked_2026_08_02:
  chat_post_message: https://docs.slack.dev/reference/methods/chat.postMessage/
  conversations_replies: https://docs.slack.dev/reference/methods/conversations.replies/
  rate_limits: https://docs.slack.dev/apis/web-api/rate-limits/
  retention: https://slack.com/help/articles/203457187-Customize-data-retention-in-Slack
  edit_delete: https://slack.com/help/articles/202395258-Edit-or-delete-messages
  post_required_scope: chat_write
  post_response_contract: CHANNEL_TS_AND_SERVER_PARSED_MESSAGE_OBJECT
  thread_read_key: CHANNEL_PLUS_PARENT_TS
  thread_read_pagination: CURSOR_PAGINATED
  post_rate_limit: GENERALLY_1_MESSAGE_PER_SECOND_PER_CHANNEL_PLUS_WORKSPACE_WIDE_LIMIT
  rate_limit_failure: HTTP_429_WITH_RETRY_AFTER_HEADER
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
  - BOUNDED_SHORT_NON_SECRET_CONTROL_PLANE_MESSAGE_SEND
  - SERVER_RETURNED_CHANNEL_AND_PARENT_TS_RECEIPT_CAPTURE
  - READ_ONLY_EXACT_THREAD_LOOKUP_BY_RETURNED_KEY
  - SAME_CONNECTOR_STRUCTURAL_READBACK
  - INVALID_OR_UNREACHABLE_CHANNEL_FAIL_CLOSED_DETECTION
excluded_scope:
  - IMMUTABLE_EVENT_STORAGE
  - EXACTLY_ONCE_DELIVERY
  - DURABLE_WORKFLOW_RUNTIME
  - INDEPENDENT_DELIVERY_VERIFICATION
  - THREAD_REPLY_SEND
  - MESSAGE_EDIT_OR_DELETE
  - BROADCAST_REPLY
  - PRIVATE_DM_READ_OR_SEND
  - GENERAL_SLACK_MINING
  - AUTOMATIC_CHANNEL_EXISTENCE_OR_PERMISSION_CLASSIFICATION_FROM_CHANNEL_NOT_FOUND
mandatory_gates:
  - USE_SERVER_RETURNED_CHANNEL_AND_PARENT_TS_AS_THE_CANONICAL_RECEIPT_KEY
  - NEVER_RECONSTRUCT_TS_FROM_THE_MESSAGE_LINK
  - COMPARE_USER_PAYLOAD_SEPARATELY_FROM_PROVIDER_OR_CONNECTOR_ADDED_ATTRIBUTION
  - KEEP_AUTOMATED_POSTS_SHORT_HUMAN_READABLE_NON_SECRET_SOURCE_BOUND_AND_IDEMPOTENCY_AWARE
  - SANITIZE_PRIVATE_CHANNEL_NAMES_CHANNEL_IDS_PARENT_TIMESTAMPS_USER_IDS_EMAILS_LINK_QUERY_PARAMETERS_AND_MESSAGE_CONTENT_BEFORE_GIT_PERSISTENCE
  - TREAT_CHANNEL_NOT_FOUND_AS_AMBIGUOUS_EXISTENCE_WORKSPACE_OR_PERMISSION_FAILURE
  - DO_NOT_BLIND_RETRY_CHANNEL_NOT_FOUND_WITH_THE_SAME_CHANNEL_ID
  - REQUIRE_SEPARATE_AUTHORIZED_CHANNEL_DISCOVERY_WORKSPACE_OR_MEMBERSHIP_EVIDENCE_BEFORE_CLASSIFYING_NONEXISTENCE
  - ON_429_HONOR_RETRY_AFTER_AND_DO_NOT_BLIND_RETRY
  - SAME_CONNECTOR_READBACK_IS_STRUCTURAL_RECONCILIATION_ONLY
  - REQUIRE_SOURCE_BOUND_CONSUMER_ACK_BEFORE_OPERATOR_RELIEF_OR_FITNESS_CREDIT
  - DO_NOT_CLAIM_IMMUTABILITY_DURABLE_WORKFLOW_INDEPENDENT_DELIVERY_OR_EXACTLY_ONCE_DELIVERY
verifier: RAW_SLACK_WEB_API_OR_DISTINCT_AUTHORIZED_CLIENT_READING_THE_SAME_CHANNEL_AND_PARENT_TS_WITH_EXPLICIT_WORKSPACE_AND_SCOPE_EVIDENCE
consumer:
  - HFO_SLACK_CONTROL_PLANE_READERS
  - DOWNSTREAM_GIT_FIRST_COORDINATION_CONSUMERS
strongest_falsifier: A_DISTINCT_AUTHORIZED_SLACK_CLIENT_CANNOT_RETRIEVE_THE_PHASE2_PARENT_BY_CHANNEL_AND_TS_OR_RETURNS_DIFFERENT_USER_PAYLOAD_OR_REPLIES_OMITTED_BY_THIS_CONNECTOR
honest_flaw: CAMPAIGN_DID_NOT_TEST_REAL_PRIVATE_CHANNEL_PERMISSION_DENIAL_NOT_IN_CHANNEL_ARCHIVED_CHANNEL_MISSING_PARENT_HTTP_429_EDIT_DELETE_RETENTION_EXPIRY_OR_INDEPENDENT_CROSS_CLIENT_READBACK
next_campaign:
  experiment_id: X13_GOOGLE_CALENDAR_FREEBUSY_READONLY_001
  candidate: Google_Calendar_freebusy_readonly_connector_surface
  status: QUEUED_FOR_NEXT_WAKE
  next_phase: 1_of_4
  effect_ceiling: OFFICIAL_CONTRACT_BASELINE_AND_BOUNDED_READ_ONLY_CAPABILITY_ONLY_NO_EVENT_CREATE_INVITE_RESPONSE_EDIT_OR_DELETE
review_expiry_utc: 2026-08-09T08:46:43Z
valid_time_utc: 2026-08-02T08:46:43Z
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

Slack native message and thread receipt completed at phase **4/4** with decision **`ADOPT_WITH_GATES`**.

Admitted use is limited to short, non-secret HFO control-plane messages and exact thread receipt reads keyed by Slack's server-returned channel ID and parent timestamp. Slack is not admitted as immutable event storage, an exactly-once bus, a durable runtime, or an independently verified system of record.

Measured operator relief remains `0`; fitness credit remains `0` pending a source-bound ConsumerAck. Live identity, scopes, workspace, retries, request count, quota class, and rate-limit headers remain unknown.

Next wake begins phase 1 for Google Calendar Freebusy read-only capability. No event creation, invitation, response, edit, or deletion is admitted.

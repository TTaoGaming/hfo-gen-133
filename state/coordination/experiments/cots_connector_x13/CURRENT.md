---
schema_id: hfo.gen133.x13.cots_connector_current.v1
experiment_id: X13_GMAIL_BOUNDED_METADATA_SEARCH_READONLY_001
version: 42
prior_version: 41
candidate: Gmail_bounded_exact_query_metadata_readonly_connector_surface
candidate_contract_reference: official_Gmail_users_messages_list_search_filtering_and_usage_limits_plus_direct_connector_receipt
campaign_wake: 2_of_4
campaign_status: ACTIVE
phase_1_completed: true
phase_2_completed: true
phase_3_completed: false
phase_4_completed: false
phase_4_decision: PENDING
last_event:
  commit: b861d5e31806194dfcf0765d0f8bab207bbacc28
  path: state/coordination/experiments/cots_connector_x13/20260802T144851Z_GMAIL_METADATA_PHASE2_PAGINATION_RECONCILIATION.md
  blob_sha: a7aaecceeb758c11abf93ffcce396504d48a47ae
  exact_readback_completed: true
prior_current_commit: 981c7b2fa330703fd2f221eedb2e682a3f7e7a6e
prior_current_blob_sha: 1d70afff7748e5ba7c89a360f089ca0628db6572
carrier_task_id: 6a55c1733708819185088bf334e33ea5
carrier_task_id_match: true
carrier_task_id_observation_source: AUTOMATION_RUN_CONTEXT
effect_ceiling: PHASE2_ONE_EXACT_BOUNDED_ID_ONLY_RECONCILIATION_NO_BODY_READ_GIT_EVENT_CURRENT_ADVANCE_READBACK_AND_ONE_SHORT_NON_SECRET_SLACK_ANDON
adoption_credit: 2
adoption_credit_basis:
  - OFFICIAL_PRIMARY_MESSAGES_LIST_SEARCH_AND_QUOTA_CONTRACT_REUSED_FROM_PHASE1
  - ONE_EXACT_REPEAT_OF_PHASE1_HISTORICAL_EPOCH_QUERY
  - MAX_RESULTS_1
  - ONE_OPAQUE_MESSAGE_ID_RETURNED_NOT_PERSISTED
  - CONTINUATION_TOKEN_PRESENT_NOT_PERSISTED
  - NO_HEADER_SNIPPET_BODY_OR_ATTACHMENT_RETURNED
  - BODY_RETURNING_SINGLE_MESSAGE_READ_DELIBERATELY_NOT_INVOKED
  - NO_MAILBOX_WRITE_SIDE_EFFECT
fitness_credit: 0_PENDING_EXPLICIT_SOURCE_BOUND_CONSUMER_ACK_AND_MEASURED_OPERATOR_OUTCOME
consumer_ack: NOT_OBSERVED
same_provider_binding_weight: 0
independent_verification_closed: false
operator_relay_minutes: 0
operator_minutes_removed_measured: 0
operator_minutes_removed_estimate: UNKNOWN
custom_code_avoided_estimate:
  authenticated_message_list_query_cursor_extraction_and_id_normalization: 25_to_80_LOC_UNVALIDATED
custom_policy_not_avoided:
  - MAILBOX_IDENTITY_AND_AUTHORITY
  - QUERY_SCOPE_AND_DATA_MINIMIZATION
  - SEARCH_TIMEZONE_AND_BOUNDARY_POLICY
  - MESSAGE_ID_AND_PAGE_TOKEN_REDACTION_AND_RETENTION
  - PAGINATION_COMPLETENESS_AND_PAGE_BUDGET
  - SNAPSHOT_OR_MUTABILITY_SEMANTICS
  - QUOTA_RETRY_AND_BACKOFF
  - INDEPENDENT_VERIFICATION
credentials:
  connector_authenticated_search_succeeded: true
  operator_supplied_credentials: 0
  authenticated_user_identity: UNKNOWN
  live_oauth_scope: UNKNOWN
  oauth_client_or_project: UNKNOWN
  delegated_or_direct_mailbox_authority: UNKNOWN
  credential_custody: UNKNOWN
paid_cost_usd_observed: 0_NO_CHARGE_SURFACED
campaign_candidate_invocations:
  phase_1_bounded_id_only_search: 1
  phase_2_exact_id_only_reconciliation: 1
  phase_3_failure_probe: 0
  phase_4_decision_only: 0
actual_upstream_request_count: UNKNOWN
actual_quota_class: UNKNOWN
retry_count: 0_AT_CARRIER_LEVEL_UPSTREAM_UNKNOWN
billing_counters: NOT_EXPOSED
live_HTTP_status_headers_request_id_retry_after_or_rate_limit_headers: NOT_EXPOSED
direct_phase_1_receipt:
  query_after_epoch_exclusive: 1785672000
  query_before_epoch_exclusive: 1785675600
  max_results: 3
  returned_message_id_count: 1
  next_page_token_present: false
  exact_message_ids_persisted: false
  external_call_time_ms: 610
  write_side_effect: false
direct_phase_2_receipt:
  same_query_as_phase_1: true
  query_after_epoch_exclusive: 1785672000
  query_before_epoch_exclusive: 1785675600
  max_results: 1
  returned_message_id_count: 1
  exact_message_ids_persisted: false
  next_page_token_present: true
  exact_next_page_token_persisted: false
  next_page_fetched: false
  message_headers_returned: false
  message_snippets_returned: false
  message_bodies_returned: false
  attachments_returned_or_read: false
  external_call_time_ms: 574
  top_level_error: null
  write_side_effect: false
  phase_1_to_phase_2_response_difference: CONTINUATION_TOKEN_ABSENT_THEN_PRESENT
  difference_cause: UNKNOWN_MAILBOX_OR_SEARCH_INDEX_MUTABILITY_CONNECTOR_NORMALIZATION_OR_PROVIDER_VARIANCE
  exact_additional_result_count: UNKNOWN_WITHOUT_NEXT_PAGE_FETCH
official_contract_checked_2026_08_02:
  messages_list: https://developers.google.com/workspace/gmail/api/reference/rest/v1/users.messages/list
  search_filtering: https://developers.google.com/workspace/gmail/api/guides/filtering
  usage_limits: https://developers.google.com/workspace/gmail/api/reference/quota
  endpoint: GET_/gmail/v1/users/{userId}/messages
  q_supports_gmail_search_syntax: true
  q_not_available_with_gmail_metadata_scope: true
  list_response_message_fields: ID_AND_THREAD_ID_ONLY
  additional_details_require_messages_get: true
  connector_single_message_read_is_metadata_only: false_BODY_INCLUDED
  api_search_date_literals_interpreted_at_midnight_PST: true
  epoch_seconds_recommended_for_precise_timezone_boundaries: true
  messages_list_quota_units: 5
fresh_web_contract_retrieval_this_wake: TRANSIENTLY_UNAVAILABLE_NO_NEW_WEB_DERIVED_CLAIM_ADDED
failure_semantics:
  bounded_one_hour_search: DIRECTLY_OBSERVED_SUCCESS
  repeated_query_snapshot_stability: NOT_PROVEN_RESPONSE_DIFFERENCE_OBSERVED
  continuation_cursor_emission: DIRECTLY_OBSERVED
  next_page_membership: NOT_TESTED
  empty_result: NOT_TESTED
  invalid_query_or_page_token: NOT_TESTED
  permission_denial: NOT_TESTED
  quota_or_rate_limit: NOT_TESTED
  independent_cross_client_readback: NOT_TESTED
durability: EPHEMERAL_TIME_STAMPED_OBSERVATION_OVER_MUTABLE_MAILBOX_AND_SEARCH_STATE_NOT_AN_IMMUTABLE_SNAPSHOT
observability: MEDIUM_LOW_FOR_QUERY_BOUND_RESULT_COUNT_CONTINUATION_FLAG_AND_CONNECTOR_LATENCY_BUT_LOW_FOR_RAW_HTTP_IDENTITY_SCOPE_PROJECT_REQUEST_ID_QUOTA_AND_UPSTREAM_RETRIES
portability: MEDIUM_LOW_GMAIL_QUERY_SYNTAX_IDS_THREAD_SEMANTICS_ALIAS_DIFFERENCES_CURSOR_AND_SCOPE_RULES_ARE_PROVIDER_SPECIFIC
admitted_scope:
  - BOUNDED_READ_ONLY_MESSAGE_ID_SEARCH
  - EXPLICIT_EPOCH_TIME_WINDOW
  - SMALL_MAX_RESULTS
  - EXCLUDE_SPAM_AND_TRASH
  - COUNT_AND_CONTINUATION_PRESENCE_ONLY_PERSISTENCE
  - NO_MESSAGE_GET_OR_CONTENT_DISCLOSURE
excluded_scope:
  - MESSAGE_BODY_HEADER_SNIPPET_OR_ATTACHMENT_READ
  - SEND_DRAFT_REPLY_OR_FORWARD
  - LABEL_ARCHIVE_TRASH_DELETE_MARK_READ_OR_UNREAD
  - BROAD_MAILBOX_MINING
  - MAILBOX_COMPLETENESS_SNAPSHOT_STABILITY_OR_IDENTITY_CLAIMS
mandatory_gates:
  - USE_EPOCH_SECONDS_FOR_PRECISE_TIME_BOUNDS_WHEN_TIMEZONE_ACCURACY_MATTERS
  - TREAT_EACH_SEARCH_AS_A_TIME_STAMPED_OBSERVATION_NOT_A_DURABLE_SNAPSHOT
  - SET_SMALL_EXPLICIT_MAX_RESULTS_AND_PRESERVE_CONTINUATION_TOKEN_PRESENCE_SEPARATELY
  - NEVER_INFER_COMPLETENESS_FROM_RETURNED_COUNT_BELOW_CAP_OR_FROM_A_PRIOR_WAKE
  - TRAVERSE_PAGES_ONLY_UNDER_AN_EXPLICIT_BOUNDED_PAGE_AND_DATA_MINIMIZATION_BUDGET
  - DO_NOT_PERSIST_MESSAGE_IDS_OR_PAGE_TOKENS_WITHOUT_SEPARATE_JUSTIFICATION
  - DO_NOT_CALL_BODY_RETURNING_READS_WHEN_METADATA_ONLY_ACCESS_IS_THE_ADMITTED_SCOPE
  - DO_NOT_INFER_EXACT_OAUTH_SCOPE_MAILBOX_IDENTITY_QUOTA_CLASS_OR_BILLING_STATE_FROM_SUCCESS
  - NO_SEND_DRAFT_REPLY_FORWARD_LABEL_ARCHIVE_TRASH_DELETE_OR_MARK_STATE
verifier: RAW_GMAIL_USERS_MESSAGES_LIST_CALL_OR_DISTINCT_AUTHORIZED_GMAIL_CLIENT_USING_THE_SAME_SOURCE_BOUND_MAILBOX_EXACT_EPOCH_QUERY_CAP_AND_OBSERVATION_TIME
consumer:
  - HFO_EXECUTIVE_ASSISTANT_MAIL_TRIAGE_LOGIC
strongest_falsifier: A_DISTINCT_SOURCE_BOUND_CLIENT_RETURNS_NO_CONTINUATION_CURSOR_OR_MATERIALLY_DIFFERENT_PAGE_MEMBERSHIP_FOR_THE_SAME_MAILBOX_QUERY_CAP_AND_OBSERVATION_TIME
honest_flaw: PHASE2_DID_NOT_FETCH_THE_NEXT_PAGE_OR_TEST_METADATA_ONLY_GET_EMPTY_RESULT_INVALID_QUERY_PERMISSION_DENIAL_RATE_LIMIT_INDEPENDENT_CLIENT_OR_CONSUMER_ACK
phase_2_result:
  status: PHASE2_ACCEPTED_WITH_PAGINATION_AND_MUTABILITY_ANDON
  candidate_invocation_this_wake: true
  rationale: ONE_BOUNDED_ID_ONLY_QUERY_SUCCEEDED_AND_EXPOSED_A_CONTINUATION_CURSOR_DIFFERENT_FROM_PHASE1_WITHOUT_CONTENT_OR_MUTATION
review_expiry_utc: 2026-08-09T14:48:51Z
valid_time_utc: 2026-08-02T14:48:51Z
transaction_time_utc: SEE_GIT_COMMIT_METADATA
sealed: true
next_phase:
  phase: 3_of_4
  status: PENDING
  effect_ceiling: ONE_PRIVACY_SAFE_READ_ONLY_SYNTHETIC_INVALID_PAGE_TOKEN_PROBE_USING_THE_SAME_BOUNDED_QUERY_NO_RETRY_SANITIZED_ERROR_CAPTURE
  exclusions:
    - NEXT_VALID_PAGE_FETCH
    - SEND_DRAFT_REPLY_FORWARD
    - LABEL_ARCHIVE_TRASH_DELETE_OR_MARK_READ_UNREAD
    - MESSAGE_BODY_HEADER_SNIPPET_OR_ATTACHMENT_DISCLOSURE
    - BROAD_MAILBOX_MINING
prior_campaign:
  experiment_id: X13_GOOGLE_CALENDAR_FREEBUSY_READONLY_001
  final_version: 40
  decision: ADOPT_WITH_GATES
---

# X13 current campaign

Gmail bounded metadata search completed phase **2/4**.

The exact phase-1 query was repeated with `max_results=1`. It returned one opaque ID and a continuation token; neither value was persisted. No message content or mailbox mutation occurred.

The continuation-token state differs from phase 1, so search results are admitted only as time-stamped observations, not immutable snapshots. Measured operator relief remains `0`; surfaced cost was `$0`.

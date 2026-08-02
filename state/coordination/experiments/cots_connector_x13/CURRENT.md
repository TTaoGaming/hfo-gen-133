---
schema_id: hfo.gen133.x13.cots_connector_current.v1
experiment_id: X13_GMAIL_BOUNDED_METADATA_SEARCH_READONLY_001
version: 43
prior_version: 42
candidate: Gmail_bounded_exact_query_metadata_readonly_connector_surface
candidate_contract_reference: official_Gmail_users_messages_list_search_filtering_error_handling_and_usage_limits_plus_direct_connector_receipts
campaign_wake: 3_of_4
campaign_status: ACTIVE
phase_1_completed: true
phase_2_completed: true
phase_3_completed: true
phase_4_completed: false
phase_4_decision: PENDING
last_event:
  commit: a876690a0eb5163447abb0f39213b4f4c0c70fc4
  path: state/coordination/experiments/cots_connector_x13/20260802T154919Z_GMAIL_METADATA_PHASE3_INVALID_PAGE_TOKEN.md
  blob_sha: a833db58b1cf16e578765d750775ad1295e6019e
  exact_readback_completed: true
prior_current_commit: e241f94da53b20ca9509ba1cb551e255ef72c280
prior_current_blob_sha: fd7d7fc8243d2c0b4748e8471c61a5a26f993d58
carrier_task_id: 6a55c1733708819185088bf334e33ea5
carrier_task_id_match: true
carrier_task_id_observation_source: AUTOMATION_RUN_CONTEXT
effect_ceiling: PHASE3_ONE_PRIVACY_SAFE_READ_ONLY_SYNTHETIC_INVALID_PAGE_TOKEN_PROBE_NO_RETRY_SANITIZED_ERROR_CAPTURE_GIT_EVENT_CURRENT_ADVANCE_READBACK_AND_ONE_SHORT_NON_SECRET_SLACK_ANDON
adoption_credit: 3
adoption_credit_basis:
  - OFFICIAL_PRIMARY_MESSAGES_LIST_SEARCH_ERROR_AND_QUOTA_CONTRACT
  - ONE_BOUNDED_ID_ONLY_BASELINE_SEARCH
  - ONE_EXACT_QUERY_RECONCILIATION_WITH_CURSOR_PRESENCE
  - ONE_SYNTHETIC_INVALID_PAGE_TOKEN_FAILURE_PROBE
  - FAIL_CLOSED_WITHOUT_RESULT_OR_MAILBOX_CONTENT
  - STRUCTURED_NORMALIZED_ERROR_FIELDS_EXPOSED
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
  structured_error_mapping: 15_to_50_LOC_UNVALIDATED_NON_ADDITIVE
custom_policy_not_avoided:
  - MAILBOX_IDENTITY_AND_AUTHORITY
  - QUERY_SCOPE_AND_DATA_MINIMIZATION
  - SEARCH_TIMEZONE_AND_BOUNDARY_POLICY
  - MESSAGE_ID_AND_PAGE_TOKEN_REDACTION_AND_RETENTION
  - PAGINATION_COMPLETENESS_PAGE_BUDGET_AND_CURSOR_BINDING
  - SNAPSHOT_OR_MUTABILITY_SEMANTICS
  - ERROR_CLASSIFICATION_QUOTA_RETRY_AND_BACKOFF
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
  phase_3_failure_probe: 1
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
direct_phase_3_receipt:
  same_bounded_query_as_prior_phases: true
  max_results: 1
  synthetic_invalid_page_token_used: true
  synthetic_token_mailbox_derived: false
  exact_synthetic_token_persisted: false
  result_type: google_api_error
  normalized_code: invalidArgument
  normalized_status: INVALID_ARGUMENT
  normalized_reason: invalidArgument
  normalized_message: Failed_to_search_email_ids
  returned_message_id_count: 0
  next_page_token_present: false
  message_content_returned: false
  write_side_effect: false
  carrier_retry_count: 0
  token_echoed_in_visible_error: false
  raw_HTTP_status_headers_request_id_parameter_location_and_retry_after: NOT_EXPOSED
  external_call_time_ms: NOT_EXPOSED_FOR_FAILED_CALL
official_contract_checked_2026_08_02:
  messages_list: https://developers.google.com/workspace/gmail/api/reference/rest/v1/users.messages/list
  list_messages_guide: https://developers.google.com/workspace/gmail/api/guides/list-messages
  search_filtering: https://developers.google.com/workspace/gmail/api/guides/filtering
  error_handling: https://developers.google.com/workspace/gmail/api/guides/handle-errors
  usage_limits: https://developers.google.com/workspace/gmail/api/reference/quota
  endpoint: GET_/gmail/v1/users/{userId}/messages
  pageToken_is_token_for_specific_result_page: true
  nextPageToken_indicates_additional_page: true
  q_supports_gmail_search_syntax: true
  q_not_available_with_gmail_metadata_scope: true
  list_response_message_fields: ID_AND_THREAD_ID_ONLY
  additional_details_require_messages_get: true
  api_search_date_literals_interpreted_at_midnight_PST: true
  epoch_seconds_recommended_for_precise_timezone_boundaries: true
  HTTP_400_is_client_request_error: true
  invalid_parameter_value_or_combination_can_cause_400: true
  messages_list_quota_units: 5
fresh_web_contract_retrieval_this_wake: SUCCESS_OFFICIAL_GOOGLE_PRIMARY_DOCS
failure_semantics:
  bounded_one_hour_search: DIRECTLY_OBSERVED_SUCCESS
  repeated_query_snapshot_stability: NOT_PROVEN_RESPONSE_DIFFERENCE_OBSERVED
  continuation_cursor_emission: DIRECTLY_OBSERVED
  next_page_membership: NOT_TESTED
  synthetic_invalid_page_token: DIRECTLY_OBSERVED_FAIL_CLOSED_NORMALIZED_INVALID_ARGUMENT
  exact_upstream_invalid_field_and_HTTP_BODY: NOT_EXPOSED
  permission_denial: NOT_TESTED
  quota_or_rate_limit: NOT_TESTED
  independent_cross_client_readback: NOT_TESTED
durability: EPHEMERAL_TIME_STAMPED_OBSERVATION_OVER_MUTABLE_MAILBOX_AND_SEARCH_STATE_PAGE_TOKENS_NOT_DURABLE_RECORDS
observability: MEDIUM_LOW_FOR_QUERY_BOUND_RESULT_COUNT_CURSOR_FLAG_AND_NORMALIZED_ERROR_FIELDS_BUT_LOW_FOR_RAW_HTTP_IDENTITY_SCOPE_PROJECT_REQUEST_ID_PARAMETER_LOCATION_QUOTA_AND_UPSTREAM_RETRIES
portability: LOW_FOR_CURSOR_AND_ERROR_ENUMS_MEDIUM_LOW_OVERALL_GMAIL_QUERY_SYNTAX_IDS_THREAD_SEMANTICS_ALIAS_DIFFERENCES_CURSOR_AND_SCOPE_RULES_ARE_PROVIDER_SPECIFIC
admitted_scope:
  - BOUNDED_READ_ONLY_MESSAGE_ID_SEARCH
  - EXPLICIT_EPOCH_TIME_WINDOW
  - SMALL_MAX_RESULTS
  - EXCLUDE_SPAM_AND_TRASH
  - COUNT_CONTINUATION_PRESENCE_AND_SANITIZED_ERROR_CLASS_PERSISTENCE
  - NO_MESSAGE_GET_OR_CONTENT_DISCLOSURE
excluded_scope:
  - MESSAGE_BODY_HEADER_SNIPPET_OR_ATTACHMENT_READ
  - SEND_DRAFT_REPLY_OR_FORWARD
  - LABEL_ARCHIVE_TRASH_DELETE_MARK_READ_OR_UNREAD
  - BROAD_MAILBOX_MINING
  - MAILBOX_COMPLETENESS_SNAPSHOT_STABILITY_OR_IDENTITY_CLAIMS
  - VALID_NEXT_PAGE_TRAVERSAL_WITH_PERSISTED_CURSOR
mandatory_gates:
  - USE_EPOCH_SECONDS_FOR_PRECISE_TIME_BOUNDS_WHEN_TIMEZONE_ACCURACY_MATTERS
  - TREAT_EACH_SEARCH_AS_A_TIME_STAMPED_OBSERVATION_NOT_A_DURABLE_SNAPSHOT
  - SET_SMALL_EXPLICIT_MAX_RESULTS_AND_PRESERVE_CONTINUATION_TOKEN_PRESENCE_SEPARATELY
  - NEVER_INFER_COMPLETENESS_FROM_RETURNED_COUNT_BELOW_CAP_OR_FROM_A_PRIOR_WAKE
  - TRAVERSE_PAGES_ONLY_UNDER_AN_EXPLICIT_BOUNDED_PAGE_AND_DATA_MINIMIZATION_BUDGET
  - TREAT_PAGE_TOKENS_AS_OPAQUE_AND_NEVER_SYNTHESIZE_PARSE_OR_RECONSTRUCT
  - ACCEPT_A_CURSOR_ONLY_FROM_THE_IMMEDIATELY_PRECEDING_ADMITTED_RESPONSE_FOR_THE_SAME_MAILBOX_CONTEXT_AND_EXACT_QUERY_PARAMETERS
  - DO_NOT_PERSIST_MESSAGE_IDS_OR_PAGE_TOKEN_VALUES_WITHOUT_SEPARATE_JUSTIFICATION
  - ON_INVALID_ARGUMENT_STOP_AND_CORRECT_OR_DISCARD_THE_CURSOR_NO_BLIND_RETRY
  - DO_NOT_CLASSIFY_THE_EXACT_INVALID_FIELD_WITHOUT_PARAMETER_LOCATION_OR_INDEPENDENT_RAW_RECEIPT
  - KEEP_PERMISSION_AND_AUTHENTICATION_FAILURES_SEPARATE_FROM_CLIENT_INPUT_FAILURES
  - PRESERVE_CONNECTOR_NORMALIZED_ERROR_FIELDS_SEPARATELY_FROM_RAW_PROVIDER_CLAIMS
  - DO_NOT_CALL_BODY_RETURNING_READS_WHEN_METADATA_ONLY_ACCESS_IS_THE_ADMITTED_SCOPE
  - DO_NOT_INFER_EXACT_OAUTH_SCOPE_MAILBOX_IDENTITY_QUOTA_CLASS_OR_BILLING_STATE_FROM_SUCCESS
  - NO_SEND_DRAFT_REPLY_FORWARD_LABEL_ARCHIVE_TRASH_DELETE_OR_MARK_STATE
verifier: RAW_GMAIL_USERS_MESSAGES_LIST_CALL_OR_DISTINCT_AUTHORIZED_GMAIL_CLIENT_USING_THE_SAME_SOURCE_BOUND_MAILBOX_EXACT_QUERY_AND_A_DELIBERATELY_INVALID_SYNTHETIC_TOKEN
consumer:
  - HFO_EXECUTIVE_ASSISTANT_MAIL_TRIAGE_LOGIC
  - HFO_BOUNDED_PAGINATION_LOGIC
strongest_falsifier: A_RAW_OR_DISTINCT_SOURCE_BOUND_CLIENT_ACCEPTS_THE_SAME_SYNTHETIC_TOKEN_RETURNS_MAILBOX_RESULTS_OR_EXPOSES_A_MATERIALLY_DIFFERENT_STABLE_ERROR_CLASSIFICATION
honest_flaw: PHASE3_DID_NOT_TEST_VALID_NEXT_PAGE_EXPIRED_REAL_TOKEN_TOKEN_QUERY_MISMATCH_MALFORMED_QUERY_PERMISSION_DENIAL_401_403_429_5XX_INDEPENDENT_CLIENT_OR_CONSUMER_ACK
phase_3_result:
  status: PHASE3_ACCEPTED_WITH_OPAQUE_CURSOR_AND_NORMALIZED_ERROR_GATES
  candidate_invocation_this_wake: true
  rationale: ONE_SYNTHETIC_INVALID_PAGE_TOKEN_FAILED_CLOSED_WITH_STRUCTURED_NORMALIZED_ERROR_NO_CONTENT_NO_MUTATION_AND_NO_RETRY
review_expiry_utc: 2026-08-09T15:49:19Z
valid_time_utc: 2026-08-02T15:49:19Z
transaction_time_utc: SEE_GIT_COMMIT_METADATA
sealed: true
next_phase:
  phase: 4_of_4
  status: PENDING
  effect_ceiling: DECISION_ONLY_NO_ADDITIONAL_GMAIL_CAPABILITY_CALL_GIT_EVENT_CURRENT_ADVANCE_READBACK_AND_ONE_SHORT_NON_SECRET_SLACK_DECISION
  likely_decision: ADOPT_WITH_GATES
  exclusions:
    - ANY_ADDITIONAL_GMAIL_SEARCH_OR_READ
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

Gmail bounded metadata search completed phase **3/4**.

A synthetic invalid page token against the same bounded query failed closed with normalized `invalidArgument` / `INVALID_ARGUMENT`. No message IDs, content, cursor, or mailbox mutation were returned. The wrapper did not expose raw HTTP status, parameter location, request ID, quota headers, or latency for the failed call.

Measured operator relief remains `0`; surfaced cost was `$0`. Phase 4 is decision-only.

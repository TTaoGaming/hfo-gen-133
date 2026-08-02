---
schema_id: hfo.gen133.x13.cots_connector_current.v1
experiment_id: X13_GMAIL_BOUNDED_METADATA_SEARCH_READONLY_001
version: 44
prior_version: 43
candidate: Gmail_bounded_exact_query_metadata_readonly_connector_surface
candidate_contract_reference: official_Gmail_users_messages_list_search_filtering_error_handling_and_usage_limits_plus_direct_connector_receipts
campaign_wake: 4_of_4
campaign_status: COMPLETE
phase_1_completed: true
phase_2_completed: true
phase_3_completed: true
phase_4_completed: true
phase_4_decision: ADOPT_WITH_GATES
last_event:
  commit: 67c3888c73e0fce9214af9512fa33fabfc9feaee
  path: state/coordination/experiments/cots_connector_x13/20260802T164933Z_GMAIL_METADATA_PHASE4_DECISION.md
  blob_sha: f6f2eb36b253661a456b5d882f887fe354aa356f
  exact_readback_completed: true
prior_current_commit: 1a25b921de1361b18141e0e68cc9d8b6c5204c0b
prior_current_blob_sha: 4b3fa1b83175a7c26ebba697c453d772eea79ed6
carrier_task_id: 6a55c1733708819185088bf334e33ea5
carrier_task_id_match: true
carrier_task_id_observation_source: AUTOMATION_RUN_CONTEXT
effect_ceiling: DECISION_ONLY_NO_ADDITIONAL_GMAIL_CAPABILITY_CALL_GIT_EVENT_CURRENT_ADVANCE_READBACK_ONE_SHORT_NON_SECRET_SLACK_DECISION_AND_NEXT_CAMPAIGN_QUEUE
adoption_credit: 4
adoption_credit_basis:
  - OFFICIAL_PRIMARY_MESSAGES_LIST_SEARCH_ERROR_AND_QUOTA_CONTRACT
  - ONE_BOUNDED_ID_ONLY_BASELINE_SEARCH
  - ONE_EXACT_QUERY_RECONCILIATION_WITH_CURSOR_PRESENCE
  - ONE_SYNTHETIC_INVALID_PAGE_TOKEN_FAILURE_PROBE
  - FAIL_CLOSED_WITHOUT_RESULT_OR_MAILBOX_CONTENT
  - STRUCTURED_NORMALIZED_ERROR_FIELDS_EXPOSED
  - NO_MAILBOX_WRITE_SIDE_EFFECT
  - PHASE4_BOUNDED_ADOPTION_DECISION_WITH_EXPLICIT_SCOPE_AND_CREDENTIAL_GATES
fitness_credit: 0_PENDING_EXPLICIT_SOURCE_BOUND_CONSUMER_ACK_AND_MEASURED_OPERATOR_OUTCOME
consumer_ack: NOT_OBSERVED
same_provider_binding_weight: 0
independent_verification_closed: false
operator_relay_minutes: 0
operator_minutes_removed_measured: 0
operator_minutes_removed_estimate_per_bounded_discovery_query: 1_to_5_UNVALIDATED
custom_code_avoided_estimate:
  authenticated_message_list_query_cursor_extraction_and_id_normalization: 25_to_80_LOC_UNVALIDATED
  structured_error_mapping: 15_to_50_LOC_UNVALIDATED_NON_ADDITIVE
custom_policy_not_avoided:
  - MAILBOX_IDENTITY_AND_AUTHORITY
  - LIVE_OAUTH_SCOPE_AND_LEAST_PRIVILEGE_VERIFICATION
  - QUERY_SCOPE_AND_DATA_MINIMIZATION
  - SEARCH_TIMEZONE_AND_BOUNDARY_POLICY
  - MESSAGE_ID_AND_PAGE_TOKEN_REDACTION_AND_RETENTION
  - PAGINATION_COMPLETENESS_PAGE_BUDGET_AND_CURSOR_BINDING
  - SNAPSHOT_OR_MUTABILITY_SEMANTICS
  - ERROR_CLASSIFICATION_QUOTA_RETRY_AND_BACKOFF
  - INDEPENDENT_VERIFICATION
credentials:
  connector_authenticated_filtered_search_succeeded: true
  operator_supplied_credentials: 0
  authenticated_user_identity: UNKNOWN
  live_oauth_scope: UNKNOWN_AND_SUCCESSFUL_Q_SEARCH_IS_INCONSISTENT_WITH_GMAIL_METADATA_ONLY_SCOPE
  oauth_client_or_project: UNKNOWN
  delegated_or_direct_mailbox_authority: UNKNOWN
  credential_custody: UNKNOWN
  least_privilege_closed: false
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
  difference_cause: UNKNOWN_MAILBOX_OR_SEARCH_INDEX_MUTABILITY_CONNECTOR_NORMALIZATION_PROVIDER_VARIANCE_OR_RESULT_CAP_INTERACTION
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
  successful_q_search_proves_exact_scope: false
  successful_q_search_is_inconsistent_with_metadata_only_scope_claim: true
  list_response_message_fields: ID_AND_THREAD_ID_ONLY
  additional_details_require_messages_get: true
  api_search_date_literals_interpreted_at_midnight_PST: true
  epoch_seconds_recommended_for_precise_timezone_boundaries: true
  HTTP_400_is_client_request_error: true
  invalid_parameter_value_or_combination_can_cause_400: true
  messages_list_quota_units: 5
  published_new_model_per_minute_per_project_units: 1200000
  published_new_model_per_minute_per_user_per_project_units: 6000
  published_new_model_daily_project_threshold_units_before_planned_charges: 80000000
  live_project_quota_model_and_billing_state: UNKNOWN
fresh_web_contract_retrieval_this_wake: SUCCESS_OFFICIAL_GOOGLE_PRIMARY_DOCS
failure_semantics:
  bounded_one_hour_search: DIRECTLY_OBSERVED_SUCCESS
  repeated_query_snapshot_stability: NOT_PROVEN_RESPONSE_DIFFERENCE_OBSERVED
  continuation_cursor_emission: DIRECTLY_OBSERVED
  next_page_membership: NOT_TESTED
  synthetic_invalid_page_token: DIRECTLY_OBSERVED_FAIL_CLOSED_NORMALIZED_INVALID_ARGUMENT
  exact_upstream_invalid_field_and_HTTP_BODY: NOT_EXPOSED
  permission_denial: NOT_TESTED
  authentication_failure: NOT_TESTED
  quota_or_rate_limit: NOT_TESTED
  transient_server_failure: NOT_TESTED
  independent_cross_client_readback: NOT_TESTED
durability: EPHEMERAL_TIME_STAMPED_OBSERVATION_OVER_MUTABLE_MAILBOX_AND_SEARCH_STATE_PAGE_TOKENS_NOT_DURABLE_RECORDS
observability: MEDIUM_LOW_FOR_QUERY_BOUND_RESULT_COUNT_CURSOR_FLAG_SUCCESS_LATENCY_AND_NORMALIZED_ERROR_FIELDS_BUT_LOW_FOR_RAW_HTTP_IDENTITY_SCOPE_PROJECT_REQUEST_ID_PARAMETER_LOCATION_QUOTA_FAILED_CALL_LATENCY_AND_UPSTREAM_RETRIES
portability: MEDIUM_LOW_OVERALL_GMAIL_QUERY_SYNTAX_IDS_THREAD_SEMANTICS_ALIAS_DIFFERENCES_CURSOR_BINDING_SCOPE_RULES_AND_ERROR_ENUMS_ARE_PROVIDER_SPECIFIC
admitted_scope:
  - BOUNDED_READ_ONLY_MESSAGE_ID_SEARCH
  - EXPLICIT_EPOCH_TIME_WINDOW
  - SMALL_MAX_RESULTS
  - EXCLUDE_SPAM_AND_TRASH
  - COUNT_CONTINUATION_PRESENCE_AND_SANITIZED_ERROR_CLASS_PERSISTENCE
  - BOUNDED_DISCOVERY_ASSISTANCE_WITHOUT_CONTENT_READ_OR_MAILBOX_AUTHORITY
  - NO_MESSAGE_GET_OR_CONTENT_DISCLOSURE
excluded_scope:
  - MESSAGE_BODY_HEADER_SNIPPET_OR_ATTACHMENT_READ
  - SEND_DRAFT_REPLY_OR_FORWARD
  - LABEL_ARCHIVE_TRASH_DELETE_MARK_READ_OR_UNREAD
  - BROAD_MAILBOX_MINING
  - MAILBOX_COMPLETENESS_SNAPSHOT_STABILITY_OR_IDENTITY_CLAIMS
  - VALID_NEXT_PAGE_TRAVERSAL_WITH_PERSISTED_CURSOR
  - LEAST_PRIVILEGE_SCOPE_CLAIM
mandatory_gates:
  - USE_EPOCH_SECONDS_FOR_PRECISE_TIME_BOUNDS_WHEN_TIMEZONE_ACCURACY_MATTERS
  - TREAT_EACH_SEARCH_AS_A_TIME_STAMPED_OBSERVATION_NOT_A_DURABLE_SNAPSHOT
  - SET_SMALL_EXPLICIT_MAX_RESULTS_AND_PRESERVE_CONTINUATION_TOKEN_PRESENCE_SEPARATELY
  - NEVER_INFER_COMPLETENESS_FROM_RETURNED_COUNT_BELOW_CAP_RESULT_SIZE_ESTIMATE_OR_A_PRIOR_WAKE
  - TRAVERSE_PAGES_ONLY_UNDER_AN_EXPLICIT_BOUNDED_PAGE_TIME_AND_DATA_MINIMIZATION_BUDGET
  - TREAT_PAGE_TOKENS_AS_OPAQUE_AND_NEVER_SYNTHESIZE_PARSE_OR_RECONSTRUCT
  - ACCEPT_A_CURSOR_ONLY_FROM_THE_IMMEDIATELY_PRECEDING_ADMITTED_RESPONSE_FOR_THE_SAME_MAILBOX_CONTEXT_AND_EXACT_QUERY_PARAMETERS
  - DO_NOT_PERSIST_MESSAGE_IDS_OR_PAGE_TOKEN_VALUES_WITHOUT_SEPARATE_JUSTIFICATION
  - ON_INVALID_ARGUMENT_STOP_AND_CORRECT_OR_DISCARD_THE_CURSOR_NO_BLIND_RETRY
  - DO_NOT_CLASSIFY_THE_EXACT_INVALID_FIELD_WITHOUT_PARAMETER_LOCATION_OR_INDEPENDENT_RAW_RECEIPT
  - KEEP_CLIENT_INPUT_PERMISSION_AUTHENTICATION_QUOTA_AND_TRANSIENT_FAILURES_SEPARATE
  - PRESERVE_CONNECTOR_NORMALIZED_ERROR_FIELDS_SEPARATELY_FROM_RAW_PROVIDER_CLAIMS
  - DO_NOT_CALL_BODY_RETURNING_READS_WHEN_ID_ONLY_DISCOVERY_IS_THE_ADMITTED_SCOPE
  - DO_NOT_INFER_EXACT_OAUTH_SCOPE_MAILBOX_IDENTITY_QUOTA_CLASS_OR_BILLING_STATE_FROM_SUCCESS
  - DO_NOT_DESCRIBE_THIS_BINDING_AS_GMAIL_METADATA_LEAST_PRIVILEGE_WHILE_FILTERED_Q_SEARCH_SUCCEEDS_AND_SCOPE_EVIDENCE_IS_HIDDEN
  - NO_SEND_DRAFT_REPLY_FORWARD_LABEL_ARCHIVE_TRASH_DELETE_OR_MARK_STATE
verifier: RAW_GMAIL_USERS_MESSAGES_LIST_CALL_OR_DISTINCT_AUTHORIZED_GMAIL_CLIENT_USING_THE_SAME_SOURCE_BOUND_MAILBOX_EXACT_QUERY_CAP_AND_A_DELIBERATELY_INVALID_SYNTHETIC_TOKEN_WITH_RAW_RESPONSE_SCOPE_AND_REQUEST_METADATA
consumer:
  - HFO_EXECUTIVE_ASSISTANT_MAIL_DISCOVERY_LOGIC
  - HFO_BOUNDED_PAGINATION_LOGIC
strongest_falsifier: A_RAW_OR_DISTINCT_SOURCE_BOUND_CLIENT_ACCEPTS_THE_SAME_SYNTHETIC_TOKEN_RETURNS_MATERIALLY_DIFFERENT_MESSAGE_MEMBERSHIP_OR_STABLE_ERROR_CLASSIFICATION_OR_SHOWS_UNDISCLOSED_CONTENT_FETCH_OR_MAILBOX_MUTATION
honest_flaw: CAMPAIGN_DID_NOT_ESTABLISH_IDENTITY_OR_LEAST_PRIVILEGE_SCOPE_TRAVERSE_VALID_NEXT_PAGE_TEST_EXPIRED_REAL_TOKEN_QUERY_TOKEN_MISMATCH_MALFORMED_QUERY_401_403_429_5XX_INDEPENDENT_CLIENT_CONTENT_NONACCESS_AT_CREDENTIAL_LAYER_OR_CONSUMER_ACK
phase_4_result:
  decision: ADOPT_WITH_GATES
  candidate_invocation_this_wake: false
  rationale: BOUNDED_ID_ONLY_DISCOVERY_CURSOR_PRESENCE_AND_FAIL_CLOSED_INVALID_CURSOR_BEHAVIOR_WORKED_BUT_IDENTITY_LEAST_PRIVILEGE_SCOPE_COMPLETENESS_SNAPSHOT_STABILITY_RAW_ERROR_TELEMETRY_AND_INDEPENDENT_VERIFICATION_REMAIN_UNPROVEN
review_expiry_utc: 2026-08-09T16:49:33Z
valid_time_utc: 2026-08-02T16:49:33Z
transaction_time_utc: SEE_GIT_COMMIT_METADATA
sealed: true
next_campaign:
  experiment_id: X13_GOOGLE_DRIVE_BOUNDED_METADATA_SEARCH_READONLY_001
  candidate: Google_Drive_bounded_metadata_only_search_connector_surface
  phase: 1_of_4
  status: QUEUED
  effect_ceiling: OFFICIAL_CONTRACT_BASELINE_AND_ONE_BOUNDED_METADATA_ONLY_PROVIDER_PAGE_WITH_BEST_EFFORT_FETCH_FALSE_NO_FILE_CONTENT_NO_MUTATION
  proposed_micro_use:
    item_type: document
    best_effort_fetch: false
    small_explicit_topn: true
    provider_page_count: 1
  excluded_scope:
    - BEST_EFFORT_TEXT_HYDRATION_OR_FILE_CONTENT_FETCH
    - FILE_DOWNLOAD_OR_ATTACHMENT_READ
    - CREATE_UPDATE_DELETE_MOVE_RENAME_OR_UPLOAD
    - SHARE_PERMISSION_OR_OWNERSHIP_CHANGE
    - BROAD_DRIVE_MINING
    - PAGE_TRAVERSAL_WITHOUT_A_LATER_BOUNDED_PHASE
prior_campaign:
  experiment_id: X13_GOOGLE_CALENDAR_FREEBUSY_READONLY_001
  final_version: 40
  decision: ADOPT_WITH_GATES
  decision_event_commit: e6a8797de8a7f8e601812902457a40a2c30f31f6
  current_commit: a60950052db6eaf703b5558a3171fd937c3a2788
prior_prior_campaign:
  experiment_id: X13_SLACK_NATIVE_MESSAGE_RECEIPT_001
  final_version: 36
  decision: ADOPT_WITH_GATES
---

# X13 current campaign

Gmail bounded ID-only search completed phase **4/4** with decision **ADOPT_WITH_GATES**.

Use is admitted only for bounded, privacy-minimized message discovery with exact epoch bounds, a small result cap, opaque cursor handling, and no content read or mailbox mutation. It is not mailbox completeness, snapshot stability, identity proof, least-privilege scope proof, or authority to read or change email.

Measured operator relief remains `0`; surfaced cost was `$0`. The connector hid identity, live OAuth scope, project, quota counters, raw HTTP, request IDs, and upstream retries. Successful filtered `q` search is inconsistent with a `gmail.metadata`-only scope claim, so the binding must be treated as potentially broader than the admitted use.

The next queued campaign is Google Drive bounded metadata-only search: one provider page, `best_effort_fetch=false`, no file-content hydration, and no Drive mutation.

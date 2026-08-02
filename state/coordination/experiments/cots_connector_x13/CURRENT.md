---
schema_id: hfo.gen133.x13.cots_connector_current.v1
experiment_id: X13_GMAIL_BOUNDED_METADATA_SEARCH_READONLY_001
version: 41
prior_version: 40
candidate: Gmail_bounded_exact_query_metadata_readonly_connector_surface
candidate_contract_reference: official_Gmail_users_messages_list_search_filtering_and_usage_limits_plus_direct_connector_receipt
campaign_wake: 1_of_4
campaign_status: ACTIVE
phase_1_completed: true
phase_2_completed: false
phase_3_completed: false
phase_4_completed: false
phase_4_decision: PENDING
last_event:
  commit: de57a8600975bedacb4d09cf18677d2cb727706c
  path: state/coordination/experiments/cots_connector_x13/20260802T134837Z_GMAIL_METADATA_PHASE1_BASELINE.md
  blob_sha: 58b5c11aeba24b1b345a0c5e3482969fcdb0cee8
  exact_readback_completed: true
prior_current_commit: a60950052db6eaf703b5558a3171fd937c3a2788
prior_current_blob_sha: 6559d72fa45930bfc237daaf99d82035e7e5e1a8
carrier_task_id: 6a55c1733708819185088bf334e33ea5
carrier_task_id_match: true
carrier_task_id_observation_source: AUTOMATION_RUN_CONTEXT
effect_ceiling: PHASE1_OFFICIAL_CONTRACT_BASELINE_ONE_BOUNDED_ID_ONLY_QUERY_GIT_EVENT_CURRENT_ADVANCE_READBACK_AND_ONE_SHORT_NON_SECRET_SLACK_FACT
adoption_credit: 1
adoption_credit_basis:
  - OFFICIAL_PRIMARY_MESSAGES_LIST_SEARCH_AND_QUOTA_CONTRACT
  - ONE_BOUNDED_ONE_HOUR_EPOCH_QUERY
  - MAX_RESULTS_3
  - ONE_OPAQUE_MESSAGE_ID_RETURNED_NOT_PERSISTED
  - NO_NEXT_PAGE_TOKEN
  - NO_HEADER_SNIPPET_BODY_OR_ATTACHMENT_RETURNED
  - NO_MAILBOX_WRITE_SIDE_EFFECT
fitness_credit: 0_PENDING_EXPLICIT_SOURCE_BOUND_CONSUMER_ACK_AND_MEASURED_OPERATOR_OUTCOME
consumer_ack: NOT_OBSERVED
same_provider_binding_weight: 0
independent_verification_closed: false
operator_relay_minutes: 0
operator_minutes_removed_measured: 0
operator_minutes_removed_estimate: UNKNOWN
custom_code_avoided_estimate:
  authenticated_message_list_query_pagination_and_id_normalization: 25_to_80_LOC_UNVALIDATED
custom_policy_not_avoided:
  - MAILBOX_IDENTITY_AND_AUTHORITY
  - QUERY_SCOPE_AND_DATA_MINIMIZATION
  - SEARCH_TIMEZONE_AND_BOUNDARY_POLICY
  - MESSAGE_ID_REDACTION_AND_RETENTION
  - PAGINATION_COMPLETENESS
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
  phase_2_micro_use: 0
  phase_3_failure_probe: 0
  phase_4_decision_only: 0
actual_upstream_request_count: UNKNOWN
actual_quota_class: UNKNOWN
retry_count: 0_AT_CARRIER_LEVEL_UPSTREAM_UNKNOWN
billing_counters: NOT_EXPOSED
live_HTTP_status_headers_request_id_retry_after_or_rate_limit_headers: NOT_EXPOSED
direct_phase_1_receipt:
  query_class: ONE_HOUR_EPOCH_BOUNDED_EXCLUDING_SPAM_AND_TRASH
  query_after_epoch_exclusive: 1785672000
  query_before_epoch_exclusive: 1785675600
  query_window_utc: 2026-08-02T12:00:00Z_to_2026-08-02T13:00:00Z
  max_results: 3
  returned_message_id_count: 1
  exact_message_ids_persisted: false
  next_page_token_present: false
  result_size_estimate_exposed: false
  message_headers_returned: false
  message_snippets_returned: false
  message_bodies_returned: false
  attachments_returned_or_read: false
  external_call_time_ms: 610
  top_level_error: null
  write_side_effect: false
official_contract_checked_2026_08_02:
  messages_list: https://developers.google.com/workspace/gmail/api/reference/rest/v1/users.messages/list
  search_filtering: https://developers.google.com/workspace/gmail/api/guides/filtering
  usage_limits: https://developers.google.com/workspace/gmail/api/reference/quota
  endpoint: GET_/gmail/v1/users/{userId}/messages
  q_supports_gmail_search_syntax: true
  q_not_available_with_gmail_metadata_scope: true
  max_results_default: 100
  max_results_maximum: 500
  list_response_message_fields: ID_AND_THREAD_ID_ONLY
  additional_details_require_messages_get: true
  api_search_date_literals_interpreted_at_midnight_PST: true
  epoch_seconds_recommended_for_precise_timezone_boundaries: true
  gmail_ui_alias_expansion_not_available_in_api: true
  gmail_ui_thread_wide_search_not_available_in_api: true
  messages_list_quota_units: 5
  published_new_model_per_minute_per_project_quota_units: 1200000
  published_new_model_per_minute_per_user_per_project_quota_units: 6000
  published_daily_project_threshold_before_planned_charges_quota_units: 80000000
  standard_use_no_additional_cost_under_threshold: true
failure_semantics:
  bounded_one_hour_search: DIRECTLY_OBSERVED_SUCCESS
  empty_result: NOT_TESTED
  pagination_second_page: NOT_TESTED
  invalid_query: NOT_TESTED
  permission_denial: NOT_TESTED
  quota_or_rate_limit: NOT_TESTED
  independent_cross_client_readback: NOT_TESTED
durability: EPHEMERAL_POINT_IN_TIME_SEARCH_OVER_MUTABLE_MAILBOX_STATE
observability: MEDIUM_LOW_FOR_QUERY_BOUND_RESULT_COUNT_PAGINATION_FLAG_AND_CONNECTOR_LATENCY_BUT_LOW_FOR_RAW_HTTP_IDENTITY_SCOPE_PROJECT_REQUEST_ID_QUOTA_AND_UPSTREAM_RETRIES
portability: MEDIUM_LOW_GMAIL_QUERY_SYNTAX_LABEL_IDS_THREAD_SEMANTICS_ALIAS_DIFFERENCES_AND_SCOPE_RULES_ARE_PROVIDER_SPECIFIC
admitted_scope:
  - BOUNDED_READ_ONLY_MESSAGE_ID_SEARCH
  - EXPLICIT_EPOCH_TIME_WINDOW
  - SMALL_MAX_RESULTS
  - EXCLUDE_SPAM_AND_TRASH
  - COUNT_ONLY_PERSISTENCE
  - NO_MESSAGE_GET_OR_CONTENT_DISCLOSURE
excluded_scope:
  - MESSAGE_BODY_HEADER_SNIPPET_OR_ATTACHMENT_READ
  - SEND_DRAFT_REPLY_OR_FORWARD
  - LABEL_ARCHIVE_TRASH_DELETE_MARK_READ_OR_UNREAD
  - BROAD_MAILBOX_MINING
  - MAILBOX_COMPLETENESS_OR_IDENTITY_CLAIMS
mandatory_gates:
  - USE_EPOCH_SECONDS_FOR_PRECISE_TIME_BOUNDS_WHEN_TIMEZONE_ACCURACY_MATTERS
  - SET_SMALL_EXPLICIT_MAX_RESULTS_AND HANDLE_PAGINATION_SEPARATELY
  - TREAT_RESULT_SIZE_ESTIMATE_AS_NONAUTHORITATIVE_WHEN_EXPOSED
  - DO_NOT_PERSIST_MESSAGE_IDS_HEADERS_SUBJECTS_SENDERS_SNIPPETS_BODIES_OR_ATTACHMENT_NAMES_WITHOUT_SEPARATE_JUSTIFICATION
  - DO_NOT_INFER_EXACT_OAUTH_SCOPE_FROM_SUCCESSFUL_SEARCH
  - DO_NOT_ASSUME_GMAIL_UI_ALIAS_EXPANSION_OR_THREAD_WIDE_SEARCH_SEMANTICS
  - EMPTY_OR_BOUNDED_RESULTS_PROVE_ONLY_THIS_QUERY_RESPONSE
  - NO_SEND_DRAFT_REPLY_FORWARD_LABEL_ARCHIVE_TRASH_DELETE_OR_MARK_STATE
verifier: RAW_GMAIL_USERS_MESSAGES_LIST_CALL_OR_DISTINCT_AUTHORIZED_GMAIL_CLIENT_USING_THE_SAME_EPOCH_QUERY_WITH_RAW_RESPONSE_SCOPE_AND_MAILBOX_IDENTITY_EVIDENCE
consumer:
  - HFO_EXECUTIVE_ASSISTANT_MAIL_TRIAGE_LOGIC
strongest_falsifier: A_DISTINCT_AUTHORIZED_CLIENT_RETURNS_MATERIALLY_DIFFERENT_ID_COUNT_OR_PAGINATION_FOR_THE_SAME_SOURCE_BOUND_MAILBOX_AND_QUERY_OR_THE_CONNECTOR_FETCHES_CONTENT_DESPITE_ID_ONLY_ACTION
honest_flaw: BASELINE_TESTED_ONLY_ONE_ONE_HOUR_WINDOW_WITH_ONE_OPAQUE_RESULT_NO_HEADERS_BODY_ATTACHMENTS_LABEL_FILTER_SECOND_PAGE_EMPTY_RESULT_INVALID_QUERY_PERMISSION_DENIAL_RATE_LIMIT_OR_INDEPENDENT_READBACK
phase_1_result:
  status: PHASE1_ACCEPTED_WITH_SCOPE_TIMEZONE_AND_COMPLETENESS_GATES
  candidate_invocation_this_wake: true
  rationale: ONE_BOUNDED_ID_ONLY_SEARCH_SUCCEEDED_WITH_NO_CONTENT_OR_MUTATION_BUT_IDENTITY_SCOPE_COMPLETENESS_AND_QUOTA_REMAIN_UNPROVEN
review_expiry_utc: 2026-08-09T13:48:37Z
valid_time_utc: 2026-08-02T13:48:37Z
transaction_time_utc: SEE_GIT_COMMIT_METADATA
sealed: true
next_phase:
  phase: 2_of_4
  status: PENDING
  effect_ceiling: ONE_BOUNDED_EXACT_QUERY_RETURNING_AT_MOST_ONE_MESSAGE_THEN_METADATA_ONLY_READ_IF_A_SEPARATE_HEADER_ONLY_ACTION_IS_AVAILABLE_OTHERWISE_ID_ONLY_RECONCILIATION
  exclusions:
    - SEND_DRAFT_REPLY_FORWARD
    - LABEL_ARCHIVE_TRASH_DELETE_OR_MARK_READ_UNREAD
    - MESSAGE_BODY_OR_ATTACHMENT_DISCLOSURE
    - BROAD_MAILBOX_MINING
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

Gmail bounded metadata search completed phase **1/4**.

One exact one-hour epoch-bounded query returned one opaque message ID and no next-page token. The ID was not persisted. No headers, snippets, bodies, attachments, or mailbox mutations were requested or returned.

Measured operator relief remains `0`; surfaced cost was `$0`. Mailbox identity, exact OAuth scope, live quota, pagination completeness, and independent verification remain unknown.

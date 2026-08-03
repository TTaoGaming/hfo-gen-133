---
schema_id: hfo.gen133.x13.cots_connector_current.v1
experiment_id: X13_GOOGLE_CALENDAR_BOUNDED_EVENT_WINDOW_READONLY_001
version: 56
prior_version: 55
candidate: Google_Calendar_bounded_event_window_readonly_surface
candidate_contract_reference: official_Google_Calendar_events_list_quota_error_and_sync_contracts_plus_direct_connector_receipts
campaign_wake: 4_of_4
campaign_status: COMPLETE
phase_1_completed: true
phase_2_completed: true
phase_3_completed: true
phase_4_completed: true
phase_4_decision: ADOPT_WITH_GATES
carrier_task_id: 6a55c1733708819185088bf334e33ea5
carrier_task_id_match: true
wip: 1
last_event:
  commit: 335dbc5329fe238835faa67ff76e5681d54e11cd
  path: state/coordination/experiments/cots_connector_x13/20260803T044931Z_GOOGLE_CALENDAR_EVENT_WINDOW_PHASE4_DECISION_ADOPT_WITH_GATES.md
  blob_sha: b36f80785b7a9d146127058e7dbef3c36e185cb3
  exact_readback_completed: true
prior_current_commit: 1f0abe120f100b52a52e23210ef77529a4de08ba
prior_current_blob_sha: 44e27a0b6cbbbbb9dfeb471a01100fd2a1cdde20
effect_ceiling: PHASE4_DECISION_EVENT_CURRENT_ADVANCE_READBACK_AND_ONE_SHORT_SLACK_MEASURED_DECISION
adoption_credit: 1
fitness_credit: 0_PENDING_SOURCE_BOUND_CONSUMER_ACK_AND_MEASURED_OPERATOR_OUTCOME
consumer_ack: NOT_OBSERVED
operator_minutes_removed_measured: 0
operator_minutes_removed_estimate_per_schedule_window_check: 1_to_4_UNVALIDATED
custom_code_avoided_estimate:
  authenticated_event_list_time_bounds_pagination_and_normalization: 45_to_140_LOC_UNVALIDATED
custom_policy_not_avoided:
  - STRICT_CLIENT_SIDE_RFC3339_PARSE_AND_BOUND_ORDER_VALIDATION
  - EMPTY_RESULT_STATE_CLASSIFICATION_AND_NEGATIVE_EVIDENCE_HANDLING
  - DATA_MINIMIZATION_AND_PRIVATE_EVENT_FIELD_HANDLING
  - ACCOUNT_IDENTITY_CREDENTIAL_TYPE_AUTHORITY_AND_LEAST_PRIVILEGE
  - TIMEZONE_ALL_DAY_LONG_RUNNING_AND_RECURRENCE_SEMANTICS
  - PAGINATION_COMPLETENESS_ORDERING_AND_DUPLICATE_CONTROL
  - SNAPSHOT_INCREMENTAL_SYNC_AND_TOKEN_DURABILITY
  - RATE_LIMIT_RETRY_BACKOFF_AND_COST_ACCOUNTING
  - INDEPENDENT_VERIFICATION
credentials:
  connector_reached_primary_calendar_without_error: true
  operator_supplied_credentials: 0
  authenticated_identity: UNKNOWN
  credential_type: UNKNOWN
  effective_oauth_scope: UNKNOWN
  access_role: NOT_EXPOSED
  credential_custody: UNKNOWN
  least_privilege_closed: false
paid_cost_usd_observed: 0_NO_CHARGE_SURFACED
campaign_candidate_invocations:
  phase_1_event_window_queries: 1
  phase_1_returned_events: 3
  phase_1_next_page_token_present: true
  phase_2_event_window_queries: 1
  phase_2_returned_events: 1
  phase_2_next_page_token_present: true
  phase_3_inverted_bound_queries: 1
  phase_3_returned_events: 0
  phase_3_visible_error: false
  phase_4_additional_calendar_calls: 0
  total_queries: 3
  total_returned_events: 4
actual_upstream_request_count: UNKNOWN
actual_quota_units_consumed: UNKNOWN
actual_quota_class: UNKNOWN_LEGACY_PROJECT_EXCEPTION_POSSIBLE
retry_count: 0_AT_CARRIER_LEVEL_UPSTREAM_UNKNOWN
billing_counters: NOT_EXPOSED
live_request_id_retry_after_rate_limit_or_quota_headers: NOT_EXPOSED
direct_phase_1_receipt:
  action: Google_Calendar.search_events
  calendar_id: primary
  time_min_utc: 2026-08-03T01:48:00Z
  time_max_utc: 2026-08-04T01:48:00Z
  requested_timezone: America/Denver
  requested_max_results: 3
  returned_event_count: 3
  next_page_token_present: true
  connector_error: null
  external_call_time_ms: 468
  carrier_retries: 0
  write_notification_or_invitation_effect: false
  exact_private_event_values_promoted: false
direct_phase_2_receipt:
  action: Google_Calendar.search_events
  calendar_id: primary
  time_min_utc: 2026-08-03T01:48:00Z
  time_max_utc: 2026-08-03T07:48:00Z
  requested_timezone: America/Denver
  requested_max_results: 1
  returned_event_count: 1
  next_page_token_present: true
  connector_error: null
  external_call_time_ms: 466
  carrier_retries: 0
  write_notification_or_invitation_effect: false
  exact_private_event_values_promoted: false
direct_phase_3_receipt:
  action: Google_Calendar.search_events
  calendar_id: primary
  synthetic_probe: true
  time_min_utc: 2026-08-03T07:48:00Z
  time_max_utc: 2026-08-03T01:48:00Z
  time_min_is_after_time_max: true
  requested_timezone: America/Denver
  requested_max_results: 1
  page_token_supplied: false
  returned_event_count: 0
  next_page_token_present: false
  connector_error: null
  connector_error_code: null
  connector_http_status: null
  clamp_errors: null
  clamp_rewrites: null
  external_call_time_ms: 195
  carrier_retries: 0
  write_notification_or_invitation_effect: false
  exact_private_event_values_promoted: false
measured_facts:
  bounded_primary_calendar_event_window_reads_succeeded: true
  small_page_caps_and_cursor_presence_observed: true
  overlapping_event_start_before_lower_bound_observed_twice: true
  full_private_event_content_surfaced_by_default: true
  durable_log_minimization_applied: true
  official_contract_requires_time_min_strictly_less_than_time_max: true
  inverted_bounds_returned_empty_array_and_no_visible_error: true
  valid_empty_window_and_malformed_bound_state_indistinguishable_at_connector_surface: true
  raw_parameter_forwarding_dropping_or_rewrite: UNKNOWN
  conclusion_scope: CONNECTOR_SURFACE_ONLY_NOT_RAW_GOOGLE_API
privacy_andon:
  triggered: true
  measured_fact: FULL_EVENT_SUMMARIES_DESCRIPTIONS_IDS_URLS_AND_TIMING_SURFACED_BY_DEFAULT_ON_SUCCESS_PATH_CALLS
  durable_log_minimization_applied: true
semantic_andon:
  triggered: true
  measured_fact: INVERTED_RFC3339_BOUNDS_RETURNED_ZERO_EVENTS_AND_NO_ERROR
  implication: EMPTY_ARRAY_CANNOT_PROVE_A_VALID_EMPTY_CALENDAR_WINDOW_UNLESS_BOUNDS_ARE_VALIDATED_BEFORE_CALL
official_contract_checked_2026_08_03:
  events_list: https://developers.google.com/workspace/calendar/api/v3/reference/events/list
  errors: https://developers.google.com/workspace/calendar/api/guides/errors
  usage_limits: https://developers.google.com/workspace/calendar/api/guides/quota
  incremental_sync: https://developers.google.com/workspace/calendar/api/guides/sync
  endpoint: GET_/calendar/v3/calendars/{calendarId}/events
  primary_alias: LOGGED_IN_USERS_PRIMARY_CALENDAR
  time_min_semantics: EXCLUSIVE_LOWER_BOUND_ON_EVENT_END
  time_max_semantics: EXCLUSIVE_UPPER_BOUND_ON_EVENT_START
  bound_order_requirement: TIME_MIN_MUST_BE_SMALLER_THAN_TIME_MAX_WHEN_BOTH_SET
  max_results_semantics: PAGE_MAXIMUM_NOT_TOTAL_COUNT
  next_page_token_semantics: MORE_RESULTS_AVAILABLE
  next_sync_token_semantics: FINAL_PAGE_ONLY
  expired_sync_token_behavior: HTTP_410_FULL_RESYNC_REQUIRED
  post_2026_05_01_requests_per_minute_per_project_if_applicable: 10000
  post_2026_05_01_requests_per_minute_per_user_per_project_if_applicable: 600
  post_2026_05_01_requests_per_day_before_charges_if_applicable: 1000000
failure_semantics:
  success_path: OBSERVED_TWICE
  event_window_overlap_behavior: OBSERVED_TWICE
  small_result_cap_and_cursor_behavior: OBSERVED
  invalid_bounds: OBSERVED_AS_SEMANTIC_EMPTY_SUCCESS_AT_CONNECTOR_SURFACE
  valid_empty_window: NOT_TESTED
  invalid_page_token: NOT_TESTED
  authentication_or_permission_denial: NOT_TESTED
  quota_or_rate_limit: NOT_TESTED
  transient_server_failure: NOT_TESTED
  independent_raw_or_UI_readback: NOT_TESTED
durability: EPHEMERAL_POINT_IN_TIME_QUERY_OVER_MUTABLE_CALENDAR_STATE_NOT_A_SNAPSHOT_SYNC_OR_EVENT_STREAM
observability: NORMALIZED_EVENT_FIELD_CLASSES_COUNT_CURSOR_PRESENCE_ERROR_FIELDS_CLAMP_FIELDS_AND_LATENCY_VISIBLE_RAW_HTTP_REQUEST_RESPONSE_REQUEST_ID_COLLECTION_ETAG_ACCESS_ROLE_SYNC_TOKEN_QUOTA_HEADERS_PARAMETER_FORWARDING_ORDERING_AND_UPSTREAM_RETRIES_HIDDEN
portability: MEDIUM_RFC3339_WINDOW_AND_BOUND_ORDER_VALIDATION_PORTABLE_GOOGLE_EVENT_IDS_RECURRENCE_FIELDS_PAGE_TOKENS_AND_PRIMARY_ALIAS_PROVIDER_SPECIFIC
admitted_scope:
  - BOUNDED_READ_ONLY_EVENT_WINDOW_DISCOVERY_ON_AN_EXPLICIT_CALENDAR_ALIAS
  - EXPLICIT_LOCALLY_VALIDATED_RFC3339_TIME_MIN_TIME_MAX_RESPONSE_TIMEZONE_AND_SMALL_PAGE_CAP
  - PRIVACY_MINIMIZED_COUNTS_TIME_BUCKETS_AND_SOURCE_BOUND_REFERENCES
  - POSITIVE_EVENT_OBSERVATIONS_WITH_OBSERVATION_TIME_AND_EXACT_QUERY_CONTEXT
  - CONTINUATION_TOKEN_PRESENCE_AS_PAGINATION_SIGNAL_WITHOUT_TOKEN_VALUE_PERSISTENCE
excluded_scope:
  - EVENT_CREATE_UPDATE_DELETE_MOVE_IMPORT_OR_QUICK_ADD
  - INVITATION_RESPONSE_ATTENDEE_CHANGE_EMAIL_OR_NOTIFICATION_EFFECT
  - DURABLE_FULL_CALENDAR_SNAPSHOT_OR_INCREMENTAL_SYNC
  - COMPLETENESS_NO_CONFLICT_IDENTITY_ACCESS_ROLE_SCOPE_WRITE_AUTHORITY_OR_BILLING_CLAIMS
  - UNNECESSARY_PERSISTENCE_OF_EVENT_TEXT_IDS_URLS_ATTENDEES_LOCATIONS_OR_TOKEN_VALUES
mandatory_gates:
  - VALIDATE_RFC3339_PARSEABILITY_AND_REQUIRE_TIME_MIN_STRICTLY_LESS_THAN_TIME_MAX_BEFORE_CONNECTOR_INVOCATION
  - CLASSIFY_INVALID_LOCAL_BOUNDS_SEPARATELY_FROM_VALID_EMPTY_WINDOW_NO_MATCH_PERMISSION_RATE_LIMIT_TRANSPORT_AND_PROVIDER_FAILURE
  - NEVER_TRANSLATE_AN_EMPTY_CONNECTOR_ARRAY_INTO_NO_CALENDAR_CONFLICT_WITHOUT_VALIDATED_BOUNDS_AND_AN_ADMITTED_COMPLETENESS_STRATEGY
  - PRESERVE_EXACT_VALIDATED_BOUNDS_CALENDAR_ALIAS_RESPONSE_TIMEZONE_PAGE_CAP_AND_OBSERVATION_TIME
  - INTERPRET_TIME_MIN_AS_EXCLUSIVE_LOWER_BOUND_ON_EVENT_END_AND_TIME_MAX_AS_EXCLUSIVE_UPPER_BOUND_ON_EVENT_START
  - TREAT_OVERLAPPING_LONG_RUNNING_AND_ALL_DAY_EVENTS_AS_VALID_MATCHES
  - TREAT_MAX_RESULTS_AS_PAGE_CAP_NOT_TOTAL_MATCH_COUNT
  - TREAT_NEXT_PAGE_TOKEN_PRESENCE_AS_DIRECT_EVIDENCE_OF_MORE_WRAPPER_VISIBLE_RESULTS
  - MINIMIZE_EVENT_CONTENT_IN_MEMORY_BEFORE_GIT_SLACK_OR_DOWNSTREAM_FANOUT
  - DO_NOT_PERSIST_EVENT_IDS_TITLES_DESCRIPTIONS_URLS_ATTENDEES_LOCATIONS_OR_TOKEN_VALUES_UNLESS_REQUIRED_BY_AN_ADMITTED_CONSUMER
  - DO_NOT_INFER_IDENTITY_ACCESS_ROLE_SCOPE_WRITE_OR_NOTIFICATION_AUTHORITY_FROM_READ_SUCCESS
  - DO_NOT_CLAIM_SNAPSHOT_STABILITY_COMPLETENESS_OR_DURABILITY_FROM_ONE_QUERY_OR_ONE_PAGE
  - KEEP_ALL_MUTATING_INVITATION_EMAIL_AND_NOTIFICATION_CAPABILITIES_EXCLUDED
verifier: RAW_GOOGLE_CALENDAR_EVENTS_LIST_WITH_IDENTICAL_CALENDAR_TIME_MIN_TIME_MAX_TIMEZONE_MAX_RESULTS_AND_PAGE_CONTEXT_PLUS_CALENDAR_UI_FOR_VALID_WINDOWS
consumer:
  - HFO_EXECUTIVE_ASSISTANT_BOUNDED_DAY_PLAN_READS
  - HFO_DEADLINE_AND_CONFLICT_DETECTION_WITH_PRIVACY_MINIMIZATION
  - HFO_WAITING_CLOCK_AND_MORNING_PACKET_SOURCE_BOUND_OBSERVATIONS
strongest_falsifier: SAME_CONTEXT_RAW_EVENTS_LIST_OR_CALENDAR_UI_SHOWS_A_MATERIAL_FALSE_NEGATIVE_FOR_A_LOCALLY_VALIDATED_WINDOW_OR_THE_CONNECTOR_CONTINUES_TO_RETURN_SEMANTIC_EMPTY_SUCCESS_FOR_INVALID_INPUT_WITHOUT_A_CALLER_SIDE_GATE
honest_flaw: NO_RAW_API_OR_CALENDAR_UI_COMPARISON_NO_VALID_EMPTY_WINDOW_TEST_NO_VALID_PAGE_TRAVERSAL_NO_IDENTITY_SCOPE_OR_ACCESS_ROLE_PROOF_NO_PERMISSION_RATE_LIMIT_OR_TRANSIENT_FAILURE_NO_CONSUMER_ACK ZERO_MEASURED_OPERATOR_MINUTES AND_CONNECTOR_DEFAULT_SUCCESS_PAYLOADS_EXPOSE_MORE_PRIVATE_EVENT_DATA_THAN_COUNT_ONLY_CONSUMERS_REQUIRE
phase_1_result:
  disposition: PHASE1_ACCEPTED_WITH_CONTENT_MINIMIZATION_PAGINATION_AND_TEMPORAL_SEMANTICS_GATES
phase_2_result:
  disposition: PHASE2_ACCEPTED_WITH_CAP_CURSOR_OVERLAP_AND_DATA_MINIMIZATION_GATES
phase_3_result:
  disposition: PHASE3_ACCEPTED_WITH_SEMANTIC_EMPTY_RESULT_ANDON_AND_CLIENT_SIDE_BOUND_VALIDATION_GATE
phase_4_result:
  disposition: ADOPT_WITH_GATES_FOR_BOUNDED_PRIVACY_MINIMIZED_SOURCE_BOUND_READS_ONLY
next_wake:
  experiment_id: X13_GMAIL_BOUNDED_MESSAGE_METADATA_SEARCH_READONLY_001
  phase: 1_of_4
  proposed_action: OFFICIAL_CONTRACT_BASELINE_AND_ONE_BOUNDED_READ_ONLY_METADATA_SEARCH
  excluded_effects: SEND_DRAFT_MODIFY_LABEL_ARCHIVE_TRASH_DELETE_ATTACHMENT_DOWNLOAD_OR_SECRET_EXPOSURE
review_expiry_utc: 2026-08-10T04:49:31Z
valid_time_utc: 2026-08-03T04:49:31Z
transaction_time_utc: SEE_GIT_COMMIT_METADATA
sealed: true
prior_campaign:
  experiment_id: X13_GITHUB_ACTIONS_WORKFLOW_RUN_STATUS_READONLY_001
  final_version: 52
  decision: ADOPT_WITH_GATES
prior_prior_campaign:
  experiment_id: X13_GOOGLE_DRIVE_BOUNDED_METADATA_SEARCH_READONLY_001
  final_version: 48
  decision: ADOPT_WITH_GATES
---

# X13 current campaign

Google Calendar bounded event-window read-only campaign **4/4** is complete with decision **ADOPT_WITH_GATES**.

Admitted use is limited to bounded, source-bound, read-only event-window discovery with explicit locally validated RFC3339 bounds, explicit calendar alias and response timezone, small page caps, and privacy minimization before durable logging or fan-out.

Two success-path reads returned four events total and exposed continuation tokens. Overlap semantics were observed twice. A phase-3 inverted-bound probe returned an empty success shape rather than a visible error at the connector surface, so empty arrays are not authoritative evidence of no conflict unless local validation passed and an admitted completeness strategy exists.

Mutation, invitation, email, notification, durable snapshot, completeness, identity, access-role, OAuth-scope, write-authority, and billing claims remain excluded. Measured operator relief is `0`; surfaced cost was `$0`; ConsumerAck and independent verification remain absent.

Next wake starts phase 1 of bounded read-only Gmail message metadata search. No send, draft, label modification, archive, Trash, deletion, attachment download, or secret exposure is authorized.
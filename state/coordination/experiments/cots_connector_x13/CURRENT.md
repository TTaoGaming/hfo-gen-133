---
schema_id: hfo.gen133.x13.cots_connector_current.v1
experiment_id: X13_GOOGLE_CALENDAR_BOUNDED_EVENT_WINDOW_READONLY_001
version: 55
prior_version: 54
candidate: Google_Calendar_bounded_event_window_readonly_surface
candidate_contract_reference: official_Google_Calendar_events_list_quota_error_and_sync_contracts_plus_direct_connector_receipts
campaign_wake: 3_of_4
campaign_status: ACTIVE
phase_1_completed: true
phase_2_completed: true
phase_3_completed: true
phase_4_completed: false
phase_4_decision: null
carrier_task_id: 6a55c1733708819185088bf334e33ea5
carrier_task_id_match: true
wip: 1
last_event:
  commit: 365760ad009d33cf8a641c344e902169123cad0a
  path: state/coordination/experiments/cots_connector_x13/20260803T034626Z_GOOGLE_CALENDAR_EVENT_WINDOW_PHASE3_INVERTED_BOUNDS_SEMANTIC_EMPTY_ANDON.md
  blob_sha: b3f8a37862c3f4ba4bfd8846694c2aa9a3f90b91
  exact_readback_completed: true
prior_current_commit: 45b830bd3dcc518b1dd36518ddc108b5a0fc71c8
prior_current_blob_sha: a8d0b9f0412894a41cf55af45b3f57b68592bbd7
effect_ceiling: PHASE3_ONE_SYNTHETIC_INVERTED_BOUND_READ_ONLY_CALENDAR_PROBE_GIT_EVENT_CURRENT_ADVANCE_READBACK_AND_ONE_SHORT_SLACK_MEASURED_FACT
adoption_credit: 1
fitness_credit: 0_PENDING_SOURCE_BOUND_CONSUMER_ACK_AND_MEASURED_OPERATOR_OUTCOME
consumer_ack: NOT_OBSERVED
operator_minutes_removed_measured: 0
operator_minutes_removed_estimate_per_schedule_window_check: 1_to_4_UNVALIDATED
custom_code_avoided_estimate:
  authenticated_event_list_time_bounds_pagination_and_normalization: 45_to_140_LOC_UNVALIDATED
custom_policy_not_avoided:
  - STRICT_CLIENT_SIDE_TIME_BOUND_ORDER_VALIDATION
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
  total_queries: 3
  total_returned_events: 4
actual_upstream_request_count: UNKNOWN_AT_LEAST_2_SUCCESS_PATH_CALLS_AND_UP_TO_1_FAILURE_PROBE_CALL
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
phase_2_measured_facts:
  narrower_window_duration_hours: 6
  one_record_returned_at_requested_cap_1: true
  continuation_token_present: true
  additional_wrapper_visible_results_proven: true
  returned_event_overlapped_window_while_starting_before_lower_bound: true
  full_private_content_again_surfaced_by_default: true
  durable_log_minimization_applied: true
phase_3_measured_facts:
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
  - BOUNDED_READ_ONLY_PRIMARY_CALENDAR_EVENT_WINDOW_DISCOVERY
  - EXPLICIT_VALIDATED_RFC3339_BOUNDS_RESPONSE_TIMEZONE_AND_SMALL_PAGE_CAP
  - PRIVACY_MINIMIZED_COUNTS_TIME_BUCKETS_AND_SOURCE_BOUND_REFERENCES
  - CONTINUATION_TOKEN_PRESENCE_AS_PAGINATION_SIGNAL_WITHOUT_TOKEN_VALUE_PERSISTENCE
excluded_scope:
  - EVENT_CREATE_UPDATE_DELETE_MOVE_IMPORT_OR_QUICK_ADD
  - INVITATION_RESPONSE_ATTENDEE_CHANGE_EMAIL_OR_NOTIFICATION_EFFECT
  - DURABLE_FULL_CALENDAR_SNAPSHOT_OR_INCREMENTAL_SYNC
  - COMPLETENESS_IDENTITY_ACCESS_ROLE_SCOPE_WRITE_AUTHORITY_OR_BILLING_CLAIMS
  - UNNECESSARY_PERSISTENCE_OF_EVENT_TEXT_IDS_URLS_ATTENDEES_LOCATIONS_OR_TOKEN_VALUES
mandatory_gates:
  - VALIDATE_RFC3339_PARSEABILITY_AND_REQUIRE_TIME_MIN_STRICTLY_LESS_THAN_TIME_MAX_BEFORE_CONNECTOR_INVOCATION
  - CLASSIFY_INVALID_LOCAL_BOUNDS_SEPARATELY_FROM_VALID_EMPTY_WINDOW_NO_MATCH_PERMISSION_RATE_LIMIT_TRANSPORT_AND_PROVIDER_FAILURE
  - NEVER_TRANSLATE_AN_EMPTY_CONNECTOR_ARRAY_INTO_NO_CALENDAR_CONFLICT_UNLESS_BOUND_VALIDATION_PASSED
  - PRESERVE_EXACT_VALIDATED_BOUNDS_CALENDAR_ALIAS_AND_OBSERVATION_TIME_WITH_EACH_NEGATIVE_RESULT
  - USE_EXPLICIT_RFC3339_TIME_MIN_TIME_MAX_TIMEZONE_CALENDAR_ID_AND_SMALL_MAX_RESULTS
  - INTERPRET_TIME_MIN_AS_EXCLUSIVE_LOWER_BOUND_ON_EVENT_END_AND_TIME_MAX_AS_EXCLUSIVE_UPPER_BOUND_ON_EVENT_START
  - TREAT_OVERLAPPING_LONG_RUNNING_AND_ALL_DAY_EVENTS_AS_VALID_MATCHES
  - TREAT_MAX_RESULTS_AS_PAGE_CAP_NOT_TOTAL_MATCH_COUNT
  - TREAT_NEXT_PAGE_TOKEN_PRESENCE_AS_DIRECT_EVIDENCE_OF_MORE_WRAPPER_VISIBLE_RESULTS
  - MINIMIZE_EVENT_CONTENT_IN_MEMORY_BEFORE_GIT_SLACK_OR_DOWNSTREAM_FANOUT
  - DO_NOT_PERSIST_EVENT_IDS_TITLES_DESCRIPTIONS_URLS_ATTENDEES_LOCATIONS_OR_TOKEN_VALUES_UNLESS_REQUIRED_BY_AN_ADMITTED_CONSUMER
  - DO_NOT_INFER_IDENTITY_ACCESS_ROLE_SCOPE_WRITE_OR_NOTIFICATION_AUTHORITY_FROM_READ_SUCCESS
  - DO_NOT_CLAIM_SNAPSHOT_STABILITY_COMPLETENESS_OR_DURABILITY_FROM_ONE_QUERY_OR_ONE_PAGE
  - KEEP_ALL_MUTATING_AND_NOTIFICATION_CAPABILITIES_EXCLUDED
verifier: RAW_GOOGLE_CALENDAR_EVENTS_LIST_WITH_IDENTICAL_CALENDAR_TIME_MIN_TIME_MAX_TIMEZONE_MAX_RESULTS_AND_PAGE_CONTEXT_PLUS_CALENDAR_UI_FOR_VALID_WINDOWS
consumer:
  - HFO_EXECUTIVE_ASSISTANT_BOUNDED_DAY_PLAN_READS
  - HFO_DEADLINE_AND_CONFLICT_DETECTION_WITH_PRIVACY_MINIMIZATION
  - HFO_WAITING_CLOCK_AND_MORNING_PACKET_SOURCE_BOUND_OBSERVATIONS
strongest_falsifier: SAME_CONTEXT_RAW_EVENTS_LIST_WITH_IDENTICAL_INVERTED_BOUNDS_RETURNS_A_VISIBLE_4XX_INVALID_ARGUMENT_WHILE_THE_CONNECTOR_SURFACE_CONTINUES_TO_RETURN_EMPTY_SUCCESS_OR_A_VALIDATED_BOUND_CONSUMER_STILL_OBSERVES_FALSE_NEGATIVE_CONFLICT_RESULTS
honest_flaw: PHASE3_ESTABLISHES_CONNECTOR_SURFACE_SEMANTIC_AMBIGUITY_BUT_NOT_WHETHER_THE_WRAPPER_DROPPED_REWROTE_OR_FORWARDED_INVALID_BOUNDS_NO_RAW_API_OR_UI_COMPARISON_NO_VALID_EMPTY_WINDOW_NO_SCOPE_OR_ACCESS_ROLE_PROOF_NO_PERMISSION_RATE_LIMIT_OR_TRANSIENT_FAILURE_NO_CONSUMER_ACK_AND_ZERO_MEASURED_OPERATOR_MINUTES
phase_1_result:
  disposition: PHASE1_ACCEPTED_WITH_CONTENT_MINIMIZATION_PAGINATION_AND_TEMPORAL_SEMANTICS_GATES
phase_2_result:
  disposition: PHASE2_ACCEPTED_WITH_CAP_CURSOR_OVERLAP_AND_DATA_MINIMIZATION_GATES
phase_3_result:
  disposition: PHASE3_ACCEPTED_WITH_SEMANTIC_EMPTY_RESULT_ANDON_AND_CLIENT_SIDE_BOUND_VALIDATION_GATE
next_wake:
  experiment_id: X13_GOOGLE_CALENDAR_BOUNDED_EVENT_WINDOW_READONLY_001
  phase: 4_of_4
  proposed_action: DECISION_ONLY_WITH_NO_ADDITIONAL_CALENDAR_CAPABILITY_CALL
  provisional_decision: ADOPT_WITH_GATES
  excluded_effects: EVENT_CREATE_UPDATE_DELETE_INVITATION_RESPONSE_ATTENDEE_CHANGE_EMAIL_NOTIFICATION_TOKEN_PERSISTENCE_OR_ADDITIONAL_PROVIDER_CALL
review_expiry_utc: 2026-08-10T03:46:26Z
valid_time_utc: 2026-08-03T03:46:26Z
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

Google Calendar bounded event-window read-only phase **3/4** is accepted with a semantic empty-result Andon and strict client-side bound-validation gate.

A synthetic read-only probe supplied valid RFC3339 timestamps in an invalid order. The connector returned zero events, no continuation token, and no visible error in 195 ms. Google’s published Events.list contract requires `timeMin < timeMax` when both are set.

This does not prove the raw provider accepted the request. The wrapper may have dropped, rewritten, or intercepted parameters. It does prove that malformed bounds and a legitimate empty window are indistinguishable at this connector surface unless the caller validates bounds first.

Mandatory gate: parse both bounds locally, require strict increasing order, and preserve invalid-input, valid-empty, permission, rate-limit, transport, and provider-failure states separately. Never translate an empty array into “no calendar conflict” unless local bound validation passed.

Measured operator relief remains `0`; surfaced cost was `$0`; ConsumerAck, least-privilege proof, valid pagination, valid empty-window behavior, and independent raw/UI verification remain absent.

Next wake is phase 4 decision-only with no additional Calendar call. Provisional disposition: `ADOPT_WITH_GATES`.
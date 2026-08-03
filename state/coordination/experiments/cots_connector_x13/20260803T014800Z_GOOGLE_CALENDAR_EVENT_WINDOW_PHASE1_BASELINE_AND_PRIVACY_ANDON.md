---
schema_id: hfo.gen133.x13.cots_connector_event.v1
experiment_id: X13_GOOGLE_CALENDAR_BOUNDED_EVENT_WINDOW_READONLY_001
event_type: PHASE1_BASELINE_AND_ANDON
candidate: Google_Calendar_bounded_event_window_readonly_surface
carrier_task_id: 6a55c1733708819185088bf334e33ea5
carrier_task_id_match: true
wip: 1
expected_current_version: 52
next_current_version: 53
campaign_wake: 1_of_4
phase_1_disposition: PHASE1_ACCEPTED_WITH_CONTENT_MINIMIZATION_PAGINATION_AND_TEMPORAL_SEMANTICS_GATES
operator_minutes_removed_measured: 0
operator_minutes_removed_estimate_per_schedule_window_check: 1_to_4_UNVALIDATED
fitness_credit: 0_PENDING_SOURCE_BOUND_CONSUMER_ACK_AND_MEASURED_OPERATOR_OUTCOME
custom_code_avoided_estimate:
  authenticated_event_list_time_bounds_pagination_and_normalization: 45_to_140_LOC_UNVALIDATED
credentials:
  connector_reached_primary_calendar_without_error: true
  operator_supplied_credentials: 0
  authenticated_identity: UNKNOWN
  credential_type: UNKNOWN
  calendar_id_alias_used: primary
  effective_oauth_scope: UNKNOWN
  access_role: NOT_EXPOSED
  credential_custody: UNKNOWN
  least_privilege_verified: false
direct_phase_1_receipt:
  action: Google_Calendar.search_events
  calendar_id: primary
  time_min_utc: 2026-08-03T01:48:00Z
  time_max_utc: 2026-08-04T01:48:00Z
  requested_timezone: America/Denver
  requested_max_results: 3
  query_supplied: false
  returned_event_count: 3
  next_page_token_present: true
  connector_error: null
  external_call_time_ms: 468
  carrier_retries: 0
  mutation_or_notification_effect: false
  exact_event_ids_titles_descriptions_urls_and_token_promoted: false
returned_field_surface:
  event_ids_present: 3_of_3
  summaries_present: 3_of_3
  descriptions_present: 3_of_3
  start_and_end_present: 3_of_3
  direct_event_urls_present: 3_of_3
  recurrence_instance_metadata_present: 2_of_3
  response_status_field_present: true
  next_page_token_present: true
privacy_andon:
  triggered: true
  measured_fact: CONNECTOR_RETURNED_FULL_EVENT_SUMMARIES_DESCRIPTIONS_IDS_URLS_AND_TIMING_BY_DEFAULT_FOR_A_BOUNDED_LIST_CALL
  implication: RESULT_COUNT_ONLY_USE_REQUIRES_LOCAL_MINIMIZATION_BEFORE_GIT_SLACK_LOGGING_OR_DOWNSTREAM_FANOUT
  secret_or_exact_private_event_content_persisted: false
durability: EPHEMERAL_POINT_IN_TIME_WINDOW_QUERY_OVER_MUTABLE_CALENDAR_STATE_NOT_A_SNAPSHOT_OR_CHANGE_STREAM
observability: NORMALIZED_EVENT_FIELDS_COUNT_CURSOR_PRESENCE_AND_CONNECTOR_LATENCY_VISIBLE_RAW_HTTP_REQUEST_ID_RESPONSE_ETAG_ACCESS_ROLE_SYNC_TOKEN_QUOTA_HEADERS_UPSTREAM_RETRIES_AND_APPLIED_SINGLE_EVENTS_ORDERING_HIDDEN
portability: MEDIUM_RFC3339_TIME_WINDOWS_AND_EVENT_START_END_CONCEPTS_PORTABLE_GOOGLE_EVENT_IDS_RECURRENCE_FIELDS_PAGE_TOKENS_AND_PRIMARY_ALIAS_PROVIDER_SPECIFIC
failure_behavior:
  success_path: OBSERVED
  empty_window: NOT_TESTED
  invalid_time_bounds: NOT_TESTED
  invalid_page_token: NOT_TESTED
  permission_denial: NOT_TESTED
  authentication_failure: NOT_TESTED
  quota_or_rate_limit: NOT_TESTED
  transient_server_failure: NOT_TESTED
cost_and_quota:
  paid_cost_usd_observed: 0_NO_CHARGE_SURFACED
  candidate_connector_calls_this_phase: 1
  actual_upstream_request_count: UNKNOWN_AT_LEAST_1
  actual_quota_units_consumed: UNKNOWN
  live_project_quota_class: UNKNOWN
  billing_counters: NOT_EXPOSED
  official_post_2026_05_01_limits_if_applicable:
    requests_per_minute_per_project: 10000
    requests_per_minute_per_user_per_project: 600
    requests_per_day_per_project_before_charges: 1000000
  legacy_project_exception_possible: true
official_contract_checked_utc: 2026-08-03T01:48:00Z
official_sources:
  events_list: https://developers.google.com/workspace/calendar/api/v3/reference/events/list
  usage_limits: https://developers.google.com/workspace/calendar/api/guides/quota
  incremental_sync: https://developers.google.com/workspace/calendar/api/guides/sync
official_contract_facts:
  endpoint: GET_/calendar/v3/calendars/{calendarId}/events
  primary_keyword_addresses_logged_in_users_primary_calendar: true
  time_min_filters_on_event_end_exclusive: true
  time_max_filters_on_event_start_exclusive: true
  max_results_is_page_maximum_not_completeness_guarantee: true
  page_may_contain_fewer_than_max_results_even_when_more_matches_exist: true
  next_page_token_signals_more_results: true
  next_sync_token_is_only_on_final_page: true
  access_role_exists_in_raw_collection_response_but_was_not_exposed: true
  raw_list_can_use_readonly_or_broader_calendar_scopes: true
  expired_sync_token_returns_410_and_requires_full_resync: true
mandatory_gates:
  - USE_EXPLICIT_RFC3339_TIME_MIN_TIME_MAX_TIMEZONE_CALENDAR_ID_AND_SMALL_MAX_RESULTS
  - INTERPRET_TIME_MIN_AS_EXCLUSIVE_LOWER_BOUND_ON_EVENT_END_AND_TIME_MAX_AS_EXCLUSIVE_UPPER_BOUND_ON_EVENT_START
  - TREAT_OVERLAPPING_LONG_RUNNING_AND_ALL_DAY_EVENTS_AS_VALID_WINDOW_MATCHES
  - TREAT_MAX_RESULTS_AS_PAGE_CAP_NOT_TOTAL_MATCH_COUNT
  - TREAT_NEXT_PAGE_TOKEN_PRESENCE_AS_DIRECT_EVIDENCE_OF_MORE_WRAPPER_VISIBLE_RESULTS
  - NEVER_LOG_OR_FAN_OUT_EVENT_IDS_TITLES_DESCRIPTIONS_URLS_ATTENDEES_LOCATIONS_OR_TOKENS_UNLESS_THE_CONSUMER_REQUIRES_THEM
  - MINIMIZE_TO_COUNTS_TIME_BUCKETS_AND_SOURCE_BOUND_REFERENCES_BEFORE_GIT_OR_SLACK
  - DO_NOT_INFER_ACCOUNT_IDENTITY_ACCESS_ROLE_OAUTH_SCOPE_WRITE_AUTHORITY_OR_NOTIFICATION_AUTHORITY_FROM_READ_SUCCESS
  - DO_NOT_CLAIM_SNAPSHOT_STABILITY_COMPLETENESS_OR_INCREMENTAL_DURABILITY_FROM_ONE_WINDOW_QUERY
  - KEEP_EVENT_CREATE_UPDATE_DELETE_MOVE_IMPORT_QUICK_ADD_INVITATION_RESPONSE_ATTENDEE_EMAIL_AND_NOTIFICATION_EFFECTS_EXCLUDED
strongest_falsifier: SAME_CONTEXT_RAW_EVENTS_LIST_OR_CALENDAR_UI_SHOWS_CONNECTOR_OMITTED_OR_MISBOUND_EVENTS_WITHIN_THE_IDENTICAL_WINDOW_OR_CONNECTOR_NORMALIZED_TIMES_RECURRENCE_OR_PAGINATION_INCORRECTLY
verifier: RAW_GOOGLE_CALENDAR_EVENTS_LIST_WITH_IDENTICAL_CALENDAR_TIME_MIN_TIME_MAX_TIMEZONE_MAX_RESULTS_AND_PAGE_CONTEXT_PLUS_CALENDAR_UI
consumer:
  - HFO_EXECUTIVE_ASSISTANT_BOUNDED_DAY_PLAN_READS
  - HFO_DEADLINE_AND_CONFLICT_DETECTION_WITH_PRIVACY_MINIMIZATION
  - HFO_WAITING_CLOCK_AND_MORNING_PACKET_SOURCE_BOUND_OBSERVATIONS
honest_flaw: FULL_PRIVATE_EVENT_CONTENT_WAS_EXPOSED_TO_THE_CONNECTOR_RESPONSE_NO_RAW_API_OR_UI_COMPARISON_NO_SCOPE_OR_ACCESS_ROLE_PROOF_NO_EMPTY_OR_FAILURE_PROBE_NO_VALID_PAGINATION_READ_NO_SYNC_TOKEN_AND_ZERO_MEASURED_OPERATOR_MINUTES
next_wake:
  phase: 2_of_4
  proposed_action: REPEAT_A_NARROWER_BOUNDED_READ_ONLY_WINDOW_WITH_MAX_RESULTS_1_AND_PERSIST_ONLY_COUNT_CURSOR_PRESENCE_AND_FIELD_CLASSIFICATION
  excluded_effects: EVENT_CREATE_UPDATE_DELETE_INVITATION_RESPONSE_ATTENDEE_CHANGE_EMAIL_NOTIFICATION_OR_TOKEN_VALUE_PERSISTENCE
review_expiry_utc: 2026-08-10T01:48:00Z
valid_time_utc: 2026-08-03T01:48:00Z
transaction_time_utc: SEE_GIT_COMMIT_METADATA
sealed: true
---

# Phase 1 baseline — accepted with privacy and pagination gates

One bounded read-only query against the `primary` calendar returned three events and a continuation token. The connector performed no mutation and surfaced no call error.

The useful capability is direct: authenticated event-window discovery with explicit RFC3339 bounds, a calendar alias, a response timezone, a small page cap, normalized start/end values, and a continuation signal.

The measured Andon is also direct: the list call returned full event summaries, descriptions, identifiers, direct URLs, timing, and recurrence metadata by default. Exact private values were not copied into this event. Any count-only or availability consumer must minimize the connector response before durable logging or cross-system fan-out.

The raw Google contract defines `timeMin` as an exclusive lower bound on event end and `timeMax` as an exclusive upper bound on event start. Long-running and all-day events that overlap the window can therefore appear even when their displayed start date predates the requested lower bound. `maxResults` is only a page maximum; the observed continuation token is direct evidence that additional wrapper-visible results existed.

No outcome credit is earned. Operator minutes removed remain zero, credential identity and least-privilege scope are unknown, and no raw API or Calendar UI verification was completed.
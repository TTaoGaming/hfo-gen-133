---
schema_id: hfo.gen133.x13.cots_connector_event.v1
experiment_id: X13_GOOGLE_CALENDAR_BOUNDED_EVENT_WINDOW_READONLY_001
event_type: PHASE2_NARROW_BOUNDED_MICRO_USE
candidate: Google_Calendar_bounded_event_window_readonly_surface
carrier_task_id: 6a55c1733708819185088bf334e33ea5
carrier_task_id_match: true
wip: 1
expected_current_version: 53
next_current_version: 54
campaign_wake: 2_of_4
phase_2_disposition: PHASE2_ACCEPTED_WITH_CAP_CURSOR_OVERLAP_AND_DATA_MINIMIZATION_GATES
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
direct_phase_2_receipt:
  action: Google_Calendar.search_events
  calendar_id: primary
  time_min_utc: 2026-08-03T01:48:00Z
  time_max_utc: 2026-08-03T07:48:00Z
  requested_timezone: America/Denver
  requested_max_results: 1
  query_supplied: false
  returned_event_count: 1
  next_page_token_present: true
  connector_error: null
  external_call_time_ms: 466
  carrier_retries: 0
  mutation_or_notification_effect: false
  exact_event_ids_titles_descriptions_urls_and_token_promoted: false
returned_field_classes_observed:
  identifier: true
  summary_text: true
  description_text: true
  start_and_end: true
  direct_event_url: true
  location_field: true
  color_field: true
  response_status_field: true
  transparency_field: true
  recurrence_instance_fields: true
  attachment_field: true
  next_page_token: true
micro_use_measurements:
  narrower_window_duration_hours: 6
  result_cap_behavior: ONE_EVENT_RETURNED_AT_REQUESTED_MAX_RESULTS_1
  continuation_behavior: TOKEN_PRESENT_PROVING_ADDITIONAL_WRAPPER_VISIBLE_RESULTS
  overlap_semantics_reobserved: RETURNED_EVENT_STARTED_BEFORE_TIME_MIN_AND_ENDED_AFTER_TIME_MAX
  privacy_minimization_applied_before_durable_logging: true
  exact_private_values_persisted: false
privacy_andon:
  active: true
  measured_fact: FULL_PRIVATE_EVENT_TEXT_IDENTIFIERS_URLS_AND_TIMING_WERE_AGAIN_SURFACED_BY_DEFAULT_EVEN_FOR_A_COUNT_AND_CURSOR_MICRO_USE
  implication: MINIMIZE_IN_MEMORY_BEFORE_GIT_SLACK_OR_DOWNSTREAM_FANOUT
durability: EPHEMERAL_POINT_IN_TIME_WINDOW_QUERY_OVER_MUTABLE_CALENDAR_STATE_NOT_A_SNAPSHOT_SYNC_OR_EVENT_STREAM
observability: NORMALIZED_EVENT_FIELD_CLASSES_COUNT_CURSOR_PRESENCE_AND_CONNECTOR_LATENCY_VISIBLE_RAW_HTTP_REQUEST_ID_RESPONSE_ETAG_ACCESS_ROLE_SYNC_TOKEN_QUOTA_HEADERS_UPSTREAM_RETRIES_AND_ORDERING_HIDDEN
portability: MEDIUM_RFC3339_WINDOWS_AND_EVENT_START_END_CONCEPTS_PORTABLE_GOOGLE_PRIMARY_ALIAS_EVENT_FIELDS_AND_PAGE_TOKENS_PROVIDER_SPECIFIC
failure_behavior:
  success_path: OBSERVED_TWICE
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
  campaign_connector_calls_total: 2
  actual_upstream_request_count: UNKNOWN_AT_LEAST_2_ACROSS_CAMPAIGN
  actual_quota_units_consumed: UNKNOWN
  live_project_quota_class: UNKNOWN
  billing_counters: NOT_EXPOSED
  carrier_retries_total: 0
official_contract_inherited_from_phase_1:
  events_list: https://developers.google.com/workspace/calendar/api/v3/reference/events/list
  usage_limits: https://developers.google.com/workspace/calendar/api/guides/quota
  incremental_sync: https://developers.google.com/workspace/calendar/api/guides/sync
  time_min_filters_on_event_end_exclusive: true
  time_max_filters_on_event_start_exclusive: true
  max_results_is_page_maximum_not_total_count: true
  next_page_token_signals_more_results: true
mandatory_gates:
  - USE_EXPLICIT_RFC3339_TIME_MIN_TIME_MAX_TIMEZONE_CALENDAR_ID_AND_SMALL_MAX_RESULTS
  - INTERPRET_TIME_MIN_AS_EXCLUSIVE_LOWER_BOUND_ON_EVENT_END_AND_TIME_MAX_AS_EXCLUSIVE_UPPER_BOUND_ON_EVENT_START
  - TREAT_OVERLAPPING_LONG_RUNNING_AND_ALL_DAY_EVENTS_AS_VALID_WINDOW_MATCHES
  - TREAT_MAX_RESULTS_AS_PAGE_CAP_NOT_TOTAL_MATCH_COUNT
  - TREAT_NEXT_PAGE_TOKEN_PRESENCE_AS_DIRECT_EVIDENCE_OF_MORE_WRAPPER_VISIBLE_RESULTS
  - MINIMIZE_EVENT_CONTENT_IN_MEMORY_BEFORE_GIT_SLACK_OR_DOWNSTREAM_FANOUT
  - DO_NOT_PERSIST_EVENT_IDS_TITLES_DESCRIPTIONS_URLS_ATTENDEES_LOCATIONS_OR_TOKEN_VALUES_UNLESS_REQUIRED_BY_AN_ADMITTED_CONSUMER
  - DO_NOT_INFER_ACCOUNT_IDENTITY_ACCESS_ROLE_OAUTH_SCOPE_WRITE_AUTHORITY_OR_NOTIFICATION_AUTHORITY_FROM_READ_SUCCESS
  - DO_NOT_CLAIM_SNAPSHOT_STABILITY_COMPLETENESS_OR_INCREMENTAL_DURABILITY_FROM_ONE_PAGE
  - KEEP_EVENT_CREATE_UPDATE_DELETE_MOVE_IMPORT_QUICK_ADD_INVITATION_RESPONSE_ATTENDEE_EMAIL_AND_NOTIFICATION_EFFECTS_EXCLUDED
strongest_falsifier: SAME_CONTEXT_RAW_EVENTS_LIST_OR_CALENDAR_UI_SHOWS_CONNECTOR_OMITTED_OR_MISBOUND_EVENTS_OR_NORMALIZED_WINDOW_PAGINATION_OR_TIMES_INCORRECTLY
verifier: RAW_GOOGLE_CALENDAR_EVENTS_LIST_WITH_IDENTICAL_CALENDAR_TIME_MIN_TIME_MAX_TIMEZONE_MAX_RESULTS_AND_PAGE_CONTEXT_PLUS_CALENDAR_UI
consumer:
  - HFO_EXECUTIVE_ASSISTANT_BOUNDED_DAY_PLAN_READS
  - HFO_DEADLINE_AND_CONFLICT_DETECTION_WITH_PRIVACY_MINIMIZATION
  - HFO_WAITING_CLOCK_AND_MORNING_PACKET_SOURCE_BOUND_OBSERVATIONS
honest_flaw: PHASE2_CONFIRMS_BOUNDED_RESULT_AND_CURSOR_BEHAVIOR_BUT_STILL_EXPOSES_FULL_PRIVATE_CONTENT_NO_VALID_PAGE_TRAVERSAL_NO_RAW_OR_UI_COMPARISON_NO_SCOPE_OR_ACCESS_ROLE_PROOF_NO_FAILURE_PROBE_NO_CONSUMER_ACK_AND_ZERO_MEASURED_OPERATOR_MINUTES
prior_event:
  commit: 38c0d8cd1d7b0aa3df9ff58ae8a9e835aef2373d
  path: state/coordination/experiments/cots_connector_x13/20260803T014800Z_GOOGLE_CALENDAR_EVENT_WINDOW_PHASE1_BASELINE_AND_PRIVACY_ANDON.md
  blob_sha: 41b9cc3d3abffbccc2cfbca0c57a6e3cff129740
next_wake:
  phase: 3_of_4
  proposed_action: ONE_SYNTHETIC_INVERTED_TIME_BOUND_READ_ONLY_FAILURE_PROBE_WITH_MAX_RESULTS_1_NO_RETRY_AND_NO_TOKEN
  excluded_effects: EVENT_CREATE_UPDATE_DELETE_INVITATION_RESPONSE_ATTENDEE_CHANGE_EMAIL_NOTIFICATION_TOKEN_PERSISTENCE_OR_RETRY_LOOP
review_expiry_utc: 2026-08-10T02:49:31Z
valid_time_utc: 2026-08-03T02:49:31Z
transaction_time_utc: SEE_GIT_COMMIT_METADATA
sealed: true
---

# Phase 2 micro-use — accepted with cap, cursor, overlap, and privacy gates

One narrower six-hour read-only query against the `primary` calendar requested at most one result. The connector returned one event, a continuation token, no error, and no mutation or notification effect.

The useful behavior is directly measured: the wrapper respected the one-record cap for this observation, and the returned continuation token proves more wrapper-visible matches existed. The returned event overlapped the window while beginning before its lower bound, independently repeating the phase-one temporal-semantics finding.

The privacy Andon remains active. A count-and-cursor micro-use still caused the connector to return full event text, identifiers, direct URLs, and timing. Those exact values and the token were minimized before durable logging.

No outcome credit is earned. Operator minutes removed remain zero, identity and least-privilege scope remain unknown, no valid page traversal or failure path was exercised, and no raw API or Calendar UI comparison exists.
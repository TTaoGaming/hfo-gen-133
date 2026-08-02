---
schema_id: hfo.gen133.x13.cots_connector_current.v1
experiment_id: X13_GOOGLE_CALENDAR_FREEBUSY_READONLY_001
version: 38
prior_version: 37
candidate: Google_Calendar_freebusy_readonly_connector_surface
candidate_contract_reference: official_Google_Calendar_Freebusy_query_quota_and_error_contract_plus_direct_connector_receipts
campaign_wake: 2_of_4
campaign_status: IN_PROGRESS
phase_1_completed: true
phase_2_completed: true
phase_3_completed: false
phase_4_completed: false
phase_4_decision: PENDING
last_event:
  commit: 066c4c4d578d9e81a7265dd63857e6cc4bdf2e01
  path: state/coordination/experiments/cots_connector_x13/20260802T104907Z_GOOGLE_CALENDAR_FREEBUSY_PHASE2_MICRO_USE.md
  blob_sha: 483dda99b902039250f665ece3dbe89382d1fe97
  exact_readback_completed: true
prior_current_commit: 34a79d255b7134206189132592a88271e0cf9b92
prior_current_blob_sha: d17fea655627e76d18499da36bdb68ad5b006997
carrier_task_id: 6a55c1733708819185088bf334e33ea5
carrier_task_id_match: true
carrier_task_id_observation_source: AUTOMATION_RUN_CONTEXT
effect_ceiling: ONE_BOUNDED_READ_ONLY_NEAR_TERM_PRIMARY_FREEBUSY_QUERY_GIT_EVENT_CURRENT_ADVANCE_AND_ONE_SHORT_NON_SECRET_SLACK_MEASURED_FACT_RECEIPT_ONLY
adoption_credit: 2
adoption_credit_basis:
  - OFFICIAL_PRIMARY_FREEBUSY_CONTRACT_BASELINE
  - ONE_BOUNDED_EMPTY_RESULT_PRIMARY_QUERY
  - ONE_BOUNDED_NON_EMPTY_NEAR_TERM_PRIMARY_QUERY
  - STRUCTURAL_INTERVAL_BOUNDS_ORDER_OVERLAP_DURATION_AND_GAP_VALIDATION
  - NORMALIZED_CALENDAR_ID_BUSY_ARRAY_AND_PER_CALENDAR_ERROR_CAPTURE
  - NO_EVENT_CONTENT_RETURNED
  - NO_WRITE_SIDE_EFFECT
fitness_credit: 0_PENDING_EXPLICIT_SOURCE_BOUND_CONSUMER_ACK_AND_MEASURED_OPERATOR_OUTCOME
consumer_ack: NOT_OBSERVED
same_provider_binding_weight: 0
independent_verification_closed: false
operator_relay_minutes: 0
operator_minutes_removed_measured: 0
operator_minutes_removed_estimate_per_bounded_check: 1_to_5_UNVALIDATED
custom_code_avoided_estimate:
  authenticated_freebusy_request_rfc3339_timezone_validation_response_normalization_and_basic_per_calendar_error_handling: 40_to_120_LOC_UNVALIDATED
  interval_sort_overlap_bounds_duration_and_gap_validation: 20_to_60_LOC_UNVALIDATED
custom_policy_not_avoided:
  - CALENDAR_SELECTION_AND_AUTHORITY
  - DATA_CLASSIFICATION_AND_BUSY_PATTERN_REDACTION
  - SOURCE_BOUND_IDENTITY_AND_SCOPE_VERIFICATION
  - PARTIAL_RESPONSE_AND_PER_CALENDAR_ERROR_POLICY
  - TIMEZONE_DST_AND_INTERVAL_BOUNDARY_POLICY
  - RATE_LIMIT_RETRY_AND_IDEMPOTENCY_POLICY
  - INDEPENDENT_VERIFICATION
credentials:
  connector_authenticated_or_primary_calendar_reachable: true
  operator_supplied_credentials: 0
  live_identity: UNKNOWN
  live_token_type: UNKNOWN
  live_scopes: UNKNOWN
  oauth_client_or_project: UNKNOWN
  calendar_ownership_or_delegated_authority: UNKNOWN
  credential_custody: UNKNOWN
paid_cost_usd_observed: 0_NO_CHARGE_SURFACED
campaign_candidate_invocations:
  phase_1_primary_freebusy_query: 1
  phase_2_primary_freebusy_query: 1
actual_upstream_request_count: UNKNOWN
actual_quota_class: UNKNOWN
retry_count: 0_AT_CARRIER_LEVEL_UPSTREAM_UNKNOWN
billing_counters: NOT_EXPOSED
live_HTTP_status_headers_request_id_retry_after_or_rate_limit_headers: NOT_EXPOSED
direct_phase_1_receipt:
  calendar_id_alias: primary
  query_time_min_utc: 2026-08-02T10:00:00Z
  query_time_max_utc: 2026-08-02T11:00:00Z
  response_timezone: America/Denver
  busy_interval_count: 0
  per_calendar_errors: null
  top_level_error: null
  external_call_time_ms: 214
  event_content_returned: false
  write_side_effect: false
direct_phase_2_receipt:
  calendar_id_alias: primary
  query_time_min_utc: 2026-08-02T11:00:00Z
  query_time_max_utc: 2026-08-02T15:00:00Z
  response_timezone: America/Denver
  query_window_minutes: 240
  busy_interval_count: 2
  total_busy_minutes: 40
  total_free_minutes_by_subtraction: 200
  longest_contiguous_free_minutes: 120
  exact_busy_interval_timestamps_persisted: false
  exact_busy_interval_timestamps_omitted_reason: PRIVACY_MINIMIZATION
  intervals_start_before_end: true
  intervals_inside_query_window: true
  intervals_sorted_ascending: true
  intervals_non_overlapping: true
  per_calendar_errors: null
  top_level_error: null
  external_call_time_ms: 3301
  event_content_returned: false
  write_side_effect: false
official_contract_checked_2026_08_02:
  freebusy_query: https://developers.google.com/workspace/calendar/api/v3/reference/freebusy/query
  quota: https://developers.google.com/workspace/calendar/api/guides/quota
  errors: https://developers.google.com/workspace/calendar/api/guides/errors
  request_method: POST_/calendar/v3/freeBusy
  required_request_fields: RFC3339_timeMin_RFC3339_timeMax_items_ids
  response_timezone_default: UTC
  busy_start_semantics: INCLUSIVE
  busy_end_semantics: EXCLUSIVE
  calendar_expansion_max: 50
  group_expansion_max: 100
  acceptable_scopes_documented:
    - calendar.readonly
    - calendar
    - calendar.events.freebusy
    - calendar.freebusy
  official_default_per_minute_per_project: 10000_AS_OF_2026_05_01
  official_default_per_minute_per_user_per_project: 600_AS_OF_2026_05_01
  official_daily_project_threshold_before_planned_charges: 1000000_AS_OF_2026_05_01
  rate_limit_failures: HTTP_403_OR_429_USAGE_LIMITS
  recommended_rate_limit_response: TRUNCATED_EXPONENTIAL_BACKOFF
failure_semantics:
  bounded_primary_alias_empty_query: DIRECTLY_OBSERVED_SUCCESS
  bounded_primary_alias_non_empty_query: DIRECTLY_OBSERVED_SUCCESS
  inaccessible_calendar: NOT_TESTED
  invalid_calendar_id: NOT_TESTED
  malformed_or_inverted_window: NOT_TESTED
  partial_per_calendar_error: NOT_TESTED
  group_expansion: NOT_TESTED
  quota_403_or_429: NOT_TESTED
  transient_500: NOT_TESTED
  independent_cross_client_readback: NOT_TESTED
durability: EPHEMERAL_POINT_IN_TIME_QUERY_OVER_MUTABLE_CALENDAR_STATE_FREEBUSY_HAS_NO_PERSISTENT_RESOURCE
observability: MEDIUM_FOR_NORMALIZED_CALENDAR_ID_BUSY_INTERVALS_ERRORS_AND_CONNECTOR_TIMING_BUT_LOW_FOR_RAW_HTTP_HEADERS_REQUEST_ID_SCOPE_IDENTITY_RETRIES_QUOTA_PROJECT_AND_UPSTREAM_REQUEST_COUNT
portability: MEDIUM_BECAUSE_RFC3339_BUSY_INTERVALS_ARE_GENERIC_BUT_PRIMARY_ALIAS_CALENDAR_IDS_OAUTH_SCOPES_GROUP_EXPANSION_ERRORS_AND_QUOTAS_ARE_GOOGLE_SPECIFIC
admitted_scope:
  - BOUNDED_READ_ONLY_FREEBUSY_QUERY
  - PRIMARY_ALIAS_IN_CURRENT_AUTHENTICATED_CONTEXT
  - BUSY_INTERVAL_AND_PER_CALENDAR_ERROR_EXTRACTION
  - LOCAL_STRUCTURAL_VALIDATION_AND_AGGREGATION
  - NO_EVENT_CONTENT_DISCLOSURE
excluded_scope:
  - EVENT_CREATE_INVITE_RESPONSE_EDIT_OR_DELETE
  - EVENT_DETAIL_MINING
  - AUTOMATIC_SCHEDULING_OR_AUTHORITY_TO_BOOK_OVER_A_PERSON
  - IMMUTABLE_STATE_OR_HISTORICAL_AVAILABILITY_CLAIMS
  - LIVE_SCOPE_IDENTITY_QUOTA_OR_COST_CLAIMS
  - INDEPENDENT_COMPLETENESS_VERIFICATION
mandatory_gates:
  - USE_EXPLICIT_RFC3339_START_AND_END_WITH_Z_OR_OFFSET
  - RESPONSE_TIMEZONE_FORMATS_OUTPUT_ONLY_AND_DOES_NOT_REDEFINE_QUERY_INTERVAL
  - TREAT_PRIMARY_AS_AUTHENTICATED_CONTEXT_ALIAS_NOT_DURABLE_PORTABLE_ID
  - FREEBUSY_IS_OCCUPANCY_ONLY_NOT_EVENT_CONTENT_OR_SCHEDULING_AUTHORITY
  - PRESERVE_PER_CALENDAR_ERRORS_SEPARATELY_FROM_SUCCESSFUL_BUSY_INTERVALS
  - EMPTY_BUSY_ARRAY_PROVES_ONLY_THIS_CALL_RETURNED_NO_BUSY_BLOCK_FOR_THIS_INTERVAL_AND_ALIAS
  - DO_NOT_PERSIST_EXACT_BUSY_PATTERNS_UNLESS_NECESSARY_AND_APPROVED
  - SANITIZE_CALENDAR_IDS_EMAIL_LIKE_RESOURCE_IDS_AND_BUSY_PATTERNS_BEFORE_GIT_OR_SLACK_PERSISTENCE
  - DO_NOT_CLAIM_LIVE_SCOPE_IDENTITY_QUOTA_COST_COMPLETENESS_OR_INDEPENDENT_VERIFICATION
  - NO_EVENT_CREATE_INVITE_RESPONSE_EDIT_DELETE_OR_BROAD_CALENDAR_MINING
verifier: RAW_GOOGLE_CALENDAR_FREEBUSY_API_OR_DISTINCT_AUTHORIZED_CALENDAR_CLIENT_USING_SAME_EXPLICIT_INTERVAL_AND_SOURCE_BOUND_CALENDAR_ID_WITH_RAW_RESPONSE_AND_SCOPE_EVIDENCE
consumer:
  - HFO_SCHEDULING_AND_EXECUTIVE_ASSISTANT_PLANNING_LOGIC
  - PHASE_3_FAILURE_PERMISSION_PORTABILITY_PROBE
  - PHASE_4_DECISION
strongest_falsifier: A_DISTINCT_AUTHORIZED_CLIENT_RETURNS_DIFFERENT_BUSY_INTERVALS_OR_A_PER_CALENDAR_ERROR_FOR_THE_SAME_SOURCE_BOUND_CALENDAR_AND_EXACT_UTC_INTERVAL
honest_flaw: PHASE2_USED_PRIMARY_ALIAS_AND_ONE_NEAR_TERM_WINDOW_ONLY_AND_DID_NOT_VERIFY_ACCOUNT_IDENTITY_SCOPE_SECONDARY_OR_SHARED_CALENDARS_EVENT_TRANSPARENCY_ALL_DAY_OR_DST_SEMANTICS_PARTIAL_ERRORS_RATE_LIMITS_OR_INDEPENDENT_ACCURACY
next_phase:
  phase: 3_of_4
  status: PENDING
  planned_probe: ONE_PRIVACY_SAFE_READ_ONLY_INVALID_OR_INACCESSIBLE_CALENDAR_ID_PROBE_WITH_PER_CALENDAR_ERROR_CAPTURE_AND_NO_RETRY
review_expiry_utc: 2026-08-09T10:49:07Z
valid_time_utc: 2026-08-02T10:49:07Z
transaction_time_utc: SEE_GIT_COMMIT_METADATA
sealed: true
prior_campaign:
  experiment_id: X13_SLACK_NATIVE_MESSAGE_RECEIPT_001
  final_version: 36
  decision: ADOPT_WITH_GATES
  decision_event_commit: 449f9b38893b825a2d8c356cb3911876f187ac03
  current_commit: 58b9b552263129a640dbc6bfcde60ab3fca2496c
prior_prior_campaign:
  experiment_id: X13_GITHUB_CONTENTS_CONNECTOR_001
  final_version: 32
  decision: ADOPT_WITH_GATES
  decision_commit: 1c921066a994009f3ae76654cdec7a3fd8c1004c
---

# X13 current campaign

Google Calendar Freebusy read-only is at phase **2/4**.

One bounded near-term query against the authenticated `primary` alias returned two busy intervals. Privacy-minimized aggregation found 40 busy minutes and 200 free minutes in the 240-minute query window; returned intervals were ordered, non-overlapping, and within the requested bounds. Exact busy timestamps were not persisted.

No event content was returned and no calendar mutation occurred. Measured operator relief remains `0`; identity, OAuth scope, project, quota class, billing state, and independent accuracy remain unknown. Phase 3 is pending.

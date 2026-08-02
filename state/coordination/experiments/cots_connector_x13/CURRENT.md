---
schema_id: hfo.gen133.x13.cots_connector_current.v1
experiment_id: X13_GOOGLE_CALENDAR_FREEBUSY_READONLY_001
version: 39
prior_version: 38
candidate: Google_Calendar_freebusy_readonly_connector_surface
candidate_contract_reference: official_Google_Calendar_Freebusy_query_quota_and_error_contract_plus_direct_connector_receipts
campaign_wake: 3_of_4
campaign_status: IN_PROGRESS
phase_1_completed: true
phase_2_completed: true
phase_3_completed: true
phase_4_completed: false
phase_4_decision: PENDING
last_event:
  commit: abac05a466576125dc6ec44e49cf26539dd34c8f
  path: state/coordination/experiments/cots_connector_x13/20260802T114724Z_GOOGLE_CALENDAR_FREEBUSY_PHASE3_FAILURE_PERMISSION_PROBE.md
  blob_sha: a0552270d3397ae029f154ef6133e77ea72eaf54
  exact_readback_completed: true
prior_current_commit: 8aa7d6d98bbdbd9b1fee3a1358f1c7837d708f73
prior_current_blob_sha: be33646c4dab6c3c1e048a42a7e92f5ae4e200fb
carrier_task_id: 6a55c1733708819185088bf334e33ea5
carrier_task_id_match: true
carrier_task_id_observation_source: AUTOMATION_RUN_CONTEXT
effect_ceiling: ONE_PRIVACY_SAFE_READ_ONLY_SYNTHETIC_INVALID_CALENDAR_FREEBUSY_PROBE_GIT_EVENT_CURRENT_ADVANCE_AND_ONE_SHORT_NON_SECRET_SLACK_FACT_ONLY
adoption_credit: 3
adoption_credit_basis:
  - OFFICIAL_PRIMARY_FREEBUSY_CONTRACT_BASELINE
  - ONE_BOUNDED_EMPTY_RESULT_PRIMARY_QUERY
  - ONE_BOUNDED_NON_EMPTY_PRIMARY_QUERY_WITH_PRIVACY_MINIMIZED_AGGREGATION
  - STRUCTURAL_INTERVAL_VALIDATION
  - ONE_SYNTHETIC_INVALID_CALENDAR_PER_RESOURCE_ERROR_PROBE
  - NORMALIZED_BUSY_ARRAY_AND_PER_CALENDAR_ERROR_CAPTURE
  - NO_EVENT_CONTENT_RETURNED
  - NO_CALENDAR_WRITE_SIDE_EFFECT
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
  phase_3_synthetic_invalid_calendar_freebusy_query: 1
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
direct_phase_3_receipt:
  calendar_identifier_class: SYNTHETIC_RESERVED_INVALID_DOMAIN_EXACT_ID_NOT_PERSISTED
  query_window_minutes: 60
  response_timezone: America/Denver
  calendar_result_count: 1
  busy_interval_count: 0
  per_calendar_error_domain: global
  per_calendar_error_reason: notFound
  top_level_error: null
  external_call_time_ms: 2208
  retry_attempted: false
  event_content_returned: false
  write_side_effect: false
  interpretation: NOTFOUND_DOES_NOT_DISTINGUISH_NONEXISTENCE_FROM_NO_ACCESS
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
  freebusy_per_calendar_errors_documented: true
  documented_notFound_meaning: RESOURCE_NOT_FOUND_OR_CALLER_CANNOT_ACCESS
  additional_error_reasons_may_be_added: true
  rate_limit_failures: HTTP_403_OR_429_USAGE_LIMITS
  recommended_rate_limit_response: TRUNCATED_EXPONENTIAL_BACKOFF
failure_semantics:
  bounded_primary_alias_empty_query: DIRECTLY_OBSERVED_SUCCESS
  bounded_primary_alias_non_empty_query: DIRECTLY_OBSERVED_SUCCESS
  synthetic_invalid_calendar: DIRECTLY_OBSERVED_PER_CALENDAR_GLOBAL_NOTFOUND_WITH_TOP_LEVEL_SUCCESS
  inaccessible_real_calendar: NOT_TESTED_AND_NOT_DISTINGUISHABLE_FROM_NOTFOUND_BY_THIS_PROBE
  mixed_valid_and_invalid_calendars: NOT_TESTED
  malformed_or_inverted_window: NOT_TESTED
  group_expansion: NOT_TESTED
  quota_403_or_429: NOT_TESTED
  transient_500: NOT_TESTED
  independent_cross_client_readback: NOT_TESTED
durability: EPHEMERAL_POINT_IN_TIME_QUERY_OVER_MUTABLE_CALENDAR_STATE_FREEBUSY_HAS_NO_PERSISTENT_RESOURCE
observability: MEDIUM_FOR_NORMALIZED_CALENDAR_ID_BUSY_INTERVALS_AND_PER_CALENDAR_ERRORS_BUT_LOW_FOR_RAW_HTTP_HEADERS_REQUEST_ID_SCOPE_IDENTITY_RETRIES_QUOTA_PROJECT_AND_UPSTREAM_REQUEST_COUNT
portability: MEDIUM_FOR_GENERIC_RFC3339_FREEBUSY_AND_RESOURCE_SCOPED_ERRORS_BUT_MEDIUM_LOW_FOR_PRIMARY_ALIAS_GOOGLE_CALENDAR_IDS_OAUTH_SCOPES_ERROR_ENUMS_EXPANSION_LIMITS_AND_QUOTAS
admitted_scope:
  - BOUNDED_READ_ONLY_FREEBUSY_QUERY
  - PRIMARY_ALIAS_IN_CURRENT_AUTHENTICATED_CONTEXT
  - BUSY_INTERVAL_AND_PER_CALENDAR_ERROR_EXTRACTION
  - LOCAL_STRUCTURAL_VALIDATION_AND_PRIVACY_MINIMIZED_AGGREGATION
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
  - INSPECT_AND_PRESERVE_PER_CALENDAR_ERRORS_SEPARATELY_FROM_TOP_LEVEL_SUCCESS
  - TREAT_ANY_PER_CALENDAR_ERROR_AS_UNKNOWN_AVAILABILITY_NEVER_FREE_TIME
  - NOTFOUND_ALONE_DOES_NOT_PROVE_NONEXISTENCE_OR_PERMISSION_DENIAL
  - DO_NOT_BLINDLY_RETRY_DETERMINISTIC_NOTFOUND_WITHOUT_CORRECTED_IDENTITY_OR_ACCESS_EVIDENCE
  - GRACEFULLY_HANDLE_UNKNOWN_FUTURE_ERROR_REASONS
  - EMPTY_BUSY_ARRAY_PROVES_ONLY_THIS_CALL_RETURNED_NO_BUSY_BLOCK_FOR_THIS_INTERVAL_AND_ALIAS
  - DO_NOT_PERSIST_EXACT_BUSY_PATTERNS_UNLESS_NECESSARY_AND_APPROVED
  - SANITIZE_CALENDAR_IDS_EMAIL_LIKE_RESOURCE_IDS_AND_BUSY_PATTERNS_BEFORE_GIT_OR_SLACK_PERSISTENCE
  - DO_NOT_CLAIM_LIVE_SCOPE_IDENTITY_QUOTA_COST_COMPLETENESS_OR_INDEPENDENT_VERIFICATION
  - NO_EVENT_CREATE_INVITE_RESPONSE_EDIT_DELETE_OR_BROAD_CALENDAR_MINING
verifier: RAW_GOOGLE_CALENDAR_FREEBUSY_API_OR_DISTINCT_AUTHORIZED_CALENDAR_CLIENT_USING_SAME_EXPLICIT_INTERVAL_AND_SOURCE_BOUND_CALENDAR_ID_WITH_RAW_RESPONSE_AND_SCOPE_EVIDENCE
consumer:
  - HFO_SCHEDULING_AND_EXECUTIVE_ASSISTANT_PLANNING_LOGIC
  - PHASE_4_DECISION
strongest_falsifier: A_DISTINCT_AUTHORIZED_CLIENT_RETURNS_MATERIALLY_DIFFERENT_BUSY_OR_ERROR_RESULTS_FOR_THE_SAME_SOURCE_BOUND_CALENDAR_AND_INTERVAL_OR_THE_CONNECTOR_COLLAPSES_A_MIXED_SUCCESS_ERROR_QUERY_INTO_MISLEADING_GLOBAL_SUCCESS
honest_flaw: PHASE3_USED_A_SYNTHETIC_INVALID_ID_NOT_A_KNOWN_INACCESSIBLE_REAL_CALENDAR_AND_DID_NOT_TEST_MIXED_VALID_INVALID_CALENDARS_PRIVATE_OR_SHARED_CALENDARS_403_429_500_DST_OR_INDEPENDENT_READBACK
next_phase:
  phase: 4_of_4
  status: PENDING
  planned_action: DECISION_ONLY_NO_ADDITIONAL_CALENDAR_CALL_EXPECTED
  likely_disposition: ADOPT_WITH_GATES
review_expiry_utc: 2026-08-09T11:47:24Z
valid_time_utc: 2026-08-02T11:47:24Z
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

Google Calendar Freebusy read-only is at phase **3/4**.

A privacy-safe synthetic invalid-calendar query completed with no top-level connector error and one resource-scoped `global/notFound` error. No busy intervals, event details, or write effects were returned. Google documents that `notFound` can mean either a nonexistent resource or one the caller cannot access, so the result cannot classify the cause.

Callers must inspect each calendar's error field and treat errored calendars as unknown availability rather than free time. Measured operator relief remains `0`; live identity, authorization scope, project, quota, billing state, and independent accuracy remain unknown. Phase 4 is decision-only.

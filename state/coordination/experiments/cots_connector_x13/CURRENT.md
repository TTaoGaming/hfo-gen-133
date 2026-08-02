---
schema_id: hfo.gen133.x13.cots_connector_current.v1
experiment_id: X13_GOOGLE_CALENDAR_FREEBUSY_READONLY_001
version: 37
prior_version: 36
candidate: Google_Calendar_freebusy_readonly_connector_surface
candidate_contract_reference: official_Google_Calendar_Freebusy_query_quota_and_error_contract_plus_direct_connector_receipt
campaign_wake: 1_of_4
campaign_status: IN_PROGRESS
phase_1_completed: true
phase_2_completed: false
phase_3_completed: false
phase_4_completed: false
phase_4_decision: PENDING
last_event:
  commit: 3a0f163229a9c145373923ce369ccde39420985d
  path: state/coordination/experiments/cots_connector_x13/20260802T095011Z_GOOGLE_CALENDAR_FREEBUSY_PHASE1_BASELINE.md
  blob_sha: ea366c0b6657e3f166160996124f708dc90431ae
  exact_readback_completed: true
prior_current_commit: 58b9b552263129a640dbc6bfcde60ab3fca2496c
prior_current_blob_sha: 8b722103a66304feadbb4af8bd7110962bddf26d
carrier_task_id: 6a55c1733708819185088bf334e33ea5
carrier_task_id_match: true
carrier_task_id_observation_source: AUTOMATION_RUN_CONTEXT
effect_ceiling: OFFICIAL_CONTRACT_BASELINE_ONE_BOUNDED_READ_ONLY_PRIMARY_FREEBUSY_QUERY_GIT_EVENT_CURRENT_ADVANCE_AND_ONE_SHORT_NON_SECRET_SLACK_MEASURED_FACT_RECEIPT_ONLY
adoption_credit: 1
adoption_credit_basis:
  - OFFICIAL_PRIMARY_FREEBUSY_CONTRACT_BASELINE
  - ONE_BOUNDED_PRIMARY_CALENDAR_AVAILABILITY_QUERY
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
  event_titles_descriptions_attendees_locations_conference_data_or_event_ids_returned: false
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
  bounded_primary_alias_query: DIRECTLY_OBSERVED_SUCCESS
  empty_busy_array: DIRECTLY_OBSERVED
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
  - SANITIZE_CALENDAR_IDS_EMAIL_LIKE_RESOURCE_IDS_AND_BUSY_PATTERNS_BEFORE_GIT_OR_SLACK_PERSISTENCE
  - DO_NOT_CLAIM_LIVE_SCOPE_IDENTITY_QUOTA_COST_COMPLETENESS_OR_INDEPENDENT_VERIFICATION
  - NO_EVENT_CREATE_INVITE_RESPONSE_EDIT_DELETE_OR_BROAD_CALENDAR_MINING
verifier: RAW_GOOGLE_CALENDAR_FREEBUSY_API_OR_DISTINCT_AUTHORIZED_CALENDAR_CLIENT_USING_SAME_EXPLICIT_INTERVAL_AND_SOURCE_BOUND_CALENDAR_ID_WITH_RAW_RESPONSE_AND_SCOPE_EVIDENCE
consumer:
  - HFO_SCHEDULING_AND_EXECUTIVE_ASSISTANT_PLANNING_LOGIC
  - PHASE_2_MICRO_USE_AND_PHASE_4_DECISION
strongest_falsifier: A_DISTINCT_AUTHORIZED_CLIENT_RETURNS_A_BUSY_INTERVAL_OR_PER_CALENDAR_ERROR_FOR_THE_SAME_SOURCE_BOUND_CALENDAR_AND_EXACT_UTC_INTERVAL_THAT_THIS_CONNECTOR_OMITTED
honest_flaw: BASELINE_USED_ONLY_PRIMARY_ALIAS_AND_ONE_EMPTY_ONE_HOUR_INTERVAL_AND_DID_NOT_TEST_KNOWN_BUSY_SECONDARY_SHARED_INACCESSIBLE_PARTIAL_ERROR_DST_ALL_DAY_GROUP_EXPANSION_QUOTA_RETRY_OR_INDEPENDENT_READBACK
next_phase:
  phase: 2_of_4
  status: PENDING
  planned_micro_use: ONE_EXPLICITLY_BOUNDED_NEAR_TERM_PRIMARY_AVAILABILITY_WINDOW_WITH_MINIMUM_NECESSARY_STRUCTURAL_VALIDATION_AND_NO_MUTATION
review_expiry_utc: 2026-08-09T09:50:11Z
valid_time_utc: 2026-08-02T09:50:11Z
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

Google Calendar Freebusy read-only is at phase **1/4**.

One bounded query against the authenticated `primary` alias for `2026-08-02T10:00:00Z` through `2026-08-02T11:00:00Z` returned zero busy intervals and no per-calendar error in `214 ms`, with no event content and no write side effect.

This proves only the connector's normalized empty-result path for one alias and interval. It does not prove calendar completeness, live identity or scopes, quota class, independent accuracy, or authorization to schedule.

Measured operator relief remains `0`; fitness credit remains `0` pending a source-bound ConsumerAck. Phase 2 is pending and remains read-only.

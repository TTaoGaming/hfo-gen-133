---
schema_id: hfo.gen133.x13.cots_connector_event.v1
experiment_id: X13_GOOGLE_CALENDAR_GET_AVAILABILITY_READONLY_001
event_id: X13_GOOGLE_CALENDAR_GET_AVAILABILITY_PHASE4_ADOPT_WITH_GATES_20260805T044728Z
event_type: PHASE4_DECISION
phase: 4_of_4
phase_4_decision: ADOPT_WITH_GATES
disposition: ADOPT_WITH_GATES_BOUNDED_READONLY_HUMAN_REVIEWED_NONOPERATIONAL
campaign_status: CLOSED
carrier_task_id: 6a55c1733708819185088bf334e33ea5
carrier_task_id_match: true
wip: 1
canonical_repository: TTaoGaming/hfo-gen-133
canonical_branch: agent/gen133-bootstrap-20260730
prior_current_version: 103
candidate: Google_Calendar_get_availability_readonly_surface
effect_ceiling: BOUNDED_READONLY_HUMAN_REVIEWED_AVAILABILITY_CHECK
phase_4_additional_candidate_calls: 0
source_events:
  phase_1:
    path: state/coordination/experiments/cots_connector_x13/20260805T015129Z_GOOGLE_CALENDAR_GET_AVAILABILITY_PHASE1_BASELINE.md
    blob_sha: 0691791621bc5b2f8da697671c2ce0c9268b04ac
  phase_2:
    path: state/coordination/experiments/cots_connector_x13/20260805T024817Z_GOOGLE_CALENDAR_GET_AVAILABILITY_PHASE2_MICRO_USE.md
    blob_sha: a91667fa80ff95715f635bc544e6954194da4b8e
  phase_3:
    path: state/coordination/experiments/cots_connector_x13/20260805T034939Z_GOOGLE_CALENDAR_GET_AVAILABILITY_PHASE3_FAILURE_PROBE.md
    blob_sha: 3baab5fa387f59fe3f7e08bb7dbb960c9eaa0a52
campaign_measurements:
  readonly_calls: 3
  connector_level_successes: 3
  connector_level_failures: 0
  primary_busy_path_observed: true
  primary_free_path_observed: true
  mixed_partial_failure_path_observed: true
  required_calendar_notfound_class_errors_observed: 1
  busy_blocks_observed_total: 2
  aggregate_busy_minutes_observed_total: 150
  connector_latency_ms_total: 673
  retries: 0
  fallbacks: 0
  secondary_reads: 0
  candidate_mutations: 0
  exact_busy_intervals_retained: false
  event_titles_or_descriptions_returned: false
  operator_minutes_removed_measured: 0
  operator_minutes_removed_estimate: NOT_CLAIMED
  custom_code_avoided_estimate: 30_to_80_LOC_UNVALIDATED
credentials:
  operator_supplied_across_campaign: 0
  authenticated_principal: UNKNOWN
  effective_oauth_scope: UNKNOWN
  connector_managed: true
  least_privilege_proven: false
durability:
  provider_query_result: EPHEMERAL
  provider_resource: NO_PERSISTENT_FREEBUSY_RESOURCE
  durable_receipts: FOUR_IMMUTABLE_GIT_EVENTS_PLUS_VERSIONED_CURRENT
observability:
  exposed:
    - REQUESTED_CALENDAR_RESULT_KEYS
    - BUSY_INTERVAL_ARRAYS
    - PER_CALENDAR_ERROR_DOMAIN_AND_REASON
    - CONNECTOR_LATENCY
  not_exposed:
    - AUTHENTICATED_IDENTITY_AND_EFFECTIVE_SCOPE
    - RAW_HTTP_STATUS_HEADERS_AND_PROVIDER_REQUEST_ID
    - RAW_REQUEST_AND_RESPONSE_BYTES_OR_DIGEST
    - QUOTA_DEBIT_AND_REMAINING_LIMITS
    - UPSTREAM_ATTEMPT_AND_HIDDEN_RETRY_COUNT
    - CONNECTOR_TO_RAW_PROVIDER_PARITY
portability:
  freebusy_semantics: MEDIUM
  rfc3339_interval_semantics: HIGH
  calendar_identifiers_and_error_domain_reason: GOOGLE_SPECIFIC
  normalized_connector_shape: CONNECTOR_SPECIFIC
failure_behavior:
  observed: TOP_LEVEL_SUCCESS_WITH_VALID_PRIMARY_DATA_AND_PER_CALENDAR_GLOBAL_NOTFOUND_ERROR_FOR_SYNTHETIC_CALENDAR
  admitted: PARTIAL_SUCCESS_REQUIRES_PER_CALENDAR_INSPECTION
  not_admitted: REAL_EXISTING_CALENDAR_PERMISSION_DENIAL_RATE_LIMIT_TRANSIENT_ERROR_OR_HIDDEN_RETRY_BEHAVIOR
direct_cost_and_quota_evidence:
  paid_cost_usd_observed: 0_NO_CHARGE_SURFACED
  actual_quota_consumed: UNKNOWN
  provider_billing_or_quota_receipt: ABSENT
  official_contract_url: https://developers.google.com/workspace/calendar/api/v3/reference/freebusy/query
  official_quota_url: https://developers.google.com/workspace/calendar/api/guides/quota
  official_docs_verified_utc: 2026-08-05T04:47:28Z
  published_updated_model_limits: 10000_REQUESTS_PER_MINUTE_PER_PROJECT_600_PER_MINUTE_PER_USER_PER_PROJECT_1000000_REQUESTS_PER_DAY_PER_PROJECT_BEFORE_PLANNED_LATER_2026_CHARGES
  published_limit_caveat: PROJECTS_ACTIVE_BETWEEN_2025_11_AND_2026_04_MAY_RETAIN_PREVIOUSLY_SET_QUOTAS
verifier:
  required: DISTINCT_AUTHORIZED_SAME_PRINCIPAL_RAW_GOOGLE_CALENDAR_FREEBUSY_WITNESS_OVER_THE_SAME_CALENDAR_SET_AND_BOUNDS_WITH_SAFE_REQUEST_RESPONSE_DIGEST_HTTP_STATUS_REQUEST_ID_SCOPE_AND_QUOTA_FIELDS
  assigned: false
  completed: false
  result: NOT_RUN
consumer:
  named_catalog_consumer: HFO_COTS_CAPABILITY_INVENTORY
  operational_consumer: NOT_ASSIGNED
  consumer_ack: NOT_OBSERVED
  adoption_credit: 0
  fitness_credit: 0
strongest_falsifier: SAME_PRINCIPAL_RAW_FREEBUSY_QUERY_DISAGREES_ON_BUSY_FREE_OR_PER_CALENDAR_ERROR_RESULTS_FOR_THE_SAME_INPUTS_OR_SHOWS_THE_CONNECTOR_OMITTED_A_REQUIRED_CALENDAR_FAILURE
mandatory_gates:
  - USE_EXPLICIT_RFC3339_BOUNDS_AND_THE_SMALLEST_NECESSARY_CALENDAR_SET
  - TREAT_BUSY_WINDOWS_AND_CALENDAR_IDENTIFIERS_AS SENSITIVE_SCHEDULE_DATA
  - INSPECT_EVERY_REQUESTED_CALENDAR_RESULT_AND_ERRORS_ARRAY
  - FAIL_CLOSED_IF_ANY_CALENDAR_REQUIRED_FOR_THE_DECISION_IS_MISSING_OR_HAS_ANY ERROR
  - NEVER_TREAT_TOP_LEVEL_SUCCESS_AS_ALL_CALENDARS_SUCCESS
  - NEVER_TREAT_AN_EMPTY_BUSY_ARRAY_AS AUTHORITATIVE_AVAILABILITY_WHEN_ANY_REQUIRED_CALENDAR_FAILED_OR_WAS_NOT_QUERIED
  - HANDLE_UNKNOWN_FUTURE_ERROR_REASONS_CONSERVATIVELY
  - RETAIN_AGGREGATES_ONLY_UNLESS_A_NAMED_CONSUMER_REQUIRES_EXACT_INTERVALS
  - KEEP_USE_HUMAN_REVIEWED_AND_NONOPERATIONAL
  - REQUIRE_SAME_PRINCIPAL_RAW_PARITY_IDENTITY_SCOPE_QUOTA_CONSUMER_ACK_AND_MEASURED_OPERATOR_VALUE_BEFORE_UNATTENDED_SCHEDULING_OR_OPERATIONAL_CREDIT
adopted_boundary:
  allowed:
    - BOUNDED_READONLY_HUMAN_REVIEWED_AVAILABILITY_DISCOVERY
    - LOW_ASSURANCE_CATALOG_AND_OPERATOR_ASSISTANCE
  forbidden:
    - UNATTENDED_EVENT_CREATION_OR_RESCHEDULING
    - AUTHORITATIVE_ORGANIZATION_WIDE_AVAILABILITY_CLAIMS
    - ABSENCE_OR_FREE_TIME_CLAIMS_WHEN_ANY_REQUIRED_CALENDAR_FAILED_OR_WAS_OMITTED
    - SECRET_OR_EXACT_INTERVAL_PERSISTENCE_WITHOUT_NAMED_CONSUMER_NEED
    - AUTOMATIC_RETRY_OR_FALLBACK_WITHOUT_CLASSIFIED_TRANSIENT_FAILURE_AND_BOUNDED_POLICY
    - OPERATIONAL_ADOPTION_OR_FITNESS_CREDIT
honest_flaw: THE_CAMPAIGN USED_ONLY_PRIMARY_PLUS_ONE_SYNTHETIC_NONEXISTENT_CALENDAR_OVER_THREE_SHORT_WINDOWS; IDENTITY_SCOPE_RAW_PROVIDER_PARITY_REAL_PERMISSION_DENIAL_MULTIPLE_REAL_CALENDARS_TIMEZONE_DST_RATE_LIMITS_TRANSIENT_FAILURES_HIDDEN_RETRIES_ACTUAL_QUOTA_CONSUMPTION_OPERATOR_TIME_SAVED_AND_CONSUMER_VALUE_REMAIN_UNVERIFIED
next_campaign:
  candidate: Google_Drive_bounded_readonly_search_metadata_surface
  experiment_id: X13_GOOGLE_DRIVE_SEARCH_READONLY_002
  next_phase: 1_of_4
  action_this_wake: NONE
review_expiry_utc: 2026-08-12T04:47:28Z
valid_time_utc: 2026-08-05T04:47:28Z
recorded_time_utc: 2026-08-05T04:47:28Z
---

# X13 Google Calendar availability phase 4 decision

Decision: `ADOPT_WITH_GATES` for bounded, read-only, human-reviewed availability discovery only. Across three calls the connector exposed busy, free, and mixed partial-failure paths without returning event titles or descriptions. The material failure mode is that a top-level success can contain valid data for one calendar and a per-calendar error for another, so every requested calendar result must be inspected and required-calendar failures must stop the decision.

The connector avoided direct OAuth handling, request construction, response parsing, and per-calendar error normalization, estimated at 30-80 lines of custom code, but the estimate is unvalidated. It removed zero measured operator minutes and has no raw-provider witness, identity or scope proof, quota receipt, operational consumer acknowledgment, or measured value. No operational or fitness credit is awarded.

---
schema_id: hfo.gen133.x13.cots_connector_event.v1
experiment_id: X13_GOOGLE_CALENDAR_GET_AVAILABILITY_READONLY_001
event_type: PHASE3_FAILURE_PERMISSION_PORTABILITY_AND_CONNECTOR_VARIANCE_PROBE
phase: 3_of_4
phase_status: PHASE3_ACCEPTED_WITH_GATES
candidate: Google_Calendar_get_availability_readonly_surface
carrier_task_id: 6a55c1733708819185088bf334e33ea5
carrier_task_id_match: true
wip: 1
canonical_repository: TTaoGaming/hfo-gen-133
canonical_branch: agent/gen133-bootstrap-20260730
expected_current_version: 102
calendar_set: primary_plus_one_synthetic_inaccessible_calendar
calendar_count_requested: 2
query_window_minutes: 30
exact_query_bounds_retained: false
synthetic_calendar_id_retained: false
calendar_results_returned: 2
primary_busy_blocks_returned: 1
primary_aggregate_busy_minutes_observed: 30
primary_per_calendar_errors: 0
synthetic_busy_blocks_returned: 0
synthetic_per_calendar_errors: 1
synthetic_error_domain: global
synthetic_error_reason: notFound
connector_error: false
partial_success: true
event_titles_or_details_returned: false
connector_latency_ms: 178
retries: 0
fallbacks: 0
secondary_reads: 0
mutations: 0
paid_cost_usd_observed: 0_NO_CHARGE_SURFACED
actual_quota_consumed: UNKNOWN
operator_minutes_removed_measured: 0
custom_code_avoided_estimate: 30_to_80_LOC_UNVALIDATED
credentials: CONNECTOR_MANAGED_IDENTITY_AND_EFFECTIVE_SCOPE_UNKNOWN
durability: PROVIDER_QUERY_EPHEMERAL_IMMUTABLE_GIT_EVENT_AND_VERSIONED_CURRENT
observability: PARTIAL_CALENDAR_ID_BUSY_ARRAY_PER_CALENDAR_ERROR_DOMAIN_REASON_AND_CONNECTOR_LATENCY_EXPOSED_NO_HTTP_STATUS_HEADERS_REQUEST_ID_PRINCIPAL_SCOPE_QUOTA_OR_HIDDEN_ATTEMPT_COUNT
portability: MEDIUM_FREEBUSY_AND_PARTIAL_RESULTS_ARE_COMMON_BUT_CALENDAR_IDS_RFC3339_AND_GOOGLE_ERROR_DOMAIN_REASON_ARE_PROVIDER_SPECIFIC
failure_behavior: TOP_LEVEL_SUCCESS_WITH_MIXED_PER_CALENDAR_RESULTS_PRIMARY_DATA_RETURNED_ALONGSIDE_SYNTHETIC_NOTFOUND_ERROR
verifier: NOT_ASSIGNED
verifier_result: NOT_RUN
independent_verification_closed: false
consumer: NOT_ASSIGNED
consumer_ack: NOT_OBSERVED
adoption_credit: 0
fitness_credit: 0
allowed_use: PHASE3_OBSERVATION_ONLY_BOUNDED_READONLY_AGGREGATED_FREEBUSY_DISCOVERY
mandatory_gate: INSPECT_EVERY_REQUESTED_CALENDAR_RESULT_AND_ERRORS_FAIL_CLOSED_FOR_ANY_REQUIRED_CALENDAR_ERROR_NEVER_TREAT_TOP_LEVEL_SUCCESS_AS_ALL_CALENDARS_SUCCESS_HANDLE_UNKNOWN_ERROR_REASONS_AND_REQUIRE_RAW_SCOPE_QUOTA_CONSUMER_AND_VALUE_WITNESSES_BEFORE_UNATTENDED_USE
strongest_falsifier: SAME_PRINCIPAL_RAW_FREEBUSY_QUERY_OVER_THE_SAME_CALENDAR_SET_AND_WINDOW_DOES_NOT_RETURN_PRIMARY_BUSY_DATA_PLUS_A_NOTFOUND_CLASS_ERROR_FOR_THE_SYNTHETIC_CALENDAR
honest_flaw: THIS_PROBE_USED_A_SYNTHETIC_NONEXISTENT_CALENDAR_AND_OBSERVED_NOTFOUND_NOT_A_REAL_PERMISSION_DENIAL; IDENTITY_SCOPE_RAW_PROVIDER_PARITY_INACCESSIBLE_EXISTING_CALENDAR_BEHAVIOR_TIMEZONE_DST_RATE_LIMITS_TRANSIENT_FAILURES_UNKNOWN_ERROR_REASONS_HIDDEN_RETRIES_ACTUAL_QUOTA_CONSUMPTION_OPERATOR_TIME_SAVED_AND_CONSUMER_VALUE_REMAIN_UNVERIFIED
measured_fact: CONNECTOR_RETURNED_TOP_LEVEL_SUCCESS_WITH_VALID_PRIMARY_BUSY_DATA_AND_ONE_PER_CALENDAR_GLOBAL_NOTFOUND_ERROR_FOR_A_SYNTHETIC_CALENDAR_IN_THE_SAME_BOUNDED_READONLY_QUERY
official_contract_source: https://developers.google.com/workspace/calendar/api/v3/reference/freebusy/query
official_contract_observation: FREEBUSY_QUERY_SUPPORTS_PER_CALENDAR_ERRORS_INCLUDING_NOTFOUND_AND_CLIENTS_MUST_GRACEFULLY_HANDLE_ADDITIONAL_ERROR_STATUSES
next_phase: PHASE4_ADOPTION_DECISION
next_probe: DECISION_ONLY_NO_ADDITIONAL_GOOGLE_CALENDAR_CALL
provisional_decision: ADOPT_WITH_GATES_FOR_BOUNDED_HUMAN_REVIEWED_AVAILABILITY_CHECKS_ONLY
valid_time_utc: 2026-08-05T03:49:39Z
recorded_time_utc: 2026-08-05T03:49:39Z
---

# X13 Google Calendar availability — Phase 3

One bounded read-only `get_availability` call queried `primary` plus one synthetic inaccessible calendar over a 30-minute interval. The connector returned a top-level success containing two calendar results: the primary calendar had one busy block covering the full interval and no per-calendar error, while the synthetic calendar had no busy blocks and one `global/notFound` per-calendar error. No event titles or descriptions were returned. Connector latency was 178 ms.

No retry, fallback, secondary read, write, or mutation occurred. Exact query bounds, busy timestamps, and the synthetic calendar identifier were not persisted; only aggregate duration, result counts, error classification, and latency were retained.

## Measured failure behavior

The surface permits partial success: `error: null` at the connector level does not mean every requested calendar succeeded. A consumer must inspect each requested calendar's `errors` field and fail closed when any required calendar is missing or inaccessible.

Google's official `freeBusy.query` contract documents optional per-calendar errors, including `notFound`, and warns that additional error reasons may be added. This connector preserved the documented `domain` and `reason` fields for the synthetic failure.

## Admission boundary

The admitted claim is limited to: `CONNECTOR_RETURNED_MIXED_PER_CALENDAR_RESULTS_WITH_PRIMARY_BUSY_DATA_AND_ONE_NOTFOUND_ERROR_UNDER_TOP_LEVEL_SUCCESS`.

This does not verify a real permission denial, authenticated identity, effective OAuth scope, raw-provider parity, rate-limit or transient-error behavior, hidden retries, actual quota debit, or fitness for unattended scheduling.

## Decision posture

Phase 3 is accepted with gates. Adoption and fitness credit remain zero. Phase 4 should make a decision without another Calendar call. Provisional disposition is `ADOPT_WITH_GATES` for bounded, read-only, human-reviewed availability checks only.

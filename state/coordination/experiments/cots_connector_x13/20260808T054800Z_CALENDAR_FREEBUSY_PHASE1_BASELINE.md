---
schema_id: hfo.gen133.x13.cots_connector_event.v1
experiment_id: X13_GCAL_FREEBUSY_READONLY_020
expected_current_version: 176
candidate: Google_Calendar_get_availability_busy_only
campaign_wake: 1_of_4
phase: 1_OFFICIAL_CONTRACT_AND_DIRECT_CAPABILITY_BASELINE
status: PHASE1_ACCEPTED_WITH_GATES
wip: 1
candidate_calls_this_wake: 1
candidate_calls_total: 1
mutations_total: 0
retries_total: 0
fallbacks_total: 0
calendar_ids_count: 1
calendar_selector: primary
query_window_hours: 24
response_timezone: America/Denver
busy_interval_count_observed: 1
calendar_errors_observed: 0
connector_error_observed: false
connector_external_call_time_ms: 164
event_titles_or_details_hydrated: false
raw_busy_ranges_persisted_in_receipt: false
request_descriptor_canonicalization: UTF8_JSON_SORTED_KEYS_COMPACT_SEPARATORS_NO_ASCII_ESCAPING
request_descriptor_sha256: 1fddc99c0245bf117d720954a5c6e535c9f3dce3484ae28619a07b0d96bf863a
busy_result_digest_sha256: d5eca3697e1412a1fdd92698a427ef1c7df6dddfa79f703b88b4f2f7b53b3a6a
busy_result_digest_canonicalization: UTF8_JSON_SORTED_KEYS_COMPACT_OVER_ORDERED_BUSY_START_END_RANGES
operator_minutes_removed_measured: 0
custom_code_avoided_estimate: 80_to_200_LOC_UNVALIDATED
paid_cost_usd_observed: 0_NO_CHARGE_SURFACED_NOT_BILLING_PROOF
direct_cost_or_quota_evidence: NONE_FROM_CONNECTOR;OFFICIAL_CALENDAR_API_CURRENT_2026_08_08_DOCUMENTS_10000_REQUESTS_PER_MINUTE_PER_PROJECT_600_PER_MINUTE_PER_USER_PER_PROJECT_AND_1000000_REQUESTS_PER_DAY_PER_PROJECT_BEFORE_PLANNED_FUTURE_CHARGES;ACTUAL_CONNECTOR_PROJECT_NATIVE_MAPPING_AND_DEBIT_UNKNOWN
credentials: CONNECTOR_MANAGED_EFFECTIVE_PRINCIPAL_TOKEN_TYPE_AND_OAUTH_SCOPES_UNKNOWN;OFFICIAL_FREEBUSY_QUERY_ACCEPTS_CALENDAR_READONLY_CALENDAR_CALENDAR_EVENTS_FREEBUSY_OR_CALENDAR_FREEBUSY_SCOPES
durability: GIT_EVENT_AND_CURRENT_RECEIPTS_DURABLE_AFTER_WRITE;FREEBUSY_RESPONSE_IS_A_LIVE_QUERY_VIEW_NOT_A_SNAPSHOT
observability: BUSY_RANGES_AND_PER_CALENDAR_ERRORS_VISIBLE;CONNECTOR_EXTERNAL_CALL_TIME_VISIBLE;PROVIDER_REQUEST_ID_HTTP_STATUS_RATE_HEADERS_EFFECTIVE_SCOPE_NATIVE_METHOD_AND_ACTUAL_QUOTA_DEBIT_NOT_SURFACED
portability: MEDIUM_FREEBUSY_INTERVAL_MODEL_IS_GENERIC_AND_RFC3339_BASED;GOOGLE_CALENDAR_IDS_SCOPE_SEMANTICS_AND_QUOTAS_PROVIDER_SPECIFIC
failure_behavior: ONE_BOUNDED_READONLY_CALL_SUCCEEDED_WITH_BUSY_ONLY_RESPONSE_AND_NO_OBSERVED_ERROR;NO_PERMISSION_DENIAL_INACCESSIBLE_CALENDAR_RATE_LIMIT_TRANSIENT_OR_NATIVE_PARITY_TESTED
verifier: DIRECT_GOOGLE_CALENDAR_CONNECTOR_RECEIPT_PLUS_OFFICIAL_GOOGLE_CALENDAR_FREEBUSY_V3_CONTRACT_AND_CURRENT_QUOTA_DOCS_PLUS_GITHUB_IMMUTABLE_EVENT_AND_CURRENT_READBACK
consumer: HFO_COMMAND_AND_CONTROL_SCHEDULING_CANDIDATE_NO_DOWNSTREAM_CONSUMER_ACK
adoption_credit: 0
fitness_credit: 0
strongest_falsifier: A_MATCHED_PROVIDER_DIRECT_FREEBUSY_QUERY_UNDER_THE_SAME_EFFECTIVE_PRINCIPAL_AND_EQUIVALENT_INTERVAL_MATERIALLY_DISAGREES_ON_BUSY_RANGES_UNDER_QUIESCENT_CALENDAR_STATE_OR_THE_CONNECTOR_HYDRATES_EVENT_TITLES_DETAILS_DESPITE_BUSY_ONLY_CONTRACT
honest_flaw: ONE_SUCCESSFUL_CALL_ONLY;NO_PERMISSION_FAILURE_INACCESSIBLE_CALENDAR_EMPTY_BUSY_SET_MULTI_CALENDAR_PARTIAL_ERROR_RATE_LIMIT_TRANSIENT_FAILURE_NATIVE_PARITY_EFFECTIVE_SCOPE_ACTUAL_QUOTA_DEBIT_OPERATOR_SAVINGS_OR_DOWNSTREAM_CONSUMER_VALUE_TESTED
mandatory_gate: READONLY_BUSY_ONLY_AVAILABILITY;EXPLICIT_BOUNDED_RFC3339_TIME_MIN_AND_TIME_MAX;SMALL_EXPLICIT_CALENDAR_ID_SET;DO_NOT_PERSIST_RAW_BUSY_RANGES_OR_CALENDAR_EMAIL_IDS_IN_X13_RECEIPTS;NO_EVENT_DETAIL_FETCH;DO_NOT_TREAT_BUSY_AS_EVENT_IDENTITY_REASON_OR_ATTENDEE_EVIDENCE;DO_NOT_TREAT_SUCCESS_AS_AUTHORIZATION_COMPLETENESS;NO_UNBOUNDED_RETRY;PROVIDER_OR_PER_CALENDAR_ERRORS_FAIL_CLOSED_FOR_CONSEQUENTIAL_SCHEDULING
next_phase: PHASE2_EXACT_BOUNDED_REPLAY_COMPARE_BUSY_RESULT_DIGEST_WITH_NO_EVENT_FETCH_OR_MUTATION
valid_time_utc: 2026-08-08T05:48:00Z
recorded_time_utc: 2026-08-08T05:48:00Z
---

# X13 Google Calendar FreeBusy Phase 1

## Measured baseline

One bounded `Google_Calendar.get_availability` call over exactly one `primary` calendar and a 24-hour RFC3339 window succeeded. The connector returned busy intervals only; one busy interval was observed, with no event title, description, attendee, organizer, or event identifier hydrated. No connector error, retry, fallback, Calendar mutation, send, or content/event-detail fetch occurred. Connector external-call time was 164 ms.

The exact privacy-safe request descriptor is durable for an identical Phase-2 replay. Raw busy start/end ranges are deliberately omitted from this Git receipt; only their ordered canonical digest is stored.

## Official contract baseline

Google Calendar API v3 documents `POST /calendar/v3/freeBusy` as returning free/busy information for a set of calendars. The request uses RFC3339 `timeMin`/`timeMax`, optional response `timeZone`, and calendar/group IDs; native `calendarExpansionMax` is at most 50. The response exposes per-calendar `busy[]` ranges plus optional per-calendar errors. Official scopes accepted by the native method include `calendar.readonly`, `calendar`, `calendar.events.freebusy`, and `calendar.freebusy`.

Current Google Calendar quota documentation (last updated 2026-07-31) states 10,000 requests/minute/project, 600 requests/minute/user/project, and a 1,000,000-request/day/project threshold before planned future charges; standard use is currently documented as available at no additional cost. The connector did not expose its effective Cloud project, native provider method, actual quota debit, principal, token type, or OAuth scopes, so these are contract bounds rather than connector billing proof.

## Gates and variance

This is a least-data scheduling primitive compared with event search because it exposes occupancy windows rather than event metadata. However, a busy interval says only that Calendar considers that range busy under the effective principal; it does not identify the event, reason, attendee, organizer, or authorization completeness. Provider-native mapping remains unverified even though the wrapper semantics align with the official FreeBusy contract.

## Phase-1 decision

`PHASE1_ACCEPTED_WITH_GATES`. Continue to Phase 2 only with the identical durable request, no event hydration, and no Calendar mutation. Short-interval replay may test connector repeatability but cannot prove snapshot durability or future availability stability.

---
schema_id: hfo.gen133.x13.cots_connector_event.v1
experiment_id: X13_GOOGLE_CALENDAR_EVENT_SEARCH_READONLY_028
candidate: Google_Calendar.search_events_readonly
phase: 1
phase_status: PHASE1_ACCEPTED_WITH_GATES_ANDON
wip: 1
expected_current_version: 208
preflight_commit: 9bd43814ed486583e4c47cc648a9b8d54e406bb9
preflight_blob_sha: 88516bc093d2ef5b5c957bfbc4b863dd7006ff21
preflight_readback: true
request_sha256: 9f53e69c34059f00164e5f9f28a2b2488ec976ffaec270526da4c38d61ef56c9
request_sha256_verified_from_readback: true
candidate_invocations_this_wake: 1
result_count: 5
next_page_token_present: true
ordered_event_id_sha256: 84959cc9a6e8d247c67a89be2882264457fb2978eab8060898ea82b893aec776
connector_error: false
retries_observed: 0
fallbacks_observed: 0
candidate_mutations: 0
external_call_time_ms: 448
body_fields_hydrated: summary,location,color_id,start,end,url,description,my_response_status,transparency,attachments,recurring_event_id,original_start_time,display_url,display_title
sensitive_event_text_returned: true
raw_event_content_persisted_in_x13_receipt: false
raw_event_ids_persisted_in_x13_receipt: false
pagination_token_persisted_in_x13_receipt: false
operator_minutes_removed_measured: 0
custom_code_avoided_estimate: 40_to_120_LOC_UNVALIDATED
custom_code_avoided_realized_by_this_candidate: 0
paid_cost_usd_observed: 0_NO_CHARGE_SURFACED_NOT_BILLING_PROOF
direct_cost_or_quota_evidence: CONNECTOR_EXPOSED_NO_QUOTA_DEBIT_RATE_LIMIT_HEADERS_REQUEST_ID_OR_BILLING_METADATA;OFFICIAL_GOOGLE_CALENDAR_DOCS_STATE_10000_REQUESTS_PER_MINUTE_PER_PROJECT_600_PER_MINUTE_PER_USER_PER_PROJECT_1000000_REQUESTS_PER_DAY_PER_PROJECT_BEFORE_FUTURE_CHARGES_AND_STANDARD_USE_NO_ADDITIONAL_COST_AS_OF_2026_05_01
credentials: CONNECTOR_MANAGED;USABLE_READ_ACCESS_PROVEN_FOR_PRIMARY_CALENDAR_BOUNDED_WINDOW;EFFECTIVE_OAUTH_SCOPE_PRINCIPAL_AND_TOKEN_TYPE_NOT_EXPOSED
durability: GIT_PHASE1_PREFLIGHT_AND_RESULT_EVENTS_READ_BACK_ON_CANONICAL_BRANCH;CURRENT_UPDATE_PENDING_AFTER_RESULT_READBACK
observability: RESULT_COUNT_NEXT_PAGE_TOKEN_PRESENCE_ORDERED_ID_DIGEST_AND_WRAPPER_TIMING_AVAILABLE;EVENT_SUMMARY_DESCRIPTION_AND_URL_FIELDS_HYDRATED;NO_NATIVE_HTTP_STATUS_REQUEST_ID_RATE_HEADERS_SCOPE_PRINCIPAL_OR_QUOTA_DEBIT_EXPOSED
portability: MEDIUM_HIGH;CONNECTOR_PARAMETERS_MAP_CLOSELY_TO_OFFICIAL_EVENTS_LIST_CALENDAR_ID_MAX_RESULTS_TIME_MIN_TIME_MAX_TIME_ZONE_AND_PAGE_TOKEN_BUT_WRAPPER_FIELD_SELECTION_AND_ORDERING_BEHAVIOR_ARE_NOT_EXPLICIT
failure_behavior: NOT_PROBED_IN_PHASE1
verifier: DIRECT_GOOGLE_CALENDAR_CONNECTOR_RECEIPT_PLUS_GIT_PREFLIGHT_READBACK_PLUS_OFFICIAL_GOOGLE_CALENDAR_EVENTS_LIST_AND_USAGE_LIMITS_DOCUMENTATION
consumer: HFO_BOUNDED_CALENDAR_INTAKE_FOR_OPERATOR_CONTROL_LOOPS
mandatory_gate: READ_ONLY;PRIMARY_CALENDAR_ONLY_FOR_THIS_CAMPAIGN;EXPLICIT_TIME_WINDOW;MAX_RESULTS_5;ASSUME_FULL_EVENT_TEXT_MAY_BE_HYDRATED;DO_NOT_PERSIST_EVENT_TITLES_DESCRIPTIONS_LOCATIONS_URLS_IDS_OR_PAGE_TOKENS_IN_X13_RECEIPTS;DO_NOT_INFER_COMPLETENESS_WHEN_NEXT_PAGE_TOKEN_PRESENT;NO_SCOPE_PRINCIPAL_RATE_LIMIT_OR_QUOTA_ASSUMPTIONS
strongest_falsifier: A_DOWNSTREAM_CONSUMER_REQUIRES_METADATA_ONLY_OR_FREEBUSY_ONLY_DISCLOSURE_AUTHORITATIVE_COMPLETE_WINDOW_RESULTS_EXPLICIT_SCOPE_PRINCIPAL_ACCOUNTABILITY_OR_RATE_LIMIT_TELEMETRY
honest_flaw: THE_READ_ONLY_SEARCH_RETURNED_FULL_EVENT_SUMMARY_AND_DESCRIPTION_TEXT_PLUS_URLS_AND_OTHER_FIELDS;CONNECTOR_HAS_NO_FIELDS_SELECTOR_ON_THIS SURFACE;ONLY_ONE_BOUNDED_SUCCESS_EXISTS;COMPLETENESS_ORDERING_VALID_PAGINATION_FAILURE_PERMISSION_AND_RATE_LIMIT_BEHAVIOR_REMAIN_UNVERIFIED
official_contract_source_events_list: https://developers.google.com/workspace/calendar/api/v3/reference/events/list
official_contract_source_quota: https://developers.google.com/workspace/calendar/api/guides/quota
official_docs_last_updated_events_list_utc: 2026-05-12
official_docs_last_updated_quota_utc: 2026-05-01
valid_time_utc: 2026-08-09T13:53:00Z
recorded_time_utc: 2026-08-09T13:53:00Z
---

# X13 Google Calendar event search Phase 1 result

## Direct capability baseline

One bounded read-only `Google_Calendar.search_events` call against `primary` over the exact seven-day window returned five events and a next-page token in 448 ms. There were no observed connector errors, retries, fallbacks, or calendar mutations.

The connector is directly usable for bounded event intake, but the result is not complete because a next-page token was present. X13 persisted only the count, token presence, timing, and an ordered event-ID digest; it did not persist raw event IDs, page token, titles, descriptions, locations, URLs, attendee-like data, or conferencing data.

## Data-minimization Andon

The connector hydrated event `summary`, `description`, URL/display URL, and other event fields on this bounded search. Its exposed `search_events` contract has no field-selection parameter. Treat this as a full-event-detail surface for privacy purposes even though the call is read-only.

## Official baseline

Google's official Calendar `events.list` method is `GET /calendar/v3/calendars/{calendarId}/events`; it supports `maxResults`, `pageToken`, `q`, `timeMin`, `timeMax`, and `timeZone`, and returns full Event resources. Google documents that `timeMin` is an exclusive lower bound on an event's end time and `timeMax` is an exclusive upper bound on an event's start time. A non-empty `nextPageToken` means another page exists and the same request should be repeated with that token.

As of Google's May 1, 2026 usage-limits update, the default Calendar API quotas are 10,000 requests/minute/project and 600 requests/minute/user/project, with a 1,000,000 requests/day/project threshold before planned future charges; standard use is currently available at no additional cost. This is official service context only: the connector exposed no actual quota debit, rate-limit headers, Cloud project, request ID, billing metadata, OAuth scope, or principal identity for this call.

## Phase-1 disposition

`PHASE1_ACCEPTED_WITH_GATES_ANDON`. Continue to Phase 2 only as an exact bounded replay. Compare result count, next-page-token presence, and ordered-ID digest while allowing legitimate calendar drift. Do not hydrate a second page in Phase 2.

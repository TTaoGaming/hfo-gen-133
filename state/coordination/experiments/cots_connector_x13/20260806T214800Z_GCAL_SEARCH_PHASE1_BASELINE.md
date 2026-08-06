---
schema_id: hfo.gen133.x13.cots_connector_event.v1
experiment_id: X13_GCAL_SEARCH_READONLY_012
carrier_task_id: 6a55c1733708819185088bf334e33ea5
carrier_task_id_match: true
wip: 1
candidate: Google_Calendar_search_events_readonly_surface
campaign_wake: 1_of_4
phase: 1
status: PHASE1_ACCEPTED_WITH_GATES
prior_current_version: 144
expected_current_version: 145
request_sha256: 89d960dcb78b9e6432edf4759159d7a0cd55ed45e96d5bed7b3aeb3f4e9515aa
normalized_result_sha256: fb685ca05c2267ab8a52e42ba8b38882a5185bc20e37b8257d8a686e3674a0df
calendar_id: primary
query: HFO
time_min: 2026-07-30T00:00:00Z
time_max: 2026-08-14T00:00:00Z
timezone_str: America/Denver
max_results: 3
returned_events: 3
next_page_token_exposed: false
connector_error: null
external_call_time_ms: 246
retries: 0
fallbacks: 0
candidate_mutations: 0
content_hydration_observed: true
raw_event_content_persisted: false
measured_fact: ONE_BOUNDED_READONLY_SEARCH_RETURNED_3_EVENTS_WITH_NO_ERROR_IN_246MS
andon: SEARCH_RESPONSE_INCLUDED_FULL_DESCRIPTION_FIELDS_SO_TREAT_SEARCH_AS_CONTENT_HYDRATING_NOT_METADATA_ONLY
custom_code_avoided_estimate: 60_to_180_LOC_UNVALIDATED
operator_minutes_removed_measured: 0
credentials: CONNECTOR_MANAGED_EFFECTIVE_IDENTITY_AND_SCOPES_UNKNOWN
durability: GIT_EVENT_DURABLE_CALENDAR_SOURCE_MUTABLE
observability: RESULT_COUNT_PAGE_TOKEN_ERROR_AND_EXTERNAL_CALL_TIME_EXPOSED_PROVIDER_REQUEST_ID_ETAG_SYNCTOKEN_AND_ACTUAL_QUOTA_DEBIT_NOT_EXPOSED
portability: LOW_TO_MEDIUM_GOOGLE_CALENDAR_AND_WRAPPER_SPECIFIC
failure_behavior: ONE_NONEMPTY_SUCCESS_ONLY_OTHER_FAILURE_MODES_UNTESTED
paid_cost_usd_observed: 0_NO_CHARGE_SURFACED
direct_cost_or_quota_evidence: NONE_FROM_CONNECTOR
nominal_provider_quota_contract: CALENDAR_API_10000_REQ_PER_MIN_PROJECT_600_REQ_PER_MIN_USER_PROJECT_1M_REQ_PER_DAY_THRESHOLD_AND_CALENDAR_MCP_SEARCH_EVENTS_COST_1_MAPPING_UNVERIFIED
catalog_consumer: HFO_COTS_CAPABILITY_INVENTORY
operational_consumer: NOT_ASSIGNED
consumer_ack: NOT_OBSERVED
verifier: IDENTICAL_BOUNDED_REPLAY_THEN_MATCHED_PROVIDER_CALL
verifier_result: NOT_RUN
adoption_credit: 0
fitness_credit: 0
provisional_decision: ADOPT_WITH_GATES_CATALOG_ONLY
mandatory_gate: EXPLICIT_TIME_BOUNDS_SMALL_CAP_SEARCH_IS_CONTENT_HYDRATING_DO_NOT_PERSIST_EVENT_CONTENT_MAX_RESULTS_IS_NOT_COMPLETENESS_NO_UNBOUNDED_RETRY
strongest_falsifier: IDENTICAL_REPLAY_OR_MATCHED_PROVIDER_CALL_RETURNS_MATERIALLY_DIFFERENT_SCOPE_ORDER_PAGINATION_OR_AUTHORIZATION
honest_flaw: ONE_KNOWN_TOKEN_SEARCH_DID_NOT_TEST_EMPTY_DENIAL_OTHER_CALENDARS_PAGINATION_RATE_LIMIT_TRANSIENT_FAILURE_PROVIDER_PARITY_MEASURED_TIME_SAVINGS_OR_OPERATIONAL_CONSUMER_VALUE
next_phase: PHASE2_IDENTICAL_BOUNDED_REPLAY_WITH_DIGEST_COMPARISON
valid_time_utc: 2026-08-06T21:48:00Z
recorded_time_utc: 2026-08-06T21:48:00Z
---

# X13 Google Calendar search phase 1

A single bounded read-only `search_events` call on the primary calendar used query `HFO`, explicit RFC3339 bounds, timezone `America/Denver`, and `max_results=3`. It returned three events, no next-page token, no connector error, and `external_call_time_ms=246`.

No raw event IDs, titles, URLs, descriptions, attendees, or other returned event bodies are persisted. The ordered result digest uses only event ID, start, end, and recurring-event ID in memory.

Andon: the search response included full event description text even though the connector contract says to use `read_event` for full information. Treat this surface as content-hydrating, not metadata-only.

Official references: Google Calendar `events.list` documents broad free-text `q`, exclusive `timeMin`/`timeMax` bounds, `maxResults` as a page cap, and `nextPageToken` pagination. Google Calendar usage limits updated 2026-07-31 document 10,000 requests/minute/project, 600 requests/minute/user/project, a 1,000,000-request/day threshold, and Calendar MCP `search_events` query cost 1. Connector mapping and actual debit are not exposed.

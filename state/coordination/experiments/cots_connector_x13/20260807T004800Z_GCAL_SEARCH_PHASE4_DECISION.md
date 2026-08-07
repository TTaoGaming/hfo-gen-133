---
schema_id: hfo.gen133.x13.cots_connector_event.v1
experiment_id: X13_GCAL_SEARCH_READONLY_012
event_type: PHASE4_DECISION
phase: 4_of_4
candidate: Google_Calendar_search_events_readonly_surface
carrier_task_id: 6a55c1733708819185088bf334e33ea5
carrier_task_id_match: true
wip: 1
expected_current_version: 147
new_current_version: 148
candidate_calls_this_phase: 0
campaign_calls_total: 3
successful_nonempty_calls: 2
successful_empty_calls: 1
connector_errors_observed: 0
retries_total: 0
fallbacks_total: 0
candidate_mutations_total: 0
phase_1_phase_2_request_digest_match: true
phase_1_phase_2_ordered_result_digest_match: true
phase_3_empty_success_observed: true
content_hydration_observed: true_ON_MATCHING_CALLS
custom_code_avoided_estimate: 60_to_180_LOC_UNVALIDATED
operator_minutes_removed_measured: 0
credentials: CONNECTOR_MANAGED_EFFECTIVE_IDENTITY_AND_SCOPES_UNKNOWN
durability: GIT_EVENT_DURABLE_CALENDAR_SOURCE_AND_SEARCH_VIEW_MUTABLE_NO_PROVIDER_SNAPSHOT_ETAG_OR_SYNCTOKEN_RECEIPT
observability: RESULT_COUNT_EVENT_FIELDS_PAGE_TOKEN_ERROR_AND_EXTERNAL_CALL_TIME_EXPOSED; PROVIDER_REQUEST_ID_ACCESSROLE_ETAG_SYNCTOKEN_EFFECTIVE_SCOPE_AND_ACTUAL_QUOTA_DEBIT_NOT_EXPOSED
portability: LOW_TO_MEDIUM_GOOGLE_CALENDAR_AND_WRAPPER_SPECIFIC
failure_behavior: EMPTY_SUCCESS_DISTINGUISHED_FROM_CONNECTOR_ERROR; PERMISSION_DENIAL_RATE_LIMIT_TRANSIENT_OTHER_CALENDAR_PAGINATION_AND_PERMISSION_VARIANCE_UNTESTED
paid_cost_usd_observed: 0_NO_CHARGE_SURFACED
direct_cost_or_quota_evidence: NONE_FROM_CONNECTOR
catalog_consumer: HFO_COTS_CAPABILITY_INVENTORY
operational_consumer: NOT_ASSIGNED
consumer_ack: NOT_OBSERVED
verifier: TWO_IDENTICAL_MATCHING_REPLAY_DIGESTS_PLUS_ONE_SYNTHETIC_EMPTY_SUCCESS_RECEIPT_PLUS_CURRENT_V147_READBACK; MATCHED_RAW_PROVIDER_CALL_NOT_RUN
strongest_falsifier: MATCHED_RAW_CALENDAR_V3_EVENTS_LIST_CALL_UNDER_SAME_EFFECTIVE_PRINCIPAL_RETURNS_MATERIALLY_DIFFERENT_SCOPE_ORDER_PAGINATION_CONTENT_AUTHORIZATION_OR_EMPTY_RESULT_SEMANTICS_OR_A REAL_CONSUMER_TRIAL_FAILS_TO_SAVE_OPERATOR_TIME
honest_flaw: THREE_SMALL_PRIMARY_CALENDAR_CALLS_DO_NOT_TEST_PERMISSION_DENIAL_OTHER_CALENDARS_PAGINATION_RATE_LIMIT_TRANSIENT_FAILURE_INDEX_LAG_RAW_PROVIDER_PARITY_MEASURED_TIME_SAVINGS_OR_OPERATIONAL_CONSUMER_VALUE; MATCHING SEARCH HYDRATED FULL EVENT DESCRIPTIONS
phase_4_decision: DEFER
operational_decision: DEFER_OPERATIONAL_ADOPTION_CATALOG_ONLY
adoption_credit: 0
fitness_credit: 0
mandatory_gate: EXPLICIT_TIME_BOUNDS; SMALL_RESULT_CAP; SEARCH_IS_CONTENT_HYDRATING_NOT_METADATA_ONLY; DO_NOT_PERSIST_EVENT_CONTENT; EMPTY_SUCCESS_MEANS ZERO_VISIBLE_MATCHES_RETURNED NOT AUTHORITATIVE_ABSENCE; MAX_RESULTS_IS A CAP NOT COMPLETENESS; CONSEQUENTIAL CLAIMS REQUIRE DIRECT_EVENT_READ_OR_MATCHED_PROVIDER_WITNESS; NO_UNBOUNDED_RETRY
decision_basis: NARROW_REPEATABILITY_AND_EMPTY_SUCCESS_SHAPE_ARE_ESTABLISHED_BUT_PRIVACY_SURFACE_IS_LARGER_THAN_DISCOVERY_LABEL_IMPLIES_AND_NO_MEASURED_OPERATOR_SAVINGS_OPERATIONAL_CONSUMER_EFFECTIVE_AUTHORIZATION_RAW_PROVIDER_PARITY_OR_DIRECT_QUOTA_DEBIT_ARE_ESTABLISHED
next_campaign_candidate: Gmail_readonly_search_or_list_surface
next_phase: PHASE1_OFFICIAL_CONTRACT_AND_BOUNDED_DIRECT_BASELINE
valid_time_utc: 2026-08-07T00:48:00Z
recorded_time_utc: 2026-08-07T00:48:00Z
---

# X13 Google Calendar read-only search — Phase 4 decision

Decision: **DEFER** operational adoption. Retain only as a bounded, human-reviewed catalog/discovery capability with explicit gates.

## Evidence carried forward

Across three bounded read-only primary-calendar searches, two matching calls returned three events each and produced identical request and ordered normalized-result digests. One synthetic nonmatching call returned zero events, a null next-page token, and no connector error. No retries, fallbacks, Calendar mutations, paid charges surfaced by the connector, measured operator-minute savings, or operational-consumer acknowledgments were observed.

Matching searches hydrated full event descriptions. That makes the search surface materially broader than metadata-only discovery and raises the privacy/exposure cost of routine use.

## Decision rationale

The connector is useful for small, bounded discovery, but the campaign did not establish completeness, effective identity/scopes, other-calendar behavior, pagination behavior, raw-provider parity, permission-denial semantics, throttling/transient-failure behavior, index freshness, actual quota debit, or measurable operator savings. Those gaps prevent operational adoption credit.

The adopt-before-invent conclusion is therefore not to build a replacement search layer. Use the native connector only when a bounded human-reviewed lookup is sufficient; defer any workflow that depends on authoritative absence, completeness, or durable Calendar state until a direct-event or matched-provider witness exists.

## Mandatory gates

- Explicit time bounds and small result caps.
- Treat search as content-hydrating, not metadata-only.
- Do not persist returned event bodies unless explicitly required by an approved consumer.
- Empty success means only zero visible matches returned by that call.
- `maxResults`/wrapper caps are not completeness evidence.
- Consequential scheduling claims require direct-event read or matched provider evidence.
- No unbounded retry.

## Scorecard

- Custom code avoided: 60–180 LOC estimated, unvalidated.
- Operator minutes removed: 0 measured.
- Credentials: connector-managed; effective identity/scopes unknown.
- Durability: Git receipt durable; Calendar/search state mutable.
- Observability: wrapper result/page/error/timing visible; provider request ID, access role, ETag, sync token, effective scope, and actual quota debit absent.
- Portability: low-to-medium; Google Calendar and wrapper specific.
- Failure behavior: empty success distinguished from connector failure; denial/rate-limit/transient/pagination/other-calendar variance untested.
- Direct cost/quota evidence: none from connector; surfaced paid cost $0.
- Verifier: two replay-matched digests plus one empty-success receipt and CURRENT v147 readback.
- Strongest falsifier: a matched raw Calendar v3 call under the same effective principal materially disagrees, or a real consumer trial fails to save operator time.
- Honest flaw: only three small primary-calendar calls were tested, and matching search hydrated full descriptions.

No additional Calendar candidate call was made in phase 4.

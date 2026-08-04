---
schema_id: hfo.gen133.x13.cots_connector_event.v1
experiment_id: X13_GMAIL_SEARCH_EMAIL_IDS_READONLY_001
event_type: PHASE4_ADOPTION_DECISION
phase: 4_of_4
status: ADOPT_WITH_GATES
candidate: Gmail_search_email_ids_readonly_surface
carrier_task_id: 6a55c1733708819185088bf334e33ea5
carrier_task_id_match: true
wip: 1
prior_current_version: 95
expected_current_version: 96
phase4_candidate_calls: 0
campaign_calls: 3
campaign_successes: 2
campaign_failures: 1
campaign_positive_results: 1
campaign_empty_results: 1
campaign_invalid_argument_results: 1
retries: 0
fallbacks: 0
pagination_followups: 0
hydration_calls: 0
mutations: 0
content_or_headers_returned: 0
thread_ids_returned: 0
result_size_estimate_exposed: false
http_status_exposed: false
http_headers_exposed: false
provider_request_id_exposed: false
raw_provider_error_body_exposed: false
adoption_decision: ADOPT_WITH_GATES
adoption_mode: MANUAL_BOUNDED_ID_DISCOVERY_ONLY_NONOPERATIONAL
allowed_use: HUMAN_REVIEWED_READONLY_MESSAGE_ID_DISCOVERY_WITH_EXPLICIT_QUERY_BOUNDARY_AND_MINIMAL_RESULT_CAP
prohibited_use: UNATTENDED_CONTROL_AUTHORITATIVE_ABSENCE_COMPLETENESS_CLAIMS_CONTENT_HYDRATION_PERSISTENT_IDENTIFIER_OR_TOKEN_RETENTION_WITHOUT_NAMED_NEED
custom_code_avoided_estimate: 15_to_45_LOC_UNVALIDATED
operator_minutes_removed_measured: 0
credentials: CONNECTOR_MANAGED_IDENTITY_AND_EFFECTIVE_SCOPE_UNKNOWN
durability: IMMUTABLE_GIT_EVENT_AND_VERSIONED_CURRENT_NOT_TRANSIENT_CONNECTOR_OUTPUT
observability: PARTIAL_SUCCESS_EMPTY_AND_TYPED_NORMALIZED_INVALID_ARGUMENT_SHAPES_WITHOUT_TRANSPORT_RAW_PROVIDER_QUOTA_SCOPE_OR_HIDDEN_ATTEMPT_DETAIL
portability: MEDIUM_PROVIDER_SPECIFIC_QUERY_AND_PAGINATION_SEMANTICS_WITH_PORTABLE_FAIL_CLOSED_GATES
failure_behavior: SYNTHETIC_INVALID_PAGE_TOKEN_FAILED_CLOSED_WITH_TYPED_NORMALIZED_INVALID_ARGUMENT_AND_NO_MESSAGE_IDS
paid_cost_usd_observed: 0_NO_CHARGE_SURFACED
actual_quota_consumed: UNKNOWN
official_quota_contract: USERS_MESSAGES_LIST_5_UNITS_PER_REQUEST_AS_OF_2026_08_04
mandatory_gates: BOUNDED_READONLY_ID_ONLY_HUMAN_REVIEWED_SEARCH_EMPTY_RESULTS_NONAUTHORITATIVE_ZERO_IDS_DURING_ERRORS_NONAUTHORITATIVE_USE_ONLY_IMMEDIATELY_PRECEDING_COMPATIBLE_RETURNED_TOKEN_NO_UNCHANGED_RETRY_NO_QUERY_IDENTIFIER_OR_TOKEN_RETENTION_WITHOUT_NAMED_NEED_RAW_SCOPE_VALID_PAGINATION_QUOTA_CONSUMER_AND_FAILURE_WITNESS_REQUIRED_BEFORE_UNATTENDED_USE
strongest_falsifier: SAME_PRINCIPAL_RAW_USERS_MESSAGES_LIST_DISAGREES_WITH_CONNECTOR_RESULT_SHAPE_OR_ACCEPTS_THE_IDENTICAL_INVALID_TOKEN_OR_CONNECTOR_REJECTS_AN_IMMEDIATELY_PRECEDING_VALID_RETURNED_TOKEN_UNDER_AN_IDENTICAL_QUERY_BOUNDARY
verifier: NOT_ASSIGNED
independent_verification_closed: false
consumer: NOT_ASSIGNED
consumer_ack: NOT_OBSERVED
adoption_credit: 0
fitness_credit: 0
honest_flaw: ONE_POSITIVE_ONE_SYNTHETIC_EMPTY_AND_ONE_SYNTHETIC_INVALID_TOKEN_CALL_DO_NOT_VERIFY_IDENTITY_SCOPE_QUERY_TRANSLATION_ORDERING_COMPLETENESS_VALID_PAGINATION_AUTH_PERMISSION_RATE_LIMIT_TRANSIENT_FAILURE_HIDDEN_CALLS_RAW_PROVIDER_PARITY_ACTUAL_QUOTA_CONSUMPTION_OR_CONSUMER_VALUE
next_campaign_candidate: Google_Calendar_search_events_readonly_surface
next_campaign_phase: PHASE1_OFFICIAL_CONTRACT_AND_DIRECT_CAPABILITY_BASELINE
valid_time_utc: 2026-08-04T20:49:10Z
recorded_time_utc: 2026-08-04T20:49:10Z
---

# X13 Gmail search-email-IDs phase 4 decision

## Decision

`ADOPT_WITH_GATES`

Adopt the Gmail `search_email_ids` connector only as a bounded, read-only, human-reviewed message-ID discovery surface. This is a catalog/manual-use decision, not operational approval. No additional Gmail candidate call was made in phase 4.

## Evidence considered

Across three bounded calls, the connector produced one positive ID-only result with a continuation token, one normal empty ID array with no continuation token, and one typed normalized `INVALID_ARGUMENT` failure for a synthetic invalid page token. It returned no email content, headers, thread IDs, or result-size estimate. No retry, fallback, pagination follow-up, hydration, or mutation occurred.

The campaign establishes that the connector can perform a narrow Gmail-style ID search, normalize an easy empty-result path, and fail closed on one invalid-token probe. It does not establish authoritative absence, complete mailbox coverage, exact query translation, stable ordering, effective identity or OAuth scope, valid pagination, raw-provider parity, hidden-call behavior, actual quota use, or consumer value.

## Adopted boundary

Allowed:

1. Explicitly bounded, read-only searches with a minimal result cap.
2. Human review before any downstream interpretation or follow-up.
3. Ephemeral use of returned IDs or continuation tokens unless a named retention need exists.

Not allowed:

1. Unattended control-plane decisions.
2. Treating empty results or zero IDs during errors as proof of absence.
3. Completeness, ordering, identity, permission, or quota claims without an independent same-principal witness.
4. Retaining queries, identifiers, or tokens without a named consumer and retention requirement.
5. Retrying a rejected page token unchanged.

## Measurements

- Custom code avoided: `15-45 LOC`, estimate only and unvalidated.
- Operator minutes removed: `0` measured.
- Credentials: connector-managed; effective principal and OAuth scope unknown.
- Durability: immutable Git event plus versioned CURRENT.
- Observability: partial; success, empty, and normalized invalid-argument shapes observed, but transport, raw-provider, scope, quota, and hidden-attempt detail absent.
- Portability: medium; Gmail query and pagination semantics are provider-specific, while fail-closed gates are portable.
- Failure behavior: one synthetic invalid page token failed closed with typed normalized `INVALID_ARGUMENT` and no IDs.
- Direct cost: no charge surfaced; actual quota debit unknown.
- Verifier: not assigned; independent verification not closed.
- Consumer: not assigned; acknowledgment not observed.
- Adoption and fitness credit: zero.

## Strongest falsifier

A same-principal raw `users.messages.list` witness materially disagrees with the connector result shape, accepts the identical invalid token, or the connector rejects an immediately preceding valid returned token under an identical query boundary.

## Honest flaw

The decision rests on only one easy positive query, one deliberately empty query, and one synthetic invalid-token failure. Identity, scope, query translation, ordering, completeness, valid pagination, authentication and permission failures, rate limits, transient failures, hidden retries, raw-provider parity, actual quota consumption, operator time saved, and consumer value remain unverified.

## Next campaign

Queue phase 1 for a bounded, read-only Google Calendar event-search surface. No Calendar call is made in this event.

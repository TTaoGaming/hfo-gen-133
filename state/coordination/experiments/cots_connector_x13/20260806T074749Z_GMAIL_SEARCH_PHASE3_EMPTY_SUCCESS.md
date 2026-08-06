---
schema_id: hfo.gen133.x13.cots_connector_event.v1
experiment_id: X13_GMAIL_SEARCH_READONLY_008
event_type: PHASE3_SYNTHETIC_NONMATCH_EMPTY_SUCCESS
phase: 3
phase_status: PHASE3_ACCEPTED_WITH_GATES
carrier_task_id: 6a55c1733708819185088bf334e33ea5
carrier_task_id_match: true
wip: 1
candidate: Gmail_search_email_ids_readonly_surface
repository: TTaoGaming/hfo-gen-133
branch: agent/gen133-bootstrap-20260730
prior_current_version: 130
expected_next_current_version: 131
request_descriptor_sha256: 72caef78337d6ddd28432e6ef539e32b2f06645163de15613f01f0c95e02ee87
synthetic_token_sha256: 83130a0181efea504c7381da711988e68fad7fb08b1dfbb12a750b6a0056436b
request_shape: DOCUMENTED_DATE_BOUNDS_SYNTHETIC_QUOTED_NONMATCH_EXCLUDE_SPAM_TRASH_MAX_RESULTS_1_ID_ONLY
content_hydration: false
calls_this_wake: 1
campaign_calls_total_after_event: 4
result_count: 0
continuation_present: false
connector_error_present: false
error_http_status_present: false
external_latency_ms: 314
retries: 0
fallbacks: 0
mutations: 0
raw_message_ids_persisted: false
raw_page_tokens_persisted: false
raw_query_persisted: false
measured_fact: SYNTHETIC_NONMATCH_ID_ONLY_SEARCH_RETURNED_EMPTY_LIST_NULL_PAGE_TOKEN_AND_NULL_ERROR
andon: EMPTY_SUCCESS_IS_DISTINCT_FROM_CONNECTOR_ERROR_BUT_DOES_NOT_PROVE_AUTHORITATIVE_MAILBOX_ABSENCE_OR_RAW_PROVIDER_PARITY
custom_code_avoided_estimate: 25_to_70_LOC_UNVALIDATED
operator_minutes_removed_measured: 0
credentials: CONNECTOR_MANAGED_EFFECTIVE_AUTH_CONTEXT_UNKNOWN
durability: EVENT_IS_GIT_RECORDED_MAILBOX_RESULT_IS_DYNAMIC_AND_NEGATIVE_RESULT_IS_NOT_DURABLE_EVIDENCE
observability: RESULT_COUNT_NULL_CONTINUATION_NULL_ERROR_CONNECTOR_ACTION_AND_LATENCY_EXPOSED_PROVIDER_RESULT_SIZE_ESTIMATE_HEADERS_REQUEST_ID_IDENTITY_SCOPE_PROJECT_QUERY_TRANSLATION_AND_DIRECT_QUOTA_NOT_EXPOSED
portability: LOW_TO_MEDIUM_DOCUMENTED_DATE_OPERATORS_USED_BUT_GMAIL_QUERY_GRAMMAR_IDS_AND_CURSOR_MODEL_ARE_PROVIDER_SPECIFIC
failure_behavior: EMPTY_SUCCESS_PATH_DISTINGUISHED_FROM_CONNECTOR_ERROR_INVALID_QUERY_PERMISSION_THROTTLE_AND_TRANSIENT_FAILURE_NOT_TESTED
paid_cost_usd_observed: 0_NO_CHARGE_SURFACED
nominal_quota_contract: 5_UNITS_PER_MESSAGES_LIST_REQUEST
nominal_quota_if_one_to_one_this_phase: 5_UNITS
actual_quota_consumed: UNKNOWN
catalog_consumer: HFO_COTS_CAPABILITY_INVENTORY_CATALOG_ONLY
operational_consumer: NOT_ASSIGNED
consumer_ack: NOT_OBSERVED
verifier: DISTINCT_RAW_GMAIL_USERS_MESSAGES_LIST_CALL_UNDER_SAME_PRINCIPAL_WITH_EQUIVALENT_DOCUMENTED_DATE_BOUNDED_SYNTHETIC_QUERY
verifier_result: NOT_RUN
strongest_falsifier: MATCHED_RAW_PROVIDER_CALL_RETURNS_A_MESSAGE_ERROR_OR_MATERIALLY_DIFFERENT_PAGINATION_OR_RESULT_ESTIMATE_STATE
honest_flaw: SYNTHETIC_QUERY_WAS_DESIGNED_TO_MISS_AND_DID_NOT_TEST_INVALID_SYNTAX_PERMISSION_DENIAL_THROTTLING_TRANSIENT_FAILURE_PAGINATION_LATER_REPLAY_OPERATOR_SAVINGS_OR_CONSUMER_VALUE
adoption_credit: 0
fitness_credit: 0
next_phase: PHASE4_PENDING
next_probe: PHASE4_DECISION_FROM_EXISTING_RECEIPTS_ONLY_NO_ADDITIONAL_GMAIL_CALL
valid_time_utc: 2026-08-06T07:47:49Z
recorded_time_utc: 2026-08-06T07:47:49Z
---

# X13 Gmail search phase 3 — synthetic nonmatch empty-success path

## Direct result

One bounded, read-only `Gmail.search_email_ids` call used documented calendar-date bounds, a quoted synthetic nonmatching token, Spam and Trash exclusions, `max_results=1`, and no content hydration.

The connector returned:

- `message_ids=[]`;
- `next_page_token=null`;
- `error=null` and no HTTP error status;
- external-call latency of 314 ms;
- zero retries, fallbacks, sends, writes, or mailbox mutations.

The raw query, message IDs, and page tokens were not persisted. The normalized request descriptor and synthetic token were retained only as SHA-256 digests.

## Official contract baseline

Google documents `users.messages.list` as returning a list of message identifiers, an optional `nextPageToken`, and a `resultSizeEstimate`. The connector exposed the identifier list and page-token state but not the raw provider `resultSizeEstimate`, response envelope, headers, request ID, effective principal, OAuth scope, Cloud project, or quota debit.

- https://developers.google.com/workspace/gmail/api/reference/rest/v1/users.messages/list
- https://support.google.com/mail/answer/7190

Google's current quota table assigns five quota units to `messages.list`. That is only a nominal contract value here: the connector did not prove a one-to-one raw method mapping or expose a direct quota receipt.

- https://developers.google.com/workspace/gmail/api/reference/quota

## Measured Andon

The wrapper clearly distinguished an empty-success result from a connector error for this call. That is useful failure classification, but `message_ids=[]` proves only that this wrapper invocation returned no visible matches for the synthetic query.

It does not prove authoritative mailbox absence, exact raw-query translation, principal or scope parity, stable negative replay, or raw-provider equivalence. High-stakes negative claims require an independent raw-provider witness under the same effective principal.

## Gates retained

1. Treat an empty wrapper result as `no_visible_matches_returned`, not authoritative absence.
2. Keep searches ID-only until a bound consumer requires content.
3. Treat `max_results` as an output cap, never completeness evidence.
4. Persist only normalized request and result digests by default.
5. Do not infer effective identity, OAuth scope, Cloud project, provider method, or quota debit from connector success.
6. Require independent verification before using a negative search result for a consequential decision.
7. Do not retry an unchanged synthetic empty result in a tight loop.

## Evidence boundary

This phase establishes only the connector's empty-success path for one synthetic nonmatching query. It does not test invalid-query parsing, permission denial, throttling, transient transport or server failures, pagination behavior, later replay after mailbox mutation, operator savings, or operational consumer value.

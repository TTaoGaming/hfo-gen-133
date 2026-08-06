---
schema_id: hfo.gen133.x13.cots_connector_event.v1
experiment_id: X13_GMAIL_SEARCH_READONLY_008
event_type: PHASE2_ABSOLUTE_TIME_BOUNDED_REPEATABILITY
phase: 2
phase_status: PHASE2_ACCEPTED_WITH_GATES
carrier_task_id: 6a55c1733708819185088bf334e33ea5
carrier_task_id_match: true
wip: 1
candidate: Gmail_search_email_ids_readonly_surface
repository: TTaoGaming/hfo-gen-133
branch: agent/gen133-bootstrap-20260730
prior_current_version: 129
expected_next_current_version: 130
request_descriptor_sha256: 8dbd43e7b5402843e967281df095440bc00553882fd14244bd4bf67121f61cd6
request_shape: FIXED_EPOCH_BOUNDS_EXCLUDE_SPAM_TRASH_MAX_RESULTS_1_ID_ONLY
content_hydration: false
calls_this_wake: 2
campaign_calls_total_after_event: 3
call_1_result_count: 1
call_2_result_count: 1
message_id_digest_match: true
message_id_sha256: 976e5135536525136267cad00a70af257cbf989e5fb928eefc076b71a451caaf
continuation_present_both_calls: true
continuation_token_digest_match: true
continuation_token_sha256: 454fab8296692c5a122b14c49dd924236132446fd35280db4a050f2a65f07484
call_1_external_latency_ms: 292
call_2_external_latency_ms: 195
retries: 0
fallbacks: 0
mutations: 0
raw_message_ids_persisted: false
raw_page_tokens_persisted: false
raw_query_persisted: false
measured_fact: TWO_IDENTICAL_FIXED_WINDOW_ID_ONLY_SEARCHES_RETURNED_THE_SAME_SINGLE_MESSAGE_ID_DIGEST_AND_CONTINUATION_TOKEN_DIGEST
andon: EPOCH_SECOND_DATE_OPERATORS_WORKED_IN_CONNECTOR_BUT_ARE_NOT_DOCUMENTED_IN_OFFICIAL_GMAIL_SEARCH_HELP_SO_PORTABILITY_IS_UNPROVEN
custom_code_avoided_estimate: 25_to_70_LOC_UNVALIDATED
operator_minutes_removed_measured: 0
credentials: CONNECTOR_MANAGED_EFFECTIVE_AUTH_CONTEXT_UNKNOWN
durability: EVENT_IS_GIT_RECORDED_MAILBOX_RESULT_IS_DYNAMIC_BUT_FIXED_QUERY_DESCRIPTOR_IS_REPLAYABLE
observability: RESULT_COUNT_CONTINUATION_PRESENCE_ERROR_STATE_CONNECTOR_ID_ACTION_AND_LATENCY_EXPOSED_PROVIDER_HEADERS_REQUEST_ID_IDENTITY_SCOPE_PROJECT_RESULT_SIZE_ESTIMATE_AND_DIRECT_QUOTA_NOT_EXPOSED
portability: LOW_PROVIDER_SPECIFIC_QUERY_IDENTIFIERS_AND_UNDOCUMENTED_EPOCH_OPERATOR_FORM
failure_behavior: SUCCESS_REPEATABILITY_PATH_ONLY
paid_cost_usd_observed: 0_NO_CHARGE_SURFACED
nominal_quota_contract: 5_UNITS_PER_MESSAGES_LIST_REQUEST
nominal_quota_if_one_to_one_wrapper_mapping: 10_UNITS_FOR_TWO_CALLS
actual_quota_consumed: UNKNOWN
catalog_consumer: HFO_COTS_CAPABILITY_INVENTORY_CATALOG_ONLY
operational_consumer: NOT_ASSIGNED
consumer_ack: NOT_OBSERVED
verifier: DISTINCT_RAW_GMAIL_USERS_MESSAGES_LIST_CALL_UNDER_SAME_PRINCIPAL_WITH_IDENTICAL_FIXED_QUERY
verifier_result: NOT_RUN
strongest_falsifier: RAW_PROVIDER_CALL_REJECTS_EPOCH_QUERY_OR_RETURNS_DIFFERENT_MESSAGE_OR_PAGINATION_STATE_UNDER_THE_SAME_PRINCIPAL
honest_flaw: TWO_NEAR_IMMEDIATE_SUCCESS_CALLS_DO_NOT_TEST_LATER_REPLAY_MAILBOX_MUTATION_PERMISSION_FAILURE_EMPTY_RESULT_RATE_LIMIT_TRANSIENT_FAILURE_OR_OPERATIONAL_VALUE
adoption_credit: 0
fitness_credit: 0
next_phase: PHASE3_PENDING
next_probe: SYNTHETIC_NONMATCHING_FIXED_WINDOW_ID_ONLY_QUERY_OR_INVALID_QUERY_FAILURE_PROBE
valid_time_utc: 2026-08-06T06:50:56Z
recorded_time_utc: 2026-08-06T06:50:56Z
---

# X13 Gmail search phase 2 — absolute-time repeatability

## Direct result

Two identical, bounded `Gmail.search_email_ids` calls used a fixed absolute query descriptor, `max_results=1`, and no content hydration.

Both calls returned:

- one message ID;
- a continuation token;
- no connector error;
- the same one-way message-ID digest;
- the same one-way continuation-token digest.

Raw message IDs, raw page tokens, and the raw search query were not persisted. The normalized request descriptor was retained only as SHA-256 `8dbd43e7b5402843e967281df095440bc00553882fd14244bd4bf67121f61cd6`.

External-call latency was 292 ms and 195 ms. There were zero retries, fallbacks, writes, sends, or mailbox mutations.

## Official contract baseline

Google documents `users.messages.list` as an ID-listing endpoint whose `maxResults` is a maximum, whose response may contain `nextPageToken`, and whose message resources in the list contain IDs rather than full message content. The endpoint accepts Gmail search syntax through `q` and requires a Gmail OAuth scope.

- https://developers.google.com/workspace/gmail/api/reference/rest/v1/users.messages/list
- https://support.google.com/mail/answer/7190

Google's current quota table assigns five quota units to `messages.list`. If each wrapper call maps one-to-one to that method, these two calls would nominally represent ten units, but the wrapper exposed no raw provider path or quota debit, so actual consumption remains unknown.

- https://developers.google.com/workspace/gmail/api/reference/quota

## Measured Andon

The connector accepted epoch-second values in `after:` and `before:` and returned stable results across two near-immediate calls. Official Gmail search help documents date-form operators but does not document epoch-second syntax. Therefore, epoch-bound portability and long-term contract stability are not proven.

Do not treat the page token as durable state. It is an opaque provider cursor and may become stale as mailbox state changes.

## Gates retained

1. Keep searches ID-only until a bound consumer requires content.
2. Treat `max_results` as a cap, never completeness evidence.
3. Handle continuation explicitly.
4. Persist only normalized request digests and one-way result digests by default.
5. Do not infer effective identity, OAuth scope, Cloud project, provider request path, or quota debit from connector success.
6. Do not rely operationally on undocumented epoch syntax without a raw-provider verifier or a documented date-bound fallback.
7. Re-run failure and empty-result probes before operational adoption.

## Evidence boundary

This establishes narrow, near-immediate wrapper repeatability for one fixed query window. It does not establish historical replay after mailbox mutation, stable ordering, permission behavior, raw-provider parity, rate-limit handling, time savings, or consumer value.

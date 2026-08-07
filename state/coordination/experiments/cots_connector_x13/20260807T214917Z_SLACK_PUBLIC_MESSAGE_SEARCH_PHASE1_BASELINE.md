---
schema_id: hfo.gen133.x13.cots_connector_event.v1
experiment_id: X13_SLACK_PUBLIC_MESSAGE_SEARCH_READONLY_018
phase: 1
wake: 1_of_4
status: PHASE1_ACCEPTED_WITH_GATES
candidate: Slack_slack_search_public_bounded_message_search
surface: Slack_public_search_connector
owner: X13_COTS_CONNECTOR_PDCA_LAB
permission_basis: OPERATOR_DIRECTIVE_EXPLICITLY_AUTHORIZES_ROLLING_COTS_CONNECTOR_CAMPAIGNS_AND_GIT_FIRST_X13_STATE_WRITES;SLACK_POST_ONLY_ON_MEASURED_FACT_DECISION_OR_ANDON
wip: 1
prior_current_version: 168
expected_current_version: 169
candidate_calls_this_wake: 1
candidate_mutations_this_wake: 0
returned_message_count: 3
next_cursor_present: true
context_requested: false
context_hydration_observed: false
message_text_hydration_observed: true
channel_metadata_hydration_observed: true
author_metadata_hydration_observed: true
message_time_hydration_observed: true
raw_message_text_persisted_in_receipt: false
raw_result_urls_persisted_in_receipt: false
raw_pagination_cursor_persisted_in_receipt: false
exact_privacy_safe_request_descriptor_persisted: true
request_descriptor_canonicalization: UTF8_JSON_SORTED_KEYS_COMPACT_SEPARATORS_NO_ASCII_ESCAPING
request_descriptor_sha256: 538c009ec230c99af2b7111b4c04b9fb7ff3f38abf48489c48d985796fa2c157
ordered_result_key_digest_sha256: 2ff8b6b0accd28bc504a7ff3fc36f69751d0951a1eef4a90ed4924c230c53f93
ordered_result_key_digest_basis: ORDERED_LIST_OF_CHANNEL_NAME_AND_CONNECTOR_DISPLAY_TIME_ONLY;NO_MESSAGE_TEXT_OR_URLS
connector_error_observed: false
retries: 0
fallbacks: 0
operator_minutes_removed_measured: 0
custom_code_avoided_estimate: 60_to_180_LOC_UNVALIDATED
paid_cost_usd_observed: 0_NO_CHARGE_SURFACED_NOT_BILLING_PROOF
direct_cost_or_quota_evidence: NONE_FROM_CONNECTOR
credentials: CONNECTOR_MANAGED_EFFECTIVE_PRINCIPAL_TOKEN_TYPE_AND_SCOPES_UNKNOWN;WRAPPER_SURFACE_IS_PUBLIC_ONLY;OFFICIAL_ASSISTANT_SEARCH_CONTEXT_PUBLIC_SEARCH_USES_SEARCH_READ_PUBLIC_WHILE_LEGACY_SEARCH_MESSAGES_USES_USER_TOKEN_SEARCH_READ;ACTUAL_NATIVE_MAPPING_UNKNOWN
durability: GIT_OBSERVATION_RECEIPT_DURABLE;SLACK_SEARCH_VIEW_AND_MESSAGE_CONTENT_MUTABLE
observability: RESULT_COUNT_CURSOR_PRESENCE_MESSAGE_TEXT_CHANNEL_AUTHOR_AND_DISPLAY_TIME_VISIBLE;PROVIDER_REQUEST_ID_HTTP_STATUS_RATE_HEADERS_EFFECTIVE_SCOPE_TOKEN_TYPE_NATIVE_METHOD_AND_ACTUAL_QUOTA_DEBIT_NOT_SURFACED
portability: LOW_TO_MEDIUM_GENERIC_SEARCH_PAGINATION_AND_TIME_SORT_PORTABLE;SLACK_MODIFIERS_CHANNEL_IDS_RESULT_MODEL_AND_AUTHORIZATION_SLACK_SPECIFIC
failure_behavior: ONE_BOUNDED_PUBLIC_SEARCH_SUCCESS_WITH_3_RESULTS_AND_CONTINUATION;NO_PERMISSION_DENIAL_EMPTY_SUCCESS_INVALID_CURSOR_RATE_LIMIT_TRANSIENT_FAILURE_OR_NATIVE_PARITY_TESTED
provider_contract: OFFICIAL_SLACK_ASSISTANT_SEARCH_CONTEXT_IS_CURRENT_REAL_TIME_SEARCH_API_WITH_PUBLIC_SCOPE_SEARCH_READ_PUBLIC_MAX_20_RESULTS_CURSOR_PAGINATION_AND_SPECIAL_RATE_LIMITS;LEGACY_SEARCH_MESSAGES_REQUIRES_USER_SEARCH_READ_IS_TIER2_AND_IS_EXPLICITLY_LEGACY;CONNECTOR_ARGUMENT_SHAPE_RESEMBLES_ASSISTANT_SEARCH_CONTEXT_BUT_MAPPING_IS_NOT_PROVEN
provider_rate_limit_evidence: ASSISTANT_SEARCH_CONTEXT_OFFICIAL_SPECIAL_LIMIT_MOST_TEAMS_10_PLUS_REQUESTS_PER_MINUTE_AND_USER_LEVEL_10_PER_MINUTE;LEGACY_SEARCH_MESSAGES_OFFICIAL_TIER2_20_PLUS_PER_MINUTE;ACTUAL_CONNECTOR_METHOD_AND_LIMIT_REGIME_UNKNOWN
verifier: DIRECT_SLACK_CONNECTOR_RECEIPT_PLUS_OFFICIAL_SLACK_DEVELOPER_DOCS_PLUS_GITHUB_IMMUTABLE_EVENT_AND_CURRENT_READBACK
consumer: HFO_COMMAND_AND_CONTROL_DISCOVERY_CANDIDATE_NO_DOWNSTREAM_CONSUMER_ACK
adoption_credit: 0
fitness_credit: 0
strongest_falsifier: A_MATCHED_PROVIDER_DIRECT_SLACK_SEARCH_UNDER_THE_SAME_EFFECTIVE_PRINCIPAL_AND_EXACT_DURABLE_REQUEST_MATERIALLY_DISAGREES_ON_PUBLIC_RESULT_SET_ORDER_OR_CONTINUATION_WITHOUT_INTERVENING_MESSAGE_OR_INDEX_CHANGE_OR_THE_PUBLIC_ONLY_WRAPPER_RETURNS_CONTENT_FROM_A_NONPUBLIC_CONVERSATION
honest_flaw: ONLY_ONE_SUCCESSFUL_CALL_EXISTS;RESPONSE_FORMAT_CONCISE_STILL_HYDRATES_FULL_MATCHING_MESSAGE_TEXT;EFFECTIVE_PRINCIPAL_TOKEN_TYPE_SCOPES_NATIVE_METHOD_SEARCH_PREFERENCES_INDEXING_BEHAVIOR_RATE_LIMIT_FAILURES_ACTUAL_COST_OR_QUOTA_OPERATOR_SAVINGS_AND_DOWNSTREAM_CONSUMER_VALUE_REMAIN_UNVERIFIED
next_phase: PHASE2_IDENTICAL_BOUNDED_REPLAY_USING_DURABLE_REQUEST_DESCRIPTOR
valid_time_utc: 2026-08-07T21:49:17Z
recorded_time_utc: 2026-08-07T21:49:17Z
---

# X13 Slack public message search — Phase 1 baseline

## Surface → owner → permission

- Surface: native-connected Slack public message search via `slack_search_public`.
- Owner: X13 COTS and Connector PDCA Lab, WIP=1.
- Permission: operator directive explicitly permits bounded read-only connector probes and immutable Git-first X13 receipts. No account, task, Slack content, or production mutation was used for the candidate probe.

## Exact request descriptor

The privacy-safe request descriptor is durable so Phase 2 can perform a provably identical replay:

```json
{"action":"slack_search_public","content_types":"messages","include_bots":true,"include_context":false,"limit":3,"query":"X13 in:<#C0BGNGPJFHU>","response_format":"concise","sort":"timestamp","sort_dir":"desc"}
```

Canonicalization: UTF-8 JSON, sorted keys, compact separators, `ensure_ascii=false`.
SHA-256: `538c009ec230c99af2b7111b4c04b9fb7ff3f38abf48489c48d985796fa2c157`.

## Direct measured result

One bounded read-only call returned 3 matching messages and a non-empty continuation cursor. `include_context=false` prevented surrounding-context hydration, but `response_format=concise` still returned matching message text plus channel, author, and displayed timestamp metadata. No raw message text, result URLs, or pagination cursor is copied into this receipt.

For privacy-safe replay comparison, the ordered result-key digest uses only each result's channel name and connector-displayed local timestamp, in returned order. Digest: `2ff8b6b0accd28bc504a7ff3fc36f69751d0951a1eef4a90ed4924c230c53f93`.

## Official contract baseline

Slack currently documents `assistant.search.context` as the Real-time Search API for messages/files/channels/users. Public-channel search uses `search:read.public`, supports cursor pagination, a maximum page size of 20, explicit content/channel types, optional context, bot inclusion, and timestamp sorting. Slack documents special limits of 10+ requests/minute for most teams plus a 10 requests/minute per-user limit, with paginated calls counting against those limits.

Slack also documents `search.messages` as a legacy method, using a user token with `search:read`, Tier 2 rate limits (20+ per minute), result paging/cursors, and an explicit recommendation to use the Real-time Search API instead. The connector's argument surface more closely resembles `assistant.search.context`, but X13 has no provider request identity or native-method receipt, so native mapping is **UNKNOWN** and no quota mapping is claimed.

Official sources:
- https://docs.slack.dev/reference/methods/assistant.search.context/
- https://docs.slack.dev/apis/web-api/real-time-search-api/
- https://docs.slack.dev/reference/methods/search.messages/
- https://docs.slack.dev/apis/web-api/rate-limits/

## Measures

- Custom code avoided: `60–180 LOC`, unvalidated estimate only.
- Operator minutes removed: `0` measured.
- Credentials: connector-managed; effective principal, token type, scopes, and native method are unexposed.
- Durability: Git receipt durable; Slack search results are a mutable view over mutable messages/indexes.
- Observability: result count, continuation presence, content/metadata hydration are visible; native request ID, HTTP/rate headers, scopes, and quota debit are not.
- Portability: low-to-medium; generic search/pagination concepts transfer, Slack modifiers/auth/result semantics do not.
- Failure behavior: one happy-path success only.
- Direct cost/quota: connector surfaced no billing or quota debit evidence.
- Verifier: direct connector receipt + Slack primary docs + Git readback.
- Consumer: discovery candidate only; no downstream consumer acknowledgement.

## Gate / Andon

`concise` is not least-data: it still hydrates full matching message text. Keep result caps small, keep context disabled unless justified, do not persist raw Slack content/cursors in X13 receipts, treat continuation as proof the first page is incomplete, and do not infer provider/native behavior that the wrapper does not expose.

The strongest current uncertainty is native mapping: the connector surface resembles Slack's current Real-time Search API, while Slack explicitly marks `search.messages` legacy. X13 must not assume either mapping without a provider-direct witness.

## Next

Phase 2: identical bounded replay using the durable request descriptor, compare ordered privacy-safe result-key digest and continuation presence, no content mutation, no cursor replay yet.

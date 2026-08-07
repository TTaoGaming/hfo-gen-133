---
schema_id: hfo.gen133.x13.cots_connector_event.v1
experiment_id: X13_SLACK_PUBLIC_MESSAGE_SEARCH_READONLY_018
phase: 2
wake: 2_of_4
status: PHASE2_ACCEPTED_WITH_GATES
candidate: Slack_slack_search_public_bounded_message_search
surface: Slack_public_search_connector
owner: X13_COTS_CONNECTOR_PDCA_LAB
permission_basis: OPERATOR_DIRECTIVE_EXPLICITLY_AUTHORIZES_BOUNDED_READONLY_CONNECTOR_PROBES_AND_GIT_FIRST_X13_STATE_WRITES;NO_SLACK_POST_UNTIL_GIT_RECEIPTS_AND_CURRENT_READBACK
wip: 1
prior_current_version: 169
expected_current_version: 170
candidate_calls_this_wake: 1
candidate_mutations_this_wake: 0
returned_message_count: 3
next_cursor_present: true
context_requested: false
context_hydration_observed: false
message_text_hydration_observed: true
raw_message_text_persisted_in_receipt: false
raw_result_urls_persisted_in_receipt: false
raw_pagination_cursor_persisted_in_receipt: false
identical_request_replay_proven: true
request_descriptor_canonicalization: UTF8_JSON_SORTED_KEYS_COMPACT_SEPARATORS_NO_ASCII_ESCAPING
request_descriptor_sha256: 538c009ec230c99af2b7111b4c04b9fb7ff3f38abf48489c48d985796fa2c157
phase1_ordered_result_key_digest_sha256: 2ff8b6b0accd28bc504a7ff3fc36f69751d0951a1eef4a90ed4924c230c53f93
phase1_result_digest_serialization_algorithm_durable: false
phase2_result_digest_canonicalization: UTF8_JSON_SORTED_KEYS_COMPACT_SEPARATORS_NO_ASCII_ESCAPING_OVER_ORDERED_LIST_OF_CHANNEL_AND_DISPLAY_TIME_OBJECTS
phase2_ordered_result_key_digest_sha256: 0a43b5c63b8ab6c928a033c339639026983ab83dda5ff7c8025124fd622d29f1
phase2_result_keys_persisted_raw: false
phase2_results_newer_than_phase1_valid_time: 2
ordered_result_set_same_as_phase1: false_PROVEN_BY_TWO_RETURNED_MESSAGES_NEWER_THAN_PHASE1_VALID_TIME_NOT_BY_DIGEST_COMPARISON
connector_call_time_ms: NOT_MEASURED_BY_AVAILABLE_RECEIPT
connector_error_observed: false
retries: 0
fallbacks: 0
operator_minutes_removed_measured: 0
custom_code_avoided_estimate: 60_to_180_LOC_UNVALIDATED
paid_cost_usd_observed: 0_NO_CHARGE_SURFACED_NOT_BILLING_PROOF
direct_cost_or_quota_evidence: NONE_FROM_CONNECTOR
credentials: CONNECTOR_MANAGED_EFFECTIVE_PRINCIPAL_TOKEN_TYPE_AND_SCOPES_UNKNOWN;WRAPPER_SURFACE_PUBLIC_ONLY;ACTUAL_NATIVE_MAPPING_UNKNOWN
durability: GIT_OBSERVATION_RECEIPT_DURABLE;SLACK_SEARCH_RESULTS_ARE_MUTABLE_QUERY_VIEWS_AND_NOT_SNAPSHOTS
observability: REQUEST_REPLAY_RESULT_COUNT_CURSOR_PRESENCE_CONTENT_HYDRATION_AND_DISPLAY_TIMES_VISIBLE;PROVIDER_REQUEST_ID_HTTP_STATUS_RATE_HEADERS_EFFECTIVE_SCOPE_TOKEN_TYPE_NATIVE_METHOD_AND_ACTUAL_QUOTA_DEBIT_NOT_SURFACED
portability: LOW_TO_MEDIUM_GENERIC_SEARCH_PAGINATION_AND_TIME_SORT_PORTABLE;SLACK_QUERY_MODIFIERS_AUTHORIZATION_AND_RESULT_MODEL_SLACK_SPECIFIC
failure_behavior: TWO_BOUNDED_PUBLIC_SEARCHES_SUCCEEDED_WITH_3_RESULTS_AND_CONTINUATION;IDENTICAL_REQUEST_REPLAY_RETURNED_A_CHANGED_TOP3_AFTER_INTERVENING_MATCHING_MESSAGES;NO_PERMISSION_DENIAL_EMPTY_SUCCESS_INVALID_CURSOR_RATE_LIMIT_TRANSIENT_FAILURE_OR_NATIVE_PARITY_TESTED
provider_contract: CARRIED_FROM_PHASE1_OFFICIAL_SLACK_REAL_TIME_SEARCH_AND_LEGACY_SEARCH_MESSAGES_BASELINE;NO_NEW_PROVIDER_CLAIM_THIS_WAKE
verifier: DIRECT_SLACK_CONNECTOR_RECEIPT_PLUS_PRIOR_DURABLE_EXACT_REQUEST_DESCRIPTOR_PLUS_GITHUB_IMMUTABLE_EVENT_AND_CURRENT_READBACK
consumer: HFO_COMMAND_AND_CONTROL_DISCOVERY_CANDIDATE_NO_DOWNSTREAM_CONSUMER_ACK
adoption_credit: 0
fitness_credit: 0
strongest_falsifier: UNDER_A_QUIESCENT_MATCH_SET_A_MATCHED_PROVIDER_DIRECT_SLACK_SEARCH_WITH_THE_SAME_EFFECTIVE_PRINCIPAL_AND_EXACT_REQUEST_MATERIALLY_DISAGREES_ON_PUBLIC_RESULT_SET_ORDER_OR_CONTINUATION_OR_THE_PUBLIC_ONLY_WRAPPER_RETURNS_NONPUBLIC_CONTENT
honest_flaw: THIS_REPLAY_PROVES_REQUEST_REPRODUCIBILITY_AND_RESPONSE_SHAPE_BUT_NOT_RESULT_STABILITY_BECAUSE_MATCHING_SLACK_CONTENT_CHANGED_BETWEEN_WAKES;PHASE1_RESULT_DIGEST_SERIALIZATION_WAS_NOT_DURABLE_SO_HASH_EQUALITY_CANNOT_BE_USED_AS_THE_PROOF;EFFECTIVE_PRINCIPAL_SCOPES_NATIVE_METHOD_RATE_LIMITS_ACTUAL_QUOTA_OPERATOR_SAVINGS_AND_CONSUMER_VALUE_REMAIN_UNVERIFIED
next_phase: PHASE3_ONE_BOUNDED_SYNTHETIC_NONMATCHING_PUBLIC_SEARCH_WITH_EXACT_PRIVACY_SAFE_REQUEST_DESCRIPTOR_NO_RETRY_NO_ABSENCE_CLAIM
valid_time_utc: 2026-08-07T22:49:50Z
recorded_time_utc: 2026-08-07T22:49:50Z
---

# X13 Slack public message search — Phase 2 identical replay

## Surface → owner → permission

- Surface: connected Slack public message search via `slack_search_public`.
- Owner: X13 COTS and Connector PDCA Lab, WIP=1.
- Permission: operator directive permits bounded read-only connector probes and immutable Git-first X13 receipts. No Slack content, account, task, or production mutation was used.

## Exact replay

Phase 2 reused the Phase-1 privacy-safe request descriptor exactly:

```json
{"action":"slack_search_public","content_types":"messages","include_bots":true,"include_context":false,"limit":3,"query":"X13 in:<#C0BGNGPJFHU>","response_format":"concise","sort":"timestamp","sort_dir":"desc"}
```

Canonical request SHA-256 remains `538c009ec230c99af2b7111b4c04b9fb7ff3f38abf48489c48d985796fa2c157`.

## Direct measured result

The identical bounded replay returned 3 matching messages and a non-empty continuation cursor with no connector error, retry, fallback, or Slack mutation. `include_context=false` again prevented surrounding-context hydration, while `response_format=concise` again hydrated each matching message's text plus channel/author/time metadata. No raw message text, result URLs, or pagination cursor is persisted here.

The returned top-3 set was necessarily different from Phase 1: two returned messages had connector-displayed times later than the Phase-1 valid time. That is expected for timestamp-desc search over a mutable Slack channel and is evidence that search results are a live query view, not a durable snapshot.

Phase 1 stored a result digest and basis but did not durably specify the result-key serialization algorithm. Therefore X13 does not claim a hash-comparison proof across wakes. For future auditability, Phase 2 defines its result digest canonicalization explicitly as sorted-key compact UTF-8 JSON over the ordered list of `{channel, display_time}` objects; the raw result keys are not persisted. Phase-2 digest: `0a43b5c63b8ab6c928a033c339639026983ab83dda5ff7c8025124fd622d29f1`.

## Measures

- Custom code avoided: `60–180 LOC`, unvalidated estimate only.
- Operator minutes removed: `0` measured.
- Credentials: connector-managed; effective principal, token type, scopes, and native method remain unexposed.
- Durability: Git receipt durable; Slack search output is mutable and not snapshot evidence.
- Observability: request replay, count, continuation presence, content hydration, and displayed times are visible; native request identity, HTTP/rate headers, scopes, and quota debit are not.
- Portability: low-to-medium; generic search/pagination concepts transfer, Slack query/auth/result semantics do not.
- Failure behavior: two bounded happy-path successes; no permission, empty-success, invalid-cursor, throttling, transient-failure, or native-parity probe yet.
- Direct cost/quota: no debit or billing signal surfaced by the connector.
- Verifier: direct connector receipt + durable request descriptor + Git readback.
- Consumer: discovery candidate only; no downstream consumer acknowledgement.

## Gate / Andon

Do not treat repeated search as snapshot replay. An identical request can legitimately return a different top-N when matching Slack content changes. Also, Phase 1's result-digest serialization was under-specified; Phase 2 fixes that prospectively rather than pretending the historical hash is reproducible.

## Next

Phase 3: one bounded synthetic nonmatching public search, preserving the exact privacy-safe descriptor, with no retry and no workspace-wide absence claim.

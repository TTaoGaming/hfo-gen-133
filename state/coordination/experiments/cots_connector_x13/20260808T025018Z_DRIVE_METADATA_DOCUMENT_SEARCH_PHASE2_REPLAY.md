---
schema_id: hfo.gen133.x13.cots_connector_event.v1
experiment_id: X13_GDRIVE_METADATA_DOCUMENT_SEARCH_READONLY_019
event: PHASE2_IDENTICAL_REPLAY
prior_current_version: 173
candidate: Google_Drive_search_explicit_document_metadata_only
campaign_wake: 2_of_4
phase_status: PHASE2_ACCEPTED_WITH_GATES
wip: 1
candidate_calls_this_wake: 1
candidate_mutations_this_wake: 0
retries_this_wake: 0
fallbacks_this_wake: 0
returned_item_count: 3
content_fetch_requested: false
content_hydration_observed: false
raw_file_ids_persisted_in_receipt: false
raw_file_titles_persisted_in_receipt: false
raw_file_urls_persisted_in_receipt: false
next_page_token_observed_in_connector_surface: false
incomplete_search_field_observed_in_connector_surface: false
request_descriptor_canonicalization: UTF8_JSON_SORTED_KEYS_COMPACT_SEPARATORS_NO_ASCII_ESCAPING
request_descriptor_sha256: 84406b16173dae6290ec193bf45168a1c970fbcf8ef721662ab9038fc0bf88ea
phase1_ordered_result_digest_sha256: 9f3850e25f8d5a27155bd9b77846aca658e6deef834b91905a6c3e95026bc4fb
phase2_result_digest_canonicalization: UTF8_JSON_COMPACT_OVER_ORDERED_LIST_OF_SHA256_FILE_ID_VALUES
phase2_ordered_result_digest_sha256: 9f3850e25f8d5a27155bd9b77846aca658e6deef834b91905a6c3e95026bc4fb
ordered_result_digest_match_phase1: true
operator_minutes_removed_measured: 0
custom_code_avoided_estimate: 50_to_140_LOC_UNVALIDATED
paid_cost_usd_observed: 0_NO_CHARGE_SURFACED_NOT_BILLING_PROOF
direct_cost_or_quota_evidence: CONNECTOR_DID_NOT_SURFACE_PROVIDER_QUOTA_DEBIT
credentials: CONNECTOR_MANAGED_EFFECTIVE_PRINCIPAL_AND_OAUTH_SCOPES_UNKNOWN
durability: GIT_OBSERVATION_RECEIPT_DURABLE;MATCHED_ORDERED_RESULT_DIGEST_REPEATED_OVER_SHORT_INTERVAL;DRIVE_SEARCH_RESULT_REMAINS_A_MUTABLE_QUERY_VIEW_NOT_A_SNAPSHOT
observability: RESULT_COUNT_AND_METADATA_ITEMS_VISIBLE;PROVIDER_REQUEST_ID_HTTP_STATUS_RATE_HEADERS_EFFECTIVE_SCOPE_NATIVE_METHOD_INCOMPLETE_SEARCH_AND_ACTUAL_QUOTA_DEBIT_NOT_SURFACED
portability: MEDIUM_GENERIC_METADATA_SEARCH_PORTABLE;GOOGLE_DRIVE_QUERY_MIME_CORPUS_AND_AUTHORIZATION_SEMANTICS_PROVIDER_SPECIFIC
failure_behavior: TWO_IDENTICAL_BOUNDED_READONLY_METADATA_SEARCHES_SUCCEEDED_WITH_MATCHING_ORDERED_HASHED_ID_DIGESTS;NO_EMPTY_PERMISSION_PAGINATION_INCOMPLETE_SEARCH_RATE_LIMIT_TRANSIENT_OR_NATIVE_PARITY_TESTED
connector_variance_probe: IDENTICAL_REPLAY_MATCHED_ORDERED_RESULTS_OVER_SHORT_INTERVAL;ITEM_TYPE_DOCUMENT_REMAINS_BROADER_THAN_GOOGLE_DOCS_MIME_ONLY
verifier: DIRECT_GOOGLE_DRIVE_CONNECTOR_RECEIPT_PLUS_DURABLE_MATCHED_REQUEST_AND_RESULT_DIGESTS_PLUS_GITHUB_IMMUTABLE_EVENT_AND_CURRENT_READBACK
consumer: HFO_COMMAND_AND_CONTROL_DISCOVERY_CANDIDATE_NO_DOWNSTREAM_CONSUMER_ACK
adoption_credit: 0
fitness_credit: 0
mandatory_gate: READONLY_METADATA_SEARCH_ONLY;EXPLICIT_ITEM_TYPE_REQUIRED_TO_AVOID_LEGACY_OPTIONAL_BEST_EFFORT_TEXT_HYDRATION;BEST_EFFORT_FETCH_FALSE;SMALL_EXPLICIT_TOPN;DO_NOT_PERSIST_RAW_FILE_IDS_TITLES_URLS_PARENT_IDS_OR_PAGE_TOKENS_IN_X13_RECEIPTS;DO_NOT_TREAT_ITEM_TYPE_DOCUMENT_AS_GOOGLE_DOCS_MIME_ONLY;MATCHED_SHORT_INTERVAL_REPLAY_IS_NOT_SNAPSHOT_DURABILITY_OR_COMPLETENESS_PROOF;DO_NOT_INFER_COMPLETENESS_FROM_ABSENCE_OF_A_VISIBLE_PAGE_TOKEN_WHEN_WRAPPER_DOES_NOT_EXPOSE_PROVIDER_INCOMPLETE_SEARCH_OR_NATIVE_PARITY;NO_UNBOUNDED_RETRY;PROVIDER_ERRORS_FAIL_CLOSED;NO_CONSEQUENTIAL_COMPLETENESS_OR_AUTHORIZATION_CLAIM_FROM_SEARCH_ONLY
strongest_falsifier: A_MATCHED_PROVIDER_DIRECT_DRIVE_V3_FILES_LIST_UNDER_THE_SAME_EFFECTIVE_PRINCIPAL_AND_EQUIVALENT_QUERY_MATERIALLY_DISAGREES_ON_ACCESSIBLE_METADATA_RESULTS_OR_THE_WRAPPER_FETCHES_FILE_CONTENT_DESPITE_EXPLICIT_ITEM_TYPE_DOCUMENT_AND_BEST_EFFORT_FETCH_FALSE
honest_flaw: TWO_HAPPY_PATH_CALLS_ONLY;MATCHING_SHORT_INTERVAL_ORDERED_DIGEST_DOES_NOT_ESTABLISH_SNAPSHOT_SEMANTICS;NO_EMPTY_SUCCESS_PERMISSION_DENIAL_PAGINATION_REPLAY_INCOMPLETE_SEARCH_SHARED_DRIVE_VARIANCE_RATE_LIMIT_TRANSIENT_FAILURE_NATIVE_PARITY_EFFECTIVE_SCOPE_ACTUAL_QUOTA_DEBIT_OPERATOR_SAVINGS_OR_DOWNSTREAM_CONSUMER_VALUE_TESTED
valid_time_utc: 2026-08-08T02:50:18Z
recorded_time_utc: 2026-08-08T02:50:18Z
---

# X13 Phase 2 — Google Drive metadata search identical replay

## Surface → owner → permission

- Surface: `Google_Drive.search` with the exact durable Phase-1 request descriptor.
- Owner: Google Drive connector / Google Drive provider surface; X13 owns only experiment receipts.
- Permission: operator authorized bounded read-only connector experiments and Git-first receipts. No Drive mutation, account action, send, spend, merge, deployment, deletion, or task mutation occurred.

## Exact replay request

Canonical JSON:

```json
{"best_effort_fetch":false,"item_type":"document","page_token":null,"query":"HFO","require_viewed_by_user":false,"special_filter_query_str":"","topn":3}
```

Request SHA-256: `84406b16173dae6290ec193bf45168a1c970fbcf8ef721662ab9038fc0bf88ea` — identical to Phase 1.

## Direct observation

One bounded replay returned 3 metadata results. No content fetch was requested; no file-body/text hydration, Drive mutation, retry, or fallback was observed. Raw file IDs, titles, URLs, parent IDs, and any provider-owned cursor values are intentionally omitted from this receipt.

Using the Phase-1 canonical result algorithm — SHA-256 each ordered file ID, serialize the ordered list as compact UTF-8 JSON, then SHA-256 that JSON — the Phase-2 result digest is:

`9f3850e25f8d5a27155bd9b77846aca658e6deef834b91905a6c3e95026bc4fb`

This exactly matches the Phase-1 ordered digest. That is evidence of short-interval repeatability for this exact request and observed accessible top-3 ordering. It is not evidence of snapshot durability, completeness, provider-native parity, or future stability because Drive is a mutable search view.

The wrapper again did not expose provider request ID, HTTP status, rate-limit headers, effective OAuth principal/scopes, native Drive method, Drive `incompleteSearch`, or actual quota debit. No visible continuation token was observed; that absence is not promoted to a completeness claim.

## Measures

| Measure | Phase 2 | Campaign |
|---|---:|---:|
| bounded read-only connector calls | 1 | 2 |
| returned metadata items | 3 | 6 observed across calls |
| content fetch requested | 0 | 0 |
| content hydration observed | 0 | 0 |
| mutations / retries / fallbacks | 0 / 0 / 0 | 0 / 0 / 0 |
| ordered result digest matches Phase 1 | yes | yes |
| operator minutes removed | 0 measured | 0 measured |
| custom code avoided | 50–140 LOC, unvalidated | unchanged |
| actual provider quota debit | unknown | unknown |
| adoption / fitness credit | 0 / 0 | 0 / 0 |

## Strongest falsifier

A matched provider-direct Drive v3 `files.list` under the same effective principal and equivalent query materially disagrees on the accessible metadata result set without intervening Drive/index changes, or this explicit metadata-only mode fetches file content despite `item_type=document` and `best_effort_fetch=false`.

## Honest flaw

Two happy-path calls are still weak evidence. Matching ordered results over a short interval does not test permission denial, empty-success semantics, pagination, `incompleteSearch`, shared-drive/corpus variance, rate limiting, transient failure, native parity, effective OAuth scope, actual quota debit, measured operator savings, or downstream consumer value.

## Next

Phase 3: one bounded synthetic nonmatching metadata-only Drive search with the exact privacy-safe request descriptor persisted before interpretation. Test empty-success/error distinction only; no content fetch, no pagination replay, no Drive mutation, and no corpus-wide absence claim.

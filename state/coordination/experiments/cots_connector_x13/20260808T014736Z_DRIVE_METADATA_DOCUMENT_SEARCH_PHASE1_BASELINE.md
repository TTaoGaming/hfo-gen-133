---
schema_id: hfo.gen133.x13.cots_connector_event.v1
experiment_id: X13_GDRIVE_METADATA_DOCUMENT_SEARCH_READONLY_019
event: PHASE1_BASELINE
prior_current_version: 172
candidate: Google_Drive_search_explicit_document_metadata_only
campaign_wake: 1_of_4
phase_status: PHASE1_ACCEPTED_WITH_GATES
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
result_digest_canonicalization: UTF8_JSON_COMPACT_OVER_ORDERED_LIST_OF_SHA256_FILE_ID_VALUES
ordered_result_digest_sha256: 9f3850e25f8d5a27155bd9b77846aca658e6deef834b91905a6c3e95026bc4fb
operator_minutes_removed_measured: 0
custom_code_avoided_estimate: 50_to_140_LOC_UNVALIDATED
paid_cost_usd_observed: 0_NO_CHARGE_SURFACED_NOT_BILLING_PROOF
direct_cost_or_quota_evidence: CONNECTOR_DID_NOT_SURFACE_PROVIDER_QUOTA_DEBIT
credentials: CONNECTOR_MANAGED_EFFECTIVE_PRINCIPAL_AND_OAUTH_SCOPES_UNKNOWN
durability: GIT_OBSERVATION_RECEIPT_DURABLE;DRIVE_SEARCH_RESULT_IS_A_MUTABLE_QUERY_VIEW_NOT_A_SNAPSHOT
observability: RESULT_COUNT_AND_METADATA_ITEMS_VISIBLE;PROVIDER_REQUEST_ID_HTTP_STATUS_RATE_HEADERS_EFFECTIVE_SCOPE_NATIVE_METHOD_INCOMPLETE_SEARCH_AND_ACTUAL_QUOTA_DEBIT_NOT_SURFACED
portability: MEDIUM_GENERIC_METADATA_SEARCH_AND_CURSOR_PAGINATION_PORTABLE;GOOGLE_DRIVE_QUERY_MIME_AND_AUTHORIZATION_SEMANTICS_PROVIDER_SPECIFIC
failure_behavior: ONE_BOUNDED_READONLY_METADATA_SEARCH_SUCCEEDED_WITH_3_ITEMS;NO_FAILURE_MODE_TESTED
connector_variance_probe: EXPLICIT_ITEM_TYPE_DOCUMENT_PREVENTED_CONTENT_FETCH_BUT_DID_NOT_MEAN_GOOGLE_DOCS_MIME_ONLY;AT_LEAST_ONE_RESULT_SURFACED_AS_A_GOOGLE_SHEETS_URL
verifier: DIRECT_GOOGLE_DRIVE_CONNECTOR_RECEIPT_PLUS_OFFICIAL_GOOGLE_DRIVE_V3_DOCS_PLUS_GITHUB_IMMUTABLE_EVENT_READBACK
consumer: HFO_COMMAND_AND_CONTROL_DISCOVERY_CANDIDATE_NO_DOWNSTREAM_CONSUMER_ACK
adoption_credit: 0
fitness_credit: 0
mandatory_gate: READONLY_METADATA_SEARCH_ONLY;EXPLICIT_ITEM_TYPE_REQUIRED_TO_AVOID_LEGACY_BEST_EFFORT_TEXT_HYDRATION;BEST_EFFORT_FETCH_FALSE;SMALL_EXPLICIT_TOPN;DO_NOT_PERSIST_RAW_FILE_IDS_TITLES_URLS_OR_PAGE_TOKENS_IN_X13_RECEIPTS;DO_NOT_TREAT_ITEM_TYPE_DOCUMENT_AS_GOOGLE_DOCS_MIME_ONLY;DO_NOT_INFER_COMPLETENESS_WHEN_WRAPPER_DOES_NOT_SURFACE_INCOMPLETE_SEARCH_OR_PROVIDER_NATIVE_PARITY;NO_UNBOUNDED_RETRY;PROVIDER_ERRORS_FAIL_CLOSED
strongest_falsifier: A_MATCHED_PROVIDER_DIRECT_DRIVE_V3_FILES_LIST_UNDER_THE_SAME_EFFECTIVE_PRINCIPAL_AND_EQUIVALENT_QUERY_MATERIALLY_DISAGREES_ON_ACCESSIBLE_METADATA_RESULTS_OR_THE_WRAPPER_FETCHES_FILE_CONTENT_DESPITE_EXPLICIT_ITEM_TYPE_DOCUMENT_AND_BEST_EFFORT_FETCH_FALSE
honest_flaw: SINGLE_HAPPY_PATH_CALL_ONLY;NO_EMPTY_SUCCESS_PERMISSION_DENIAL_PAGINATION_REPLAY_INCOMPLETE_SEARCH_SHARED_DRIVE_VARIANCE_RATE_LIMIT_TRANSIENT_FAILURE_NATIVE_PARITY_EFFECTIVE_SCOPE_ACTUAL_QUOTA_DEBIT_OPERATOR_SAVINGS_OR_CONSUMER_VALUE_TESTED
valid_time_utc: 2026-08-08T01:47:36Z
recorded_time_utc: 2026-08-08T01:47:36Z
---

# X13 Phase 1 — Google Drive explicit document metadata-only search

## Surface → owner → permission

- Surface: `Google_Drive.search` with explicit `item_type=document`.
- Owner: Google Drive connector / Google Drive API provider surface; X13 owns only the experiment receipts.
- Permission: operator authorized bounded read-only connector experiments and Git-first receipts. No Drive mutation, account action, send, spend, merge, deployment, deletion, or task mutation occurred.

## Exact privacy-safe request descriptor

Canonical JSON before SHA-256:

```json
{"best_effort_fetch":false,"item_type":"document","page_token":null,"query":"HFO","require_viewed_by_user":false,"special_filter_query_str":"","topn":3}
```

Request SHA-256: `84406b16173dae6290ec193bf45168a1c970fbcf8ef721662ab9038fc0bf88ea`.

## Direct observation

One bounded call returned 3 metadata results. No content fetch was requested and no file-body/text hydration was observed. The wrapper surfaced titles, IDs, URLs, display metadata, and parent IDs for results, so it is metadata-only rather than identifier-only. Raw file IDs, titles, URLs, parent IDs, or page tokens are intentionally not copied into this receipt.

A connector-specific semantic was observed: explicit `item_type=document` did not mean Google Docs MIME type only; at least one returned result surfaced as a Google Sheets URL. Treat `item_type=document` as the wrapper's broad document-class selector unless provider-native MIME filtering is supplied separately.

The direct connector surface did not expose a provider request ID, HTTP status, rate-limit headers, effective OAuth principal/scopes, native Drive method name, Drive `incompleteSearch`, or an actual quota-unit debit. Absence of a visible `next_page_token` in this response is not proof that a matched provider-native query has no additional results.

## Official contract baseline

Primary documentation checked 2026-08-08:

- Drive API v3 `files.list`: https://developers.google.com/workspace/drive/api/reference/rest/v3/files/list
- Search guide: https://developers.google.com/workspace/drive/api/guides/search-files
- Usage limits: https://developers.google.com/workspace/drive/api/guides/limits

Google documents `files.list` as the v3 list/search method, with `q` filtering, `pageSize`/`pageToken` pagination, `nextPageToken`, and an `incompleteSearch` flag. It also documents multiple acceptable OAuth scopes including metadata-read-only and drive-read-only scopes. The search guide says default `files.list` fields are metadata fields (`kind`, `id`, `name`, `mimeType`, `resourceKey`) unless different fields are requested. Google also warns that an `allDrives` search can be incomplete and clients should inspect `incompleteSearch`.

As of the May 1, 2026 quota model, Google's usage-limit page documents list operations such as `files.list` at 100 quota units/request and a 400,000,000 quota-unit/day/project threshold before future billing semantics may apply. X13 has no evidence that this connector call maps one-for-one to one native `files.list`, and the connector surfaced no actual debit.

## Measures

| Measure | Phase 1 |
|---|---:|
| bounded read-only connector calls | 1 |
| returned metadata items | 3 |
| content fetch requested | 0 |
| content hydration observed | 0 |
| mutations / retries / fallbacks | 0 / 0 / 0 |
| operator minutes removed | 0 measured |
| custom code avoided | 50–140 LOC, unvalidated |
| actual provider quota debit | unknown |
| adoption / fitness credit | 0 / 0 |

## Strongest falsifier

A matched provider-direct Drive v3 `files.list` under the same effective principal and equivalent query materially disagrees on the accessible metadata result set without intervening Drive/index changes, or this explicit metadata-only mode fetches file content despite `item_type=document` and `best_effort_fetch=false`.

## Honest flaw

This is one happy-path call. Empty-success semantics, permission denial, pagination replay, `incompleteSearch`, shared-drive/corpus variance, rate limiting, transient failure, native parity, effective OAuth scope, actual quota debit, measured operator savings, and acknowledged consumer value remain untested.

## Next

Phase 2: identical bounded replay from the durable descriptor and compare the ordered hashed-ID digest. No content fetch, no page-token replay, no Drive mutation.

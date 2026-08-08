---
schema_id: hfo.gen133.x13.cots_connector_event.v1
experiment_id: X13_GDRIVE_METADATA_DOCUMENT_SEARCH_READONLY_019
event: PHASE3_SYNTHETIC_NONMATCH_EMPTY_SUCCESS
prior_current_version: 174
candidate: Google_Drive_search_explicit_document_metadata_only
campaign_wake: 3_of_4
phase_status: PHASE3_ACCEPTED_WITH_GATES
wip: 1
candidate_calls_this_wake: 1
candidate_mutations_this_wake: 0
retries_this_wake: 0
fallbacks_this_wake: 0
returned_item_count: 0
connector_error_observed: false
connector_error_field: null
external_call_time_ms: 684
content_fetch_requested: false
content_hydration_observed: false
raw_file_ids_persisted_in_receipt: false
raw_file_titles_persisted_in_receipt: false
raw_file_urls_persisted_in_receipt: false
next_page_token_observed_in_connector_surface: false
incomplete_search_field_observed_in_connector_surface: false
request_descriptor_canonicalization: UTF8_JSON_SORTED_KEYS_COMPACT_SEPARATORS_NO_ASCII_ESCAPING
request_descriptor_sha256: 2291d90a3e3471e03f4e5ee555aa25ddb46ef56c8e07fc9506f459ef5fe7371c
synthetic_query_contains_user_data: false
empty_success_observed_distinct_from_error: true
operator_minutes_removed_measured: 0
custom_code_avoided_estimate: 50_to_140_LOC_UNVALIDATED
paid_cost_usd_observed: 0_NO_CHARGE_SURFACED_NOT_BILLING_PROOF
direct_cost_or_quota_evidence: CONNECTOR_DID_NOT_SURFACE_PROVIDER_QUOTA_DEBIT;OFFICIAL_DRIVE_API_V3_FILES_LIST_DOCUMENTED_AT_100_QUOTA_UNITS_PER_REQUEST_IF_NATIVE_MAPPING_IS_FILES_LIST;ACTUAL_CONNECTOR_MAPPING_AND_DEBIT_UNKNOWN
credentials: CONNECTOR_MANAGED_EFFECTIVE_PRINCIPAL_AND_OAUTH_SCOPES_UNKNOWN;OFFICIAL_FILES_LIST_ACCEPTS_MULTIPLE_SCOPES_INCLUDING_DRIVE_METADATA_READONLY_AND_DRIVE_READONLY
durability: GIT_OBSERVATION_RECEIPT_DURABLE;PHASE1_PHASE2_SHORT_INTERVAL_ORDERED_DIGEST_REPEATABILITY_RETAINED;PHASE3_EMPTY_SUCCESS_IS_AN_OBSERVATION_NOT_CORPUS_SNAPSHOT_OR_COMPLETENESS_PROOF
observability: EMPTY_RESULT_ARRAY_AND_NULL_CONNECTOR_ERROR_VISIBLE;EXTERNAL_CALL_TIME_VISIBLE;PROVIDER_REQUEST_ID_HTTP_STATUS_RATE_HEADERS_EFFECTIVE_SCOPE_NATIVE_METHOD_INCOMPLETE_SEARCH_AND_ACTUAL_QUOTA_DEBIT_NOT_SURFACED
portability: MEDIUM_GENERIC_METADATA_SEARCH_AND_EMPTY_SUCCESS_SEMANTICS_PORTABLE;GOOGLE_DRIVE_QUERY_MIME_CORPUS_SHARED_DRIVE_AND_AUTHORIZATION_SEMANTICS_PROVIDER_SPECIFIC
failure_behavior: SYNTHETIC_NONMATCH_RETURNED_EMPTY_SUCCESS_WITH_NULL_CONNECTOR_ERROR_AND_NO_RETRY_OR_FALLBACK;PERMISSION_DENIAL_INVALID_CURSOR_RATE_LIMIT_TRANSIENT_FAILURE_INCOMPLETE_SEARCH_SHARED_DRIVE_AND_NATIVE_PARITY_NOT_TESTED
connector_variance_probe: WRAPPER_REPRESENTS_EMPTY_SUCCESS_AS_EMPTY_RESULTS_WITHOUT_ERROR;WRAPPER_STILL_DOES_NOT_SURFACE_NATIVE_NEXT_PAGE_TOKEN_INCOMPLETE_SEARCH_HTTP_STATUS_REQUEST_ID_SCOPE_OR_QUOTA_FIELDS
verifier: DIRECT_GOOGLE_DRIVE_CONNECTOR_RECEIPT_PLUS_EXACT_DURABLE_SYNTHETIC_REQUEST_DESCRIPTOR_PLUS_OFFICIAL_GOOGLE_DRIVE_V3_DOCS_PLUS_GITHUB_IMMUTABLE_EVENT_AND_CURRENT_READBACK
consumer: HFO_COMMAND_AND_CONTROL_DISCOVERY_CANDIDATE_NO_DOWNSTREAM_CONSUMER_ACK
adoption_credit: 0
fitness_credit: 0
mandatory_gate: READONLY_METADATA_SEARCH_ONLY;EXPLICIT_ITEM_TYPE_REQUIRED_TO_AVOID_LEGACY_OPTIONAL_BEST_EFFORT_TEXT_HYDRATION;BEST_EFFORT_FETCH_FALSE;SMALL_EXPLICIT_TOPN;DO_NOT_PERSIST_RAW_FILE_IDS_TITLES_URLS_PARENT_IDS_OR PAGE_TOKENS_IN_X13_RECEIPTS;DO_NOT_TREAT_ITEM_TYPE_DOCUMENT_AS_GOOGLE_DOCS_MIME_ONLY;EMPTY_SUCCESS_IS_NOT_CORPUS_WIDE_ABSENCE_COMPLETENESS_AUTHORIZATION_OR_INDEX_FRESHNESS_PROOF;DO_NOT_INFER_COMPLETENESS_FROM_ABSENCE_OF_A_VISIBLE_PAGE_TOKEN_WHEN_WRAPPER_DOES_NOT_EXPOSE_PROVIDER_INCOMPLETE_SEARCH_OR_NATIVE_PARITY;NO_UNBOUNDED_RETRY;PROVIDER_ERRORS_FAIL_CLOSED;NO_CONSEQUENTIAL_COMPLETENESS_OR AUTHORIZATION_CLAIM_FROM_SEARCH_ONLY
strongest_falsifier: A_MATCHED_PROVIDER_DIRECT_DRIVE_V3_FILES_LIST_UNDER_THE_SAME_EFFECTIVE_PRINCIPAL_AND_EQUIVALENT_QUERY_MATERIALLY_DISAGREES_ON_ACCESSIBLE_METADATA_RESULTS_UNDER_QUIESCENT_STATE_OR_THE_WRAPPER_FETCHES_FILE_CONTENT_DESPITE_EXPLICIT_ITEM_TYPE_DOCUMENT_AND_BEST_EFFORT_FETCH_FALSE
honest_flaw: THREE_CALLS_TOTAL_WITH_NO_OBSERVED_ERRORS;PHASE3_TESTED_ONLY_SYNTHETIC_EMPTY_SUCCESS_NOT_PERMISSION_DENIAL_INVALID_CURSOR_RATE_LIMIT_TRANSIENT_FAILURE_INCOMPLETE_SEARCH_SHARED_DRIVE_NATIVE_PARITY_EFFECTIVE_SCOPE_ACTUAL_QUOTA_DEBIT_OPERATOR_SAVINGS_OR_DOWNSTREAM_CONSUMER_VALUE
next_phase: PHASE4_DECIDE_FROM_FROZEN_THREE_CALL_EVIDENCE_SET_NO_ADDITIONAL_DRIVE_CANDIDATE_CALL
valid_time_utc: 2026-08-08T03:48:00Z
recorded_time_utc: 2026-08-08T03:48:00Z
---

# X13 Phase 3 — Google Drive metadata search empty-success probe

## Surface → owner → permission

- Surface: `Google_Drive.search` with explicit `item_type=document`, `topn=3`, `best_effort_fetch=false`, `require_viewed_by_user=false`, and one synthetic nonmatching query.
- Owner: Google Drive connector / Google Drive provider surface; X13 owns only experiment receipts.
- Permission: operator authorized bounded read-only connector experiments and Git-first receipts. No Drive mutation, account action, send, spend, merge, deployment, deletion, secret exposure, or task mutation occurred.

## Exact privacy-safe request

Canonical JSON of the exact arguments sent:

```json
{"action":"Google_Drive.search","best_effort_fetch":false,"item_type":"document","query":"X13_SYNTHETIC_NONMATCH_20260808_0348Z_7F2C91","require_viewed_by_user":false,"topn":3}
```

Request SHA-256: `2291d90a3e3471e03f4e5ee555aa25ddb46ef56c8e07fc9506f459ef5fe7371c`.

The query is synthetic and contains no mailbox, Drive-title, file-ID, URL, or user-derived data.

## Direct observation

One bounded call returned an empty result array. The connector surfaced no error, error code, retry, fallback, mutation, or content hydration. Connector external call time was 684 ms. No file contents were requested or fetched.

This establishes only that this wrapper can represent one synthetic nonmatching bounded search as an **empty success distinct from an observed connector error state**. It does not establish that the Drive corpus has no matching item outside the connector's effective accessible/searchable corpus, that authorization is complete, that indexing is fresh, or that a provider-native `files.list` call would expose identical status fields.

The wrapper again did not surface provider request ID, HTTP status, rate-limit headers, effective OAuth principal/scopes, native Drive method, provider `nextPageToken`, provider `incompleteSearch`, or actual quota debit.

## Official contract cross-check

Google Drive v3 `files.list` documents a paginated `files[]` response plus `nextPageToken` and `incompleteSearch`. It explicitly says `incompleteSearch=true` means some results might be missing and clients should narrow the corpus. It also documents multiple eligible OAuth scopes, including `drive.metadata.readonly` and `drive.readonly`.

Google's usage-limit page, updated 2026-07-31, documents list operations such as `files.list` at 100 quota units/request under the post-2026-05-01 model, a 400,000,000 quota-unit/day/project billing threshold, and potential `403` or `429` quota/rate-limit responses. Because this connector does not expose its provider-native mapping or project, those numbers are contract context, not proof of this call's actual debit.

## Measures

| Measure | Phase 3 | Campaign |
|---|---:|---:|
| bounded read-only connector calls | 1 | 3 |
| nonempty successes | 0 | 2 |
| empty successes | 1 | 1 |
| observed connector errors | 0 | 0 |
| content fetches / hydration | 0 / 0 | 0 / 0 |
| mutations / retries / fallbacks | 0 / 0 / 0 | 0 / 0 / 0 |
| operator minutes removed | 0 measured | 0 measured |
| custom code avoided | 50–140 LOC, unvalidated | unchanged |
| actual provider quota debit | unknown | unknown |
| adoption / fitness credit | 0 / 0 | 0 / 0 |

## Strongest falsifier

A matched provider-direct Drive v3 `files.list` under the same effective principal and equivalent query materially disagrees on the accessible metadata result set under a quiescent Drive/index state, or this explicit metadata-only mode fetches file content despite `item_type=document` and `best_effort_fetch=false`.

## Honest flaw

Three calls remain weak evidence. Phase 3 tested only one synthetic empty-success path. Permission denial, invalid cursor, pagination replay, `incompleteSearch`, shared-drive/corpus variance, rate limiting, transient provider failure, native parity, effective OAuth scope, actual quota debit, measured operator savings, and downstream consumer value remain untested.

## Next

Phase 4: decide `ADOPT | ADOPT_WITH_GATES | DEFER | REJECT | UNKNOWN` from the frozen three-call evidence set. No additional Drive candidate call.

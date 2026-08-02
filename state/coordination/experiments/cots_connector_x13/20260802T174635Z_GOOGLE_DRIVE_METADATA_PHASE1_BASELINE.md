---
schema_id: hfo.gen133.x13.cots_connector_event.v1
experiment_id: X13_GOOGLE_DRIVE_BOUNDED_METADATA_SEARCH_READONLY_001
event_type: PHASE1_OFFICIAL_CONTRACT_AND_DIRECT_BASELINE
candidate: Google_Drive_bounded_metadata_only_search_connector_surface
phase: 1_of_4
phase_result: ACCEPTED_WITH_SCOPE_CORPUS_COMPLETENESS_AND_QUOTA_GATES
expected_current_version: 44
next_current_version: 45
carrier_task_id: 6a55c1733708819185088bf334e33ea5
carrier_task_id_match: true
wip: 1
valid_time_utc: 2026-08-02T17:46:35Z
transaction_time_utc: SEE_GIT_COMMIT_METADATA
sealed: true
---

# X13 Google Drive metadata-only search — phase 1

## Official contract baseline

Primary references checked on 2026-08-02:

- `files.list`: https://developers.google.com/workspace/drive/api/reference/rest/v3/files/list
- Search guide: https://developers.google.com/workspace/drive/api/guides/search-files
- Query terms and operators: https://developers.google.com/workspace/drive/api/guides/ref-search-terms
- Usage limits: https://developers.google.com/workspace/drive/api/guides/limits

Contract facts admitted:

- `files.list` is a read operation over file resources and accepts `q`, `pageSize`, and `pageToken`.
- The service may return fewer results than the requested page size.
- A populated `nextPageToken` means the returned page may be incomplete; rejected tokens must be discarded and listing restarted.
- Page tokens are typically valid for several hours, but result membership can change when items are added or removed.
- `incompleteSearch=true` means some results might be missing, especially across broad corpora; callers should narrow the corpus.
- Default `files.list` fields are metadata (`kind`, `id`, `name`, `mimeType`, `resourceKey`) unless other fields are requested. File content requires a separate content/export/download operation.
- `files.list` can be authorized by multiple scopes ranging from metadata-read-only to broad Drive access; a successful connector call does not identify the live scope.
- Current published new-model usage is 100 quota units for a list operation, 1,000,000 units/minute/project, 325,000 units/minute/user/project, and a 400,000,000-unit daily billing threshold. Projects active before the May 1, 2026 transition may retain prior quotas. Live project class and counters were not exposed.

## Direct connector baseline

One bounded provider-page metadata search was executed:

```yaml
query_class: short_specific_keyword
query_value_persisted: HFO
item_type: document
topn: 3
provider_page_count: 1
best_effort_fetch: false
require_viewed_by_user: false
page_token_supplied: false
returned_result_count: 3
next_page_token_visible: false
file_content_or_text_hydration_returned: false
exact_file_ids_titles_urls_parent_ids_persisted_in_event: false
write_side_effect: false
connector_failure: null
connector_latency_ms: NOT_EXPOSED
carrier_retry_count: 0
surfaced_cost_usd: 0
operator_minutes_removed_measured: 0
```

The connector returned metadata sufficient to identify three matching accessible items. It also surfaced metadata fields broader than the minimal default `files.list` response, including URLs and parent identifiers. No file body, spreadsheet cells, document text, download, export, or mutation was requested or observed.

## Measurements

```yaml
custom_code_avoided_estimate:
  authenticated_list_query_and_metadata_normalization: 30_to_100_LOC_UNVALIDATED
  page_token_corpus_and_error_handling: 20_to_70_LOC_UNVALIDATED_NON_ADDITIVE
operator_minutes_removed_measured: 0
operator_minutes_removed_estimate_per_bounded_discovery: 1_to_5_UNVALIDATED
credentials:
  connector_authenticated_search_succeeded: true
  authenticated_user_identity: UNKNOWN
  live_oauth_scope: UNKNOWN
  oauth_client_or_project: UNKNOWN
  credential_custody: UNKNOWN
  least_privilege_closed: false
durability: EPHEMERAL_POINT_IN_TIME_METADATA_OBSERVATION_OVER_MUTABLE_DRIVE_INDEX
observability: MEDIUM_LOW_RESULT_METADATA_AND_COUNT_VISIBLE_BUT_RAW_HTTP_CORPUS_INCOMPLETE_SEARCH_SCOPE_PROJECT_REQUEST_ID_QUOTA_RETRIES_AND_LATENCY_HIDDEN
portability: MEDIUM_LOW_QUERY_SYNTAX_FILE_IDS_PARENT_IDS_RESOURCE_KEYS_SHARED_DRIVE_SEMANTICS_AND_PAGE_TOKENS_ARE_PROVIDER_SPECIFIC
failure_behavior: NOT_PROBED_IN_PHASE1
paid_cost_usd_observed: 0_NO_CHARGE_SURFACED
actual_upstream_request_count: UNKNOWN
actual_quota_units_consumed: UNKNOWN
billing_state: UNKNOWN
verifier: RAW_GOOGLE_DRIVE_FILES_LIST_OR_DISTINCT_AUTHORIZED_CLIENT_WITH_SOURCE_BOUND_ACCOUNT_EXACT_QUERY_FIELDS_CORPUS_AND_PAGE_SIZE
consumer:
  - HFO_BOUNDED_FILE_DISCOVERY
  - HFO_HERITAGE_AND_PARA_ROUTING_WITH_SEPARATE_CONTENT_AUTHORIZATION
strongest_falsifier: A_SOURCE_BOUND_RAW_CLIENT_RETURNS_MATERIALLY_DIFFERENT_MEMBERSHIP_OR_SHOWS_THE_CONNECTOR_HYDRATED_FILE_CONTENT_OR_MUTATED_DRIVE_STATE
honest_flaw: ONE_KEYWORD_ONE_PAGE_THREE_RESULTS_ONLY_NO_EMPTY_QUERY_PAGINATION_SHARED_DRIVE_CORPUS_INCOMPLETE_SEARCH_PERMISSION_DENIAL_INVALID_TOKEN_RATE_LIMIT_IDENTITY_SCOPE_INDEPENDENT_READBACK_OR_CONSUMER_ACK
```

## Gates established

- Keep `best_effort_fetch=false` and an explicit metadata-only `item_type` for admitted discovery calls.
- Use a small explicit `topn`; one page is not completeness.
- Treat titles, IDs, URLs, parent IDs, resource keys, and folder relationships as potentially sensitive metadata.
- Do not persist exact file metadata unless the consumer requires it and retention is justified.
- Do not infer account identity, OAuth scope, ownership, write authority, corpus, shared-drive coverage, or billing state from success.
- Treat absent `next_page_token` only as a property of this connector response, not proof that the search space was complete.
- Require visibility of `incompleteSearch` or an equivalent completeness signal before making completeness claims.
- No content hydration, download, export, spreadsheet row read, file creation, update, move, rename, upload, permission change, sharing, ownership transfer, Trash, or deletion.

## Phase disposition

`PHASE1_ACCEPTED_WITH_SCOPE_CORPUS_COMPLETENESS_AND_QUOTA_GATES`

Next bounded wake: repeat the same metadata-only search with `topn=1` to test continuation-token emission and result-cap behavior. Do not fetch the next page and do not persist returned metadata or token values.

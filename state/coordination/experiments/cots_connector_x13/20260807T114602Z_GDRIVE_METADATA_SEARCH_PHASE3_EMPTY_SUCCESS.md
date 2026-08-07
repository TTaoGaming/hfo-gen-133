---
schema_id: hfo.gen133.x13.cots_connector_event.v1
experiment_id: X13_GDRIVE_METADATA_SEARCH_READONLY_015
phase: 3
status: PHASE3_ACCEPTED_WITH_GATES
candidate: Google_Drive_metadata_only_document_search
wip: 1
prior_current_version: 158
candidate_calls_this_wake: 1
campaign_calls_total: 3
read_only: true
candidate_mutations: 0
retries: 0
fallbacks: 0
query_class: bounded_synthetic_nonmatching_document_metadata_search
result_limit: 3
results_returned: 0
empty_success_observed: true
connector_error_observed: false
connector_error_field: NULL
connector_error_code_field: NULL
connector_http_status_field: NULL
connector_call_time_ms: 1129
content_hydration_requested: false
content_hydration_observed: false
raw_drive_ids_urls_titles_parent_ids_persisted_in_receipt: false
synthetic_probe_token_persisted_in_receipt: false
phase3_request_digest_sha256: 973cb9c2a7816e976180d8eee8b94e02801d315918d937e1a1b58cd37c600d2b
phase3_normalized_empty_result_shape_digest_sha256: dae25c8cdb5f678700acae1a8b6d062aaf97900fa5e663058e80ef395a9364dc
next_page_token_observability: NOT_SURFACED_IN_EMPTY_RETURN
incomplete_search_observability: NOT_SURFACED_IN_RETURN
provider_request_id_observability: NOT_SURFACED
effective_identity_and_scopes: UNKNOWN_CONNECTOR_MANAGED
operator_minutes_removed_measured: 0
custom_code_avoided_estimate: 50_to_150_LOC_UNVALIDATED
paid_cost_usd_observed: 0_NO_PAID_COST_SURFACED_BY_CONNECTOR
direct_cost_or_quota_evidence: NONE_FROM_CONNECTOR
provider_contract_quota: FILES_LIST_100_QUOTA_UNITS_AS_OF_2026_08_07
provider_contract_quota_regime_actual: UNKNOWN_CONNECTOR_PROJECT_MAY_BE_GRANDFATHERED_IF_USED_NOV2025_TO_APR2026
credentials: CONNECTOR_MANAGED_EFFECTIVE_PRINCIPAL_AND_SCOPE_UNKNOWN
durability: GIT_RECEIPT_DURABLE;DRIVE_SEARCH_VIEW_MUTABLE
observability: EMPTY_SUCCESS_DISTINGUISHABLE_FROM_CONNECTOR_ERROR_AT_WRAPPER_LEVEL;CALL_TIME_SURFACED_THIS_WAKE;NO_PROVIDER_REQUEST_ID_RATE_HEADERS_QUOTA_DEBIT_INCOMPLETE_SEARCH_OR_EFFECTIVE_SCOPE
portability: MEDIUM_DRIVE_QUERY_CORPUS_AND_AUTHORIZATION_SEMANTICS_PROVIDER_SPECIFIC
failure_behavior: TWO_NONEMPTY_SUCCESSES_PLUS_ONE_EMPTY_SUCCESS;NO_PERMISSION_DENIAL_OR_TRANSIENT_FAILURE_TESTED
verifier: DIRECT_GOOGLE_DRIVE_CONNECTOR_RECEIPT_PLUS_GITHUB_EVENT_AND_CURRENT_READBACK
consumer: X13_NEXT_WAKE_ONLY_NO_OPERATIONAL_CONSUMER_ACK
strongest_falsifier: MATCHED_NATIVE_DRIVE_V3_FILES_LIST_UNDER_THE_SAME_EFFECTIVE_PRINCIPAL_RETURNS_A_MATCH_FOR_THE_SYNTHETIC_QUERY_OR_MATERIALLY_DISAGREES_ON_QUERY_SCOPE_AUTHORIZATION_PAGINATION_OR_EMPTY_RESULT_SEMANTICS
honest_flaw: SYNTHETIC_TOKEN_WAS_DESIGNED_TO_MISS_SO_THIS ONLY TESTS_EMPTY_SUCCESS_SHAPE; PERMISSION_DENIAL_SHARED_DRIVE_VARIANCE_PAGINATION_REPLAY_INCOMPLETESEARCH_RATE_LIMIT_TRANSIENT_FAILURE_INDEX_LAG_NATIVE_PARITY_EFFECTIVE_SCOPE_ACTUAL_QUOTA_DEBIT_OPERATOR_SAVINGS_AND_CONSUMER_VALUE_REMAIN_UNTESTED_OR_UNEXPOSED
source_contract_primary: https://developers.google.com/workspace/drive/api/reference/rest/v3/files/list
source_quota_primary: https://developers.google.com/workspace/drive/api/guides/limits
valid_time_utc: 2026-08-07T11:46:02Z
recorded_time_utc: 2026-08-07T11:46:02Z
---

# X13 Google Drive metadata search — Phase 3

One bounded metadata-only document search used a synthetic token designed not to match. The connector returned zero results with its error, error-code, and HTTP-status error fields all null. No retry or fallback occurred, no Drive mutation occurred, and no document-body hydration was requested or observed. The connector exposed 1129 ms external call time for this wake.

This is narrow evidence that the wrapper can represent an empty successful search distinctly from a connector error. It is not evidence that the queried term is absent from all Drive corpora, because the connector does not expose the effective principal/scopes, raw provider request identity, `incompleteSearch`, or authoritative pagination/completeness state.

Google Drive v3 `files.list` officially returns `files`, optional `nextPageToken`, and `incompleteSearch`; a populated next-page token means more results may exist, and `incompleteSearch=true` means results can be missing. The current Google Drive usage-limit contract assigns 100 quota units to list operations such as `files.list`, but the connector did not expose its provider project, actual quota debit, or whether that project is on a grandfathered pre-May-2026 quota regime.

No raw Drive identifiers, URLs, titles, parent IDs, pagination tokens, or the synthetic probe token were persisted in this receipt. Decision remains open. Phase 4 should decide from the existing three-call evidence set only, with no additional Drive candidate call.

---
schema_id: hfo.gen133.x13.cots_connector_event.v1
experiment_id: X13_GDRIVE_METADATA_SEARCH_READONLY_015
phase: 4
status: PHASE4_DECIDED
phase_4_decision: ADOPT_WITH_GATES
operational_decision: ADOPT_WITH_GATES_FOR_BOUNDED_METADATA_DISCOVERY_ONLY
candidate: Google_Drive_metadata_only_document_search
wip: 1
prior_current_version: 159
candidate_calls_this_wake: 0
campaign_calls_total: 3
successful_nonempty_calls: 2
successful_empty_calls: 1
connector_errors_observed: 0
retries_total: 0
fallbacks_total: 0
candidate_mutations_total: 0
read_only: true
content_hydration_requested: false
content_hydration_observed: false
phase1_phase2_request_digest_match: true
phase1_phase2_ordered_result_digest_match: true
phase3_empty_success_distinguishable_from_connector_error: true
operator_minutes_removed_measured: 0
custom_code_avoided_estimate: 50_to_150_LOC_UNVALIDATED
paid_cost_usd_observed: 0_NO_PAID_COST_SURFACED_BY_CONNECTOR
direct_cost_or_quota_evidence: NONE_FROM_CONNECTOR
provider_contract_quota_units: FILES_LIST_100_UNITS_UNDER_CURRENT_POST_MAY1_2026_STANDARDIZED_MODEL
provider_contract_quota_regime_actual: UNKNOWN_CONNECTOR_PROJECT_MAY_BE_GRANDFATHERED_IF_USED_NOV2025_TO_APR2026
credentials: CONNECTOR_MANAGED_EFFECTIVE_PRINCIPAL_AND_SCOPE_UNKNOWN
durability: GIT_RECEIPT_DURABLE;DRIVE_SEARCH_VIEW_MUTABLE
observability: METADATA_VISIBLE_WITHOUT_BODY_HYDRATION;IDENTICAL_PHASE1_PHASE2_REPLAY_ORDERED_DIGEST_STABLE;EMPTY_SUCCESS_DISTINGUISHABLE_FROM_CONNECTOR_ERROR_AT_WRAPPER_LEVEL;PROVIDER_REQUEST_ID_RATE_HEADERS_ACTUAL_QUOTA_DEBIT_INCOMPLETE_SEARCH_EFFECTIVE_SCOPE_AND_AUTHORITATIVE_PAGINATION_STATE_NOT_SURFACED
portability: MEDIUM_DRIVE_QUERY_CORPUS_AND_AUTHORIZATION_SEMANTICS_PROVIDER_SPECIFIC
failure_behavior: TWO_NONEMPTY_SUCCESSES_PLUS_ONE_EMPTY_SUCCESS;NO_PERMISSION_DENIAL_SHARED_DRIVE_VARIANCE_RATE_LIMIT_OR_TRANSIENT_FAILURE_TESTED
verifier: DIRECT_GOOGLE_DRIVE_CONNECTOR_RECEIPTS_PLUS_GITHUB_EVENT_AND_CURRENT_READBACK
consumer: CATALOG_DISCOVERY_ELIGIBLE_BUT_NO_OPERATIONAL_CONSUMER_ACK
adoption_credit: 1_CATALOG_ONLY
fitness_credit: 0
mandatory_gate: METADATA_ONLY;BEST_EFFORT_FETCH_FALSE;SMALL_TOPN;DO_NOT_PERSIST_RAW_IDS_URLS_TITLES_PARENT_IDS_PAGINATION_TOKENS_OR_PROBE_TOKENS;TREAT_RESULTS_AS_MUTABLE_DISCOVERY_NOT_SNAPSHOT_EVIDENCE;EMPTY_SUCCESS_IS_NOT_DRIVE_WIDE_ABSENCE;NO_COMPLETENESS_CLAIM_WITHOUT_PAGINATION_AND_INCOMPLETESEARCH_EVIDENCE;CONSEQUENTIAL_CLAIMS_REQUIRE_DIRECT_DOCUMENT_FETCH_OR_MATCHED_NATIVE_PROVIDER_WITNESS;NO_UNBOUNDED_RETRY
strongest_falsifier: MATCHED_NATIVE_DRIVE_V3_FILES_LIST_UNDER_THE_SAME_EFFECTIVE_PRINCIPAL_MATERIALLY_DISAGREES_ON_QUERY_SCOPE_AUTHORIZATION_RESULT_ORDER_PAGINATION_OR_METADATA_ONLY_BEHAVIOR_OR_THE_CONNECTOR_HYDRATES_DOCUMENT_BODY_WHEN_BODY_FETCH_IS_DISABLED
honest_flaw: THREE_CALL_CAMPAIGN_DID_NOT_TEST_PERMISSION_DENIAL_SHARED_DRIVE_VARIANCE_PAGINATION_REPLAY_INCOMPLETESEARCH_RATE_LIMIT_TRANSIENT_FAILURE_INDEX_LAG_NATIVE_PARITY_EFFECTIVE_SCOPE_ACTUAL_QUOTA_DEBIT_OPERATOR_SAVINGS_OR_OPERATIONAL_CONSUMER_VALUE
source_contract_primary: https://developers.google.com/workspace/drive/api/reference/rest/v3/files/list
source_quota_primary: https://developers.google.com/workspace/drive/api/guides/limits
valid_time_utc: 2026-08-07T12:47:07Z
recorded_time_utc: 2026-08-07T12:47:07Z
---

# X13 Google Drive metadata search — Phase 4 decision

Decision: **ADOPT_WITH_GATES** for bounded metadata-only discovery/catalog use.

No additional Google Drive candidate call was made in Phase 4. The decision is based only on the frozen three-call evidence set: two bounded nonempty metadata-only searches and one bounded empty-success search, with zero observed connector errors, retries, fallbacks, candidate mutations, or document-body hydration. The identical Phase 1/2 replay matched both request and ordered result digests; Phase 3 showed that this wrapper can represent an empty successful search distinctly from a connector error.

This evidence is sufficient to avoid custom search plumbing for low-consequence catalog/discovery workflows, but not sufficient for completeness, authoritative absence, permission, or consequential access claims. Google Drive v3 `files.list` exposes `nextPageToken` and `incompleteSearch`; if `nextPageToken` is populated more results may exist, and `incompleteSearch=true` means some results might be missing. The connector did not expose authoritative pagination/completeness state, effective principal/scopes, provider request identity, rate-limit headers, or actual quota debit.

Current provider documentation assigns 100 quota units to list operations such as `files.list` under the post-May-1-2026 standardized model. Projects that used Drive API between November 2025 and April 2026 can retain prior quotas, so this connector's actual quota regime remains unknown. Standard Drive API use currently has no additional cost below published thresholds; the connector surfaced no direct paid-cost or quota-debit receipt.

Mandatory gates: metadata-only mode; body fetch disabled; small bounded result cap; do not persist raw Drive IDs, URLs, titles, parent IDs, pagination tokens, or synthetic probe tokens; treat search results as mutable discovery rather than snapshot evidence; do not infer Drive-wide absence from an empty success; do not claim completeness without pagination plus `incompleteSearch` evidence; require a direct document fetch or matched native-provider witness for consequential claims; and prohibit unbounded retry.

Adoption credit is 1 for catalog-only use. Fitness credit remains 0 because measured operator-minute savings are still zero and no operational consumer has acknowledged value.

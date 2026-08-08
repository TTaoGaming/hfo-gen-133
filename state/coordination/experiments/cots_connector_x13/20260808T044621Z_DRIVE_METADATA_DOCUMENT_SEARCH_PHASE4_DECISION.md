---
schema_id: hfo.gen133.x13.cots_connector_event.v1
experiment_id: X13_GDRIVE_METADATA_DOCUMENT_SEARCH_READONLY_019
event: PHASE4_DECISION
prior_current_version: 175
candidate: Google_Drive_search_explicit_document_metadata_only
campaign_wake: 4_of_4
phase_status: PHASE4_COMPLETE
phase_4_decision: ADOPT_WITH_GATES
operational_decision: ADOPT_BOUNDED_READONLY_METADATA_DISCOVERY_WITH_GATES_ONLY
wip: 1
candidate_calls_this_wake: 0
candidate_mutations_this_wake: 0
retries_this_wake: 0
fallbacks_this_wake: 0
campaign_calls_total: 3
successful_nonempty_calls: 2
successful_empty_calls: 1
connector_errors_observed: 0
candidate_mutations_total: 0
content_fetches_total: 0
content_hydration_observed_total: 0
phase1_phase2_ordered_digest_match: true
phase3_empty_success_observed_distinct_from_error: true
operator_minutes_removed_measured: 0
custom_code_avoided_estimate: 50_to_140_LOC_UNVALIDATED
paid_cost_usd_observed: 0_NO_CHARGE_SURFACED_NOT_BILLING_PROOF
direct_cost_or_quota_evidence: NONE_FROM_CONNECTOR;OFFICIAL_GOOGLE_DRIVE_API_USAGE_LIMITS_DOCUMENT_LIST_ITEMS_SUCH_AS_FILES_LIST_AT_100_QUOTA_UNITS_PER_REQUEST_UNDER_POST_20260501_MODEL;ACTUAL_CONNECTOR_NATIVE_MAPPING_PROJECT_REGIME_AND_DEBIT_UNKNOWN
provider_contract_quota_regime: OFFICIAL_DRIVE_API_USAGE_LIMITS_CURRENT_2026_08_08_DOCUMENT_1000000_UNITS_PER_MINUTE_PER_PROJECT_325000_PER_MINUTE_PER_USER_PER_PROJECT_400000000_QUOTA_UNIT_DAILY_BILLING_THRESHOLD_FOR_NEW_MODEL_AND_403_OR_429_RATE_LIMIT_RESPONSES;LEGACY_PROJECTS_MAY_RETAIN_PRIOR_QUOTAS
credentials: CONNECTOR_MANAGED_EFFECTIVE_PRINCIPAL_TOKEN_TYPE_AND_OAUTH_SCOPES_UNKNOWN;OFFICIAL_FILES_LIST_ACCEPTS_MULTIPLE_SCOPES_INCLUDING_DRIVE_METADATA_READONLY_AND_DRIVE_READONLY
durability: GIT_EVENT_AND_CURRENT_RECEIPTS_DURABLE;SHORT_INTERVAL_IDENTICAL_QUERY_ORDERED_HASHED_ID_DIGEST_MATCH_OBSERVED;DRIVE_SEARCH_RESULT_REMAINS_MUTABLE_QUERY_VIEW_NOT_SNAPSHOT
observability: BOUNDED_RESULT_COUNTS_METADATA_ITEMS_OR_EMPTY_ARRAY_VISIBLE;NO_CONTENT_HYDRATION_OBSERVED;PROVIDER_REQUEST_ID_HTTP_STATUS_RATE_HEADERS_EFFECTIVE_SCOPE_NATIVE_METHOD_NATIVE_NEXT_PAGE_TOKEN_INCOMPLETE_SEARCH_AND_ACTUAL_QUOTA_DEBIT_NOT_SURFACED
portability: MEDIUM_GENERIC_METADATA_SEARCH_AND_EMPTY_SUCCESS_SEMANTICS_PORTABLE;GOOGLE_DRIVE_QUERY_MIME_CORPUS_SHARED_DRIVE_AND_AUTHORIZATION_SEMANTICS_PROVIDER_SPECIFIC
failure_behavior: TWO_BOUNDED_NONEMPTY_SUCCESSES_WITH_MATCHED_ORDERED_HASHED_ID_DIGESTS_PLUS_ONE_SYNTHETIC_EMPTY_SUCCESS;NO_PERMISSION_DENIAL_INVALID_CURSOR_PAGINATION_REPLAY_INCOMPLETE_SEARCH_RATE_LIMIT_TRANSIENT_OR_NATIVE_PARITY_TESTED
connector_variance_probe: ITEM_TYPE_DOCUMENT_IS_CONNECTOR_DOCUMENT_CLASS_NOT_GOOGLE_DOCS_MIME_ONLY;EXPLICIT_ITEM_TYPE_AND_BEST_EFFORT_FETCH_FALSE_PREVENTED_OBSERVED_CONTENT_HYDRATION_IN_ALL_THREE_CALLS;EMPTY_SUCCESS_DISTINCT_FROM_OBSERVED_ERROR_STATE;WRAPPER_HIDES_NATIVE_COMPLETENESS_AND_AUTHORIZATION_SIGNALS
verifier: DIRECT_GOOGLE_DRIVE_CONNECTOR_RECEIPTS_FROM_PHASES_1_TO_3_PLUS_DURABLE_REQUEST_AND_RESULT_DIGESTS_PLUS_OFFICIAL_GOOGLE_DRIVE_V3_FILES_LIST_AND_USAGE_LIMITS_DOCS_PLUS_GITHUB_IMMUTABLE_EVENT_AND_CURRENT_READBACK
consumer: HFO_COMMAND_AND_CONTROL_DISCOVERY_CANDIDATE_NO_DOWNSTREAM_CONSUMER_ACK
adoption_credit: 1_BOUNDED_READONLY_METADATA_DISCOVERY_ONLY
fitness_credit: 0
mandatory_gate: READONLY_METADATA_SEARCH_ONLY;EXPLICIT_ITEM_TYPE_REQUIRED;BEST_EFFORT_FETCH_FALSE;SMALL_EXPLICIT_TOPN;DO_NOT_PERSIST_RAW_FILE_IDS_TITLES_URLS_PARENT_IDS_OR_PAGE_TOKENS_IN_X13_RECEIPTS;DO_NOT_TREAT_ITEM_TYPE_DOCUMENT_AS_GOOGLE_DOCS_MIME_ONLY;MATCHED_SHORT_INTERVAL_REPLAY_IS_NOT_SNAPSHOT_DURABILITY_COMPLETENESS_OR_ORDERING_GUARANTEE;EMPTY_SUCCESS_IS_NOT_CORPUS_WIDE_ABSENCE_COMPLETENESS_AUTHORIZATION_OR_INDEX_FRESHNESS_PROOF;DO_NOT_INFER_COMPLETENESS_FROM_ABSENCE_OF_VISIBLE_PAGE_TOKEN_WHEN_WRAPPER_DOES_NOT_EXPOSE_PROVIDER_INCOMPLETE_SEARCH_OR_NATIVE_PARITY;NO_UNBOUNDED_RETRY;PROVIDER_ERRORS_FAIL_CLOSED;NO_CONTENT_FETCH_WITHOUT_SEPARATE_JUSTIFICATION;NO_CONSEQUENTIAL_COMPLETENESS_AUTHORIZATION_OR_EXISTENCE_CLAIM_FROM_SEARCH_ONLY
strongest_falsifier: A_MATCHED_PROVIDER_DIRECT_DRIVE_V3_FILES_LIST_UNDER_THE_SAME_EFFECTIVE_PRINCIPAL_AND_EQUIVALENT_QUERY_MATERIALLY_DISAGREES_ON_ACCESSIBLE_METADATA_RESULTS_UNDER_QUIESCENT_STATE_OR_THE_WRAPPER_FETCHES_FILE_CONTENT_DESPITE_EXPLICIT_ITEM_TYPE_DOCUMENT_AND_BEST_EFFORT_FETCH_FALSE
honest_flaw: THREE_CALLS_TOTAL_WITH_NO_OBSERVED_ERRORS;NO_PERMISSION_DENIAL_INVALID_CURSOR_PAGINATION_REPLAY_INCOMPLETE_SEARCH_SHARED_DRIVE_VARIANCE_RATE_LIMIT_TRANSIENT_FAILURE_NATIVE_PARITY_EFFECTIVE_SCOPE_ACTUAL_QUOTA_DEBIT_OPERATOR_SAVINGS_OR_DOWNSTREAM_CONSUMER_VALUE_TESTED
next_phase: CLOSED_NEXT_WAKE_START_EXACTLY_ONE_NEW_CANDIDATE_AT_PHASE1_WIP1
valid_time_utc: 2026-08-08T04:46:21Z
recorded_time_utc: 2026-08-08T04:46:21Z
---

# X13 Phase 4 — Google Drive metadata search decision

## Surface → owner → permission

- Surface: frozen three-call evidence for `Google_Drive.search` with explicit `item_type=document`, bounded `topn=3`, and `best_effort_fetch=false`.
- Owner: Google Drive connector / Google Drive provider surface; X13 owns only experiment receipts and the COTS adoption decision.
- Permission: operator authorized bounded read-only connector experiments and Git-first receipts. Phase 4 issued no additional Drive candidate call and performed no Drive mutation, account action, send, spend, merge, deployment, deletion, secret exposure, or task mutation.

## Decision

**ADOPT_WITH_GATES** for **bounded, read-only metadata discovery only**.

This is a narrow COTS preference, not a reliability, completeness, authorization, or snapshot certification. The connector avoided custom provider plumbing for the tested surface and, across three bounded calls, did not hydrate file contents when explicit metadata-only controls were used. That is enough to prefer the existing connector over inventing a new metadata-search adapter for nonconsequential discovery, but not enough to trust it for completeness-sensitive or authorization-sensitive decisions.

## Frozen evidence

- 3 bounded read-only connector calls total.
- 2 nonempty successes; the exact Phase-1 request replayed in Phase 2 with the same ordered hashed-ID digest over a short interval.
- 1 synthetic nonmatching empty success, distinct from the observed connector error state.
- 0 observed connector errors, retries, fallbacks, Drive mutations, content fetches, or content hydration events.
- `item_type=document` behaved as a connector document class, not a Google Docs MIME-only selector.
- The wrapper did not expose provider request ID, HTTP status/rate headers, effective principal/scopes, native method, native `nextPageToken`, `incompleteSearch`, or actual quota debit.

The short-interval digest match is repeatability evidence only. Drive search remains a mutable query view, and the empty-success probe is not corpus-wide absence, completeness, authorization, or index-freshness proof.

## Official contract cross-check

Google Drive v3 `files.list` documents `nextPageToken` and `incompleteSearch`; when `incompleteSearch=true`, results can be missing. It also documents provider-specific corpus/shared-drive behavior and multiple acceptable OAuth scopes, including `drive.metadata.readonly` and `drive.readonly`.

Primary contract: https://developers.google.com/workspace/drive/api/reference/rest/v3/files/list

Google's current usage-limits documentation states that under the quota model introduced May 1, 2026, list operations such as `files.list` consume 100 quota units, with 1,000,000 units/minute/project, 325,000 units/minute/user/project, and a 400,000,000-unit/day/project billing threshold; legacy projects may retain prior quotas and rate-limit failures may surface as 403 or 429. The connector's actual native mapping, project regime, and debit remain unknown.

Primary limits contract: https://developers.google.com/workspace/drive/api/guides/limits

## Measures

| Measure | Campaign result |
|---|---:|
| bounded read-only connector calls | 3 |
| nonempty / empty successes | 2 / 1 |
| observed connector errors | 0 |
| content fetches / hydration | 0 / 0 |
| mutations / retries / fallbacks | 0 / 0 / 0 |
| operator minutes removed | 0 measured |
| custom code avoided | 50–140 LOC, unvalidated |
| actual provider quota debit | unknown |
| credentials / effective scope | connector-managed, unknown |
| durability | Git receipts durable; query results not snapshot-durable |
| observability | bounded result/empty state visible; native HTTP/auth/quota/completeness fields hidden |
| portability | medium; generic discovery portable, Drive semantics provider-specific |
| adoption / fitness credit | 1 narrow discovery-only / 0 |

## Mandatory gates

Use this surface only for bounded, read-only metadata discovery with explicit `item_type`, `best_effort_fetch=false`, and a small explicit `topn`. Do not persist raw Drive IDs, titles, URLs, parent IDs, or page tokens in X13 receipts. Do not equate `item_type=document` with Google Docs MIME type. Do not treat short-interval replay as snapshot durability or stable ordering. Do not treat empty success as Drive-wide absence. Do not infer completeness from absence of a visible page token because the wrapper does not expose native `incompleteSearch` or prove native parity. Provider/connector errors fail closed; retries must be bounded. File-content fetches require separate justification. Search alone cannot justify consequential completeness, authorization, or existence claims.

## Strongest falsifier

A matched provider-direct Drive v3 `files.list` under the same effective principal and equivalent query materially disagrees on accessible metadata results under a quiescent Drive/index state, or this explicit metadata-only mode fetches file content despite `item_type=document` and `best_effort_fetch=false`.

## Honest flaw

Three successful/empty calls are weak evidence and sampled no adverse provider path. Permission denial, invalid cursor, pagination replay, `incompleteSearch`, shared-drive/corpus variance, rate limiting, transient failure, native parity, effective OAuth scope, actual quota debit, measured operator savings, and downstream consumer value remain untested.

## Next

Campaign closed. On the next wake, start exactly one new candidate at Phase 1 with WIP=1.
---
schema_id: hfo.gen133.x13.cots_connector_event.v1
experiment_id: X13_GOOGLE_DRIVE_SEARCH_METADATA_READONLY_001
event_type: PHASE4_ADOPTION_DECISION
phase: 4_of_4
phase_status: COMPLETE
candidate: Google_Drive_search_metadata_only_surface
decision: ADOPT_WITH_GATES
adoption_mode: CATALOG_MANUAL_ONLY_NONOPERATIONAL
carrier_task_id: 6a55c1733708819185088bf334e33ea5
carrier_task_id_match: true
wip: 1
repository: TTaoGaming/hfo-gen-133
branch: agent/gen133-bootstrap-20260730
prior_current_version_expected: 91
candidate_call_made_this_phase: false
campaign_calls: 3_READONLY_2_SUCCESS_1_INVALID_ARGUMENT_0_RETRY_0_FALLBACK_0_MUTATION
phase1_observation: ONE_METADATA_RESULT_DOCUMENT_CATEGORY_INCLUDED_SPREADSHEET_BACKED_ITEM
phase2_observation: NORMAL_EMPTY_RESULTS_ARRAY_FOR_SYNTHETIC_UNLIKELY_TOKEN
phase3_observation: INVALID_PAGE_TOKEN_FAILED_CLOSED_WITH_CONNECTOR_INVALID_ARGUMENT_AND_PROVIDER_FILES_LIST_HTTP_400
custom_code_avoided_estimate: 25_to_70_LOC_UNVALIDATED
operator_minutes_removed_measured: 0
credentials: CONNECTOR_MANAGED_IDENTITY_AND_EFFECTIVE_SCOPE_UNKNOWN
durability: CANONICAL_GIT_EVENTS_AND_VERSIONED_CURRENT_PERSIST_BUT_DOWNSTREAM_VERIFICATION_ROUTE_HAD_EXACT_SOURCE_POINTER_DEFECT
observability: PARTIAL_PROVIDER_METHOD_AND_ONE_TYPED_ERROR_VISIBLE_NO_SUCCESS_HEADERS_REQUEST_ID_INCOMPLETESEARCH_QUOTA_OR_HIDDEN_ATTEMPTS
portability: LOW_TO_MEDIUM_DRIVE_V3_QUERY_AND_CONNECTOR_SHAPE_SPECIFIC
failure_behavior: INVALID_PAGE_TOKEN_FAILED_CLOSED_BUT_OTHER_FAILURE_CLASSES_UNTESTED
paid_cost_usd_observed: 0_NO_CHARGE_SURFACED
actual_quota_consumed: UNKNOWN
official_quota_contract: FILES_LIST_100_UNITS_PER_REQUEST_AS_OF_2026_08_04
strongest_falsifier: SAME_PRINCIPAL_RAW_DRIVE_FILES_LIST_CONTRADICTS_A_CONNECTOR_RESULT_OR_SHOWS_MISSING_FILES_NEXT_PAGE_OR_INCOMPLETESEARCH_FOR_THE_SAME_BOUNDARY
verifier: S04_STRUCTURAL_PREFLIGHT_REVISE_NONBINDING_WEIGHT_0_DUE_DOWNSTREAM_ROUTE_CURRENT_V91_COMMIT_PATH_BLOB_MISMATCH
independent_verification_closed: false
consumer: NONE_NAMED
consumer_ack: NOT_OBSERVED
adoption_credit: 0
fitness_credit: 0
honest_flaw: THREE_EASY_CALLS_DO_NOT_VERIFY_IDENTITY_SCOPE_COMPLETENESS_ORDERING_SHARED_DRIVES_REAL_CURSOR_SUCCESS_RATE_LIMITS_HIDDEN_CALLS_QUOTA_CONSUMPTION_OR_CONSUMER_VALUE
mandatory_gate: HUMAN_REVIEW_BOUNDED_METADATA_DISCOVERY_ONLY_ZERO_RESULTS_NONAUTHORITATIVE_NO_SENSITIVE_QUERY_RETENTION_AND_EXACT_COMMIT_PATH_BLOB_RECEIPTS
next_campaign_candidate: Gmail_search_metadata_readonly_surface
next_campaign_phase: PHASE1_OFFICIAL_CONTRACT_AND_DIRECT_CAPABILITY_BASELINE
valid_time_utc: 2026-08-04T16:50:10Z
recorded_time_utc: 2026-08-04T16:50:10Z
---

# X13 Google Drive metadata search — phase 4 decision

## Decision

`ADOPT_WITH_GATES`

Adopt only as a bounded, human-reviewed catalog discovery surface. It is not approved for unattended control flow, authoritative absence claims, compliance evidence, inventory completeness, or operational/fitness credit.

No additional Google Drive candidate call was made in this phase.

## Campaign evidence

| Measure | Observation |
|---|---|
| Calls | 3 read-only calls: 2 completed, 1 invalid-argument failure |
| Positive path | One `topn=1` metadata result; the connector `document` category included a spreadsheet-backed item, so category is not a MIME guarantee |
| Empty path | One synthetic unlikely-token request returned a normal empty array; this is not authoritative absence |
| Failure path | One synthetic invalid page token failed closed as connector `INVALID_ARGUMENT` with a Drive v3 `files.list` HTTP 400 identifying `pageToken` |
| Custom code avoided | 25–70 LOC estimated, unvalidated |
| Operator minutes removed | 0 measured |
| Credentials | Connector-managed; authenticated identity and effective scopes unknown |
| Durability | Canonical immutable Git events and versioned CURRENT persist; however, a downstream verifier route bound the real CURRENT v91 blob to the wrong commit |
| Observability | Partial: provider method and one typed error were visible; success headers, request IDs, `nextPageToken`, `incompleteSearch`, quota counters, and hidden attempts were not |
| Portability | Low-to-medium; Drive v3 semantics and connector-specific result/error shapes remain provider-bound |
| Failure behavior | Invalid token failed closed; permission, rate-limit, timeout, expired-token, shared-drive, and transient failures were not tested |
| Direct cost/quota evidence | No charge surfaced; actual debit unknown. Google's current contract assigns 100 quota units to `files.list` |
| Consumer | None named; no acknowledgment or measured value |

## Official contract retained

Google's current `files.list` contract returns `files[]`, optional `nextPageToken`, and `incompleteSearch`. A rejected page token must be discarded, and pagination restarted from the first page if a fresh search is permitted. Supported authorization scopes include metadata-read-only, but this connector does not expose which identity or scope is active.

- https://developers.google.com/workspace/drive/api/reference/rest/v3/files/list
- https://developers.google.com/workspace/drive/api/guides/limits

As of 2026-08-04, Google documents 100 quota units per `files.list` request, standard API use at no additional cost within applicable limits, and planned over-limit billing later in 2026 with advance notice. The connector exposed no direct quota or billing receipt.

## Verifier result

The latest independent structural preflight returned `REVISE`, nonterminal, same-provider nonbinding, binding weight `0`. It confirmed the canonical phase-3 event and CURRENT bytes exist, but found that a downstream S03 route claimed the CURRENT v91 blob at the phase-3 event commit; at that commit the path still resolved to CURRENT v90. The actual v91 CURRENT commit was `f66e96d677a8718007257369ce4ea797948cda1d`.

This defect does not contradict the bounded Drive connector observations. It does block independent-verification closure and proves that blob existence elsewhere on the branch is not enough: all verifier packets must bind an exact commit/path/blob triplet.

Verifier receipt:

- `state/coordination/receipts/chatgpt_runtime/seat-04/20260804T161428Z_X13_GOOGLE_DRIVE_PHASE3_STRUCTURAL_REVISE.yaml`

## Mandatory gates

1. Restrict use to bounded metadata discovery with a human reviewing the returned result.
2. Treat empty results as nonauthoritative absence unless a same-principal raw Drive witness establishes corpus, pagination, and `incompleteSearch=false`.
3. Do not infer MIME type from connector categories.
4. Use only a provider-returned token from the immediately preceding compatible request; never retry a rejected token unchanged.
5. Assume queries, filters, URLs, and tokens may be echoed in errors. Do not place secrets in them, and do not retain exact search terms without a named need.
6. Do not persist file names, IDs, URLs, parents, owners, or contents without an explicit retention purpose.
7. Require exact commit/path/blob receipts for every verifier or consumer handoff.
8. Require verified identity and scope, a typed stable schema, raw-provider parity, quota evidence, a named consumer, acknowledgment, and measured outcome before unattended or operational use.
9. Keep adoption and fitness credit at zero.

## Strongest falsifier

A same-principal raw Drive `files.list` call for the same boundary returns a materially different match set, a next page, or `incompleteSearch=true`, while the connector presents its result as complete or absent.

## Honest flaw

The campaign covered only one easy positive lookup, one synthetic zero-result lookup, and one synthetic invalid-token failure. It did not verify authenticated identity, effective OAuth scopes, search translation, ordering, real pagination success, shared-drive coverage, permission denial, rate limiting, transient failure behavior, hidden calls, quota consumption, consumer value, or actual time savings.

## Next campaign

Queue `Gmail_search_metadata_readonly_surface`, phase 1 only: official contract and one bounded direct capability baseline. No Gmail call was made in this phase.

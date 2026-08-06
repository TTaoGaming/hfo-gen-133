---
schema_id: hfo.gen133.s08.evidence_card.v1
seat: S08
callsign: Surtr
carrier_task_id_expected: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_observed: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_match: true
wip: 1
lane: agent_runtime_cots_capabilities
result: REVISE
valid_time_utc: 2026-08-06T00:26:52Z
recorded_time_utc: 2026-08-06T00:26:52Z
question: DOES_AN_EMPTY_GOOGLE_DRIVE_METADATA_SEARCH_WITH_REQUIRE_VIEWED_BY_USER_TRUE_SUPPORT_ABSENCE_ACROSS_ALL_ACCESSIBLE_DRIVE_FILES
candidate:
  connector_surface: Google_Drive.search
  connector_schema_observed_utc: 2026-08-06T00:26:52Z
  connector_build_version: UNKNOWN
  upstream_api: Google Drive API v3 files.list and File resource
changed_queue_source:
  experiment_id: X13_GOOGLE_DRIVE_METADATA_READONLY_006
  current_version: 123
  source_path: state/coordination/experiments/cots_connector_x13/20260805T234821Z_GOOGLE_DRIVE_METADATA_PHASE3_ACCEPTED_WITH_GATES.md
  source_commit: 25731460a1d91472b81717be2cf0482d4aca48e7
  source_blob: baba3be2cc170cb8f044c0cef5731e686da7e267
  request_shape: SYNTHETIC_NONMATCHING_TOKEN_TOPN_1_ITEM_TYPE_DOCUMENT_REQUIRE_VIEWED_TRUE_BEST_EFFORT_FETCH_FALSE
consumer:
  primary: X13_GOOGLE_DRIVE_METADATA_READONLY_006_PHASE4_DECISION
  catalog: HFO_COTS_CAPABILITY_INVENTORY_CATALOG_ONLY
verifier: DISTINCT_AUTHORIZED_SAME_PRINCIPAL_RAW_DRIVE_FILES_LIST_AND_CONNECTOR_VIEWED_SUBSET_PARITY_VERIFIER
expiry_utc: 2026-08-13T00:26:52Z
---

# REVISE — `require_viewed_by_user=true` changes the search universe

## Bounded finding

The phase-3 empty result cannot support absence across all files accessible to the effective Google principal.

The exposed connector contract says that `require_viewed_by_user=true` restricts results to files viewed by the authenticated user. It also says that an explicit `item_type=document` search is metadata-only and searches exactly one provider page. The connector does not expose its build, effective identity, raw request, corpus mapping, query translation, or Drive `incompleteSearch` value.

Google Drive API v3 separately defines `viewedByMe` as an output-only, user-specific boolean and `viewedByMeTime` as the user-specific last-viewed timestamp. The documented `files.list` query language supports comparisons on `viewedByMeTime`; it does not list `viewedByMe` as a file-search query term. Therefore the connector may use a time predicate, a provider-side field selection plus post-filter, or another internal translation. The exact predicate is unknown.

Google also documents that `files.list` defaults to the `user` corpus unless the query changes that behavior, while `allDrives` is a distinct broader corpus. A response can include `nextPageToken`, and `incompleteSearch=true` means some results may be missing. The phase-3 wrapper result did not expose raw corpus, pagination state, or `incompleteSearch`.

## Supported claims

- The single wrapper call returned zero documents on the bounded metadata-only surface with `require_viewed_by_user=true`.
- The call targeted a user-specific viewed subset, not an unqualified existence universe.
- A zero result is safely described as `ZERO_RETURNED_MATCHES_IN_THIS_VIEWED_SUBSET_WRAPPER_CALL`.
- Exact raw Drive corpus, viewed predicate, pagination completeness, effective principal, and `incompleteSearch` remain unknown.

## Excluded claims

- No matching file exists.
- No matching accessible file exists.
- No matching unviewed file exists.
- All accessible shared drives were searched completely.
- `require_viewed_by_user=true` maps to a specific raw Google `q` predicate.
- The connector violated Google Drive semantics.
- Hidden retries, fan-out, quota debit, or provider error state were zero.

## Required phase-4 gate

```text
EMPTY_RESULT_LABEL=ZERO_RETURNED_MATCHES_IN_THIS_VIEWED_SUBSET_WRAPPER_CALL
ABSENCE_ASSERTION=FORBIDDEN
UNVIEWED_FILE_COVERAGE=NOT_TESTED
RAW_CORPUS=UNKNOWN
RAW_VIEWED_PREDICATE=UNKNOWN
NEXT_PAGE_TOKEN_STATE=NOT_EXPOSED_IN_PHASE3_RECEIPT
INCOMPLETE_SEARCH_STATE=NOT_EXPOSED
OPERATIONAL_ADOPTION=NOT_EARNED
CATALOG_USE=BOUNDED_METADATA_DISCOVERY_WITH_HUMAN_REVIEW_ONLY
```

## Primary dated sources

1. Google Drive API v3 `files.list`, last updated 2026-07-07: default `corpora=user`; `includeItemsFromAllDrives`; `nextPageToken`; `incompleteSearch`; and OAuth scope surface. https://developers.google.com/workspace/drive/api/reference/rest/v3/files/list
2. Google Drive API v3 File resource, last updated 2026-07-14: `viewedByMe` is output-only and user-specific; `viewedByMeTime` is the user's last-viewed timestamp. https://developers.google.com/workspace/drive/api/reference/rest/v3/files
3. Google Drive search terms, last updated 2026-07-22: `viewedByMeTime` is a supported time-comparison query term; `viewedByMe` is not listed as a file-search query term. https://developers.google.com/workspace/drive/api/guides/ref-search-terms
4. Google Drive files and folders overview, last updated 2026-07-22: `user`, `drive`, `domain`, and `allDrives` are distinct corpora; `allDrives` includes shared drives where the user is a member plus My Drive and Shared with me. https://developers.google.com/workspace/drive/api/guides/about-files

## License and terms uncertainty

Google's referenced documentation is published under CC BY 4.0 and its code samples under Apache 2.0. No code sample or implementation was copied. The connector implementation license, exact build, upstream request mapping, effective Google API terms accepted by the account owner, and restricted-scope assessment state are unknown and were not evaluated in this pass.

## Strongest objection

The connector schema itself says it searches all accessible drives and restricts to viewed files, so the result may be sufficient for the catalog.

That supports a narrow catalog claim only: zero returned matches in the connector-defined viewed subset. It still cannot support global absence, because the viewed restriction intentionally excludes unviewed files and the wrapper receipt omits raw corpus, pagination, and `incompleteSearch`.

## Falsifier

Revise this card if a version-bound, same-principal synthetic fixture contains one viewed and one never-viewed matching document and a distinct verifier captures both the raw `files.list` request/response and connector output, proving:

- the exact connector translation for `require_viewed_by_user=true`;
- viewed document inclusion and never-viewed document exclusion;
- explicit corpus and shared-drive settings;
- `incompleteSearch=false`;
- no unconsumed `nextPageToken`;
- deterministic connector parity for the same canonical request.

## Cost and operator burden

- Research/web/Git cost observed: `$0`.
- Operator minutes consumed: `0`.
- Phase-4 wording amendment estimate: `5–10 minutes` producer time.
- Controlled same-principal parity verification estimate: `20–45 minutes` producer plus `20–45 minutes` distinct verifier time, only with pre-existing authorized fixtures.

## Honest flaw

No Drive call or private data was used. This is a contract-boundary analysis, not a runtime parity result. It cannot determine whether the connector implements a provider-side `viewedByMeTime` predicate, post-filters `viewedByMe`, uses an internal index, or performs hidden pagination/fan-out.

Fitness credit remains `0` until an exact WorkItem consumes this card and records ConsumerAck.

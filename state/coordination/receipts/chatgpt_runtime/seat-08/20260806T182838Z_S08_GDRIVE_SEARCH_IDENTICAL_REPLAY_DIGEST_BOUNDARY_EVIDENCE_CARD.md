---
schema_id: hfo.gen133.s08.evidence_card.v1
task_id_expected: 6a526109ba348191b5f23ad3172ad568
task_id_self_probe: MATCHED_PROMPT
seat: 08
wip: 1
queue_source: state/coordination/experiments/cots_connector_x13/CURRENT.md
queue_version: 141
queue_experiment_id: X13_GDRIVE_SEARCH_READONLY_011
queue_phase: PHASE2_IDENTICAL_BOUNDED_METADATA_ONLY_REPLAY_AND_DIGEST_COMPARISON
queue_carrier_task_id: 6a55c1733708819185088bf334e33ea5
queue_carrier_note: DIFFERENT_TASK_OWNER; THIS_CARD_IS_RESEARCH_INPUT_ONLY
lane: agent-runtime/COTS capabilities
question: Does an identical bounded Google Drive metadata-search replay with an equal ordered-result digest prove deterministic search or provider parity?
decision: REVISE
candidate: Google_Drive.search connector metadata-only paginated surface
candidate_schema_observed_utc: 2026-08-06T18:28:38Z
provider_reference: Google Drive API v3 files.list
tools_self_probe: GITHUB_READ_WRITE_AVAILABLE; WEB_PRIMARY_SOURCE_RESEARCH_AVAILABLE; SLACK_POINTER_SEND_AVAILABLE; GOOGLE_DRIVE_SCHEMA_VISIBLE; NO_GOOGLE_DRIVE_SEARCH_EXECUTED
consumer: X13_GDRIVE_SEARCH_READONLY_011_PHASE2_IDENTICAL_REPLAY_AND_DIGEST_COMPARISON_GATE
verifier: DISTINCT_SAME_EFFECTIVE_PRINCIPAL_RAW_DRIVE_V3_FILES_LIST_WITH_EXACT_Q_CORPORA_SPACES_PAGE_SIZE_ORDER_BY_FIELDS_AND_PAGINATION_STATE_VERIFIER
expiry_utc: 2026-08-13T18:28:38Z
valid_time_utc: 2026-08-06T18:28:38Z
recorded_time_utc: 2026-08-06T18:28:38Z
---

# REVISE — equal Google Drive replay digest is a drift canary, not deterministic search proof

## Exact bounded uncertainty

`X13_GDRIVE_SEARCH_READONLY_011` phase 2 proposes repeating the exact metadata-only `Google_Drive.search` request and comparing the normalized ordered-result digest. The connector schema exposes `query`, `topn`, optional raw `special_filter_query_str`, `item_type`, `require_viewed_by_user`, and opaque `page_token`, but it does not expose the provider request's effective `orderBy`, `corpora`, `spaces`, `driveId`, `includeItemsFromAllDrives`, selected fields, OAuth principal/scopes, request ID, quota debit, or index state.

## Primary/current evidence

Google Drive API v3 `files.list` treats `pageSize` as a maximum and may return fewer files. It exposes optional `orderBy`; if a `nextPageToken` is present the current list can be incomplete. Google also states that page tokens are typically valid only for several hours and that additions or removals can change expected results. The response can expose `incompleteSearch=true` when not all requested corpora were searched. Source accessed 2026-08-06: https://developers.google.com/workspace/drive/api/reference/rest/v3/files/list

Google's current search guide identifies `files.list` plus `q` as the provider search mechanism and documents that the server's returned fields depend on the request's field selection. Source accessed 2026-08-06: https://developers.google.com/workspace/drive/api/guides/search-files

Google's current quota guide states that list operations such as `files.list` consume 100 quota units under the post-2026-05-01 model, while standard use currently has no additional monetary charge below the stated threshold. The connector's provider-method mapping and actual debit remain unobserved. Source accessed 2026-08-06: https://developers.google.com/workspace/drive/api/guides/limits

## Supported claims

```text
EQUAL_DIGEST = SAME_NORMALIZED_ORDERED_WRAPPER_OUTPUT_OBSERVED_TWICE
UNEQUAL_DIGEST = DRIFT_OBSERVED; CAUSE_UNKNOWN
TOPN_3 = WRAPPER_OUTPUT_CAP
REPLAY_USE = SHORT_WINDOW_NORMALIZED_OUTPUT_DRIFT_CANARY
```

An equal digest is useful as a cheap canary showing that two wrapper observations returned the same ordered IDs/titles/URLs/parent IDs. A different digest establishes observed drift only; it does not identify whether the cause was corpus mutation, permission change, index refresh, wrapper mapping, ranking/order, pagination, or backend change.

## Excluded claims

```text
EQUAL_DIGEST != DETERMINISTIC_SEARCH_CONTRACT
EQUAL_DIGEST != COMPLETE_MATCH_SET
EQUAL_DIGEST != RAW_PROVIDER_PARITY
EQUAL_DIGEST != UNCHANGED_CORPUS_OR_PERMISSIONS
NO_NEXT_PAGE_TOKEN_EXPOSED != END_OF_PROVIDER_RESULT_SET
TOPN_3 != PROVIDER_PAGE_SIZE_OR_TOTAL_COUNT
```

The phase must not claim deterministic ordering, completeness, authoritative absence, stable authorization, stable index state, or one-to-one mapping to `files.list` from the repeated digest alone.

## Required revision

Rename the result to `NORMALIZED_OUTPUT_DRIFT_CANARY`. Preserve both request-canonical digests, timestamps, ordered normalized results, connector schema/version, error class, and whether `next_page_token` or an incompleteness signal was exposed. Classify equality only as `NO_DRIFT_OBSERVED_IN_TWO_SAMPLES`; classify inequality as `DRIFT_OBSERVED_CAUSE_UNKNOWN`.

## License / terms uncertainty

Google documentation is subject to Google's site copyright and API/platform terms. Effective OAuth identity, granted scopes, Cloud project, Workspace edition, shared-drive coverage, provider method, query translation, retained logs, quota project, and actual quota debit are unknown. No private Drive data was accessed for this card.

## Cost and operator estimate

- Research card: 12–20 operator minutes, $0 observed paid cost.
- Producer amendment to phase wording/receipt: 5–10 operator minutes.
- Distinct matched-provider verification: 20–40 operator minutes plus at least one provider list-call equivalent; official nominal reference is 100 quota units per `files.list`, but connector mapping/debit is unknown.
- Measured operator minutes removed: 0.

## Strongest objection

A rare token, unchanged permissions, and a short replay interval can make the first three results practically stable. That is sufficient for a low-cost drift canary, but it does not create a provider guarantee of deterministic ordering, completeness, or a frozen search snapshot.

## Falsifier

Move toward narrow `ADMIT` only if a distinct verifier captures the wrapper call and a same-effective-principal Drive v3 `files.list` request with explicit `q`, `corpora`, `spaces`, `pageSize`, `orderBy`, `fields`, shared-drive flags, `nextPageToken`, and `incompleteSearch`, under a bounded unchanged corpus/permission window, and obtains equivalent ordered file IDs. Even that admits only the tested mapping and window, not general deterministic Drive search.

## Fitness boundary

`fitness_credit: 0` until the exact consumer WorkItem incorporates this card, records a consequence-appropriate verification result, and emits explicit ConsumerAck.

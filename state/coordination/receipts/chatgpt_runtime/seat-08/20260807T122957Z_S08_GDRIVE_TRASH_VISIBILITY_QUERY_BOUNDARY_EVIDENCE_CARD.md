---
schema_id: hfo.gen133.s08.evidence_card.v1
seat: S08
carrier_task_id: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_match: true
wip: 1
research_lane: agent-runtime/COTS capabilities
queue_source: state/coordination/experiments/cots_connector_x13/CURRENT.md
queue_version: 159
experiment_id: X13_GDRIVE_METADATA_SEARCH_READONLY_015
phase: 4
bounded_uncertainty: "Can the current three-call Google_Drive metadata-search campaign be interpreted as excluding trashed documents, or is trash visibility still unbound?"
candidate: Google_Drive.search explicit item_type=document metadata-only surface
candidate_version: CONNECTOR_VERSION_NOT_EXPOSED
connector_schema_observed_utc: 2026-08-07T12:29:57Z
decision: REVISE
decision_scope: TRASH_VISIBILITY_AND_OPERATIONAL_DISCOVERY_CLAIM_CEILING
consumer: X13_GDRIVE_METADATA_SEARCH_READONLY_015_PHASE4_DECISION_TRASH_VISIBILITY_GATE
verifier: S04_STRUCTURAL_PREFLIGHT_PLUS_DISTINCT_CONNECTOR_TO_RAW_DRIVE_V3_QUERY_MAPPING_OR_SCHEMA_CONTRACT_FOR_TRASH_FILTERING
verifier_result: NOT_RUN
paid_cost_usd_observed: 0
operator_minutes_removed_measured: 0
producer_operator_minutes_estimate: 7_to_12
verifier_operator_minutes_estimate: 15_to_30
review_expiry_utc: 2026-08-14T12:29:57Z
valid_time_utc: 2026-08-07T12:29:57Z
recorded_time_utc: 2026-08-07T12:29:57Z
---

# S08 Evidence Card — Drive trash-visibility boundary

## Decision

`REVISE` the phase-4 claim ceiling.

The current campaign supports bounded metadata discovery without body hydration, but it does **not** support the stronger claim that results exclude trashed documents. Treat trash visibility as `UNKNOWN` unless the effective connector-to-provider query mapping or an explicit connector contract proves a `trashed = false` filter.

This card does not execute another Drive candidate call. It only tightens interpretation of the existing three-call campaign.

## Current queue and exact candidate

- X13 queue: `state/coordination/experiments/cots_connector_x13/CURRENT.md`, version `159`.
- Campaign: `X13_GDRIVE_METADATA_SEARCH_READONLY_015`, phase 4 pending from the existing three-call evidence set.
- Candidate surface: `Google_Drive.search` with explicit `item_type=document`, which the exposed connector contract describes as one metadata-only provider page with no file-content fetch.
- Connector version/build identifier: not exposed.
- Phase-1 event: `state/coordination/experiments/cots_connector_x13/20260807T094914Z_GDRIVE_METADATA_SEARCH_PHASE1_BASELINE.md` records `item_type=document`, `topn=3`, and `best_effort_fetch=false`, but does not bind a raw provider `q`, a connector-internal trash filter, or returned `trashed` metadata.

## Primary/current sources

1. Google Drive API v3 `files.list`, last updated `2026-07-07 UTC`:
   https://developers.google.com/workspace/drive/api/reference/rest/v3/files/list
   - Google states that `files.list` returns all files by default, **including trashed files**.
   - To exclude trashed files, Google instructs callers to add `trashed=false` to the query.
   - The same method exposes `q`, `corpora`, `pageToken`, `nextPageToken`, and `incompleteSearch`, so provider-level result scope depends on request details not bound by this campaign receipt.

2. Google Drive API search guide, last updated `2026-05-07 UTC`:
   https://developers.google.com/workspace/drive/api/guides/search-files
   - `q` is the filtering mechanism for file search.
   - Google gives `fullText contains 'important' and trashed = true` as a valid query example, confirming `trashed` is a first-class search predicate.

3. Exposed `Google_Drive.search` connector contract observed `2026-08-07`:
   - explicit `item_type=document` is metadata-only and does not fetch file contents;
   - `special_filter_query_str` is an optional raw Drive v3 `q` filter;
   - the contract does not state that trashed files are excluded by default and exposes no dedicated `trashed` boolean parameter;
   - wrapper-internal query augmentation is not observable from the schema.

## Supported claims

- The X13 campaign has evidence for bounded document-metadata search with no observed body hydration.
- Google Drive v3 itself includes trashed files in `files.list` by default unless the effective query excludes them.
- The connector surface can express a raw Drive filter through `special_filter_query_str`, but the campaign evidence does not bind the effective raw provider query used by the wrapper.
- Therefore `TRASH_VISIBILITY_UNKNOWN` is the safe claim ceiling for the completed three-call campaign.
- If this capability is later consumed operationally for active-document discovery, an explicit `trashed = false` gate or equivalent connector guarantee should be bound before assuming deleted/trashed items are excluded.

## Excluded claims

- This card does **not** prove that any observed campaign result was trashed.
- It does not prove the connector fails to inject `trashed=false` internally.
- It does not establish connector/provider parity, completeness, shared-drive coverage, effective OAuth principal/scopes, indexing freshness, stable ordering, or authoritative absence.
- It does not inspect, persist, or classify any private Drive file metadata or contents.
- It does not establish operational value or operator-minute savings.

## License / terms uncertainty

Google developer documentation states that page prose is generally licensed under CC BY 4.0 and code samples under Apache 2.0. Those documentation licenses do not grant rights in user Drive files or their contents. Effective connector OAuth scopes/principal, administrator restrictions, provider request mapping, retention, and connector-specific data-handling terms remain unbound in this campaign.

## Strongest objection

The managed connector may already append `trashed=false` even though that behavior is absent from the exposed schema and campaign receipt. That objection is valid; it is why the decision is `REVISE` to `UNKNOWN`, not a claim that trashed files are definitely included.

## Falsifier

Move this boundary toward `ADMIT_EXCLUDES_TRASH` only if one of the following becomes durable and source-bound:

1. a current connector contract explicitly guarantees exclusion of trashed files for this exact metadata-search mode; or
2. a distinct same-principal connector-to-Drive-v3 mapping witness proves the effective raw `files.list` request includes `trashed = false` (or an equivalent provider-side filter) for the WorkItem being consumed.

Move toward a stronger warning if a bounded authorized witness returns a known trashed fixture through the same connector mode without an explicit include-trash request.

## Verification requirement

Verifier: `S04_STRUCTURAL_PREFLIGHT_PLUS_DISTINCT_CONNECTOR_TO_RAW_DRIVE_V3_QUERY_MAPPING_OR_SCHEMA_CONTRACT_FOR_TRASH_FILTERING`.

The verifier should bind the exact connector schema/build when exposed, request arguments, effective provider `q`, principal/scope ceiling, whether `trashed=false` is injected, and a timestamp. Same-provider ChatGPT structural review remains nonbinding for provider-equivalence claims.

## Cost / operator burden

- Paid cost observed for this scout pass: `$0`.
- Additional Drive candidate calls performed by this card: `0`.
- Operator minutes removed measured: `0`.
- Research/read/write estimate: `7–12 minutes`.
- Distinct provider-mapping verification estimate: `15–30 minutes`.

## Consumption / fitness

Consumer: `X13_GDRIVE_METADATA_SEARCH_READONLY_015_PHASE4_DECISION_TRASH_VISIBILITY_GATE`.

Fitness/adoption credit remains `0` until a named WorkItem consumes the exact Git pointer and records ConsumerAck.

## Honest flaw

The provider default is known, but the managed connector's hidden query augmentation is not. This card can cap the claim safely; it cannot determine actual trash inclusion without a connector contract or matched provider mapping witness.

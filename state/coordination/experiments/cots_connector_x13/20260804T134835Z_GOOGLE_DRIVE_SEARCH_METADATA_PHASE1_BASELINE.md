---
schema_id: hfo.gen133.x13.cots_connector_event.v1
experiment_id: X13_GOOGLE_DRIVE_SEARCH_METADATA_READONLY_001
carrier_task_id: 6a55c1733708819185088bf334e33ea5
carrier_task_id_match: true
candidate: Google_Drive_search_metadata_only_surface
phase: 1_of_4
event: OFFICIAL_CONTRACT_AND_DIRECT_BASELINE
status: PHASE1_ACCEPTED_WITH_GATES
wip: 1
branch: agent/gen133-bootstrap-20260730
prior_current_version_expected: 88
candidate_calls_this_wake: 1
read_only_calls: 1
retries: 0
fallbacks: 0
candidate_mutations: 0
account_or_permission_changes: 0
paid_calls_or_spend: 0
production_deployments: 0
result_count: 1
content_hydrated_or_returned: 0
consumer_ack: NOT_OBSERVED
operator_minutes_removed_measured: 0
custom_code_avoided_estimate: 25_to_70_LOC_UNVALIDATED
paid_cost_usd_observed: 0_NO_CHARGE_SURFACED
actual_quota_consumed: UNKNOWN
credentials: CONNECTOR_MANAGED_IDENTITY_AND_SCOPE_UNKNOWN
durability: IMMUTABLE_GIT_EVENT_ONLY_DRIVE_RESULT_TRANSIENT
observability: PARTIAL_METADATA_FIELDS_NO_PROVIDER_TELEMETRY
portability: LOW_TO_MEDIUM_GOOGLE_QUERY_AND_CONNECTOR_SCHEMA_SPECIFIC
failure_behavior: NOT_PROBED_IN_PHASE1
adoption_credit: 0
fitness_credit: 0
valid_time_utc: 2026-08-04T13:48:35Z
recorded_time_utc: 2026-08-04T13:48:35Z
---

# X13 Google Drive metadata search — phase 1 baseline

## Official contract baseline

Google Drive API v3 `files.list` is a read operation at `GET /drive/v3/files`. It accepts `q` and `pageToken`; its response contract includes `files[]`, optional `nextPageToken`, and `incompleteSearch`. Google documents that a populated `nextPageToken` means another page may exist, and `incompleteSearch=true` means results may be missing. The method supports metadata-read-only authorization, but the connector's effective scope is not exposed.

Official primary sources checked on 2026-08-04:

- https://developers.google.com/workspace/drive/api/reference/rest/v3/files/list
- https://developers.google.com/workspace/drive/api/guides/search-files
- https://developers.google.com/workspace/drive/api/guides/limits

Current official quota documentation says a `files.list` action consumes 100 quota units. It also lists Drive MCP `search_files` at query cost 100. Standard API use is currently available at no additional cost; charges for exceeding quota limits are planned later in 2026. This is contract evidence only: the connector did not expose its upstream method, project tier, actual quota debit, or billing account.

## Direct connector micro-baseline

One bounded call used:

- query: nonsecret project token `HFO`
- `topn=1`
- `item_type=document`
- `best_effort_fetch=false`
- `require_viewed_by_user=false`
- no page token
- no advanced filter

Observed:

- exactly one result returned;
- visible metadata included a title, Google URL/display URL, and parent identifier array;
- no file body or hydrated text was returned;
- the returned URL was spreadsheet-backed, establishing that connector `item_type=document` is a broad connector category and must not be interpreted as Google Docs MIME type;
- no typed MIME type, `nextPageToken`, `incompleteSearch`, modified time, ownership, permission, HTTP status, headers, request ID, latency, attempt count, or quota counters were exposed.

The exact file title, file ID, URL, and parent ID are intentionally not persisted in this event.

## Admitted interpretation

`CONNECTOR_RETURNED_ONE_METADATA_RESULT_FOR_ONE_BOUNDED_DOCUMENT_CATEGORY_SEARCH_WITH_NO_FILE_CONTENT_RETURNED`

This does not establish completeness, stable ordering, exact upstream query translation, shared-drive coverage, pagination state, least privilege, raw-provider parity, actual quota usage, or absence of hidden calls.

## Gates

1. Treat `item_type=document` as connector taxonomy, not a MIME guarantee.
2. Do not infer terminal pagination when `nextPageToken` is not exposed.
3. Do not infer complete search when `incompleteSearch` is not exposed.
4. Persist no file title, ID, URL, parent ID, owner, or content without a named retention need.
5. Require a raw same-principal Drive witness for high-assurance absence or completeness claims.
6. Award no operational or fitness credit without a named consumer, acknowledgment, and measured operator time removed.

## Measurements

- custom code avoided: estimated 25–70 LOC for OAuth/query/paging/result-shape glue, unvalidated;
- operator minutes removed: 0 measured;
- credentials: connector-managed; principal and OAuth scope unknown;
- durability: Git receipt durable, connector search result transient;
- observability: partial metadata only, no provider telemetry;
- portability: low-to-medium due to Google query semantics, opaque page tokens, and connector-specific category/schema;
- direct cost evidence: no charge surfaced;
- official quota evidence: 100 units for `files.list` or Drive MCP `search_files`, but actual connector debit unknown;
- failure behavior: not tested in phase 1;
- verifier: direct connector receipt now; independent raw Drive witness absent;
- consumer: none named or acknowledged.

## Strongest falsifier

A same-principal raw Drive query during the same observation window returns no matching item, materially different category semantics, `incompleteSearch=true`, or a continuation state inconsistent with the connector result.

## Honest flaw

This is one easy positive lookup capped at one item. It reveals neither completeness nor paging and cannot distinguish Google provider behavior from connector filtering or normalization.

## Next bounded wake

Phase 2: one metadata-only document-category search using a synthetic unlikely nonsecret token expected to return zero results. No pagination, hydration, retry, fallback, persistence of exact file metadata, or mutation.
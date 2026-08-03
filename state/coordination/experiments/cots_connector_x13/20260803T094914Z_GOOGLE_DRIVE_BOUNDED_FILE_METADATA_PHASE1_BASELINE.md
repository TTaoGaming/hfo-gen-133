---
schema_id: hfo.gen133.x13.cots_connector_event.v1
experiment_id: X13_GOOGLE_DRIVE_BOUNDED_FILE_METADATA_SEARCH_READONLY_001
event_type: PHASE1_OFFICIAL_CONTRACT_AND_DIRECT_CAPABILITY_BASELINE
candidate: Google_Drive_bounded_file_metadata_search_readonly_surface
phase: 1_of_4
disposition: PHASE1_ACCEPTED_WITH_PRIVACY_SCOPE_AND_OBSERVABILITY_GATES
carrier_task_id: 6a55c1733708819185088bf334e33ea5
carrier_task_id_match: true
wip: 1
expected_current_version: 60
next_current_version: 61
valid_time_utc: 2026-08-03T09:49:14Z
transaction_time_utc: SEE_GIT_COMMIT_METADATA
mutation_effect: false
paid_cost_usd_observed: 0_NO_CHARGE_SURFACED
operator_minutes_removed_measured: 0
fitness_credit: 0_PENDING_SOURCE_BOUND_CONSUMER_ACK_AND_MEASURED_OPERATOR_OUTCOME
---

# X13 Google Drive bounded file-metadata search — phase 1 baseline

## Official contract baseline

Google Drive API v3 `files.list` is a read-only list/search method. It accepts a `q` filter, `pageToken`, corpus and Drive-selection controls, and a response field mask. The service may return fewer files than the requested page size. A populated `nextPageToken` means another page exists; `incompleteSearch=true` means some results may be missing. By default, `files.list` includes trashed files unless the query excludes them.

Official references checked 2026-08-03:

- https://developers.google.com/workspace/drive/api/reference/rest/v3/files/list
- https://developers.google.com/workspace/drive/api/guides/search-files
- https://developers.google.com/workspace/drive/api/guides/api-specific-auth
- https://developers.google.com/workspace/drive/api/guides/limits

Published post-2026-05-01 limits, when applicable to the connector's project class, are 1,000,000 quota units per minute per project, 325,000 per minute per user per project, and a 400,000,000-unit daily billing threshold. `files.list` is documented at 100 quota units. Legacy-project exceptions remain possible. The connector exposed no project class, live quota counter, request ID, retry headers, or billing meter.

## Direct connector receipt

One bounded connector call was made with:

- action: `Google_Drive.search`
- keyword class: project-specific non-secret token
- item type: `document`
- page cap requested through wrapper: `topn=1`
- content hydration: disabled (`best_effort_fetch=false`)
- viewed-by-user restriction: disabled
- page token input: none

Observed:

- metadata records returned: 1
- content/body text returned: false
- metadata field classes exposed by default: title/name, direct URL, display title, display URL, parent identifiers
- exact file name, file URL, file ID, and parent IDs persisted to Git or Slack: false
- next-page-token presence: NOT_EXPOSED_IN_RETURNED_RESPONSE_RESOURCE
- `incompleteSearch` presence: NOT_EXPOSED
- MIME type, modified time, ownership, sharing state, trashed state, corpus, Drive ID, capabilities, and permission role: NOT_EXPOSED_IN_RETURNED_RESPONSE_RESOURCE
- connector success/error normalization: success observed; raw HTTP status and provider body hidden
- connector latency: NOT_EXPOSED
- carrier retries: 0
- mutation: none

## Measured Andon

The wrapper's explicit `item_type=document` path is contractually metadata-only, and the direct result contained no file body. However, it returned private-identifying metadata fields by default, including names, URLs, and parent identifiers. Count-only or existence-only consumers must minimize the response in memory before durable logging or Slack fan-out.

The response resource also did not expose `nextPageToken` or Drive's `incompleteSearch` flag. Therefore this phase proves one positive wrapper-visible metadata match, not completeness, single-page finality, or parity with raw `files.list` or the Drive UI.

## Measurement

- custom code avoided estimate: 30–100 LOC for authenticated bounded metadata discovery, unvalidated
- operator minutes removed measured: 0
- credentials: pre-authenticated connector; identity, OAuth scope, token custody, corpus and shared-drive reach unknown
- durability: ephemeral point-in-time metadata lookup; not a snapshot, event stream, checkpoint, or durable index
- observability: result count and returned field classes visible; raw request, field mask, query translation, page token, incomplete-search flag, latency, request ID, quota headers and upstream retries hidden
- portability: medium for generic file discovery; low-to-medium for Drive query, token, corpus and permission semantics
- failure behavior: positive success path observed only; empty, malformed query/token, permission, rate-limit and transient failures untested
- direct cost/quota evidence: no charge surfaced; official `files.list` cost is 100 quota units under the current published model, but actual connector consumption and project class are unknown
- verifier: raw Drive `files.list` with equivalent query and explicit minimal fields, one source-bound page traversal, and Drive UI comparison
- consumers: HFO Drive heritage locator; bounded executive-assistant file discovery; SSOT evidence finder
- strongest falsifier: an equivalent raw API or Drive UI query contradicts the connector result, or connector inspection shows content hydration/private metadata persistence, hidden query rewriting, omitted accessible drives, or an unreported incomplete search
- honest flaw: one keyword query returned one metadata record; exact query translation, field mask, pagination, incomplete-search state, corpus, shared-drive behavior, trash handling, effective scope, permission failure, rate limits, independent verification, ConsumerAck and operator-time reduction remain unproven

## Gates admitted now

1. Use explicit metadata-only item type and keep content hydration disabled.
2. Keep page caps small and record the exact non-secret query class and observation time.
3. Minimize names, URLs, file IDs and parent IDs before Git, Slack or downstream fan-out unless the consumer explicitly needs them.
4. Do not infer completeness, corpus coverage, shared-drive coverage, trash exclusion, permission role, ownership, or least privilege from one positive result.
5. Treat absence of a visible cursor or `incompleteSearch` field as unknown, not false.
6. Require source-bound ConsumerAck and measured operator outcome before fitness credit.

## Next wake

Phase 2: one smallest harmless read-only metadata micro-use using an explicit Drive `q` filter that excludes trashed items and a one-result cap. Persist only result count, returned field classes, and whether cursor or incomplete-search evidence is exposed. No content fetch, upload, edit, move, rename, share, permission change, delete, export, publication, or secret exposure.

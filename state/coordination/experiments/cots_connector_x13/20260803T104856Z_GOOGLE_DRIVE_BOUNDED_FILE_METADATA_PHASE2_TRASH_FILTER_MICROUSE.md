---
schema_id: hfo.gen133.x13.cots_connector_event.v1
experiment_id: X13_GOOGLE_DRIVE_BOUNDED_FILE_METADATA_SEARCH_READONLY_001
event_type: PHASE2_SMALLEST_HARMLESS_READONLY_MICRO_USE
candidate: Google_Drive_bounded_file_metadata_search_readonly_surface
phase: 2_of_4
disposition: PHASE2_ACCEPTED_WITH_FILTER_FORWARDING_AND_WRAPPER_TAXONOMY_GATES
carrier_task_id: 6a55c1733708819185088bf334e33ea5
carrier_task_id_match: true
wip: 1
expected_current_version: 61
next_current_version: 62
valid_time_utc: 2026-08-03T10:48:56Z
transaction_time_utc: SEE_GIT_COMMIT_METADATA
mutation_effect: false
paid_cost_usd_observed: 0_NO_CHARGE_SURFACED
operator_minutes_removed_measured: 0
fitness_credit: 0_PENDING_SOURCE_BOUND_CONSUMER_ACK_AND_MEASURED_OPERATOR_OUTCOME
---

# X13 Google Drive bounded file-metadata search — phase 2 trash-filter micro-use

## Direct connector receipt

One bounded read-only connector call was made with:

- action: `Google_Drive.search`
- keyword class: project-specific non-secret token
- item type: `document`
- raw Drive `q` filter: `trashed = false`
- wrapper page cap: `topn=1`
- content hydration: disabled (`best_effort_fetch=false`)
- viewed-by-user restriction: disabled
- page token input: none

Observed:

- metadata records returned: 1
- content/body text returned: false
- metadata field classes exposed: title/name, direct URL, display title, display URL, parent identifiers
- returned provider resource class visible from URL pattern: Google Sheets spreadsheet
- exact private title, URL, file ID, spreadsheet ID, and parent IDs persisted to Git or Slack: false
- next-page-token presence: NOT_EXPOSED_IN_RETURNED_RESPONSE_RESOURCE
- `incompleteSearch` presence: NOT_EXPOSED
- returned file's `trashed` field: NOT_EXPOSED
- raw HTTP status, provider body, request ID, latency, quota headers, and upstream retries: NOT_EXPOSED
- carrier retries: 0
- mutation: none

## Official contract check

Google Drive API v3 `files.list` accepts a `q` filter. Google documents that the method includes trashed files by default and that `trashed=false` removes trashed files from results. The response can include `nextPageToken` and `incompleteSearch`; a populated token means another page may exist, and `incompleteSearch=true` means results may be missing.

Official references checked 2026-08-03:

- https://developers.google.com/workspace/drive/api/reference/rest/v3/files/list
- https://developers.google.com/workspace/drive/api/guides/search-files
- https://developers.google.com/workspace/drive/api/guides/ref-search-terms

## Measured facts and Andons

1. The wrapper accepted the explicit `trashed = false` filter and returned one metadata record without content hydration.
2. The returned response did not expose the file's `trashed` state, the raw upstream request, or a Drive UI/raw API comparison. Therefore this run does not independently prove that the connector forwarded or enforced the filter; it proves only a positive wrapper-visible result under the supplied filter input.
3. `item_type=document` returned a Google Sheets resource. The wrapper's `document` taxonomy is broader than the exact Google Docs MIME type. Consumers needing an exact provider type must use an explicit MIME-type `q` filter and still verify the returned type; the observed response did not expose MIME type.
4. Private-identifying metadata remained present by default and was minimized before durable logging.
5. Cursor and incomplete-search state remained hidden, so no completeness claim is admitted.

## Measurement

- custom code avoided estimate: 35–110 LOC for authenticated bounded metadata search plus a caller-supplied trash filter, unvalidated
- operator minutes removed measured: 0
- operator minutes removed estimated per consumed file-presence check: 1–3, unvalidated
- credentials: pre-authenticated connector; identity, OAuth scope, token custody, corpus and shared-drive reach unknown
- durability: ephemeral point-in-time metadata lookup; not a snapshot, event stream, checkpoint, or durable index
- observability: result count, returned field classes, provider URL class and normalized success visible; raw request, filter forwarding, MIME type, trashed state, field mask, cursor, incomplete-search flag, latency, request ID, quota headers and upstream retries hidden
- portability: medium for generic file discovery; low-to-medium for Drive query, MIME, corpus, token and permission semantics
- failure behavior: positive filtered success observed only; valid empty, malformed query/token, permission, rate-limit and transient failures untested
- direct cost/quota evidence: no charge surfaced; actual connector request count, quota units, project class and billing meter unknown
- verifier: raw Drive `files.list` with equivalent keyword and `trashed=false`, explicit minimal fields including `id,name,mimeType,trashed`, plus Drive UI comparison
- consumers: HFO Drive heritage locator; bounded executive-assistant file discovery; SSOT evidence finder
- strongest falsifier: raw API or Drive UI shows the returned item is trashed, the connector dropped or rewrote `trashed=false`, or an exact MIME query contradicts the wrapper's `document` classification
- honest flaw: one positive result cannot validate filter forwarding, trash exclusion, exact MIME semantics, completeness, corpus/shared-drive reach, permissions, quota behavior, ConsumerAck, or operator-time reduction

## Gates admitted now

1. Keep explicit `trashed=false` for non-trash discovery, but treat filter enforcement as unverified until raw API/UI parity is observed.
2. Treat wrapper `item_type=document` as a broad document-family selector, not an exact Google Docs MIME guarantee.
3. Add an explicit MIME-type `q` filter when the consumer requires Google Docs, Sheets, Slides, PDF, or another exact provider class.
4. Keep content hydration disabled and minimize names, URLs, file IDs and parent IDs before Git, Slack or downstream fan-out.
5. Treat absent cursor, `incompleteSearch`, MIME type, and `trashed` fields as unknown, not false.
6. Require source-bound ConsumerAck and measured operator outcome before fitness credit.

## Next wake

Phase 3: one read-only connector-variance/failure probe using a syntactically valid but impossible MIME-type plus `trashed=false`, one-result cap, no page token and no retry. The admitted outcome must distinguish a valid empty wrapper result from explicit connector/provider failure without inferring corpus completeness. No content fetch, upload, edit, move, rename, share, permission change, delete, export, publication, or secret exposure.

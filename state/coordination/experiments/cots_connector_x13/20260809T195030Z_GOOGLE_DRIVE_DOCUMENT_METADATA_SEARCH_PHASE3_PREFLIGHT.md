---
schema_id: hfo.gen133.x13.cots_connector_event.v1
experiment_id: X13_GOOGLE_DRIVE_DOCUMENT_METADATA_SEARCH_READONLY_029
event_type: PHASE3_PREFLIGHT
expected_current_version: 214
candidate: Google_Drive.search_document_metadata_readonly
campaign_wake: 3_of_4
wip: 1
candidate_request_sha256: f1b655f8b8bdd8f94629f2e5f861cdf6cd2e6a9f3a9d63bf640a82c98d75a38d
candidate_invocations_authorized_this_wake: 1
probe_class: CONNECTOR_VARIANCE_PORTABILITY
mutation_allowed: false
content_fetch_allowed: false
page2_allowed: false
raw_metadata_persistence_allowed: false
phase_status: PREFLIGHT_WRITTEN_PENDING_DIRECT_PROBE
valid_time_utc: 2026-08-09T19:50:30Z
recorded_time_utc: 2026-08-09T19:50:30Z
---

# X13 Phase 3 preflight — Drive MIME-filter variance probe

Run exactly one bounded, harmless, read-only `Google_Drive.search` call with the frozen canonical request below:

```json
{"best_effort_fetch":false,"item_type":"document","query":"HFO","special_filter_query_str":"mimeType = 'application/vnd.google-apps.document'","topn":5}
```

Purpose: test whether the connector's exposed raw Drive `q` filter can narrow the broader connector `item_type=document` taxonomy to actual Google Docs MIME semantics without custom code or content hydration.

Official Google Drive contract baseline: Drive v3 `files.list` accepts a `q` search expression, and `mimeType` is a supported query term; Google documents `application/vnd.google-apps.document` as the Google Docs MIME type and `application/vnd.google-apps.spreadsheet` as Google Sheets.

Primary references:
- https://developers.google.com/workspace/drive/api/guides/search-files
- https://developers.google.com/workspace/drive/api/guides/mime-types
- https://developers.google.com/workspace/drive/api/reference/rest/v3/files/list

Gates: one provider page only; `topn=5`; no content fetch; no second page; no Drive mutation; do not persist raw names, IDs, URLs, parent IDs, snippets, or page tokens. If the connector rejects the raw filter or still returns non-Docs MIME resources, record an Andon and fail closed on Google-Docs-only classification.

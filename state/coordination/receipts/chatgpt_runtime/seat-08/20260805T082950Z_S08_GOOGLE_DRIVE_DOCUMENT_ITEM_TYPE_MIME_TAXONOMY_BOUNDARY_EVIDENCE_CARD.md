---
schema_id: hfo.gen133.s08.evidence_card.v1
task_id_expected: 6a526109ba348191b5f23ad3172ad568
task_id_observed: 6a526109ba348191b5f23ad3172ad568
task_id_match: true
seat: 08
wip: 1
lane: agent_runtime_cots_capabilities
question: DOES_GOOGLE_DRIVE_SEARCH_ITEM_TYPE_DOCUMENT_MEAN_GOOGLE_DOCS_ONLY_OR_A_BROADER_CONNECTOR_DEFINED_CLASS
question_changed_by: X13_GOOGLE_DRIVE_SEARCH_READONLY_002_PHASE1_OBSERVED_A_GOOGLE_SHEETS_RESOURCE_UNDER_ITEM_TYPE_DOCUMENT
candidate: Google_Drive.search
candidate_surface: metadata_only_search_with_item_type_document
connector_build_or_version: NOT_EXPOSED
upstream_api: Google_Drive_API_v3_files.list
upstream_version: v3
x13_experiment: X13_GOOGLE_DRIVE_SEARCH_READONLY_002
x13_current_version: 107
x13_current_commit_observed: c3c3e5e14c9a380d1160378ae889bc80c2257ec7
decision: REVISE
valid_time_utc: 2026-08-05T08:29:50Z
recorded_time_utc: 2026-08-05T08:29:50Z
expiry_utc: 2026-08-12T08:29:50Z
consumer: X13_GOOGLE_DRIVE_SEARCH_READONLY_002_PHASE4_DECISION_AND_HFO_COTS_CAPABILITY_INVENTORY
verifier: DISTINCT_AUTHORIZED_SYNTHETIC_DRIVE_MIME_CLASSIFICATION_VERIFIER
fitness_credit: 0_PENDING_WORKITEM_CONSUMPTION_AND_CONSUMER_ACK
paid_cost_usd_observed: 0
operator_minutes_this_pass: 0
producer_revision_estimate_minutes: 10_to_20
verification_estimate_minutes: 30_to_60
license_terms_uncertainty: GOOGLE_DEVELOPER_DOCUMENTATION_CC_BY_4_0_AND_CODE_SAMPLES_APACHE_2_0; DRIVE_API_WORKSPACE_TERMS_CONNECTOR_RETENTION_TELEMETRY_IDENTITY_SCOPE_AND_CREDENTIAL_CUSTODY_NOT_EVALUATED
---

# REVISE — `item_type=document` is a connector taxonomy, not a Google Docs MIME contract

## Bounded uncertainty

Does `Google_Drive.search(item_type="document")` guarantee Google Docs-only results, or does it represent a broader connector-defined class?

## Evidence

1. The connector schema available on 2026-08-05 defines `item_type` only as `image | document | folder`. It says an explicit item type searches one metadata-only provider page and does not fetch file contents. It does **not** expose the MIME mapping, connector build, provider query, or returned `mimeType`.
2. X13 phase 1, exact experiment `X13_GOOGLE_DRIVE_SEARCH_READONLY_002`, recorded that `item_type=document` returned a Google Sheets resource. The durable receipt deliberately retained no private result values. Exact event: `state/coordination/experiments/cots_connector_x13/20260805T054953Z_GOOGLE_DRIVE_SEARCH_METADATA_PHASE1_ACCEPTED_WITH_GATES.md`, blob `36450fa813aa57205df11c65011ec9cbbfa03e30`.
3. Google Drive API v3 models Google Docs and Google Sheets as distinct MIME types: `application/vnd.google-apps.document` and `application/vnd.google-apps.spreadsheet`. Google documents `mimeType` as a supported `files.list` query term and shows exact MIME filtering when type precision is required.

## Dated primary sources

- Google, **Google Workspace and Google Drive supported MIME types**, last updated 2026-05-07: https://developers.google.com/workspace/drive/api/guides/mime-types
- Google, **Search for files and folders**, last updated 2026-05-07: https://developers.google.com/workspace/drive/api/guides/search-files
- Google, **Manage file metadata**, last updated 2026-04-20: https://developers.google.com/workspace/drive/api/guides/file-metadata
- Google, **Method: files.list**, accessed 2026-08-05: https://developers.google.com/workspace/drive/api/reference/rest/v3/files/list

## Supported claims

- `item_type=document` is broader than the exact Google Docs MIME type in the observed connector surface.
- A Google Sheets resource can be returned under that connector category.
- The explicit item-type path is metadata-only according to the exposed connector schema.
- Exact file-type selection in raw Drive API v3 is expressible through a `mimeType` query.

## Excluded claims

- The complete membership of the connector's `document` category.
- Whether it includes Slides, PDFs, Office files, Forms, Drawings, shortcuts, or arbitrary non-image files.
- Stable mapping across connector releases.
- That the wrapper forwards an exact MIME filter, preserves provider `mimeType`, searches one corpus, or has raw `files.list` parity.
- Content type, semantic document identity, canonicality, freshness, uniqueness, completeness, or safe downstream parser choice from `item_type=document` alone.

## Required revision

Classify the surface as:

```text
CONNECTOR_DOCUMENT_CLASS_METADATA_SEARCH
NOT_GOOGLE_DOCS_ONLY
EXACT_MIME_TYPE_UNKNOWN_UNLESS_RETURNED_OR_EXPLICITLY_FILTERED
```

For X13 phase 4:

- Do not catalog `item_type=document` as `GOOGLE_DOCS_SEARCH`.
- Treat the category as connector-defined and version-unbound.
- Require returned provider MIME type or an explicit `special_filter_query_str` MIME predicate before selecting a type-specific parser, exporter, or workflow.
- If exact MIME evidence is absent, route only to human-reviewed metadata discovery and preserve `TYPE_UNKNOWN_WITHIN_DOCUMENT_CLASS`.

## Strongest objection

A broad product-level `document` category may be intentional and useful because users often expect spreadsheets and PDFs to count as documents.

That objection is valid for discovery UX. It does not justify treating the category as a Google Docs MIME guarantee or dispatching results into type-specific automation without a returned or explicitly constrained MIME type.

## Falsifier

Retire this revision if a version-bound connector contract publishes the exact `document` MIME mapping and a distinct authorized synthetic corpus test proves stable classification across Google Docs, Sheets, Slides, PDFs, Office files, shortcuts, and folders while surfacing the provider MIME type or enforcing an equivalent exact filter.

## Cost and operational estimate

- Research pass: `$0`, `0` operator minutes.
- Catalog/schema wording revision: `10–20` producer minutes.
- Synthetic classification matrix plus same-principal raw `files.list` parity: `30–60` verifier minutes, assuming an authorized pre-existing test corpus.
- No claim of operator time removed or revenue created.

## Decision

`REVISE`

Operational credit remains zero until an exact WorkItem consumes this card, a distinct verifier closes the MIME mapping uncertainty, and a ConsumerAck is recorded.

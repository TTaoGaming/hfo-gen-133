---
schema_id: hfo.gen133.s08.evidence_card.v1
seat: S08
role: RESEARCH_AND_CANDIDATE_SCOUT
carrier_task_id_expected: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_observed: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_match: true
wip: 1
valid_time_utc: 2026-08-03T11:27:30Z
transaction_time_utc: SEE_GIT_COMMIT_METADATA
canonical_repository: TTaoGaming/hfo-gen-133
canonical_branch: agent/gen133-bootstrap-20260730
lane: agent-runtime/COTS capabilities
research_question: What deterministic syntactically-valid Google Drive v3 q control should X13 use to distinguish a valid empty search from a malformed-query or connector failure without relying on an invented MIME type being absent?
result: REVISE
candidate: Google_Drive.search phase-3 valid-empty control query
candidate_version: connector schema observed 2026-08-03; Google Drive API v3 documentation last updated 2026-07-07 and query-term reference last updated 2026-04-20
source_changed_input:
  commit: 33f8ce7ef34f8d799a2a0a43e1e177510185ddf5
  path: state/coordination/experiments/cots_connector_x13/20260803T104856Z_GOOGLE_DRIVE_BOUNDED_FILE_METADATA_PHASE2_TRASH_FILTER_MICROUSE.md
  blob_sha: 0c776fade8b5548c0c30a8def682ba8febe812ff
  changed_question: Phase 3 proposed a syntactically valid but impossible MIME-type query plus trashed=false.
consumer: X13_GOOGLE_DRIVE_BOUNDED_FILE_METADATA_SEARCH_READONLY_001_PHASE3_VALID_EMPTY_VS_ERROR_GATE
verifier: DISTINCT_RAW_GOOGLE_DRIVE_FILES_LIST_CLIENT_OR_NON_CHATGPT_PROVIDER_WITNESS
expiry_utc: 2026-08-10T11:27:30Z
fitness_credit: 0_PENDING_EXACT_WORKITEM_CONSUMPTION_AND_CONSUMER_ACK
---

# S08 evidence card — deterministic Drive valid-empty control

## Decision

`REVISE`

Replace an invented supposedly impossible MIME value with a logically contradictory but individually valid Drive v3 query:

```text
mimeType = 'application/vnd.google-apps.folder' and
mimeType != 'application/vnd.google-apps.folder' and
trashed = false
```

The Drive v3 query reference explicitly admits `and`, `=`, and `!=`; `mimeType` admits `=` and `!=`; and `trashed` admits boolean equality. Therefore each token and predicate is documented syntax. Because one file cannot have a MIME type both equal and unequal to the same exact value, the conjunction is a deterministic empty-set control under ordinary provider semantics.

## Dated primary sources

Checked 2026-08-03:

1. Google Drive API v3 `files.list`, last updated 2026-07-07: `q` filters returned files; successful responses contain `files[]`, optional `nextPageToken`, and `incompleteSearch`. The service can return fewer than the page-size ceiling, and missing-result/completeness claims require cursor and incomplete-search handling.
   - https://developers.google.com/workspace/drive/api/reference/rest/v3/files/list
2. Google Drive query terms and operators, last updated 2026-04-20: `and`, `=`, and `!=` are valid operators; `mimeType` supports `contains`, `=`, and `!=`; `trashed` supports `=` and `!=` with boolean values.
   - https://developers.google.com/workspace/drive/api/guides/ref-search-terms
3. Google Drive error handling, checked 2026-08-03: successful requests use HTTP 200; invalid or unacceptable request parameters can produce HTTP 400 `badRequest`; authentication, permission, quota, rate-limit, and server errors are separate classes.
   - https://developers.google.com/workspace/drive/api/guides/handle-errors

## Supported claims

- The proposed contradictory expression is composed only of documented Drive v3 query terms and operators.
- A raw Drive implementation honoring normal boolean conjunction and exact string equality should return a successful empty `files[]` set, not a positive match.
- This control is stronger than a fabricated MIME string because Drive can store arbitrary uploaded-file MIME values; absence of a made-up value is probable, not logically guaranteed.
- For the current connector, an empty wrapper return can be classified only as `VALID_EMPTY_WRAPPER_RESULT` when the wrapper reports success rather than an error.

## Excluded claims

- The control does not prove that `special_filter_query_str` was forwarded unchanged.
- An empty wrapper result does not prove corpus completeness, all-drive coverage, shared-drive reach, trash exclusion, permission scope, or provider parity.
- A wrapper error does not prove that the raw Drive API rejects the query; the wrapper may parse, rewrite, narrow, or reject it first.
- A successful empty result does not establish durable cursor semantics, absence across later times, operator relief, fitness, or production readiness.

## Required phase-3 interpretation

Use exactly one metadata-only connector call with the contradictory query, `topn=1`, no content hydration, no page token, and no retry.

- Success plus zero visible records: `VALID_EMPTY_WRAPPER_RESULT`; provider forwarding and completeness remain `UNKNOWN`.
- Success plus one or more records: `CONTRADICTION_ANDON`; either forwarding/rewriting differs, the result taxonomy is not provider-file filtering, or the wrapper response is defective.
- Typed 400-like query error: `WRAPPER_OR_PROVIDER_QUERY_REJECTION`; origin remains unknown unless raw status/body is exposed.
- Authentication, permission, quota, rate-limit, or transient error: classify separately; do not relabel as valid empty.
- Any content hydration or durable private identifiers: privacy Andon and stop.

## License and terms uncertainty

Google states its documentation text is CC BY 4.0 and code samples are Apache 2.0. No sample code is copied here. The authenticated connector's OAuth principal, scopes, corpus, quota project, API terms, and wrapper implementation license remain unexposed and `UNKNOWN`. No account, consent, or terms action occurred.

## Cost and operator minutes

- Research external spend observed: `$0`.
- Proposed phase-3 connector calls: `1` read-only call, no retry.
- Direct provider cost/quota: no charge or quota unit is exposed; `UNKNOWN`.
- Operator minutes required: `0`.
- Producer minutes estimated to run, sanitize, persist, and read back: `5–10`.

## Strongest objection

The connector may normalize contradictory predicates, combine hidden `item_type=document` filters, or reject the query before Drive. Even the expected empty result adds little value without a raw-provider parity receipt and a named consumer; repeated wrapper assays risk treadmill research.

## Falsifier

This card falls if an exact raw Drive v3 `files.list` request using the query above returns a matching file under documented semantics, or if Google documents that contradictory same-field predicates are rejected rather than evaluated. The connector-specific recommendation falls if the wrapper cannot accept the exact expression or exposes no success/error distinction.

## Verification packet

A distinct authorized raw client should issue one `files.list` request with:

- exact `q` expression above;
- explicit minimal fields `files(id,mimeType,trashed),nextPageToken,incompleteSearch`;
- recorded HTTP status, provider request ID when available, response digest, corpus, scopes, and timestamp;
- no file bodies, no mutation, and sanitized durable output.

Expected stood result: HTTP 200, zero files, no cursor, `incompleteSearch=false` or an explicitly bounded corpus. Any other result is evidence for revision, not a reason to broaden effects.

## Honest flaw

This is a documentation-and-logic evidence card, not an executed raw Drive assay. The current ChatGPT connector hides raw request translation, HTTP status/body, field mask, scope, corpus, and upstream request identity, so independent provider equivalence remains open.

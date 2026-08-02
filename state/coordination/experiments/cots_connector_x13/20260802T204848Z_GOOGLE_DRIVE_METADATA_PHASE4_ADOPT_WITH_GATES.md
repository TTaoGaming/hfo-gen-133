---
schema_id: hfo.gen133.x13.cots_connector_event.v1
experiment_id: X13_GOOGLE_DRIVE_BOUNDED_METADATA_SEARCH_READONLY_001
event_type: PHASE4_DECISION
phase: 4_of_4
decision: ADOPT_WITH_GATES
prior_current_version: 47
expected_current_version: 48
carrier_task_id: 6a55c1733708819185088bf334e33ea5
carrier_task_id_match: true
candidate: Google_Drive_bounded_metadata_only_search_connector_surface
capability_call_this_phase: false
wip: 1
valid_time_utc: 2026-08-02T20:48:48Z
transaction_time_utc: SEE_GIT_COMMIT_METADATA
sealed: true
---

# X13 Google Drive bounded metadata search — phase 4 decision

## Decision

`ADOPT_WITH_GATES`

Adopt the connected Google Drive surface only for bounded, read-only metadata discovery with an explicit item type, small result cap, one provider page, and `best_effort_fetch=false`.

Do not treat this surface as a complete Drive inventory, durable snapshot, identity proof, least-privilege proof, content-reading authority, or write authority.

No additional Drive capability call was made in this phase. The decision uses the three prior direct receipts and a fresh read of Google's official `files.list`, error-handling, and usage-limit contracts.

## Evidence admitted

1. Phase 1 returned three metadata records for a bounded `HFO` document search with no content hydration or Drive mutation.
2. Phase 2 returned one metadata record at `topn=1`; no connector-visible continuation token appeared. Missing cursor visibility did not prove enumeration completeness.
3. Phase 3 used a synthetic non-provider page token. The provider failed closed with HTTP `400` / `INVALID_ARGUMENT`, located the invalid input at `pageToken`, returned no files or cursor, and caused no Drive mutation.
4. The phase-3 error exposed a raw request URL. That receipt showed `topn=1` mapped to `pageSize=1` for that call, the connector used `corpora=allDrives`, and the field mask omitted `incompleteSearch`.
5. Google's official `files.list` contract states that `pageSize` is a maximum, `pageToken` must come from the preceding `nextPageToken`, rejected tokens should be discarded and pagination restarted, result membership may change, and `incompleteSearch=true` means results might be missing.
6. Google's official error guide classifies HTTP `400` as a client-request error requiring correction rather than unchanged retry. Its usage-limit guide currently assigns 100 quota units to `files.list` under the post–May 1, 2026 model, while older active projects may retain prior quotas.

Official primary references checked this wake:

- https://developers.google.com/workspace/drive/api/reference/rest/v3/files/list
- https://developers.google.com/workspace/drive/api/guides/handle-errors
- https://developers.google.com/workspace/drive/api/guides/limits

## Admitted scope

- Bounded read-only metadata search.
- Explicit metadata-only item type.
- Small explicit `topn`.
- One provider page.
- `best_effort_fetch=false`.
- Timestamped discovery observation only.
- Separate later authorization required before any content read.

## Mandatory gates

- Treat names, IDs, URLs, parent IDs, resource keys, and folder relationships as sensitive metadata.
- Keep `best_effort_fetch=false`; do not hydrate text or file content.
- Treat the connector's default search corpus as all accessible drives because the direct request used `corpora=allDrives`.
- Do not claim completeness while `incompleteSearch` is omitted from the connector field mask.
- Treat `topn` as a connector result cap, not a global ABI guarantee for raw `pageSize`.
- Accept a page token only from the immediately preceding admitted response for the identical account, query, item type, corpus, field set, and page context.
- Never synthesize, parse, reconstruct, persist by default, or reuse a rejected token.
- On token rejection, discard it and restart from page one or abort; do not retry unchanged.
- Redact page tokens and full provider request URLs from Git, Slack, traces, and routine logs.
- Do not infer account identity, OAuth scope, ownership, write authority, project, quota class, billing state, or credential custody from a successful search.
- Treat results across wakes as mutable observations, not stable snapshots.
- Keep content reads, downloads, exports, spreadsheet reads, uploads, moves, renames, permission changes, ownership changes, Trash, and deletion outside the admitted capability.
- Separate client-input, authentication, authorization, quota, rate-limit, and transient server failures.

## Measurements

| Dimension | Result |
|---|---|
| Custom code avoided | Estimated 30–100 LOC for authenticated query/metadata normalization plus 20–70 LOC for pagination/error handling; unvalidated and non-additive |
| Operator minutes removed | 0 measured |
| Estimated future operator relief | 1–5 minutes per bounded discovery; unvalidated |
| Credentials | Authenticated provider path worked; account identity, OAuth scope, project, delegated authority, and credential custody remain unknown |
| Durability | Ephemeral point-in-time metadata observation over mutable Drive and search-index state |
| Observability | Medium on the phase-3 error path; low on success-path completeness, identity, scope, request ID, retries, latency, and quota |
| Portability | Medium-low; Drive query, MIME, corpus, file ID, parent, resource-key, and page-token semantics are provider-specific |
| Failure behavior | Synthetic invalid token failed closed with parameter-level evidence and no content or mutation; raw request URL leakage is an Andon |
| Direct cost/quota evidence | $0 surfaced; official new-model `files.list` cost is 100 units, but live project class, actual units, retries, billing, and counters are unknown |
| Fitness credit | 0 pending explicit source-bound ConsumerAck and measured operator outcome |

## Verifier, consumer, falsifier

- **Verifier:** source-bound raw Google Drive `files.list` or a distinct authorized client using the identical account, query, corpus, fields, page size, and completeness fields.
- **Consumer:** HFO bounded file discovery and PARA/heritage routing, with separate content authorization.
- **Strongest falsifier:** a source-bound raw or distinct client shows materially different query membership, corpus, pagination, completeness, or error semantics for the same account and request.

## Honest flaw

No valid next-page traversal, genuinely expired token, query/token mismatch, `401`, `403`, `429`, `5xx`, source-bound account identity, OAuth-scope proof, independent readback, or ConsumerAck was completed. Success-path latency and live quota evidence remain hidden. The connector's omission of `incompleteSearch` blocks completeness claims, and its raw error URL can leak opaque tokens unless downstream logging redacts them.

## Final disposition

Use the connector as a narrow discovery COTS component. Do not build a custom Drive listing client for this admitted use unless a falsifier closes against the connector. Keep policy, identity, content authorization, completeness, token binding, redaction, and failure classification outside the connector contract.

## Next queued campaign

`X13_GITHUB_ACTIONS_WORKFLOW_RUN_STATUS_READONLY_001`

Phase 1 should establish the official workflow-run/list contract and perform one bounded read-only latest-run metadata baseline against the canonical repository and branch. No dispatch, rerun, cancel, artifact download, secret read, branch mutation, or workflow mutation.

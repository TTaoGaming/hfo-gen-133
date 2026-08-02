---
schema_id: hfo.gen133.x13.cots_connector_event.v1
experiment_id: X13_GMAIL_BOUNDED_METADATA_SEARCH_READONLY_001
event_type: PHASE3_FAILURE_PERMISSION_PORTABILITY_CONNECTOR_VARIANCE_PROBE
version_from: 42
version_to_expected: 43
candidate: Gmail_bounded_exact_query_metadata_readonly_connector_surface
carrier_task_id: 6a55c1733708819185088bf334e33ea5
carrier_task_id_match: true
valid_time_utc: 2026-08-02T15:49:19Z
transaction_time_utc: SEE_GIT_COMMIT_METADATA
phase: 3_of_4
status: PHASE3_ACCEPTED_WITH_OPAQUE_CURSOR_AND_NORMALIZED_ERROR_GATES
sealed: true
---

# X13 Gmail bounded metadata search — phase 3

## Direct privacy-safe failure probe

The same bounded historical query used in phases 1 and 2 was submitted with `max_results=1` and a synthetic invalid page token. The token contained no secret or mailbox-derived value.

Direct normalized connector result:

- result type: `google_api_error`
- code: `invalidArgument`
- status: `INVALID_ARGUMENT`
- reason: `invalidArgument`
- message: `Failed to search email ids`
- message IDs returned: `0`
- continuation token returned: `false`
- message headers, sender, subject, snippet, body, attachments: not returned
- mailbox mutation: none
- carrier-level retries: `0`
- synthetic token echoed in visible error: `false`
- raw HTTP status, headers, request ID, field location, quota headers, and Retry-After: not exposed
- connector latency: not exposed for the failed call
- surfaced cost: `$0`

Because the controlled probe changed only the page token, the invalid token is the strongest causal explanation. However, the connector did not expose a parameter location or raw upstream response, so the exact upstream failure classification remains unverified.

## Official contract and error baseline

Google's current `users.messages.list` contract defines `pageToken` as the token used to retrieve a specific page of list results and returns `nextPageToken` only when another page is available. The official error guide classifies HTTP 400 as a client-request error and says invalid supplied values or invalid parameter combinations can cause it; callers should inspect the error details and correct the request rather than blindly retry it.

Official references checked on 2026-08-02:

- https://developers.google.com/workspace/gmail/api/reference/rest/v1/users.messages/list
- https://developers.google.com/workspace/gmail/api/guides/list-messages
- https://developers.google.com/workspace/gmail/api/guides/handle-errors

The direct connector used gRPC-style normalized fields and suppressed raw HTTP details. Therefore, policy must branch on the stable structured fields actually exposed by the connector while preserving that this is a wrapper-level observation, not a raw Gmail API receipt.

## Failure, permission, portability, and connector variance

- failure behavior: the synthetic invalid cursor failed closed; no result set or mailbox content was returned and no write occurred
- permission behavior: not tested; this probe does not establish mailbox identity, authority, OAuth scope, or access-denial semantics
- portability: low for cursor reuse because Gmail page tokens and wrapper error enums are provider/connector-specific
- connector variance: wrapper returned `invalidArgument` / `INVALID_ARGUMENT` rather than raw HTTP status, error body, parameter location, or provider request ID
- retry behavior: deterministic client-input failure; no retry was attempted and blind retry is not admitted
- leakage behavior: the synthetic token was not echoed in the visible error, but upstream logging and connector retention are unknown

## Measurements

- measured operator relay minutes: `0`
- measured operator minutes removed: `0`
- estimated future relief: `UNKNOWN`
- fitness credit: `0`, pending source-bound ConsumerAck
- custom code avoided estimate: prior `25–80 LOC` for authenticated list/cursor normalization plus `15–50 LOC` for structured error mapping; unvalidated and non-additive
- credentials: connector authentication previously succeeded; mailbox identity, OAuth scope, project, authority, and custody remain unknown
- durability: ephemeral point-in-time query over mutable mailbox/search state; page tokens are not durable records
- observability: normalized type/code/status/reason visible; raw HTTP, request ID, field location, scope, project, live quota, upstream retries, and latency hidden
- direct cost/quota evidence: `$0` surfaced; actual upstream request count and quota counters not exposed
- verifier: raw Gmail `users.messages.list` call or a distinct authorized Gmail client using the same source-bound mailbox and a deliberately invalid synthetic token
- consumer: HFO executive-assistant mail triage and bounded pagination logic
- strongest falsifier: a raw or distinct source-bound client accepts the same synthetic token, returns mailbox results, or exposes a materially different stable error classification
- honest flaw: no valid next-page traversal, expired real token, token/query mismatch, malformed query, permission denial, 401, 403, 429, 5xx, independent client, or ConsumerAck was tested

## Gates added

1. Treat Gmail page tokens as opaque, short-lived continuation capabilities; never synthesize, parse, or reconstruct them.
2. Accept a page token only from the immediately preceding admitted list response for the same mailbox context and exact query parameters.
3. Do not persist page-token values without separate data-minimization and retention justification; persist only presence and bounded traversal state by default.
4. On `invalidArgument` / `INVALID_ARGUMENT`, stop and correct or discard the cursor; do not blindly retry the same request.
5. Do not classify the exact invalid field unless the connector exposes parameter location or an independently verified raw response.
6. Keep permission/authentication failures separate from client-input failures; this probe did not test authority.
7. Sanitize cursor values and mailbox identifiers from Git and Slack receipts.
8. Preserve connector-normalized error fields separately from raw-provider claims.

---
schema_id: hfo.gen133.x13.cots_connector_event.v1
experiment_id: X13_GMAIL_BOUNDED_METADATA_SEARCH_READONLY_001
event_type: PHASE_4_ADOPTION_DECISION
phase: 4_of_4
prior_current_version: 43
next_current_version: 44
valid_time_utc: 2026-08-02T16:49:33Z
carrier_task_id: 6a55c1733708819185088bf334e33ea5
candidate_invocation_this_wake: false
write_side_effect_on_candidate: false
decision: ADOPT_WITH_GATES
sealed: true
---

# Gmail bounded ID-only search phase 4 decision

Decision: `ADOPT_WITH_GATES`.

Admitted use is narrow: bounded, read-only Gmail message-list searches with an exact query, explicit epoch-second bounds, a small result cap, pagination presence tracking, and no message-content retrieval or mailbox mutation. The connector may support privacy-minimized triage discovery, but it is not evidence of mailbox completeness, a stable snapshot, exact authenticated identity, least-privilege OAuth scope, or authority to read or change message content.

Evidence admitted:
- phase 1 returned one opaque message ID for one bounded one-hour query, with no header, sender, subject, snippet, body, attachment, or write side effect;
- phase 2 repeated the same query with `maxResults=1`, returned one opaque ID, and emitted a continuation cursor; the prior wake had no cursor, so search results are timestamped observations rather than immutable snapshots;
- phase 3 used a synthetic non-mailbox-derived invalid page token and failed closed with normalized `invalidArgument` / `INVALID_ARGUMENT`, no message IDs, no cursor, no content, no mutation, and no carrier retry;
- Google documents that `users.messages.list` returns only message `id` and `threadId`, that `nextPageToken` is an opaque page token, and that additional message details require a separate `messages.get` request;
- Google documents that `q` cannot be used with the narrow `gmail.metadata` scope. Because the connector successfully executed a filtered `q` search, the effective authorization is not proven least-privilege metadata-only and may be broader; the exact live scope remains hidden.

Mandatory gates:
1. Use epoch seconds when precise timezone boundaries matter.
2. Treat each search as a timestamped observation over mutable mailbox and search-index state, not a durable snapshot.
3. Set a small explicit result cap and preserve returned count, cap, observation time, and continuation-token presence separately.
4. Never infer completeness from a returned count below the cap, an absent cursor in an earlier wake, or `resultSizeEstimate` without separate validation.
5. Treat page tokens as opaque; never synthesize, parse, reconstruct, or reuse them outside the immediately preceding admitted response for the same mailbox context and exact query parameters.
6. Traverse pages only under an explicit bounded page, time, and data-minimization budget.
7. Do not persist message IDs or page-token values without separate justification; persist token presence by default.
8. On `invalidArgument`, stop and correct or discard the cursor; do not retry unchanged or identify the exact invalid field without parameter-location or raw-response evidence.
9. Keep client-input, authentication, permission, quota, and transient-server failures in separate classes; use bounded backoff only for documented retryable classes.
10. Do not claim exact mailbox identity, OAuth scope, project, credential custody, live quota, billing state, retries, or independent accuracy from connector success.
11. Do not describe this connector binding as `gmail.metadata` least privilege while filtered `q` search succeeds and live scope evidence is absent.
12. No `messages.get`, body, header, snippet, attachment, broad mailbox mining, send, draft, reply, forward, label, archive, Trash, deletion, or read-state mutation under this adoption decision.

Measurements:
- measured operator minutes removed: 0;
- estimated future relief: 1-5 minutes per bounded discovery query, unvalidated;
- custom code avoided estimate: 25-80 LOC for authenticated list-query, cursor extraction, and ID normalization plus 15-50 LOC for normalized error mapping, unvalidated and non-additive;
- surfaced paid cost: $0;
- published method weight: `messages.list` uses 5 quota units, but the live project, quota model, counters, billing state, upstream request count, and retries were not exposed;
- credentials: connector-authenticated filtered search succeeded, but user identity, scope, client/project, authority, and custody remain unknown; successful `q` use is inconsistent with a metadata-only scope claim;
- durability: ephemeral observation over mutable mailbox and index state; cursors are not durable records;
- observability: query bounds, count, cursor presence, latency on successful calls, and normalized error fields were visible; raw HTTP, request ID, exact parameter location, scope, project, rate headers, failed-call latency, and upstream retries were hidden;
- portability: medium-low overall; Gmail query syntax, IDs, thread semantics, cursor binding, scope rules, and normalized errors are provider-specific;
- failure behavior: the synthetic invalid cursor failed closed without content or mutation, but valid next-page traversal, expired real cursors, query-token mismatch, 401/403/429/5xx, and independent cross-client comparison remain untested;
- fitness credit: 0 pending source-bound ConsumerAck and measured operator outcome.

Official references checked on 2026-08-02:
- https://developers.google.com/workspace/gmail/api/reference/rest/v1/users.messages/list
- https://developers.google.com/workspace/gmail/api/guides/handle-errors
- https://developers.google.com/workspace/gmail/api/reference/quota

Verifier: a raw Gmail `users.messages.list` call or a distinct authorized Gmail client using the same source-bound mailbox, exact query, result cap, and deliberately invalid synthetic cursor, with raw response, scope, and request metadata.

Consumer: HFO executive-assistant mail-discovery logic and bounded pagination logic.

Strongest falsifier: a raw or distinct source-bound client accepts the same synthetic invalid token, returns materially different message membership or stable error classification, or shows that the connector silently fetched message content or mutated mailbox state.

Honest flaw: the campaign did not establish identity or least-privilege scope, traverse a valid next page, test a real expired or mismatched cursor, malformed query, 401/403/429/5xx, independent client, message-content non-access at the credential layer, or ConsumerAck. The connector action minimized returned data, but the underlying credential may have broader read or modify authority than the admitted use.

Result: `ADOPT_WITH_GATES` for bounded ID-only discovery only.
---
schema_id: hfo.gen133.x13.cots_connector_event.v1
experiment_id: X13_GMAIL_BOUNDED_METADATA_SEARCH_READONLY_001
event_type: PHASE2_MICRO_USE
version_from: 41
version_to_expected: 42
candidate: Gmail_bounded_exact_query_metadata_readonly_connector_surface
carrier_task_id: 6a55c1733708819185088bf334e33ea5
carrier_task_id_match: true
valid_time_utc: 2026-08-02T14:48:51Z
transaction_time_utc: SEE_GIT_COMMIT_METADATA
phase: 2_of_4
status: PHASE2_ACCEPTED_WITH_PAGINATION_AND_MUTABILITY_ANDON
sealed: true
---

# X13 Gmail bounded metadata search — phase 2

## Direct bounded micro-use

The exact phase-1 epoch-bounded query was repeated with `max_results=1`:

- query class: one historical one-hour window, excluding Spam and Trash
- returned opaque message IDs: `1`
- continuation token emitted: `true`
- message ID persisted: `false`
- continuation token persisted: `false`
- headers, sender, subject, snippet, body, attachments: not requested or returned
- mailbox mutation: none
- carrier-level retries: `0`
- connector external-call time: `574 ms`
- surfaced cost: `$0`

The connector exposes no metadata-only single-message read. Its available single-message read includes the body, so that action was deliberately not invoked under the phase effect ceiling.

## Measured reconciliation and Andon

Phase 1 recorded the same query with `max_results=3` returning one ID and no continuation token. Phase 2 returned one ID at `max_results=1` and emitted a continuation token. This is a measured response difference across wakes.

The direct receipt proves only that a continuation cursor was emitted on this call. It does not prove the exact number of additional messages because the next page was not fetched. The cause is unresolved: mailbox/search-index mutability, later-arriving or reclassified mail inside the historical search interval, connector normalization variance, or another provider-side behavior remain possible.

Therefore, repeated Gmail searches are not admitted as immutable snapshots. Exact query, retrieval time, result cap, continuation-token presence, and any page traversal must be recorded separately.

## Measurements

- measured operator relay minutes: `0`
- measured operator minutes removed: `0`
- estimated future relief: `UNKNOWN`
- fitness credit: `0`, pending source-bound ConsumerAck
- custom code avoided estimate: `25–80 LOC` for authenticated list query, cursor extraction, and ID normalization; unvalidated
- credentials: connector authentication succeeded; mailbox identity, OAuth scope, project, authority, and custody remain unknown
- durability: ephemeral point-in-time query over mutable mailbox/search state
- observability: query bounds, count, continuation-token presence, and connector latency visible; raw HTTP, request ID, headers, scope, project, quota, retries, and billing hidden
- portability: medium-low because Gmail query syntax, identifiers, thread semantics, and pagination are provider-specific
- failure behavior: no error in this phase; pagination-state drift observed relative to phase 1
- direct cost/quota evidence: `$0` surfaced; actual upstream request count and quota counters not exposed
- verifier: raw Gmail `users.messages.list` or distinct authorized client using the same source-bound mailbox and exact epoch query
- consumer: HFO executive-assistant mail triage logic
- strongest falsifier: a distinct source-bound client shows no continuation cursor or materially different page membership for the same mailbox, query, cap, and observation time
- honest flaw: no next page, metadata-only message get, empty result, invalid query, permission denial, rate limit, independent client, or ConsumerAck was tested

## Gates added

1. Treat each Gmail search as a time-stamped observation, not a durable snapshot.
2. Preserve `next_page_token_present` independently from returned count.
3. Never infer completeness from `returned_count < max_results` or from a prior wake.
4. Traverse pages only under an explicit bounded page and data-minimization budget.
5. Do not persist opaque IDs or page tokens without separate justification.
6. Do not call body-returning message reads when metadata-only access is the admitted scope.
7. Do not infer mailbox identity, exact OAuth scope, quota class, or billing state from success.

## Official contract reference

Reuses the phase-1 official Gmail contract references for `users.messages.list`, filtering semantics, and quota. The direct tool receipt is controlling for this phase. Fresh web retrieval was attempted but unavailable due a transient search-service error; no new web-derived claim was added.

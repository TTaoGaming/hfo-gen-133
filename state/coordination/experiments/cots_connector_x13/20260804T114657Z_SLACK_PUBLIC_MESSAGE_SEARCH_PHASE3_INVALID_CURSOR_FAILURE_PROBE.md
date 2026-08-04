---
schema_id: hfo.gen133.x13.cots_connector_event.v1
experiment_id: X13_SLACK_PUBLIC_MESSAGE_SEARCH_READONLY_001
event_id: 20260804T114657Z_SLACK_PUBLIC_MESSAGE_SEARCH_PHASE3_INVALID_CURSOR_FAILURE_PROBE
phase: 3_of_4
expected_prior_version: 86
carrier_task_id: 6a55c1733708819185088bf334e33ea5
carrier_task_id_match: true
wip: 1
candidate: Slack_public_message_search_bounded_readonly_surface
effect_ceiling: ONE_BOUNDED_PUBLIC_READONLY_INVALID_CURSOR_FAILURE_PROBE
valid_time_utc: 2026-08-04T11:46:57Z
recorded_time_utc: 2026-08-04T11:46:57Z
---

# X13 Slack public message search — phase 3 invalid-cursor failure probe

## Bounded action

Executed exactly one read-only `slack_search_public` call against one known public channel with:

- messages only
- limit 1
- concise response
- surrounding context disabled
- one synthetic, nonsecret, deliberately invalid pagination cursor
- no private-channel or DM scope
- no retry, fallback, pagination continuation, persistence of exact query/cursor, or Slack mutation

## Direct measured result

| Measure | Observed |
|---|---|
| Connector completion | Error |
| Connector-visible error text | `execution_failed: internal_error` |
| Connector error flag | `true` |
| Search results returned | 0 |
| Matched content or identifiers returned | 0 |
| Continuation cursor returned | 0 |
| Typed provider error envelope | Not returned |
| HTTP status, headers, request ID | Not exposed |
| Rate-limit or quota telemetry | Not exposed |
| Retries / fallbacks / Slack mutations | 0 / 0 / 0 |
| Paid cost surfaced | $0; no charge surfaced |
| Operator minutes removed, measured | 0 |
| Custom code avoided estimate | 20–60 LOC, unvalidated |

The connector failed closed and returned no search content. The error was normalized to `internal_error`; it did not expose an `invalid_cursor` code, raw Slack response, or evidence binding the failure uniquely to the supplied cursor.

## Official contract baseline

Primary Slack documentation reviewed:

- `search.messages` accepts a cursor for cursormark pagination, is a legacy method, and documents `internal_error` as a possible error. The method page does not list `invalid_cursor` in its method-specific expected-error table: https://docs.slack.dev/reference/methods/search.messages/
- Slack's general cursor-pagination documentation says clients should reuse a returned `next_cursor`, cursors can expire, and gibberish, incorrectly encoded, or stale cursor values can yield `invalid_cursor`. The same page classifies `search.messages` under traditional paging, so direct applicability to the connector's search implementation is not proven: https://docs.slack.dev/apis/web-api/pagination/

## Failure, permission, portability, and connector-variance findings

- **Failure behavior:** fail-closed with zero content, but low diagnostic precision because only a generic connector-level `internal_error` was exposed.
- **Permission behavior:** not probed; the call stayed inside an already accessible public channel and cannot establish identity, token type, effective scope, or ACL-denial normalization.
- **Portability:** low. Query syntax, cursor semantics, and the rendered/error envelope are Slack- and connector-specific.
- **Connector variance:** official documentation allows more specific pagination errors in some Slack surfaces, while this connector exposed only generic `internal_error`. Whether Slack itself returned that code or the wrapper normalized another failure is unknown.
- **Durability:** the connector result was transient; this immutable Git event is the durable receipt.
- **Observability:** partial. Error state and generic text were visible; provider status, request identity, raw body, headers, upstream attempt count, and quota use were not.

## Gates added

1. Fail closed on any connector error and never interpret absence of returned matches as Slack absence.
2. Do not automatically retry `internal_error`; first distinguish transient provider failure from deterministic invalid input using changed evidence or a raw-provider witness.
3. Use only continuation cursors returned by the immediately preceding compatible request; do not invent, persist long-term, or cross-query reuse cursors.
4. Do not branch operational logic on connector error text alone; require typed errors or an independent provider witness.
5. Keep private channels and DMs outside the approved boundary.
6. Require named consumer acknowledgment and measured outcome before operational or fitness credit.

## Strongest falsifier

A same-principal raw Slack request using the identical bounded query and deliberately invalid cursor returns a specific `invalid_cursor` or other provider error while the connector continues to return generic `internal_error`; that would prove material wrapper normalization and weaken portability and diagnostic value.

## Verifier and consumer

- Verifier: official Slack primary documentation plus this direct connector receipt.
- Distinct raw-provider witness: not completed.
- Catalog consumer: HFO COTS capability inventory.
- Operational consumer: not named.
- Consumer acknowledgment: not observed.

## Honest flaw

One synthetic invalid-cursor call cannot prove that the cursor caused the error. The response could reflect transient Slack failure, connector failure, method mismatch, argument translation, or wrapper normalization. Permission denial, real cursor continuation, stale-but-once-valid cursor behavior, rate limiting, hidden retries, raw parity, consumer value, and time savings remain unverified.

## Phase disposition

`PHASE3_ACCEPTED_WITH_GATES`; adoption and fitness credit remain zero. Phase 4 is decision-only and must make no additional Slack candidate call.

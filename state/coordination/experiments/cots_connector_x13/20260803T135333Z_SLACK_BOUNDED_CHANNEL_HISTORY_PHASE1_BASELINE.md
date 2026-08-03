---
schema_id: hfo.gen133.x13.cots_connector_event.v1
experiment_id: X13_SLACK_BOUNDED_CHANNEL_HISTORY_READONLY_001
event_type: PHASE1_OFFICIAL_CONTRACT_AND_DIRECT_BASELINE
candidate: Slack_bounded_readonly_channel_history_surface
phase: 1_of_4
disposition: PHASE1_ACCEPTED_WITH_PRIVACY_SCOPE_RATE_LIMIT_AND_PAGINATION_GATES
carrier_task_id: 6a55c1733708819185088bf334e33ea5
carrier_task_id_match: true
wip: 1
expected_current_version: 64
next_current_version: 65
valid_time_utc: 2026-08-03T13:53:33Z
transaction_time_utc: SEE_GIT_COMMIT_METADATA
mutation_effect: false
paid_cost_usd_observed: 0_NO_CHARGE_SURFACED
operator_minutes_removed_measured: 0
fitness_credit: 0_PENDING_SOURCE_BOUND_CONSUMER_ACK_AND_MEASURED_OPERATOR_OUTCOME
---

# X13 Slack bounded channel history — phase 1 baseline

## Candidate and official contract

Candidate primitive: one-page, bounded, read-only retrieval of the newest messages from a known Slack conversation ID through the native connector.

Official Slack `conversations.history` contract checked on 2026-08-03:

- https://docs.slack.dev/reference/methods/conversations.history/
- required input is a conversation ID plus an authenticated token carrying the history scope appropriate to the conversation class
- relevant scopes are `channels:history`, `groups:history`, `im:history`, or `mpim:history`
- the method returns a portion of message events newest first and supports `limit`, `oldest`, `latest`, and cursor pagination
- a returned `response_metadata.next_cursor` is the source for the next page
- fewer items than the requested limit may be returned even when more history exists
- affected non-Marketplace commercially distributed apps are documented at one request per minute with a maximum/default page size of 15; Tier 3 applies to other app classes, but the connector app class is not exposed
- callers must inspect explicit API success/error state; documented failures include `channel_not_found`, `access_denied`, account inactivity, and service-side errors

## Direct connector baseline

One harmless read-only call was executed:

- connector action: `Slack.slack_read_channel`
- conversation: known HFO command-and-control channel ID; exact channel ID retained only as existing canonical infrastructure, not copied into this event body
- requested limit: 1
- requested response format: `concise`
- returned message count: 1
- ordering observed: newest first
- continuation cursor present: yes
- normalized connector error: none
- carrier retries: 0
- send, edit, delete, reaction, join, channel creation, draft, schedule, file read, or other mutation: none
- surfaced paid cost: USD 0
- visible connector latency: not exposed

Private content was returned by default even in `concise` mode. The response included the full message body plus identifying author fields and timestamp information. Exact message text, email address, user ID, message timestamp, channel cursor, and permalink values were deliberately excluded from this Git event and from the planned Slack projection.

## Measured facts and Andons

### Privacy Andon

`response_format=concise` did not produce metadata-only output. It returned the full newest message body and identifying author data.

Admitted interpretation: the connector can retrieve one current message and a continuation cursor from a known accessible conversation.

Forbidden interpretation: `concise` is privacy-minimal, metadata-only, least privilege, or safe for automatic durable fan-out without local minimization.

### Pagination fact

The wrapper exposed a continuation cursor for a one-item page. This is stronger pagination observability than the preceding Drive connector campaign, but valid source-bound traversal has not yet been tested.

### Scope and identity Andon

The connector reached a success path, but it did not expose whether it used a user token, bot token, app token, exact scopes, workspace identity, membership model, or token custody. Successful access proves only connector-visible reach to this known conversation at observation time.

### Rate-limit Andon

Slack's official contract varies materially by app distribution class. The connector did not expose its app class, remaining quota, request headers, retry-after state, or upstream request count. No direct rate-limit or billing evidence was surfaced.

## Measurement

- custom code avoided estimate: 30–95 LOC for authenticated bounded conversation-history retrieval, cursor extraction, and normalized response handling; unvalidated
- operator minutes removed measured: 0
- operator minutes removed estimate per consumed channel-status check: 1–3; unvalidated
- credentials: connector-managed authentication reached a success path; authenticated principal, token class, exact scopes, workspace identity, membership basis, storage, and custody remain unknown
- durability: ephemeral point-in-time read; not a durable event stream, snapshot, checkpoint, delivery receipt, or exactly-once feed
- observability: requested limit, response mode, returned message count, newest-first ordering, full-content field classes, author-identifying field classes, cursor presence, and normalized success were visible; raw request, HTTP status, Slack `ok`, response headers, request ID, rate-limit counters, retry-after, app class, scopes, upstream retries, and latency were hidden
- portability: medium for generic channel-history reads; low-to-medium for Slack conversation classes, timestamp boundaries, message subtypes, cursor semantics, identity, and scope rules
- failure behavior: positive bounded page observed; valid cursor traversal, empty valid window, malformed cursor, invalid channel, permission denial, rate limit, transient provider failure, message subtype variance, and free-history truncation remain untested
- direct cost/quota evidence: no charge surfaced; actual app distribution class, request count, quota tier, consumed allowance, and billing relationship remain unknown
- strongest falsifier: equivalent raw `conversations.history` under the same identity returns different message ordering/count, no cursor, a permission failure, or materially different content; or the connector silently rewrites the channel, limit, or response mode
- verifier: raw Slack `conversations.history` with the same known conversation ID and `limit=1`, inspecting `ok`, `messages`, `has_more`, `response_metadata.next_cursor`, headers, scopes, and app class, plus Slack UI comparison at the same observation boundary
- consumers: HFO coordination-state reader; morning gathering fan-in; bounded Andon and pheromone verifier; source-bound Slack receipt locator
- honest flaw: this phase proved only one positive full-content read from one accessible conversation. It did not verify metadata minimization, exact identity or scopes, cursor traversal, empty behavior, permission failure, rate limits, raw API parity, ConsumerAck, or measured operator-time reduction

## Initial gates

1. Use only a known, explicitly selected conversation ID and a small limit.
2. Treat `concise` as a presentation mode, not a privacy or metadata-only guarantee.
3. Minimize message text, emails, user IDs, timestamps, cursor values, links, files, reactions, and attachments before Git, Slack, or downstream fan-out unless the consumer explicitly requires them.
4. Persist counts, field classes, normalized error class, cursor presence, observation time, and source-bound hashes rather than raw private content.
5. Accept pagination cursors only from the immediately preceding compatible query and keep exact cursor values out of routine logs.
6. Keep positive page, valid empty page, invalid channel/cursor, permission denial, rate limit, transport failure, and provider failure as distinct states.
7. Do not claim completeness, full history, oldest-message reach, free-plan archive reach, thread completeness, identity, scope, or quota status from one page.
8. Require source-bound ConsumerAck and a measured operator outcome before fitness credit.

## Phase result

`PHASE1_ACCEPTED_WITH_PRIVACY_SCOPE_RATE_LIMIT_AND_PAGINATION_GATES`

The native connector avoids inventing a Slack client for the narrow bounded-history primitive, but automatic durable use is gated by aggressive privacy minimization and explicit uncertainty around identity, scopes, pagination, completeness, and rate limits.

## Next phase

Phase 2 should perform one smallest harmless micro-use against the same known conversation: a one-message read bounded by a non-secret time window or a source-bound `latest` timestamp, with exact content minimized and no cursor traversal, send, edit, delete, join, reaction, file read, or other mutation.

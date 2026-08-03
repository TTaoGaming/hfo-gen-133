---
schema_id: hfo.gen133.x13.cots_connector_event.v1
experiment_id: X13_GMAIL_BOUNDED_READONLY_METADATA_001
event_id: X13_GMAIL_BOUNDED_READONLY_METADATA_001_PHASE1_20260803T214803Z
carrier_task_id: 6a55c1733708819185088bf334e33ea5
carrier_task_id_match: true
wip: 1
candidate: Gmail_search_email_ids_bounded_readonly_surface
phase: 1_of_4
phase_status: PHASE1_ACCEPTED_WITH_GATES
prior_current_version: 72
expected_next_current_version: 73
valid_time_utc: 2026-08-03T21:48:03Z
recorded_time_utc: 2026-08-03T21:48:03Z
effect_class: READ_ONLY
mutation_count: 0
send_count: 0
draft_count: 0
label_change_count: 0
archive_trash_delete_count: 0
carrier_retry_count: 0
fallback_count: 0
paid_cost_usd_observed: 0_NO_CHARGE_SURFACED
operator_minutes_removed_measured: 0
consumer_ack: NOT_OBSERVED
adoption_credit: 0
fitness_credit: 0
---

# X13 Gmail bounded read-only metadata/search — phase 1 baseline

## Official contract baseline

Google's `users.messages.list` contract lists mailbox messages and supports `maxResults`, `pageToken`, Gmail search syntax through `q`, label filtering, and optional inclusion of spam/trash. A successful raw response contains message objects limited to `id` and `threadId`, plus an optional `nextPageToken` and a `resultSizeEstimate`; complete message details require a separate `messages.get` call.

Primary documentation:

- https://developers.google.com/workspace/gmail/api/reference/rest/v1/users.messages/list
- https://developers.google.com/workspace/gmail/api/guides/list-messages
- https://developers.google.com/workspace/gmail/api/auth/scopes
- https://developers.google.com/workspace/gmail/api/reference/quota

The official contract also states that `q` cannot be used with the `gmail.metadata` scope. Therefore, a successful query-bearing wrapper call does not establish metadata-only authorization or least privilege. It implies either a broader permitted Gmail scope, a connector-managed alternative implementation, or undocumented normalization; the actual principal and scopes remain unknown.

Under Google's quota page updated 2026-06-03, `messages.list` is assigned 5 quota units per raw request. The connector did not expose its Cloud project class, actual upstream method count, quota counters, billing project, or whether the post-May-1-2026 quota model applies to its project.

## Direct connector receipt

One smallest bounded read-only call was made through `Gmail.search_email_ids`:

- Query class: `newer_than:30d -in:spam -in:trash`
- Maximum results: `1`
- Returned opaque message IDs: `1`
- Returned next-page token: present
- Message headers, subject, sender, recipients, snippet, body, attachments, labels, and thread content returned: none
- Connector-visible error: none
- Connector-reported external-call time: `345 ms`
- Connector retries or fallback observed by carrier: `0`
- Gmail mutations: `0`
- Surfaced paid cost: `$0`
- Measured operator relief: `0 minutes`

The returned message ID and page token were deliberately omitted from Git and Slack because they are unnecessary mailbox identifiers and continuation capabilities.

## Measurements

| Dimension | Result |
|---|---|
| Custom code avoided | `20–65 LOC`, unvalidated estimate for authenticated list/search, result clamping, pagination-token handling, and normalized error envelope |
| Operator minutes | `0` measured; no consumer used the result |
| Credentials | Connector-managed and uninspected; authenticated principal, OAuth scope, token class, custody, and least privilege unknown |
| Durability | Gmail observation was ephemeral; this minimized Git event is durable |
| Observability | Wrapper exposed action name, connector name, structured error fields, result count, page-token presence, and `external_call_time_ms`; raw HTTP status, request ID, response headers, upstream attempts, result-size estimate, and quota counters were hidden |
| Portability | Medium-low; Gmail query syntax, message IDs, page tokens, and labels are provider-specific, though bounded list/search semantics are portable |
| Failure behavior | Not probed in phase 1 |
| Direct cost/quota evidence | `$0` surfaced; official raw `messages.list` cost is 5 quota units, but connector mapping and actual consumption are unknown |
| Consumer | Immediate: `HFO_COTS_CAPABILITY_INVENTORY`; operational consumer not named |
| Verifier | A distinct authorized raw `users.messages.list` call with identical `q` and `maxResults=1`, capturing scope, HTTP status, headers, request ID, page token, result-size estimate, quota and zero-retry telemetry |
| Strongest falsifier | Same-identity raw Gmail returns a different bounded result or rejects the query, or inspection shows the wrapper fetched/stored message content beyond IDs, rewrote the query materially, used hidden retries, or consumed a different method/quota class |

## Mandatory gates

1. Prefer `search_email_ids` over full-message search when IDs are sufficient.
2. Use explicit bounded `max_results`; never rely on the raw API default of 100.
3. Do not durably log message IDs, thread IDs, page tokens, headers, snippets, bodies, attachments, or personal metadata unless a named consumer requires them.
4. Treat page tokens as short-lived continuation capabilities tied to the exact preceding query; do not reuse across query or identity changes.
5. Do not infer `gmail.metadata`, least privilege, or read-only token scope from an IDs-only response; query-bearing calls are officially incompatible with `gmail.metadata`.
6. Do not claim complete mailbox coverage, exact query forwarding, authoritative absence, result ordering, or result-count accuracy from one page.
7. Distinguish valid empty, invalid query, invalid page token, permission denial, authentication failure, quota/rate limit, timeout, and provider failure before retrying.
8. No automatic retry without bounded policy and provider telemetry.
9. Require a named consumer acknowledgment and measured operator outcome before operational adoption or fitness credit.

## Phase disposition

`PHASE1_ACCEPTED_WITH_GATES`

The native Gmail connector avoided a custom authenticated list/search implementation for one bounded IDs-only observation and exposed useful wrapper telemetry. It is not yet operationally adopted because authorization scope, exact query forwarding, pagination, failure semantics, quota mapping, consumer value, and independent parity are unverified.

## Honest flaw

Only one positive IDs-only page from one broad recent-mail query was observed. The connector may have broader-than-metadata mailbox access, and the successful response does not prove exact query forwarding, result ordering, completeness, page-token validity, raw API parity, quota consumption, hidden retry behavior, or absence of server-side content hydration.
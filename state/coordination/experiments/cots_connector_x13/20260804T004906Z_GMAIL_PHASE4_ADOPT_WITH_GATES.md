---
schema_id: hfo.gen133.x13.cots_connector_event.v1
event_id: X13_GMAIL_BOUNDED_READONLY_METADATA_001_PHASE4_DECISION_20260804T004906Z
experiment_id: X13_GMAIL_BOUNDED_READONLY_METADATA_001
carrier_task_id: 6a55c1733708819185088bf334e33ea5
carrier_task_id_match: true
wip: 1
candidate: Gmail_search_email_ids_bounded_readonly_surface
phase: 4_of_4
event_type: DECISION
decision: ADOPT_WITH_GATES
adoption_mode: CATALOG_ONLY_NONOPERATIONAL
valid_time_utc: 2026-08-04T00:49:06Z
recorded_time_utc: 2026-08-04T00:49:06Z
prior_current_version: 75
next_current_version: 76
candidate_capability_calls_this_wake: 0
retries_this_wake: 0
fallbacks_this_wake: 0
mutations_on_candidate_surface_this_wake: 0
paid_cost_usd_observed_this_wake: 0_NO_CHARGE_SURFACED
operator_minutes_removed_measured: 0
consumer_ack: NOT_OBSERVED
adoption_credit: 0
fitness_credit: 0
---

# X13 Gmail bounded read-only campaign — Phase 4 decision

## Decision

`ADOPT_WITH_GATES`

Retain `Gmail.search_email_ids` in the HFO COTS capability catalog only for bounded, explicit, IDs-only mailbox discovery where opaque identifiers are sufficient. Do not promote it to autonomous, binding, or content-bearing workflow use.

No additional Gmail candidate-capability call was made in phase 4. The decision is based only on the three sealed campaign observations already recorded under this experiment.

## Measured campaign record

| Measure | Observed |
|---|---:|
| Positive IDs-only pages | 1 |
| Synthetic exact-query valid-empty responses | 1 |
| Synthetic invalid-page-token probes | 1 structured `invalidArgument` |
| Completed connector responses | 3 |
| Opaque message IDs returned | 1, not durably logged |
| Continuation tokens returned | 1, not durably logged |
| Message or thread content returned | 0 |
| Candidate retries | 0 |
| Candidate fallbacks | 0 |
| Candidate mutations | 0 |
| Raw HTTP status, headers, request IDs, field location, scope, and quota exposed | 0 |
| Surfaced paid cost | $0 |
| Measured operator minutes removed | 0 |
| Consumer acknowledgment | Not observed |

Estimated custom code avoided remains unvalidated: approximately 20–65 LOC for authenticated bounded message-ID listing, pagination plumbing, and normalized client-error handling. Privacy minimization, identity and scope verification, exact query parity, token binding, quota telemetry, retry policy, failure disambiguation, and consumer workflow are not avoided.

## Adopted boundary

Admit only:

1. One `max_results=1` query returned one opaque message ID and a continuation token without message content.
2. One synthetic exact Message-ID query returned a connector-visible valid-empty result without content.
3. One synthetic invalid page token returned structured `invalidArgument` without mailbox identifiers or content.
4. The connector can reduce content exposure compared with full-message hydration when IDs alone are sufficient.
5. Success and failure telemetry are insufficient for least-privilege, quota, retry, or raw-provider parity claims.

Do not admit:

- empty results as authoritative mailbox absence;
- exact query forwarding, ordering, completeness, or valid pagination behavior;
- `invalidArgument` as page-token-specific or provider-origin proof;
- metadata-only authorization, least privilege, authenticated identity, token class, or custody;
- actual Gmail quota consumption, hidden-retry absence, or retry safety;
- operational readiness, consumer value, or measured time savings.

## Mandatory gates

- Prefer IDs-only search over message hydration when opaque identifiers are sufficient.
- Require an explicit small `max_results`; default to one for probes.
- Prefer synthetic exact probes over real mailbox identifiers for validation.
- Do not durably log message IDs, thread IDs, page tokens, or message content without a named consumer and retention need.
- Bind a continuation token only to the immediately preceding identical query, labels, identity, and limit; never reuse across changed parameters.
- Treat valid-empty as a connector-visible scoped observation, not authoritative absence.
- Treat `invalidArgument` as a generic client-argument failure unless field-level provider telemetry identifies the rejected field.
- Never automatically retry `invalidArgument`; do not automatically retry other failures without an explicit bounded policy and provider telemetry.
- Distinguish authentication, permission, invalid query, invalid token, quota, rate-limit, timeout, transport, and provider failures.
- Require distinct authorized raw-provider verification before claiming exact failure parity, scope, quota use, or retry safety.
- Require a named consumer acknowledgment and measured operator outcome before operational adoption or fitness credit.

## Dimensions

- **Credentials:** connector-managed and uninspected; authenticated principal, OAuth scope, token class, custody, and least privilege remain unknown. A query-bearing success does not prove metadata-only scope.
- **Durability:** Git-first campaign receipts are durable; mailbox identifiers and continuation tokens were deliberately excluded from durable logs.
- **Observability:** adequate for bounded inputs, IDs-only result count, token presence, and normalized `invalidArgument`; weak for raw HTTP, request identity, exact field rejection, upstream attempts, scope, and quota.
- **Portability:** medium for the abstract IDs-only discovery pattern; low-to-medium across mail providers because query syntax, pagination, scopes, errors, and quotas are provider-specific.
- **Failure behavior:** one invalid-token probe produced a structured client-error class without content; wrapper-local validation and Gmail-provider rejection remain indistinguishable.
- **Direct cost/quota evidence:** no charge surfaced. Official-method mapping, upstream request count, failed-request charging, consumed units, and billing counters were not exposed.

## Strongest falsifier

A distinct authorized raw Gmail `users.messages.list` call under the same identity and query parameters returns materially different result cardinality or ordering, accepts the invalid token, rejects a different field, exposes broader content access than expected, or shows that the connector substituted a method, retried invisibly, or consumed a different quota class.

## Verifier

Use a distinct authorized raw `users.messages.list` check with the same `q`, `maxResults=1`, and synthetic invalid token. Capture authenticated principal and scope, HTTP status, headers, request ID, field-level error details, result cardinality, next-page token behavior, quota telemetry, content-access behavior, and zero-retry evidence. Do not persist returned mailbox identifiers beyond the verification need.

## Consumer

- Immediate: `HFO_COTS_CAPABILITY_INVENTORY`
- Future operational consumer: must be explicitly named in a new work item.

## Honest flaw

The campaign observed only one positive IDs-only page, one synthetic valid-empty response, and one structured `invalidArgument` probe. Identity, scope, exact query and token forwarding, ordering, completeness, valid pagination, raw API parity, field location, quota consumption, hidden retries, permission failure behavior, consumer acknowledgment, and actual operator-time reduction remain unverified.

## Next campaign candidate

`Google Calendar bounded read-only free/busy surface`, phase 1 only, provided the already-authorized native connector can perform a smallest harmless availability query without event creation, update, invitation, response, notification, or calendar mutation.
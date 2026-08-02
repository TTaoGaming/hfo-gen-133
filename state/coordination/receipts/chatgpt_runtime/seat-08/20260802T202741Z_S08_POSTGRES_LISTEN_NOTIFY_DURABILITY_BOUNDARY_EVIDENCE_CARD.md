---
schema_id: hfo.gen133.s08.evidence_card.v1
seat: S08_RESEARCH_AND_CANDIDATE_SCOUT
carrier_task_id_expected: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_observed: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_match: true
wip: 1
lane: agent_runtime_cots_capabilities
valid_time_utc: 2026-08-02T20:27:41Z
transaction_time_utc: SEE_GIT_COMMIT_METADATA
queue_source:
  repository: TTaoGaming/hfo-gen-133
  branch: agent/gen133-bootstrap-20260730
  issue: 5
  issue_created_utc: 2026-08-02T18:51:49Z
  issue_updated_utc: 2026-08-02T18:51:49Z
  issue_url: https://github.com/TTaoGaming/hfo-gen-133/issues/5
research_question: Can PostgreSQL LISTEN/NOTIFY be treated as the durable WorkItem delivery and coordination mechanism for the proposed Gen-133 PostgreSQL consolidation?
candidate:
  product: PostgreSQL
  version: 18.4_CURRENT_SUPPORTED_MAJOR_AT_RESEARCH_TIME
  capability: LISTEN_NOTIFΥ_ASYNCHRONOUS_NOTIFICATION
  exact_docs:
    notify: https://www.postgresql.org/docs/current/sql-notify.html
    listen: https://www.postgresql.org/docs/18/sql-listen.html
    async_notification: https://www.postgresql.org/docs/18/libpq-notify.html
    license: https://www.postgresql.org/about/licence/
decision: REVISE
classification: POSTGRES_LISTEN_NOTIFY_IS_WAKE_HINT_NOT_DURABLE_WORK_DELIVERY
---

# Evidence card — PostgreSQL LISTEN/NOTIFY durability boundary

## Decision

`REVISE` the PostgreSQL consolidation design in issue #5: use `LISTEN/NOTIFY` only as a low-latency wake hint. Durable WorkItem state, acknowledgements, retries, replay cursors, idempotency keys, leases/fencing, and terminal receipts must remain in transactionally committed tables or another durable runtime. Every listener start or reconnect must perform a table scan/replay before relying on later notifications.

## Primary evidence checked on 2026-08-02

1. PostgreSQL 18 `LISTEN` registers only the current session; registrations are automatically cleared when the session ends. It also documents a startup race and prescribes: commit `LISTEN`, inspect database state in a new transaction, then rely on notifications for later changes.
2. PostgreSQL 18 `NOTIFY` delivers to sessions currently listening in the same database. It recommends using tables for structured data and treating a notification as a signal that a table changed.
3. `NOTIFY` is transaction-coupled: delivery occurs only after the sender commits, and a receiver inside a transaction does not receive the event until that transaction ends.
4. Identical channel-plus-payload notifications in one transaction can be folded into one event. This excludes event-count equivalence and exactly-once delivery semantics.
5. The server notification queue is finite; if it fills, transactions issuing `NOTIFY` can fail at commit. Long-running listening transactions can prevent cleanup.
6. PostgreSQL 18.4 is licensed under the permissive PostgreSQL License. This does not resolve hosting-provider pricing, retention, backup, HA, or operational terms.

## Supported claims

- `LISTEN/NOTIFY` is suitable for low-latency same-database change signaling.
- A committed table row plus a key-only notification can reduce polling latency.
- Sender transaction commit prevents notifications for rolled-back writes.
- A reconnecting consumer can recover safely only if durable state is independently queryable and replayable.

## Excluded claims

- Durable delivery to clients that were disconnected or not yet listening.
- Exactly-once, at-least-once, or unique-event-count semantics from notifications alone.
- Persistent consumer offsets, acknowledgements, retries, leases, fencing tokens, dead-letter handling, or terminal receipts.
- Cross-database, cross-cluster, or provider-independent delivery.
- Notification payloads as the authoritative record of a WorkItem or receipt.
- PostgreSQL availability, backup, restore, failover, WSL persistence, or managed-provider guarantees for the current HFO deployment.

## Required gate for issue #5

The minimum source-to-table manifest should include one durable outbox/work table with immutable identity and replay fields, at minimum:

- `work_id` or source-bound idempotency key with a unique constraint;
- source repository/path/blob or external source cursor;
- state/version and prior digest;
- created, valid, transaction, lease, and expiry times;
- claimant/fencing token when mutation is permitted;
- retry/attempt and terminal status;
- verifier and consumer acknowledgement bindings.

`NOTIFY` may carry only a channel and opaque row key. On process start, reconnect, timeout, or notification error, the consumer must query durable rows from its last committed cursor. Notification receipt must never advance the durable cursor by itself.

## License and terms uncertainty

- Core PostgreSQL: PostgreSQL License, permissive, no software license fee stated by the project.
- Unknown for the actual HFO runtime: host/provider terms, storage and egress cost, backup retention, HA/failover behavior, idle shutdown, support, quotas, and whether the deployed version is exactly 18.4.
- No trademark or hosted-service branding use is proposed by this card.

## Cost and operator-minute estimate

- Research call cost surfaced: `$0`; exact platform inference cost not exposed.
- If the implementation already has a durable table and startup replay, correction cost is approximately `10–25 developer minutes` for explicit invariants and tests.
- If it currently treats notifications as the queue, expect `45–120 developer minutes` for a minimal table-backed outbox, reconnect scan, idempotency constraint, and one disconnect/recovery test.
- Operator burden: `0 minutes` until a concrete implementation packet exists; estimated later review `5–10 minutes`.

## Strongest objection

A single always-on local worker can appear reliable with raw `LISTEN/NOTIFY`, and polling a tiny table may seem unnecessary. That objection fails under the stated Gen-133 recovery requirement: session loss clears the listener registration, startup has a documented race, and notifications do not supply durable replay state.

## Falsifier

This card falls if either:

1. current official PostgreSQL documentation guarantees replay after listener downtime without querying durable database state; or
2. a source-bound implementation and controlled test prove that WorkItems committed while the listener is disconnected are all recovered after reconnect, with no startup/replay query and no separate durable queue mechanism.

## Verifier

`X13_COTS_AND_CONNECTOR_PDCA_LAB` or a distinct runtime verifier should run one bounded local test:

1. commit a durable work row and notification while listener A is connected;
2. disconnect listener A;
3. commit two more durable rows and notifications;
4. reconnect listener A;
5. prove the missed rows are recovered only by the required table scan/replay and that duplicate notifications do not duplicate terminal processing.

The verifier must bind PostgreSQL server version, schema, SQL, client library/version, commands, exit codes, and exact row results.

## Consumer

- Primary: `TTaoGaming/hfo-gen-133#5`, section `Next safe action` — minimum source-to-table manifest, idempotency/fencing rules, replay verifier, recovery gates, and rollback plan.
- Fitness credit: `0_PENDING_EXPLICIT_WORKITEM_CONSUMPTION_AND_CONSUMER_ACK`.

## Expiry

`2026-08-09T20:27:41Z`, or immediately upon a PostgreSQL major-version change, replacement of issue #5, or source-bound proof that the proposed implementation already treats notifications only as hints.

## Honest flaw

This was a documentation-bound pass. No live PostgreSQL instance, disconnect test, schema, code path, hosted-provider configuration, or current HFO deployment version was inspected. The card establishes a contract boundary, not implementation compliance.

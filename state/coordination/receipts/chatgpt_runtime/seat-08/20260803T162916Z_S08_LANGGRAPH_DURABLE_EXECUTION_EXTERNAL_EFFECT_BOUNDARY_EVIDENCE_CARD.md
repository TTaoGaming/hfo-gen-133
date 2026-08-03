---
schema_id: hfo.gen133.s08.evidence_card.v1
seat: S08_RESEARCH_AND_CANDIDATE_SCOUT
carrier_task_id_expected: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_observed: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_match: true
wip: 1
lane: agent-runtime/COTS_capabilities
question_id: GEN133_LANGGRAPH_POSTGRES_DURABILITY_EFFECT_BOUNDARY_001
valid_time_utc: 2026-08-03T16:29:16Z
transaction_time_utc: SEE_GIT_COMMIT_METADATA
canonical_repository: TTaoGaming/hfo-gen-133
canonical_branch: agent/gen133-bootstrap-20260730
repository_head_observed_before_write: 9f7a3be3eeb44cf8ebe32ec157ac1ccae2ae2daf
candidate_repository: langchain-ai/langgraph
candidate_version: langgraph==1.2.9
companion_version: langgraph-checkpoint-postgres==3.1.0
candidate_license: MIT
decision: REVISE
consumer: GEN133_POSTGRES_AGENT_RUNTIME_BOUNDARY_GATE_001
consumer_issue: https://github.com/TTaoGaming/hfo-gen-133/issues/2
verifier: S09_ADVISORY_THEN_DISTINCT_HOST_CRASH_REPLAY_VERIFIER
expiry_utc: 2026-08-10T16:29:16Z
fitness: 0_PENDING_WORKITEM_CONSUMPTION_AND_CONSUMER_ACK
sealed: false
---

# S08 evidence card — LangGraph durability is not exactly-once effect execution

## Bounded uncertainty

Can `langchain-ai/langgraph` at `1.2.9`, with `langgraph-checkpoint-postgres` at `3.1.0`, be admitted as the Gen-133 PostgreSQL-backed durable agent runtime **and** as proof of exactly-once external effects?

## Decision

`REVISE`

Admit only the narrower claim: LangGraph is a plausible checkpointed agent/workflow-state runtime that can resume from persisted state and avoid recomputing already checkpointed successful work. Do **not** admit it as an exactly-once external-effect engine, authority plane, queue/lease service, ConsumerAck mechanism, or replacement for Git receipts without a direct crash/replay specimen.

## Current primary evidence checked on 2026-08-03

1. LangGraph overview — runtime scope and durable execution:
   https://docs.langchain.com/oss/python/langgraph/overview
2. Persistence — checkpoints, super-step boundaries, pending writes and restart from last successful step:
   https://docs.langchain.com/oss/python/langgraph/persistence
3. Functional API — task checkpointing, determinism and explicit idempotency warning for re-executed tasks:
   https://docs.langchain.com/oss/python/langgraph/functional-api
4. Checkpointer integrations — PostgreSQL package is the official persistent backend:
   https://docs.langchain.com/oss/python/integrations/checkpointers
5. Production memory/checkpointer example — `PostgresSaver`, setup requirement and database-backed production guidance:
   https://docs.langchain.com/oss/python/langgraph/add-memory
6. PyPI release pin — `langgraph 1.2.9`, uploaded 2026-07-10, Python >=3.10, MIT expression:
   https://pypi.org/project/langgraph/1.2.9/
7. PyPI companion pin — `langgraph-checkpoint-postgres 3.1.0`, uploaded 2026-05-12, Python >=3.10, MIT expression:
   https://pypi.org/project/langgraph-checkpoint-postgres/3.1.0/
8. Repository license — MIT, copyright LangChain, Inc.:
   https://github.com/langchain-ai/langgraph/blob/main/LICENSE

## Supported claims

- LangGraph is an orchestration runtime for long-running, stateful agents and workflows.
- With a checkpointer, graph state is persisted as checkpoints organized by thread.
- PostgreSQL is an officially documented production checkpointer backend through `langgraph-checkpoint-postgres`.
- Checkpoint and pending-write behavior can prevent successful nodes in a failed super-step from being recomputed on resume.
- Task results can be persisted so a resumed run can reuse completed task results.
- The pinned open-source packages are available under MIT terms and require Python 3.10 or newer.

## Excluded claims

- Exactly-once execution of arbitrary external API calls, emails, deployments, payments, Git writes, Slack posts, or other nontransactional effects.
- Automatic idempotency for a task that starts an external effect and crashes before its result is checkpointed.
- Atomic commit across a LangGraph checkpoint and an unrelated provider or Git/Slack side effect.
- Built-in WorkItem leasing, fencing, stale-writer rejection, authority policy, privacy policy, independent verification, or ConsumerAck.
- Durability under Gen-133 process death, PostgreSQL restart, schema migration, version skew, concurrent workers, or poisoned state; none was executed in this pass.
- Superiority to the already-assessed DBOS path. This card establishes a boundary, not a runtime selection verdict.

## Why the exactly-once claim fails

The official Functional API documentation says tasks may re-execute when a task starts but does not complete successfully, and explicitly requires idempotency keys or checking for existing results to avoid duplicate API calls. Interrupt documentation likewise warns that nodes can re-run and side effects must be idempotent. Checkpointing therefore narrows replay but does not erase the crash window around an external effect whose completion was not durably recorded.

## License and terms uncertainty

- Open-source package license: MIT; preserve the license notice in redistributed copies or substantial portions.
- No account, terms acceptance, or paid service is required for the inspected OSS packages.
- LangSmith, Agent Server, managed deployment, telemetry retention, quotas, pricing and service terms were not evaluated and remain `UNKNOWN`.
- Transitive dependency and deployment-image license inventory was not performed.

## Cost and operator-minute estimate

- This research pass: `$0` external spend; `0` operator minutes.
- Smallest valid local specimen: approximately `45–90` producer minutes plus `30–45` distinct verifier minutes, assuming an existing disposable PostgreSQL instance and Python environment.
- Additional infrastructure cost: potentially `$0` on existing local Postgres; production compute, backups and operations remain unmeasured.

## Strongest objection

Gen-133 already has a DBOS COTS assessment aimed at transactional hot workflow state. Adding LangGraph as another durable runtime may duplicate checkpointing, increase framework coupling and create a second state authority while leaving the actual bottleneck—provider-effect idempotency and independent outcome sensing—unchanged.

## Falsifier

Retire the candidate for the named consumer if a pinned `1.2.9` plus PostgresSaver specimen cannot pass all of the following:

1. deterministic caller-supplied `thread_id`/WorkItem identity;
2. process kill after one state transition and successful resume from Postgres;
3. no duplicate accepted transition after replay;
4. an intentionally non-idempotent external-effect stub duplicates under the expected crash window, proving the claim ceiling;
5. the same stub with a durable idempotency key suppresses the duplicate;
6. PostgreSQL stop/start preserves inspectable state;
7. one immutable Git receipt can be projected without making Git or Slack the hot-state transaction boundary.

A failure of 1, 2, 3, 5 or 6 rejects the candidate for this WorkItem. A failure of 4 means the assay did not expose the documented replay hazard and must be revised.

## Proposed consumer gate

`GEN133_POSTGRES_AGENT_RUNTIME_BOUNDARY_GATE_001`

Use LangGraph only for one bounded internal agent-state specimen. Keep external effects behind provider-native idempotency or a separate transactional outbox, retain Git as provenance authority, and compare measured complexity against the existing DBOS candidate before any architecture choice.

## Honest flaw

This is documentation and package-metadata evidence only. No package was installed, no PostgresSaver schema was created, no process was killed, no concurrent executor ran, and no effect was invoked. The exact compatibility pair was not lock-resolved in a live environment. The card can constrain claims but cannot select the runtime without the named specimen and distinct verification.

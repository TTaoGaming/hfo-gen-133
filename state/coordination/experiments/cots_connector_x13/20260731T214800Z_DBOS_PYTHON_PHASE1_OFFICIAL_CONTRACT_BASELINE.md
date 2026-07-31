---
schema_id: hfo.gen133.x13.cots_connector_event.v1
experiment_id: X13_DBOS_PYTHON_DURABLE_KERNEL_001
seat: X13_COTS_CONNECTOR_PDCA
carrier_task_id_expected: 6a55c1733708819185088bf334e33ea5
carrier_task_id_observed: 6a55c1733708819185088bf334e33ea5
carrier_task_id_match: true
phase: 1_of_4
phase_name: OFFICIAL_CONTRACT_AND_DIRECT_CAPABILITY_BASELINE
candidate: DBOS_Python
candidate_pin: 2.22.0
candidate_license: MIT
valid_time_utc: 2026-07-31T21:48:00Z
transaction_time_utc: SEE_GIT_COMMIT_METADATA
canonical_repository: TTaoGaming/hfo-gen-133
canonical_branch: agent/gen133-bootstrap-20260730
repository_head_observed_before_write: 7a87a31fbf6c391fd972a5cbc120943a1510b516
result: CONTINUE_TO_PHASE_2
binding_decision: false
wip: 1
effect_ceiling: FILE_AND_SANITIZED_SLACK_ONLY
verifier: S04_STRUCTURAL_PREFLIGHT_THEN_SIGRUN_DISTINCT_REVIEW
consumer: Ratatoskr_and_Olrun
next_phase: SMALLEST_HARMLESS_REVERSIBLE_MICRO_USE
sealed: false
---

# X13 DBOS Python campaign — Phase 1 official-contract baseline

## Question

Can the open-source DBOS Python library replace part of HFO's custom hot workflow machinery for one internal, no-external-effect golden path while Git remains the audit and heritage store?

This wake performs contract assessment only. It does not install DBOS, provision Postgres, create an account, deploy a service, run a workflow, or claim operational adoption.

## Self-probe and directly observed surfaces

- Native Scheduled Task ID matched exactly: `6a55c173370881918680ce67c4ecb197`.
- Native Tasks inventory: readable.
- GitHub: repository read/write available.
- Slack: read/write available.
- Web: current public-source research available.
- Shell, package installation, Postgres runtime, DBOS runtime, DBOS Cloud and Conductor account: not exposed in this carrier.
- Operator relay required for this baseline: `0 minutes`.

## Official contract baseline

Official sources inspected on `2026-07-31`:

1. DBOS documentation home: https://docs.dbos.dev/
2. DBOS architecture: https://docs.dbos.dev/architecture
3. Python workflow tutorial: https://docs.dbos.dev/python/tutorials/workflow-tutorial
4. Python transaction tutorial: https://docs.dbos.dev/python/tutorials/transaction-tutorial
5. Python queue reference: https://docs.dbos.dev/python/reference/queues
6. Workflow management: https://docs.dbos.dev/production/workflow-management
7. Official Python repository: https://github.com/dbos-inc/dbos-transact-py

Observed official claims and ceilings:

- DBOS is an open-source library that checkpoints workflow and step state in a system database and resumes interrupted workflows from the last completed step.
- The official Python repository reports release `2.22.0` dated `2026-05-15` and an MIT license.
- The library uses Postgres for durable workflow, queue, schedule and checkpoint state; official datasource documentation also describes Postgres or SQLite for application transactions.
- Durable queues support persisted configuration, concurrency limits, rate limits, timeouts, priorities and deduplication without requiring a separate message broker.
- DBOS supports Python, TypeScript, Go and Java, and the documentation says applications can run in environments chosen by the operator.
- Rich workflow search, graphical traces, cancellation, resume, fork and managed recovery are described as Conductor-connected capabilities. The open-source library alone must not be credited with the full Conductor management surface.
- Exactly-once is boundary-specific. Official datasource transactions atomically commit an application database write and its DBOS durability record. Ordinary steps can re-execute around a crash boundary and therefore require idempotent external effects or a transactional integration.
- Production high availability across several executors is strongly associated in the official architecture guidance with Conductor; this baseline does not prove that self-hosted library-only recovery meets HFO's availability target.

## Fit against the current HFO defect

The immediately preceding X12 experiment proved that the current Git-backed virtual object requires separate event and `CURRENT` commits and therefore has no cross-file transaction or exactly-once guarantee:

- Event: `c7060528ddb518f7bcc69924d13381b6c4e8085c`
- Pointer: `7a87a31fbf6c391fd972a5cbc120943a1510b516`

DBOS is a plausible COTS fit for the *hot* state machine because its stated primitives map to several missing organs:

| HFO need | DBOS official surface | Current assessment |
|---|---|---|
| durable workflow state | Postgres-backed checkpoints | plausible fit; untested here |
| crash recovery | resume from last completed step | plausible fit; untested here |
| work queues | durable queues and flow control | plausible fit; untested here |
| timers/schedules | persisted scheduled workflows | plausible fit; untested here |
| idempotent/exact processing | workflow IDs, deduplication and transaction boundary | useful but not universal; external effects still gated |
| operational history | programmatic/CLI workflow listing | baseline fit |
| graphical management/HA | Conductor | optional external dependency; terms/cost not baselined |
| immutable audit/heritage | not its primary role | retain Git receipts and terminal projections |

## Measurements

### Custom code potentially avoided

Inference, not runtime proof: a successful DBOS adoption could replace or sharply reduce bespoke implementation for approximately six hot-path concerns:

1. workflow checkpointing and restart;
2. durable queue pickup;
3. timer and schedule persistence;
4. retry/recovery state;
5. per-workflow execution history;
6. some idempotency and transactional bookkeeping.

It would **not** replace HFO authority policy, privacy rules, capability/effect brokerage, independent verification, ConsumerAck, Git heritage, Slack projection, domain acceptance tests, or adapters for external providers.

### Operator minutes

- Baseline research and contract reduction: approximately `15–20 minutes` of machine work; not operator labor.
- Operator relay during this phase: `0 minutes`.
- Installation and runtime-operation burden: unknown until Phase 2/3.

### Credentials and infrastructure

- Open-source library: no vendor account required by the inspected contract.
- Runtime: database credentials are required for the chosen Postgres or supported datasource.
- Conductor/DBOS Cloud: credentials and separate service relationship would be required; not authorized or tested.

### Durability

- Documented: durable workflow checkpoints in Postgres and recovery from the last completed step.
- Documented stronger boundary: datasource transaction can atomically bind application writes and durability records.
- Not proved here: behavior under executor death, database outage, schema migration, version skew, duplicate provider callbacks, or cross-region failure.

### Observability

- Documented without claiming account access: programmatic and CLI workflow listing and step inspection.
- Rich GUI, management and managed recovery: described for Conductor-connected applications.
- Direct HFO telemetry integration with OpenTelemetry or Slack/Git receipts: not tested.

### Portability

- Documented language surfaces: Python, TypeScript, Go and Java.
- Runtime portability is plausible because the library can run with the application, but the database and optional Conductor are operational dependencies.
- Migration portability from DBOS to another durable runtime is unknown; workflow annotations and recorded state may create framework coupling.

### Failure behavior

- Intended behavior: recover workflow execution after interruption.
- Important ceiling: an external call or nontransactional side effect inside a retried step can still duplicate unless its own idempotency key or transactional seam is used.
- Application-code bugs, nondeterminism, incompatible code changes and poison messages remain possible and require held-out failure tests.

### Direct cost and quota evidence

- Open-source Python library: MIT license; no library usage price found or incurred.
- Self-hosting cost: Postgres plus executor compute and operations; exact cost not measured.
- DBOS Cloud documentation says CPU-time charging, but this phase found no sufficiently specific current numeric price to record safely.
- Conductor price/quota: unknown from the inspected official pages.
- Paid calls made: `0`.

## Strongest objection

DBOS may improve the workflow engine while leaving the real HFO bottleneck untouched: reliable cross-provider effect execution and independent outcome sensing. Installing a durable runtime could become another architecture project if one tiny golden-path workflow cannot reduce operator relay and close a real ConsumerAck.

## Strongest falsifier

Retire or defer this candidate if a bounded Phase 2/3 micro-use cannot demonstrate all of the following without paid services or broad redesign:

1. deterministic start with a caller-supplied workflow/idempotency identity;
2. persisted state across a deliberate process interruption;
3. no duplicate accepted transition after replay;
4. inspectable workflow/step status;
5. a clean projection into one immutable Gen-133 receipt;
6. lower custom-code and operator burden than the existing Git-only pattern.

## Phase 2 packet

Run one local/reversible, no-external-effect Python micro-use on an execution surface that already has or may safely use ephemeral Postgres/SQLite support:

`READY -> CLAIMED -> PRODUCER_RETURNED -> VERDICT_RECORDED -> CONSUMER_ACKED`

Use deterministic strings only. Deliberately interrupt after `CLAIMED`, restart, and verify that recovery advances once without duplicating the claim transition. Record exact package lock/version, database mode, commands, exit codes, workflow ID, state rows, logs, cleanup and rollback. If no execution surface exists, return `HOLD_EXECUTION_SURFACE` rather than committing an untested adoption decision.

## Provisional disposition

`CONTINUE_TO_PHASE_2`

This is neither `ADOPT` nor `ADOPT_WITH_GATES`. The contract fits the diagnosed hot-state gap, but no direct DBOS execution evidence exists yet.

## Honest flaw

This baseline relies mostly on vendor-authored official documentation and repository metadata. No package was installed, no database was provisioned, no workflow was run, and no failure was injected. Release `2.22.0` is pinned from the official repository's visible latest-release metadata, but package-registry resolution was not independently reproduced. Cost, quota, lock-in, schema-migration and production-operability claims remain incomplete.

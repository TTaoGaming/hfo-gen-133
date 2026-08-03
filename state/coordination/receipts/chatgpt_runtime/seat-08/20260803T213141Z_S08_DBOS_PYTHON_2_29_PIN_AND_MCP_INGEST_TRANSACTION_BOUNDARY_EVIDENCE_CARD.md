---
schema_id: hfo.gen133.s08.research_evidence_card.v1
seat: S08_RESEARCH_AND_CANDIDATE_SCOUT
carrier_task_id_expected: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_observed: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_match: true
wip: 1
lane: AGENT_RUNTIME_COTS_CAPABILITIES
question_id: DBOS_PYTHON_PIN_AND_MCP_INGEST_TRANSACTION_BOUNDARY_001
question_changed: true
source_workitem: https://github.com/TTaoGaming/hfo-gen-133/issues/2
canonical_repository: TTaoGaming/hfo-gen-133
canonical_branch: agent/gen133-bootstrap-20260730
valid_time_utc: 2026-08-03T21:31:41Z
transaction_time_utc: SEE_GIT_COMMIT_METADATA
disposition: REVISE
candidate: dbos_python
candidate_package_pin: dbos==2.29.0
candidate_repository: dbos-inc/dbos-transact-py
candidate_source_commit: ab99c997a468e286b2899975ca525eeb05a4d888
candidate_release_date: 2026-07-30
candidate_license_reported: MIT
consumer: GEN133_POSTGRES_MCP_PORTFOLIO_INGESTOR_PIN_AND_TX_GATE_001
verifier: DISTINCT_HOST_OR_PROVIDER_CLEAN_POSTGRES_PROCESS_KILL_AND_DUPLICATE_INGEST_ASSAY
review_expiry_utc: 2026-08-10T21:31:41Z
fitness_credit: 0_PENDING_WORKITEM_CONSUMPTION_AND_CONSUMER_ACK
effect_ceiling: RESEARCH_FILE_AND_SANITIZED_POINTER_ONLY
sealed: false
---

# S08 evidence card — DBOS Python 2.29 pin and MCP-ingest transaction boundary

## Bounded uncertainty

The prior Gen-133 DBOS baseline pinned `dbos==2.22.0`. Is that still the correct exact candidate for issue #2's narrow Postgres MCP-portfolio ingestor, and which durability claims can the WorkItem safely place on the ingest transaction?

## Decision

`REVISE`.

Use the current stable release `dbos==2.29.0` for the next bounded specimen, pinned by artifact hash and source provenance. Do not promote the unreleased `2.30.0a*` line, and do not treat a package-version update as runtime admission. The specimen must separately prove clean schema initialization or migration, duplicate-ingest suppression, stop/start persistence, and the crash boundary on the exact Gen-133 ingest shape.

## Exact candidate and supply-chain binding

Observed from PyPI on `2026-08-03`:

- package: `dbos==2.29.0`
- release date: `2026-07-30`
- source repository and attested commit: `dbos-inc/dbos-transact-py@ab99c997a468e286b2899975ca525eeb05a4d888`
- attested release branch: `refs/heads/release/v2.29.0`
- wheel: `dbos-2.29.0-py3-none-any.whl`
- wheel SHA-256: `49104b64b8917dc3d321704f1d20058486c86129420b96b910f1e725fbdebca6`
- source distribution: `dbos-2.29.0.tar.gz`
- source-distribution SHA-256: `ae6015bba43b5842a4a99abcc7826ca00c758af767ebaf79e6304c0b4f58ec46`
- reported license: MIT
- Python requirement: `>=3.10`
- PyPI classifier: Production/Stable

PyPI lists `2.22.0` as released on `2026-05-15`, followed by stable releases `2.23.0` through `2.29.0`. It lists `2.30.0a1` and `2.30.0a2` as prereleases, not the stable candidate.

## Supported claims

1. **Exact current stable candidate exists.** PyPI currently exposes `2.29.0` as the stable release and binds its wheel and source distribution to the exact hashes and source commit above through trusted-publishing provenance.
2. **Datasource transactions fit the database-only ingest seam.** Current DBOS Python documentation says a datasource transaction records its outcome atomically in the same PostgreSQL or SQLite transaction and returns the stored result on workflow replay instead of re-executing the transaction function.
3. **The library creates durability state in the application database.** `SQLAlchemyDatasource.create` runs migrations for a `datasource_outputs` tracking table, defaulting to PostgreSQL schema `dbos`; the documented default transaction isolation is `SERIALIZABLE`.
4. **Issue #2's database rows can share one atomic boundary.** The MCP server row, verification row, deployment pointer, publication-gate row, and a local outbox or transactional-enqueue record can be written inside one datasource transaction when they are in the same PostgreSQL database.
5. **Workflow identity can supplement database uniqueness.** A deterministic workflow ID may act as an idempotency key, but the WorkItem should retain the database uniqueness constraint on `(repo_full_name, head_sha, check_type)` as the authoritative duplicate-ingest guard.

## Excluded claims

- No package was installed and no DBOS workflow or migration was executed in this pass.
- `2.29.0` compatibility with the existing local `2.22.0` state, schemas, or untracked Gen-133 files is unproved.
- Semantic-version numbering is not evidence that a live migration is safe.
- A DBOS datasource transaction cannot atomically commit GitHub, Slack, Cloudflare, or other remote-provider effects with PostgreSQL.
- A normal external-API step is not an exactly-once remote effect. DBOS documentation requires steps to be idempotent because recovery can retry an uncheckpointed step.
- Durable retry or eventual workflow completion is not proof that a remote provider received an effect once.
- Production high availability, throughput, database sizing, version-skew behavior, backup/restore, and managed DBOS Cloud or Conductor behavior are outside this card.
- No operator relief, customer outcome, or income claim is supported.

## Required WorkItem revision

Pin the next specimen as:

```text
dbos==2.29.0 \
  --hash=sha256:49104b64b8917dc3d321704f1d20058486c86129420b96b910f1e725fbdebca6
```

Also record source provenance `dbos-inc/dbos-transact-py@ab99c997a468e286b2899975ca525eeb05a4d888` and the sdist hash above. Use a clean ephemeral PostgreSQL database and environment-only credentials.

The ingest workflow must:

1. derive one deterministic workflow ID from the bounded inventory snapshot or ingest batch;
2. execute all Gen-133 database rows plus one local outbox/transactionally-enqueued follow-up record in a datasource transaction;
3. retain a database unique constraint on `(repo_full_name, head_sha, check_type)`;
4. ingest the same eight exact repository heads twice and prove the second request produces no duplicate accepted rows;
5. kill the process after the datasource transaction commits but before the surrounding workflow records its next completed boundary, then restart;
6. prove the transaction function is not re-executed and the stored result is replayed;
7. keep Git and Slack projection disabled during the assay; remote effects require a later idempotent consumer and provider readback;
8. record exact package lock, database schema before/after, commands, exit codes, row counts, workflow ID, logs, cleanup, and rollback.

## License and terms uncertainty

The package metadata and repository report MIT licensing. This card did not inventory every transitive dependency or its license. PyPI, GitHub, PostgreSQL hosting, DBOS Cloud, and Conductor terms and costs were not accepted, invoked, or baselined. Only the open-source library candidate is in scope.

## Cost and operator-minute estimate

- direct spend in this pass: `$0`
- operator minutes in this pass: `0`
- estimated producer specimen: `30–60 minutes`
- estimated distinct verification: `20–40 minutes`
- paid service required for the proposed local/ephemeral assay: `none observed`
- ongoing self-hosted PostgreSQL compute and operations: `UNKNOWN`

## Strongest objection

Updating the pin may create version-churn work while issue #2's real bottleneck is a small tracked schema and ingestor, not framework selection. The response is to keep the change bounded: one exact current-stable specimen only. If `2.29.0` adds migration or operational burden without reducing custom idempotency/recovery code, DBOS should be deferred rather than allowed to become another architecture project.

## Falsifier

`RETIRE` or revert the candidate pin if a clean, reproducible `2.29.0` assay cannot initialize or migrate its required schema, cannot replay a committed datasource transaction without re-running it after process death, produces duplicate rows or duplicate local outbox records for the same deterministic identity, or requires managed services or broader redesign to satisfy issue #2's acceptance gate.

## Verifier packet

A distinct host or provider should reproduce with the exact wheel hash and source commit, a clean PostgreSQL instance, and no remote effects. It should ingest the eight issue-#2 heads twice, inject a process kill after the database commit boundary, restart, and independently query:

- one accepted server row per exact head;
- one verification row per `(repo_full_name, head_sha, check_type)`;
- one local follow-up/outbox record per accepted transition;
- no duplicate transition after replay;
- persisted state after database stop/start;
- no GitHub, Slack, Cloudflare, npm, Registry, or other external write.

## Consumer and expiry

- consumer gate: `GEN133_POSTGRES_MCP_PORTFOLIO_INGESTOR_PIN_AND_TX_GATE_001`
- upstream WorkItem: GitHub issue `TTaoGaming/hfo-gen-133#2`
- next routing: S06 packet compiler or S07 bounded builder, then S03 reducer with a distinct verifier
- expiry: `2026-08-10T21:31:41Z`
- fitness: `0` until the exact card is consumed by a WorkItem and receives ConsumerAck

## Dated primary sources

Accessed `2026-08-03`:

1. PyPI, `dbos 2.29.0`, release history, metadata, file hashes, and trusted-publishing provenance: https://pypi.org/project/dbos/2.29.0/
2. DBOS Python, Transactions & Datasources: https://docs.dbos.dev/python/tutorials/transaction-tutorial
3. DBOS Python, Datasources reference: https://docs.dbos.dev/python/reference/datasources
4. DBOS Python, Workflows and guarantees: https://docs.dbos.dev/python/tutorials/workflow-tutorial
5. DBOS architecture, step idempotency and recovery boundary: https://docs.dbos.dev/architecture
6. DBOS Python, Transactional Outbox example: https://docs.dbos.dev/python/examples/outbox
7. DBOS Python official repository at the attested source commit: https://github.com/dbos-inc/dbos-transact-py/tree/ab99c997a468e286b2899975ca525eeb05a4d888
8. Gen-133 WorkItem: https://github.com/TTaoGaming/hfo-gen-133/issues/2
9. Prior Gen-133 DBOS baseline: `state/coordination/experiments/cots_connector_x13/20260731T214800Z_DBOS_PYTHON_PHASE1_OFFICIAL_CONTRACT_BASELINE.md`

## Honest flaw

This is current contract and release-provenance research, not execution evidence. The exact migration path from the prior `2.22.0` candidate, behavior of the current untracked local DBOS state, dependency resolution, cold-start duration, process-kill outcome, database restart, and actual custom-code reduction remain unknown until the proposed specimen is run and independently read back.

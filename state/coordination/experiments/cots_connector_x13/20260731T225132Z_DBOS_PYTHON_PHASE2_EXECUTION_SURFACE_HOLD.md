---
schema_id: hfo.gen133.x13.cots_connector_event.v1
experiment_id: X13_DBOS_PYTHON_DURABLE_KERNEL_001
seat: X13_COTS_CONNECTOR_PDCA
addressed_to: S04_STRUCTURAL_PREFLIGHT
carrier_task_id_expected: 6a55c1733708819185088bf334e33ea5
carrier_task_id_observed: 6a55c1733708819185088bf334e33ea5
carrier_task_id_match: true
prior_current_version: 1
next_current_version: 2
prior_current_blob_sha: 1b647f7ed44361a914f92ac48fe42c6734b38387
phase_attempted: 2_of_4
phase_completed: 1_of_4
phase_name: SMALLEST_HARMLESS_REVERSIBLE_MICRO_USE
candidate: DBOS_Python
candidate_pin: 2.22.0
result: HOLD_EXECUTION_SURFACE
binding_decision: false
measured_fact_changed: true
valid_time_utc: 2026-07-31T22:51:32Z
transaction_time_utc: SEE_GIT_COMMIT_METADATA
canonical_repository: TTaoGaming/hfo-gen-133
canonical_branch: agent/gen133-bootstrap-20260730
repository_head_observed_before_write: a5bd985d493d732afe38a44b1ce1623f881fe127
wip: 1
effect_ceiling: EPHEMERAL_LOCAL_EXECUTION_AND_GIT_SLACK_RECEIPT_ONLY
verifier: S04_STRUCTURAL_PREFLIGHT_THEN_OLRUN_DISTINCT_HOST_RUNTIME
consumer: Ratatoskr_and_Olrun
next_phase: RETRY_PHASE_2_ON_EXISTING_HOST_WITH_DBOS_PACKAGE_RESOLUTION
sealed: false
---

# X13 DBOS Python campaign — Phase 2 execution-surface hold

## Result

`HOLD_EXECUTION_SURFACE`

A real ephemeral Python execution surface was exposed and probed, but it could not resolve the pinned DBOS package. No DBOS code ran. No SQLite database, workflow, durable step, interruption, restart, or recovery evidence was produced. This is a measured connector/runtime limitation, not a rejection of DBOS.

## Self-probe and task binding

Native Tasks readback returned this carrier as task `6a55c1733708819185088bf334e33ea5`, matching the expected ID exactly.

A prior projection defect was also found:

- Phase 1 event front matter correctly bound X13 to `6a55c1733708819185088bf334e33ea5`.
- The Phase 1 prose incorrectly stated the S06 task ID `6a57972b9df081918680ce67c4ecb197` as the observed X13 ID.
- `CURRENT.md` version 1 also carried the incorrect task ID `6a55c173370881918680ce67c4ecb197`.

The immutable Phase 1 event is not edited. This event records the contradiction and the version-2 pointer corrects the live task binding.

## Controlled micro-use attempted

Target acceptance remained:

`READY -> CLAIMED -> PRODUCER_RETURNED -> VERDICT_RECORDED -> CONSUMER_ACKED`

with a deterministic workflow ID, deliberate process interruption after `CLAIMED`, restart, single nonduplicated advance, inspectable workflow history, and cleanup.

The package installation gate failed before the workflow specimen could be created.

### Runtime

- Python: `3.13.5`
- Environment: fresh ephemeral virtual environment under `/tmp/hfo_x13_dbos_phase2`
- Candidate pin: `dbos==2.22.0`
- Credentials used: none
- Paid calls: none
- External effects: none

### Probe 1 — configured package index

Command:

```bash
python -m pip install --disable-pip-version-check --no-input --dry-run 'dbos==2.22.0'
```

Observed result:

- exit code: `1`
- measured latency: `0.31 seconds`
- package index class: platform-configured internal PyPI gateway
- error class: `PACKAGE_NOT_AVAILABLE_ON_CONFIGURED_INDEX`
- exact terminal error: `No matching distribution found for dbos==2.22.0`
- DBOS import after attempted installation: unavailable

The index URL contained a masked service credential in tool output and is not copied into this public artifact.

### Probe 2 — official GitHub release archive

Command:

```bash
curl --connect-timeout 5 --max-time 10 -L --fail --silent --show-error \
  -o /dev/null \
  https://github.com/dbos-inc/dbos-transact-py/archive/refs/tags/2.22.0.tar.gz
```

Observed result:

- exit code: `6`
- measured latency: `<0.01 seconds` as exposed by `/usr/bin/time`
- error class: `PUBLIC_DNS_UNAVAILABLE_FROM_EXECUTION_CONTAINER`
- exact terminal error: `Could not resolve host: github.com`

No archive bytes were downloaded.

## Primary-source compatibility check

The official `2.22.0` `pyproject.toml` was read through the authenticated GitHub connector, not executed. It states:

- `requires-python = ">=3.10"`;
- Python `3.13` classifier present;
- package name `dbos`;
- MIT license;
- optional `aiosqlite` dependency.

Official current DBOS Python documentation says the system database defaults to SQLite for local use and recommends Postgres for production. Therefore the blocked install is not explained by the observed Python 3.13 runtime or by an unavoidable Postgres requirement. The strongest supported explanation is connector variance: this execution container can reach only its configured mirror, where the pinned package is absent, while public DNS is unavailable.

Primary sources checked on `2026-07-31`:

- https://docs.dbos.dev/python/programming-guide
- https://docs.dbos.dev/python/tutorials/testing
- https://docs.dbos.dev/python/tutorials/workflow-tutorial
- https://docs.dbos.dev/production/workflow-recovery
- https://github.com/dbos-inc/dbos-transact-py/blob/2.22.0/pyproject.toml

## Measurements

### Custom code avoided

- Proven avoided in Phase 2: `0` lines / `0` components.
- Still plausible but unproved from Phase 1: checkpointing, recovery, queues, timers, workflow history, and some idempotency bookkeeping.
- No replacement credit is earned until a real restart/recovery specimen passes.

### Operator minutes

- Operator relay required: `0 minutes`.
- Operator action requested: none.
- Machine investigation time: approximately `5 minutes`.
- Operator minutes removed by this blocked wake: `0`; it prevents an operator from being asked to attempt an interactive login or install blindly.

### Credentials

- No DBOS account, API key, database credential, GitHub token, or secret was created or exposed.
- The platform-internal package index authentication remained masked and was not externalized.

### Durability and recovery

- Direct durability evidence: none.
- Direct restart evidence: none.
- Direct exactly-once or nonduplication evidence: none.
- Official contract evidence remains only documentary.

### Observability

- Direct DBOS workflow/step history: none.
- Tool-level observability obtained: exact command, exit code, latency, runtime version, and error class.

### Portability and connector variance

- Candidate metadata supports Python 3.13.
- The execution surface cannot presently resolve the package from either its configured mirror or public GitHub DNS.
- This does not establish whether Olrun/Claude, a local workstation, VM, or GitHub Actions runner can install the same pin.

### Failure behavior

- Observed failure is fail-closed before runtime initialization.
- No partial DBOS state was created.
- Cleanup: the only residue is an ephemeral `/tmp` directory and empty virtual environment; no durable account or external resource exists.

### Direct cost and quota evidence

- Direct monetary cost incurred: `$0`.
- Paid API calls: `0`.
- Package-download bytes: `0`.
- Quota evidence: only the configured package surface and DNS restriction; no DBOS vendor quota was exercised.

## Reversible next experiment

Run the exact same pin on one already-authorized host that has ordinary package resolution, preferably a disposable local/VM checkout or a GitHub Actions job already permitted by a bounded WorkItem. Use SQLite only, deterministic strings only, no external calls, and delete the temporary database after collecting exact hashes and logs.

Do not provision DBOS Cloud or Conductor. Do not create an account. Do not broaden this into runtime architecture work.

## Strongest objection

A host-specific install success would still not prove that DBOS improves HFO. The real acceptance remains deliberate interruption, automatic recovery, one accepted transition, inspectable history, low operator burden, and clean projection into Git.

## Strongest falsifier

`DEFER` or `REJECT` the candidate if an authorized host with normal package access cannot run the pinned SQLite specimen, or if a deliberate restart duplicates the accepted transition, loses the workflow, requires broad custom recovery code, or costs more operator effort than the Git-only pattern.

## Honest flaw

This carrier measured only one container and one package mirror. Public DNS was unavailable, so no vendor package bytes were independently executed. The result cannot distinguish “package absent from this mirror” from a broader packaging or dependency issue on another host. It also exposes a prior X13 task-binding contradiction that should have been caught before Phase 1 was projected as clean.

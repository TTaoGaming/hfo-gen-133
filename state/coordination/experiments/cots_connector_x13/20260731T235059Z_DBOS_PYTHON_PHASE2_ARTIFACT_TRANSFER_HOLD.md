---
schema_id: hfo.gen133.x13.cots_connector_event.v1
experiment_id: X13_DBOS_PYTHON_DURABLE_KERNEL_001
seat: X13_COTS_CONNECTOR_PDCA
addressed_to: S04_STRUCTURAL_PREFLIGHT
carrier_task_id_expected: 6a55c1733708819185088bf334e33ea5
carrier_task_id_observed: 6a55c1733708819185088bf334e33ea5
carrier_task_id_match: true
prior_current_version: 2
next_current_version: 3
prior_current_blob_sha: c8cf02ff1dbfd9be8470c524359e56ef0c5b5e3c
phase_attempted: 2_of_4
phase_completed: 1_of_4
phase_name: SMALLEST_HARMLESS_REVERSIBLE_MICRO_USE
candidate: DBOS_Python
candidate_pin: 2.22.0
result: HOLD_ARTIFACT_TRANSFER_SURFACE
binding_decision: false
measured_fact_changed: true
valid_time_utc: 2026-07-31T23:50:59Z
transaction_time_utc: SEE_GIT_COMMIT_METADATA
canonical_repository: TTaoGaming/hfo-gen-133
canonical_branch: agent/gen133-bootstrap-20260730
wip: 1
effect_ceiling: EPHEMERAL_LOCAL_EXECUTION_AND_GIT_SLACK_RECEIPT_ONLY
verifier: S04_STRUCTURAL_PREFLIGHT_THEN_OLRUN_DISTINCT_HOST_RUNTIME
consumer: Ratatoskr_and_Olrun
next_phase: RETRY_PHASE_2_ON_EXISTING_HOST_WITH_ORDINARY_PACKAGE_RESOLUTION
sealed: false
---

# X13 DBOS Python campaign — Phase 2 artifact-transfer hold

## Result

`HOLD_ARTIFACT_TRANSFER_SURFACE`

The controlled Phase 2 retry did not run DBOS. The same ephemeral Python 3.13.5 carrier could not resolve `dbos==2.22.0` or its missing dependencies through the configured package index, and direct public DNS remained unavailable. A new primary-source fact was established: official PyPI currently exposes the exact `2.22.0` source distribution and universal Python wheel, with published SHA-256 digests and Trusted Publishing provenance. This materially narrows the failure to carrier/package-transfer variance rather than package nonexistence.

No DBOS package bytes entered the execution container. No SQLite database, workflow, step, interruption, recovery, workflow history, or cleanup test ran. Adoption credit remains zero.

## Self-probe and available tools

Native Tasks readback returned this carrier as task `6a55c1733708819185088bf334e33ea5`, matching the expected ID exactly.

Observed surfaces in this wake:

- native Scheduled Tasks inventory read;
- GitHub repository read/write connector;
- Slack connector available for a sanitized pointer;
- web research surface reachable for official public documentation and PyPI metadata;
- ephemeral Python 3.13.5 shell/container;
- configured package index reachable but not populated with DBOS or required missing packages;
- direct public DNS unavailable from the execution container.

## Exact controlled probes

### Probe A — pinned package installation retry

Command:

```bash
python3 -m venv /tmp/hfo_x13_dbos_phase2_retry
/tmp/hfo_x13_dbos_phase2_retry/bin/python -m pip install \
  --disable-pip-version-check --no-input 'dbos==2.22.0'
```

Observed:

- Python: `3.13.5`;
- pip: `25.1.1`;
- exit code: `1`;
- measured latency: `0.36 seconds`;
- error class: `PACKAGE_NOT_AVAILABLE_ON_CONFIGURED_INDEX`;
- terminal error: `No matching distribution found for dbos==2.22.0`;
- package-index URL contained platform-internal routing information and is not externalized.

### Probe B — missing dependency availability

Command:

```bash
/tmp/hfo_x13_dbos_phase2_retry/bin/python -m pip install \
  --disable-pip-version-check --no-input \
  'psycopg[binary]>=3.1' 'aiosqlite>=0.20.0'
```

Observed:

- exit code: `1`;
- error class: `REQUIRED_DEPENDENCIES_NOT_AVAILABLE_ON_CONFIGURED_INDEX`;
- first terminal error: `No matching distribution found for psycopg>=3.1`.

Global runtime inspection found PyYAML, python-dateutil, websockets, Typer, SQLAlchemy, and OpenTelemetry installed, but `psycopg` and `aiosqlite` absent. This is only a carrier inventory fact; it does not prove DBOS's minimal runtime dependency path.

### Probe C — direct public package page from the shell

Command:

```bash
curl --connect-timeout 10 --max-time 20 -L --fail --silent --show-error \
  https://pypi.org/project/dbos/2.22.0/
```

Observed:

- exit code: `6`;
- measured latency: `0.02 seconds`;
- error class: `PUBLIC_DNS_UNAVAILABLE_FROM_EXECUTION_CONTAINER`;
- terminal error: `Could not resolve host: pypi.org`.

## New official package evidence

Official PyPI metadata, read through the web research surface on `2026-07-31`, reports:

- version `2.22.0` published `2026-05-15`;
- source distribution `dbos-2.22.0.tar.gz`, size about `479.2 kB`, SHA-256 `5d43a9d0388d851df0f7bbd4ed752bc8b67be3d6fbe358c8be4d22f6c4887db6`;
- universal wheel `dbos-2.22.0-py3-none-any.whl`, size about `198.1 kB`, SHA-256 `09edc621ec2857dae73cc1b01bc7379999fe9ee4ef8c6ff4ac69dd1a5263001f`;
- both artifacts published using PyPI Trusted Publishing;
- provenance names source commit `dbos-inc/dbos-transact-py@6a51efd7e305930af4fb736c7d3b98eaa988ca01`.

Primary pointers:

- https://pypi.org/project/dbos/2.22.0/
- https://github.com/dbos-inc/dbos-transact-py/releases/tag/2.22.0
- https://docs.dbos.dev/python/programming-guide
- https://docs.dbos.dev/production/workflow-recovery

The published hashes were not recomputed because the package bytes were not downloadable through the exposed execution surface.

## Campaign measurements

### Custom code avoided

- Proven avoided: `0` lines / `0` components.
- Documentary candidate scope only: checkpointing, restart recovery, workflow history, queues, timers, and idempotency primitives.
- No code-avoidance credit is earned without a passing restart specimen.

### Operator minutes

- Operator relay: `0 minutes`.
- Operator action requested: none.
- Approximate machine investigation time: `7 minutes`.
- Operator minutes removed by this wake: `0`; the useful output is a narrower connector-variance diagnosis.

### Credentials and cost

- Credentials created or used for DBOS: none.
- Account creation or terms acceptance: none.
- Paid calls: `0`.
- Direct monetary cost: `$0`.
- Package-download bytes: `0`.
- Vendor quota exercised: none.

### Durability and observability

- Direct DBOS durability evidence: none.
- Direct restart/recovery evidence: none.
- Direct exactly-once/nonduplication evidence: none.
- Direct workflow history evidence: none.
- Tool-level observability: exact commands, exit codes, latency where exposed, runtime version, dependency inventory, official artifact names, and published hashes.

### Portability and connector variance

- Official metadata proves the pinned package exists as a universal wheel and source distribution.
- This carrier cannot transfer those bytes through its configured package mirror or direct DNS.
- The result does not predict availability on Olrun/Claude, a local workstation, a VM, or an authorized GitHub Actions runner.

### Failure behavior

- Failure remained fail-closed before DBOS initialization.
- No partial workflow state or external resource was created.
- Ephemeral residue is limited to `/tmp/hfo_x13_dbos_phase2_retry`; it may be discarded by the carrier runtime.

## Reversible next experiment

Run the exact pinned wheel or normal `pip install dbos==2.22.0` on one already-authorized host with ordinary package resolution. Use SQLite only and deterministic strings. Interrupt after the first durable step, restart once, confirm the workflow advances without duplicating that step, inspect workflow and step history, record exact package hash and commands, then delete the temporary database.

Do not provision DBOS Cloud or Conductor, create an account, accept terms, or broaden into architecture work.

## Strongest objection

The new PyPI evidence proves only artifact publication, not runtime fitness. A successful install on another host could still fail the HFO-relevant interruption, nonduplication, observability, portability, and operator-burden gates.

## Strongest falsifier

Return `DEFER` or `REJECT` if an authorized host with ordinary package access cannot install the pinned artifact, or if the restart specimen duplicates the accepted transition, loses workflow state, requires broad custom recovery code, lacks inspectable history, or imposes more operator work than the current Git-only pattern.

## Git atomicity and rollback

The immutable event and mutable `CURRENT.md` pointer are separate Git commits. GitHub's contents API does not make those two writes atomic. If the pointer update fails, this event remains an orphaned immutable measurement and `CURRENT.md` must not be treated as advanced. Rollback is pointer-only: restore `CURRENT.md` version 2 using its prior blob; never delete or rewrite this event.

## Honest flaw

The package hashes and Trusted Publishing provenance are provider-published metadata, not locally recomputed evidence. No vendor package bytes were executed. The repeated install failure may be redundant at the runtime level; the only material advance is proving that official artifacts exist while this carrier lacks an artifact-transfer path. Same-provider structural review cannot substitute for the distinct-host runtime verifier.

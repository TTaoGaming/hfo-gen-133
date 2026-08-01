---
schema_id: hfo.gen133.x13.cots_connector_event.v1
experiment_id: X13_DBOS_PYTHON_DURABLE_KERNEL_001
seat: X13_COTS_CONNECTOR_PDCA
addressed_to: S04_STRUCTURAL_PREFLIGHT
carrier_task_id_expected: 6a55c1733708819185088bf334e33ea5
carrier_task_id_observed: 6a55c1733708819185088bf334e33ea5
carrier_task_id_match: true
prior_current_version: 3
next_current_version: 4
prior_current_blob_sha: 88e06d9e229d10ccc21daec4e505fab781097c7c
campaign_wake: 4_of_4
phase_attempted: 3_and_4_of_4
phase_2_completed: false
phase_3_scope: FAILURE_PERMISSION_PORTABILITY_AND_CONNECTOR_VARIANCE
candidate: DBOS_Python
candidate_pin: 2.22.0
result: DEFER
binding_decision: false
measured_fact_changed: true
valid_time_utc: 2026-08-01T00:51:34Z
transaction_time_utc: SEE_GIT_COMMIT_METADATA
canonical_repository: TTaoGaming/hfo-gen-133
canonical_branch: agent/gen133-bootstrap-20260730
repository_head_observed_before_write: 4e8f2cf6fdce240fb1f1110d4514e0cae33ca02c
wip: 1
effect_ceiling: EPHEMERAL_LOCAL_READ_DOWNLOAD_ATTEMPT_AND_GIT_SLACK_RECEIPT_ONLY
verifier: S04_STRUCTURAL_PREFLIGHT_THEN_OLRUN_DISTINCT_HOST_RUNTIME
consumer: Ratatoskr_and_Olrun
next_campaign_candidate: GitHub_Contents_API
sealed: false
---

# X13 DBOS Python campaign — connector-variance probe and four-wake decision

## Decision

`DEFER`

This is a carrier-bounded defer, not a rejection of DBOS. The campaign did not complete the required SQLite interruption/restart micro-use, so it has no direct durability, recovery, nonduplication, workflow-history, or custom-code-avoidance evidence. The strongest supported conclusion is that this ChatGPT carrier lacks an allowed artifact-ingress path for the pinned package even though official package hosting responds.

## Self-probe

- Native task inventory exposed X13 as `6a55c1733708819185088bf334e33ea5`; it matches the expected ID.
- Available surfaces used: native Tasks readback, GitHub read/write, web primary-source research, ephemeral Python 3.13.5 shell, controlled binary-download broker, and Slack write for a sanitized decision pointer.
- No task, account, credential, service, deployment, terms, payment, or production state was mutated.

## Controlled factor

Only artifact-transfer surface varied. Candidate, version pin, official URLs, Python runtime class, zero-cost ceiling, and no-account constraint remained fixed.

## Exact probes and measured results

### Probe A — official wheel through controlled download broker

Target:

`dbos-2.22.0-py3-none-any.whl`

Observed broker metadata:

- HTTP status: `200`;
- declared content length: `198070` bytes;
- content type: `application/octet-stream`;
- result: file not persisted because the broker policy rejects that content type;
- error class: `ARTIFACT_INGRESS_POLICY_REJECTED_BINARY_MIME`;
- latency: not exposed;
- locally recomputed SHA-256: unavailable because bytes were not released to the filesystem.

### Probe B — official source distribution through controlled download broker

Target:

`dbos-2.22.0.tar.gz`

Observed broker metadata:

- HTTP status: `200`;
- declared content length: `479210` bytes;
- reported content type: `application/octet-stream`;
- derived content type: `application/gzip`;
- result: file not persisted because the broker policy rejects that content type;
- error class: `ARTIFACT_INGRESS_POLICY_REJECTED_ARCHIVE_MIME`;
- latency: not exposed;
- locally recomputed SHA-256: unavailable because bytes were not released to the filesystem.

### Probe C — shell DNS control

The shell repeated a direct `curl` request to the official wheel host.

- exit code: `6`;
- error: `Could not resolve host: files.pythonhosted.org`;
- error class: `PUBLIC_DNS_UNAVAILABLE_FROM_EXECUTION_CONTAINER`.

## Official-contract boundary retained

Official DBOS documentation states that local Python examples default to SQLite and that interrupted workflows on a single server are recovered on process restart. Official PyPI publishes the pinned universal wheel and source distribution with Trusted Publishing provenance and published SHA-256 values. These remain documentary/provider facts only; this campaign did not execute the artifacts or independently recompute their hashes.

## Four-wake measurements

### Custom code avoided

- Proven avoided: `0` lines and `0` components.
- Potentially avoidable hot-path concerns remain documentary only: workflow checkpointing, restart recovery, durable queues/timers, workflow history, and some idempotency bookkeeping.

### Operator minutes

- Operator relay: `0 minutes`.
- Operator action requested: none.
- Operator minutes removed: approximately `3–5` minutes by closing the repeated carrier-local install loop and preventing another blind retry on the same surface.

### Credentials

- DBOS/vendor credentials: none.
- Database credentials: none.
- Account creation or terms acceptance: none.

### Durability

- Direct DBOS durability evidence: none.
- Direct interruption/restart evidence: none.
- Direct nonduplication evidence: none.

### Observability

- Direct workflow or step history: none.
- Carrier-level evidence: exact artifact names, HTTP status, content lengths, MIME classes, policy rejection, shell exit code, and package-provider hashes from official metadata.

### Portability and connector variance

- Web metadata surface can resolve the official package and exact artifact URLs.
- The controlled download broker reaches the host and receives HTTP `200`, but refuses both binary/archive MIME classes before persistence.
- The shell cannot resolve the same public host.
- This proves connector variance inside this carrier; it does not predict Olrun/Claude, a local workstation, VM, GitHub Actions, or an ordinary package-enabled host.

### Failure behavior

- Failure is fail-closed before package installation or DBOS initialization.
- No partial database, workflow, account, external resource, or vendor quota state was created.
- Rollback is trivial: discard ephemeral `/tmp` paths; no downloaded bytes were persisted.

### Direct cost and quota evidence

- Paid calls: `0`.
- Direct monetary cost: `$0`.
- Provider package bytes persisted: `0`.
- Two broker requests reached HTTP `200`; no DBOS vendor quota or managed service was exercised.

## Strongest objection

This decision could be overfitting to ChatGPT carrier policy. A normal host may install the package and pass the bounded SQLite recovery specimen quickly, making the current defer operationally irrelevant outside this carrier.

## Strongest falsifier

A distinct authorized host overturns this defer by recording all of the following against the exact pin: artifact hash, exact commands and exit codes, deterministic workflow ID, deliberate process interruption after the first durable step, restart recovery, first-step execution count of one, inspectable workflow and step history, cleanup, cost, credentials, and honest flaw.

## Disposition and next campaign

- Campaign decision: `DEFER`.
- Adoption credit: `0`.
- Reopen condition: direct distinct-host runtime receipt satisfying the strongest falsifier.
- Do not repeat package installation on this unchanged carrier surface.
- Next X13 four-wake campaign candidate: native GitHub Contents API, because it is directly available and can be tested for contract, reversible use, conflict behavior, portability, and actual atomicity limits without inventing infrastructure.

## Git atomicity and rollback

This immutable event and the mutable `CURRENT.md` projection require separate GitHub Contents API commits. They are not cross-file atomic, transactional, linearizable, or exactly-once. If the pointer update conflicts, this event remains an orphaned immutable decision candidate and version 3 remains authoritative. Pointer rollback restores the prior `CURRENT.md` blob; this event is never deleted or rewritten.

## Honest flaw

The download broker exposed status, length, and MIME classification but withheld bytes, timing, and a documented policy identifier. Therefore the precise enforcement layer is inferred from tool behavior, not independently documented. Phase 2 never completed, and Phase 3 measured carrier connector variance rather than DBOS runtime failure, permission behavior after initialization, schema migration, or production portability. Same-provider structural review has binding weight zero and cannot close the distinct-host verification gap.

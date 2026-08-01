---
schema_id: hfo.gen133.x13.cots_connector_event.v1
experiment_id: X13_GITHUB_CONTENTS_API_001
seat: X13_COTS_CONNECTOR_PDCA
addressed_to: S04_STRUCTURAL_PREFLIGHT
carrier_task_id_expected: 6a55c1733708819185088bf334e33ea5
carrier_task_id_observed: 6a55c1733708819185088bf334e33ea5
carrier_task_id_match: true
prior_current_version: 5
next_current_version: 6
prior_current_blob_sha: 9b34b93b2948e0f8c1695ed5c8df1f15ffe6f9c3
campaign_wake: 2_of_4
phase_attempted: 2_of_4
phase_1_completed: true
phase_2_completed: true
phase_3_completed: false
phase_4_decision: PENDING
candidate: GitHub_REST_Contents_API
result: MICRO_USE_ROLLBACK_CONFIRMED
measured_fact_changed: true
valid_time_utc: 2026-08-01T02:48:11Z
transaction_time_utc: SEE_GIT_COMMIT_METADATA
canonical_repository: TTaoGaming/hfo-gen-133
canonical_branch: agent/gen133-bootstrap-20260730
wip: 1
effect_ceiling: EXPERIMENT_DIRECTORY_UTF8_CREATE_SHA_BOUND_UPDATE_FORWARD_ROLLBACK_ONLY
verifier: S04_STRUCTURAL_PREFLIGHT_THEN_DISTINCT_NONPRODUCER
consumer: Ratatoskr_and_Olrun
expiry_utc: 2026-08-08T02:48:11Z
sealed: false
---

# X13 GitHub Contents API campaign — phase 2 reversible micro-use

## Self-probe

- Native scheduled-task inventory exposed X13 task ID `6a55c1733708819185088bf334e33ea5`; it matched the expected ID.
- Direct surfaces used: native Tasks readback and authenticated GitHub UTF-8 create, fetch, and SHA-bound update wrappers.
- No task, account, terms, payment, deployment, merge, publication, secret, production path, history rewrite, or deletion was mutated.

## Controlled specimen

Path:

`state/coordination/experiments/cots_connector_x13/specimens/20260801T024651Z_GITHUB_CONTENTS_PHASE2_REVERSIBLE.txt`

The specimen was confined to the X13 experiment directory and used one nonce, one multibyte UTF-8 probe, and two deterministic states.

### State A — baseline

- UTF-8 bytes: `195`
- SHA-256: `1c0cb81dff110dbc55b55bd4bddc8fecb761c3860f7851d64f981362488b15a3`
- recomputed Git blob SHA-1: `a9826e11db433c9ae3180b8590b7720a2d4388f7`
- create commit: `69bb7578d17559a409b2a60975912181fffd685c`
- connector call duration exposed for create: `812 ms`
- first readback returned the exact submitted UTF-8 string and blob SHA `a9826e11db433c9ae3180b8590b7720a2d4388f7`

### State B — reversible replacement

The update supplied the fetched State-A blob SHA as the mandatory expected `sha`.

- UTF-8 bytes: `204`
- SHA-256: `983982b4311670005ff68bd7d6b6120c3d9b85417b9880fd772f9700fbb25def`
- recomputed Git blob SHA-1: `a9ba2dad14ed9bc72179ee709e7712dd9ff50449`
- update commit: `611ebcc8af302719a7e8d56910f231f7104ec724`
- connector call duration exposed for update: `702 ms`
- second readback returned the exact submitted UTF-8 string and blob SHA `a9ba2dad14ed9bc72179ee709e7712dd9ff50449`

### Forward rollback to State A

The rollback supplied the fetched State-B blob SHA and restored the exact State-A bytes with a new forward commit.

- rollback commit: `aeaffd84eaa0af957c319e3c99c3d720c109923c`
- connector call duration exposed for rollback update: `891 ms`
- final readback returned exact State-A bytes
- final SHA-256: `1c0cb81dff110dbc55b55bd4bddc8fecb761c3860f7851d64f981362488b15a3`
- final blob SHA: `a9826e11db433c9ae3180b8590b7720a2d4388f7`
- rollback required no deletion, reset, force push, or history rewrite

## Measured capability

The bounded connector surface successfully performed:

1. deterministic UTF-8 creation;
2. exact content and blob readback;
3. replacement bound to the currently fetched blob SHA;
4. exact replacement readback;
5. forward rollback bound to the replacement blob SHA; and
6. final exact-byte readback.

This is direct evidence for serial, single-path, reversible repository-content mutation on the named branch. It is not evidence for multi-file atomicity, exactly-once execution, conflict safety, least privilege, workflow durability, or independent verification.

## Adoption measurements

### Custom code avoided

For this micro-use, the connector avoided bespoke authentication handling, REST URL construction, Base64 encoding, request serialization, response decoding, and Git blob transport. Estimated custom adapter avoided remains approximately `40–120` lines for a basic implementation.

Not avoided: event schemas, expected-version discipline, idempotency keys, orphan reconciliation, retries, cross-file transactions, independent verification, and ConsumerAck tracking.

### Operator minutes

- operator relay: `0 minutes`
- operator action requested: none
- estimated operator minutes removed for the create/read/update/read/rollback/read sequence plus receipt pointers: `5–10 minutes`

### Credentials and permissions

- direct fact: the connected identity can read and write this repository branch through the wrapper
- credentials required from the operator during this wake: `0`
- hidden or unknown: token type, identity, scopes, installation, expiry, SSO, branch-rule interaction, and audit attribution
- no credential value was exposed

### Durability

- successful writes produced Git commits and content-addressed blobs
- rollback was a durable forward commit restoring prior bytes
- no database transaction, exactly-once guarantee, multi-path atomicity, durable timer, lease recovery, or automatic compensation was established

### Observability

Exposed:

- create/update commit SHAs;
- update result blob SHAs;
- fetch content and blob SHAs;
- connector-level call durations for writes;
- structured error fields when errors occur.

Not exposed:

- HTTP status and headers;
- request ID;
- API-version response header;
- rate-limit state;
- ETag;
- retry count;
- token identity;
- audit-log event;
- server-side timing.

### Portability

- conceptual portability: medium-high within GitHub REST-compatible implementations
- wrapper portability: medium-low because action names, hidden authentication, return shapes, and omitted headers are carrier-specific
- forge portability: unproven outside GitHub

### Failure behavior

- no failure was intentionally triggered in phase 2
- all serial operations succeeded and returned consistent exact-byte/blob evidence
- stale expected SHA, duplicate create, permission denial, missing path, concurrent writer, and quota behavior remain untested

### Direct cost and quota evidence

- paid call initiated: none
- incremental monetary charge observed: `$0`
- operator-provided credential interaction: none
- exact plan allocation, connector billing, request budget, and remaining quota: unknown

## Strongest objection

This success can still be a privileged happy-path wrapper demonstration. Hidden credentials, scopes, headers, retries, and audit attribution prevent proof of least privilege or portable operational control. Separate event and `CURRENT` commits remain non-atomic and can diverge.

## Strongest falsifier

Phase 3 should attempt a quarantined stale-SHA update after an intervening valid update. The candidate must be gated or rejected if the stale update silently overwrites newer bytes, targets the wrong branch/path, returns an ambiguous success, or cannot expose enough error detail to distinguish conflict from authentication, quota, or transport failure.

## Next phase

Run one harmless connector-variance and failure probe on a new quarantined specimen:

1. create and read State A;
2. validly advance to State B;
3. attempt State C with the now-stale State-A blob SHA;
4. require rejection and unchanged State-B readback;
5. restore State A by a valid forward update;
6. record the connector error class and all metadata actually exposed.

## Honest flaw

The SHA-256 and Git blob SHA recomputations were performed over the UTF-8 strings returned by the connector, not raw HTTP bodies. Same-provider structural review has binding weight zero. Phase 2 does not establish stale-writer rejection, permission boundaries, quota behavior, cross-file atomicity, independent verification, or consumer acceptance.

---
schema_id: hfo.gen133.architecture.electronic_institution.v0_1
claim_status: proposed
valid_time_utc: 2026-07-30T05:37:26Z
transaction_time_utc: SEE_GIT_COMMIT_METADATA
world_effects_proven: false
---

# Gen133 electronic institution — smallest durable spine

## Authority and projections

```text
Git exact bytes
  ├─ validated ingest ─→ XTDB bitemporal read model
  └─ admitted WorkItem ─→ actor Durable Object ─→ OPA decision
                                                └─ allow ─→ durable Workflow
                                                              └─ candidate Git receipt
                                                                    └─ held-out verifier
                                                                          └─ ConsumerAck
                                                                                └─ Arweave manifest
                                                                                      └─ optional ArNS pointer
```

Git is the authority. Every WorkItem, charter, policy bundle, candidate, and
receipt is addressed as `repo@commit:path#blob` plus a payload digest. XTDB,
Durable Objects, Workflows, Slack, Arweave gateways, and ArNS are projections,
execution infrastructure, or navigation. None can silently outrank the Git
bytes that authorized an effect.

## WIP=1 virtual actor

The first pilot has one institution and one active WorkItem:

- One SQLite-backed `InstitutionDO` serializes a named actor's inbox cursor,
  lease/CAS state, idempotency keys, and persisted due-event priority queue.
- OPA is the policy decision point; the Durable Object and Workflow are the
  enforcement points. Undefined, unhealthy, stale, or digest-mismatched policy
  means `HOLD`.
- A Workflow starts only after explicit admission. Its instance ID is derived
  deterministically from the exact WorkItem pointer, actor, action version, and
  effect class.
- External handlers are idempotent because durable retries do not make external
  effects exactly once.
- A distinct verifier reads the exact candidate and sealed fixtures. It returns
  `PASS`, `FAIL`, or `ABSTAIN`; it cannot edit the candidate.
- A separate ConsumerAck is required before closure.

State machine:

```text
PROPOSED → ADMITTED → LEASED → RUNNING → CANDIDATE
         → VERIFIED → CONSUMED → EXTERNALIZED
```

Any digest mismatch, stale temporal basis, expired lease, policy mismatch,
missing distinct verifier, missing ConsumerAck, or unknown external effect
transitions to `HOLD/ANDON`.

## Bitemporal world state

XTDB is a rebuildable query layer, not a second source of truth. The minimum
record families are:

- `actor_state`
- `work_item`
- `lease`
- `policy_decision`
- `run_observation`
- `verification_result`
- `consumer_ack`

Every record carries:

- `valid_time`: when the fact is true in the modeled world;
- `transaction_time`: when the system learned or recorded it;
- `source_repo`, `source_commit`, `source_path`, `source_blob`;
- `payload_sha256`;
- `claim_status`, `remaining_risk`, `honest_flaw`.

Queries used for receipts must record XTDB `SNAPSHOT_TOKEN` and `CLOCK_TIME`;
cross-connection read-after-write must use the returned transaction token.

## OPA fail-closed contract

An action is admitted only when all of these are true:

1. OPA is healthy and ready.
2. The active bundle revision/digest equals the Git-bound expected value.
3. The decision is defined and explicitly `allow`.
4. The caller records decision ID, bundle revision/digest, sanitized input
   hash, result, and enforcement outcome.

OPA decides; the caller enforces. The policy source, tests, and expected bundle
digest live in Git. Signature verification is configured with a public key
distributed outside the bundle it verifies.

## Stigmergy event contract

A pheromone counts only after this lifecycle:

```text
Delta → Git readback → distinct review → Slack projection
      → ProjectionReceipt back-binding → ConsumerAck
```

Slack messages never become authority. The projection contains only the exact
Git pointer, bounded status, falsifier, and one next safe action. A scheduled or
active actor without a fresh receipt is not green.

## Deployment status

This document is an architecture candidate. No XTDB node, Durable Object, OPA
bundle, Workflow, held-out runtime, ConsumerAck, Arweave upload, or ArNS record
is established by this file.

## Official references

- XTDB time model: <https://docs.xtdb.com/about/time-in-xtdb.html>
- XTDB transactions and basis tokens: <https://docs.xtdb.com/about/txs-in-xtdb.html>
- Cloudflare Durable Object SQLite storage: <https://developers.cloudflare.com/durable-objects/api/sqlite-storage-api/>
- Cloudflare Durable Object alarms: <https://developers.cloudflare.com/durable-objects/api/alarms/>
- Cloudflare Workflow rules: <https://developers.cloudflare.com/workflows/build/rules-of-workflows/>
- OPA deployment model: <https://www.openpolicyagent.org/docs/deploy>
- OPA bundles: <https://www.openpolicyagent.org/docs/management-bundles>
- Arweave path manifests: <https://docs.ar.io/build/upload/manifests>
- ArNS model: <https://docs.ar.io/learn/arns/>

## Honest flaw

The component boundaries are source-backed, but none is deployed or
independently exercised here. Platform availability, limits, cost, recovery,
and operator-minute relief remain unproven.

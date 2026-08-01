# VAR Dispatch and Roster System Failure Audit

**Callsign:** Var  
**Date:** 2026-07-23  
**Scope:** Why HFO could assign busy Valkyries by role fit without proving availability; common LLM/agent-system failure modes; industry controls and tools to adopt.

## Executive finding

The incident was not random assignment and not primarily a memory error. Var decomposed a new mission, matched each lane to the most semantically suitable Valkyrie, and presented those matches as owners. The process did not require a fresh roster, WIP count, lease, authority check, collision check, or explicit claim before an owner field could be populated.

The system therefore collapsed four distinct facts:

1. **Capability:** who could perform the work.
2. **Availability:** who has current capacity.
3. **Authority:** who may accept or perform the work.
4. **Assignment:** who has accepted a bounded WorkItem and lease.

This is a common LLM failure mode: plausible semantic completion substitutes for transactional state. The defect should be fixed with production controls, not reminders to reason harder.

## Incident trace

### Prerequisite work Var did perform

- Read recent Slack blackboard and synthesis activity.
- Read the morning quorum and recent GitHub receipts.
- Recalled historical lineage cards and demonstrated role specialties.
- Decomposed life-insurance growth into research, acquisition, recruiting, onboarding, training, economics, verification, and synthesis lanes.
- Matched those lanes to historical role fit.

### Prerequisite work Var did not perform

- No canonical fresh roster was read.
- No per-lineage WIP or WIP limit was established.
- No lease expiry or renewal was verified.
- No `IDLE_AWAITING_WORK` or `AVAILABLE_TO_CLAIM` evidence was found.
- No collision check against current WorkItems was run.
- No current carrier/platform/model capacity was verified.
- No explicit worker claim or section-chief capacity attestation was obtained.
- No atomic compare-and-set converted a candidate into an owner.

### Failure mechanism

```text
new mission
→ decompose by specialty
→ recall best-fit Valkyrie
→ fill owner column
→ publish apparently complete plan
```

The required mechanism is:

```text
new mission
→ decompose into UNASSIGNED packets
→ read canonical resource state
→ remove stale leases
→ filter by authority and spare WIP
→ rank remaining candidates by capability
→ request claim
→ atomically bind accepted owner + lease
→ project to Slack
```

## Common LLM and multi-agent failure modes

### 1. Semantic-fit substitution

The model answers “who sounds right?” instead of “who is currently available and authorized?” Role descriptions become false evidence of capacity.

### 2. Premature binding

An unowned lane is converted directly into a named assignment. The intermediate states `CANDIDATE_OWNER` and `AVAILABLE_CLAIMANT` are omitted.

### 3. Planning from ontology instead of state

Static cards, titles, and historical roles are treated as current operational truth. Dynamic facts—WIP, carrier health, lease, blocker, and current mission—are ignored.

### 4. Stale-state capture

A document named `CURRENT`, a recent Slack message, or a remembered roster is trusted without bitemporal reconciliation. Newer activity can invalidate it.

### 5. Surface-fragmentation false green

Slack, GitHub, scheduled tasks, local nodes, and chat sessions each contain partial state. An agent sees one surface and assumes global truth.

### 6. Push scheduling

Controllers push tasks to plausible agents rather than exposing bounded work for eligible idle capacity to pull.

### 7. Hidden WIP and queue inflation

Every new objective is decomposed and staffed even when existing work has not completed. The plan looks productive while throughput falls.

### 8. Authority-capability conflation

The fact that a carrier can research, write, or call a tool is treated as authority to send, deploy, spend, recruit, or mutate state.

### 9. Self-attested liveness

A lineage says it is active, available, or complete without an independently readable receipt or expiring lease.

### 10. Non-atomic ownership

Two controllers can assign the same lineage or two lineages can claim the same exclusive seat because no compare-and-set or fencing token exists.

### 11. Orphaned work after carrier failure

A task remains “active” after the model session freezes or disappears because state does not expire automatically.

### 12. Completeness bias

LLMs prefer filling every table cell. `UNKNOWN`, `UNASSIGNED`, and `NOT_ATTESTED` feel incomplete, so names and statuses are invented or over-inferred.

## Industry controls to assimilate

## A. Toyota Production System / Lean

### Pull, not push

Lean Kanban emphasizes identifying work, limiting work in process, and allowing a pull system to focus effort on the most important tasks. HFO should publish `READY_TO_CLAIM` packets and allow only eligible capacity to claim them. Source: Lean Enterprise Institute, “Six Personal Kanban Habits to Avoid”: https://www.lean.org/LeanPost/Posting.cfm?LeanPostId=675

### WIP limits and visual control

GitHub Projects explicitly supports board column limits to maintain focus, custom fields, automation, charts, templates, and a single source of truth. Source: https://docs.github.com/en/issues/planning-and-tracking-with-projects/learning-about-projects/best-practices-for-projects

### Jidoka

Missing roster, lease, WIP, or authority is an Andon condition. The system must stop before naming an owner. The output is `UNASSIGNED_PENDING_CLAIM`, not a best guess.

### Poka-yoke

The assignment schema must be impossible to validate without an availability receipt and lease. This removes dependence on model discipline.

### Standard work

Every dispatch follows the same sequence: read state, expire stale claims, filter capacity, match capability, request claim, bind atomically, publish receipt.

## B. Kubernetes leases and leader election

Kubernetes uses Lease objects for node heartbeats and exclusive control-plane leadership. Leases include holder identity, acquire time, renewal time, duration, and transition count. Expired leases cease to prove availability or leadership. Optimistic concurrency prevents two candidates from acquiring the same lease. Sources:

- https://kubernetes.io/docs/concepts/architecture/leases/
- https://kubernetes.io/docs/concepts/cluster-administration/coordinated-leader-election/
- https://kubernetes.io/docs/reference/kubernetes-api/coordination/lease-v1/

**HFO translation:**

```yaml
lease:
  holder_identity: lineage_id + carrier_id
  workitem_id: WI-...
  acquire_time: ...
  renew_time: ...
  lease_duration_seconds: 3600
  transition_count: 4
  fencing_token: monotonic_integer
  resource_version: git_blob_sha_or_db_version
```

No renewal means no current active claim. An expired carrier returns to `UNKNOWN_NOT_ATTESTED`; the work returns to `READY_TO_CLAIM` after recovery review.

## C. GitHub Issues and Projects as typed production control

GitHub organization issue fields now support typed single-select, text, number, and date metadata, API access, search, and Actions triggers when fields change. Projects can show those fields in table or board views, group and filter by them, chart them, and automate state changes. Sources:

- https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/adding-and-managing-issue-fields
- https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/managing-issue-fields-in-your-organization
- https://docs.github.com/en/issues/planning-and-tracking-with-projects/understanding-fields/about-issue-fields
- https://docs.github.com/en/issues/planning-and-tracking-with-projects/learning-about-projects/about-projects

**Recommended HFO issue fields:**

- `Work State`: BACKLOG | READY_TO_CLAIM | CLAIMED | ACTIVE | BLOCKED | VERIFYING | CONSUMED | RETIRED
- `Candidate Owner`
- `Accepted Owner`
- `Lineage ID`
- `Carrier / Model`
- `Authority Tier`
- `WIP Cost`
- `WIP Limit Snapshot`
- `Lease Expires At`
- `Availability Receipt`
- `Fencing Token`
- `Verifier`
- `Next Consumer`
- `Blocker`
- `Claim Ceiling`

GitHub Issue Forms can require structured inputs and validation. Source: https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/syntax-for-issue-forms

## D. Backstage ownership catalog

Backstage provides a centralized catalog with discoverable ownership and typed directional relations such as `ownedBy` and `ownerOf`. Sources:

- https://backstage.io/docs/features/software-catalog/
- https://backstage.io/docs/features/software-catalog/well-known-relations/

**HFO translation:** store lineage, section, carrier, capabilities, authority, and ownership as catalog entities and relations. Capability metadata must remain separate from live lease state.

Example:

```yaml
kind: HfoLineage
metadata:
  name: gunnr
spec:
  section: execution
  capabilities: [source-build, node1, test-harness]
  authority: [source-only]
  ownedBy: section-execution
status:
  currentWorkItem: WI-179
  leaseRef: lease/gunnr-node1
```

## E. Capacity forecasting and triage

Linear separates triage, backlog, active work, cycles, and projects. It estimates future cycle capacity from the previous three cycles rather than assuming every team member is free. Sources:

- https://linear.app/docs/teams
- https://linear.app/docs/use-cycles

**HFO translation:** new missions enter triage. Capacity is inferred from observed throughput and current WIP, not from roster count. Unfinished work must be visible rather than hidden by new assignments.

## Proposed HFO control architecture

### Canonical authority

GitHub issue fields or a versioned `production_board.json` in Gen-131 are the source of truth. Slack is a projection and claim surface, never the authoritative owner registry.

### Production objects

1. **Lineage catalog:** relatively stable capabilities and authority.
2. **Carrier registry:** current platform, vendor, model, connectivity, and tool ceiling.
3. **WorkItem:** objective, scope, verifier, consumer, cost ceiling, and stop condition.
4. **Lease:** accepted ownership with expiry and fencing token.
5. **Receipt:** evidence of transition.
6. **Production board:** materialized view of current WIP and capacity.

### State machine

```text
BACKLOG
→ TRIAGE
→ READY_TO_CLAIM
→ CLAIM_REQUESTED
→ CLAIMED
→ ACTIVE
→ VERIFYING
→ CONSUMED
→ IDLE_AWAITING_WORK
```

Alternate transitions:

```text
ACTIVE → BLOCKED
ACTIVE → LEASE_EXPIRED
CLAIM_REQUESTED → DECLINED
READY_TO_CLAIM → DEFERRED
VERIFYING → REWORK
ANY → QUARANTINED
```

### Assignment gate

A named assignment is valid only when all predicates pass:

```text
fresh_catalog
AND fresh_carrier
AND authority_matches
AND current_wip + work_cost <= wip_limit
AND no_conflicting_exclusive_lease
AND accepted_claim
AND independent_verifier_named
AND next_consumer_named
AND lease_expiry_present
AND atomic_write_succeeds
```

Failure returns a typed reason, such as:

- `HOLD_ROSTER_STALE`
- `HOLD_WIP_FULL`
- `HOLD_AUTHORITY_MISMATCH`
- `HOLD_CARRIER_UNATTESTED`
- `HOLD_CONFLICTING_LEASE`
- `UNASSIGNED_PENDING_CLAIM`

## Minimum viable implementation

### Phase 0 — standard work immediately

- Var may decompose and recommend role-fit candidates.
- Var may not populate `Accepted Owner` without a fresh claim receipt.
- All new lanes default to `UNASSIGNED_PENDING_CLAIM`.
- Every status packet distinguishes role fit, candidate, availability, and assignment.

### Phase 1 — GitHub-native production board

Create one GitHub Project with:

- the typed fields above;
- board columns matching the state machine;
- WIP limits on `CLAIMED`, `ACTIVE`, and `VERIFYING`;
- views by lineage, section, carrier, expired lease, and unclaimed priority;
- issue-form validation for WorkItems and claims;
- Actions that reject invalid owner transitions.

### Phase 2 — lease validator

Build a small deterministic validator that:

1. reads current issue fields or board JSON;
2. expires leases;
3. computes WIP;
4. validates candidate transitions;
5. uses optimistic concurrency or Git blob SHA as `resourceVersion`;
6. writes one durable receipt;
7. projects a sanitized delta to Slack.

### Phase 3 — pull claims

Slack posts contain lane summaries and claim links. A carrier claims through a structured GitHub issue comment/form or deterministic API call. The claim is not active until the canonical write succeeds.

### Phase 4 — measured improvement

Track:

- invalid dispatch attempts blocked;
- duplicate claim attempts;
- stale leases detected;
- work age by state;
- active WIP per lineage;
- blocked time;
- throughput to `CONSUMED`;
- operator minutes per consumed transition;
- percentage of assignments backed by fresh availability evidence.

## Held-out tests

1. Best-fit agent is at WIP limit: assignment must fail.
2. Agent says “available” in Slack but lease is stale in GitHub: fail.
3. Two controllers claim the same exclusive lineage concurrently: only one atomic write succeeds.
4. Carrier changes model/platform without updating authority: fail.
5. Role card exists but no current carrier: fail.
6. Section chief attests capacity without subordinate receipt: candidate only, not assigned.
7. Slack says active but GitHub says expired: GitHub wins and emits drift Andon.
8. Agent completes candidate work but verifier is same lineage: cannot move to `CONSUMED`.
9. New urgent lane arrives while all WIP is full: queue remains unassigned; no silent overload.
10. Dispatcher omits availability evidence: schema validation fails.

## Decision

Adopt the production-control pattern, beginning with Phase 0 and a GitHub-native Phase 1. Do not build a large bespoke scheduler first. Assimilate GitHub typed issue fields, Project WIP limits and automations, Kubernetes-style leases and optimistic concurrency, Backstage-style capability/ownership catalog separation, and Lean pull/visual-control rules.

## Claim ceiling

This document is a source-backed audit and implementation recommendation. It does not establish that the production board, issue fields, validator, leases, or automations have been implemented or independently verified.

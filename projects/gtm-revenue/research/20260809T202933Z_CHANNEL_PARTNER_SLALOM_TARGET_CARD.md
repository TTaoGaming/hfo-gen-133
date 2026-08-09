# S08 TARGET CARD — SLALOM

```yaml
schema_id: hfo.gen133.gtm.target_card.v1
task_id_expected: 6a526109ba348191b5f23ad3172ad568
seat: S08_GTM_TARGET_AND_PAIN_SCOUT
wip: 1
target: Slalom
species: CHANNEL_PARTNER
vertical: enterprise AI consulting / agentic workflow delivery
route: RELATIONSHIP_ONLY
privacy: PUBLIC_SAFE_SYNTHETIC_ONLY
world_effect_ceiling: T0_PREP_RESEARCH_GIT
verifier: S04_HRIST_STRUCTURAL_PREFLIGHT
next_consumer: S07
consumer_workitem: S07_SLALOM_AGENT_AUTHORITY_PROOF_GATE_V1
expiry_utc: 2026-08-14T14:08:00Z
evidence_digest_sha256: 5dbd9612b75b9ebba02490757cca7d913f15ec28253431f75a78560f9b2353b4
```

## Current signal

Slalom is a live agentic-AI delivery channel, not merely a strategy consultancy. On **2026-03-24**, its official agentic-AI guidance framed enterprise agent scaling as an authority problem and explicitly proposed **proof-gated autonomy**, hard permission limits, escalation/revocation, auditability, and measurable KPIs including permission cycle time, revocation cycle time, audit coverage, escalation load, exception cost, and proof-to-permission ratio. Slalom's current AI-services page, verified **2026-08-09**, says it designs and builds agent-driven workflows and also operates agentic workflows in production as a managed service with monitoring, governance, continuous improvement, and defined accountability for outcomes. On **2026-04-10**, Slalom and AMD announced a collaboration to move enterprise AI beyond experiments into business workflows with responsible-AI practices and measurable outcomes.

Primary official sources:
- 2026-03-24 — https://www.slalom.com/us/en/insights/technology-trends-agentic-ai-outcome-engines
- current, verified 2026-08-09 — https://www.slalom.com/us/en/services/artificial-intelligence
- 2026-04-10 — https://www.slalom.com/us/en/who-we-are/newsroom/slalom-and-amd-strategic-collaboration

## Persona / bridge

**Best buyer/user persona:** Slalom AI delivery / managed-services leadership responsible for production agentic workflows, governance, permission design, monitoring, and measurable client outcomes.

**Named public bridge:** **Rick Koppin, Managing Director at Slalom**, named in Slalom's 2026-04-10 AMD collaboration announcement. No procurement authority, subcontracting authority, accessibility, or interest is inferred.

## Expensive-pain hypothesis

**Hypothesis:** while Slalom scales agentic engagements across clients, delivery teams *may* spend material consultant + client-control time converting high-level authority designs into exact, testable release evidence for each agent/workflow revision: which principal can perform which action, under what conditions, what proof expands authority, what event revokes it, what must escalate, and whether that exact revision remains inside the agreed permission envelope.

**Primary measurable value metric:** consultant + client reviewer hours per accepted agent/workflow revision.  
**Secondary metrics:** permission cycle time; revocation cycle time; audit coverage rate; escalation load; exception cost — all metrics Slalom itself names as relevant to agentic authority systems.

### Evidence for

- Slalom directly states that enterprise agent scaling creates an authority/permission problem and recommends proof-gated expansion, hard limits, escalation, revocation, and auditable decisions.
- Slalom explicitly names permission cycle time, revocation cycle time, audit coverage, escalation load, exception cost, and proof-to-permission ratio as operating KPIs.
- Slalom says it operates agentic workflows in production as a managed service, creating a recurring need to maintain, tune, monitor, govern, and evidence changes over time.

### Evidence against

- These same sources show Slalom already understands and sells this problem; this is evidence of capability, not evidence of a gap.
- No official source found in this pass establishes excess reviewer hours, permission-control failures, audit incidents, stalled releases, margin leakage, or unmet demand for an outside specialist.
- Slalom may already implement these controls natively inside client IAM, cloud, workflow, or AI-platform stacks, leaving little specialist whitespace.

## 2-minute utility gift

**Agent Authority Proof-Gate Card — Principal × Action × Limit × Evidence × Escalation × Revocation.**

For one tiny synthetic before/after agent revision, bind the exact principal, allowed/denied actions, contextual limits, held-out evidence required to expand authority, human-escalation conditions, revocation trigger, audit-trail completeness, and rollback revision; output `PROMOTE | HOLD | REJECT` while showing only changed authority edges or missing proof.

## Deeper proof artifact

**Synthetic Agent Authority Promotion Harness:** fake enterprise workflow + mocked tools; OPA/Rego as an independent deterministic authorization oracle; held-out behavior/eval fixtures; principal and action matrices; approval/escalation thresholds; revocation tests; trace evidence; exact revision/policy/eval digests; negative controls for wrong principal, privilege widening, stale policy, missing proof, missing escalation, incomplete audit trail, failed revocation, and rollback mismatch. No Slalom systems, client data, paid model calls, deployment, compliance claim, security-outcome claim, or savings claim.

## Route / falsifier / flaw

**Route:** `RELATIONSHIP_ONLY`. This is a channel/subcontracting hypothesis, not evidence that Slalom is seeking external specialist capacity.

**Strongest falsifier:** kill the wedge if Slalom already has a low-overhead standard mechanism that binds exact agent/workflow revisions to principal/action authority, proof thresholds, escalation, revocation, audit evidence, approval, and rollback across its managed-agent engagements — or if its delivery model does not admit narrow specialist/subcontractor work.

**Honest flaw:** **high redundancy risk.** Slalom's public 2026 position is already strikingly close to the operator's authority/release-gate toolbox. A generic OPA/Rego or "AI governance" demo would mostly restate Slalom's own thesis. S07 earns fitness only if it makes the missing seam concrete: a portable, revision-bound proof-to-permission contract that is demonstrably useful inside heterogeneous client stacks.

## Evidence digest preimage

```text
target=Slalom
species=CHANNEL_PARTNER
source1=2026-03-24|https://www.slalom.com/us/en/insights/technology-trends-agentic-ai-outcome-engines|agentic authority proof-gated autonomy permission cycle time revocation cycle time audit coverage escalation load exception cost
source2=current_verified_2026-08-09|https://www.slalom.com/us/en/services/artificial-intelligence|agentic AI consulting production managed service monitoring governance continuous improvement
source3=2026-04-10|https://www.slalom.com/us/en/who-we-are/newsroom/slalom-and-amd-strategic-collaboration|move beyond experimentation embed generative AI business workflows responsible AI measurable outcomes
bridge=Rick Koppin|Managing Director at Slalom|source3
consumer=S07_SLALOM_AGENT_AUTHORITY_PROOF_GATE_V1
```

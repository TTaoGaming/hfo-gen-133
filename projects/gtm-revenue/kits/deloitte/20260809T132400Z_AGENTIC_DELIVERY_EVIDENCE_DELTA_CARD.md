# Agentic Delivery Evidence Delta Card

**Recipient:** Deloitte Agentic AI / AI Engineering delivery leadership  
**Use:** public-safe synthetic review aid for one agent/workflow revision  
**Decision:** `PROMOTE | HOLD | REJECT`  
**Boundary:** not a claim about Deloitte's internal process, client systems, compliance status, release speed, or outcomes.

## Plausible problem

A small agent revision can change more than code: held-out quality, principal identity, allowed tool actions, data/provenance, human escalation, model/tool routing, cost/latency, traces, or rollback.

**Hypothesis only:** across heterogeneous client/provider stacks, review effort may rise when those deltas are scattered across tests, policy, traces, approvals, and deployment notes instead of bound to one promotion decision.

## WHY_THIS_MAY_MATTER

Deloitte publicly describes Agentic AI services spanning design/build/deploy, agent development, multi-agent systems, governance/trust implementation, Agent Ops, managed services, and governance/trust monitoring. Its April 22, 2026 Google Cloud announcement says its agentic transformation practice spans implementation, governance, and adoption; has a growing library of 1,000+ pre-built industry-specific AI agents; connects agents across providers through A2A; and uses forward deployed engineers for client use cases. Deloitte's AI Risk Management and Governance page also describes lifecycle checkpoints, HITL/access/monitoring/fallback/kill-switch controls, performance validation, and audit-ready evidence.

Those are source-backed facts about Deloitte's stated service surface. They do **not** prove a Deloitte deficiency. This card asks a narrower question: can one revision be reviewed from its material evidence deltas without re-reading the whole system?

## HOW_TO_USE_IN_2_MINUTES

1. Bind the exact baseline and candidate revision.
2. Fill only rows where something changed; mark the rest `SAME`.
3. Attach one evidence pointer for each changed row or mark `MISSING`.
4. Apply the decision rule. If the decision cannot be explained from this page, return `HOLD`.

## Revision binding

| Field | Value |
|---|---|
| Workload / use case | `________________` |
| Baseline revision / digest | `________________` |
| Candidate revision / digest | `________________` |
| Eval-set revision / digest | `________________` |
| Policy / authority revision | `________________` |
| Trace / run-set pointer | `________________` |
| Rollback target | `________________` |
| Reviewer / date | `________________` |

## Material delta scan

| Surface | Ask only what changed | Evidence | Gate |
|---|---|---|---|
| **Held-out quality** | Any agreed task, edge case, or failure class regress? Repeated runs where stochasticity matters? | `____` | `SAME/PASS/HOLD/REJECT` |
| **Principal / identity** | Acting principal, service identity, delegation path, or credential boundary changed? | `____` | `SAME/PASS/HOLD/REJECT` |
| **Tool / action authority** | Any tool, operation, write scope, destination, or irreversible action added/widened? | `____` | `SAME/PASS/HOLD/REJECT` |
| **Data / provenance** | Any source, retrieval index, dataset, retention boundary, or provenance requirement changed? | `____` | `SAME/PASS/HOLD/REJECT` |
| **HITL / escalation** | Approval threshold, exception route, timeout, or fallback ownership changed? | `____` | `SAME/PASS/HOLD/REJECT` |
| **Model / tool routing** | Provider, model class, fallback order, or tool-selection logic changed? | `____` | `SAME/PASS/HOLD/REJECT` |
| **Cost / latency** | Measured unit cost, token/tool use, timeout, or latency outside the agreed envelope? | `____` | `SAME/PASS/HOLD/REJECT` |
| **Trace evidence** | Can reviewer reconstruct principal → decision → tool → result → approval/escalation for the changed path? | `____` | `SAME/PASS/HOLD/REJECT` |
| **Rollback** | Is the rollback target exact, available, and compatible with the changed state/data contract? | `____` | `SAME/PASS/HOLD/REJECT` |

## Seven held-out negative controls

Use synthetic or authorized fixtures only.

- **Authority widening:** candidate gains one write-capable action absent from baseline.
- **Principal substitution:** same task arrives under a different principal/delegation path.
- **Provenance loss:** answer remains plausible but required source evidence disappears.
- **Hidden regression:** aggregate score is stable while one agreed critical slice regresses.
- **Fallback drift:** preferred model/tool fails and fallback violates cost, latency, or authority expectations.
- **Trace break:** action succeeds but a required decision/tool/approval edge is missing.
- **Rollback drift:** rollback artifact exists but no longer matches the candidate's data/tool contract.

Mark each `CAUGHT | NOT_CAUGHT | NOT_RUN`. `NOT_RUN` is missing evidence, not a pass.

## Starter promotion rule

This is a review starter, **not Deloitte policy** and not legal/compliance advice.

- `PROMOTE`: every material changed row has current evidence, required negative controls are `CAUGHT`, and rollback is bound.
- `HOLD`: candidate may be acceptable but required evidence, approval, measurement, negative control, or rollback binding is missing/stale.
- `REJECT`: candidate violates a predeclared redline such as unauthorized action scope, disallowed data use, unacceptable held-out regression, required-HITL bypass, or known-bad rollback.

**Smallest missing-evidence reason:** `________________________________________`  
**Decision:** `PROMOTE | HOLD | REJECT`

## Source-backed facts

- **April 22, 2026:** Deloitte announced an end-to-end Google Cloud Agentic Transformation Practice spanning strategy/process redesign through implementation, governance, and adoption; it also reported 1,000+ pre-built industry-specific AI agents, cross-provider A2A connectivity, and FDE support for client use cases.
- **May 29, 2026:** Deloitte and Google Cloud published a framework for scaling Agentic AI beyond experimentation toward business value.
- **Verified August 9, 2026:** Deloitte's Agentic AI page lists design/build/deploy, agent development, multi-agent systems/frameworks, governance/trust implementation, Agent Ops, managed services, and governance/trust monitoring.
- **Verified August 9, 2026:** Deloitte US AI Risk Management and Governance describes lifecycle checkpoints, HITL/access/monitoring/fallback/kill-switch controls, performance validation, monitoring/response, third-party risk, and audit-ready evidence.

## Hypothesis ceiling

A revision-bound evidence-delta view **may** reduce re-reading and coordination effort if the underlying evidence otherwise lives across several delivery surfaces.

No cited source establishes Deloitte's reviewer hours, release delays, failed controls, incidents, margin leakage, backlog, or demand for an external specialist.

## Evidence links

1. https://www.deloitte.com/global/en/about/press-room/ai-transformation-gemini-enterprise-google-cloud.html
2. https://www.deloitte.com/global/en/alliances/google/perspectives/scaling-agentic-ai-business-value.html
3. https://www.deloitte.com/global/en/what-we-do/capabilities/agentic-ai.html
4. https://www.deloitte.com/us/en/services/consulting/services/ai-risk-governance-program.html

## Assumptions

- One review can bind an exact baseline and candidate revision.
- Authoritative eval, identity, policy, observability, approval, cost/latency, and rollback evidence already exists elsewhere; this card does not replace those systems.
- Client-specific thresholds/redlines are set by responsible delivery/control owners.
- Synthetic examples are not production evidence.

## Falsifier

Discard this wedge if Deloitte already has a low-overhead revision-bound mechanism surfacing the same material deltas across acceptance, held-out quality, principal/tool authority, provenance, HITL, cost/latency, traces, approval, and rollback across provider stacks. Also discard it if Deloitte's partner/subcontractor model does not admit narrow specialist contributions of this type.

## Optional operator-reviewed outreach note — NO SEND

I noticed Deloitte's current Agentic AI material spans production delivery, governance, Agent Ops, and cross-provider integration. I made a one-page synthetic "evidence delta" card for reviewing what materially changed between two agent revisions—evals, identity/authority, provenance, HITL, routing/cost, traces, and rollback. It is not a claim that Deloitte lacks this capability; the useful question is whether this view removes any review friction in a real delivery handoff. If it duplicates your existing process, that is the falsifier.

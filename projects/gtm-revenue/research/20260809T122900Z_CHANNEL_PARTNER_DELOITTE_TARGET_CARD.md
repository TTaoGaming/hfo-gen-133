# S08 GTM Target Card — Deloitte

```yaml
schema: hfo.gen133.gtm_target_card.v1
task_id: 6a526109ba348191b5f23ad3172ad568
wip: 1
target: Deloitte
species: CHANNEL_PARTNER
vertical: enterprise_agentic_ai_consulting_and_delivery
route: RELATIONSHIP_ONLY
privacy: PUBLIC_SAFE_SYNTHETIC_ONLY
effect_ceiling: T0_PREP_RESEARCH_GIT
verifier: S04
next_consumer: S07
consumer_workitem: S07_DELOITTE_AGENTIC_DELIVERY_EVIDENCE_DELTA_CARD_V1
expiry_utc: 2026-08-14T14:08:00Z
evidence_digest_sha256: ee7f161529b12fc17025b196cb24f32c38f10e971b76a52a00bbff672e0c11df
```

## Current business signal

Deloitte is actively selling and expanding end-to-end Agentic AI delivery rather than only advisory work. On 2026-04-22 it announced a dedicated Google Cloud Agentic Transformation Practice spanning strategy/process redesign through implementation, governance and adoption; the announcement says Deloitte has a library of more than 1,000 pre-built industry-specific AI agents and is connecting agents across providers with Google's A2A protocol. On 2026-05-29 Deloitte and Google Cloud published a scaling framework aimed at moving enterprise Agentic AI beyond experimentation into measurable business value. Deloitte's current Agentic AI service surface, verified 2026-08-09, explicitly includes design/build/deploy, AI-agent development, multi-agent systems/frameworks, governance and trust implementation, Agent Ops, managed services, and governance/trust monitoring.

Primary sources:
- 2026-04-22 — https://www.deloitte.com/global/en/about/press-room/ai-transformation-gemini-enterprise-google-cloud.html
- 2026-05-29 — https://www.deloitte.com/global/en/alliances/google/perspectives/scaling-agentic-ai-business-value.html
- verified current 2026-08-09 — https://www.deloitte.com/global/en/what-we-do/capabilities/agentic-ai.html
- verified current 2026-08-09 — https://www.deloitte.com/us/en/services/consulting/services/ai-risk-governance-program.html

## Buyer / user persona and bridge

Best persona: Deloitte Agentic AI / AI Engineering delivery leadership responsible for moving client agents from prototype to governed production while preserving value, security, reliability and repeatability across heterogeneous client stacks.

Named public bridge: **Gopal Srinivasan — Alphabet Google Alliance AI & Data Leader, Deloitte Consulting LLP**, named by Deloitte on the 2026-05-29 Google Cloud Agentic AI scaling paper. This establishes public role relevance only; procurement authority, subcontracting authority, accessibility and interest are not inferred.

## Expensive-pain hypothesis

**Hypothesis, not a claim of current Deloitte pain:** as Deloitte scales agentic delivery across many clients, consultant and client-control teams may consume material engineering/reviewer time per promoted agent or workflow revision proving that the exact revision still satisfies held-out quality, tool/action authority, data/provenance constraints, human escalation, model/tool cost-latency expectations, traceability and rollback readiness across changing provider and client environments.

Primary measurable value metric: **consultant + client reviewer hours per accepted agent/workflow production revision**. Secondary metric: **calendar days from accepted prototype to governed production promotion**.

Evidence for the hypothesis:
- Deloitte explicitly sells moving agents from strategy to production and operating/monitoring them afterward.
- Its Google Cloud practice spans implementation, governance and adoption, and it is integrating a large agent library across providers through A2A.
- Its AI Risk and Governance service explicitly describes lifecycle controls and audit-ready evidence embedded in delivery.

Evidence against the hypothesis:
- Deloitte already has mature Trustworthy AI, governance, Agent Ops, managed-service and AI Engineering capabilities.
- The 1,000+ agent library and dedicated transformation practice are evidence of substantial internal delivery maturity, not a capability gap.
- No cited source establishes slow releases, excess review hours, failed controls, incidents, margin leakage, backlog, or demand for an external specialist.

## Two-minute utility gift

**Agentic Delivery Evidence Delta Card — Eval × Authority × Cost × Audit × Rollback.** For one synthetic before/after agent revision, show only material promotion deltas: held-out eval regression, newly allowed/denied tool actions, principal/identity changes, data/provenance boundary changes, HITL/escalation changes, model/tool cost-latency movement, trace completeness and rollback target. Return `PROMOTE | HOLD | REJECT` with the smallest missing-evidence reason.

## Deeper proof artifact

Build a public-safe synthetic multi-agent delivery-assurance harness shaped like a consulting handoff: fake enterprise data, mocked A2A/MCP-style tools, held-out evals, an independent OPA/Rego-style authorization oracle, principal/permission negative controls, provider-routing and cost fixtures, trace requirements, HITL thresholds, failure injection, exact revision/evidence binding and rollback. No Deloitte systems, Google Cloud tenant, client data, deployment, savings, compliance or security-outcome claims.

## Strongest falsifier

Kill this wedge if Deloitte already has a low-overhead revision-bound mechanism that binds business acceptance, held-out eval quality, principal/tool authority, provenance, HITL, cost/latency, traces, approval and rollback to each promoted client-agent revision across provider stacks. Also kill it if Deloitte's partner/subcontractor model does not admit narrow specialist contributions of this type.

## Honest flaw

Technical adjacency is high but commercial whitespace is unproven and may be small. Deloitte already sells the same broad governance/productionization outcomes, so a generic "agent governance" artifact would be redundant and potentially naïve. S07 earns fitness only if the proof exposes one concrete evidence-binding seam that complements Deloitte's existing delivery stack rather than repackaging it.

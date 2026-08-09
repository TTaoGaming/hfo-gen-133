# S08 GTM Target Card — Zurich Insurance Agentic AI Pilot→Production

```yaml
schema_id: hfo.gen133.gtm.target_card.v1
created_utc: 2026-08-09T07:28:00Z
producer: S08_GTM_TARGET_SCOUT
carrier_task_id: 6a526109ba348191b5f23ad3172ad568
wip: 1
target: Zurich Insurance Group
species: ENTERPRISE_BUYER
vertical: insurance_agentic_ai_production_governance
route: RELATIONSHIP_ONLY
privacy: PUBLIC_SAFE_SYNTHETIC_ONLY
world_effect_ceiling: T0_PREP_RESEARCH_GIT
verifier: S04
next_consumer: S07
consumer_workitem: S07_ZURICH_AGENTIC_PILOT_PROMOTION_EVIDENCE_CARD_V1
expiry_utc: 2026-08-14T14:08:00Z
evidence_digest_sha256: c85d06d516f2e5d75453280eca20a6f032c8eccc2cceab85522bb894e5f7b30f
```

## Target / current signal

Zurich's current **AI at Zurich** page, verified **2026-08-09**, says its AI360 strategy aims to make Zurich an **AI-native insurer**. It reports that the 2025 Agentic AI Hyper Challenge produced **218 prototypes across 17 use cases, with 5 pilots now moving into production**, and says Zurich has more than 50 ongoing startup collaborations. The same page names five Agentic AI principles: secure/private/accountable by design; responsible/explainable/governed AI; context as an asset; discoverability/interoperability; and technology standardization to reduce complexity, cost and risk.

A currently live Zurich/ServiZurich **AI & Process Automation Engineer (Agents, Automation & Digitalisation)** role, verified **2026-08-09**, calls for production-ready automation that is tested, monitored, documented, maintainable and version-controlled, with auditability, human-in-the-loop controls, responsible-AI compliance, CI/CD and governed reuse patterns. Separately, Zurich's **2026-03-24** article on scaling AI says pilots should run in controlled environments with strong governance and human oversight, then only solutions that demonstrate value should be integrated and scaled.

These sources establish active agentic-AI productionization and explicit governance requirements. They do **not** establish a current release bottleneck, excess review cost, control failure, or external budget for this proposed wedge.

## Sources

1. **Zurich — AI at Zurich**, current undated page, **verified 2026-08-09**. https://www.zurich.com/about-us/ai-at-zurich
2. **Zurich — Scaling AI with confidence: the smart approach to unlocking business value**, **2026-03-24**. https://www.zurich.com/commercial-insurance/sustainability-and-insights/commercial-insurance-risk-insights/scaling-ai-with-confidence-the-smart-approach-to-unlocking-business-value
3. **Zurich Careers — AI & Process Automation Engineer (Agents, Automation & Digitalisation)**, current listing, **verified 2026-08-09**. https://www.careers.zurich.com/job/Barcelona-AI-%26-Process-Automation-Engineer-%28Agents%2C-Automation-%26-Digitalisation%29/811422502/

## Best buyer / user persona

Primary user: **AI Engineering / Responsible AI / platform leader responsible for moving agentic pilots into controlled production across underwriting, claims, finance or operations**. Secondary users: business process owners, security/identity engineering, risk/compliance reviewers and operations owners who sign off production promotion.

**Named public bridge:** **Maria Apazoglou — Group Head of AI Engineering & Platforms**, source-backed by Zurich's current AI page. Her title makes her a relevant public context bridge; no procurement authority, accessibility, sponsorship or interest in this specific artifact is inferred.

## Expensive pain hypothesis

**HYPOTHESIS:** as Zurich moves agentic pilots into production, teams may consume material **calendar time plus AI-engineering/control-review hours per promoted agent revision** assembling evidence that the exact candidate still satisfies business-value thresholds, held-out quality, data/privacy constraints, bounded action authority, human escalation, traceability, cost/latency expectations and rollback readiness.

**Measurable value metric:** primary = **calendar days from accepted agentic pilot revision to production promotion**; secondary = **AI-engineering + control-owner reviewer hours per promoted revision**.

### Evidence for

- Zurich explicitly reports **5 agentic pilots now moving into production**, so prototype→production transition is a real current operating surface.
- Zurich's Agentic AI principles explicitly cover accountable action, governance, interoperability and standardization to reduce complexity, cost and risk.
- Zurich's live automation-engineering role requires testing, monitoring, auditability, HITL controls, version control, CI/CD and governed reuse patterns.
- Zurich's 2026 scaling guidance says controlled pilots should be quantified and only value-producing systems integrated and scaled.

### Evidence against

- Zurich already has a Group Responsible AI function, AI Engineering & Platforms leadership, explicit agentic principles and enterprise standardization goals; the proposed seam may already be solved internally.
- The live role is specifically building governed reusable automation patterns, suggesting current investment rather than unmet external demand.
- Zurich's public case studies already describe mature AI deployments and startup collaborations; agent promotion evidence may intentionally remain inside existing platform, risk and CI/CD controls.
- No source found reports slow promotions, failed agent releases, audit findings, incident burden or missing tooling.

## Two-minute utility gift

**Zurich Agentic Pilot→Production Evidence Card — Value × Eval × Data × Authority × HITL × Rollback**

A one-page reviewer card for one synthetic candidate agent revision. It records one quantified business-value criterion, a tiny held-out regression result, data/privacy boundary, permitted actions/principal, mandatory human escalation, trace completeness and known-good rollback target, then returns `PROMOTE | HOLD | REJECT` with explicit missing-evidence reasons.

## Deeper proof artifact

A public-safe synthetic **travel-claims agent promotion harness**, inspired only by Zurich's public Agentic AI claims use case and using fake claimants/documents. Include held-out triage/consistency tests; an independent OPA/Rego-style action-policy oracle; wrong-principal and unauthorized-payout negative controls; privacy/data-boundary checks; prompt/tool misuse tests; human escalation; trace completeness; model/tool cost-latency fixtures; revision-bound evidence; failure injection; and rollback. Report synthetic measurements only; make no claims about Zurich production systems, compliance, savings or security outcomes.

## Route

`RELATIONSHIP_ONLY` — public research/proof preparation only. No outreach, challenge entry, procurement claim, application, send, negotiation or private-data use.

## Strongest falsifier

**Kill this wedge** if Zurich already has a low-overhead, revision-bound promotion mechanism that binds business-value evidence, held-out evals, data/privacy controls, deterministic action authority, HITL, traces, cost/latency, approval and rollback to every agentic production revision — or if the five production-moving pilots are deliberately scoped so that action-level release controls add negligible incremental value.

## S07 consumer contract

`S07_ZURICH_AGENTIC_PILOT_PROMOTION_EVIDENCE_CARD_V1`

S07 should build exactly one two-minute recipient-useful card first. Do not expand into the deeper harness unless the card reveals a concrete evidence seam not already covered by Zurich's published Agentic AI principles and production-governance practices.

## Honest flaw

Zurich is unusually explicit about the exact governance and standardization concerns this artifact addresses. That makes the technical fit strong but the commercial gap uncertain: the evidence proves active agentic-AI productionization, not unmet demand. Fast falsification is more valuable than building a generic governance layer Zurich may already possess.

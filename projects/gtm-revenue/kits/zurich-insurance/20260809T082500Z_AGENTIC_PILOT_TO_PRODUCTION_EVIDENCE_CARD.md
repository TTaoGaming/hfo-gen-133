# Zurich Agentic Pilot→Production Evidence Card

**Public-safe synthetic utility — RELATIONSHIP_ONLY — not a claim about Zurich production controls**

## Plausible problem

Zurich publicly says five Agentic AI pilots are moving into production. When one pilot revision is ready to cross that boundary, evidence for business value, held-out quality, data/privacy, action authority, human escalation, observability and rollback can live in different systems or reviews. **Hypothesis:** one revision-bound evidence card may reduce reviewer ambiguity if those signals are currently fragmented. This card does not assert that Zurich has a release bottleneck or lacks any of these controls.

## WHY_THIS_MAY_MATTER

Source-backed signals make the promotion surface real: Zurich reports five Agentic AI pilots moving into production; its Agentic AI principles emphasize secure/private/accountable actions, governed AI, interoperability and technology standardization; a current Zurich automation-engineering role requires production-ready solutions that are tested, monitored, documented, auditable, maintainable, version-controlled and equipped with appropriate human-in-the-loop controls. Zurich's March 24, 2026 scaling guidance also says pilots should run in controlled environments with strong governance and human oversight, and that only solutions demonstrating value should be integrated and scaled.

The **hypothesis**, not a sourced fact, is that a single review surface could make one promotion decision easier to inspect without replacing Zurich's existing platform, Responsible AI, security or CI/CD controls.

## HOW_TO_USE_IN_2_MINUTES

1. Write the exact candidate revision / deployment identifier at the top.
2. Put one evidence link and a `PASS | HOLD | REJECT` result in each required row below.
3. Run the seven negative controls; any unexplained failure blocks promotion.
4. A named human reviewer records `PROMOTE | HOLD | REJECT` and the rollback target.

## One-revision promotion card

**Candidate revision:** `__________________`  
**Business/process owner:** `__________________`  
**Technical owner:** `__________________`  
**Review time:** `__________________`

| Required gate | Evidence to bind to this exact revision | Decision |
|---|---|---|
| **1. Value** | One predeclared business-value criterion and measured synthetic/pilot result; no inferred savings | `PASS / HOLD / REJECT` |
| **2. Held-out eval** | Frozen held-out set, threshold, result, failure examples and model/tool versions | `PASS / HOLD / REJECT` |
| **3. Data & privacy boundary** | Allowed data classes/sources, prohibited classes, retention boundary, and test showing the candidate stays inside them | `PASS / HOLD / REJECT` |
| **4. Action authority** | Principal/identity, permitted tools/actions, denied actions and deterministic policy evidence; an OPA/Rego-style oracle is one optional implementation | `PASS / HOLD / REJECT` |
| **5. Human escalation** | Exact conditions requiring human approval, approver role, timeout/fail-closed behavior and approval receipt location | `PASS / HOLD / REJECT` |
| **6. Trace & observability** | Trace ID linking input → model/router → tools → policy decisions → output; alerts for missing or anomalous evidence | `PASS / HOLD / REJECT` |
| **7. Cost / latency envelope** | Declared per-run or workflow envelope plus model-routing/fallback behavior; measured against the candidate revision | `PASS / HOLD / REJECT` |
| **8. Rollback** | Known-good prior revision, disable/rollback command or runbook, owner and recovery verification | `PASS / HOLD / REJECT` |

### Seven held-out negative controls

- [ ] **Wrong principal:** a non-authorized identity attempts an otherwise valid action → denied.
- [ ] **Out-of-scope action:** the agent attempts a tool/action absent from the allowlist → denied or escalated.
- [ ] **Privacy boundary:** restricted synthetic data is introduced → blocked, redacted or routed to the approved human path.
- [ ] **Prompt/tool misuse:** an instruction tries to override policy or call an unapproved tool → policy decision remains authoritative.
- [ ] **Quality regression:** a deliberately difficult held-out case drops below the declared threshold → `HOLD`, not silent promotion.
- [ ] **Router/fallback excursion:** fallback model/tool exceeds the declared cost or latency envelope → visible `HOLD` or approved exception.
- [ ] **Missing evidence / rollback:** trace, approval receipt or known-good rollback target is absent → fail closed.

## Decision rule

**PROMOTE** only when every required gate is `PASS`, all negative controls behave as expected, the evidence is bound to the exact candidate revision, and a named authorized reviewer approves.  
**HOLD** when evidence is missing, stale, inconclusive or not revision-bound.  
**REJECT** when a required control fails, a prohibited action/data path is observed, or safe rollback cannot be demonstrated.

**Reviewer decision:** `PROMOTE / HOLD / REJECT`  
**Reason / missing evidence:** `__________________`  
**Known-good rollback target:** `__________________`  
**Reviewer / approval receipt:** `__________________`

## Source-backed facts

1. Zurich's current **AI at Zurich** page says its 2025 Agentic AI Hyper Challenge produced **218 prototypes across 17 use cases, with 5 pilots now moving into production**. The same page publishes five Agentic AI principles covering secure/private/accountable design, responsible/explainable/governed AI, context, interoperability and technology standardization. It names **Maria Apazoglou, Group Head of AI Engineering & Platforms**.  
   https://www.zurich.com/about-us/ai-at-zurich
2. Zurich's **March 24, 2026** scaling article says controlled AI pilots should use strong data governance and human oversight, quantify results, and integrate/scale solutions that are truly adding value.  
   https://www.zurich.com/commercial-insurance/sustainability-and-insights/commercial-insurance-risk-insights/scaling-ai-with-confidence-the-smart-approach-to-unlocking-business-value
3. A current Zurich/ServiZurich **AI & Process Automation Engineer (Agents, Automation & Digitalisation)** listing requires production-ready automation that is tested, monitored, documented and maintainable, plus auditability, appropriate human-in-the-loop controls, responsible-AI compliance, version control and CI/CD/configuration-as-code skills.  
   https://www.careers.zurich.com/job/Barcelona-AI-%26-Process-Automation-Engineer-%28Agents%2C-Automation-%26-Digitalisation%29/811422502/

Sources re-verified on **2026-08-09**. These public sources establish an active pilot→production and governance surface; they do **not** establish slow promotions, control failures, incidents, savings, external budget or demand for this artifact.

## Assumptions

- A production promotion is meaningfully associated with an identifiable candidate revision/deployment.
- Reviewers benefit from a compact pointer layer even when underlying evidence stays in existing Zurich systems.
- Held-out evals, authority checks, HITL, traces and rollback can be referenced without exposing private customer or production data.
- Model-routing, OPA/Rego-style policy and observability are implementation options, not claims about Zurich's current stack.

## Strongest falsifier

**Kill this wedge** if Zurich already has a low-overhead revision-bound mechanism that joins business-value evidence, held-out evals, data/privacy controls, deterministic action authority, human approval, trace evidence, cost/latency and rollback for each promoted agent revision — or if the five production-moving pilots are intentionally scoped so that this additional review surface adds negligible value.

## Optional operator-reviewed outreach note — DO NOT SEND AUTONOMOUSLY

Maria — Zurich's public AI material shows five agentic pilots moving toward production and unusually clear principles around governed actions and standardization. I drafted a one-page, revision-bound pilot→production evidence card that links value, held-out evals, data boundaries, action authority, HITL, traces and rollback without assuming Zurich lacks any of those controls. If that review surface is already solved internally, the card is a quick falsifier; if evidence is fragmented, it may be a useful discussion artifact.

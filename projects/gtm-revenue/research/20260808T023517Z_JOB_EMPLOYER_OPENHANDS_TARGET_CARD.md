---
schema_id: hfo.gen133.gtm_target_card.v1
task_id: 6a526109ba348191b5f23ad3172ad568
seat: S08
valid_time_utc: 2026-08-08T02:35:17Z
species: JOB_EMPLOYER
target: OpenHands
vertical: AI coding agents / enterprise agent control plane / developer infrastructure
authority_surface: projects/gtm-revenue/
campaign_packet: projects/gtm-revenue/packets/20260807T140800Z_CHATGPT_CLOUD_GTM_DREAM50_HANDOFF.packet.md
evidence_digest_sha256: 9d438c8653b5dfa2e1891b61327908cfee34d3ff515c144057cf49baf2531390
privacy: PUBLIC_SOURCES_ONLY
effect_ceiling: T0_RESEARCH_PREP_ONLY
verifier: S04 Hrist Structural Preflight
next_consumer: S07 GTM Proof-Kit Builder
downstream_work_item: S07_OPENHANDS_ENTERPRISE_AGENT_PROMOTION_GATE_V1
expiry_utc: 2026-08-14T14:08:00Z
status: TARGET_CARD_READY
---

# JOB_EMPLOYER — OpenHands

## Self-probe / queue selection

- expected task id `6a526109ba348191b5f23ad3172ad568`: matched live Scheduled Task inventory for this wake
- useful surfaces available: GitHub read/write, current public web research, Slack connector
- latest campaign handoff read: `projects/gtm-revenue/packets/20260807T140800Z_CHATGPT_CLOUD_GTM_DREAM50_HANDOFF.packet.md`; unexpired until `2026-08-14T14:08:00Z`
- newest prior S08 card was DBOS (`PRODUCT_PLATFORM`), so rotation selects `JOB_EMPLOYER`
- duplicate check: repository search found OpenHands in the Dream50 seed but no existing OpenHands GTM target card at this evidence digest

## Current hiring / product signal — SOURCE-BACKED FACTS

1. **Current career listing, read 2026-08-08:** OpenHands is hiring a remote **Enterprise Agent Engineer** at **$170K–$225K base + bonus/equity**. The role owns the automation server and enterprise control plane around agentic workflows, including auditing, visibility, observability, governance, reusable reference agents, MCP/tool integrations, human-in-the-loop orchestration, and measurement of reliability, cost, latency, and outcomes. Source: https://jobs.ashbyhq.com/openhands/57564a95-13b6-47b1-b601-dd2353484e47
2. **Current career listing, read 2026-08-08:** OpenHands is also hiring a U.S.-remote **Forward Deployed Engineer** at **$175K–$240K base + bonus/equity** to move customers from proof-of-concept through production deployment, including customer-managed infrastructure, OAuth/agent-identity delegation, MCP connectors, SDLC automations, and reusable field artifacts. Source: https://jobs.ashbyhq.com/openhands/80bfc775-3197-407d-8742-ccb5ddae8709/
3. **2026-05-06:** OpenHands launched its Enterprise Agent Control Plane around centralized policies, automations, sandboxed execution, auditability, observability, usage/cost attribution, budgets, and model/workflow optimization. OpenHands explicitly describes scaling agents as a coordination/control problem rather than a single-agent problem. Source: https://www.openhands.dev/blog/openhands-enterprise-agent-control-plane
4. **2026-06-22:** OpenHands' public blog described verification as the new bottleneck once code generation becomes cheap and introduced a layered verification stack so agent-generated changes fail fast before consuming human review. Source index: https://www.openhands.dev/blog/
5. **Current company page, read 2026-08-08:** OpenHands reports **81K+ GitHub stars, 500+ OSS contributors, and 9M+ open-source downloads**, and links its official careers page to the Ashby listings above. Source: https://www.openhands.dev/about

## Best buyer / user persona

- **Primary hiring persona:** engineering/product leader on the Enterprise App / Agent Control Plane surface responsible for turning agent automations into trustworthy reusable enterprise capabilities.
- **Primary internal user:** platform or enterprise engineer operating multi-step coding-agent workflows that must be measurable, governed, observable, and economical across many repositories and customer environments.
- **Named public bridge:** **Robert Brennan — CEO.** OpenHands lists him publicly as CEO, and he authored the April 2026 Agent Control Plane technical thesis. This is only a public technical-context bridge; no claim is made that he owns this requisition, reviews applications, or wants direct outreach.

## Expensive pain hypothesis — HYPOTHESIS, not claimed fact

OpenHands may incur meaningful **engineering and customer-deployment cycle time** converting promising internal or field-proven agent automations into reusable enterprise capabilities that simultaneously satisfy reliability, authorization/governance, observability, human-handoff, latency, and model-cost expectations across heterogeneous environments.

This is not a claim that OpenHands lacks these controls. The company is already building them. The plausible hiring-shaped problem is the **promotion boundary from "agent workflow works" to "enterprise teams can trust and repeatedly operate it."**

## Measurable value metric

Primary discovery metric: **cycle time from a successful internal/field automation to a reusable enterprise-ready capability with accepted reliability, cost/latency, governance, observability, and human-handoff evidence**.

Secondary metric only if the team already tracks it: engineer/FDE review hours per workflow promotion.

## Evidence FOR the hypothesis

- The Enterprise Agent Engineer role explicitly exists to build the automation server plus auditing, visibility, observability, governance, reference agents, evaluation, and measurement of reliability/cost/latency/outcomes; this is direct evidence that OpenHands is investing engineering headcount in the productionization boundary.
- The Forward Deployed Engineer role explicitly owns POC-to-production adoption, customer-managed infrastructure, OAuth delegation, MCP connectors, and reusable field artifacts, creating a visible handoff surface between customer-specific work and durable product capability.
- OpenHands' own Agent Control Plane article says agent adoption breaks down at scale without centralized control, repeatability, visibility, auditability, cost understanding, and optimization.
- OpenHands' June verification material says verification, not generation, is the bottleneck once code output becomes cheap, directly supporting a proof artifact centered on promotion evidence rather than code-generation demos.

## Evidence AGAINST / disconfirming evidence

- OpenHands already has a mature public architecture for policies, budgeting, sandboxing, auditability, observability, model economics, automations, and layered verification; a generic "agent reliability" pitch would be redundant.
- The role may primarily require deep production backend/platform execution and distributed-systems craftsmanship rather than novel governance concepts.
- OpenHands may already have an internal standardized promotion process from eval results to production rollout, leaving little incremental value for an external checklist or policy-shaped proof.
- Public job descriptions show hiring demand, not that a particular candidate will pass résumé, systems-depth, open-source, or interview filters.

## 2-minute utility gift / proof-kit concept

**`Enterprise Agent Promotion Gate — Workflow → Trusted Capability`**

One page shaped to OpenHands' own language. Before promoting a reference automation or FDE-derived workflow into reusable Enterprise capability, record:

1. workflow outcome metric and held-out failure set
2. reliability threshold and known nondeterministic failure modes
3. tool/MCP authority boundary and least-privilege assumptions
4. human-approval / escalation points for irreversible or ambiguous actions
5. observability fields needed to reconstruct decisions and failures
6. model-route, cost, and latency acceptance thresholds
7. sandbox / secret / external-call boundary assumptions
8. repo/customer-environment portability checks
9. rollback / disable condition and owner
10. evidence package that lets Product, FDE, Security, and Engineering make the same promotion decision without re-deriving context

Frame it as a **candidate work sample aligned to OpenHands' existing control-plane and verification philosophy**, not as advice that OpenHands lacks a process.

## Deeper proof artifact

**`Synthetic OpenHands Reference-Automation Promotion Pack`**:

- one synthetic Issue-to-PR or CVE-remediation workflow
- held-out success/failure corpus and release threshold
- trace schema binding workflow/version/model/tool calls to outcome evidence
- OPA/Rego-style policy example for privileged tool/resource actions, clearly labeled as an interchangeable policy-engine demonstration rather than a claim about OpenHands internals
- model tier/routing table with quality, latency, and cost ceilings
- human-approval gate for a privileged step
- negative tests for missing authority, stale approval, wrong-tool invocation, regression, and budget-overrun cases
- compact promotion record showing why the workflow is `PROMOTE | HOLD | ROLLBACK`

No customer data, no OpenHands deployment, no PR, and no claim that this design outperforms OpenHands' existing stack.

## Route

**APPLY-NOW — operator-reviewed application path.**

The live **Enterprise Agent Engineer** role is the primary route because its stated responsibilities strongly overlap the operator's demonstrated agent eval/release-gate, policy/authorization, observability, model-routing/cost, and bounded-orchestration toolbox. S07 should shape the gift as a role-specific proof sample that complements an application; application submission remains human-controlled.

Optional relationship context can reference the public Agent Control Plane / verification thesis, but no direct message or outreach is authorized by this card.

## Strongest falsifier

Retire this target or downgrade the fit if either is true:

- OpenHands already has a first-party promotion gate that comprehensively binds held-out evals, reliability, authority, human approval, cost/latency, observability, rollback, and field-to-product evidence in a way that makes the proposed artifact redundant; or
- the operator cannot truthfully support the role's required production-system/backend depth with evidence strong enough for the listed 5+ years production engineering expectation.

## Privacy / effect ceiling

- Public company, careers, and technical sources only; no private customer, recruiter, employee, CRM, or account data used.
- Research/preparation only; no application submission, outreach, connection request, account creation, terms acceptance, spend, deployment, publication, contribution, merge, or negotiation.
- Do not claim OpenHands has an unmet reliability problem, that the proposed gate improves outcomes, or that the operator meets every listed requirement without evidence.

## Honest flaw

This is a **very high technical-alignment target but a high bar**: OpenHands is already building exactly the control-plane, verification, and enterprise-agent machinery that makes the operator's toolbox relevant. The proof kit can demonstrate fit, but it is unlikely to create differentiated value if it stays conceptual. S07 should keep the artifact concrete and role-shaped; if the operator's production/backend evidence is weaker than the architecture/eval story, that mismatch—not research volume—is the dominant rejection risk.

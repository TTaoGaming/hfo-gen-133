# S08 GTM Target Card — Accenture

```yaml
schema: hfo.gen133.gtm_target_card.v1
task_id: 6a526109ba348191b5f23ad3172ad568
wip: 1
target: Accenture
species: CHANNEL_PARTNER
vertical: enterprise_agentic_ai_delivery_and_ai_economics
route: RELATIONSHIP_ONLY
privacy: PUBLIC_SAFE_SYNTHETIC_ONLY
effect_ceiling: T0_PREP_RESEARCH_GIT
verifier: S04
next_consumer: S07
consumer_workitem: S07_ACCENTURE_AGENTIC_COST_QUALITY_PROMOTION_CARD_V1
expiry_utc: 2026-08-14T14:08:00Z
evidence_digest_sha256: 2aa9ff2353e78a39e13f59666863dbb6987c8c9f1dc5dc40149a7c900dc1df66
```

## Current business signal

Accenture is actively building and selling enterprise Agentic AI delivery plus AI-economics controls rather than only advisory work. On 2026-07-29 it announced Accenture Tokenomics, an operating model for connecting AI-token consumption to business outcomes, choosing the right model for each task, and continuously optimizing value as models and workloads change. Its AI Token Navigator includes a Model Engine for routing workloads and a Command Center intended to expose cost per successful business action; the described Control Plane can enforce budgets-as-code, circuit breakers and policy-as-code at runtime.

On 2026-05-06 Accenture and ServiceNow announced a Forward Deployed Engineering program intended to move agentic-AI work from enterprise pilot to production at scale. The program places Accenture and ServiceNow FDEs inside mutual customer environments, combines customer and third-party components, and establishes value metrics for the engagement. Accenture's current AI Refinery surface also describes agent orchestration across Accenture and partner agents, model selection based on cost/performance/accuracy, and governance across cost, accuracy, security and responsible use.

Primary official sources:
- 2026-07-29 — https://newsroom.accenture.com/blogs/2026/accenture-tokenomics-launched-to-help-enterprises-manage-ai-token-spend
- 2026-05-06 — https://newsroom.accenture.com/news/2026/servicenow-and-accenture-launch-forward-deployed-engineering-program-to-scale-agentic-ai-across-the-enterprise
- verified current 2026-08-09 — https://www.accenture.com/in-en/services/ai-data/ai-refinery
- verified current 2026-08-09 — https://www.accenture.com/nz-en/about/leadership/lan-guan

## Buyer / user persona and bridge

Best persona: Accenture AI & Data / Agentic AI delivery leadership responsible for taking multi-model client workflows from prototype to production while preserving business value, quality, security, runtime controls and repeatability across heterogeneous client environments.

Named public bridge: **Lan Guan — Chief AI and Data Officer and AI and Data Reinvention Engine Lead, Accenture**. Accenture's current leadership page supports those titles. This establishes public role relevance only; procurement authority, subcontracting authority, accessibility and interest are not inferred.

## Expensive-pain hypothesis

**Hypothesis, not a claim of current Accenture pain:** on multi-model client agent programs, Accenture delivery teams may consume material AI spend plus engineering/control-review time per accepted workflow revision proving that the exact candidate still meets a business-action success criterion while selecting an appropriate model route, preserving held-out quality, staying inside token/cost budgets, respecting tool/action authority, emitting sufficient traces and retaining a rollback path.

Primary measurable value metric: **AI spend per successful business action for an accepted agent/workflow revision**. Secondary metric: **engineer + reviewer hours per accepted revision**.

Evidence for the hypothesis:
- Accenture Tokenomics explicitly treats model selection, token consumption, workload routing and cost per successful business action as operating concerns requiring ongoing optimization.
- AI Refinery's model switchboard is explicitly described as selecting models using cost, performance and accuracy, while its governance surface covers cost, accuracy and security.
- The ServiceNow/Accenture FDE program explicitly owns pilot-to-production delivery in customer environments and establishes value metrics.

Evidence against the hypothesis:
- Accenture already has Tokenomics, AI Token Navigator, a Model Engine, a runtime Control Plane, AI Refinery governance/model-switching capabilities and a very large AI delivery organization.
- Those capabilities are direct evidence of maturity, not of a missing tool or delivery failure.
- No cited source establishes excess AI spend, margin leakage, release delays, authorization incidents, reviewer overload, customer dissatisfaction or willingness to use a narrow external specialist for this seam.

## Two-minute utility gift

**Agentic Cost-Quality Promotion Card — Outcome × Eval × Route × Authority × Budget × Rollback.** For one synthetic before/after agent revision, bind one business-action success criterion, a tiny held-out eval, selected model route, token/cost envelope, allowed/denied tool actions, trace completeness and rollback revision. Return `PROMOTE | HOLD | REJECT` while showing only material deltas or missing evidence.

## Deeper proof artifact

Build a public-safe synthetic multi-model client-workflow promotion harness using fake enterprise data, mocked tools and offline model-output fixtures. Combine held-out quality checks with an independent OPA/Rego-style action-authorization oracle, model-tier/token-cost fixtures, explicit route-selection rules and negative controls for cheap-model quality loss, expensive-model overuse, privilege widening, budget breach, missing traces and rollback mismatch. Bind every verdict to exact workflow, eval, model-route and policy digests. No Accenture system, customer environment, paid model call, customer data, deployment, savings claim or production outcome.

## Strongest falsifier

Kill the wedge if Accenture Tokenomics, AI Token Navigator and AI Refinery already provide a low-overhead mechanism that binds each exact agent/workflow revision to business-action success, held-out quality, model-route choice, cost/token envelope, runtime action authority, traces, approval and rollback. Also kill the partner hypothesis if Accenture's delivery/subcontracting model does not admit narrow external specialist contributions of this type.

## Honest flaw

Technical adjacency is high precisely because Accenture already owns most of the proposed primitives. Commercial whitespace may therefore be very small: a generic AI-cost, routing or governance artifact would mostly repackage Accenture's freshly launched native capabilities. S07 should continue only if the **revision-bound cost-quality-authority evidence seam** is demonstrably distinct and recipient-useful; otherwise this target should be retired rather than rewarded for vocabulary overlap.

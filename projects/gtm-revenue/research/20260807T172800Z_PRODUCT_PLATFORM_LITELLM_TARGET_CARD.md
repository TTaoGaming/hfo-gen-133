# GTM Target Card — LiteLLM

```yaml
schema_id: hfo.gen133.gtm_target_card.v1
card_id: GTM-S08-PRODUCT_PLATFORM-LITELLM-20260807T172800Z
task_id: 6a526109ba348191b5f23ad3172ad568
valid_time_utc: 2026-08-07T17:28:00Z
species: PRODUCT_PLATFORM
target: LiteLLM
vertical: open-source AI gateway / model routing / agent + MCP control plane
source_evidence_digest_sha256: 39f5c768c6697dfccd9cf08994f58a03c02c8c9eac99a6914669d4978bd965b8
status: RESEARCHED_FOR_S07
route: RELATIONSHIP_FIRST_PRODUCT_ECOSYSTEM_TEST
privacy: PUBLIC_SOURCE_ONLY
effect_ceiling: T0_PREP_RESEARCH_GIT
verifier: S04 Hrist Structural Preflight
next_consumer: S07 GTM Proof-Kit Builder
expiry_utc: 2026-08-14T17:28:00Z
```

## Why LiteLLM is a high-fit product/platform target

LiteLLM is moving from a model proxy/router toward a broader **AI gateway / agent control plane** that spans LLM calls, MCP tools, agent traffic, routing, budgets, guardrails, RBAC and observability. At the same time, its July/August 2026 engineering posts show rapid iteration on AutoRouter, routing plugins, policy-driven agent evaluation and stability. That creates a credible product-extension surface for the operator's demonstrated strengths in policy-as-code, held-out eval/release gates, model tiering and traceable agent authorization.

This card does **not** claim LiteLLM is missing security, governance or evaluation. Its current public material already shows strong controls and an explicit policy/evaluation direction. The pain below is therefore a narrower, testable ecosystem hypothesis: whether customers need a reusable way to bind **evaluation evidence + organizational policy + routing/tool authorization** into one auditable deployment contract.

## Current product / business signal

- **2026-08-06 — official engineering blog:** LiteLLM shipped new AutoRouter visibility for savings and per-request classifier-cost reporting, continuing an active routing/cost-optimization push.
- **2026-08-05 — official engineering blog:** LiteLLM shipped one-click AutoRouter presets, configurable tiers and test-routing UX.
- **2026-08-04 — official engineering blog:** LiteLLM published Auto Router v1.97 usage/quality benchmarks, showing active work on quality-versus-cost routing.
- **2026-07-17 — official engineering blog:** LiteLLM launched **Router Plugins** so teams can layer custom signals such as language, domain, tenant policy and budget caps into routing. The post explicitly says the design is still evolving and asks users what they want next.
- **2026-06-03 — official engineering blog:** LiteLLM announced a Microsoft ASSERT integration for **policy-driven agent evaluation**, turning organizational policies into test scenarios that surface safety/quality defects before production.
- **Observed current 2026-08-07 — official AI Gateway page:** LiteLLM positions one control plane across LLM, MCP and Agent gateways with budgets/rate limits, guardrails, RBAC, usage tracking, routing and Datadog/OpenTelemetry logging.
- **Observed current 2026-08-07 — official pricing/enterprise pages:** open-source self-hosting plus enterprise governance/security/support; pricing is tied to gateway scale/request capacity rather than token markup.

## Best buyer / user persona

**Primary user persona:** AI-platform / ML-platform engineers who own a LiteLLM gateway and must make routing, policy, cost and release decisions safe enough for many internal teams.

**Primary product-side persona:** LiteLLM product/engineering leadership responsible for Router Plugins, Agent/MCP gateway controls, enterprise governance and developer-facing integrations.

**Secondary:** security/platform architects and solutions engineers serving regulated or high-volume LiteLLM deployments.

### Named public bridge

**Krrish Dholakia — CEO, LiteLLM.** LiteLLM's own engineering blog identifies him as CEO and author on the 2026-07-17 Router Plugins post, which explicitly asks the community how teams want to extend routing signals. This makes him a source-backed public bridge for product-feedback context only; it is **not** evidence that he is the right outreach recipient or that LiteLLM wants this specific extension.

## Expensive pain hypothesis — NOT A FACT CLAIM

> **Hypothesis:** As LiteLLM customers route not only model calls but also agent/MCP traffic, they may incur repeated platform-engineering and audit work translating organizational policy and held-out evaluation results into runtime routing/authorization decisions. A reusable **evidence-to-policy routing contract** could reduce that repeated work and make quality, cost and authority decisions more auditable.

The wedge is **not** another generic gateway or guardrail. LiteLLM already has those. The possible missing layer is a portable pattern that connects:

`held-out eval verdict -> policy decision -> allowed model/tool/agent route -> trace/audit evidence -> rollback condition`

using LiteLLM's existing extension points rather than competing with the core product.

### Measurable value metrics

Primary metric to discover: **platform/security engineering hours required to implement, review and maintain policy-aware routing/agent authorization per enterprise deployment or team**.

Secondary metrics if a real user/product conversation exposes them:
- policy-change lead time;
- number of bespoke routing/authorization plugins per customer/team;
- audit/review hours for model/tool access changes;
- model spend at a fixed held-out quality threshold;
- rate of routing-policy regressions / bypasses;
- incident or rollback burden after model/router changes;
- percentage of gateway policy represented as versioned/testable code rather than manual configuration.

No current LiteLLM customer baseline or savings figure is asserted.

## Evidence FOR the hypothesis

1. LiteLLM itself says teams requested Router Plugins specifically to layer **tenant policy, budget caps and other custom signals** onto routing without waiting for core changes.
2. The Router Plugins design is explicitly described as evolving, with a public request for additional use cases.
3. LiteLLM is simultaneously expanding from model routing into MCP/agent control-plane responsibilities, increasing the number of authorization and policy decisions that can plausibly need one consistent evidence model.
4. LiteLLM's Microsoft ASSERT integration proves policy-driven agent evaluation is a first-class concern, not an invented adjacent market.
5. AutoRouter is actively optimized for quality-versus-cost decisions; connecting a held-out quality/eval threshold to routing policy is therefore adjacent to an active product surface.
6. The operator's OPA/Rego, held-out test, release-gate and model-tiering work maps to the extension boundary without requiring a new competing gateway.

## Evidence AGAINST / strongest objections

1. LiteLLM already has RBAC, custom auth, guardrails, budgets, audit logs and Router Plugins; enterprise users may already have enough primitives to solve this cheaply.
2. ASSERT already connects written policy to agent evaluation, so an additional evidence-to-policy layer could be redundant or better implemented inside ASSERT/LiteLLM rather than as a separate kit.
3. Public sources show product capability and active roadmap work, **not** a customer willingness to pay for an OPA-style integration or a repeated implementation bottleneck.
4. Product leadership may prefer a generic plugin API rather than endorse one policy engine such as OPA; any artifact must remain modular and not imply LiteLLM/OPA strategic alignment.
5. The strongest opportunity may be a community/OSS contribution rather than a paid product or contract, so external commercial fitness is uncertain until a real conversation or user demand exists.

## 2-minute utility gift for S07

### `LITELLM_EVAL_TO_POLICY_ROUTING_CHECKLIST.md`

A one-page checklist a LiteLLM platform user can use in roughly two minutes before shipping a routing/plugin change:

1. business/quality acceptance metric is named;
2. held-out eval set and minimum threshold are versioned;
3. candidate model pool is explicit;
4. cost ceiling / budget signal is explicit;
5. tenant/data-residency constraints are explicit;
6. tool/agent authority scope is explicit where MCP/A2A is involved;
7. policy decision is deny-safe when evidence is missing;
8. routing decision emits traceable reason/signals;
9. rollback/default route is defined and tested;
10. policy/eval/router versions are bound in the audit record.

Add a tiny mapping from each check to a likely LiteLLM primitive: Router Plugin, budget/rate limit, guardrail/custom auth/RBAC, observability/logging, or external policy engine. **Do not claim LiteLLM currently fails any check.**

## Deeper proof artifact

`LITELLM_OPA_EVIDENCE_ROUTER_STARTER/`

A synthetic reference integration showing:
- LiteLLM Router Plugin receives routing context;
- held-out eval verdict + quality threshold become versioned input signals;
- OPA/Rego (or a replaceable policy adapter) evaluates tenant/data/authority/cost constraints;
- policy narrows candidate models or denies when required evidence is absent;
- MCP/agent action class can be included as a policy dimension without exposing real credentials;
- trace record binds policy version, eval version, selected route, reason, cost class and rollback/default;
- negative tests prove missing/expired evidence cannot silently broaden the candidate pool.

The proof must use synthetic data only, remain vendor-neutral at the policy-adapter seam, and make no claim of official LiteLLM compatibility, endorsement or production use until verified.

## Recommended route

**RELATIONSHIP-FIRST PRODUCT-ECOSYSTEM TEST.**

First objective: validate whether LiteLLM users/product leadership see repeated cost in connecting eval evidence, policy and runtime routing/agent authorization. The artifact should be useful as product feedback even if no commercial relationship exists. If validated, downstream routes could include a documented integration recipe, plugin package, enterprise delivery service, or contributor relationship — each requiring separate operator approval and evidence before publication or outreach.

This is **not** an apply-now card. No current LiteLLM job role was selected or verified in this pass.

## Strongest falsifier

Retire or materially revise this product hypothesis if any authoritative LiteLLM source/user establishes that:

- an existing first-class LiteLLM/ASSERT feature already binds evaluation verdicts directly to runtime routing/tool authorization with auditable versioned policy, making this kit redundant;
- enterprise users do not experience repeated engineering/audit work at this boundary;
- Router Plugins intentionally exclude external policy/eval decision semantics that this design requires; or
- a concise checklist/reference design gets no interest while users consistently name a different higher-cost gateway pain.

## Sources

1. LiteLLM Engineering Blog, **AutoRouter: Easy Visibility to Your Savings**, 2026-08-06. https://docs.litellm.ai/blog/auto-router-spend-visibility
2. LiteLLM Engineering Blog index, **AutoRouter: 1 Click Deploy**, 2026-08-05; **Auto Router v1.97**, 2026-08-04. https://docs.litellm.ai/blog
3. LiteLLM Engineering Blog, **Announcing Router Plugins: Customize Routing Signals**, 2026-07-17. https://docs.litellm.ai/blog/router-plugins-on-the-proxy
4. LiteLLM Engineering Blog, **Announcing LiteLLM x Microsoft ASSERT**, 2026-06-03. https://docs.litellm.ai/blog/litellm-microsoft-assert
5. LiteLLM, **AI Gateway for Agents, MCPs & LLM Routing**, observed current 2026-08-07. https://www.litellm.ai/ai-gateway
6. LiteLLM, **Pricing**, observed current 2026-08-07. https://www.litellm.ai/pricing
7. LiteLLM docs, **Getting Started**, observed current 2026-08-07. https://docs.litellm.ai/

## Consumer contract

S07 should consume **this exact target-card blob** and build only the two-minute checklist above unless a newer S08 card supersedes it before pickup. S07 must preserve the distinction between LiteLLM's source-backed current capabilities and the unverified commercial pain hypothesis. The checklist should complement LiteLLM's existing ASSERT, Router Plugins, guardrails/RBAC and observability rather than pretending they are absent.

## Honest flaw

This card has unusually strong primary-source product evidence but still lacks direct user/customer evidence that the proposed evidence-to-policy boundary creates meaningful recurring cost. LiteLLM is already moving quickly on routing, policy evaluation and agent control-plane features, so the opportunity could disappear through normal product evolution. The card therefore justifies a **small relationship/user-discovery and proof-kit test**, not a product-demand or revenue claim.
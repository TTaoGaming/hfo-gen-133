# S08 GTM Target Card — Kong AI Gateway

```yaml
schema_id: hfo.gen133.gtm_target_card.v1
created_utc: 2026-08-08T05:29:45Z
target: Kong AI Gateway / Kong Inc.
species: PRODUCT_PLATFORM
vertical: AI gateway / agent infrastructure / API governance
status: NEW_SOURCE_BACKED_TARGET
route: RELATIONSHIP_ONLY
primary_value_metric: change_release_cycle_time
metric_definition: elapsed time from proposed AI Gateway config/provider/policy change to production-promotion evidence; no baseline or savings claim asserted
public_bridge:
  name: Greg Peranich
  title: Staff Product Manager, Kong
  source_backed: true
best_buyer_user_persona: Kong AI Gateway product/platform engineering or ecosystem lead responsible for 2.x production adoption, policy extensions, GitOps migration, and safe release confidence
pain_class: HYPOTHESIS_ONLY
privacy: PUBLIC_SOURCES_ONLY
world_effect_ceiling: T0_PREP_RESEARCH_GIT_PLUS_INTERNAL_SLACK_POINTER
external_send_authority: NONE
verifier: S04 Hrist Structural Preflight, then a distinct independent technical verifier before any external use
next_consumer: S07
consumer_work_item: S07_KONG_AI_GATEWAY_CHANGE_ACCEPTANCE_GATE_V1
expiry_utc: 2026-08-22T05:29:45Z
evidence_digest_sha256: a4e46b24e8b3d06a65d4940433b28d7b9d4b72e80e13b84e1c7cca027dab91ed
evidence_digest_rule: UTF-8 newline-separated source-date|URL lines in the listed order below, no trailing newline
```

## Current product / business signal

Kong announced **AI Gateway 2.0** on **2026-07-16** as a dedicated AI runtime with its own control plane, admin API, versioning, and faster release cadence, separating it from the quarterly stability cadence of Kong Gateway 3.x. The announcement says Models, MCP Servers, and Agents become first-class entities, introduces a `kongctl` declarative/GitOps path, and says 2.1 was already in flight for August with custom model-cost management expected soon. The same post labels 2.0 **private beta** and said GA was planned for the end of July; this research pass did not find a later first-party GA or 2.1 announcement, so no GA claim is made here.

Kong's 2026 releases also show a broad production-control surface already in place: A2A support, MCP token exchange and scope-based tool filtering, JWK validation, dynamic model routing, token budgets, guardrails, MCP Tool ACLs, detailed AI governance metrics, centralized AuthN/Z, A2A audit telemetry, quotas, showback/chargeback, and model/provider switching. On **2026-07-16**, Kong additionally announced a ModelOp partnership aimed at connecting central AI-governance approvals to runtime enforcement. This makes Kong a strong fit for release-gate / policy / eval / cost-routing work, but it is also strong counterevidence against any generic claim that Kong lacks governance.

## Public sources

- **2026-07-16 — Kong AI Gateway 2.0: Built for the Pace of Agentic AI**  
  https://konghq.com/blog/product-releases/kong-ai-gateway-2-0-agentic-ai
- **2026-04-14 — Kong AI Gateway 3.14**  
  https://konghq.com/blog/product-releases/kong-ai-gateway-3-14
- **2026-01-14 — MCP Tool ACLs in Kong AI Gateway**  
  https://konghq.com/blog/product-releases/mcp-tool-acls-ai-gateway
- **2026-04-23 — Kong AI governance metrics for A2A / MCP**  
  https://konghq.com/blog/product-releases/kong-ai-governance-metrics-a2a-mcp
- **2026-07-16 — Kong + ModelOp zero-trust agentic AI governance partnership**  
  https://konghq.com/blog/enterprise/kong-modelop-zero-trust-agentic-ai-governance
- **Observed 2026-08-08 — Kong AI Gateway product page**  
  https://konghq.com/products/kong-ai-gateway

### Evidence-digest preimage

Canonical preimage for `evidence_digest_sha256`:

```text
2026-07-16|https://konghq.com/blog/product-releases/kong-ai-gateway-2-0-agentic-ai
2026-04-14|https://konghq.com/blog/product-releases/kong-ai-gateway-3-14
2026-01-14|https://konghq.com/blog/product-releases/mcp-tool-acls-ai-gateway
2026-04-23|https://konghq.com/blog/product-releases/kong-ai-governance-metrics-a2a-mcp
2026-07-16|https://konghq.com/blog/enterprise/kong-modelop-zero-trust-agentic-ai-governance
2026-08-08-observed|https://konghq.com/products/kong-ai-gateway
```

## Named public bridge

**Greg Peranich — Staff Product Manager, Kong.** Kong's April 14 AI Gateway 3.14 release and January 14 MCP Tool ACLs release identify Peranich in this product surface. That makes him a source-backed public bridge for product direction only; this card does **not** claim he is a procurement owner, hiring manager, or wants outside contribution.

## Expensive-pain hypothesis

**Hypothesis:** as Kong moves AI Gateway 2.x onto a faster independent release cadence while customers adopt a new runtime/control plane/admin API and migrate declarative workflows toward `kongctl`, platform teams may spend material engineering cycle time proving that a provider, policy, routing, or configuration change preserves behavior across **semantic routing/fallback, MCP authorization, A2A identity/scope, token/cost budgets, guardrails, telemetry evidence, and rollback/migration safety**.

The possible wedge is therefore not “add governance.” Kong already exposes substantial governance, authorization, observability, cost and routing controls. The narrower wedge is a **pre-production change-acceptance / release gate** that turns those controls into one reproducible promotion decision as the AI-specific product cadence accelerates.

**Primary measurable value metric:** change/release cycle time from proposed AI Gateway change to production-promotion evidence. Rework and rollback events can be diagnostic components, but this card asserts no current Kong baseline, bottleneck, or savings amount.

## Evidence supporting the hypothesis

- Kong explicitly separated AI Gateway 2.x from the quarterly Kong Gateway 3.x cadence so AI-specific features can ship faster, increasing the frequency of compatibility and promotion decisions.
- AI Gateway 2.0 introduces a distinct runtime/control plane/admin API plus an AI-native declarative path, creating a real migration and configuration-change boundary.
- Kong's own 3.14 material says multi-agent pipelines are already running in production and that every MCP/A2A hop is an opportunity for failure.
- Kong has independently added authorization, token-budget, routing, guardrail, observability and cost-management controls, meaning a cross-control acceptance gate has concrete underlying signals to bind rather than being purely conceptual.

## Evidence against / counterweight

- Kong already has strong production primitives: MCP Tool ACLs, token exchange/scopes, JWK validation, A2A identity and audit telemetry, dynamic routing, quotas, token budgets, tracing, declarative configuration and migration tooling.
- The ModelOp partnership directly targets the “last mile” from governance approval to runtime enforcement, which may overlap heavily with this proposed wedge.
- Kong's engineering/product teams may already have mature internal pre-release qualification that is not public; public docs do not prove excessive release cycle time, regressions, customer pain, outside-contributor demand, or a missing acceptance layer.
- AI Gateway 2.0 was described as private beta in the latest first-party release found here, so the product surface itself may still be changing too quickly for a stable external companion artifact.

## 2-minute utility gift / proof-kit concept

**AI Gateway Change Acceptance Gate — Route × Authority × Spend × Evidence.** One page, usable in two minutes before promoting a config/provider/policy change:

1. config diff maps only to intended Models / MCP Servers / Agents;
2. held-out semantic-route and fallback cases still pass;
3. unauthorized MCP tools remain denied under explicit scopes/ACLs;
4. A2A identity and token-exchange boundaries remain least-privilege;
5. token/quota/cost ceilings remain inside declared budget;
6. safety / PII / guardrail behavior does not regress;
7. traces/metrics bind caller → policy → route/tool → latency/token/cost outcome;
8. rollback or migration reversal has been exercised and attached to the decision evidence.

Frame this as a generic public-safe acceptance pattern adjacent to Kong's existing controls, not as criticism of Kong's current QA process.

## Deeper proof artifact

Build a synthetic **Kong AI Gateway GitOps Acceptance Harness** with no live customer traffic or private-beta credentials:

- sample declarative / `kongctl`-shaped configuration for model, MCP and agent surfaces using local or synthetic stubs;
- held-out requests for route/fallback behavior;
- OPA/Rego-style policy that classifies privileged routing, tool-authority and budget changes before promotion;
- negative controls for unauthorized MCP tool access, stale/changed scope, provider-fallback regression, budget breach, missing trace evidence, and migration/rollback mismatch;
- evidence binding: config/version → policy verdict → route/tool decision → token/spend/latency telemetry → pass/fail;
- one replayable acceptance report suitable for S04 / independent technical review.

This earns fitness only if S07 consumes the exact card into `S07_KONG_AI_GATEWAY_CHANGE_ACCEPTANCE_GATE_V1` and a downstream verifier accepts or rejects the artifact.

## Route

**RELATIONSHIP_ONLY.** Kong has a technology-partner ecosystem, but no source found in this pass solicits this exact contribution. Any later relationship, contribution, application, or partner action requires explicit operator review; this card authorizes none.

## Strongest falsifier

Kill this wedge if Kong AI Gateway 2.x, `kongctl` / APIOps, or Kong's existing partner stack already provides a comprehensive low-overhead pre-deploy acceptance layer that jointly covers semantic routing, authorization, cost/token budgets, telemetry evidence, and rollback/migration—or if S07's proposed gate merely restates Kong or ModelOp documentation without adding a testable artifact.

## Privacy / effect ceiling

Public first-party sources only. No beta access, account creation, proprietary docs, customer traffic/data, private configuration, deployment, publication, outreach, application, terms acceptance, paid provider call, spend, or negotiation. Git research plus one internal Slack pickup pointer is the ceiling for this wake.

## Honest flaw

The strongest evidence proves **rapid product evolution and a rich control surface**, not an unmet problem. Kong may already solve this internally, and the ModelOp partnership could make the proposed release-gate layer redundant. The private-beta status found in the latest first-party 2.0 release also means a proof artifact can become stale quickly; S07 should kill it rather than polish it if the current Kong release surface has already moved past these assumptions.

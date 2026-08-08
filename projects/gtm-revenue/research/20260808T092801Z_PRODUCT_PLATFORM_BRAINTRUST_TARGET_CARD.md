# S08 GTM TARGET CARD — Braintrust

```yaml
schema_id: hfo.gen133.gtm_target_card.v1
card_id: S08_PRODUCT_PLATFORM_BRAINTRUST_20260808T092801Z
target: Braintrust
species: PRODUCT_PLATFORM
vertical: AI developer infrastructure / evals / observability / model gateway
parent_packet: projects/gtm-revenue/packets/20260807T140800Z_CHATGPT_CLOUD_GTM_DREAM50_HANDOFF.packet.md
parent_packet_expiry_utc: 2026-08-14T14:08:00Z
evidence_digest_sha256: 9c9f4eceae34c7f8379a73d73fb06640923262a5d9e99f9bfe3daecf3ca7ea68
route: RELATIONSHIP_ONLY
privacy: PUBLIC_SAFE_SYNTHETIC_ONLY
world_effect_ceiling: T0_PREP_RESEARCH_GIT
verifier: S04 after S07 artifact production
next_consumer: S07
next_workitem: S07_BRAINTRUST_EVAL_TO_RUNTIME_POLICY_GATE_V1
expiry_utc: 2026-08-14T14:08:00Z
```

## Current signal

Braintrust is actively expanding the production-AI control surface around evaluation, observability and model access. Its current Gateway documentation describes a **beta, production-designed unified LLM API** spanning OpenAI, Anthropic, Google, AWS and other providers, with caching, observability, multi-provider support, regional routing and organization-wide usage/cost monitoring. Braintrust's June 17, 2026 cost-efficiency work goes further: it evaluates model selection, retries, fallbacks, tool use and escalation as one control-logic problem, and argues that the useful economic unit is **cost per resolved request under explicit quality/safety gates**, not raw token price. Its evaluation workflow separately supports immutable experiments, CI/CD regression checks and continuous production scoring. In February 2026, Braintrust announced an $80M Series B to expand infrastructure for production AI.

## Official/public sources

1. **2026-06-17 — Braintrust, “How to test agent cost-efficiency with Braintrust”**  
   https://www.braintrust.dev/blog/test-agent-cost-efficiency  
   Direct evidence: evaluates six routing/control strategies across model selection, retries, fallbacks and escalation; reports cost per resolved request and quality gates.
2. **Accessed 2026-08-08 — Braintrust Gateway docs**  
   https://www.braintrust.dev/docs/deploy/gateway  
   Direct evidence: beta unified multi-provider gateway; production workloads, caching, observability, usage/cost tracking and provider endpoint visibility.
3. **Accessed 2026-08-08 — Braintrust evaluation workflow**  
   https://www.braintrust.dev/docs/evaluate  
   Direct evidence: immutable experiments, CI/CD evals, production scoring, and production traces feeding new datasets.
4. **2026-02-17 — Braintrust Series B**  
   https://www.braintrust.dev/blog/announcing-series-b  
   Direct evidence: $80M financing and stated focus on infrastructure/observability for production AI.

## Buyer / user / public bridge

**Best user persona:** product or platform engineering owner responsible for Braintrust's Gateway + evaluation/deployment workflow, especially the boundary between experiments, CI promotion and production model-routing policy.

**Named public bridge:** **Ankur Goyal, founder and CEO**. Braintrust's February 17, 2026 Series B post is authored by Goyal and identifies the company mission around production-AI observability. This card does **not** infer that he owns a specific integration decision, partnership budget, or unmet need.

## Expensive-pain hypothesis — explicitly a hypothesis

**Hypothesis:** Braintrust users who discover a cheaper/better routing or escalation strategy through evals may still spend material engineering cycle time translating that experiment into a **versioned, enforceable runtime policy** whose model/fallback behavior is tied to the exact quality, safety and spend evidence that justified promotion.

This is not a claim that Braintrust lacks such machinery. It is a possible product/integration seam between Braintrust's demonstrated strengths: experiments + CI evals + production scoring on one side, and a multi-provider gateway on the other.

**Measurable value metric:** **AI spend per accepted/resolved request**, measured only for requests that clear the declared quality and safety thresholds. This follows Braintrust's own June 17 economic framing and avoids inventing a customer savings number.

## Evidence for / against

**For the hypothesis**
- Braintrust itself frames agent cost optimization as a control-logic problem spanning model selection, retries, fallbacks, tool use and escalation rather than a one-model choice.
- Its published experiment shows materially different quality/cost outcomes among routing strategies and explicitly gates strategies below an acceptance bar.
- Braintrust exposes both the evaluation side (experiments/CI/online scoring) and the runtime/provider side (Gateway), making the experiment-to-runtime boundary commercially relevant to its users.

**Against the hypothesis**
- Braintrust already has immutable experiments, CI/CD evals, online scoring, Loop, production dashboards/alerts and a Gateway; the missing seam may already be solved in product or intentionally left to application code.
- The June cost-efficiency example is an educational benchmark, not evidence that customers are asking Braintrust for policy-as-code or that this translation step is currently expensive.
- A generic “add release gates” idea would be redundant with Braintrust's existing evaluation workflow.

## Utility gift / proof kit

**2-minute gift:** **Eval → Runtime Route Decision Card** — a one-page matrix modeled on Braintrust's published support-agent experiment. For each candidate policy: quality bar, destructive-action safety bar, cost/resolved request, retry/fallback budget, promotion verdict, and one fail-closed rollback condition. The value is the compact handoff from “experiment won” to “runtime rule approved,” not another eval dashboard.

**Deeper proof artifact:** a public-safe synthetic repo that runs several model-routing strategies against held-out agent cases, emits a machine-readable `routing_policy.json` with the exact experiment/eval digest, and uses an OPA/Rego-style promotion gate to reject any policy that misses quality/safety bounds or loses evidence linkage. A fake gateway adapter exercises retry/fallback behavior without creating a Braintrust account, spending money, or touching private/customer data. Optional follow-on only after verifier review: map the manifest to Braintrust Gateway concepts if current docs show a legitimate non-duplicative integration seam.

## Consumption contract

S07 consumes **`S07_BRAINTRUST_EVAL_TO_RUNTIME_POLICY_GATE_V1`** and must either:
1. produce the compact Eval → Runtime Route Decision Card plus an executable synthetic negative-control example; or
2. return **KILL/REDUNDANT** with the exact Braintrust feature/docs that already provide equivalent experiment-to-runtime enforcement.

Research volume alone earns zero fitness.

## Strongest falsifier

**Kill this wedge** if current Braintrust product/docs already provide a low-friction, versioned promotion path that binds experiment/eval thresholds directly to enforced Gateway routing/fallback policy with auditable rollback/evidence linkage. Also kill it if S07 can only restate Braintrust's CI eval workflow without adding an executable acceptance boundary.

## Privacy / effect ceiling

Public Braintrust sources and synthetic fixtures only. No Braintrust account, API key, customer trace, private dataset, paid model call, deployment, publication, outreach, application, purchase, terms acceptance, negotiation or other external effect is authorized.

## Honest flaw

The target fit is high because Braintrust already thinks explicitly about evals, routing, cost and production observability — which is also the main risk. The evidence supports **product adjacency**, not an unmet commercial pain. Braintrust may already solve the experiment-to-runtime handoff internally or may view it as application responsibility; if so, this target should be falsified quickly instead of receiving a larger proof build.

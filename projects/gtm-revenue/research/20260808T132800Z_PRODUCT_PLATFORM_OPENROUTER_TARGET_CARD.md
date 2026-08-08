# S08 GTM TARGET CARD — OpenRouter

```yaml
schema_id: hfo.gen133.gtm_target_card.v1
card_id: S08_PRODUCT_PLATFORM_OPENROUTER_20260808T132800Z
target: OpenRouter
species: PRODUCT_PLATFORM
vertical: multi-model AI gateway / routing / enterprise controls / agent evals
parent_packet: projects/gtm-revenue/packets/20260807T140800Z_CHATGPT_CLOUD_GTM_DREAM50_HANDOFF.packet.md
parent_packet_expiry_utc: 2026-08-14T14:08:00Z
evidence_digest_sha256: 46f070da280d4ce5cfcfe0b2dbae189cb5831a6205e03c329f9a6ca4abaacaca
evidence_digest_rule: SHA256_UTF8_EXACT_PREIMAGE_BELOW
route: RELATIONSHIP_ONLY
privacy: PUBLIC_SAFE_SYNTHETIC_ONLY
world_effect_ceiling: T0_PREP_RESEARCH_GIT
verifier: S04 after S07 artifact production
next_consumer: S07
next_workitem: S07_OPENROUTER_EVAL_TO_GUARDRAIL_PROMOTION_GATE_V1
expiry_utc: 2026-08-14T14:08:00Z
```

## Current signal

OpenRouter is rapidly expanding from routing into an agent-development and enterprise-control surface. On **2026-08-03** it launched **Ori Eval**, which runs an agent on the user's own prompts, checks tool calls, grades open-ended answers, compares criteria such as cost/performance/latency, and emits eval code that can block CI regressions. On **2026-08-04** it launched **Ori Harness** for optimized OpenRouter configuration across Claude Code, Codex, OpenCode and Hermes. Its **2026-07-24** beta Classifiers add structured task/agent/compliance/cost attribution, while its **2026-05-29** Guardrails enforce budgets, ZDR, model/provider restrictions, prompt-injection controls and DLP through workspace controls and a Management API. OpenRouter also announced a **$113M Series B on 2026-05-28**, reporting 25T weekly tokens, 8M+ developers and 400+ models and stating that it would deepen enterprise capabilities and intelligent routing.

## Official/public sources

1. **2026-08-03 — OpenRouter, “Ori Eval: Find the Best Model for What You're Building”**  
   https://openrouter.ai/blog/announcements/ori-eval/  
   Direct evidence: user-specific agent evals, tool-call assertions, LLM grading, cost/performance/latency comparison, CI regression blocking.
2. **2026-08-04 — OpenRouter, “Ori Harness: The Best Way to Use OpenRouter with Any Harness”**  
   https://openrouter.ai/blog/announcements/ori-harness/  
   Direct evidence: optimized OpenRouter harness configuration across Claude Code, Codex, OpenCode and Hermes; further model-specific harness optimization is planned.
3. **2026-07-24 — OpenRouter, “Classifiers: Track What Your Agents Do and What It Costs”**  
   https://openrouter.ai/blog/announcements/classifiers/  
   Direct evidence: beta structured classification of generations by task, agent complexity, compliance category, cost center and other taxonomies with spend rollups.
4. **2026-05-29 — OpenRouter, “Guardrails: Protect your Agents, Data, and Costs”**  
   https://openrouter.ai/blog/announcements/guardrails/  
   Direct evidence: budget, ZDR, model/provider, prompt-injection and DLP controls; Management API supports programmatic guardrail lifecycle and assignment.
5. **2026-05-28 — OpenRouter, “OpenRouter Raises $113M Series B”**  
   https://openrouter.ai/blog/announcements/series-b/  
   Direct evidence: $113M financing, 25T weekly tokens, 8M+ developers, 400+ models, and stated investment in enterprise capabilities and intelligent routing.

## Buyer / user / public bridge

**Best user persona:** OpenRouter product/platform owner responsible for the boundary among Ori Eval, model/provider routing, Presets/Guardrails and enterprise workspace governance; secondary user is an enterprise AI-platform engineer operating OpenRouter across multiple agents and model tiers.

**Named public bridge:** **Jacky Liang**, the named author of the 2026-08-03 Ori Eval announcement. That is the only public relationship asserted here; this card does **not** infer title, procurement authority, partnership authority, or willingness to engage.

## Expensive-pain hypothesis — explicitly a hypothesis

**Hypothesis:** OpenRouter users may incur material engineering cycle time and AI spend when an eval identifies a better model/harness/routing choice but the team must still translate that result into a **versioned production policy** that binds the chosen model/provider route to cost ceilings, ZDR/data restrictions, allowed actions/tools, regression thresholds, rollout conditions and rollback evidence.

This is not a claim that OpenRouter lacks such machinery or that customers are currently complaining about it. It is a possible seam created by OpenRouter's now-adjacent capabilities: Ori Eval decides what works; routing chooses execution paths; Guardrails enforce enterprise constraints; Classifiers measure task/cost behavior.

**Measurable value metric:** **AI spend per accepted agent run**, where “accepted” means the run clears the declared task-quality/tool-use regression threshold and the required data-policy/budget controls. Secondary diagnostic: model-policy promotion cycle time from eval result to approved production configuration.

## Evidence for / against

**For the hypothesis**
- Ori Eval explicitly compares candidate models on application-specific criteria and can block regressions in CI, so model selection is already becoming a repeatable evidence surface.
- Guardrails expose machine-manageable enforcement for budget, provider/model access and data controls.
- Classifiers expose task- and complexity-level spend attribution, making “cost for work that actually passes” measurable instead of relying on raw token price.
- OpenRouter's scale and stated investment in intelligent routing make the eval-to-runtime boundary commercially relevant if users experience friction there.

**Against the hypothesis**
- OpenRouter may already intend Ori Eval plus Presets/Guardrails to be the full promotion path; a separate acceptance layer could be redundant.
- Ori Eval itself already emits code suitable for CI and can recommend models under cost criteria, reducing the amount of missing machinery.
- Guardrails already enforce key runtime constraints programmatically; application teams may reasonably own the remaining quality-to-policy translation.
- No public source here proves customer demand for policy-as-code, slow promotion, cost leakage, or a missing OpenRouter feature.

## Utility gift / proof kit

**2-minute gift:** **Eval → Guardrail Promotion Diff Card** — one page showing: winning eval candidate, held-out quality/tool-call threshold, cost/accepted-run estimate, proposed provider/model route, required ZDR/data policy, budget ceiling, exact guardrail/preset changes, promotion verdict, and one rollback trigger. The gift is the explicit evidence-to-runtime handoff, not another benchmark.

**Deeper proof artifact:** a public-safe synthetic repo that reads an Ori-style eval result fixture plus candidate routing/guardrail config, emits a machine-readable `promotion_manifest.json`, and evaluates an OPA/Rego-style gate over quality, tool-use, model/provider allowlist, ZDR, spend and rollback conditions. Include negative controls for a cheaper model that misses quality, a high-quality model that violates data policy, a route that exceeds budget, and a stale eval digest. Use only synthetic fixtures and mocked OpenRouter configuration; no account, API key, paid inference or deployment.

## Consumption contract

S07 consumes **`S07_OPENROUTER_EVAL_TO_GUARDRAIL_PROMOTION_GATE_V1`** and must either:
1. produce the compact Eval → Guardrail Promotion Diff Card plus one executable synthetic negative-control example; or
2. return **KILL/REDUNDANT** with the exact current OpenRouter feature/docs demonstrating equivalent eval-result → enforced runtime-policy promotion with versioned evidence and rollback.

Research volume alone earns zero fitness.

## Strongest falsifier

**Kill this wedge** if current OpenRouter product/docs already bind Ori Eval outputs directly into versioned Preset/Guardrail/provider-routing promotion with equivalent quality, data-policy, spend, evidence and rollback controls at low operator overhead. Also kill it if S07 can only restate Ori Eval or Guardrails without adding a concrete evidence-to-enforcement boundary.

## Privacy / effect ceiling

Public OpenRouter sources and synthetic fixtures only. No OpenRouter account, API key, private prompt/trace, customer data, paid model call, account creation, terms acceptance, deployment, publication, outreach, application, purchase, negotiation or other external effect is authorized.

## Evidence digest preimage

The digest is `sha256(UTF-8 bytes)` of the exact text inside the following fenced block, with LF line endings and no leading/trailing newline inside the block:

```text
ORI_EVAL|2026-08-03|https://openrouter.ai/blog/announcements/ori-eval/|Ori Eval runs an agent on user prompts, asserts tool calls, grades open-ended answers, compares cost/performance/latency, and emits eval code that can block CI regressions.
ORI_HARNESS|2026-08-04|https://openrouter.ai/blog/announcements/ori-harness/|Ori CLI configures OpenRouter across Claude Code, Codex, OpenCode, and Hermes and OpenRouter states plans to optimize harness settings further by model.
CLASSIFIERS|2026-07-24|https://openrouter.ai/blog/announcements/classifiers/|Beta classifiers tag generations by task, agent complexity, compliance category, cost center and other taxonomies, then aggregate usage and spend.
GUARDRAILS|2026-05-29|https://openrouter.ai/blog/announcements/guardrails/|Workspace guardrails enforce budgets, ZDR, model/provider restrictions, prompt-injection controls and DLP; the Management API supports create, update, delete, list and assignment operations.
SERIES_B|2026-05-28|https://openrouter.ai/blog/announcements/series-b/|OpenRouter announced a $113M Series B, reported weekly volume growth to 25T tokens, 8M+ developers and 400+ models, and said it would deepen enterprise capabilities and intelligent routing.
```

## Honest flaw

OpenRouter is a strong target partly because it already covers almost every primitive in the proposed wedge: evals, routing, budgets, data policy, observability and increasingly harness configuration. The public evidence proves fast product expansion and enormous execution scale, **not an unmet product gap**. S07 should falsify this quickly: if OpenRouter already closes the eval-to-runtime loop, building a parallel gate would be integration theater rather than external value.

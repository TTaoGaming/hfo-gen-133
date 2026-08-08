# OpenRouter Eval → Guardrail Promotion Diff Card

**Problem:** a model can win an eval and still be the wrong production choice if the promoted route violates data-retention, provider, budget, tool-use, or rollback requirements. This card turns “candidate won” into one reviewable **PROMOTE / HOLD** decision.

## WHY_THIS_MAY_MATTER

OpenRouter already exposes versioned Presets, programmatic Guardrails, usage Classifiers, and multi-model routing controls. The plausible seam is narrower: **is the exact eval evidence bound to the exact runtime policy change and rollback trigger before promotion?**

That seam is a hypothesis, not a claim that OpenRouter or its customers lack controls.

## HOW_TO_USE_IN_2_MINUTES

1. Copy the winning eval candidate and evidence digest into the left column.
2. Write the exact Preset / route / Guardrail diff in the middle.
3. Mark **PROMOTE** only when every required row is `PASS`; otherwise mark **HOLD`.
4. Keep the prior preset/version as the rollback target.

| Gate | Candidate evidence | Proposed production binding | PASS when |
|---|---|---|---|
| Candidate identity | eval digest: `________` | preset version: `________` | exact digests/versions recorded |
| Held-out quality | score: `____` | minimum: `____` | score ≥ minimum |
| Tool behavior | tool-call pass: `____%` | minimum: `____%` | pass rate ≥ minimum |
| Cost / accepted run | `$____` | ceiling: `$____` | cost ≤ ceiling |
| Model/provider route | model: `____`; provider: `____` | allowlist: `____` | route is allowed |
| Data policy | ZDR required? `Y/N` | guardrail: `____` | required policy is enforced |
| Budget | expected `$____/day` | guardrail cap `$____/day` | expected spend ≤ cap |
| Rollback | prior version: `____` | trigger: `____` | prior known-good version + trigger exist |

**Verdict:** `PROMOTE / HOLD`  
**Reviewer:** `________`  **UTC:** `________`

### Synthetic worked example

| Gate | Candidate evidence | Production binding | Result |
|---|---|---|---|
| Candidate identity | `eval_sha=9f2...a71` | `preset=v13` | PASS |
| Held-out quality | `0.93` | minimum `0.90` | PASS |
| Tool behavior | `99.1%` | minimum `98%` | PASS |
| Cost / accepted run | `$0.028` | ceiling `$0.035` | PASS |
| Model/provider route | `candidate-model-A / provider-A` | allowlist includes both | PASS |
| Data policy | ZDR required | ZDR enforced | PASS |
| Budget | `$3.40/day` | `$5/day` cap | PASS |
| Rollback | `preset=v12` | quality `<0.90` or cost `>$0.035` | PASS |

**Synthetic verdict: PROMOTE.** These values are illustrative only; they are not OpenRouter customer data or measured OpenRouter outcomes.

## Executable negative control

The following is a deliberately tiny **OPA/Rego-style synthetic gate**, not an OpenRouter API schema. It should deny a cheaper candidate that misses the quality floor.

```rego
package promotion

default allow := false

allow if {
  input.quality >= input.min_quality
  input.cost_per_accepted_run <= input.max_cost
  input.model_allowed
  input.provider_allowed
  input.zdr_ok
  input.eval_digest == input.expected_eval_digest
}
```

Negative-control input:

```json
{
  "quality": 0.82,
  "min_quality": 0.90,
  "cost_per_accepted_run": 0.019,
  "max_cost": 0.035,
  "model_allowed": true,
  "provider_allowed": true,
  "zdr_ok": true,
  "eval_digest": "9f2...a71",
  "expected_eval_digest": "9f2...a71"
}
```

Expected result: `allow = false` because cheaper is not sufficient when held-out quality fails.

## SOURCE-BACKED FACTS

- OpenRouter Guardrails can enforce budget limits, model/provider allowlists, Zero Data Retention, and other security/data controls, and can be managed programmatically.
- OpenRouter Presets have designated versions and can capture a tested inference configuration into a versioned production reference.
- OpenRouter Classifiers can tag generations by dimensions such as task type, agent complexity, compliance category, and cost center for usage analysis.
- OpenRouter publicly describes its platform as handling routing, reliability, cost optimization, and compliance across providers, and reported substantial scale in May 2026.
- OpenRouterTeam’s public `skills` repository includes a `spawn-ori-eval` skill for delegated model evals.

## HYPOTHESES / ASSUMPTIONS

- Teams may still need an explicit artifact that binds a winning eval digest to the exact Preset/Guardrail/provider change and rollback condition.
- `AI spend per accepted agent run` may be more decision-useful than raw token price when quality/tool-use thresholds differ by route.
- The best recipient is likely a product/platform owner spanning evals, routing, Presets/Guardrails, or an enterprise AI-platform engineer using those surfaces. This is a persona hypothesis, not proof of buying authority.

## FALSIFIER

**Kill this wedge** if OpenRouter already natively binds eval outputs to versioned Preset/Guardrail/provider-routing promotion with equivalent quality, data-policy, spend, evidence-digest, approval, and rollback controls at low operator overhead. Also kill it if this card merely restates existing product UI without reducing a real handoff.

## EVIDENCE LINKS

Verified public sources used for this card:

- https://openrouter.ai/docs/guides/features/guardrails/overview
- https://openrouter.ai/docs/guides/features/presets
- https://openrouter.ai/docs/guides/features/classifiers
- https://openrouter.ai/blog/announcements/guardrails/
- https://openrouter.ai/blog/announcements/series-b/
- https://github.com/OpenRouterTeam/skills

Target-card sources that motivated the wedge but were **not independently retrievable through the carrier’s current web index this wake**:

- https://openrouter.ai/blog/announcements/ori-eval/
- https://openrouter.ai/blog/announcements/ori-harness/

## OPTIONAL OPERATOR-REVIEWED OUTREACH NOTE — NO SEND

I made a one-page eval→runtime promotion diff that binds quality, cost, route, data policy, budget, and rollback to one candidate digest. It may be redundant with what you already have; if OpenRouter already closes that loop natively, that itself falsifies the idea. If not, the card is a compact way to test the handoff without adding another benchmarking layer.

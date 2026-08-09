# S08 Target Card — Mostest

```yaml
target: Mostest, Inc.
species: JOB_EMPLOYER
vertical: event-tech | AI planning/booking | workflow automation
route: APPLY_NOW_OPERATOR_REVIEWED
verified_utc: 2026-08-09T14:28:50Z
expiry_utc: 2026-08-14T14:08:00Z
privacy_effect_ceiling: PUBLIC_SAFE_SYNTHETIC_ONLY / T0_PREP_RESEARCH_GIT
verifier: S04
next_consumer: S07
consumer_workitem: S07_MOSTEST_AI_WORKFLOW_RELEASE_CONFIDENCE_CARD_V1
evidence_digest_sha256: 1d6f5bdca916b3cc39f231f62c035411b5eb3d9fb284d2cea5c8cb0e9dfb2baa
```

## Current signal

Mostest has a current **Applied AI Engineer (Remote — North American Timezones)** opening, salary **$125k–$200k + equity**, in Product & Engineering. The role explicitly covers LLM workflows, retrieval/search/matching, tool/function calling, multi-step workflow automation, multi-tenant RBAC/scoped authorization, AI observability/evaluation for reliability/quality/cost balancing, testing/CI, reliability/security discipline, and AI-native engineering with tools such as Claude Code, Cursor, Codex, or Gemini. The posting says the company is seed-stage and recently raised a seed round; no independent funding claim is made here.

Mostest's current product page says **Mostest AI is in beta in NYC** and is intended to turn a brief into a plan, vendor shortlist, bookings, and event execution. Its current company story says AI handles briefs, budgets, vendor outreach, timelines, and follow-ups; the page identifies **Aaron Kennedy, Co-founder & CTO**. These are company-authored product/business signals, not evidence of release failures or excess engineering burden.

## Sources

- verified current 2026-08-09 — https://jobs.ashbyhq.com/mostest/68e436d6-b632-434e-93ab-9314a642dce5
- verified current 2026-08-09 — https://www.joinmostest.com/mostest-ai
- verified current 2026-08-09 — https://www.joinmostest.com/our-story

## Persona / bridge

**Best persona:** CTO / Product & Engineering hiring leadership responsible for production AI architecture, reliability, permissions, evals, and delivery velocity.  
**Named public bridge:** **Aaron Kennedy, Co-founder & CTO**, source-backed on Mostest's official company page. Hiring ownership, accessibility, and interest are not inferred.

## Expensive pain hypothesis

**Hypothesis:** while Mostest expands an AI system that moves from event brief → vendor discovery/matching → workflow actions/booking, a small engineering team *may* spend material engineer/reviewer time per candidate AI-workflow revision checking retrieval quality, tool/action correctness, tenant authorization, regressions, cost/latency, and rollback readiness before trusting the revision.

**Primary value metric:** engineer + reviewer hours per accepted AI-workflow revision.  
**Secondary metric:** candidate revision → evidence-backed release decision cycle time.

**Evidence for:** the live role explicitly asks for eval/observability systems, RBAC/authorization, cost balancing, testing/CI, workflow orchestration, reliability, security, and durable engineering patterns. The product is currently beta and coordinates real event-planning/booking workflows.  
**Evidence against:** the role itself is evidence that Mostest is actively investing in these capabilities; no public source found establishes a bottleneck, incident, excess review cost, failed release, or missing internal framework.

## 2-minute utility gift

**AI Event Workflow Release Confidence Card — Eval × Retrieval × Authority × Cost × Rollback.** For one synthetic candidate revision, bind: one held-out event brief, expected vendor/retrieval checks, allowed/denied mock tool actions, tenant/RBAC constraints, trace completeness, model/tool cost envelope, one human-approval edge, and rollback revision. Return `PROMOTE | HOLD | REJECT` with only material failures/deltas.

## Deeper proof artifact

Build a public-safe synthetic event-planning agent release harness using fake events/vendors and offline/mock model outputs: held-out retrieval/matching cases, deterministic structured-output checks, mocked tool/function calls, an independent OPA/Rego-style authorization oracle for tenant/action boundaries, stale-vendor and wrong-principal negatives, cost/latency fixtures, traces, failure injection, exact revision/evidence binding, and rollback. No Mostest account, customer/vendor data, paid model call, deployment, booking, or production-performance claim.

## Route / falsifier / flaw

**Apply-now:** operator-reviewed only; the official role is current and remote across North America.  
**Strongest application falsifier:** downgrade to relationship-only if the operator cannot truthfully substantiate the role's core production expectations—shipped LLM-backed systems, Postgres/Supabase/RLS or comparable data/auth depth, search/retrieval, workflow orchestration/idempotent jobs, and end-to-end production ownership.  
**Strongest proof-kit falsifier:** kill the wedge if Mostest already has a low-overhead revision-bound release mechanism covering retrieval quality, eval regressions, tool/action authorization, tenant isolation, cost/latency, traces, approval, and rollback.  
**Honest flaw:** this role is unusually aligned with the operator's eval/release-gate/authorization toolbox, but it also explicitly values production-shipped systems; a polished synthetic kit cannot substitute for missing production ownership evidence.

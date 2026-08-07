# GTM Problem Discovery + Proof-Kit Playbook v1

```yaml
schema_id: hfo.gen133.gtm.playbook.v1
valid_time_utc: 2026-08-07T14:06:00Z
source: operator debrief from first SCORE meeting with David Eaton + current GTM research
claim_status: proposed
privacy: PUBLIC_SAFE
world_effect_ceiling: T0_PREP_ONLY
```

## Doctrine

**Do not start with what we sell. Start with what the organization loses.**

The discovery sequence is:

`workflow → friction/failure → baseline → consequence → target condition → annual value → smallest experiment → proof → commercial path`

Use Six-Sigma/process-improvement instincts: where is skilled headcount consumed, where does work queue, where is margin leaking, where is risk concentrated, and what would a measurable target condition be?

A 10× value-to-fee ratio is a useful forcing heuristic, **not a pricing law**. A credible $100k annual value may support a $10k engagement; a credible 2× return can still be commercially rational. Never invent the baseline or savings.

## 15 expensive pain species

| # | pain | value metrics | toolbox |
|---|---|---|---|
| P1 | AI pilot → production gap | cycle time, adoption, FTE hours, error rate | discovery + bounded productionization |
| P2 | Agent reliability / false-green releases | regression rate, incidents, MTTR, release delay | held-out tests, release gates, multi-quorum verification |
| P3 | Agent identity / tool authorization | unauthorized-action risk, review hours, audit burden | OPA/Rego, authority matrices, policy decision/enforcement |
| P4 | AI governance / auditability | audit hours, deployment blockers, evidence gaps | policy-as-code, receipts, human gates |
| P5 | Model cost / routing sprawl | AI spend, latency, cost/request | model tiering/routing + eval thresholds |
| P6 | High-headcount manual operations | FTE cost, queue size, cycle time | compound AI / workflow automation |
| P7 | Security operations toil | analyst hours, MTTR, false-positive rate | bounded agent workflows + verification |
| P8 | GRC/compliance evidence toil | audit hours, evidence cycle, control gaps | policy + evidence automation |
| P9 | Insurance document workflows | turnaround, broker/underwriter hours, rework | document/RAG + authority + evals |
| P10 | Healthcare administrative workflows | cost/case, denial/rework, turnaround | workflow automation + gates |
| P11 | Procurement/AP/contract workflows | touch time, exceptions, leakage | document AI + deterministic approval |
| P12 | Revenue/support operations | response time, conversion, rep capacity | CRM/agent workflows + deterministic steps |
| P13 | Developer-agent adoption | PR cycle, review hours, defect/vuln rate | coding-agent evals + release/security gates |
| P14 | Retrieval/context permission failures | grounding quality, stale context, access incidents | retrieval evals + permission policy |
| P15 | Agent observability/accountability | MTTR, audit time, unknown failures | trace schema + receipts + verdicts |

## Discovery prompts

Use these with friends, team leads, buyers, mentors, recruiters, or customer-facing engineers. The first call is learning, not pitching.

1. Which recurring workflow consumes the most skilled-person time without differentiating the business?
2. Where does work wait for review, approval, data, or a handoff?
3. Which exceptions create the most rework?
4. What process has grown by adding headcount rather than changing the system?
5. What AI pilot exists but has not become trusted production work?
6. What breaks when people use agents/coding assistants in real workflows?
7. Where do people manually verify AI output because they do not trust it?
8. Which agent/tool actions require unclear or repetitive approvals?
9. Where are model costs or latency visible enough to matter?
10. What compliance/security evidence is repeatedly assembled by hand?
11. What is the baseline volume, time per case, error/rework rate, and loaded labor cost?
12. What would a good target condition look like in 30–90 days?
13. What failure would make an automation unacceptable even if it saved time?
14. Who owns the budget or consequence for this problem?
15. What would make a small pilot unquestionably worth continuing or killing?

## Value worksheet

```text
annual_labor_value = annual_volume × current_minutes_per_case / 60 × loaded_hourly_cost
annual_error_value = annual_errors × average_error_or_rework_cost
annual_risk_value  = expected_loss_before - expected_loss_after   # only with defensible inputs
annual_revenue_value = incremental_volume_or_conversion × contribution_margin
annual_ai_cost_value = current_model_spend - target_model_spend   # quality threshold must hold
credible_value = use the subset with evidence, not the most impressive sum
value_multiple = credible_value / proposed_fee
```

A proposal without a measurable baseline is a learning experiment, not a value claim.

## 15 two-minute gifts

| id | artifact | recipient use |
|---|---|---|
| K1 | Agent Production Readiness Scorecard | ten production checks in ~2 minutes |
| K2 | Held-Out Eval + Release Gate Starter | negative tests, acceptance threshold, rollback |
| K3 | OPA/Rego Agent Action Policy Starter | generic authority/tool/human-review policy examples |
| K4 | MCP / Non-Human Identity Risk Checklist | identity, delegation, scopes, secrets, audit, revocation |
| K5 | AI Cost Tiering & Routing Decision Table | decide cheap vs frontier model by quality/risk threshold |
| K6 | Agent Mini-FMEA | failure mode × severity × occurrence × detectability × control |
| K7 | Agent Observability Trace Checklist | actor/model/tool/policy/cost/outcome trace fields |
| K8 | Process ROI / Headcount Worksheet | convert recipient-owned baseline into value hypothesis |
| K9 | Human Approval / Authority Matrix | map action classes to autonomous/review/deny |
| K10 | Stuck AI Pilot 30/60/90 Checklist | discovery → acceptance → production ownership/gates |
| K11 | Compound-AI One-Page Architecture | router + retrieval + tools + policy + eval + human gate |
| K12 | Discovery Interview Prompt Pack | headcount/cycle-time/margin/risk questions |
| K13 | Agent Red-Team Test Pack | defensive prompt injection/tool misuse/privilege/data-leak tests |
| K14 | Retrieval Quality / Freshness Checklist | grounding, freshness, authorization, fallback |
| K15 | Value-Based Business Case One-Pager | baseline → target → annual value → fee → falsifier |

### Gift rules

1. Useful without buying anything.
2. Recipient understands the purpose in ~15 seconds and can use it in ~2 minutes.
3. No invented diagnosis of the recipient's company.
4. Public-safe Markdown/PDF/plain spreadsheet; no macros/executables.
5. One problem, one artifact, one optional next question.
6. Cite the public signal that caused the artifact to be relevant.
7. Prefer a checklist/calculator/sample policy over a generic portfolio link.

## Hyperpersonalized kit shape

```yaml
target: <company>
persona: <role, not guessed private identity>
public_signal: <source + date>
pain_hypothesis: <explicitly marked hypothesis>
value_metric: <headcount | margin | cycle | risk | spend | revenue>
two_minute_gift: <K#>
proof_bridge: <one accepted operator capability>
message:
  observation: <one sentence based on public evidence>
  usefulness: <one sentence about the artifact>
  ask: <small question / permission to send / 15-minute discovery>
falsifier: <what would make this angle wrong>
status: OPERATOR_REVIEW_REQUIRED
```

## Daily standard work

- 2 high-fit job applications.
- 1 contract/channel proposal candidate.
- 1 Dream-50 relationship touch, hiring or not.
- 1 company/problem research card.
- No automatic send/apply.

## Weekly standard work

- 2–3 warm practice discovery conversations.
- Add/promote at least 5 researched Dream-50 accounts.
- Review attempts → replies → meetings → qualified pains → proposals → interviews → paid receipts.
- Revise after external evidence, not after internal aesthetic debate.

## Outreach anti-patterns

- Do not say "I build AI agents" before establishing a problem.
- Do not attach five unrelated demos.
- Do not invent company pain from a job description.
- Do not mass-send the same message with a company-name token swapped.
- Do not count a connection acceptance as buyer validation.
- Do not negotiate price before a consequence/baseline exists.
- Do not hide behind more research when a safe, reviewable outreach experiment is ready.

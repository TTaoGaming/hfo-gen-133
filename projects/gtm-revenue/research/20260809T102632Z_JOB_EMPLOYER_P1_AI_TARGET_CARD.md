# S08 GTM Target Card — P-1 AI

```yaml
schema_id: hfo.gen133.gtm.target_card.v1
target: P-1 AI
species: JOB_EMPLOYER
vertical: physical-engineering AI / agentic systems / evaluation infrastructure
evidence_digest_sha256: ad614001427f98b61633c6e3999b5b8e39d352ef06ff6e34fa5977adfa496d2c
verified_utc: 2026-08-09T10:26:32Z
route: APPLY_NOW_OPERATOR_REVIEWED
privacy: PUBLIC_SAFE_SYNTHETIC_ONLY
world_effect_ceiling: T0_PREP_RESEARCH_GIT
verifier: S04
next_consumer: S07
next_workitem: S07_P1_AI_EVAL_REGRESSION_PROMOTION_CARD_V1
expiry_utc: 2026-08-14T14:08:00Z
send_authority: NONE
```

## Target + current signal

P-1 AI is building Archie, an AI engineer for physical-world engineering. Its current **AI Evals Lead** opening is remote in the United States, full time, with **$170K–$200K base plus equity**. The role owns the system for organizing, transforming, running, grading, and reporting eval benchmarks; the process for developing and QA'ing evals with engineering experts and industrial partners; CI/CD-based continuous benchmarking; detection of hallucinations, undesirable stochasticity, and regressions; and consistent automated-test implementation across the stack.

The same company currently lists a **Forward Deployed Engineer** role at **$170K–$220K plus equity**, remote US/Canada or San Mateo, responsible for customer deployments, production integrations, production evaluation criteria, measurable customer value, and live-deployment root-cause work. Together these are a direct hiring signal that production agent evaluation and customer deployment are active operating surfaces. They do **not** prove a current eval bottleneck.

Source publication dates are not exposed on the Ashby pages; both listings were verified current on 2026-08-09.

Sources:
- 2026-08-09 verified current — https://jobs.ashbyhq.com/P-1%20AI/cd5af605-45a8-4951-b7be-92771b9deec8/
- 2026-08-09 verified current — https://jobs.ashbyhq.com/p-1%20ai/3032d125-a3f5-439f-a541-e6a38127f949

## Persona / bridge

**Best buyer-user persona:** Core Engineering / AI Evals hiring owner accountable for trustworthy model-agent regression detection and CI release evidence, with physical-engineering SMEs and industrial-partner evaluators as key users/contributors.

**Named public bridge:** `NONE_SOURCE_BACKED_FOR_THIS_ROLE`. The official job source does not name the hiring manager. The interview process includes a CEO interview, but no person is named in the source, so no bridge identity is inferred.

## Expensive-pain hypothesis

**Hypothesis:** As Archie gains skills and customer-specific engineering capability, P-1 AI *may* consume material senior-engineer / domain-expert time per candidate model-agent revision converting physical-engineering expectations into reliable evals, QA'ing those evals, interpreting stochastic failures, and deciding whether a revision is safe enough to advance.

**Primary measurable value metric:** **expert + engineer reviewer hours per accepted model/agent revision**.

**Secondary metric:** elapsed time from candidate agent/model revision to a trustworthy CI-backed promote/hold decision.

This is a hypothesis. The current sources establish that P-1 AI is hiring a dedicated eval owner and expects continuous benchmarking; they do not establish that current review cost or cycle time is excessive.

## Evidence for / against

**For**
- P-1 AI is hiring a dedicated AI Evals Lead whose scope explicitly includes benchmark organization, grading/reporting, eval QA, CI/CD integration, hallucination/stochasticity/regression detection, and coordination with engineering experts and industrial partners.
- Its FDE role explicitly sources evaluation criteria from customer work, evaluates AI systems in production, and troubleshoots live deployments, creating a plausible flow of domain-specific eval requirements into the core platform.
- The stated need to compare successive generations and continuously benchmark an evolving AI platform makes revision-bound evidence directly relevant.

**Against**
- The job itself is evidence that P-1 AI is already investing in this capability; the dedicated hire may close the exact gap a proof artifact would target.
- The sources do not report failed releases, excessive expert-review cost, evaluation incidents, customer dissatisfaction, or a missing release-gate system.
- Physical-engineering evals may require proprietary customer data, simulations, CAD/tool environments, and domain expertise that a public synthetic proof cannot reproduce.

## S07 two-minute utility gift

**`S07_P1_AI_EVAL_REGRESSION_PROMOTION_CARD_V1` — Engineering-Agent Eval Revision Card: Skill × Regression × Stochasticity × Evidence × CI**

Input one tiny synthetic before/after eval run for an agent revision. Output only:
- newly passed / newly failed held-out skills;
- variance across repeated runs;
- one hallucination / unsupported-claim check;
- evidence provenance and grader version;
- exact candidate revision identifier;
- CI status;
- `PROMOTE | HOLD | REJECT` plus the smallest missing-evidence reason.

The gift should be readable in about two minutes and must not imply knowledge of Archie's proprietary eval stack.

## Deeper proof artifact

Build a **public-safe synthetic engineering-agent eval promotion harness** using invented engineering tasks and fixture tool outputs only. Include:
- held-out benchmark slices with immutable task IDs;
- deterministic expected-invariant checks plus model/LLM graders kept separate;
- repeated-run stochasticity measurement;
- regression comparison across two agent revisions;
- failure injection for unsupported claims, wrong tool selection, stale evidence, grader drift, and missing artifacts;
- a CI-style release verdict bound to exact eval-set + grader + agent revision digests;
- optional OPA/Rego-style policy for hard promotion constraints;
- trace and cost/latency summaries only where synthetic fixtures support them.

No P-1 account, customer data, proprietary engineering data, live deployment, or production-performance claim.

## Route / falsifier / ceiling

**Route:** `APPLY_NOW_OPERATOR_REVIEWED`. The role is live, remote US, and unusually aligned with held-out testing, evals, regression detection, CI/CD, and agent reliability. Application submission remains operator-only.

**Strongest falsifier:** downgrade to `RELATIONSHIP_ONLY` or drop if the operator cannot truthfully show **hands-on ownership of comprehensive software/AI test suites, metric design across successive system generations, Python, and CI/CD**. Separately, kill the proof-kit wedge if P-1 AI already has a low-overhead revision-bound promotion artifact covering held-out skills, stochasticity, grader/evidence provenance, regression deltas, and CI verdicts.

**Privacy/effect ceiling:** public sources + synthetic data only; Git research/proof preparation only. No account creation, application submission, outreach, private/customer data, deployment, purchase, or publication.

## Honest flaw

The target is technically high-fit but has a **domain-transfer risk**: P-1's eval problem is grounded in physical engineering and industrial-partner expertise, while a generic LLM-agent eval artifact can easily become superficial. The proof earns fitness only if S07 demonstrates a rigorous *eval-system pattern* without pretending to know Archie's proprietary tasks, and an application still needs credible evidence of leading real test/eval systems rather than architecture-only work.

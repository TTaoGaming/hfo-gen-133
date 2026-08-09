# Engineering-Agent Eval Revision Card
**Skill × Regression × Stochasticity × Evidence × CI**

> **Plausible problem:** an agent revision can look better on average while silently losing a held-out skill, becoming more variable across repeated runs, or passing through a grader/eval change that makes the comparison non-like-for-like. This card compresses one before→after revision decision into a reviewable `PROMOTE | HOLD | REJECT` record.

```yaml
schema_id: hfo.gen133.gtm.proof_kit.v1
target: P-1 AI
work_item: S07_P1_AI_EVAL_REGRESSION_PROMOTION_CARD_V1
privacy: PUBLIC_SAFE_SYNTHETIC_ONLY
effect_ceiling: T0_PREP_RESEARCH_GIT
artifact_kind: held-out eval / release-gate checklist
```

## WHY_THIS_MAY_MATTER

**Source-backed facts:** P-1 AI's current AI Evals Lead role owns benchmark organization, transformation, execution, grading/reporting, eval QA with engineering experts and industrial partners, CI/CD-based continuous benchmarking, and methods for detecting hallucinations, undesirable stochasticity, and regressions. Its current Forward Deployed Engineer role also sources evaluation criteria from customer work and evaluates AI systems in production.

**Hypothesis, not a claim about P-1 AI:** as an engineering agent gains skills and customer-specific capability, reviewers may benefit from a tiny revision-bound artifact that separates real skill gains from regressions, run-to-run variance, grader drift, and incomplete CI evidence. The sources do **not** establish that P-1 AI currently lacks such a mechanism or has excessive review cost.

## HOW_TO_USE_IN_2_MINUTES

1. Bind the exact baseline revision, candidate revision, held-out eval-set digest, grader/version, and CI run.
2. Fill only the delta rows below. Keep deterministic checks separate from model/LLM-graded checks.
3. Apply the verdict rule. Missing evidence is `HOLD`; a blocking deterministic regression or unsupported-claim failure is `REJECT`; `PROMOTE` requires complete evidence and no blocking regression.

## REVISION CARD

| Field | Evidence |
|---|---|
| Baseline revision | `________________` |
| Candidate revision | `________________` |
| Held-out eval-set ID + digest | `________________` |
| Deterministic checker version | `________________` |
| Model/LLM grader + prompt/version | `________________` |
| Repeated runs per stochastic task | `________________` |
| CI run / commit | `________________` |

### Delta only

| Check | Baseline | Candidate | Decision signal |
|---|---:|---:|---|
| Newly passed held-out skills | `__` | `__` | informational gain |
| Newly failed held-out skills | `__` | `__` | any blocking skill loss → `REJECT` or owner-approved exception |
| Repeated-run success distribution | `__` | `__` | variance beyond the owner-set envelope → `HOLD` |
| Unsupported/hallucinated claim sentinel | `__` | `__` | candidate failure → `REJECT` |
| Wrong-tool / invalid-tool-selection sentinel | `__` | `__` | candidate failure → `REJECT` if task-critical |
| Evidence-provenance completeness | `__` | `__` | missing task/grader/revision binding → `HOLD` |
| CI status | `__` | `__` | incomplete/failing required checks → `HOLD` |
| Grader changed since baseline? | `Y/N` | `Y/N` | changed without re-baselining → `HOLD` |

### Smallest sufficient verdict

```text
PROMOTE = all required evidence bound + CI green + no blocking regression +
          stochasticity within an owner-defined envelope.

HOLD    = evidence incomplete, non-like-for-like comparison, grader/eval drift,
          unresolved stochasticity, or required CI not complete.

REJECT  = confirmed blocking regression, unsupported-claim sentinel failure,
          or other owner-designated hard invariant failure.
```

**Verdict:** `PROMOTE | HOLD | REJECT`

**Smallest missing-evidence / rejection reason:** `________________________________________`

## HELD-OUT NEGATIVE CONTROLS

Use at least one task for each control that matters to the release. Synthetic fixtures are enough for a public proof.

- **Unsupported claim:** fixture omits a required engineering fact; agent must say evidence is insufficient rather than invent it.
- **Wrong tool:** a plausible but invalid tool is available; agent must select the task-appropriate tool or abstain.
- **Stale evidence:** an older fixture conflicts with a revision-bound current fixture; current evidence must win.
- **Skill regression:** candidate improves one headline skill but loses a previously passing held-out skill.
- **Grader drift:** same answer is graded under a modified rubric/prompt; comparison must be held until re-baselined.
- **Missing artifact:** candidate output exists but trace/eval-set/grader/revision identity is absent; verdict must be `HOLD`.

## EVIDENCE LINKS

Verified current on **2026-08-09**:

- P-1 AI — AI Evals Lead: https://jobs.ashbyhq.com/P-1%20AI/cd5af605-45a8-4951-b7be-92771b9deec8/
- P-1 AI — Forward Deployed Engineer: https://jobs.ashbyhq.com/p-1%20ai/3032d125-a3f5-439f-a541-e6a38127f949
- P-1 AI — AI Engineer: https://jobs.ashbyhq.com/p-1%20ai/b4f5f7d9-6c7f-463c-ba6d-cde8c245f1c8

The third source is corroborative: it says AI engineers regularly run evaluations/tests and analyze production traces; it is not evidence that this exact card is missing.

## ASSUMPTIONS

- Revision identity, eval-set identity, grader identity, and CI status can be bound to immutable or reviewable identifiers.
- Domain owners define which skill regressions are blocking and what stochasticity envelope is acceptable.
- Deterministic invariants stay separate from probabilistic/model-graded judgments.
- This public artifact uses no Archie internals, customer data, proprietary engineering tasks, or production measurements.

## FALSIFIER

Kill this proof-kit wedge if P-1 AI already has a low-overhead revision-bound view that exposes held-out skill deltas, repeated-run stochasticity, grader/evidence provenance, CI status, and hard promotion blockers. Separately, an application should be downgraded if the operator cannot truthfully demonstrate hands-on ownership of comprehensive software/AI test suites, cross-generation metric design, Python, and CI/CD.

## OPTIONAL OPERATOR-REVIEWED OUTREACH NOTE — NO SEND

I saw the AI Evals Lead role and made a tiny public-safe revision card for the exact eval surface you describe: held-out skill deltas, repeated-run stochasticity, grader provenance, unsupported-claim controls, and CI-bound promote/hold logic. It uses only synthetic fixtures and makes no assumptions about Archie's internal stack. If useful, I can share the one-page pattern; no response needed if your existing eval pipeline already covers this cleanly.

---

**Honest limitation:** this is an eval-system pattern, not a physical-engineering benchmark. It demonstrates release-evidence structure only; it does not demonstrate domain expertise, P-1 AI performance, or production outcomes.

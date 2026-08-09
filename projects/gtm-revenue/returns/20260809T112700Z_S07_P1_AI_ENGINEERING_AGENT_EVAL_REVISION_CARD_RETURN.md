# S07 Producer Return — P-1 AI Engineering-Agent Eval Revision Card

```yaml
schema_id: hfo.gen133.gtm.producer_return.v1
result: KIT_RETURNED
producer: S07_GTM_PROOF_KIT_BUILDER
producer_task_id_expected: 6a506f6dc5c08191b95f1707d7f00c2d
producer_task_id_observed: 6a506f6dc5c08191b95f1707d7f00c2d
producer_task_id_match: true
wip: 1
work_item: S07_P1_AI_EVAL_REGRESSION_PROMOTION_CARD_V1
target: P-1 AI
route: APPLY_NOW_OPERATOR_REVIEWED
privacy: PUBLIC_SAFE_SYNTHETIC_ONLY
producer_effect_ceiling: T0_PREP_RESEARCH_GIT
verifier: S04_HRIST_STRUCTURAL_PREFLIGHT
verifier_binding_weight: 0
consumer_after_s04: S03_REDUCER_THEN_OPERATOR
final_consumer: OPERATOR
expiry_utc: 2026-08-14T14:08:00Z
send_status: NO_SEND
application_status: NO_SUBMIT
deployment_status: NO_DEPLOY
merge_status: NO_MERGE
external_publication_status: NONE
```

## SELF_PROBE

- Task identity matched the expected S07 carrier ID.
- GitHub exact-file read, exact-commit read, code search, create-file, and readback were available.
- Fresh public-source verification was available.
- No task mutation, account action, paid provider call, deployment, merge, private-data use, or self-verification occurred.

## TARGET BINDING

- Target card: `projects/gtm-revenue/research/20260809T102632Z_JOB_EMPLOYER_P1_AI_TARGET_CARD.md`
- Target card Git blob SHA-1: `e7fa5f3c683edde861e54d8e2f6e84230938f147`
- Target card create commit: `b2a16f3cd3108106ea613225eb06ece132ec58f7`
- S08 declared evidence digest SHA-256: `ad614001427f98b61633c6e3999b5b8e39d352ef06ff6e34fa5977adfa496d2c`
- Exact fetched target-card UTF-8 bytes: `7496`
- Exact fetched full-file SHA-256: `5ee3d46586ac9ff683df50e12ceddb666e89b9f3d56c4b9452a237899039f3a2`
- Digest caveat: S08 does not bind the canonical evidence preimage/canonicalization for its declared evidence digest. The declared digest is therefore bound here as S08 metadata, **not** claimed independently reproducible or equal to the full-file SHA-256.
- Duplicate guard: bounded exact-digest repository search before build returned the target card only; no prior kit carrying the same declared target-card evidence digest was observed. Search absence is not global proof.

## CANDIDATE

- Path: `projects/gtm-revenue/kits/p1-ai/20260809T112400Z_ENGINEERING_AGENT_EVAL_REVISION_CARD.md`
- Kind: held-out eval / release-gate checklist
- Create commit: `986d55237e50541ea48fcb17395da55db84ed85d`
- Readback Git blob SHA-1: `2e29345b06ece0f6ecfec01aee34345cda21046a`
- Exact readback UTF-8 bytes: `6902`
- Exact readback SHA-256: `1c97b2ecc5b77cf456d3e3c57f7aa4625209971fd8723992b43743d5d5f9c5a3`
- Readback status: exact authored bytes observed after repository write.

## CHANGED PATHS

1. `projects/gtm-revenue/kits/p1-ai/20260809T112400Z_ENGINEERING_AGENT_EVAL_REVISION_CARD.md`
2. `projects/gtm-revenue/returns/20260809T112700Z_S07_P1_AI_ENGINEERING_AGENT_EVAL_REVISION_CARD_RETURN.md`

## PUBLIC SOURCE VERIFICATION

Verified current on 2026-08-09 from official P-1 AI Ashby job pages:

1. https://jobs.ashbyhq.com/P-1%20AI/cd5af605-45a8-4951-b7be-92771b9deec8/
   - AI Evals Lead; remote US; $170K–$200K plus equity.
   - Scope includes benchmark organization/transformation/execution/grading/reporting; eval QA with engineering experts and industrial partners; CI/CD continuous benchmarking; detection/testing of hallucinations, undesirable stochasticity, and regressions; automated-test consistency.
2. https://jobs.ashbyhq.com/p-1%20ai/3032d125-a3f5-439f-a541-e6a38127f949
   - Forward Deployed Engineer; remote US; $170K–$220K plus equity.
   - Scope includes production customer integrations, sourcing evaluation criteria from customer work, evaluating AI systems in production, and live-deployment root-cause work.
3. https://jobs.ashbyhq.com/p-1%20ai/b4f5f7d9-6c7f-463c-ba6d-cde8c245f1c8
   - AI Engineer; current listing states regular evaluations/tests and production-trace analysis.
   - Corroborative only; it does not prove this promotion-card pattern is missing.

## PAIN-HYPOTHESIS CEILING / PERSONA

**Best persona:** Core Engineering / AI Evals hiring owner responsible for trustworthy regression detection and CI-backed release evidence, with physical-engineering SMEs and industrial partners as contributors.

**Source-backed:** P-1 AI is actively hiring dedicated eval ownership around continuous benchmarking, cross-generation metrics, hallucination/stochasticity/regression detection, and CI/CD.

**Hypothesis only:** reviewer effort per accepted agent/model revision and elapsed time to a trustworthy promote/hold decision may be material. No source establishes excessive reviewer hours, a missing release gate, failed releases, customer dissatisfaction, or a current eval bottleneck.

## S02 ADMISSION STATUS

Bounded exact-WorkItem search for `S07_P1_AI_EVAL_REGRESSION_PROMOTION_CARD_V1` observed only the S08 target card. No immutable S02 admission claim path/blob, acceptance digest, claim idempotency digest, or lease/expiry was observed. This is recorded as a structural debt, not converted into an absence proof and not fabricated by S07.

## ROUTE TO S04

**S04 Hrist Structural Preflight:** verify the candidate and this producer return unchanged. S07 does not self-verify. Expected structural outcome may be `REVISE` if the current S04 contract requires an immutable S02 admission claim and independently reproducible S08 evidence-digest preimage before acceptance.

## NO-SEND / AUTHORITY

No autonomous email, LinkedIn message, DM, application submission, account creation, terms acceptance, spend, paid provider call, deployment, merge, external publication, private-data use, malware/exploit work, or task mutation occurred.

The optional outreach note inside the candidate is explicitly operator-review-only and remains unsent.

## ROLLBACK / DELETE PATH

- Candidate: if the operator decides it should not remain, remove `projects/gtm-revenue/kits/p1-ai/20260809T112400Z_ENGINEERING_AGENT_EVAL_REVISION_CARD.md` only through a later operator-controlled Git commit; Git history remains.
- Producer return: immutable append-only record. If incorrect, supersede with a new return; do not rewrite this return.

## HONEST FLAW

The artifact demonstrates an eval-release evidence pattern, not physical-engineering competence. P-1 AI's actual evals may depend on proprietary CAD/tool environments, simulations, customer data, and domain-expert judgment that a synthetic public card cannot reproduce. Separately, the live role asks for hands-on ownership of comprehensive test suites, cross-generation metric design, Python, and CI/CD; this proof-kit cannot manufacture missing career evidence. Finally, the missing observed S02 admission binding and non-reproducible S08 declared evidence digest can legitimately block downstream structural acceptance even though the utility itself is public-safe and relevant.

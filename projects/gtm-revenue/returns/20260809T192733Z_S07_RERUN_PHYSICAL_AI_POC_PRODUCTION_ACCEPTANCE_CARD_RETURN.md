# S07 Producer Return — Rerun Physical-AI POC → Production Acceptance Card

```yaml
schema_id: hfo.gen133.s07_gtm_producer_return.v1
result: KIT_RETURNED
producer: S07_GTM_PROOF_KIT_BUILDER
producer_task_id: 6a506f6dc5c08191b95f1707d7f00c2d
wip: 1
valid_time_utc: 2026-08-09T19:27:33Z
expiry_utc: 2026-08-14T14:08:00Z
canonical_repository: TTaoGaming/hfo-gen-133
canonical_branch: agent/gen133-bootstrap-20260730
effect_ceiling: T0_PREP_RESEARCH_GIT
privacy: PUBLIC_SAFE_SYNTHETIC_ONLY
send_authority: NONE
verifier: S04_HRIST_STRUCTURAL_PREFLIGHT
verifier_task_id: 6a52861fbdb08191b9ef33a0b9c3c15c
consumer: OPERATOR_CONTROLLED_GTM_REVIEW
consumer_workitem: S07_RERUN_PHYSICAL_AI_POC_PRODUCTION_ACCEPTANCE_CARD_V1
self_verification: NOT_PERFORMED
```

## Selection binding

- Target: `Rerun`
- Species: `JOB_EMPLOYER`
- Route: `APPLY_NOW_OPERATOR_REVIEWED`
- Target card: `projects/gtm-revenue/research/20260809T182900Z_JOB_EMPLOYER_RERUN_TARGET_CARD.md`
- Target-card Git blob SHA-1: `68810f73fe10e7071c5cc4c4e7cbb333f55c7201`
- Target-card source commit observed: `f2b9607143d172cde16ceb7b37054565a838ca85`
- Declared target evidence digest: `a06a9b22b3952c3205466c79eb1e19adb813afe563969aee5cfd638c6395dcbc`
- Digest method declared by S08: `sha256(canonical_source_manifest_utf8)`
- Bounded duplicate checks: exact-digest code search returned no result; commit search for `Rerun` returned only the S08 target-card commit before this build. This is bounded evidence, not global absence proof.

### Target evidence-digest recomputation

Canonicalization used: `UTF8_EXACT_PREIMAGE_NO_TERMINAL_LF`.

```text
2026-08-09|https://jobs.ashbyhq.com/rerun/ee28fed0-9ada-40ac-b828-f1ed633f60e6|LIVE_FORWARD_DEPLOYED_ENGINEER_REMOTE_US_WEST_COAST
2026-08-09|https://rerun.io/docs/overview/what-is-rerun|CURRENT_PRODUCT_OVERVIEW
2026-08-09|https://rerun.io/docs/getting-started|CURRENT_GETTING_STARTED
```

- Canonical manifest UTF-8 bytes: `284`
- Recomputed SHA-256: `a06a9b22b3952c3205466c79eb1e19adb813afe563969aee5cfd638c6395dcbc`
- Declared/recomputed match: `true`

## Candidate binding

- Candidate: `projects/gtm-revenue/kits/rerun/20260809T192700Z_PHYSICAL_AI_POC_PRODUCTION_ACCEPTANCE_CARD.md`
- Candidate create commit: `1995eee65c5d3780969ce8ca8d5efb3e37add06c`
- Candidate Git blob SHA-1 after branch readback: `7e01c3b650bcb4f7d461991e976d8ce72b6b909d`
- Candidate UTF-8 bytes: `6424`
- Candidate SHA-256: `2376f1299ae5e490c7a3642de84b49d7b9e971263b468237b2940afbc94d80b4`
- Form: `PHYSICAL_AI_POC_TO_PRODUCTION_ACCEPTANCE_CARD`
- Decision vocabulary inside candidate: `PROMOTE | HOLD | REJECT`

The candidate is intentionally Rerun-shaped rather than a generic LLM-agent governance artifact. It binds recording identity, ingest/time integrity, schema compatibility, query invariants, visual/debug behavior, resource envelope, exact revision provenance, and rollback, plus held-out synthetic negative controls.

## Public-source verification

Fresh public verification was performed on `2026-08-09`. Exact source URLs bound to this return:

1. https://jobs.ashbyhq.com/rerun/ee28fed0-9ada-40ac-b828-f1ed633f60e6
2. https://rerun.io/docs/overview/what-is-rerun
3. https://rerun.io/docs/getting-started
4. https://rerun.io/docs/howto/query-and-transform/overview
5. https://rerun.io/docs/concepts/how-does-rerun-work

Source-backed ceiling preserved:
- The live FDE role is Remote US, West Coast, User Space, and describes work from first demo through production, POC delivery, roadmap feedback, and improving POC/onboarding cycles.
- Current Rerun docs cover multi-rate multimodal logging/ingest, visualization, query/transform, catalogs, and training.
- Current Rerun docs state the open-source catalog server is API-compatible with Rerun Hub.
- No source reviewed here establishes excessive POC cycle time, integration regressions, incidents, reviewer burden, savings, or missing production controls.

Pain hypothesis ceiling:
- `HYPOTHESIS_ONLY`: Rerun FDEs and customer engineers may benefit from one low-overhead revision-bound acceptance card for POC-to-production handoffs.
- Primary value metric if tested: FDE + customer-engineer hours per accepted handoff.
- Secondary value metric if tested: calendar days from first working POC to production acceptance.
- No baseline or target value is claimed.

Best persona:
- Rerun User Space / Forward Deployed Engineering hiring leadership responsible for customer POCs and onboarding.
- Secondary user: customer robotics/data engineers moving an integration from exploratory use to repeatable production use.
- Named bridge: `NONE_SOURCE_BACKED_FOR_THIS_ROLE`; no person was inferred.

## Allowed / forbidden effects

Allowed path used:
- `projects/gtm-revenue/kits/rerun/`
- `projects/gtm-revenue/returns/`

Changed paths:
- `projects/gtm-revenue/kits/rerun/20260809T192700Z_PHYSICAL_AI_POC_PRODUCTION_ACCEPTANCE_CARD.md`
- `projects/gtm-revenue/returns/20260809T192733Z_S07_RERUN_PHYSICAL_AI_POC_PRODUCTION_ACCEPTANCE_CARD_RETURN.md`

Status:
- `NO_SEND`
- `NO_EMAIL`
- `NO_LINKEDIN`
- `NO_DM`
- `NO_APPLICATION_SUBMISSION`
- `NO_ACCOUNT_CREATION`
- `NO_TERMS_ACCEPTANCE`
- `NO_SPEND`
- `NO_PAID_PROVIDER_CALL`
- `NO_DEPLOY`
- `NO_MERGE`
- `NO_PUBLICATION_OUTSIDE_OPERATOR_REPO`
- `NO_PRIVATE_DATA`
- `NO_SELF_VERIFICATION`

## Rollback / delete path

If S04 or the operator rejects the candidate, a later operator-controlled commit may delete only:

`projects/gtm-revenue/kits/rerun/20260809T192700Z_PHYSICAL_AI_POC_PRODUCTION_ACCEPTANCE_CARD.md`

Preserve this immutable producer return and Git history. No destructive rollback was performed by S07.

## Route to verifier

Route the exact candidate bytes above to **S04 Hrist Structural Preflight**. S07 does not grade its own artifact. S04 same-provider structural review is nonbinding and cannot substitute for independent verification.

## S02 admission state

A bounded repository/commit search did not observe an immutable S02 admission claim for exact WorkItem `S07_RERUN_PHYSICAL_AI_POC_PRODUCTION_ACCEPTANCE_CARD_V1`. This is not asserted as global absence. No S02 claim path/blob, acceptance digest, claim-idempotency digest, or lease is fabricated or bound here. S04 may therefore return `REVISE` under the current structural contract even though the S08 target evidence digest is now independently reproducible.

## Honest flaw

The largest flaw is domain-transfer and applicant-evidence risk, not artifact syntax. Rerun's role is physical-AI/robotics data infrastructure and asks for a credible robotics/ML/data-engineering/database foundation, working Python, customer POC delivery, West-Coast-US fit, and roughly 30% travel. This one-page acceptance card cannot prove those qualifications, cannot prove Rerun needs an external acceptance layer, and may be redundant if Rerun already has a low-overhead production-handoff mechanism covering the same evidence.

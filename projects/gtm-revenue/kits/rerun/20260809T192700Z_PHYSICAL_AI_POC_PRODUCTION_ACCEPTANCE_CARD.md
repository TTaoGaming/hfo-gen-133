# Rerun Physical-AI POC → Production Acceptance Card

**Recipient problem:** a customer POC can look good in a demo yet still be hard to accept for production if the exact recording fixture, schema behavior, query results, visual/debug expectations, resource envelope, revision identity, and rollback target are not reviewed together.

## WHY_THIS_MAY_MATTER

**Source-backed facts:** Rerun's current Forward Deployed Engineer role owns customer work from first demo through production, asks the hire to stand up working POCs, and to make each POC/onboarding better than the last. Rerun's current docs span logging/ingest, visualization, querying/transforms, catalogs, and training on multi-rate multimodal robotics data. The open-source catalog server is documented as API-compatible with Rerun Hub.

**Hypothesis, not a reported Rerun problem:** a lightweight acceptance card may reduce review ambiguity when one customer integration revision changes across those surfaces. No public source reviewed here establishes that Rerun has excessive POC cycle time, integration regressions, customer incidents, or missing production controls.

## HOW_TO_USE_IN_2_MINUTES

1. Pick one exact integration revision and one representative public-safe or customer-approved recording fixture.
2. Fill only the eight evidence cells below. Use links/hashes where possible; do not substitute prose for missing evidence.
3. Return `PROMOTE`, `HOLD`, or `REJECT`. `PROMOTE` requires all required gates to pass and a known rollback target.

| Gate | Evidence to bind | PASS condition | HOLD / REJECT trigger |
|---|---|---|---|
| 1. Recording identity | fixture name + SHA-256 + capture/schema version | exact fixture is reproducible | missing/stale fixture → HOLD |
| 2. Ingest & time integrity | expected vs observed streams/frames; timestamp checks | required streams present; no unexplained gaps/drift | missing frames, partial recording, timestamp drift → REJECT |
| 3. Schema compatibility | required entities/components/columns + version delta | required fields remain readable or migration is explicit | silent field/type break → REJECT |
| 4. Query invariants | 2–3 deterministic dataframe/SQL assertions | baseline and candidate agree within declared tolerance | semantic/query regression → REJECT |
| 5. Visual/debug behavior | one saved expected view/annotation condition | required objects/annotations/time alignment remain inspectable | broken alignment or required view unavailable → HOLD/REJECT |
| 6. Resource envelope | ingest/query wall time and peak memory on named fixture/hardware | within predeclared envelope | envelope exceeded without accepted reason → HOLD |
| 7. Revision provenance | SDK/app/config commit or package versions | exact candidate bytes/config are identifiable | "latest" or mutable dependency only → HOLD |
| 8. Rollback | last-known-good revision + rollback check | rollback target exists and fixture replays | missing or untested rollback target → HOLD |

### Decision rule

- `PROMOTE` — all required gates pass; no unexplained regression; rollback target is known.
- `HOLD` — evidence is incomplete, stale, non-reproducible, or a resource/visual deviation needs explicit acceptance.
- `REJECT` — representative data is lost/corrupted, schema/query semantics regress beyond tolerance, or rollback cannot restore the accepted baseline.

### Minimal held-out negative controls

Before trusting the card, inject at least one synthetic failure from each relevant class:

- drop a camera frame or LiDAR chunk;
- offset one stream's timestamps;
- rename or change the type of one required field;
- perturb one deterministic query result;
- remove one required annotation/view condition;
- breach a declared latency or memory ceiling;
- point provenance at the wrong revision;
- point rollback at a non-replaying baseline.

The gate is useful only if these failures change the decision away from `PROMOTE`.

## SOURCE-BACKED FACTS VS HYPOTHESES

**Facts supported by current public sources**
- The live role is Forward Deployed Engineer, Remote US — West Coast, in User Space.
- The role describes customer work from first demo through production, working POCs, and improving POC/onboarding cycles.
- Rerun documents one data layer spanning log/ingest, visualization, query/transform, catalog workflows, and training.
- Rerun documents the open-source catalog server as API-compatible with Rerun Hub.

**Unverified hypotheses / assumptions**
- Rerun currently spends material engineering hours on repetitive POC acceptance.
- The eight-gate card would reduce those hours or shorten calendar time.
- Visual-state assertions are practical for every customer workflow.
- A single representative recording adequately covers production risk.

## EVIDENCE LINKS

- https://jobs.ashbyhq.com/rerun/ee28fed0-9ada-40ac-b828-f1ed633f60e6
- https://rerun.io/docs/overview/what-is-rerun
- https://rerun.io/docs/getting-started
- https://rerun.io/docs/howto/query-and-transform/overview
- https://rerun.io/docs/concepts/how-does-rerun-work

## ASSUMPTIONS

This card assumes the reviewer can name one representative recording, a small set of required schema/query invariants, a meaningful resource envelope, and a last-known-good revision. It does not substitute for Rerun's own testing, customer acceptance criteria, hardware-in-the-loop validation, safety validation, or production SLOs.

## FALSIFIER

Kill this wedge if Rerun already has a low-overhead standard acceptance mechanism that binds representative recordings, schema/query invariants, visual/debug behavior, resource bounds, exact revision identity, and rollback for each POC-to-production handoff. Also drop the job route if the operator cannot truthfully substantiate the role's robotics/ML/data-engineering/database foundation, working Python, customer-facing POC delivery, West-Coast-US fit, or roughly 30% travel.

## OPTIONAL OPERATOR-REVIEWED OUTREACH NOTE — NO SEND

I noticed the FDE role is explicitly about moving messy customer problems from first demo through production. I made a one-page POC→production acceptance card shaped around Rerun's recording, schema, query, visualization, resource, provenance, and rollback surfaces. It is intentionally a review aid rather than a claim that Rerun is missing these controls; if your existing process already binds the same evidence, the card should be discarded.

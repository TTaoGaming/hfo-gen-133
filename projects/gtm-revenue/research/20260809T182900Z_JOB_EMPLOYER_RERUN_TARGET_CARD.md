# S08 GTM Target Card — Rerun

```yaml
schema: hfo.gen133.gtm.target_card.v1
target: Rerun
species: JOB_EMPLOYER
vertical: Physical AI / robotics multimodal-data infrastructure / developer tooling
valid_time_utc: 2026-08-09T18:29:00Z
expiry_utc: 2026-08-14T14:08:00Z
evidence_digest: a06a9b22b3952c3205466c79eb1e19adb813afe563969aee5cfd638c6395dcbc
evidence_digest_method: sha256(canonical_source_manifest_utf8)
route: APPLY_NOW_OPERATOR_REVIEWED
privacy: PUBLIC_SAFE_SYNTHETIC_ONLY
world_effect_ceiling: T0_PREP_RESEARCH_GIT
verifier: S04
next_consumer: S07
consumer_workitem: S07_RERUN_PHYSICAL_AI_POC_PRODUCTION_ACCEPTANCE_CARD_V1
send_authority: NONE
```

## Current signal

Rerun has a current **Forward Deployed Engineer** opening for **Remote US, West Coast** in its User Space team. The role says the engineer will work with customers from first demo through production, turn messy customer problems into working POCs, relay customer struggles into the roadmap, and improve each POC/onboarding cycle. It asks for a technical foundation in robotics, ML, data engineering, or databases; working Python; interest in robotics/spatial AI/computer vision; and comfort with roughly 30% travel. The same company-authored role says Rerun Hub is in private preview managing petabytes of data and that demand is strong; treat those as company claims, not independently verified measurements.

Current Rerun documentation positions the product as a unified data layer for multi-rate, multimodal robotics data spanning logging/ingest, visualization, query/transform, cataloging, and training. The open-source catalog server is API-compatible with the commercial Rerun Hub, which is the scaled backend for collaborative data management.

## Primary sources

- `verified 2026-08-09` — https://jobs.ashbyhq.com/rerun/ee28fed0-9ada-40ac-b828-f1ed633f60e6
- `verified 2026-08-09` — https://rerun.io/docs/overview/what-is-rerun
- `verified 2026-08-09` — https://rerun.io/docs/getting-started

Canonical evidence manifest used for digest:

```text
2026-08-09|https://jobs.ashbyhq.com/rerun/ee28fed0-9ada-40ac-b828-f1ed633f60e6|LIVE_FORWARD_DEPLOYED_ENGINEER_REMOTE_US_WEST_COAST
2026-08-09|https://rerun.io/docs/overview/what-is-rerun|CURRENT_PRODUCT_OVERVIEW
2026-08-09|https://rerun.io/docs/getting-started|CURRENT_GETTING_STARTED
```

## Buyer / user persona and public bridge

Best persona: Rerun **User Space / Forward Deployed Engineering hiring leadership** responsible for customer POCs, onboarding, and the handoff from field learning into product/engineering. Secondary users are customer robotics/data engineers trying to move a Rerun integration from exploratory use to a repeatable production workflow.

Named public bridge: `NONE_SOURCE_BACKED_FOR_THIS_ROLE`. The current primary sources do not identify the hiring owner, so no person is inferred.

## Expensive-pain hypothesis

**Hypothesis:** as Rerun expands customer POCs across heterogeneous robotics and spatial-AI stacks, Rerun FDEs and customer engineers may spend material time per accepted POC-to-production handoff proving that representative recordings still ingest correctly, schemas remain compatible, queries/transforms preserve required behavior, visualization/debugging expectations remain intact, and the exact integration revision is reproducible and rollback-ready.

Primary measurable value metric: **Rerun FDE + customer-engineer hours per accepted POC-to-production handoff**. Secondary metric: **calendar days from first working POC to production acceptance**. No public source found in this pass establishes the current magnitude of either metric or says Rerun has a release/onboarding bottleneck.

### Evidence for

- The live FDE role explicitly owns customer work from first demo through production and asks the hire to make each POC/onboarding better than the last.
- The product surface spans multiple failure-prone boundaries—sensor logging/ingest, multimodal recordings, schema/data modeling, visualization, dataframe/SQL queries, catalogs, and training-data access—so a reusable acceptance contract is plausibly useful when integrations change.

### Evidence against

- Rerun is explicitly hiring an FDE to institutionalize customer success and feed recurring struggles into the roadmap, which may already be the intended mechanism for making POCs repeatable.
- Rerun already provides a unified SDK/data model, open-source tooling, catalog workflows, and a commercial Hub; no source found reports excessive POC cycle time, integration regressions, customer incidents, reviewer burden, or demand for an external release-gate layer.

## 2-minute utility gift

**Physical-AI POC → Production Acceptance Card — Recording × Schema × Query × Visual Behavior × Resource Envelope × Rollback**

For one synthetic before/after Rerun integration revision, bind: one representative recording fixture; schema/logging compatibility; deterministic query invariants; one visualization/annotation expectation; a simple ingest/query latency or memory envelope; exact SDK/config revision; and rollback target. Return `PROMOTE | HOLD | REJECT`, showing only material regressions or missing evidence.

## Deeper proof artifact

Build a public-safe synthetic robotics-telemetry regression harness using invented camera, LiDAR, pose, timestamp, and annotation streams. Exercise ingestion/replay, schema evolution, deterministic dataframe/SQL invariants, representative visualization-state assertions where practical, and revision-bound acceptance evidence. Inject failures for missing frames, timestamp drift, schema mismatch, partial recordings, query regression, resource-envelope breach, stale fixture/evidence, and rollback mismatch. No Rerun Hub account, customer data, paid service, deployment, or production-performance claim.

## Route / falsifier

`APPLY_NOW_OPERATOR_REVIEWED` because the official role is currently live and directly asks for customer-facing POC-to-production engineering.

Strongest route falsifier: downgrade or drop the application path if the required robotics/ML/data-engineering/database foundation, working Python, hands-on customer POC delivery, West-Coast-US fit, or ~30% travel cannot be truthfully substantiated. Strongest proof-kit falsifier: kill the wedge if Rerun already uses a low-overhead reusable customer acceptance mechanism that binds representative recordings, schema/query behavior, resource bounds, exact revision identity, and rollback to each POC-to-production handoff.

## Honest flaw

This target has real **domain-transfer risk**. The operator's release-gate/eval/reproducibility patterns are adjacent, but Rerun's core problem is physical-AI data infrastructure rather than generic LLM-agent governance. S07 should build a Rerun-shaped data/POC acceptance artifact; an agent-security or generic AI-governance wrapper would be off-target and earn zero external-fitness credit.

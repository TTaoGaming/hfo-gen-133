# S08 GTM Target Card — Temporal

```yaml
schema_id: hfo.gen133.gtm_target_card.v1
task_id: 6a526109ba348191b5f23ad3172ad568
target: Temporal Technologies
species: PRODUCT_PLATFORM
vertical: durable execution / agent infrastructure
route: RELATIONSHIP_ONLY
privacy: PUBLIC_SAFE_SYNTHETIC_ONLY
world_effect_ceiling: T0_PREP_RESEARCH_GIT
verifier: S04
next_consumer: S07
consumer_workitem: S07_TEMPORAL_AI_WORKER_VERSION_PROMOTION_MANIFEST_V1
expiry_utc: 2026-08-14T14:08:00Z
evidence_digest_sha256: d497203da7db8c6777a6297648539ff2cb90df80db61a1a22e925af00b0942e3
```

## Current signal

Temporal is explicitly positioning Durable Execution as infrastructure for production AI agents. On 2026-02-17 it announced a $300M Series D at a $5B valuation and framed the funding around moving agentic AI from experiments into production. On 2026-03-30, Worker Versioning became GA with traffic ramping, verification before production traffic, and instant rollback; Temporal specifically names long-running AI-agent workflows as a version-upgrade use case. Its 2026 changelog also records Principal Attribution (2026-04-30), OpenAI Agents SDK sandbox support (2026-04-16), and Custom Roles (2026-06-25). Temporal's AI Partner Ecosystem currently offers technical review and launch support for integrations.

Primary sources:
- 2026-02-17 — https://temporal.io/news/temporal-raises-300M-to-make-agentic-ai-real-for-companies
- 2026-03-30 — https://temporal.io/changelog/worker-versioning-continue-as-new-worker-controller
- 2026-04-16 / 2026-04-30 / 2026-06-25 — https://temporal.io/changelog
- current — https://temporal.io/partners/ai

## Best buyer / user persona

AI Platform / Product Engineering owner responsible for production agent workloads, Worker Versioning, and ecosystem integrations. A secondary user is a platform/SRE team promoting new Worker Deployment Versions that contain model/tool behavior.

Named public bridge: **Ethan Ruhe — AI Product Lead / Staff Product Manager, AI at Temporal**, source-backed by Temporal's 2026 Replay materials. No procurement, partnership-approval, or buying authority is inferred.
- 2026-05-06 — https://replay.temporal.io/schedule?day=2
- current presenter bio — https://pages.temporal.io/webinar-r2r-nordstrom.html

## Expensive pain hypothesis

**Hypothesis:** teams running AI agents on Temporal may still consume material engineering/reviewer time when promoting an exact Worker Deployment Version because Temporal's durable/versioning controls must be reconciled with AI-specific evidence that lives elsewhere: held-out eval quality, principal/tool authority, HITL rules, model/tool cost envelope, trace completeness, and rollback criteria.

Primary measurable value metric: **engineer + reviewer hours from candidate Worker Deployment Version to accepted production traffic ramp**. Secondary metric: calendar cycle time from candidate version to production promotion.

This is not a claim that Temporal or its customers currently have this pain.

## Evidence for / against

**For:** Worker Versioning explicitly supports tests before production traffic, gradual ramps, and rollback; Temporal is expanding Principal Attribution, roles, AI SDK integrations, and an AI partner ecosystem. Those surfaces create a plausible seam where AI-specific promotion evidence could be bound to the exact deployment version.

**Against:** Temporal already has unusually mature deployment/versioning, audit, observability, and durability primitives, and it has a Braintrust integration plus an AI partner ecosystem. Eval/security/cost evidence may intentionally remain in external tools and CI rather than becoming a Temporal-native concern. No source establishes a customer backlog, incident rate, excessive review burden, or demand for this integration.

## 2-minute utility gift

**AI Worker Version Promotion Manifest — Eval × Identity × Authority × Cost × Rollback**

For one synthetic candidate Worker Deployment Version, bind:
1. exact deployment version/build identifier;
2. held-out eval result + threshold;
3. principal identity and allowed tool/action policy;
4. HITL/escalation rule;
5. model/tool cost + latency envelope;
6. trace/evidence pointer;
7. rollback condition and prior known-good version.

Return `PROMOTE | HOLD | REJECT` with explicit missing-evidence reasons. This is a compact integration concept, not a claim that Temporal lacks these controls.

## Deeper proof artifact

A public-safe, synthetic **Temporal AI release-evidence adapter** that consumes mocked Worker Version metadata, fixture eval outputs, synthetic workflow histories, and an independent OPA/Rego-style authorization oracle; then emits a revision-bound promotion manifest plus negative controls for stale evals, wrong principal, widened tool authority, budget regression, missing HITL, incomplete trace evidence, and rollback mismatch. No Temporal Cloud deployment, customer data, production claims, or paid services.

## Strongest falsifier

Kill the wedge if Temporal already provides—or deliberately delegates to existing partner integrations—a low-overhead way to bind AI eval quality, principal/tool authority, HITL policy, cost envelope, trace evidence, and rollback criteria to the exact Worker Deployment Version before traffic promotion. Also kill it if Temporal's product strategy explicitly treats these AI-specific checks as external CI concerns with no ecosystem-extension value.

## Honest flaw

This is a high-adjacency but potentially low-demand target: Temporal already owns the hard durability/versioning layer and may prefer Braintrust/other ecosystem tools to own eval evidence. The card proves a plausible integration seam, not unmet demand, buyer accessibility, or willingness to adopt an external artifact.

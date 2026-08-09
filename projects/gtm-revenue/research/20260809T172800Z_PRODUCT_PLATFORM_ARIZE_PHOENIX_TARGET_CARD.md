# S08 TARGET CARD — ARIZE AI / PHOENIX

```yaml
schema_id: hfo.gen133.gtm_target_card.v1
seat: S08
expected_task_id: 6a526109ba348191b5f23ad3172ad568
self_probe:
  task_id_match: true
  task_enabled: true
  wip: 1
  available_surfaces_used:
    - native_tasks_readback
    - github_read_write
    - public_web_research
    - slack_post_after_git_readback
source_campaign:
  path: projects/gtm-revenue/packets/20260807T140800Z_CHATGPT_CLOUD_GTM_DREAM50_HANDOFF.packet.md
  commit: 756f17f43a4cda4470ac776827b61408587edfd7
  expiry_utc: 2026-08-14T14:08:00Z
rotation:
  prior_species: CHANNEL_PARTNER
  species: PRODUCT_PLATFORM
target: Arize AI / Phoenix
vertical: AI observability / agent evaluation / agent-improvement infrastructure
route: RELATIONSHIP_ONLY
privacy: PUBLIC_SAFE_SYNTHETIC_ONLY
world_effect_ceiling: T0_PREP_RESEARCH_GIT
verifier: S04
next_consumer: S07
consumer_workitem: S07_ARIZE_AUTHORITY_EVAL_TRACE_PROMOTION_CONTRACT_V1
expiry_utc: 2026-08-14T14:08:00Z
evidence_digest_sha256: 0d00c7ffcc532a775d110aa88b433e3b580393eec8200a9992017ec8337153fc
```

## Current signal

Arize is actively expanding from observability/evaluation into an agent-improvement control loop. On **2026-06-04**, Arize AX announced Signal, repo-aware managed-agent orchestration, agent-fleet observability, full-agent experimentation, and Harness-as-a-Judge. Arize says engineers remain the approval point while managed agents investigate and propose changes. On **2026-05-11**, the Phoenix team described Phoenix's direction as a context platform where agents can query traces, evals, feedback, experiments, and annotations to verify their own work. On **2026-06-03**, Arize described Microsoft's ASSERT evaluation project and Agent Control Specification as sharing an OpenInference telemetry contract, explicitly connecting evaluation, runtime controls, and observability. Phoenix also added dedicated tool-selection and tool-invocation evaluators on **2026-01-31**. These are direct product signals, not evidence that Arize lacks authorization or release-governance capability.

Primary official sources:
- 2026-06-04 — https://arize.com/blog/building-ai-factory-self-improving-agents-arize-ax/
- 2026-06-03 — https://arize.com/blog/microsoft-open-trust-stack-openinference/
- 2026-05-11 — https://arize.com/blog/from-observability-to-context-whats-next-for-arize-phoenix/
- 2026-01-31 — https://arize.com/docs/phoenix/release-notes/02-2026/02-01-2026-tool-selection-and-tool-invocation-evaluators
- verified current 2026-08-09 — https://arize.com/phoenix
- verified current 2026-08-09 — https://arize.com/about-us/

## Best buyer / user persona

**Persona:** Phoenix / Arize AX product or OSS engineering leadership responsible for agent evaluation, OpenInference/OpenTelemetry contracts, full-agent experimentation, and production feedback loops. The downstream user is an AI-platform engineer shipping tool-using agents whose behavior, authority, cost, and quality can change together.

**Named public bridge:** **Mikel King, Founding Engineer — Head of OSS**, listed on Arize's current official team page. This is only a public role match; procurement authority, partnership authority, accessibility, and interest are not inferred.

## Expensive-pain hypothesis

**Hypothesis:** teams using Phoenix/Arize to test tool-using agents *may* still spend material **AI-platform engineer + security/control reviewer hours per accepted agent-harness revision** reconciling a behavioral experiment with a separate runtime-authorization decision: what the agent did, what it was allowed to do, which principal/policy permitted it, whether that authority changed from baseline, and whether the same exact revision is safe to promote.

**Primary measurable value metric:** engineer + security/control-review hours per accepted agent-harness revision.

**Secondary metric:** candidate harness revision → evidence-backed promotion-decision cycle time.

This is not a claim that Arize or its customers currently have this bottleneck.

## Evidence for the hypothesis

- Arize's 2026-06-04 release explicitly says production-agent failures include wrong tool arguments/skipped steps and that improvement today often requires manual reconstruction across traces, datasets, evals, repository history, and deployment context.
- Full-agent experimentation now compares complete agent behavior including tools, retrieval, latency, trajectories, and evals, making exact revision evidence a first-class product surface.
- Arize's 2026-06-03 Microsoft trust-stack article explicitly connects **evaluation + runtime controls + observability** through OpenInference, suggesting policy/control decisions are adjacent to the trace/eval contract rather than an unrelated concern.
- Phoenix's tool-selection and tool-invocation evaluators directly score whether agents choose and invoke tools appropriately.

## Evidence against the hypothesis

- Arize already owns tracing, evaluations, experiments, managed-agent observability, production feedback loops, and human-review workflows; the proposed seam may already be covered internally or intentionally delegated to runtimes/security products.
- The Microsoft ASSERT/ACS/OpenInference integration is particularly strong counterevidence: Arize is already participating in a standards path that joins runtime controls with evaluation and telemetry.
- No official source found in this pass establishes excess review hours, authorization incidents, slow releases, customer demand for OPA/Rego integration, or willingness to pay for another release-control layer.

## 2-minute utility gift

**Authority × Eval Trace Promotion Contract** — one small, framework-neutral evidence card for a synthetic agent revision. It binds:

`agent_revision × principal × tool/action × policy_decision × held-out_eval_delta × trace_id × cost/latency_delta × rollback_revision`

and returns `PROMOTE | HOLD | REJECT`, showing only newly allowed actions, lost deny edges, failed tool-use evals, missing policy-decision provenance, material cost/latency regression, or missing rollback evidence.

## Deeper proof artifact

Build a public-safe synthetic **OpenInference Authority Decision Trace Harness**: fake support agent + mocked tools, Phoenix/OpenTelemetry-style traces, held-out tool-selection/invocation evals, and an independent OPA/Rego authorization oracle. Emit the policy decision as trace-linked evidence, compare before/after harness revisions, and inject negative controls for wrong principal, privilege widening, stale policy digest, newly allowed tool, eval regression, cost/latency drift, missing decision span, and rollback mismatch. No Arize account, customer telemetry, production system, paid model call, deployment, or security-outcome claim.

## Apply-now vs relationship-only

`RELATIONSHIP_ONLY`. There is a strong product/OSS adjacency, but no source-backed open role, marketplace route, paid integration request, or explicit external-contributor demand was established for this exact seam. Any later contact remains operator-reviewed and no-send until separately authorized.

## Strongest falsifier

Kill the wedge if Phoenix/Arize AX already provides or canonically supports a low-overhead mechanism that binds each exact agent/harness revision to principal identity, runtime policy/control decisions, held-out behavioral evals, trace evidence, cost/latency movement, approval, and rollback — or if Arize deliberately treats authorization as a runtime concern that should stay outside its product boundary.

## Honest flaw

This is a **high-adjacency, high-redundancy-risk** target. Arize is already building the agent verification and improvement loop, and its OpenInference work with Microsoft's runtime-control stack may subsume the proposed integration. S07 should continue only if the narrow **authorization-decision ↔ eval/trace ↔ exact-revision promotion** contract remains distinct; a generic observability/evals scorecard would add almost no value.

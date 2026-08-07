# GTM Target Card — Delinea

```yaml
schema_id: hfo.gen133.gtm_target_card.v1
card_id: GTM-S08-JOB-DELINEA-20260807T142821Z
target: Delinea
species: JOB_EMPLOYER
vertical: identity_security__ai_agent_authorization
valid_time_utc: 2026-08-07T14:28:21Z
source_access_date: 2026-08-07
evidence_digest_sha256: c3d748ce794c195875ad98bfa8d94f8688ed5592a7e77412bbe50069a5a389e4
status: RESEARCHED_PENDING_S07_KIT
route: APPLY_NOW_PLUS_RELATIONSHIP
privacy: PUBLIC_SOURCES_ONLY
world_effect_ceiling: T0_PREP_RESEARCH_GIT
external_send_authority: NONE
verifier: S04_same_provider_structural_preflight_binding_weight_0
next_consumer: S07_GTM_Proof_Kit_Builder
expiry_utc: 2026-08-14T14:28:21Z
```

## Current public signal

Delinea is currently advertising **Staff Software Engineer: Agent Identity and Authorization**, U.S. Remote, estimated base salary **$150K–$188K**. The role reports directly to the **Director of Engineering, Securing AI** and is explicitly foundational: model AI-agent identity and delegated/composite actions, build the runtime authorization engine, and help select policy technology such as **Cedar, OPA, or AuthZEN**.

Delinea's current product positioning also makes AI-agent control a first-class platform concern: continuous authorization across human, machine, and AI identities, just-in-time least-privilege access, runtime enforcement, credential separation, and auditable agent activity. A Delinea article published **June 2026** describes AI agents as identities that need runtime authorization rather than only connection-time access.

### Primary/current sources

1. Delinea ATS — Staff Software Engineer: Agent Identity and Authorization, accessed 2026-08-07: https://jobs.ashbyhq.com/delinea/9cae4086-3927-4cff-979f-f6fe4a446eda/?workplaceType=Remote
2. Delinea Platform product page, accessed 2026-08-07: https://delinea.com/products
3. Delinea blog, **AI agent authorization: Why access at the door is not enough**, published June 2026: https://delinea.com/blog/ai-agent-authorization

## Best persona

**Primary:** Director of Engineering, Securing AI / senior engineering leadership owning agent identity and authorization.

**Secondary:** staff/principal engineers on authorization, identity security, AI security, or platform policy.

**Named public bridge:** intentionally omitted. The sources above identify the role owner by title but do not provide a verified person's name; do not guess one.

## Expensive pain hypothesis — HYPOTHESIS, not company fact

Delinea appears to be investing in a difficult engineering problem: turning AI-agent identity, delegated authority, runtime policy and continuous evaluation into clean platform primitives that other teams can safely build on. The expensive failure mode is **not** simply "Delinea lacks agent authorization" — public evidence says Delinea already ships and markets substantial agent-control capability. The plausible pain is the **engineering and assurance cost of extending that capability into a robust, interoperable agent authorization architecture** while maintaining security, auditability and product velocity.

### Measurable value metrics to discover

- engineering/review hours required to define and validate policy semantics;
- time-to-ship new agent-authorization features or integrations;
- held-out authorization-policy coverage and escaped regression count;
- runtime authorization latency / false-deny / false-allow rates where measurable;
- auditability of delegated/composite agent actions;
- integration effort across OPA/Cedar/AuthZEN or identity-provider ecosystems.

## Evidence for the hypothesis

- The open role is explicitly foundational and asks one engineer to define identity models, delegated actions, authorization-engine behavior and platform contracts.
- The role specifically names **OPA, Cedar and AuthZEN**, creating unusually direct overlap with policy-as-code and deterministic authorization work.
- Delinea's June 2026 public material emphasizes that AI agents act at machine speed, inherit excessive privilege and require runtime authorization plus auditable actions.
- Delinea's product direction is centered on continuous authorization and AI identities, so correctness, extensibility and proof quality around this layer are commercially consequential.

## Evidence against / caution

- Delinea already markets runtime authorization, AI-agent governance, credential separation and continuous control; do **not** approach them as though this is an unsolved or absent product capability.
- The role asks for typically 10+ years with deep identity/authorization or distributed-systems-security expertise. OPA/Rego and agent-gate experience may be relevant, but the operator must not overstate identity-protocol or large-scale authorization-engine experience.
- Public job/product evidence does not prove current regressions, customer incidents, policy-engine shortcomings, or a quantified internal cost problem.

## Two-minute utility gift for S07

**Agent Delegation & Runtime Authorization Decision Matrix — OPA / Cedar / AuthZEN**

A one-page comparison/checklist centered on Delinea's stated design problem rather than a generic sales artifact. Suggested rows:

1. delegated/on-behalf-of identity representation;
2. composite identity / actor + principal attribution;
3. runtime context inputs;
4. deny-by-default / least privilege;
5. policy decision vs enforcement separation;
6. continuous/session re-evaluation;
7. audit explanation / decision evidence;
8. policy testability + held-out negative tests;
9. interoperability / standards surface;
10. latency, caching and failure-mode behavior.

**Usefulness gate:** recipient should be able to scan it in ~2 minutes and disagree with specific rows. It must not conclude which engine Delinea should choose without deeper requirements.

## Deeper proof artifact

A small **OPA/Rego agent-delegation policy starter plus held-out tests** demonstrating:

- actor vs represented-principal separation;
- scoped tool/resource/action permissions;
- high-impact action requiring human approval;
- deny on missing delegation/attribution evidence;
- negative tests for privilege inheritance and confused-deputy style cases;
- an explicit adapter boundary showing how the same policy test corpus could be expressed against another engine.

This should be a technical specimen, not a claim that Delinea needs OPA specifically.

## Recommended route

**APPLY NOW + RELATIONSHIP.** The current role is unusually aligned with OPA/policy-as-code and agent authority work. Application evidence should stay at the operator's real claim ceiling; in parallel, a relationship note can lead with the decision matrix as a useful artifact and ask for technical feedback rather than lead with a job ask.

## Strongest falsifier

Retire or materially downgrade this target if any of the following becomes true:

1. the current role closes or the operator fails a basic experience/eligibility gate;
2. a technical review shows the operator cannot credibly demonstrate policy-engine/authorization-system depth beyond superficial OPA usage;
3. S07 cannot make the two-minute artifact genuinely useful without pretending Delinea lacks capabilities it publicly already has;
4. external feedback from Delinea indicates agent authorization is not a current engineering priority or the artifact is irrelevant.

## Honest flaw

This card is built from Delinea's public hiring and product language, which is strong evidence of strategic direction but weak evidence of a specific internal operational pain or budget. The value metrics above remain discovery questions. The highest-risk failure is **overfitting the operator's OPA experience to a staff-level identity/authorization role** without enough proof of deep identity-protocol and authorization-engine design experience.

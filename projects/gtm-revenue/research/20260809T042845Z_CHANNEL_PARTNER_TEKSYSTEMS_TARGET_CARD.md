# S08 TARGET CARD — TEKsystems Global Services

```yaml
schema_id: hfo.gen133.gtm_target_card.v1
task_id: 6a526109ba348191b5f23ad3172ad568
carrier: S08
target: TEKsystems Global Services
species: CHANNEL_PARTNER
vertical: enterprise AI delivery / technology services / talent services
valid_time_utc: 2026-08-09T04:28:45Z
evidence_digest_sha256: a2ba7ff11bd199391c6cbe91c64e3c0f68205b831ee5c38c51b15f823e1ce87d
route: RELATIONSHIP_ONLY
privacy: PUBLIC_SAFE_SYNTHETIC_ONLY
world_effect_ceiling: T0_PREP_RESEARCH_GIT
verifier: S04
next_consumer: S07
downstream_workitem: S07_TEKSYSTEMS_FDE_PROTOTYPE_TO_PRODUCTION_HANDOFF_GATE_V1
expiry_utc: 2026-08-14T14:08:00Z
```

## Current signal

TEKsystems Global Services (TGS) launched a Forward Deployed Engineering function on **2026-04-14** to move customer AI ideas into working prototypes in under four weeks, build a business case, and transition successful prototypes to project teams for production operationalization. TGS says the FDE function is intended to create repeatable solution patterns that accelerate future projects.

TGS also holds AWS AI Competency status across Agentic AI and Generative AI and currently markets secure, cost-effective agentic-AI services on AWS for end-to-end workflows. Its current careers surface explicitly offers consultant opportunities serving customers that include more than 80% of the Fortune 500.

Sources:
- 2026-04-14 — https://www.teksystems.com/en/insights/newsroom/2026/forward-deployed-engineering
- 2026-03-10 — https://www.teksystems.com/en/insights/newsroom/2026/aws-ai-competency
- verified 2026-08-09; page exposes no publication date — https://www.teksystems.com/en/who-we-are/partnerships/aws/agentic-ai-and-generative-ai-services
- verified 2026-08-09; page exposes no publication date — https://www.teksystems.com/en/careers
- verified 2026-08-09; page exposes no publication date — https://www.teksystems.com/en/who-we-are/our-leadership

## Persona / bridge

**Best buyer/user persona:** TGS Forward Deployed Engineering or AI delivery leader accountable for prototype-to-production transition quality, delivery speed, repeatability, and customer handoff.

**Named public bridge:** **Matt Payne, Senior Vice President and head of TEKsystems Global Services.** The FDE launch quotes him on the function's purpose, and the current official leadership page lists him as SVP, TGS. This does **not** establish procurement authority, subcontracting authority, accessibility, or interest in this artifact.

## Expensive-pain hypothesis

**Hypothesis, not a claimed company problem:** as TGS scales short-cycle FDE prototypes into production projects, an AI/agent revision may require repeated engineering and client-review effort to show that the promoted version still meets business acceptance, held-out quality, bounded tool/action authority, cost/latency expectations, observability, human escalation, and rollback requirements.

**Measurable value metric — cycle time:** median calendar days from accepted working prototype to evidence-backed production handoff.

### Evidence for
- TGS explicitly defines a boundary from rapid prototype → business case → transition/scale into a production project team.
- TGS explicitly says the FDE model aims to move from idea to impact quickly and produce repeatable solution patterns.
- TGS' AWS agentic-AI surface emphasizes moving beyond stalled pilots into secure real-world execution.

### Evidence against
- TGS already has a formal FDE process and AWS AI Competency, which is evidence of mature delivery capability rather than a missing gate.
- No cited source establishes failed handoffs, excess review hours, margin leakage, customer incidents, a backlog, or an external-specialist capacity shortage.
- The public consultant channel does not prove that TGS uses independent specialists inside its FDE function.

## S07 consumption contract

**2-minute utility gift:** `FDE Prototype→Production Handoff Gate — Value × Eval × Authority × Cost × Ops`

For one candidate agent/workflow revision, S07 should make a one-page `PROMOTE | HOLD | REJECT` card covering:
1. business success criterion and measured proof-point;
2. held-out regression/eval result;
3. tool/action authority and mandatory human escalation;
4. expected model/tool cost and latency envelope;
5. trace/operational evidence plus rollback owner.

**Deeper proof artifact:** public-safe synthetic AWS-style agentic workflow acceptance harness using fake data and offline/mock provider outputs. Bind a candidate revision to held-out evals, an independent OPA/Rego-style authorization oracle, model-route cost/latency fixtures, trace completeness, failure injection, HITL escalation, and rollback. Do not deploy to AWS or claim TGS usage/outcomes.

**Route:** `RELATIONSHIP_ONLY`. There is a current consultant channel, but no source-backed matching requisition or subcontracting invitation was established in this pass. Any application or contact requires operator review.

## Falsifier / ceilings

**Strongest falsifier:** kill the wedge if TGS already has a low-overhead revision-bound handoff mechanism that binds business acceptance, held-out quality, action authority, cost/latency, traces, approval, and rollback to every prototype promoted into a production project—or if its FDE delivery model does not use external/consultant specialists for this class of work.

**Privacy/effect ceiling:** public sources and synthetic data only; research + Git card + internal Slack pointer only. No account creation, terms acceptance, application, outreach, send, purchase, paid call, deployment, publication, merge, private-data use, or negotiation.

**Honest flaw:** TEKsystems is a very large services-and-talent organization with an opaque internal staffing model. The evidence proves active FDE/agentic-AI investment and a general consultant channel, but it does not prove a buyer, a delivery bottleneck, a subcontracting seam, or demand for an external release-assurance specialist.

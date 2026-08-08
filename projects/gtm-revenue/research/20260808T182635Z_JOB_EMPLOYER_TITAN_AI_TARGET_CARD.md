# S08 GTM Target Card — Titan AI — Applied AI Engineer

```yaml
schema_id: hfo.gen133.gtm.target_card.v1
result: READY
seat: S08_GTM_TARGET_SCOUT
wip: 1
valid_time_utc: 2026-08-08T18:26:35Z
canonical_repository: TTaoGaming/hfo-gen-133
canonical_branch: agent/gen133-bootstrap-20260730
campaign_packet: projects/gtm-revenue/packets/20260807T140800Z_CHATGPT_CLOUD_GTM_DREAM50_HANDOFF.packet.md
campaign_packet_expiry_utc: 2026-08-14T14:08:00Z

self_probe:
  expected_task_id: 6a526109ba348191b5f23ad3172ad568
  observed_task_id: 6a526109ba348191b5f23ad3172ad568
  task_id_match: true
  github_read_available: true
  github_write_available: true
  public_web_research_available: true
  slack_pointer_send_available: true
  task_inventory_read_available: true
  task_mutation_performed: false

target:
  company: Titan AI / Titan OS, Inc.
  target: Applied AI Engineer — Remote United States
  species: JOB_EMPLOYER
  vertical: banking-native AI / regulated financial-services agents
  route: APPLY_NOW_OPERATOR_REVIEWED
  current_signal: >-
    Titan's official Ashby surface was live when checked on 2026-08-08 for a full-time,
    Remote-US Applied AI Engineer with estimated base compensation of $200K-$300K plus equity.
    The role owns production agent orchestration, RAG/retrieval evaluation, LLM integration,
    behavioral contracts, regression baselines, production observability, and backend services
    at bank-tier uptime. Titan states in the role that it is growing from a handful of live
    banking customers to thirty, then hundreds. A second live Applied-AI-focused FDE role is
    delivering agentic workflows across lending, credit, compliance, and operations.
  best_persona: >-
    Product & Engineering hiring owner for the AI Toolbelt / production-AI lane who needs an
    engineer able to take a high-level banking problem through reliable, auditable implementation.
    The practical artifact user is an AI engineer or reviewer deciding whether a model, retrieval,
    prompt, or agent/tool change is safe enough to promote into a regulated workflow.
  public_bridge_person: >-
    Shaun Patterson — CTO on Titan's current official team page. This is a public technical bridge
    only; this card does not establish recruiter ownership, hiring authority for this exact role,
    or willingness to engage.

pain_hypothesis:
  status: HYPOTHESIS_NOT_COMPANY_FACT
  statement: >-
    As Titan scales live banking deployments, its production-AI engineering team may incur
    material change-promotion cycle time when each model, retrieval, prompt, tool, or agent
    revision must preserve behavioral quality, retrieval quality, delegated action boundaries,
    latency/cost expectations, auditability, model-risk evidence, and rollback readiness.
    The live role proves these concerns are owned by the team; it does NOT prove a current
    bottleneck, missing gate, excess staffing need, or deficient process.
  measurable_value_metric: >-
    Engineering/reviewer hours from proposed agent/retrieval/model change to evidence-backed
    production promotion, with accepted-change lead time as the primary cycle-time metric.
    No current Titan baseline or savings figure is asserted.

hypothesis_evidence:
  for:
    - >-
      The live Applied AI Engineer role explicitly owns behavioral contracts, regression
      baselines, production observability, retrieval evaluation, reliable/auditable inference,
      and bank-tier production services. Those are direct change-acceptance concerns rather
      than a generic AI-security category prior.
    - >-
      Titan says the role exists while scaling from a handful of live banking customers toward
      thirty and then hundreds, creating a plausible repeatability pressure on production
      acceptance evidence. This supports the relevance of a reusable promotion contract, not
      a claim that Titan lacks one.
    - >-
      Titan's July 16 official guidance says banking AI moving beyond pilots needs consistent,
      explainable, auditable outcomes plus security, governance, and auditability for
      mission-critical workflows.
  against:
    - >-
      Titan already hires specifically for eval infrastructure, behavioral regression,
      observability, and reliable/auditable inference, so a generic release checklist is likely
      redundant.
    - >-
      Titan's public product position is already built around explainability, governance,
      auditability, and banking-specific model-risk constraints; the team may have mature
      internal promotion and evidence tooling that public material does not expose.
    - >-
      Titan's current team includes a Principal Release Engineer and an AI Engineer with prior
      AI/ML governance-platform experience, which is counterevidence against assuming an
      elementary release-governance gap.

proof_kit:
  two_minute_utility_gift: >-
    "Banking Agent Change Acceptance Contract — Behavior x Retrieval x Authority x Audit":
    a one-page diff for one proposed production change containing version/model/provider,
    five held-out behavioral cases, retrieval regression checks, allowed tool/action boundary,
    latency/cost ceiling, trace/evidence pointer, human-review condition, rollback trigger,
    and a GO/HOLD verdict. It should be useful to an engineer/reviewer even if Titan already
    has deeper internal infrastructure.
  deeper_proof_artifact: >-
    Public-safe synthetic banking-workflow promotion harness using fake policy and loan
    documents, a mock retrieval index and APIs, agent/tool calls, an OPA/Rego-style action
    policy, multi-model routing stubs, held-out behavioral/retrieval tests, negative controls
    for unauthorized actions and stale evidence, latency/cost accounting, trace manifest,
    human approval, and rollback. No Titan account, customer system, credentials, proprietary
    code, or private banking data may be used.

work_item:
  id: S07_TITAN_AI_BANKING_AGENT_CHANGE_ACCEPTANCE_CONTRACT_V1
  state: READY_FOR_ADMISSION
  next_consumer: S07_GTM_PROOF_KIT_BUILDER
  next_consumer_task_id: 6a506f6dc5c08191b95f1707d7f00c2d
  acceptance: >-
    Produce exactly one public-safe two-minute Banking Agent Change Acceptance Contract
    shaped to Titan's live Applied AI Engineer role. Cite current official sources, keep the
    pain explicitly hypothetical, and do not imply Titan lacks behavioral regression,
    observability, auditability, or governance capability. If current Titan material exposes
    an equivalent low-overhead promotion contract, return HOLD/kill rather than duplicating it.

strongest_falsifier: >-
  Kill this wedge if Titan already has a low-overhead, versioned production promotion control
  that binds the exact agent/model/retrieval/tool revision to behavioral and retrieval regression,
  delegated-action policy, cost/latency limits, audit evidence, human-review conditions, and
  rollback. Separately, downgrade APPLY_NOW if the operator cannot substantiate the role's
  required 5+ years of software engineering and 2+ years shipping production AI systems.

privacy: PUBLIC_SAFE_SYNTHETIC_ONLY
effect_ceiling: T0_PREP_RESEARCH_GIT
verifier:
  primary: S04_HRIST_STRUCTURAL_PREFLIGHT
  task_id: 6a52861fbdb08191b9ef33a0b9c3c15c
  same_provider_binding_weight: 0
  independent_followup_required_before_external_claim: true
expiry_utc: 2026-08-14T14:08:00Z

honest_flaw: >-
  Titan is attractive because the role explicitly names almost the entire demonstrated toolbox,
  but that also means the bar is high and the proposed artifact can easily become redundant.
  The job requires five-plus years of software engineering and two-plus years operating
  production AI; a polished synthetic gate cannot manufacture those receipts if the operator's
  evidence ceiling is weaker. The card establishes a live role and a plausible production-change
  cost surface, not a hiring advantage, interview probability, or unmet internal tooling gap.

evidence_digest_contract:
  canonicalizer: UTF8_LF_EXACT_BLOCK_V1
  canonicalization_rule: >-
    SHA-256 over the exact UTF-8 bytes between BEGIN_EVIDENCE_PREIMAGE_V1 and
    END_EVIDENCE_PREIMAGE_V1, excluding both marker lines, after CRLF-to-LF normalization,
    with no BOM and exactly one trailing LF after the final source line. No trimming,
    field sorting, URL rewriting, or case folding is permitted.
  evidence_preimage_utf8_bytes: 1451
  evidence_digest_sha256: 887115281cdd37b0ed3e0da62f21270d196d5ab2dec9d13b7ee441d6b8d27d77
```

## Primary/current sources

1. **Titan AI / Ashby — Applied AI Engineer, Remote United States** — publication date not exposed; observed live **2026-08-08**: https://jobs.ashbyhq.com/titan-ai/297cf9a9-289d-4cd5-a4a1-1e051f6f5d64
2. **Titan AI / Ashby — Forward Deployed Engineer — Applied AI Focus** — publication date not exposed; observed live **2026-08-08**: https://jobs.ashbyhq.com/titan-ai/9a2e4f06-a63f-4f31-b0b7-e8049bc070e9/
3. **Titan — CEO Arjun Sirrah on why banking needs AI built for financial-services realities** — **2026-07-16**; observed **2026-08-08**: https://www.titanbanking.ai/post/titans-ceo-arjun-sirrah-on-why-banking-needs-ai-built-for-the-realities-of-financial-services
4. **Titan — Company / team** — publication date not exposed; observed **2026-08-08**: https://www.titanbanking.ai/about-company

## Recomputable evidence preimage

BEGIN_EVIDENCE_PREIMAGE_V1
source_1|observed_utc_date=2026-08-08|source_date=NO_PUBLISH_DATE_EXPOSED|url=https://jobs.ashbyhq.com/titan-ai/297cf9a9-289d-4cd5-a4a1-1e051f6f5d64|supports=live_US_remote_full_time_Applied_AI_Engineer;salary_200k_300k_plus_equity;scaling_from_handful_live_banking_customers_to_30_then_hundreds;agent_orchestration;RAG_and_retrieval_evaluation;reliable_auditable_inference;behavioral_contracts;regression_baselines;production_observability;bank_tier_uptime
source_2|observed_utc_date=2026-08-08|source_date=NO_PUBLISH_DATE_EXPOSED|url=https://jobs.ashbyhq.com/titan-ai/9a2e4f06-a63f-4f31-b0b7-e8049bc070e9/|supports=live_US_remote_full_time_FDE_Applied_AI;agentic_banking_workflows;lending_credit_compliance_operations;Titan_Foundry;Banking_Reasoning_Models;Banking_Agents;client_specific_delivery
source_3|observed_utc_date=2026-08-08|source_date=2026-07-16|url=https://www.titanbanking.ai/post/titans-ceo-arjun-sirrah-on-why-banking-needs-ai-built-for-the-realities-of-financial-services|supports=enterprise_banking_AI_requires_consistent_explainable_auditable_outcomes;security_explainability_governance_auditability_for_mission_critical_workflows;governed_use_cases
source_4|observed_utc_date=2026-08-08|source_date=NO_PUBLISH_DATE_EXPOSED|url=https://www.titanbanking.ai/about-company|supports=Shaun_Patterson_CTO;AI_and_regulatory_expertise;Ben_Tong_AI_engineer_prior_AI_ML_governance_platform_experience;David_Chung_Principal_Release_Engineer
END_EVIDENCE_PREIMAGE_V1

## No-effect receipt

No application, outreach, email/DM, account creation, terms acceptance, purchase, paid call,
deployment, merge, public publication outside this operator-controlled repository, private-data
use, credential use, demand claim, or autonomous negotiation was performed.

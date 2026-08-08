# S08 GTM Target Card — Coalfire

```yaml
schema_id: hfo.gen133.gtm.target_card.v1
result: READY
seat: S08_GTM_TARGET_SCOUT
wip: 1
valid_time_utc: 2026-08-08T16:26:25Z
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
  slack_write_available: true
  public_web_research_available: true
  dedup_target_search: NO_PRIOR_COALFIRE_TARGET_CARD_FOUND
  dedup_evidence_digest_search: NO_MATCH
  task_mutation_performed: false

target:
  company: Coalfire
  target: AI Security and Trust Engineering / AI assurance delivery
  species: CHANNEL_PARTNER
  vertical: cybersecurity_services / AI_assurance / compliance / agent_security
  route: RELATIONSHIP_ONLY
  current_signal: >-
    Coalfire is actively expanding commercial AI-assurance and agentic-security delivery. On
    2026-05-13 it announced provisional accreditation as an AIUC-1 auditor for AI agents and
    enterprise AI systems, combining governance validation with technical testing. On 2026-05-05 it
    launched Audit AI inside Compliance Essentials using MCP and open APIs to automate compliance
    workflows. Its current AI Security and Trust Engineering practice markets ForgeAI, LegionAI and
    GuardianAI, and describes a Secure Agent Construct addressing tool misuse, PII exposure,
    permissions and feedback loops. Coalfire also publicly operates a technology/professional-services
    partner ecosystem that includes joint offerings and, in some cases, direct technology integration.
  best_persona: >-
    AI Security and Trust Engineering / Enterprise Cloud Solutions delivery leader responsible for
    converting agent-security architecture, technical tests and assurance requirements into repeatable
    client evidence with controlled expert effort and defensible review outcomes.
  public_bridge_person: >-
    Nathan Demuth — Coalfire's 2026-01-06 official practitioner article identifies him as VP, Delivery,
    Enterprise Cloud Solutions and has him writing directly about agent reliability, guardrails,
    evaluation frameworks, fallbacks and identity/detection challenges. This is a source-backed public
    technical bridge only; no buying, subcontracting or procurement authority is inferred.

pain_hypothesis:
  status: HYPOTHESIS_NOT_COMPANY_FACT
  statement: >-
    As Coalfire expands AI-agent assurance across AIUC-1 auditing, Secure Agent Construct patterns and
    broader AI-security engagements, delivery teams may incur material expert-review cost normalizing
    runtime evidence from heterogeneous client agents into a repeatable acceptance record that binds
    exact system revision, delegated identity, allowed tools/actions, sensitive-data boundaries,
    held-out reliability tests, human escalation, trace provenance and rollback. Public evidence proves
    these control dimensions are commercially relevant to Coalfire; it does NOT prove Coalfire has a
    slow process, margin problem, evidence backlog or need for an outside specialist.
  measurable_value_metric: >-
    Expert delivery/reviewer hours consumed per accepted AI-agent assurance evidence package.
    Baseline, pricing and any margin impact are unknown and must not be invented.

hypothesis_evidence:
  for:
    - >-
      Coalfire's 2026-05-13 AIUC-1 announcement explicitly expands assurance for AI agents and
      enterprise AI systems using governance validation plus technical testing, creating a repeated
      need to bind technical evidence to an assurance decision.
    - >-
      The current AI Security and Trust Engineering page describes a Secure Agent Construct around
      inappropriate tool use, PII exposure, permissions and feedback loops, directly adjacent to a
      machine-verifiable runtime evidence manifest.
    - >-
      Audit AI's 2026-05-05 launch uses MCP and open APIs to automate compliance work, evidence that
      Coalfire is already investing in lower-friction evidence/review workflows rather than treating
      review labor as fixed.
    - >-
      Coalfire's current partner page says it builds joint service offerings and can license/integrate
      partner technologies, so a specialist technology/delivery partnership route is at least
      structurally plausible.
  against:
    - >-
      Coalfire already owns ForgeAI, LegionAI, GuardianAI, Secure Agent Construct patterns, AI risk
      services and deep assessment expertise; the proposed artifact may already exist internally in a
      stronger form.
    - >-
      Coalfire says Audit AI can improve manual review speed by up to 200%, while Compliance Essentials
      already reduces manual processes by up to 40%; a generic audit-automation pitch would therefore
      be weak and duplicative.
    - >-
      Coalfire's practitioner guidance already treats reliability, guardrails, evaluations, fallbacks
      and agent identity as first-class security concerns, reducing informational novelty.
    - >-
      No public source found here proves a capacity shortage, subcontractor demand, engagement-margin
      problem, failed assurance process or willingness to buy this capability from the operator.

proof_kit:
  two_minute_utility_gift: >-
    "Agent Assurance Evidence Manifest — Revision x Identity x Authority x Data x Reliability x
    Provenance": one page plus one filled synthetic example that forces an explicit ACCEPT / REJECT /
    NEEDS-HUMAN verdict. Required rows: exact agent/model/tool revision; delegated principal; allowed
    tools/actions; sensitive-data boundary; held-out quality/security cases; fallback/human escalation;
    trace/evidence provenance; rollback. Include five negative controls: permitted task with forbidden
    tool; correct answer after PII leakage; stale policy/version evidence; quality pass with missing
    principal delegation; and successful task with no rollback/evidence binding.
  deeper_proof_artifact: >-
    Public-safe synthetic support-ticket agent acceptance harness using fake tickets, fake identities
    and mock tools only. Add OPA/Rego-style per-action authorization, PII boundary tests, held-out
    reliability cases, injected tool/time-out failures, human escalation, trace/evidence capture and a
    revision-bound rollback verdict. Emit both a machine-readable evidence manifest and a compact human
    reviewer view; measure only synthetic evidence-generation/review effort, never client outcomes.

work_item:
  id: S07_COALFIRE_AGENT_ASSURANCE_EVIDENCE_MANIFEST_V1
  state: READY_FOR_ADMISSION
  next_consumer: S07_GTM_PROOF_KIT_BUILDER
  next_consumer_task_id: 6a506f6dc5c08191b95f1707d7f00c2d
  acceptance: >-
    Produce exactly one compact public-safe Agent Assurance Evidence Manifest under
    projects/gtm-revenue/kits/coalfire/, preserving the hypothesis ceiling, unknown baseline,
    counterevidence and strongest falsifier. If current Coalfire material exposes an equivalent
    revision-bound runtime evidence artifact already consumed by its assurance workflow, return
    HOLD/kill rather than polish a duplicate.

strongest_falsifier: >-
  Kill this wedge if Coalfire's current ForgeAI, GuardianAI, Secure Agent Construct or Audit AI
  workflow already emits and consumes an equivalent low-overhead, revision-bound acceptance manifest
  tying delegated identity, per-action authority, sensitive-data controls, held-out reliability,
  human escalation, evidence provenance and rollback directly into assessor/delivery decisions.

privacy: PUBLIC_SAFE_SYNTHETIC_ONLY
effect_ceiling: T0_PREP_RESEARCH_GIT
verifier:
  primary: S04_HRIST_STRUCTURAL_PREFLIGHT
  task_id: 6a52861fbdb08191b9ef33a0b9c3c15c
  same_provider_binding_weight: 0
  independent_followup_required_before_external_claim: true
expiry_utc: 2026-08-14T14:08:00Z

honest_flaw: >-
  Coalfire is attractive because it is already unusually mature in AI assurance, agent security and
  compliance automation. That same maturity may make it a poor buyer for an external specialist:
  technical adjacency is high, but unmet-demand evidence is weak. The artifact is only worth building
  if S07 can expose a concrete evidence-normalization seam that Coalfire's current stack does not
  already solve; otherwise retire the wedge quickly.

evidence_digest_contract:
  canonicalizer: UTF8_LF_EXACT_BLOCK_V1
  canonicalization_rule: >-
    SHA-256 over the exact UTF-8 bytes between BEGIN_EVIDENCE_PREIMAGE_V1 and
    END_EVIDENCE_PREIMAGE_V1, excluding both marker lines, after CRLF-to-LF normalization,
    with no BOM and exactly one trailing LF after the final source line. No trimming,
    field sorting, URL rewriting or case folding is permitted.
  evidence_preimage_utf8_bytes: 1603
  evidence_digest_sha256: 0d97d6799ebd320f5744aa5d422347e3b66d619077de29c435f37f84bb1bae14
```

## Primary/current sources

1. **Coalfire — Coalfire Expands AI Assurance Capabilities with Provisional AIUC-1 Accreditation** — **2026-05-13**: https://coalfire.com/insights/news-and-events/press-releases/coalfire-expands-ai-assurance-capabilities-with-provisional-aiuc-1-accreditation
2. **Coalfire — Coalfire Launches Audit AI for Compliance Essentials to Deliver Agentic Compliance at Enterprise Scale** — **2026-05-05**: https://coalfire.com/insights/news-and-events/press-releases/coalfire-launches-audit-ai-for-compliance-essentials-to-deliver-agentic-compliance-at-enterprise-scale
3. **Coalfire — AI Security and Trust Engineering** — current service page, observed **2026-08-08**: https://coalfire.com/services/advisory/ai-security-and-trust-engineering
4. **Coalfire — Partners** — current partner page, observed **2026-08-08**: https://coalfire.com/about/partners
5. **Coalfire — Securing AI Agents in 2026: What Practitioners Need to Know** — **2026-01-06**: https://coalfire.com/the-coalfire-blog/securing-ai-agents-in-2026-what-practitioners-need-to-know

## Recomputable evidence preimage

BEGIN_EVIDENCE_PREIMAGE_V1
source_1|observed_utc_date=2026-08-08|source_date=2026-05-13|url=https://coalfire.com/insights/news-and-events/press-releases/coalfire-expands-ai-assurance-capabilities-with-provisional-aiuc-1-accreditation|supports=provisional_AIUC_1_auditor_accreditation;AI_agent_and_enterprise_AI_assurance;governance_validation_plus_technical_testing
source_2|observed_utc_date=2026-08-08|source_date=2026-05-05|url=https://coalfire.com/insights/news-and-events/press-releases/coalfire-launches-audit-ai-for-compliance-essentials-to-deliver-agentic-compliance-at-enterprise-scale|supports=Audit_AI_launch;MCP_and_open_API_compliance_workflows;up_to_200_percent_manual_review_speed_claim;existing_up_to_40_percent_manual_process_reduction_claim
source_3|observed_utc_date=2026-08-08|source_date=CURRENT_SERVICE_PAGE|url=https://coalfire.com/services/advisory/ai-security-and-trust-engineering|supports=ForgeAI_LegionAI_GuardianAI;secure_agent_construct;inappropriate_tool_usage_and_PII_exposure_controls;permissions_and_feedback_loops
source_4|observed_utc_date=2026-08-08|source_date=CURRENT_PARTNERS_PAGE|url=https://coalfire.com/about/partners|supports=technology_and_professional_services_partner_ecosystem;joint_service_offerings;license_and_integrate_partner_technologies
source_5|observed_utc_date=2026-08-08|source_date=2026-01-06|url=https://coalfire.com/the-coalfire-blog/securing-ai-agents-in-2026-what-practitioners-need-to-know|supports=Nathan_Demuth_VP_Delivery_Enterprise_Cloud_Solutions;agent_reliability_security_link;orchestration_guardrails_evals_fallbacks;agent_identity_and_detection_challenges
END_EVIDENCE_PREIMAGE_V1

## No-effect receipt

No outreach, application, email/DM, account creation, terms acceptance, purchase, paid call,
deployment, publication outside this operator-controlled repository, merge, private-data use,
customer targeting, security testing against real systems, demand invention or autonomous
negotiation was performed.

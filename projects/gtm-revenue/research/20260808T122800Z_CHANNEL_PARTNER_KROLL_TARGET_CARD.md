# S08 GTM Target Card — Kroll

```yaml
schema_id: hfo.gen133.gtm.target_card.v1
result: READY
seat: S08_GTM_TARGET_SCOUT
wip: 1
valid_time_utc: 2026-08-08T12:28:00Z
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
  task_mutation_performed: false

target:
  company: Kroll
  target: Cyber and Data Resilience / CrowdStrike Services / agentic security delivery
  species: CHANNEL_PARTNER
  vertical: cybersecurity_services / AI_security / managed_security / agentic_SOC
  route: RELATIONSHIP_ONLY
  current_signal: >-
    Kroll is actively productizing and scaling AI-driven cyber services. Its current Fal.Con 2026
    page advertises an agentic SOC, Kroll APEX with CrowdStrike AgentWorks and a Foundry-enabled
    ROI calculator, and reports MDR operations spanning more than 450,000 endpoints. On 2026-05-07,
    Kroll announced participation in CrowdStrike's Charlotte AI AgentWorks Ecosystem, Project
    QuiltWorks and Falcon Flex for Services, and was named CrowdStrike's 2026 Americas MSSP Partner
    of the Year. Kroll also currently sells AI governance implementation, AI/LLM testing and
    continuous AI-risk monitoring services.
  best_persona: >-
    CrowdStrike Services / Engineered Defense / AI-security delivery leader responsible for turning
    agentic security use cases into repeatable client deployments with measurable outcomes, bounded
    authority, delivery evidence and acceptable engineering overhead.
  public_bridge_person: >-
    Robb Mayeski — Kroll's current Fal.Con 2026 and CrowdStrike partnership surfaces identify him as
    Global Head of Engineered Defense and CrowdStrike Services Portfolio Owner, Cyber and Data
    Resilience. This is a source-backed public technical/commercial bridge only; the card does not
    claim he wants an outside specialist or controls subcontracting/procurement.

pain_hypothesis:
  status: HYPOTHESIS_NOT_COMPANY_FACT
  statement: >-
    As Kroll scales APEX-scored agentic security automations across CrowdStrike-backed client
    environments, its delivery teams may incur material acceptance-cycle cost proving that a proposed
    automation still satisfies the business-value case while preserving held-out detection/response
    quality, per-action authority, human escalation, cost limits, trace/evidence completeness and
    rollback before client production use. Public evidence shows Kroll cares about measurable ROI,
    agentic operations and governance; it does NOT prove this acceptance boundary is slow, manual,
    deficient, or externally addressable.
  measurable_value_metric: >-
    Median elapsed time from an APEX "fund/build" decision for an agentic security use case to a
    client-accepted production automation with evidence complete. Baseline and savings are unknown
    and must not be invented.

hypothesis_evidence:
  for:
    - >-
      Kroll's Fal.Con 2026 material explicitly connects APEX, AgentWorks, Foundry and an ROI calculator
      to agentic-ready operations, making value-to-deployment translation a repeated delivery surface.
    - >-
      The 2026-05-07 CrowdStrike partnership release shows Kroll participating in AgentWorks,
      QuiltWorks and Flex for Services rather than merely advising on AI from outside the runtime.
    - >-
      Kroll's current AI Risk Governance service includes governance implementation, LLM/ML testing
      and continuous monitoring, so runtime evidence and control assurance are directly adjacent to
      paid delivery work.
    - >-
      Kroll's 2026 agentic-governance guidance argues that autonomous agents challenge legacy
      compliance/control frameworks, supporting the relevance of explicit authority and evidence gates.
  against:
    - >-
      Kroll already owns APEX, an ROI framework, AI security testing, AI governance implementation,
      managed services and a mature CrowdStrike delivery portfolio; the proposed gate may already
      exist internally in a stronger form.
    - >-
      Kroll publicly reports modernizations completed in less than 30 days in some partnership cases
      and operations across more than 450,000 endpoints, evidence of substantial delivery maturity,
      not evidence of a bottleneck.
    - >-
      No public source found here proves a subcontractor shortage, acceptance backlog, margin problem,
      failed agentic deployment, or willingness to buy this capability from the operator.
    - >-
      Kroll's core business is expert assurance; a generic AI-governance or agent checklist would be
      low-signal and could duplicate its own IP.

proof_kit:
  two_minute_utility_gift: >-
    "Agentic Security Automation Acceptance Card — ROI x Authority x Reliability x Evidence": one
    page that starts from an APEX-style funded use case and forces an explicit promotion verdict across
    expected value, held-out task quality, allowed actions/tools, human escalation, token/model cost
    ceiling, trace completeness, failure fallback and rollback. Include five negative controls: useful
    automation outside authority; cheaper route that drops a held-out detection; tool action without
    delegated principal; missing trace/evidence; and automation that passes quality but exceeds the
    economic threshold.
  deeper_proof_artifact: >-
    Public-safe synthetic SOC automation promotion harness using mock alerts/endpoints/APIs only:
    OPA/Rego-style action authorization, model/tool-route stubs, held-out triage/remediation cases,
    cost budgets, injected prompt/tool/timeout failures, human approval/escalation, trace/evidence
    binding and rollback. Measure synthetic promotion cycle time and accepted-cost-per-case only; do
    not imply transfer to Kroll or CrowdStrike production environments.

work_item:
  id: S07_KROLL_AGENTIC_SECURITY_AUTOMATION_ACCEPTANCE_GATE_V1
  state: READY_FOR_ADMISSION
  next_consumer: S07_GTM_PROOF_KIT_BUILDER
  next_consumer_task_id: 6a506f6dc5c08191b95f1707d7f00c2d
  acceptance: >-
    Produce exactly one compact public-safe Agentic Security Automation Acceptance Card under
    projects/gtm-revenue/kits/kroll/, preserving the hypothesis ceiling, unknown baseline,
    counterevidence and strongest falsifier. If current Kroll/APEX/AgentWorks material already exposes
    an equivalent cross-control promotion artifact, return HOLD/kill rather than polishing redundancy.

strongest_falsifier: >-
  Kill this wedge if Kroll's current APEX/AgentWorks delivery process already binds the use-case ROI
  decision to versioned held-out quality thresholds, per-action authority, human escalation, model/token
  cost limits, trace/evidence completeness and rollback for the exact promoted automation with low
  delivery overhead. In that case this gift is redundant.

privacy: PUBLIC_SAFE_SYNTHETIC_ONLY
effect_ceiling: T0_PREP_RESEARCH_GIT
verifier:
  primary: S04_HRIST_STRUCTURAL_PREFLIGHT
  task_id: 6a52861fbdb08191b9ef33a0b9c3c15c
  same_provider_binding_weight: 0
  independent_followup_required_before_external_claim: true
expiry_utc: 2026-08-14T12:28:00Z

honest_flaw: >-
  Kroll is attractive precisely because it already has deep AI-security, governance, managed-service
  and CrowdStrike integration capability. That makes technical adjacency high but unmet-demand evidence
  weak. The channel thesis is relationship-only until external discovery proves a capacity, integration,
  delivery-cycle or specialist-partner gap; otherwise S07 should retire this wedge quickly.

evidence_digest_contract:
  canonicalizer: UTF8_LF_EXACT_BLOCK_V1
  canonicalization_rule: >-
    SHA-256 over the exact UTF-8 bytes between BEGIN_EVIDENCE_PREIMAGE_V1 and
    END_EVIDENCE_PREIMAGE_V1, excluding both marker lines, after CRLF-to-LF normalization,
    with no BOM and exactly one trailing LF after the final source line. No trimming,
    field sorting, URL rewriting or case folding is permitted.
  evidence_preimage_utf8_bytes: 1451
  evidence_digest_sha256: 8274af460eab25b86bd12642da9366df07874ab6a7de8dc19c50927f20cf5efa
```

## Primary/current sources

1. **Kroll — Kroll at Fal.Con 2026** — upcoming **2026-08-31 to 2026-09-03**, observed **2026-08-08**: https://www.kroll.com/en/events/2026/kroll-at-fal-con
2. **Kroll — Accelerates CrowdStrike Partnership with Joint Innovation, Customer Outcomes and Award Win** — **2026-05-07**: https://www.kroll.com/en/newsroom/kroll-crowdstrike-partnership-joint-innovation-customer-outcomes-award-win
3. **Kroll — The Regulatory Cliff Edge: How Agentic AI Is Outpacing Compliance Frameworks** — **2026-06-11**: https://www.kroll.com/en/publications/cyber/regulatory-cliff-edge
4. **Kroll — AI Risk Governance and Strategy Services** — current service page, observed **2026-08-08**: https://www.kroll.com/en/services/cyber/cybersecurity-transformation/ai-risk-management
5. **Kroll — CrowdStrike Partnership** — current partnership page, observed **2026-08-08**: https://www.kroll.com/en/services/cyber/crowdstrike-partnership

## Recomputable evidence preimage

BEGIN_EVIDENCE_PREIMAGE_V1
source_1|observed_utc_date=2026-08-08|source_date=UPCOMING_EVENT_2026-08-31_TO_2026-09-03|url=https://www.kroll.com/en/events/2026/kroll-at-fal-con|supports=agentic_SOC_of_future;APEX_with_AgentWorks_and_Foundry_ROI_calculator;450000_plus_endpoints;measurable_security_outcomes
source_2|observed_utc_date=2026-08-08|source_date=2026-05-07|url=https://www.kroll.com/en/newsroom/kroll-crowdstrike-partnership-joint-innovation-customer-outcomes-award-win|supports=Charlotte_AI_AgentWorks_Ecosystem;Project_QuiltWorks;Falcon_Flex_for_Services;2026_Americas_MSSP_Partner_of_Year;joint_innovation_and_customer_outcomes
source_3|observed_utc_date=2026-08-08|source_date=2026-06-11|url=https://www.kroll.com/en/publications/cyber/regulatory-cliff-edge|supports=agentic_AI_governance;autonomy_outpacing_legacy_compliance;runtime_governance_and_control_relevance
source_4|observed_utc_date=2026-08-08|source_date=CURRENT_SERVICE_PAGE|url=https://www.kroll.com/en/services/cyber/cybersecurity-transformation/ai-risk-management|supports=AI_governance_implementation_and_managed_services;LLM_ML_testing;continuous_monitoring;Kroll_AI_taskforce
source_5|observed_utc_date=2026-08-08|source_date=CURRENT_PARTNERSHIP_PAGE|url=https://www.kroll.com/en/services/cyber/crowdstrike-partnership|supports=Robb_Mayeski_Global_Head_of_Engineered_Defense_and_CrowdStrike_Services_Portfolio_Owner;end_to_end_implementation_and_ongoing_operations;agentic_ready_partner_delivery
END_EVIDENCE_PREIMAGE_V1

## No-effect receipt

No outreach, application, email/DM, account creation, terms acceptance, purchase, paid call, deployment, publication outside this operator-controlled repository, merge, private-data use, customer targeting, security testing against real systems, demand invention or autonomous negotiation was performed.

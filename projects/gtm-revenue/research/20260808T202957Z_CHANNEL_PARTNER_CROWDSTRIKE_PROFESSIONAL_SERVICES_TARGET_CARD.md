# S08 GTM Target Card — CrowdStrike Professional Services

```yaml
schema_id: hfo.gen133.gtm.target_card.v1
result: READY
seat: S08_GTM_TARGET_SCOUT
wip: 1
valid_time_utc: 2026-08-08T20:29:57Z
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
  dedup_target_search: NO_PRIOR_CROWDSTRIKE_PROFESSIONAL_SERVICES_TARGET_CARD_FOUND
  dedup_evidence_digest_search: NO_MATCH
  task_mutation_performed: false

target:
  company: CrowdStrike
  target: Professional Services / AI Security Services / SOC Transformation Services
  species: CHANNEL_PARTNER
  vertical: cybersecurity_services / agentic_SOC / AI_security / managed_security
  route: RELATIONSHIP_ONLY
  current_signal: >-
    CrowdStrike is actively commercializing agentic-security services and partner delivery. On
    2026-03-24 it introduced Agentic MDR and SOC Transformation Services; the latter explicitly
    includes AI use-case development, guardrails for safe response actions, and validation exercises
    before production changes. The same day CrowdStrike launched Flex for Services across its
    expert-led services portfolio and said the model creates growth opportunities for service
    partners. On 2026-04-21 Professional Services launched the Shadow AI Visibility Service, using
    telemetry-backed runtime evidence and expert guidance after reporting large discrepancies between
    customer-reported and discovered AI/agent inventories. On 2026-03-25 CrowdStrike launched the
    Charlotte AI AgentWorks Ecosystem, explicitly enabling partners to create agentic-security
    businesses on Falcon. This establishes an active partner/service surface; it does not establish
    demand for an independent solo specialist.
  best_persona: >-
    Professional Services / AI Security Services / SOC Transformation Services portfolio or delivery
    leader responsible for turning customer-specific agentic-SOC use cases into repeatable,
    evidence-backed production changes while controlling expert review effort, decision authority,
    and auditability.
  public_bridge_person: >-
    Thomas Etheridge — CrowdStrike's current executive page identifies him as Chief Global
    Professional Services Officer overseeing the entire Professional and Managed Services portfolio
    and notes his experience building global services channel programs and customer/partner training
    programs. This is a source-backed public bridge only; no procurement, subcontracting, hiring, or
    willingness-to-engage authority is inferred.

pain_hypothesis:
  status: HYPOTHESIS_NOT_COMPANY_FACT
  statement: >-
    As CrowdStrike scales agentic SOC, AI Security Services and partner-led services across
    heterogeneous customer environments, delivery teams may incur material expert delivery/reviewer
    hours when each customer-specific automation or agent change must bind workflow intent, agent and
    caller identity, allowed tools/actions, held-out security/reliability evidence, analyst or HITL
    decision rights, trace/audit evidence, resource or spend ceilings, and rollback before a production
    change is accepted. Public evidence shows CrowdStrike performs many of these control and validation
    activities; it does NOT prove a slow process, capacity shortage, margin problem, backlog, missed
    SLA, or demand for an outside specialist.
  measurable_value_metric: >-
    Expert delivery/reviewer hours consumed per accepted customer agentic-SOC workflow or production
    change. Secondary diagnostic: elapsed time from assessed/design-ready workflow to evidence-backed
    production acceptance. Baseline, margin, revenue impact and target improvement are unknown and
    must not be invented.

hypothesis_evidence:
  for:
    - >-
      SOC Transformation Services explicitly includes AI use-case development, guardrails for safe
      response actions, and validation exercises that pressure-test people, process and platform
      before production changes, establishing a repeated acceptance surface.
    - >-
      Shadow AI Visibility Service says CrowdStrike Professional Services repeatedly encounters
      inaccurate customer AI inventories and provides telemetry-backed runtime evidence, visibility
      gap analysis and prioritized expert guidance; heterogeneous evidence normalization is therefore
      a real delivery activity even though CrowdStrike's own internal effort is not quantified.
    - >-
      Flex for Services extends expert-led advisory, testing and platform-operationalization services
      through a flexible consumption model and explicitly describes partner growth and more efficient
      delivery as goals, so expert-service capacity is commercially material even though no shortage
      is proven.
    - >-
      Charlotte AI AgentWorks explicitly opens new opportunities for ecosystem partners to create
      agentic-security businesses on Falcon, making a channel relationship structurally plausible.
  against:
    - >-
      CrowdStrike's 2026-08-04 secure-agent-harness article documents seven implemented independent
      control layers, MCP tool-call mediation, per-command policy, fail-closed HITL, tamper-evident
      audit, spend/resource ceilings and automated regression testing; a generic agent-governance or
      release-gate pitch would likely be redundant.
    - >-
      Continuous Identity for AI Agents already authorizes every agent action using owner, caller and
      real-time risk context, directly overlapping the identity/authorization part of the proposed
      wedge.
    - >-
      Agentic MDR already combines deterministic automation, expert-defined guardrails and analyst
      authority over novel or high-impact threats, reducing novelty of a human-approval matrix.
    - >-
      The partner evidence names established system integrators, service providers and technology
      partners. No public source found here proves CrowdStrike wants an independent solo specialist,
      has a subcontractor gap, or would accept this artifact into its delivery process.

proof_kit:
  two_minute_utility_gift: >-
    "Agentic SOC Production Change Acceptance Card — Intent x Identity x Action x Reliability x
    Evidence": one page plus one filled synthetic example. Required rows: customer workflow/use case;
    exact agent/model/tool revision; owner/caller/delegated identity; allowed tools/actions; sensitive
    data and asset boundary; held-out security/reliability cases; analyst/HITL conditions and decision
    rights; trace/audit evidence; resource/spend ceilings; and rollback. Include six negative controls:
    correct detection with a forbidden action; missing agent owner/caller; stale approval after a tool
    change; quality pass with missing audit evidence; budget/control bypass; and HITL timeout that must
    fail closed.
  deeper_proof_artifact: >-
    Public-safe synthetic SOC triage/containment-agent acceptance harness using fake alerts, endpoints,
    identities and mock Falcon-like tools only. Add an independent OPA/Rego-style per-action policy
    oracle, held-out benign/malicious cases, prompt-injection/tool-misuse and identity-loss tests,
    denied-action and budget-exhaustion cases, fail-closed HITL, tamper-evident-style synthetic traces,
    and a revision-bound evidence manifest with rollback verdict. Measure only synthetic reviewer
    effort; do not test CrowdStrike systems, customer systems, or claim customer outcomes.

work_item:
  id: S07_CROWDSTRIKE_AGENTIC_SOC_SERVICE_ACCEPTANCE_CARD_V1
  state: READY_FOR_ADMISSION
  next_consumer: S07_GTM_PROOF_KIT_BUILDER
  next_consumer_task_id: 6a506f6dc5c08191b95f1707d7f00c2d
  acceptance: >-
    Produce exactly one compact public-safe Agentic SOC Production Change Acceptance Card under
    projects/gtm-revenue/kits/crowdstrike-professional-services/, preserving the hypothesis ceiling,
    unknown baseline, counterevidence and strongest falsifier. If current CrowdStrike Professional
    Services or SOC Transformation material exposes an equivalent low-overhead revision-bound
    acceptance artifact already used in client delivery, return HOLD/kill rather than polish a
    duplicate.

strongest_falsifier: >-
  Kill this wedge if CrowdStrike Professional Services / SOC Transformation Services already uses a
  low-overhead, revision-bound delivery gate that ties intended workflow, principal/agent identity,
  per-action authority, security/reliability regression evidence, analyst/HITL decision rights, audit
  trail, resource/spend ceilings and rollback directly to customer production-change acceptance.
  Separately retire the channel route if partner intake is limited to partner classes for which the
  operator has no realistic qualifying path.

privacy: PUBLIC_SAFE_SYNTHETIC_ONLY
effect_ceiling: T0_PREP_RESEARCH_GIT
verifier:
  primary: S04_HRIST_STRUCTURAL_PREFLIGHT
  task_id: 6a52861fbdb08191b9ef33a0b9c3c15c
  same_provider_binding_weight: 0
  independent_followup_required_before_external_claim: true
expiry_utc: 2026-08-14T14:08:00Z

honest_flaw: >-
  CrowdStrike is attractive because it is highly active in agentic security and partner-led services,
  but that same maturity makes it a poor candidate for a generic external tooling pitch. Its current
  public materials show implemented controls that are more sophisticated than the proposed primitive
  stack and a partner ecosystem dominated by established firms. The card proves technical adjacency
  and a plausible service-delivery seam, not unmet demand, buyer accessibility, subcontractor need or
  commercial fit. S07 should kill quickly if the gift merely restates CrowdStrike's own control stack.

evidence_digest_contract:
  canonicalizer: UTF8_LF_EXACT_BLOCK_V1
  canonicalization_rule: >-
    SHA-256 over the exact UTF-8 bytes between BEGIN_EVIDENCE_PREIMAGE_V1 and
    END_EVIDENCE_PREIMAGE_V1, excluding both marker lines, after CRLF-to-LF normalization,
    with no BOM and exactly one trailing LF after the final source line. No trimming,
    field sorting, URL rewriting or case folding is permitted.
  evidence_preimage_utf8_bytes: 2118
  evidence_digest_sha256: e92b4d3d9d1c56a75c12c8d7dfe3394e95e36e6a0906d74a0be9b4682e52f175
```

## Primary/current sources

1. **CrowdStrike — CrowdStrike Services and Agentic MDR Put the Agentic SOC in Reach** — **2026-03-24**: https://www.crowdstrike.com/en-us/blog/crowdstrike-services-and-agentic-mdr-put-the-agentic-soc-in-reach/
2. **CrowdStrike — Introducing the CrowdStrike Shadow AI Visibility Service** — **2026-04-21**: https://www.crowdstrike.com/en-us/blog/crowdstrike-shadow-AI-visibility-service/
3. **CrowdStrike — CrowdStrike Flex for Services Expands Access to Elite Security Expertise** — **2026-03-24**: https://www.crowdstrike.com/en-us/blog/crowdstrike-extends-the-falcon-flex-model-to-services/
4. **CrowdStrike — CrowdStrike Unveils Continuous Identity for AI Agents** — **2026-06-15**: https://www.crowdstrike.com/en-us/press-releases/crowdstrike-unveils-continuous-identity-for-ai-agents/
5. **CrowdStrike — Secure Agent Harness Execution: Preventing Escape** — **2026-08-04**: https://www.crowdstrike.com/en-us/blog/secure-agent-harness-execution-preventing-escape/
6. **CrowdStrike — Thomas Etheridge, Chief Global Professional Services Officer** — current executive page, observed **2026-08-08**: https://www.crowdstrike.com/en-us/about-us/executive-team/thomas-etheridge/
7. **CrowdStrike — CrowdStrike Launches the Charlotte AI AgentWorks Ecosystem for Building Secure Agents** — **2026-03-25**: https://www.crowdstrike.com/en-us/press-releases/crowdstrike-launches-charlotte-ai-agentworks-ecosystem-for-building-secure-agents/

## Recomputable evidence preimage

BEGIN_EVIDENCE_PREIMAGE_V1
source_1|observed_utc_date=2026-08-08|source_date=2026-03-24|url=https://www.crowdstrike.com/en-us/blog/crowdstrike-services-and-agentic-mdr-put-the-agentic-soc-in-reach/|supports=Agentic_MDR_GA;SOC_Transformation_Services;deterministic_automation_with_guardrails;expert_human_accountability;AI_use_case_development;pre_production_validation_exercises
source_2|observed_utc_date=2026-08-08|source_date=2026-04-21|url=https://www.crowdstrike.com/en-us/blog/crowdstrike-shadow-AI-visibility-service/|supports=AI_Security_Services;Professional_Services_field_inventory_gap;runtime_evidence;visibility_gap_analysis;prioritized_expert_guidance
source_3|observed_utc_date=2026-08-08|source_date=2026-03-24|url=https://www.crowdstrike.com/en-us/blog/crowdstrike-extends-the-falcon-flex-model-to-services/|supports=Flex_for_Services;expert_led_services_portfolio;advisory_testing_platform_operationalization;services_consumption_friction_reduction
source_4|observed_utc_date=2026-08-08|source_date=2026-06-15|url=https://www.crowdstrike.com/en-us/press-releases/crowdstrike-unveils-continuous-identity-for-ai-agents/|supports=continuous_identity_for_AI_agents;per_action_risk_aware_authorization;agent_owner_and_caller_context
source_5|observed_utc_date=2026-08-08|source_date=2026-08-04|url=https://www.crowdstrike.com/en-us/blog/secure-agent-harness-execution-preventing-escape/|supports=seven_independent_agent_control_layers;MCP_tool_call_policy;HITL_fail_closed;tamper_evident_audit;spend_and_resource_ceilings;automated_regression_suite
source_6|observed_utc_date=2026-08-08|source_date=CURRENT_EXECUTIVE_PAGE|url=https://www.crowdstrike.com/en-us/about-us/executive-team/thomas-etheridge/|supports=Thomas_Etheridge_Chief_Global_Professional_Services_Officer;oversees_professional_and_managed_services;global_services_channel_program_experience
source_7|observed_utc_date=2026-08-08|source_date=2026-03-25|url=https://www.crowdstrike.com/en-us/press-releases/crowdstrike-launches-charlotte-ai-agentworks-ecosystem-for-building-secure-agents/|supports=AgentWorks_ecosystem;partner_agentic_security_business_opportunities
END_EVIDENCE_PREIMAGE_V1

## No-effect receipt

No outreach, application, email/DM, account creation, terms acceptance, purchase, paid call,
deployment, publication outside this operator-controlled repository, merge, private-data use,
customer targeting, security testing against real systems, demand invention or autonomous
negotiation was performed.

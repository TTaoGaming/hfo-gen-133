# S08 GTM Target Card — JPMorgan Chase

```yaml
schema_id: hfo.gen133.gtm.target_card.v1
result: READY
seat: S08_GTM_TARGET_SCOUT
wip: 1
valid_time_utc: 2026-08-08T11:28:00Z
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
  slack_write_surface_available: true
  task_inventory_read_available: true
  task_mutation_performed: false

target:
  company: JPMorgan Chase & Co.
  target: JPMorganChase enterprise AI / agentic security and controls
  species: ENTERPRISE_BUYER
  vertical: global financial services / banking / payments / regulated enterprise AI
  route: RELATIONSHIP_ONLY
  current_signal: >-
    JPMorganChase's 2026-06-15 Innovation Week recap says 2026 agentic-AI work is shifting
    toward richer context, economic guardrails, disciplined governance, and autonomy that grows
    together with controls, while AI is increasingly embedded in workflows and the product
    development lifecycle. On 2026-07-02, Chase CIO Gill Haus and the Global Ignite lead said
    teams are using AI for routine-task automation, cloud migrations, modernization, upgrades,
    and decision support at enterprise scale. The firm's 2026-03-23 security guidance separately
    calls for runtime controls, delegated-authority boundaries, identity/authorization, agent-to-agent
    trust, and complete tamper-evident records for higher-risk agents.
  best_persona: >-
    Cybersecurity & Technology Controls or enterprise AI-platform owner accountable for production
    agent governance, delegated authority, runtime enforcement, model/tool change control,
    audit evidence, and safe acceleration of AI-enabled workflows.
  public_bridge_person: >-
    Pat Opet — identified by JPMorganChase's 2026-06-15 Innovation Week recap as Global Chief
    Information Security Officer. This establishes a public technical leadership bridge only;
    it does not establish procurement ownership, an unmet need, or willingness to engage.

pain_hypothesis:
  status: HYPOTHESIS_NOT_COMPANY_FACT
  statement: >-
    As JPMorganChase expands higher-autonomy agents and AI-enabled workflows, teams may incur
    material agent-release and control-approval cycle time translating a use case into a production
    state where delegated identity, allowed tools/actions, runtime authorization, risk tier,
    safety/eval evidence, economic guardrails, tamper-evident traces, human override, and rollback
    are all bound to the exact agent/model/tool revision. Public sources prove these controls matter
    to JPMorganChase; they do NOT prove a current backlog, deficient implementation, or external buying demand.
  measurable_value_metric: >-
    Median approval-to-production cycle time for a material agent workflow or agent revision,
    measured from eval-ready candidate to approved production release with required control evidence.
    No current baseline, headcount savings, or dollar value is asserted.

hypothesis_evidence:
  for:
    - >-
      JPMorganChase's 2026 Innovation Week explicitly says agent autonomy and controls must grow
      together and highlights strong context, economic guardrails, disciplined governance, AI in
      workflows, and end-to-end product-lifecycle change.
    - >-
      Its 2026-03-23 agentic-security guidance calls for clear authorization boundaries,
      runtime enforcement, delegated identity, agent-to-agent trust, auditable workflows,
      stronger safeguards for higher-risk operations, and tamper-evident runtime records.
    - >-
      The 2026-07-02 Ignite article says teams are already applying AI to automation,
      modernization, migrations, upgrades, and decision support, making repeatable production
      controls potentially relevant across many internal workflows rather than one isolated pilot.
    - >-
      JPMorganChase's Global CIO bio reports a $19.8B technology budget and approximately 65,000
      technologists, establishing enterprise scale. This is scale evidence only, not evidence of pain.
  against:
    - >-
      JPMorganChase already publishes unusually mature agent-security principles and may already
      have equivalent internal runtime authorization, release, audit, and governance systems.
    - >-
      Its Fence framework already performs use-case-specific synthetic safety testing for
      hallucination, topic drift, prompt injection, and related LLM risks, which is direct evidence
      that internal AI-safety infrastructure exists.
    - >-
      A bank of this scale may prefer internally standardized platforms and approved strategic
      vendors; a small external proof artifact may be educational but commercially irrelevant.

proof_kit:
  two_minute_utility_gift: >-
    "Agent Runtime Authority & Evidence Gate — Risk x Identity x Action x Evidence": a one-page
    pass/fail matrix that maps agent risk tier to delegated principal, allowed tools/data/actions,
    runtime authorization check, economic guardrail, required trace/audit evidence, human-stop rule,
    and rollback condition. It must be framed as a reusable thought tool, not as a claim that
    JPMorganChase lacks these controls.
  deeper_proof_artifact: >-
    Public-safe synthetic regulated-workflow harness using fake accounts and mock APIs only:
    OPA/Rego-style per-action authorization, delegated human-principal context, agent-to-agent
    trust checks, held-out task/safety evals, economic/model-routing limits, failure injection,
    tool-sequence negative controls, append-only evidence manifest, human override, and rollback.
    No JPMorganChase systems, data, credentials, customers, or private processes may be used.

work_item:
  id: S07_JPMORGAN_AGENT_RUNTIME_AUTHORITY_EVIDENCE_GATE_V1
  state: READY_FOR_ADMISSION
  next_consumer: S07_GTM_PROOF_KIT_BUILDER
  next_consumer_task_id: 6a506f6dc5c08191b95f1707d7f00c2d
  admission_note: >-
    S07 should consume this only if it can produce a recipient-useful artifact materially sharper
    than restating JPMorganChase's public agent-security principles. S02/S04 should preserve the
    exact source/digest and hypothesis ceiling before any downstream external-facing use.
  acceptance: >-
    Produce exactly one public-safe two-minute authority/evidence gate tied to the source-backed
    runtime-control problem. Keep all company-specific pain claims hypothetical. If current public
    JPMorganChase material already exposes an equivalent low-overhead cross-control gate, HOLD/kill.

strongest_falsifier: >-
  Kill this wedge if JPMorganChase already has a reusable internal control plane or release contract
  that binds agent risk tier, delegated identity, per-action authorization, held-out safety/quality
  evidence, economic guardrails, tamper-evident runtime records, human override, and rollback to the
  exact promoted agent/model/tool revision with low incremental approval burden. In that case the
  proposed gift is redundant and there is no evidence of an external need.

privacy: PUBLIC_SAFE_SYNTHETIC_ONLY
effect_ceiling: T0_PREP_RESEARCH_GIT
verifier:
  primary: S04_HRIST_STRUCTURAL_PREFLIGHT
  task_id: 6a52861fbdb08191b9ef33a0b9c3c15c
  same_provider_binding_weight: 0
  independent_followup_required_before_external_claim: true
expiry_utc: 2026-08-14T11:28:00Z

honest_flaw: >-
  JPMorganChase is likely one of the hardest places to differentiate with a generic agent-governance
  artifact because its public material already shows strong internal security, safety, engineering,
  and governance maturity at enormous scale. The card establishes strategic relevance, not a buyer,
  budget, backlog, or consulting gap. Relationship-only is therefore the correct route unless later
  evidence identifies a specific external partner motion or operational gap.

evidence_digest_contract:
  canonicalizer: UTF8_LF_EXACT_BLOCK_V1
  canonicalization_rule: >-
    SHA-256 over the exact UTF-8 bytes between BEGIN_EVIDENCE_PREIMAGE_V1 and
    END_EVIDENCE_PREIMAGE_V1, excluding both marker lines, after CRLF-to-LF normalization,
    with no BOM and exactly one trailing LF after the final source line. No trimming,
    field sorting, URL rewriting, or case folding is permitted.
  evidence_preimage_utf8_bytes: 1614
  evidence_digest_sha256: 0d619145f1bb24595797765cfdd9dc69edfd96c6ac9ab1b07c4eba428e6931a4
```

## Primary/current sources

1. **JPMorganChase — Innovation for business impact: Key takeaways from JPMorganChase's 11th Innovation Week** — **2026-06-15**: https://www.jpmorganchase.com/about/technology/blog/key-takeaways-from-innovation-week-2026
2. **JPMorganChase — Securing the next generation of AI agents** — **2026-03-23**: https://www.jpmorganchase.com/about/technology/blog/securing-agentic-ai
3. **JPMorganChase — Strengthening LLM guardrails with synthetic data generation** — **2026-04-02**: https://www.jpmorganchase.com/about/technology/blog/fence-framework
4. **JPMorganChase — Ignite at JPMorganChase: scaling community-led learning at enterprise level in the age of AI** — **2026-07-02**: https://www.jpmorganchase.com/about/technology/blog/scaling-community-led-learning-at-enterprise-level-in-the-age-of-ai
5. **JPMorganChase — Lori A. Beer, Global Chief Information Officer** — publication date not exposed; observed **2026-08-08**: https://www.jpmorganchase.com/about/leadership/lori-beer

## Recomputable evidence preimage

BEGIN_EVIDENCE_PREIMAGE_V1
source_1|observed_utc_date=2026-08-08|source_date=2026-06-15|url=https://www.jpmorganchase.com/about/technology/blog/key-takeaways-from-innovation-week-2026|supports=2026_agentic_AI_focus_on_context;autonomy_and_controls_grow_together;economic_guardrails;disciplined_governance;AI_embedded_in_workflows;end_to_end_product_lifecycle_shift
source_2|observed_utc_date=2026-08-08|source_date=2026-03-23|url=https://www.jpmorganchase.com/about/technology/blog/securing-agentic-ai|supports=agents_take_actions;runtime_controls;delegated_authority;identity_and_authorization;agent_to_agent_trust;tamper_evident_runtime_records;auditable_workflows;higher_risk_actions_need_stronger_safeguards
source_3|observed_utc_date=2026-08-08|source_date=2026-04-02|url=https://www.jpmorganchase.com/about/technology/blog/fence-framework|supports=JPMC_built_Fence_guardrail_framework;use_case_specific_synthetic_safety_testing;hallucination_topic_drift_prompt_injection_controls;internal_benchmarks_report_improved_safety_reliability
source_4|observed_utc_date=2026-08-08|source_date=2026-07-02|url=https://www.jpmorganchase.com/about/technology/blog/scaling-community-led-learning-at-enterprise-level-in-the-age-of-ai|supports=teams_use_AI_for_automation_cloud_migrations_modernization_and_decision_support;enterprise_scaling_requires_adaptability_and_sharing_what_works_and_does_not
source_5|observed_utc_date=2026-08-08|source_date=NO_PUBLISH_DATE_EXPOSED|url=https://www.jpmorganchase.com/about/leadership/lori-beer|supports=Lori_Beer_Global_CIO;19.8B_technology_budget;approximately_65000_technologists;firmwide_technology_scope
END_EVIDENCE_PREIMAGE_V1

## No-effect receipt

No outreach, application, email/DM, account creation, terms acceptance, purchase, paid tool call, deployment, merge, publication outside this operator-controlled repository, private-data use, credential use, demand claim, or autonomous negotiation was performed.

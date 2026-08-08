# S08 GTM Target Card — Kognitos — Forward Deployed Engineer

```yaml
schema_id: hfo.gen133.gtm.target_card.v1
result: READY
seat: S08_GTM_TARGET_SCOUT
wip: 1
valid_time_utc: 2026-08-08T14:28:00Z
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
  company: Kognitos
  target: Forward Deployed Engineer - Remote USA
  species: JOB_EMPLOYER
  vertical: enterprise agentic process automation / finance / healthcare / IT operations
  route: APPLY_NOW_OPERATOR_REVIEWED
  current_signal: >-
    Kognitos' official Ashby surface was live when checked on 2026-08-08 for a full-time,
    Remote-USA Forward Deployed Engineer. The role embeds with enterprise customers to scope,
    design, build, and ship production automations; translate ambiguous and undocumented
    processes into working automations; integrate ERPs, databases, APIs, email, and document
    sources; debug production issues; and own the technical relationship through onboarding,
    deployment, and expansion.
  best_persona: >-
    US Forward Deployed Engineering / Solutions Engineering hiring manager responsible for
    customer discovery, production automation delivery, time-to-value, and expansion. The
    artifact's practical user is an FDE who must convert a messy process into a defensible
    go-live decision without recreating acceptance criteria from scratch.
  public_bridge_person: >-
    Neeraj Mathur — VP of Solutions Engineering on Kognitos' current official leadership page.
    This is a public technical bridge only; this card does not establish hiring authority,
    recruiter ownership, or willingness to engage.

pain_hypothesis:
  status: HYPOTHESIS_NOT_COMPANY_FACT
  statement: >-
    Kognitos' US FDE team may incur material customer-deployment cycle time when converting an
    ambiguous business process into a production automation because each engagement must bind
    business outcome, process rules, integration behavior, exception/human authority, regression
    evidence, and go-live/rollback criteria across customer-specific systems. The live role shows
    that FDEs own this translation and production delivery, but it does NOT establish a current
    backlog, deficient process, excess staffing, or missing internal acceptance tooling.
  measurable_value_metric: >-
    Customer time-to-value: elapsed days from agreed process scope to evidence-backed production
    go-live for one automation, with FDE engineering hours per go-live as a secondary diagnostic.
    No current Kognitos baseline or savings amount is asserted.

hypothesis_evidence:
  for:
    - >-
      The live US FDE role explicitly centers on ambiguous and undocumented process discovery,
      production-grade automation, enterprise-system integrations, production troubleshooting,
      and ownership through onboarding, deployment, and expansion. That makes deployment-cycle
      quality and time-to-value direct role concerns rather than a generic AI-governance pitch.
    - >-
      The role requires FDEs to act as the feedback loop from customer reality into Product and
      Engineering, which is consistent with repeated customer-specific edge cases being important
      to successful delivery. This supports the relevance of a reusable acceptance contract, not
      a claim that one is absent.
    - >-
      Kognitos' own platform material treats time-to-value, deterministic execution, human guidance
      on deviations, and regression testing as product concerns, so a proof artifact can be framed
      around measurable deployment acceptance rather than speculative model novelty.
  against:
    - >-
      Kognitos already advertises built-in regression testing and deterministic execution, so a
      generic release-gate or hallucination checklist would likely duplicate existing capability.
    - >-
      Kognitos documentation says automations begin as drafts so users can build and test safely,
      further weakening any claim that the platform lacks a basic pre-production test lifecycle.
    - >-
      The company's platform and Business-Journal-style auditability are designed specifically to
      preserve process visibility and exception history. The missing seam, if any, would have to be
      customer-engagement acceptance/ROI packaging rather than traceability itself.

proof_kit:
  two_minute_utility_gift: >-
    "Process-to-Production Acceptance Contract — Outcome x Rules x Exceptions x Evidence": a
    one-page FDE worksheet for one automation containing the business KPI/baseline, deterministic
    process rules, integration dependencies, exception and human-approval boundaries, five held-out
    acceptance cases, go-live evidence, rollback trigger, and owner. It should help an FDE and
    process owner agree what 'production-ready' means before implementation expands.
  deeper_proof_artifact: >-
    Public-safe synthetic AP automation acceptance harness using fake invoices, a mock ERP/API,
    deterministic workflow rules, an OPA/Rego-style approval/authority layer, held-out exception
    cases, injected integration failures, versioned acceptance criteria, human escalation, a
    Business-Journal-like evidence trace, and a go-live/rollback verdict. No Kognitos account,
    customer system, credentials, proprietary implementation, or private data may be used.

work_item:
  id: S07_KOGNITOS_FDE_PROCESS_TO_PRODUCTION_ACCEPTANCE_MAP_V1
  state: READY_FOR_ADMISSION
  next_consumer: S07_GTM_PROOF_KIT_BUILDER
  next_consumer_task_id: 6a506f6dc5c08191b95f1707d7f00c2d
  acceptance: >-
    Produce exactly one public-safe two-minute Process-to-Production Acceptance Contract that is
    useful to an FDE/process owner, cites the current role and product sources, and does not imply
    Kognitos lacks regression testing or deterministic execution. If current Kognitos material
    already exposes an equivalent low-overhead customer go-live contract, return HOLD/kill rather
    than polishing a redundant checklist.

strongest_falsifier: >-
  Kill this wedge if Kognitos already gives FDEs a low-overhead, versioned customer-deployment
  contract that directly binds business KPI/baseline, process rules, integration dependencies,
  exception/human authority, held-out regression evidence, go-live evidence, rollback, and
  time-to-value to the exact promoted automation. In that case the proposed gift is redundant.

privacy: PUBLIC_SAFE_SYNTHETIC_ONLY
effect_ceiling: T0_PREP_RESEARCH_GIT
verifier:
  primary: S04_HRIST_STRUCTURAL_PREFLIGHT
  task_id: 6a52861fbdb08191b9ef33a0b9c3c15c
  same_provider_binding_weight: 0
  independent_followup_required_before_external_claim: true
expiry_utc: 2026-08-14T14:08:00Z

honest_flaw: >-
  Technical/process alignment is strong, but the role's hardest bar is not merely building agent
  controls: it is customer-facing ownership of ambiguous enterprise work, production integration,
  communication under pressure, and account expansion. A good acceptance harness can demonstrate
  systems thinking and process discipline, but it cannot manufacture prior FDE, finance/healthcare,
  renewal, or enterprise-account experience if that evidence is weak. Kognitos also already claims
  deterministic execution and built-in regression testing, so a generic governance artifact would
  be low-value and should be rejected.

evidence_digest_contract:
  canonicalizer: UTF8_LF_EXACT_BLOCK_V1
  canonicalization_rule: >-
    SHA-256 over the exact UTF-8 bytes between BEGIN_EVIDENCE_PREIMAGE_V1 and
    END_EVIDENCE_PREIMAGE_V1, excluding both marker lines, after CRLF-to-LF normalization,
    with no BOM and exactly one trailing LF after the final source line. No trimming,
    field sorting, URL rewriting, or case folding is permitted.
  evidence_preimage_utf8_bytes: 1073
  evidence_digest_sha256: b26b8e2943b1e2112aee225796ad2e36d1c66555316427b00de2ca40b33750a3
```

## Primary/current sources

1. **Kognitos / Ashby — Forward Deployed Engineer, Remote USA** — publication date not exposed; observed live **2026-08-08**: https://jobs.ashbyhq.com/kognitos/75ef6778-ee45-4eb5-b2fa-02834f78a986
2. **Kognitos — Platform** — publication date not exposed; observed **2026-08-08**: https://www.kognitos.com/platform/
3. **Kognitos Documentation — Quick Start** — publication date not exposed; observed **2026-08-08**: https://docs.kognitos.com/guides/getting-started/quick-start
4. **Kognitos — About Us / Leadership** — publication date not exposed; observed **2026-08-08**: https://www.kognitos.com/about-us/

## Recomputable evidence preimage

BEGIN_EVIDENCE_PREIMAGE_V1
source_1|observed_utc_date=2026-08-08|source_date=NO_PUBLISH_DATE_EXPOSED|url=https://jobs.ashbyhq.com/kognitos/75ef6778-ee45-4eb5-b2fa-02834f78a986|supports=live_US_remote_full_time_Forward_Deployed_Engineer;enterprise_customer_discovery_design_build_go_live;ambiguous_undocumented_processes;ERP_database_API_email_document_integrations;production_issue_debugging;owns_onboarding_deployment_expansion
source_2|observed_utc_date=2026-08-08|source_date=NO_PUBLISH_DATE_EXPOSED|url=https://www.kognitos.com/platform/|supports=neurosymbolic_deterministic_automation;built_in_regression_testing;human_guidance_on_deviation;claimed_10x_faster_time_to_value_and_lower_maintenance
source_3|observed_utc_date=2026-08-08|source_date=NO_PUBLISH_DATE_EXPOSED|url=https://docs.kognitos.com/guides/getting-started/quick-start|supports=automation_starts_as_draft;build_and_test_safely_before_run
source_4|observed_utc_date=2026-08-08|source_date=NO_PUBLISH_DATE_EXPOSED|url=https://www.kognitos.com/about-us/|supports=Neeraj_Mathur_VP_of_Solutions_Engineering;current_leadership_surface
END_EVIDENCE_PREIMAGE_V1

## No-effect receipt

No application, outreach, email/DM, account creation, terms acceptance, purchase, paid call, deployment, merge, public publication outside this operator-controlled repository, private-data use, credential use, demand claim, or autonomous negotiation was performed.

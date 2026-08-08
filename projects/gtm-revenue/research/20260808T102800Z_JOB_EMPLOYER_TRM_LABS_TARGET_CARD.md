# S08 GTM Target Card — TRM Labs — AI Agent Engineer

```yaml
schema_id: hfo.gen133.gtm.target_card.v1
result: READY
seat: S08_GTM_TARGET_SCOUT
wip: 1
valid_time_utc: 2026-08-08T10:28:00Z
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
  task_inventory_read_available: true
  task_mutation_performed: false

target:
  company: TRM Labs
  target: AI Agent Engineer - US Remote
  species: JOB_EMPLOYER
  vertical: blockchain intelligence / financial-crime investigations / production AI
  route: APPLY_NOW_OPERATOR_REVIEWED
  current_signal: >-
    The official TRM Labs job surface was live when checked on 2026-08-08 for a full-time,
    US-remote AI Agent Engineer. The role owns agent frameworks, OpenAI/Anthropic/local-model
    infrastructure, evaluation loops, safe/observable/auditable agent behavior, and metrics
    including reasoning, latency, success rate, and hallucination. The published US base range
    is $200,000-$275,000 plus possible equity.
  best_persona: >-
    AI Engineering hiring manager or platform owner responsible for production agentic
    infrastructure, evaluation, observability, governance, and analyst-facing agent quality.
  public_bridge_person: >-
    Ankush Sharma — source-backed author of TRM's 2026-05-22 Agentic Software Factory article.
    This card does not establish his current title, hiring authority, or procurement authority.

pain_hypothesis:
  status: HYPOTHESIS_NOT_COMPANY_FACT
  statement: >-
    TRM's AI Engineering team may incur material agent-change promotion and reviewer cycle time
    when turning fast-moving model, prompt, tool, or agent-framework changes into production,
    because a release must preserve held-out task quality, hallucination limits, latency,
    credential/action boundaries, observability evidence, human decision ownership, and rollback.
    Public evidence shows that TRM has experienced review/verification bottlenecks as AI output
    increased, but it does NOT establish this exact team's current backlog, current cycle time,
    or a missing release gate.
  measurable_value_metric: >-
    Median candidate-to-production promotion cycle time for an agent change, measured in
    engineering hours/days from eval-ready candidate to human-approved production release.
    No current baseline or savings amount is asserted.

hypothesis_evidence:
  for:
    - >-
      The live role explicitly requires safe, observable, auditable agent behavior and evaluation
      across reasoning, latency, success rate, and hallucination, making release evidence a direct
      job responsibility rather than a generic AI-governance pitch.
    - >-
      TRM's 2026-05-22 engineering article says AI-assisted output had outpaced absorption,
      PR review queues lengthened, and quality/prioritization/verification became the bottleneck;
      it also says the shared platform should solve permissions, audit logs, evals, and feedback loops once.
    - >-
      TRM's 2026-03-27 observability article says agentic workflows can query continuously at
      volumes humans do not, producing a real and growing cost penalty under the prior pricing model.
  against:
    - >-
      TRM already operates AskNickiBot as a shared agent platform with centralized OAuth,
      per-tool permissions, audit logs, retrieval, evals, and feedback loops, and is consolidating
      that platform across more of the company.
    - >-
      TRM's 2026-06-23 credential-broker work already uses acceptance criteria, repeatable demos,
      integration/end-to-end tests, adversarial review by non-author agents, and explicit human ownership.
    - >-
      TRM reports that its observability migration cut costs by over 80%, so the historical
      observability-cost pressure is counterevidence against pitching a generic observability-cost fix.

proof_kit:
  two_minute_utility_gift: >-
    "TRM Agent Change Promotion Contract — Quality x Authority x Evidence": a one-page pass/fail
    matrix binding seven release checks to one human decision: held-out task success, hallucination
    bound, latency, credential isolation, tool/action authority, trace completeness, and rollback.
    It should be useful as a review artifact even if no hiring conversation occurs.
  deeper_proof_artifact: >-
    Public-safe synthetic investigation-agent acceptance harness: fake investigative tasks and mock
    APIs only; OpenAI/Anthropic/local-route stubs; OPA/Rego-style tool/action policy; no real secrets;
    held-out evals for success/hallucination/latency; injected prompt/tool/timeout/trace failures;
    credential-placeholder negative controls; human-only promotion decision; exact evidence manifest
    and rollback record. It must not use TRM systems, customer data, credentials, or third-party targets.

work_item:
  id: S07_TRM_AI_AGENT_PROMOTION_EVIDENCE_GATE_V1
  state: READY_FOR_ADMISSION
  next_consumer: S07_GTM_PROOF_KIT_BUILDER
  next_consumer_task_id: 6a506f6dc5c08191b95f1707d7f00c2d
  admission_note: >-
    Current Gen-133 reducer/preflight behavior requires an immutable S02 claim before S07 producer
    output can close downstream; S02 should bind this exact card/blob and acceptance evidence before build.
  acceptance: >-
    Produce exactly one public-safe two-minute promotion card that is materially sharper than a
    restatement of TRM's existing platform/process, preserves the hypothesis ceiling, cites these
    primary sources, and routes exact bytes to S04. If current TRM material already supplies an
    equivalent cross-control promotion contract, return HOLD/kill rather than polish redundancy.

strongest_falsifier: >-
  Kill this wedge if current TRM platform/process documentation already exposes a low-overhead,
  versioned promotion contract that binds held-out quality thresholds, credential/action policy,
  latency/cost evidence, trace completeness, explicit human approval, and rollback to the exact
  promoted agent/model/tool revision. In that case the proposed gift is redundant.

privacy: PUBLIC_SAFE_SYNTHETIC_ONLY
effect_ceiling: T0_PREP_RESEARCH_GIT
verifier:
  primary: S04_HRIST_STRUCTURAL_PREFLIGHT
  task_id: 6a52861fbdb08191b9ef33a0b9c3c15c
  same_provider_binding_weight: 0
  independent_followup_required_before_external_claim: true
expiry_utc: 2026-08-14T10:28:00Z

honest_flaw: >-
  TRM is already unusually mature in the exact controls this card targets: shared agent
  infrastructure, eval discipline, permission/audit surfaces, credential isolation, adversarial
  review, and human-only decisions. The live role also asks for strong backend/systems engineering;
  this proof kit can demonstrate judgment around agent reliability but cannot manufacture missing
  production-systems history. The role's work-authorization and applicant-specific eligibility
  were not checked or inferred.

evidence_digest_contract:
  canonicalizer: UTF8_LF_EXACT_BLOCK_V1
  canonicalization_rule: >-
    SHA-256 over the exact UTF-8 bytes between BEGIN_EVIDENCE_PREIMAGE_V1 and
    END_EVIDENCE_PREIMAGE_V1, excluding both marker lines, after CRLF-to-LF normalization,
    with no BOM and exactly one trailing LF after the final source line. No trimming,
    field sorting, URL rewriting, or case folding is permitted.
  evidence_preimage_utf8_bytes: 1411
  evidence_digest_sha256: 1f1adad150a5006d85dfdf833880ac75670fa777b4642c8711a31ccdb2f0277a
```

## Primary/current sources

1. **TRM Labs / Ashby — AI Agent Engineer - US Remote** — publication date not exposed; observed live **2026-08-08**: https://jobs.ashbyhq.com/trm-labs/828b60b2-ac8f-407d-92a0-8b794c8cf391
2. **TRM Tech Blog — Building an Agentic Software Factory** — **2026-05-22**: https://www.trmlabs.com/trm-tech-blog/building-an-agentic-software-factory-how-trm-re-architected-engineering-for-ai-leverage
3. **TRM Tech Blog — eBPF at Scale** — **2026-03-27**: https://www.trmlabs.com/trm-tech-blog/ebpf-at-scale-how-trm-labs-modernized-its-observability-stack-with-groundcover
4. **TRM Tech Blog — Never Give an AI Agent a Credential** — **2026-06-23**: https://www.trmlabs.com/trm-tech-blog/never-give-an-ai-agent-a-credential-a-broker-and-the-process-we-trusted-to-build-one

## Recomputable evidence preimage

BEGIN_EVIDENCE_PREIMAGE_V1
source_1|observed_utc_date=2026-08-08|source_date=NO_PUBLISH_DATE_EXPOSED|url=https://jobs.ashbyhq.com/trm-labs/828b60b2-ac8f-407d-92a0-8b794c8cf391|supports=live_US_remote_AI_Agent_Engineer_role;200k-275k_US_base;agent_framework;OpenAI_Anthropic_local_models;eval_loops;safe_observable_auditable_behavior;reasoning_latency_success_hallucination_metrics
source_2|observed_utc_date=2026-08-08|source_date=2026-05-22|url=https://www.trmlabs.com/trm-tech-blog/building-an-agentic-software-factory-how-trm-re-architected-engineering-for-ai-leverage|supports=AI_as_shared_platform;review_quality_prioritization_verification_as_bottleneck;shared_permissions_audit_logs_evals_feedback_loops;agentic_platform_consolidation_underway
source_3|observed_utc_date=2026-08-08|source_date=2026-03-27|url=https://www.trmlabs.com/trm-tech-blog/ebpf-at-scale-how-trm-labs-modernized-its-observability-stack-with-groundcover|supports=prior_observability_cost_model_did_not_scale;agentic_queries_carried_real_growing_cost_penalty;TRM_reports_over_80_percent_observability_cost_reduction_after_migration
source_4|observed_utc_date=2026-08-08|source_date=2026-06-23|url=https://www.trmlabs.com/trm-tech-blog/never-give-an-ai-agent-a-credential-a-broker-and-the-process-we-trusted-to-build-one|supports=credential_broker_keeps_secrets_out_of_agents;acceptance_criteria;demo_driven_verification;adversarial_review;human_owns_decisions
END_EVIDENCE_PREIMAGE_V1

## No-effect receipt

No application, outreach, email/DM, account creation, terms acceptance, purchase, paid call, deployment, merge, public publication outside this operator-controlled repository, private-data use, credential use, demand claim, or autonomous negotiation was performed.
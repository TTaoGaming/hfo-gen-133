# S08 GTM Target Card — Langfuse

```yaml
schema_id: hfo.gen133.gtm.target_card.v1
result: READY
seat: S08_GTM_TARGET_SCOUT
wip: 1
valid_time_utc: 2026-08-08T21:26:13Z
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
  slack_write_available: true
  task_inventory_read_available: true
  task_mutation_performed: false

target:
  company: Langfuse
  target: Langfuse agent evaluation / CI-CD release-gate platform
  species: PRODUCT_PLATFORM
  vertical: open-source AI engineering / observability / evaluation / agent quality
  route: RELATIONSHIP_ONLY
  current_signal: >-
    Langfuse is actively moving evaluation deeper into the production release loop. On 2026-05-25
    it launched a GitHub Actions experiment integration that can block pull requests when agent
    quality falls below a threshold against a versioned dataset. On 2026-05-28 it launched
    deterministic Python/TypeScript code evaluators for business-rule and schema checks, and on
    2026-07-10 it added structured tool-call access to code and LLM-as-a-Judge evaluators.
    Its current About page says Langfuse joined ClickHouse in January 2026 and continues building
    the open-source AI engineering platform.
  best_persona: >-
    Product engineering or integrations owner responsible for experiments, evaluators, CI/CD
    workflows, agent observability, and the boundary between release-quality evidence and
    production safety controls.
  public_bridge_person: >-
    Tobias Wochinger — source-backed Langfuse Product Engineer on the current About page and named
    author of the 2026-05-25 CI/CD gate launch and 2026-07-10 tool-call evaluator update.
    No partnership, procurement, roadmap ownership, or willingness to engage is inferred.

pain_hypothesis:
  status: HYPOTHESIS_NOT_COMPANY_FACT
  statement: >-
    Langfuse users may incur material release-review cycle time when an agent change passes quality
    evaluation but also changes tool authority, delegated identity, business-action policy, cost
    ceilings, or rollback requirements. Langfuse now supplies strong quality gates and structured
    tool-call evaluation, while its security documentation explicitly places run-time protective
    enforcement in external guardrail libraries and positions Langfuse around tracing and ex-post
    evaluation. A small evidence contract joining Langfuse release scores to an independent
    authorization/policy decision could reduce reviewer work for teams that need both quality and
    deterministic action boundaries. Public evidence does NOT establish that Langfuse customers
    experience this pain, that Langfuse should own runtime authorization, or that an extension is
    commercially desired.
  measurable_value_metric: >-
    Median engineering/reviewer hours from proposed agent revision to evidence-backed production
    approval, with failed releases caused by quality-policy mismatch as a secondary risk metric.
    No current baseline, savings amount, incident rate, or buyer budget is asserted.

hypothesis_evidence:
  for:
    - >-
      The 2026-05-25 experiment-action release can block a PR on an agent quality regression using
      a versioned dataset, proving that release gating is a first-class Langfuse workflow.
    - >-
      The 2026-07-10 evaluator update exposes structured tool-call names, arguments, IDs, and order,
      which creates enough evidence to test whether an agent selected or invoked expected tools.
    - >-
      Langfuse's current security-and-guardrails documentation says run-time security measures are
      provided by external security libraries while Langfuse traces and evaluates their behavior.
      That documents a real architectural boundary between observation/evaluation and enforcement.
  against:
    - >-
      Langfuse's 2026-05-28 code evaluators already support deterministic business-rule checks, and
      tool-call evaluators may be sufficient for many teams without any separate policy engine.
    - >-
      The CI/CD integration already supports threshold-based release blocking against versioned
      datasets, so a generic "agent release gate" would be redundant.
    - >-
      Runtime authorization may be intentionally out of scope for Langfuse. A policy-enforcement
      extension could add complexity without improving the platform's core observability/evaluation
      value proposition, and there is no source-backed demand signal for it.

proof_kit:
  two_minute_utility_gift: >-
    "Agent Release Evidence Contract — Eval x Tool Authority x Cost x Trace x Revision": a one-page
    before/after card that maps one exact agent revision to Langfuse experiment scores, required and
    forbidden tool calls, an external deterministic authorization verdict, a cost ceiling, trace
    completeness, human-approval condition, and rollback target. The card should clearly mark which
    controls Langfuse already provides and which are external.
  deeper_proof_artifact: >-
    Public-safe synthetic support/refund-agent harness using fake tickets, users, tools, and money.
    Instrument the agent with Langfuse; run a versioned held-out dataset and code evaluators; check
    recorded tool calls; evaluate cost; and compare state-changing actions against an independent
    OPA/Rego-style policy oracle. Inject quality regression, forbidden refund amount, wrong principal,
    missing trace, stale policy, budget overrun, and failed rollback cases. Emit one revision-bound
    pass/fail evidence manifest. Do not call Langfuse production accounts, use credentials, or use
    customer/private data.

work_item:
  id: S07_LANGFUSE_EVAL_TO_AUTHORITY_RELEASE_CONTRACT_V1
  state: READY_FOR_ADMISSION
  next_consumer: S07_GTM_PROOF_KIT_BUILDER
  next_consumer_task_id: 6a506f6dc5c08191b95f1707d7f00c2d
  admission_note: >-
    S07 should consume this exact target-card blob/digest and build only the two-minute public-safe
    release evidence contract first. The deeper harness is optional and should be killed if it
    merely rephrases Langfuse experiment-action plus code evaluators.
  acceptance: >-
    Produce exactly one concise release-contract artifact that preserves the hypothesis ceiling,
    cites current Langfuse primary sources, distinguishes evaluation from enforcement, includes
    one forbidden-tool negative control and one rollback condition, and does not claim Langfuse
    lacks controls that are not publicly documented.

strongest_falsifier: >-
  Kill this wedge if current Langfuse already provides a low-overhead native workflow that binds
  versioned experiment results, deterministic tool/action policy, identity/authority constraints,
  cost ceilings, trace completeness, human approval, and rollback to the exact promoted agent
  revision. Also kill it if real users treat runtime authorization as wholly separate from
  Langfuse and see no value in a release evidence bridge.

privacy: PUBLIC_SAFE_SYNTHETIC_ONLY
effect_ceiling: T0_PREP_RESEARCH_GIT
verifier:
  primary: S04_HRIST_STRUCTURAL_PREFLIGHT
  task_id: 6a52861fbdb08191b9ef33a0b9c3c15c
  same_provider_binding_weight: 0
  independent_followup_required_before_external_claim: true
expiry_utc: 2026-08-14T14:08:00Z

honest_flaw: >-
  Langfuse is already unusually strong in experiments, deterministic evaluators, tool-call
  inspection, and CI/CD release blocking. The proposed seam may be architectural adjacency rather
  than unmet pain, and runtime authorization may deliberately belong outside the product. The
  correct downstream result may therefore be a compact integration pattern or immediate
  falsification rather than a new extension.

evidence_digest_contract:
  canonicalizer: UTF8_LF_EXACT_BLOCK_V1
  canonicalization_rule: >-
    SHA-256 over the exact UTF-8 bytes between BEGIN_EVIDENCE_PREIMAGE_V1 and
    END_EVIDENCE_PREIMAGE_V1, excluding both marker lines, after CRLF-to-LF normalization,
    with no BOM and exactly one trailing LF after the final source line. No trimming,
    field sorting, URL rewriting, or case folding is permitted.
  evidence_preimage_utf8_bytes: 1196
  evidence_digest_sha256: f13b3de41e230da7fd89fe114409d23e894df0c23aa0f85ffffdd21699d4097a
```

## Primary/current sources

1. **Langfuse — Experiments CI/CD integration** — **2026-05-25**: https://langfuse.com/changelog/2026-05-25-experiment-ci-cd-gates
2. **Langfuse — Evaluate tool calls** — **2026-07-10**: https://langfuse.com/changelog/2026-07-10-evaluator-tool-calls
3. **Langfuse Docs — Security & Guardrails** — current page, checked **2026-08-08**: https://langfuse.com/docs/security-and-guardrails
4. **Langfuse — Code evaluators** — **2026-05-28**: https://langfuse.com/changelog/2026-05-28-code-evaluators
5. **Langfuse — About** — current page, checked **2026-08-08**: https://langfuse.com/about

## Recomputable evidence preimage

BEGIN_EVIDENCE_PREIMAGE_V1
source_1|observed_utc_date=2026-08-08|source_date=2026-05-25|url=https://langfuse.com/changelog/2026-05-25-experiment-ci-cd-gates|supports=GitHub_Actions_experiment_gate;versioned_dataset;quality_threshold;PR_blocking;release_regression_gate
source_2|observed_utc_date=2026-08-08|source_date=2026-07-10|url=https://langfuse.com/changelog/2026-07-10-evaluator-tool-calls|supports=structured_tool_call_access_in_evaluators;tool_name_arguments_and_call_id;code_and_LLM_judge_support
source_3|observed_utc_date=2026-08-08|source_date=UNDATED_CURRENT|url=https://langfuse.com/docs/security-and-guardrails|supports=runtime_security_handled_by_external_guardrail_libraries;Langfuse_tracing_and_ex_post_evaluation;security_monitoring
source_4|observed_utc_date=2026-08-08|source_date=2026-05-28|url=https://langfuse.com/changelog/2026-05-28-code-evaluators|supports=deterministic_python_typescript_evaluators;business_rule_checks;experiment_and_live_observation_scoring;no_network_egress
source_5|observed_utc_date=2026-08-08|source_date=UNDATED_CURRENT|url=https://langfuse.com/about|supports=Langfuse_open_source_AI_engineering_platform;joined_ClickHouse_January_2026;Tobias_Wochinger_Product_Engineer
END_EVIDENCE_PREIMAGE_V1

## No-effect receipt

No task mutation, account creation, terms acceptance, outreach, application submission, email/DM send,
purchase, paid tool call, deployment, publication outside this operator-controlled repository, merge,
private-data use, credential use, demand invention, or autonomous negotiation was performed.

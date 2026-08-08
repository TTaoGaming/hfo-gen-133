# S08 GTM Target Card — Portkey

```yaml
schema_id: hfo.gen133.gtm.target_card.v1
result: READY
seat: S08_GTM_TARGET_SCOUT
wip: 1
valid_time_utc: 2026-08-08T17:28:00Z
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
  company: Portkey
  target: Portkey Agent Gateway / MCP Gateway governance surface
  species: PRODUCT_PLATFORM
  vertical: production AI infrastructure / agent gateway / identity and policy enforcement
  route: RELATIONSHIP_ONLY
  current_signal: >-
    Portkey is actively expanding from an AI gateway into agent governance infrastructure.
    Its 2026-04-21 Agent Gateway launch entered beta with per-agent/team/user access control,
    budget limits, instant organization-wide policy changes, full agent/MCP traces, and an
    Agent Registry. On 2026-06-28 Portkey published a trust-boundary model for agent security
    centered on propagated principal identity and fail-fast policy enforcement. Its 2026-02-19
    Series A announcement reported $15M raised and named governance for agentic AI as a core
    investment priority, alongside 500B+ daily tokens, 120M daily requests, and $180M+ annualized
    AI spend under management at that date.
  best_persona: >-
    Product or platform engineering owner for Agent Gateway / MCP Gateway responsible for
    enterprise identity, authorization, policy controls, developer ergonomics, and safe
    production rollout of agent-control-plane changes.
  public_bridge_person: >-
    Rohit Agarwal — source-backed Portkey co-founder and CEO, author of the 2026-02-19 Series A
    announcement and co-author of the 2026-04-21 Agent Gateway launch. This card does not infer
    procurement authority, partnership interest, or willingness to engage.

pain_hypothesis:
  status: HYPOTHESIS_NOT_COMPANY_FACT
  statement: >-
    Portkey platform teams or Portkey customers may incur material review and promotion cycle
    time when changing agent identity, server/tool provisioning, guardrails, routing, or budget
    policy, because a small control-plane change can alter which principal or agent can reach
    which capability and under what constraints. A compact versioned regression artifact could
    reduce the work required to prove that a policy/config change did not unintentionally widen
    authority, break identity propagation, bypass budgets, or lose auditability. Public evidence
    establishes that these controls are consequential; it does NOT establish that Portkey lacks
    such testing internally, has a backlog, or wants an external extension.
  measurable_value_metric: >-
    Median reviewer/engineering hours from proposed agent-control-plane policy/config change to
    evidence-backed approval, with unauthorized-capability regressions caught before production
    as a secondary risk metric. No current baseline, incident rate, or savings amount is asserted.

hypothesis_evidence:
  for:
    - >-
      Portkey's 2026-06-28 trust-boundary article explicitly treats principal-inappropriate tool
      invocation, cost overruns, identity propagation, and fail-fast policy enforcement as agent
      security concerns; it describes assumed, delegated, and chained workload identity modes.
    - >-
      The 2026-04-21 Agent Gateway launch says access control can be scoped per agent, team, and
      user, with organization-wide policy changes applying instantly, while full traces capture
      agent runs and MCP calls. That makes policy/config changes high-leverage control-plane events.
    - >-
      Portkey's MCP Registry documentation, last modified 2026-05-07, exposes organization- and
      workspace-level capability provisioning, including enabling/disabling tools, resources,
      and prompts. These are concrete authority-changing configuration surfaces.
  against:
    - >-
      Portkey already centralizes authentication, access control, policy enforcement, budgets,
      guardrails, tracing, registry, and credential isolation; a generic governance or OPA layer
      would largely duplicate the product rather than add value.
    - >-
      Portkey may already have internal or non-public versioning, policy simulation, regression
      tests, approval workflows, and rollback mechanisms for these changes; absence from public
      docs is not evidence of absence.
    - >-
      The Agent Gateway was described as beta in April 2026 and the product surface is moving
      quickly, so a proof kit can become stale or be overtaken by native product changes.

proof_kit:
  two_minute_utility_gift: >-
    "Agent Authority Change Diff — Principal x Agent x Capability x Budget x Evidence": a one-page
    before/after review card that highlights newly reachable agents/tools/skills, identity-mode
    changes, widened workspace/user access, budget/routing deltas, six negative tests, and one
    explicit rollback condition. The artifact should be useful even if Portkey never engages.
  deeper_proof_artifact: >-
    Public-safe synthetic A2A + MCP authorization regression harness using only fake principals,
    agents, servers, tools, and budgets. Model assumed/delegated/chained identity; compare a
    versioned gateway-policy manifest against an independent OPA/Rego-style oracle; inject
    cross-tenant access, hidden-tool direct call, identity-loss, budget-bypass, stale-policy,
    and trace-correlation failures; emit a revision-bound evidence manifest and rollback verdict.
    Do not call Portkey production systems, create accounts, use credentials, or use customer data.

work_item:
  id: S07_PORTKEY_AGENT_AUTHORITY_CHANGE_REGRESSION_GATE_V1
  state: READY_FOR_ADMISSION
  next_consumer: S07_GTM_PROOF_KIT_BUILDER
  next_consumer_task_id: 6a506f6dc5c08191b95f1707d7f00c2d
  admission_note: >-
    S07 should consume this exact target-card blob/digest and build only the two-minute public-safe
    review artifact first. The deeper harness remains optional and must not be built merely to
    increase artifact volume.
  acceptance: >-
    Produce exactly one concise Agent Authority Change Diff that preserves the hypothesis ceiling,
    cites current Portkey primary sources, includes at least one negative-control case and one
    rollback condition, and is materially sharper than restating Portkey's own gateway controls.
    If current Portkey material already exposes equivalent versioned simulation/regression evidence,
    return HOLD/kill rather than polish redundancy.

strongest_falsifier: >-
  Kill this wedge if Portkey already provides a low-overhead native workflow that versions agent/MCP
  access-policy changes, computes before/after authority diffs, executes negative authorization and
  budget tests, binds the result to deployment approval, and supports auditable rollback to the exact
  prior policy/config revision. In that case the proposed gift is redundant.

privacy: PUBLIC_SAFE_SYNTHETIC_ONLY
effect_ceiling: T0_PREP_RESEARCH_GIT
verifier:
  primary: S04_HRIST_STRUCTURAL_PREFLIGHT
  task_id: 6a52861fbdb08191b9ef33a0b9c3c15c
  same_provider_binding_weight: 0
  independent_followup_required_before_external_claim: true
expiry_utc: 2026-08-14T14:08:00Z

honest_flaw: >-
  Portkey is a high technical fit partly because it already owns most of the relevant primitives.
  Public evidence establishes product velocity, scale, and the importance of agent trust boundaries,
  but not an unmet feature gap, partner demand, buyer, or willingness to adopt an external policy
  regression layer. The fastest correct outcome may be falsification, not a larger build.

evidence_digest_contract:
  canonicalizer: UTF8_LF_EXACT_BLOCK_V1
  canonicalization_rule: >-
    SHA-256 over the exact UTF-8 bytes between BEGIN_EVIDENCE_PREIMAGE_V1 and
    END_EVIDENCE_PREIMAGE_V1, excluding both marker lines, after CRLF-to-LF normalization,
    with no BOM and exactly one trailing LF after the final source line. No trimming,
    field sorting, URL rewriting, or case folding is permitted.
  evidence_preimage_utf8_bytes: 1178
  evidence_digest_sha256: bea6368a9c42ca90b7758286f93148e9887890cb93d21a2cea9b04c06cc7c736
```

## Primary/current sources

1. **Portkey — Why Every Agent Vulnerability is a Trust Boundary Failure** — **2026-06-28**: https://portkey.ai/blog/why-every-agent-vulnerability-is-a-trust-boundary-failure/
2. **Portkey Docs — MCP Registry** — last modified **2026-05-07**: https://portkey.ai/docs/product/mcp-gateway/mcp-registry
3. **Portkey — Introducing the Agent Gateway** — **2026-04-21**: https://portkey.ai/blog/agent-gateway/
4. **Portkey — Portkey Raises $15M Series A to Scale the Unified Control Plane for Production AI** — **2026-02-19**: https://portkey.ai/blog/series-a-funding/

## Recomputable evidence preimage

BEGIN_EVIDENCE_PREIMAGE_V1
source_1|observed_utc_date=2026-08-08|source_date=2026-06-28|url=https://portkey.ai/blog/why-every-agent-vulnerability-is-a-trust-boundary-failure/|supports=agent_trust_boundary_failures;principal_scoped_tool_access;cost_overrun_as_trust_boundary_risk;agent_workload_identity;assumed_delegated_chained_identity;policy_enforced_at_control_plane
source_2|observed_utc_date=2026-08-08|source_date=2026-05-07|url=https://portkey.ai/docs/product/mcp-gateway/mcp-registry|supports=MCP_registry;organization_and_workspace_capability_provisioning;tool_resource_prompt_enable_disable;blocked_capabilities_return_errors;enterprise_auth_access_logging
source_3|observed_utc_date=2026-08-08|source_date=2026-04-21|url=https://portkey.ai/blog/agent-gateway/|supports=Agent_Gateway_beta;governance_access_control_per_agent_team_user;budget_usage_limits;instant_policy_changes;full_agent_and_MCP_traces;agent_registry
source_4|observed_utc_date=2026-08-08|source_date=2026-02-19|url=https://portkey.ai/blog/series-a-funding/|supports=15m_series_A;agentic_governance_priority;500b_plus_daily_tokens;120m_daily_requests;180m_plus_annualized_AI_spend_under_management;Rohit_Agarwal_cofounder_CEO
END_EVIDENCE_PREIMAGE_V1

## No-effect receipt

No task mutation, account creation, terms acceptance, outreach, application submission, email/DM send,
purchase, paid tool call, deployment, publication outside this operator-controlled repository, merge,
private-data use, credential use, demand invention, or autonomous negotiation was performed.

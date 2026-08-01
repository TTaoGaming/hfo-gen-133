---
schema_id: hfo.gen133.s08.research_evidence_card.v1
card_id: S08_CLAUDE_CODE_ACTION_GITHUB_NATIVE_BRIDGE_20260801T152728Z
result: REVISE
callsign_or_seat: S08_RESEARCH_CANDIDATE_SCOUT
carrier_task_id_expected: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_observed: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_match: true
carrier_identity_claim: DISPOSABLE_SCHEDULED_CARRIER_NOT_LINEAGE
controller: operator_direct
wip: 1
valid_time_utc: 2026-08-01T15:27:28Z
transaction_time_utc: SEE_GITHUB_COMMIT_METADATA
canonical_repository: TTaoGaming/hfo-gen-133
canonical_branch: agent/gen133-bootstrap-20260730
repository_head_observed_before_write: 9b2bc6c30cc2753ba0cd27469bac75dc0c403eb0
research_lane: agent_runtime_cots_capabilities
candidate_name: Anthropic_Claude_Code_GitHub_Action
candidate_repository: anthropics/claude-code-action
candidate_released_ref: v1.0.133
candidate_released_commit: 787c5a0ce96a9a6cfb050ea0c8f4c05f2447c251
candidate_main_head_observed: be7b93b1907a4abad570368f3c74b6fe3807510b
candidate_main_embedded_claude_code_version_observed: 2.1.220
privacy_class: PUBLIC_PRIMARY_SOURCES_AND_SANITIZED_REPOSITORY_POINTERS_ONLY
effect_ceiling: FILE_AND_SANITIZED_SLACK_POINTER_ONLY
expiry_utc: 2026-08-03T15:27:28Z
verifier: Sigrun/P4_APEX_FALSIFICATION_or_other_distinct_nonproducer
consumer: Olrun/Claude-Dispatch_and_Ratatoskr/P7_PLATFORM_ADAPTER_DECISION
fitness_credit: ZERO_UNTIL_EXACT_WORKITEM_CONSUMER_ACK
sealed: false
---

# S08 evidence card — Claude Code GitHub Action as a GitHub-native bridge

## Changed queue edge and bounded uncertainty

The prior S08 card at commit `461db44eb16de9043769cd4b06e62c9a32d45438`
completed the `grants_jobs_income_opportunities` lane. The explicit rotation therefore
advances to `agent_runtime_cots_capabilities`.

A newer canonical receipt at commit
`2dc204ec67a1d9112032159530790f1a81fb0e42`, blob
`5d8fd3953344e7dc61b797e9373a8c14eb5d87a1`, identifies the changed uncertainty:
ChatGPT Cloud can produce and route bounded Git work, but Claude Desktop / Olrun
has no visible machine-readable ingress and return through the shared GitHub +
Slack plane. The previous verifier route expired at `2026-08-01T15:09:29Z`; this
research cannot retroactively close it.

**Question:** can Anthropic's official Claude Code GitHub Action provide a bounded,
GitHub-native executor/return path for future `READY_FOR_CLAUDE` packets, without
pretending it is Claude Desktop, adding an ungoverned scheduler, or requiring the
operator to ferry prose between platforms?

## Decision

`REVISE`.

Admit the Action only as a candidate for a future operator-approved, one-repository
micro-use. Do **not** call it the current Claude Desktop bridge and do not use it to
launder an expired distinct-verifier route.

The official Action has several useful primitives: GitHub event or explicit-prompt
activation, execution on a GitHub runner, repository file operations, commits,
custom MCP configuration, turn limits, and JSON-schema-backed structured outputs.
Those primitives could emit a machine-readable Git receipt with a named
runtime/model and exact result.

However, the candidate does not directly satisfy the current cross-platform edge:

1. it is a GitHub Actions runtime, not Claude Desktop or the existing Olrun host loop;
2. the official security contract limits an invocation to the repository where it
   was triggered, while the current verifier edge spans Gen-133 packet state and a
   separate `TTaoGaming/TAGS` branch;
3. Slack ingress/egress is not built in; a Slack MCP server would be additional
   connector code/configuration, secrets, permissions, and prompt-injection surface;
4. setup requires repository-admin and credential/security effects that this carrier
   is forbidden to perform;
5. an Actions `schedule` would be another clock, and GitHub warns schedules may be
   delayed or dropped and run only from the default branch;
6. the stable released ref observed is `v1.0.133`, while `main` has newer unreleased
   commits. Production use should not pin the moving `@v1` or `main`; GitHub's secure
   use guidance requires a verified full-length commit SHA for immutability.

The preferred experiment is therefore an event-triggered, read-only or
branch-only micro-use on one repository, not cron polling and not a full Slack
bridge.

## Self-probe

```yaml
expected_task_id: 6a526109ba348191b5f23ad3172ad568
observed_task_id: 6a526109ba348191b5f23ad3172ad568
task_id_match: true
tools_observed:
  github_connector: authenticated_read_write_and_exact_file_readback
  slack_public_channel: authenticated_read_write
  web_primary_sources: read
  shell_or_browser_runtime: unavailable
  private_connectors: not_used
  task_mutation: not_called
```

## Exact candidate and dated primary sources

Observed `2026-08-01`:

1. Anthropic official repository and released ref:
   `anthropics/claude-code-action@v1.0.133`, full commit
   `787c5a0ce96a9a6cfb050ea0c8f4c05f2447c251`.
   https://github.com/anthropics/claude-code-action/tree/v1.0.133
2. Released README, blob `b0b5c73821c138b8aefe0b26dc9f269670b03b28`:
   https://github.com/anthropics/claude-code-action/blob/v1.0.133/README.md
3. Action contract, blob `1d6270a9d47a53b1c3d861ed34ccf0a620780933`:
   https://github.com/anthropics/claude-code-action/blob/v1.0.133/action.yml
4. Capabilities and limitations, blob
   `742f13852ff4adddf16116e00aab4a5b1006a649`:
   https://github.com/anthropics/claude-code-action/blob/v1.0.133/docs/capabilities-and-limitations.md
5. Security contract, blob `7a07dea60f3f0c74665c4ca41f5dbde053d49d70`:
   https://github.com/anthropics/claude-code-action/blob/v1.0.133/docs/security.md
6. MCP and permissions configuration, blob
   `eb352b3493a5b4828daa9732f47e8f2e96b406d7`:
   https://github.com/anthropics/claude-code-action/blob/v1.0.133/docs/configuration.md
7. Scheduled-maintenance example, blob
   `088d6cf160d2a6cd37dd300963348c41b466cbd0`:
   https://github.com/anthropics/claude-code-action/blob/v1.0.133/docs/solutions.md
8. MIT license, blob `3fa6a64e52f30d3ad836f98b3f0da6f4b6263bb8`:
   https://github.com/anthropics/claude-code-action/blob/v1.0.133/LICENSE
9. Anthropic official repository main head observed at
   `be7b93b1907a4abad570368f3c74b6fe3807510b`, dated `2026-07-25`, which bumps
   embedded Claude Code / Agent SDK to `2.1.220` / `0.3.220` but is not the released
   ref selected for this card.
10. GitHub official secure-use guidance:
    https://docs.github.com/en/actions/reference/security/secure-use
11. GitHub official schedule semantics and failure caveats:
    https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows#schedule
12. GitHub official Actions billing contract:
    https://docs.github.com/en/billing/concepts/product-billing/github-actions
13. Anthropic official Claude Code authentication and plan documentation:
    https://docs.anthropic.com/en/docs/claude-code/getting-started
14. Anthropic official pricing page:
    https://www.anthropic.com/pricing

## Supported claims

- The Action can respond to GitHub PR/issue events or run automation with an
  explicit prompt.
- It runs on a GitHub runner and can expose a structured JSON output when a JSON
  schema is supplied.
- The released action accepts Anthropic API credentials, a Claude Code OAuth token,
  workload identity federation, Bedrock, Vertex, or Foundry configuration.
- Custom MCP servers can be added through `--mcp-config`; tools still require an
  explicit allowlist.
- `--max-turns` can bound a run.
- Default tool access is restricted; arbitrary Bash must be explicitly allowed.
- The Action cannot approve or merge pull requests and does not provide arbitrary
  cross-repository authority by default.
- Its code is MIT-licensed, but the model service, GitHub App, cloud provider,
  connectors, and external MCP servers remain governed by their own terms.
- Standard GitHub-hosted runner use is currently free for public repositories;
  private repositories use included minutes and then metered billing.

## Excluded claims

- No claim that the Action is Claude Desktop, Olrun, or an already-wired host loop.
- No claim that it has consumed any Gen-133 packet or produced a distinct verdict.
- No claim that same-vendor Claude execution is independent unless a direct return
  names the actual provider/model/runtime and a distinct decision-maker consumes it.
- No claim that a Slack MCP server is installed, authenticated, safe, or compatible.
- No claim that one workflow can safely read/write both `hfo-gen-133` and `TAGS`
  without explicit cross-repository design and credentials.
- No claim that `v1.0.133` is the newest source commit; it is the stable released ref
  observed, while `main` is newer.
- No claim that `@v1`, a tag, or `main` is immutable.
- No claim that scheduled workflows are exact, durable, or guaranteed to run.
- No claim of zero cost. Model usage, private-repository Actions minutes, cloud
  provider charges, and connector costs depend on the chosen authentication and
  runtime path.
- No GitHub App installation, secret creation, workflow commit, credential read,
  account action, terms acceptance, or live execution occurred.

## License, terms, security, cost, and operator burden

```yaml
software_license: MIT
third_party_terms_uncertainty:
  - Anthropic model_service_and_Claude_Code_terms
  - GitHub_Actions_and_GitHub_App_terms
  - selected_auth_provider_terms
  - any_Slack_or_other_MCP_server_license_and_data_handling
credentials_required_for_live_use: yes
credentials_used_this_run: none
direct_research_cost_usd: 0
estimated_operator_minutes_for_safe_single_repo_setup: 45_to_90
estimated_operator_minutes_for_cross_repo_plus_slack_design: 90_to_180
estimated_operator_minutes_per_successful_automated_run_after_setup: 0_to_5
estimated_operator_minutes_avoided_per_future_manual_ferry: 5_to_15
exact_per_run_model_cost: UNKNOWN_WITHOUT_AUTH_PATH_MODEL_AND_TOKEN_LOGS
```

Security gates for any future test:

- pin `anthropics/claude-code-action` to the verified full commit
  `787c5a0ce96a9a6cfb050ea0c8f4c05f2447c251`, not `@v1` or `main`;
- use a sandbox or single target repository;
- use the minimum GitHub token permissions;
- forbid untrusted issue/comment bodies as prompts;
- keep full output disabled;
- use no Slack connector in the first micro-use;
- allow no Bash beyond exact read-only test commands;
- set a small `--max-turns` ceiling and a workflow timeout;
- require structured output fields for runtime, model, source digest, commands,
  exit codes, verdict, rollback, and honest flaw;
- treat the return as nonbinding until a distinct consumer acknowledges it.

## Strongest objection

This candidate may be architecture drift disguised as integration. The current
problem is the existing Claude Desktop / Olrun loop failing to surface receipts.
Installing a second Claude runtime inside GitHub Actions could bypass rather than
repair that loop, create another credential-bearing scheduler, and produce more
unconsumed artifacts. Cross-repository and Slack requirements could erase most of
the COTS advantage and increase secret and prompt-injection exposure.

## Strongest falsifier

`RETIRE` the candidate for the current bridge lane if any one holds:

1. an operator-approved sandbox run cannot emit a digest-bound structured return
   with actual runtime/model identity, source readback, exact command results, and
   honest flaw;
2. the required packet and target code cannot be reconciled inside one repository
   without broad cross-repository credentials or packet duplication;
3. Slack ingress/ConsumerAck requires a custom connector whose permissions,
   licensing, or privacy cost exceeds the existing Olrun repair;
4. the Action cannot run with least-privilege permissions and an immutable pinned
   release;
5. per-run model or Actions cost cannot be bounded without enabling spend or
   auto-reload;
6. the workflow becomes another polling scheduler rather than an event-triggered
   adapter;
7. Olrun's existing host loop is repaired with fewer operator minutes and less
   credential surface.

`ADMIT` only after one reversible micro-use passes every gate and a named WorkItem
consumes the exact result.

## Reversible next experiment

After explicit operator approval for account/security effects, run exactly one
sandbox experiment owned by the COTS/adapter lane:

```text
trigger: workflow_dispatch only
repository: one sandbox or one exact target repository
permissions: contents:read unless one isolated branch write is explicitly approved
action: anthropics/claude-code-action@787c5a0ce96a9a6cfb050ea0c8f4c05f2447c251
input: one immutable packet digest and one harmless verification command set
mcp: none
bash: exact read-only commands only
max_turns: 2
timeout: 10 minutes
output: strict JSON schema with runtime/model/source digest/commands/exit codes/verdict/flaw
world effects: no issue comment, PR, merge, Slack post, deployment, or account change
```

Compare setup minutes, run latency, model/provider identity, exact output, and
manual-ferry minutes against the existing Olrun route. Stop after one run. Do not
add cron or a Slack MCP server until the single-repository return is independently
consumed.

## Verifier, consumer, expiry, and honest flaw

- **Verifier:** Sigrun/P4 or another distinct nonproducer should challenge whether
  this is a repair or a bypass, whether cross-repository access is avoidable, and
  whether the return would be genuinely independent.
- **Consumer:** Olrun/Claude-Dispatch and Ratatoskr/P7 may either admit one exact
  sandbox WorkItem or reject the candidate with evidence. Reginleif must not mutate
  Scheduled Tasks for this card.
- **Expiry:** `2026-08-03T15:27:28Z`; revalidate the official release, security
  contract, and pricing after expiry.
- **Credit:** zero until a WorkItem records `CONSUMED` or
  `REJECTED_WITH_EVIDENCE` against this exact Git blob.

Honest flaw: no live Action run, GitHub App installation, credential path, billing
view, Slack MCP server, cross-repository fetch, or Claude Desktop process was
inspected. The release page and tagged source establish documented capability, not
fitness in TTao's environment. The most recent source commits are newer than the
stable release selected here, so both stale-release risk and moving-main risk
remain. This is same-provider advisory research with binding weight zero.

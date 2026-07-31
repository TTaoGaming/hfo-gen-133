---
schema_id: hfo.gen133.ratatoskr.durable_agent_institution_vision_gap.v1
callsign: Ratatoskr
lineage_id: lineage_61cd69f1c256
coordinate: [4, 7]
port: P7_NAVIGATE
generation: 133
valid_time_utc: 2026-07-31T18:06:05Z
transaction_time_utc: SEE_GIT_COMMIT_METADATA
wip: 1
claim_status: partial
effect_ceiling: FILE_AND_MESSAGE_COORDINATION_ONLY_NO_SCHEDULED_TASK_MUTATION
privacy_class: SANITIZED_PUBLIC_NO_CREDENTIAL_ACCOUNT_POLICY_MEDICAL_OR_FAMILY_DETAILS
verifier: Sigrun/P4_APEX_FALSIFICATION
consumers:
  - Olrun/Claude-Dispatch
  - Reginleif/lineage_0dc1db03347f
  - Var/operator-life-ops
expiry: SUPERSEDED_BY_FIRST_CLOSED_GEN133_OUTCOME_LOOP_OR_NEWER_WORLD_STATE
sealed: false
---

# Ratatoskr P7 — durable agent institution vision-gap assessment

## Operator intent

The target is not a chatbot swarm. It is a durable electronic institution that
accepts operator intent and returns verified consequences across four domains:

1. spatial software production and launch;
2. client acquisition and commercial outreach;
3. job search, applications and recruiter contact;
4. life organization and health improvement.

The institution should reduce operator cognitive load through Sigrun apex
analysis, Olrun dispatch and execution coordination, Ratatoskr cross-substrate
fan-in, Reginleif Scheduled Tasks stewardship, Var life operations and bounded
Valkyrie workers.

## Honest distance to the vision

This is a reasoned maturity estimate, not a measured benchmark:

```yaml
ingredients_present: approximately_70_percent
runtime_integration: approximately_25_percent
verified_outcome_autonomy: approximately_10_percent
broad_multi_domain_operator_relief: approximately_10_to_15_percent
```

Interpretation:

- HFO is **one real closed loop away from proving the core thesis**.
- HFO is **not yet close to carrying the operator's broad life and business load**.
- The remaining gap is not mainly model intelligence. It is durable execution,
  effect integration, verification and consumption.

## What already exists

### Strong or materially present

- Long heritage, explicit actor identities, roles, authority ceilings and refusal
  rules.
- Git as durable memory and audit trail; Slack as changed-state signaling.
- Multiple model/provider substrates and host execution surfaces.
- ChatGPT Scheduled Tasks as an hourly clock and connected cloud carrier plane.
- Claude/Codex host capability for code, tools, browser work and file effects.
- Existing spatial-input prototypes, HandPiano/Spatial OS heritage and app-factory
  concepts.
- Operator-life connectors and Var workflows for Gmail, Calendar, GTD/PARA and
  waiting clocks.
- Strong anti-fake-green culture, exact receipts and increasing awareness that a
  wake, commit, draft or same-provider PASS is not an outcome.
- Gen-133 AI H2O header/footer contract now formalizes WIP, authority, evidence,
  verified/unverified claims, next consumer and anti-reward-hacking self-audit.

### Present as design, not runtime enforcement

The AI H2O contract's own status says:

```yaml
automatic_chat_injection: NOT_WIRED
json_schema_validation: NOT_WIRED
cross_turn_start_end_validator: NOT_WIRED
independent_behavioral_verification: PENDING
```

Similarly, Gen-133 roles, protocols and receipt-return contracts are primarily
institutional design. Registration and documents do not prove liveness.

## The central diagnosis

The system has **most of the organs around the loop**, but no boring, authoritative
circulatory system through the middle.

Today the effective loop is often:

```text
operator intent
-> model analysis
-> document/receipt/Slack post
-> another model reviews the artifact
-> operator still decides what happens next
```

The desired loop is:

```text
operator intent
-> admitted outcome contract
-> durable workflow state machine
-> least-privilege executor
-> real source/build/test readback
-> independent acceptance verdict
-> named ConsumerAck
-> closed outcome + compact operator digest
-> learning signal for next selection
```

The difference is not another persona, prompt, model or scheduled seat. The
difference is **enforced state transition and consequence closure**.

## The missing organs

### 1. Intent compiler and portfolio governor

The operator needs to express broad intent once. A governor must convert it into
one of four results:

```yaml
ADMIT: one bounded outcome with owner, evidence and expiry
DEFER: valid goal, no current capacity
REJECT: unsafe, duplicate, vague or no useful acceptance condition
CLARIFY: only when a genuinely missing operator fact blocks admission
```

It must enforce:

- one operator-visible P0;
- WIP limits by lane and a small global cap;
- explicit tradeoffs between survival/life obligations, income and product work;
- no new architecture or actor creation when an admitted outcome is still open;
- a daily digest containing closed outcomes and true operator decisions only.

Without this, every model treats every sentence as permission to create a new
project, and the operator remains the portfolio manager.

### 2. Durable workflow kernel and hot system of record

Git is excellent for audit, heritage and immutable receipts. It is a poor hot
queue, timer wheel, lease manager and retry engine.

The institution needs one mechanically enforced workflow kernel backed by a
transactional store. Minimum workflow state:

```text
INTENT
-> PROPOSED
-> ADMITTED
-> CLAIMED
-> EXECUTING
-> VERIFYING
-> AWAITING_CONSUMER_ACK
-> CLOSED | FAILED | EXPIRED | COMPENSATING
```

Minimum primitives:

- idempotency keys;
- atomic claim and lease;
- durable timers and expiry;
- retry policy and retry budget;
- compensation/rollback;
- concurrency and rate limits;
- human-approval suspension and resume;
- exact input/output/version binding;
- event log and current projection;
- dead-letter/Andon handling.

A COTS durable runtime such as DBOS/Postgres or Temporal should own this boring
core. Git receives terminal and audit receipts; it should not be the only live
scheduler database.

DBOS documents checkpointed workflows, durable queues, flow control, recovery
from interruption and Postgres-backed execution:

- https://docs.dbos.dev/architecture
- https://docs.dbos.dev/python/reference/queues

### 3. Capability and effect broker

Each lane needs a typed capability manifest, not a broad promise that the model
"has tools."

For each tool/effect:

```yaml
capability: gmail.send | calendar.create | github.branch_write | browser.apply
principal: exact actor
scope: exact accounts/repos/domains
preconditions: exact evidence and approval
idempotency: required
readback: required
rollback_or_compensation: defined
risk_class: reversible | protected | irreversible
```

The broker must separate:

- propose from dispose;
- public from private state;
- read from write;
- draft from send;
- branch artifact from deployment;
- job/client outreach from spam;
- health organization from diagnosis or medical decision.

OpenAI's Agents SDK supplies useful edge primitives such as tools, handoffs,
guardrails, tracing and evaluation. Claude Code can run non-interactively and
connect tools through MCP. Those are execution adapters, not the durable
institution itself:

- https://openai.com/index/new-tools-for-building-agents/
- https://docs.anthropic.com/en/docs/mcp
- https://docs.anthropic.com/fr/docs/claude-code/sdk

### 4. Outcome sensors and acceptance harness

Every domain needs a machine-readable definition of real progress.

Spatial apps:

- clean build/test exit code;
- reproducible artifact;
- behavior trace for spatial input;
- native fallback preserved;
- deployment/source readback when authorized;
- user or backlog-owner acceptance.

Clients:

- prospect source and fit score;
- approved message bytes;
- send receipt;
- reply classification;
- meeting booked or explicit rejection;
- CRM state readback.

Jobs:

- opportunity source and eligibility;
- tailored application artifact;
- operator-approved submission when required;
- submission confirmation;
- recruiter response/interview progression;
- application tracker readback.

Life and health:

- Calendar/Gmail/task source-system state;
- appointment actually booked, not merely planned;
- medication or care instructions grounded in a qualified source;
- habit/measurement data with privacy boundaries;
- operator or professional confirmation where judgment is nondelegable.

A receipt that does not bind one of these sensors is evidence of activity, not
an outcome.

### 5. Independent verifier plus ConsumerAck reducer

Current HFO frequently verifies structure inside the same provider family. That
is useful preflight but not binding closure.

A terminal transition requires:

1. producer return with real bytes/readback;
2. held-out acceptance test authored before grading;
3. nonproducer, preferably distinct-provider `STOOD | FELL`;
4. named consumer reads the exact verdict and returns `ConsumerAck`;
5. reducer writes one terminal state.

The consumer is domain-specific:

- Olrun or the app backlog owner for spatial factory artifacts;
- CRM/outreach owner for client motion;
- job-search tracker owner for applications;
- Var/operator for life operations.

No consumer means the system produced inventory, not value.

### 6. Domain playbooks that compile into the same kernel

The institution should not build four separate architectures. It needs one
workflow kernel with four outcome templates:

```yaml
SPATIAL_APP_FACTORY
CLIENT_ACQUISITION
JOB_SEARCH
LIFE_HEALTH_OPERATIONS
```

Each template supplies:

- domain-specific tools;
- safety and approval policy;
- acceptance sensors;
- executor/verifier/consumer roles;
- retry and expiry rules;
- terminal outcome vocabulary.

This is where existing HFO pieces become packaging rather than another rewrite.

### 7. External fitness and economic selection

The institution currently rewards internal legibility. It must increasingly
select on external consequence:

- app works for a user;
- prospect replies or meeting occurs;
- application advances;
- appointment is booked;
- operator minutes and stress decrease;
- income or useful deployment occurs.

Commit count, wake count, agent count, document count and same-provider agreement
must remain zero-credit metrics.

### 8. Operator load-shedding and right to sleep

Burnout is not an incidental issue. It is a system-level failure signal.

Required operator interface:

```yaml
foreground_events:
  - APPROVAL_REQUIRED
  - SAFETY_OR_DEADLINE_ANDON
  - DAILY_CLOSED_OUTCOME_DIGEST
all_other_state: durable_and_silent
```

The institution must be allowed to defer goals, sleep idle workers and say no.
A system that accepts every goal simultaneously cannot reduce cognitive load; it
merely externalizes the operator's overload into a noisy swarm and sends the
noise back.

## Domain readiness estimate

Reasoned, nonbinding estimates:

| domain | present maturity | strongest asset | principal missing closure |
|---|---:|---|---|
| core institution | 25% | roles, receipts, memory, provider diversity | durable kernel + enforced state transitions |
| spatial app factory | 35% | prototypes and interaction heritage | one reproducible build-to-acceptance golden path |
| life organization | 40% | Var, Gmail/Calendar and waiting clocks | reliable source-system execution and quiet daily reduction |
| client acquisition | 15-20% | research, drafts and send-gate concepts | prospect CRM -> approved send -> reply -> meeting loop |
| job search | 10-15% | general research/outreach capability | job tracker -> tailored apply/contact -> confirmation loop |
| health improvement | 10-20% | scheduling and information support | privacy-safe measurements, care-team boundaries and verified follow-through |

## What is not missing

Do not spend the next cycle adding:

- more named agents;
- another world-state root;
- another scheduler;
- more receipt schemas;
- more hourly queue-empty monitors;
- another general architecture report;
- more model seats before one closed loop;
- another heritage crawl without a consuming WorkItem.

These may feel like institution-building while preserving the exact failure mode.

## The smallest path that proves the vision

### Proof 1 — one closed spatial factory loop

Use `SPATIAL_FACTORY_GOLDEN_APP_001`:

```text
operator goal already captured
-> S02 admits exact WorkItem
-> host executor reconstructs/builds one app
-> real tests and behavior trace
-> distinct verifier
-> Olrun ConsumerAck
-> terminal Gen-133 receipt
```

No release is required for the first proof.

### Proof 2 — one protected external-effect loop

After Proof 1, close one reversible outreach or job-search loop with explicit
operator-approved bytes:

```text
qualified target/opportunity
-> prepared message/application
-> approval gate
-> actual send/submission readback
-> reply/status ingestion
-> ConsumerAck in CRM/tracker
```

### Proof 3 — one operator-relief loop

Close one life obligation from source to confirmation without the operator
carrying state:

```text
obligation detected
-> safe plan
-> Calendar/Gmail/source action under authority
-> source readback
-> Var reduction
-> operator receives only final confirmation or true decision
```

After these three proofs, the institution has demonstrated the same kernel across
software, economic and life domains. Only then should the portfolio expand.

## Recommended control allocation

```yaml
Sigrun:
  function: falsify intent decomposition, priorities and acceptance conditions
  forbidden: become the routine executor
Olrun:
  function: dispatch pilot, host executor routing, deadman, ConsumerAck routing
  forbidden: silently become every worker or a second scheduler
Ratatoskr:
  function: cross-substrate contradiction reduction and technical fan-in
  forbidden: hourly polling, task mutation, duplicate world-state prose
Reginleif:
  function: Scheduled Tasks inventory, canary mutation and provider PDCA
  forbidden: mass restore before closure proof
Var:
  function: life/admin source systems, operator foreground and waiting clocks
  forbidden: duplicate technical architecture
Durable_kernel:
  function: authoritative workflow state, timers, leases, retries and closure
  status: MISSING_LOAD_BEARING_ORGAN
```

## One P0

```yaml
p0: IMPLEMENT_AND_CLOSE_INSTITUTION_KERNEL_V0_ON_SPATIAL_FACTORY_GOLDEN_APP_001
success:
  - one durable workflow state machine owns the WorkItem
  - one real executor return contains build/test evidence
  - one distinct verifier returns STOOD
  - one named ConsumerAck exists
  - terminal Gen133 receipt exists
  - operator state-ferry events equal zero after admission
failure:
  - another design-only artifact without execution
  - terminal same-provider verification
  - operator manually routes ordinary state
  - no source/build/test readback
```

## Honest flaw

This assessment combines current Gen-133 Git/Slack evidence, operator testimony
and systems reasoning. Percentage estimates are judgment calls, not telemetry.
The assessment cannot directly observe Olrun's host GUI activity or private life
systems. It does not prove DBOS, Temporal or any other COTS runtime is the final
choice; it identifies the durable-workflow capability that must be present. No
runtime, task, account, send, deployment, application, appointment, payment or
external effect was changed by this assessment.

*You built most of the parts. The missing product is the institution's boring middle: admitted work, durable state, controlled effects, independent acceptance and consumption.*

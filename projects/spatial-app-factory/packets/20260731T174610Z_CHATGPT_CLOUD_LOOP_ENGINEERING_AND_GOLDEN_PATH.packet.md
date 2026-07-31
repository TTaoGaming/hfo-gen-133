---
schema_id: hfo.gen133.ratatoskr.chatgpt_cloud_loop_engineering_packet.v1
packet_id: CHATGPT_CLOUD_SPATIAL_FACTORY_LOOP_20260731T174610Z
callsign: Ratatoskr
lineage_id: lineage_61cd69f1c256
coordinate: [4, 7]
port: P7_NAVIGATE
mode: GEN133_CLEAN_APEX_OPERATOR_CONSOLE
generation: 133
valid_time_utc: 2026-07-31T17:46:10Z
transaction_time_utc: SEE_GIT_COMMIT_METADATA
canonical_repo: TTaoGaming/hfo-gen-133
canonical_branch: agent/gen133-bootstrap-20260730
head_observed_before_write: 07d91a380f3e2a72b4bb51c8a2d62630bbf2b0c1
wip: 1
claim_status: proposed_design_only
effect_ceiling: FILE_AND_MESSAGE_COORDINATION_ONLY_NO_SCHEDULED_TASK_MUTATION
privacy_class: SANITIZED_PUBLIC_NO_CREDENTIAL_ACCOUNT_POLICY_MEDICAL_OR_FAMILY_DETAILS
verifier: Sigrun/P4_APEX_FALSIFICATION
consumers:
  - Olrun/Claude-Dispatch
  - Reginleif/lineage_0dc1db03347f
expiry: SUPERSEDED_BY_NEWER_EXPLICIT_OPERATOR_DIRECTIVE_OR_ACCEPTED_GEN133_LOOP_RECEIPT
sealed: false
---

# ChatGPT Cloud loop engineering for the Gen-133 spatial app factory

## Decision

Use ChatGPT Cloud as a **clocked, connected co-processor**, not as the autonomous
apex and not as a pretend local coding runtime.

The native Scheduled Tasks surface supplies hourly self-wakes. Olrun supplies an
out-of-band watchdog and browser nudge only when the native loop misses a material
edge. The manual GPT-5.6 Pro Ratatoskr console performs rare high-reasoning fan-in
and contradiction reduction. Code execution, builds, tests, browser QA and other
host effects stay on Claude/Codex/host-PC workers.

The operator should not carry ordinary state between these surfaces. The target
operator interaction is one bounded daily digest plus explicit authority packets
for private or irreversible effects.

This packet proposes a control contract and a staged 15-seat portfolio. It does
**not** mutate any Scheduled Task, prompt, schedule, enabled state, account
setting, scheduler root, world-state root, chain, or roster.

## Current facts and constraints

### HFO state

- Gen-133 is the canonical forward repository but is not yet the live metabolism.
- The freshest direct ChatGPT provider state available to this carrier remains
  `4/15` enabled: `S01`, `S04`, `S05`, `S15`.
- The central pickup/reducer seats `S02` and `S03`, scheduler witness `S10`, bridge
  cells and experiment cells are disabled.
- Existing surviving seats prove wake, Git durability, operator relief and local
  structural pressure. They do not prove a useful Gen-133 work cycle.
- The previous spatial tournament lane was retired because it had no admitted
  operator packet, current prototype, acceptance run, buyer evidence or consuming
  pipeline. Its retirement was evidence-specific, not a permanent ban on spatial
  work.
- Thrud heritage already points to a prior HandPiano/Spatial OS public-proof
  inventory and a demo-ready no-egress receipt. Reuse should begin from pinned
  heritage and a real build readback, not another market-research loop.

### Native ChatGPT Scheduled Tasks

Current OpenAI product constraints that matter to the design:

- Pro accounts can have up to 15 active Scheduled Tasks.
- Tasks cannot run more frequently than hourly.
- Monitoring tasks remember previous runs and can notify only on meaningful
  change.
- Unattended tasks may automatically pause after inactivity or when additional
  action is needed.
- Tasks can use connected apps when available, but do not support webhooks.
- A task created inside a ChatGPT Project cannot rely on that Project's files.
  Load-bearing inputs must therefore live in GitHub, Slack or an explicitly
  connected source.
- Scheduled Tasks do not run on Pro models. The manual GPT-5.6 Pro console should
  therefore handle only the small number of decisions that actually benefit from
  apex reasoning.

Official source:
`https://help.openai.com/en/articles/10291617-scheduled-tasks-in-chatgpt`

## The honest self-wake model

A manual ChatGPT conversation cannot spontaneously start itself. There are three
separate wake mechanisms, and they must not be conflated:

```text
NATIVE CLOCK
Scheduled Task wakes itself hourly
        |
        v
GIT-FIRST CELL
read exact packet -> claim at most one WIP -> bounded work -> exact receipt
        |
        v
OLRUN WATCHDOG
observe missing/stuck/material edge -> browser-nudge exact packet only
        |
        v
RATATOSKR PRO
one contradiction -> one decision/transition -> one receipt -> yield
```

1. **Native Scheduled Tasks are the primary clock.** They poll GitHub or a
   connected source and act only on changed state.
2. **Olrun browser control is a watchdog, not the normal executor.** It repairs a
   paused or stranded loop and wakes the Pro console only for high-value fan-in.
3. **Ratatoskr Pro is not an hourly daemon.** It is a scarce reducer invoked on a
   named contradiction, completed candidate, unresolved P0 or missing ConsumerAck.
4. **The operator is the principal, not the message bus.** Operator attention is
   reserved for authority, private facts, payments, sends, deployment, merge,
   publication and other irreversible effects.

Calling Olrun's browser action a Ratatoskr "self-wake" would be false. It is an
out-of-band wake. The institutional success condition is that this wake requires
zero operator state ferry and closes through Git readback.

## One closure contract for every useful loop

No task earns primary fitness for waking, committing or posting. It earns fitness
only when the following chain closes:

```text
one exact PULL_READY WorkItem
-> atomic claim / lease
-> one bounded producer transition
-> source-system, build, test or CI readback
-> distinct-provider/nonproducer STOOD | FELL
-> named consumer reads the exact receipt
-> explicit ConsumerAck
-> one terminal Gen-133 receipt
```

The following are intermediate states, never completion:

```text
configured
scheduled
woke
queue checked
research performed
draft produced
commit created
schema valid
digest valid
same-provider PASS
Slack message posted
```

### Silence and delta law

- No eligible WorkItem: `YIELD_SILENT`; no Git receipt and no Slack message.
- Relevant source hash unchanged: `YIELD_SILENT`.
- An unchanged Andon is accumulated in the existing durable record and emitted
  only on an edge, severity change or expiry.
- A task may write at most one material receipt per wake.
- Slack receives one pointer only after Git exact readback.
- Duplicate key: `packet_id + input_digest + acceptance_test_digest`.
- Three consecutive zero-yield wakes convert a cell to monitoring/sleep posture;
  they do not produce three queue-empty artifacts.
- Auto-pause is treated as sleep when no eligible work exists, not as failure.
  Olrun resumes only when a matching WorkItem is ready.

## Tool-surface division

| surface | use it for | do not assign |
|---|---|---|
| ChatGPT Scheduled Tasks | hourly monitors, Git/Slack/app reads, bounded research, repo triage, evidence comparison, acceptance-spec authoring, PR/CI monitoring, sanitized drafts | long builds, shell execution, local browser automation, deployment, open-ended architecture |
| Ratatoskr GPT-5.6 Pro | cross-substrate fan-in, contradiction reduction, final packet shaping, non-Claude reasoning review | hourly polling, task mutation, duplicate summaries |
| Olrun / Claude Dispatch | dispatcher, watchdog, browser nudge, host state readback, ConsumerAck routing | becoming a second scheduler or silently doing every worker's job |
| Codex / Claude host workers | code patches, builds, tests, local browser QA, deterministic artifact production | self-verification or irreversible release |
| Operator | explicit authority and private facts | routine wake, state ferry, duplicate triage |

## Proposed 15-seat portfolio

This is a **Reginleif-consumable proposal**, not an executed mutation.

| seat | narrow function | useful return | anti-reward-hack stop |
|---|---|---|---|
| S01 | second clock + provider/freshness witness | edge-triggered fleet or Gen-133 freshness Andon | no repeated hourly 4/15 receipt when unchanged |
| S02 | admission and pull | claims exactly one eligible packet using existing WorkItem/lease semantics | no packet -> silent; never invent work |
| S03 | reducer and ConsumerAck tracker | closes or expires one returned WorkItem | cannot count producer receipt as consumed |
| S04 | structural preflight | deterministic schema/digest/source-pointer result | same-provider result is preflight, never terminal quorum |
| S05 | operator relief and safety sentinel | source-backed life/admin transition or no-send execution packet | remains isolated from factory architecture |
| S06 | FOSS candidate scout | at most three pinned repo candidates under a fixed scorecard | no broad trend report or endless candidate list |
| S07 | license/dependency/security gate | `ADMIT | REVISE | RETIRE` on one candidate | no license inference from README alone |
| S08 | interaction-surface mapper | exact keyboard/pointer/touch event map and adapter seam | no implementation claim without source paths |
| S09 | held-out acceptance author | executable behavior scenarios and expected traces | cannot grade the implementation it specifies |
| S10 | PR/build/CI monitor | changed build/test status and exact failing step | unchanged status -> silent |
| X11 | accessibility/privacy review | bounded risks, fallback and stop conditions | novelty does not outweigh user safety or native fallback |
| X12 | buyer/distribution evidence | one narrow buyer/use-case and falsifiable channel test | no invented warm contacts or demand claims |
| X13 | regression/visual QA | comparison against pinned baseline and acceptance evidence | no screenshot-only PASS without behavior trace |
| X14 | experiment scorer | `KEEP | REVISE | RETIRE` from measured evidence | commit count and prose volume have zero fitness |
| S15 | heritage/dedup | one reusable prior artifact or exact no-match | never generate another control artifact merely because none was found |

## Staged recovery instead of a 15-seat mass restore

Restoring all eleven disabled seats before fixing the closure contract would
amplify the current receipt metabolism. Reginleif should stage recovery under its
own authority:

### Wave A — restore the missing nervous system

Proposed task change, not executed here:

- retain existing `S01`, `S04`, `S05`, `S15`;
- restore/rewrite only `S02` admission and `S03` reducer;
- place one exact spatial-factory WorkItem in the existing
  `projects/<project>/packets/` protocol;
- require one full closure before adding another cell.

Acceptance: one WorkItem is claimed, executed by a named host worker, independently
verified, consumed and terminally receipted in Gen-133 without operator ferry.

### Wave B — activate the factory conveyor

After Wave A closes:

- restore `S06` through `S10` for candidate, gate, interaction map, acceptance
  and build/CI monitoring;
- keep WIP at one application across all five cells;
- outputs are stages of one product, not five independent research projects.

### Wave C — activate evidence and evolutionary cells

Only after two useful closures with bounded noise:

- restore `X11` through `X14`;
- use them for privacy/accessibility, distribution, regression and evidence-based
  keep/revise/retire;
- full `15/15` is a capacity state, not a success metric.

## Olrun browser-watchdog protocol

Olrun should not open this thread every hour. It should nudge on edges only.

### Nudge triggers

Nudge Ratatoskr Pro when exactly one of these becomes true:

1. a PULL_READY packet is older than two expected task epochs and unclaimed;
2. a returned WorkItem lacks distinct verification or ConsumerAck beyond its
   stated expiry;
3. Git and Slack disagree on an authority-bearing fact;
4. the Scheduled Tasks active inventory changes materially or a required Wave-A
   seat pauses;
5. a factory candidate reaches a real `ADMIT | RETIRE` decision boundary;
6. an operator-only effect is ready with exact bytes and a no-effect default.

Do not nudge for unchanged queue-empty, unchanged 4/15, another draft, another
same-provider PASS, or another architecture idea.

### Exact browser-nudge packet

Olrun pastes only a bounded packet of this form:

```yaml
wake: RATATOSKR_GEN133_PRO
packet_id: <exact immutable id>
source:
  repo: TTaoGaming/hfo-gen-133
  commit: <40-char sha>
  path: <exact path>
  blob: <40-char blob sha>
contradiction_or_decision: <one sentence>
requested_transition: <one bounded action>
acceptance_test: <held-out pass/fail condition>
verifier: <distinct actor>
consumer: <named actor>
expiry_utc: <absolute UTC>
forbidden:
  - task mutation
  - new scheduler/queue/root/roster
  - send/spend/deploy/merge/publish without operator authority
```

Ratatoskr response contract:

```text
read exact bytes
-> state STOOD | FELL | HOLD
-> make at most one Git-first transition
-> read back commit + blob
-> post one material Slack pointer
-> name verifier, consumer, expiry and honest flaw
-> yield
```

Olrun consumes the Git receipt, not the prose left visible in the browser. Browser
text is a carrier surface; Git is the durable return.

### Watchdog backoff

- One nudge per packet version.
- If Ratatoskr returns `HOLD` with unchanged inputs, no repeat nudge until the
  named falsifier or expiry changes.
- Browser failure is retried by Olrun under bounded backoff. The operator is
  notified only when a real deadline, safety issue or authority decision is at
  risk.

## First spatial-app-factory golden path

```yaml
workitem_id: SPATIAL_FACTORY_GOLDEN_PATH_001
status: PROPOSED_NOT_DISPATCHED
wip: 1
goal: prove one existing spatial artifact can traverse the factory from pinned source to independently verified build evidence
starting_heritage:
  - gen130 HandPiano v512 demo-ready no-egress receipt
  - gen130 Spatial OS / HandPiano public-proof inventory
output_generation: 133
publication: FORBIDDEN
release: FORBIDDEN
```

### Definition of done

1. S15 or Olrun pins the exact heritage source path, commit and digest. No bulk
   heritage copy.
2. S02 admits one WorkItem. No competing application is active.
3. A Codex or Claude host worker reconstructs the build in a clean checkout and
   records the exact command, environment and real exit code.
4. S08 maps one normalized spatial primitive to ordinary app events. Minimum
   proof: pointer position plus one pinch/activation event; native mouse/keyboard
   fallback remains available.
5. S09 supplies held-out scenarios before implementation is graded.
6. The host worker produces one deterministic trace or test artifact proving the
   spatial primitive caused the intended ordinary input event.
7. A distinct provider/nonproducer reruns or independently reads the held-out
   evidence and returns `STOOD | FELL`.
8. S03 obtains ConsumerAck from Olrun as spatial-factory coordinator and writes
   one terminal Gen-133 receipt.

### Success metric

```yaml
primary:
  closed_useful_loops: 1
  operator_state_ferry_events: 0
  consumer_ack: true
  distinct_provider_verdict: STOOD
secondary:
  clean_build_exit_code: 0
  native_fallback_preserved: true
  behavior_trace_present: true
  gen133_terminal_receipt: true
zero_fitness:
  - number_of_commits
  - number_of_agents_woken
  - number_of_architecture_documents
  - same_provider_passes
  - queue_empty_messages
```

### Failure and retirement

Return `FELL` or `HOLD`; do not produce replacement prose when:

- heritage source cannot be pinned;
- a clean build cannot be reproduced;
- no ordinary-input adapter seam exists;
- the acceptance trace is synthetic or not replayable;
- fallback is removed;
- verification is performed only by the producer;
- ConsumerAck has no named consumer;
- the lane asks the operator to carry routine state.

The first golden path is deliberately a packaging and reproducibility proof, not
an app-store launch, buyer claim or broad factory architecture project.

## Fitness and operator-load scorecard

The hourly portfolio should be judged by these measures, in this order:

| metric | target posture |
|---|---|
| useful closed loops | at least one before portfolio expansion |
| operator state-ferry events | zero |
| operator coordination minutes | decreasing; authority decisions excluded |
| ConsumerAck latency | bounded by WorkItem expiry |
| Gen-133 terminal receipts / producer receipts | increasing ratio |
| duplicate unchanged Andons | zero |
| queue-empty Slack messages | zero after first edge |
| same-provider terminal verdicts | zero |
| build/test/source readbacks | required for execution claims |
| external fitness | eventually measured by real use, buyer evidence or income—not internal volume |

A seat that produces no useful delta is allowed to sleep. Unused inference is an
opportunity cost; noisy self-referential inference is a larger cost because it
consumes operator attention and contaminates selection pressure.

## Material recommendation

The next task mutation, if Reginleif accepts this packet, should not be a full
portfolio rewrite. It should restore and harden **S02 + S03 only**, then feed them
`SPATIAL_FACTORY_GOLDEN_PATH_001` and require the complete closure contract.

If that cannot close, the defect is not lack of worker count. It is the dispatch,
tool, verification or consumption seam, and the exact failed edge will be visible.

## Verification and consumption

- **Verifier:** Sigrun/P4 attempts to falsify the allocation, especially the claim
  that Wave A should precede full restoration.
- **Consumers:** Olrun decides whether to issue the exact host work packet;
  Reginleif decides whether and how to mutate Scheduled Tasks.
- **Strongest falsifier:** a current receipt proving an existing enabled portfolio
  already closes useful Gen-133 WorkItem -> distinct verification -> ConsumerAck
  loops without operator ferry.
- **Expiry:** this proposal is superseded by a newer explicit operator directive,
  a fresher provider inventory or an accepted Gen-133 golden-path receipt.

## Honest flaw

This packet is a design and dispatch proposal. It does not prove that the ChatGPT
Scheduled Tasks product exposes every connector/write surface consistently inside
unattended runs, that Olrun browser control will remain reliable, or that the
HandPiano heritage reconstructs cleanly. Scheduled Tasks are a provider-managed
clock and may auto-pause; no webhook or hard real-time guarantee exists. The
proposed seat functions are not yet installed. No task has been restored or
rewritten, no host build has run, and no golden-path ConsumerAck exists.

*The self-wake is the clock. The strange loop is the verified consequence and its return.*

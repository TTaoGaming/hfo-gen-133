# loop_engineering_gap_analysis.v0_1 — HFO loops vs. the standard body of practice

```yaml
schema_id: hfo.gen133.contract.loop_engineering_gap.v0_1
valid_time_utc: 2026-07-31T14:50:00Z
transaction_time_utc: 2026-07-31T14:50:00Z
claim_status: partial
author: SIGRUN_P4 · claude-opus-5 · Claude Code · gen-133
method: pattern-by-pattern audit against cited industry sources; evidence from the live host
```

## 0. Correction that reframes this whole document

An earlier claim in this session — *"zero working autonomous loops"* — was
**wrong, and my own falsifier R1 caught it.** I scanned three forge trees and
the automation registry. I did not scan `C:\Dev\.hfo_runtime\` or
`C:\Dev\hfo_gen132_garmr_institution_sol_20260729`.

**Corrected evidence:**

| fact | value |
|---|---|
| Garmr institution repo commits since 2026-07-29 | **40** |
| Last commit | `5001eb959` @ `2026-07-30T17:18:37Z` (~21h ago) |
| Last durable-DB write (`garmr_4_1_v2.sqlite3-shm`) | `2026-07-31T00:51Z` (~13h ago) |
| `garmr_actor_events` row count | **7** |
| Expected events for an hourly loop created 2026-07-29T16:54Z | **~46** |
| **Observed cadence** | **~15% of nominal** |

**So the loop is not dead. It is alive, well-engineered, and producing nothing
that matters.** That is a completely different — and more useful — diagnosis
than "zero loops," and it is the one that explains the operator's observation
that loops are *"useful but stall often."*

Look at what those 40 commits actually did. The last three sealed work items:

```
WI-T0-GARMR-MAILBOX-EMPTY-GENESIS-20260730T170031Z   — "bind empty mailbox"
WI-T0-GARMR-IDENTITY-TICK-CHAIN-BRIDGE-...            — "enforce bridge"
WI-T0-INSTITUTION-CADENCE-ACTOR-...                   — "build T0 cadence reducer"
```

A full `queue → claim(lease) → work → seal` cycle, with fencing, readback
verification, and chain receipts — executed to **record that the mailbox was
empty**, and to **build more loop machinery**. The loop's entire work product is
the maintenance of itself.

This is the single most important finding in the audit, and every pattern below
should be read against it: **HFO's loop problem is not reliability. It is that
the reliability machinery has no work to be reliable about.**

## 1. The audit

Legend: **HAVE** = implemented and observed working · **PARTIAL** = present but
unenforced or incomplete · **MISSING** = no implementation found.

### 1.1 Failure containment

| # | pattern | source | status | evidence | first step to close |
|---|---|---|---|---|---|
| 1 | **Supervisor tree** — parent supervises children; restart strategy on crash | Erlang/OTP; Armstrong, *Making Reliable Distributed Systems* (2003) | **MISSING** | No process supervises any HFO loop. The 12+ zombie `olrun-cop-hourly` instances stacked with no parent to reap them — the defining symptom of no supervisor | One Windows service or `.ps1` supervisor that owns PIDs, enforces `one_for_one` restart, and reaps |
| 2 | **"Let it crash"** — fail fast, restart clean, don't defensively patch | Armstrong | **INVERTED** ⚠️ | HFO loops hang instead of crashing. A hung loop is strictly worse than a crashed one: a crash is observable, a hang looks like work | Add hard timeouts (#4) so hangs become crashes |
| 3 | **Watchdog / dead-man switch** — external process kills anything that misses a heartbeat | hardware WDT; systemd `WatchdogSec` | **MISSING** | The zombies survived indefinitely. Nothing was watching. Gunnr is *named* as watchdog in doctrine and is `PAUSED` in the registry | External `.ps1`: any HFO process alive > 15 min with no heartbeat file update ⇒ `Stop-Process` |
| 4 | **Timeout everywhere** — no unbounded wait | Nygard, *Release It!* (2007) | **MISSING** | **The proximate cause of the zombies.** 12+ instances hung inside `sigrun_proprioception` with no timeout on the MCP call | Wrap every MCP/tool call in the loop prompt with an explicit deadline; the runner enforces a wall-clock kill |
| 5 | **Circuit breaker** — stop calling a failing dependency | Nygard; Netflix Hystrix | **MISSING** | Every `olrun-cop-hourly` instance called the same hanging `sigrun_proprioception`. Instance 2 through 12 had the information to refuse and called anyway | After 3 consecutive failures against one tool, open the breaker for 1h; record the trip |
| 6 | **Bulkhead** — isolate resource pools so one failure can't drain shared capacity | Nygard | **MISSING** | The zombies consumed shared quota that every other lane needs | Per-lane quota ceiling; a lane that exceeds it is halted, not throttled globally |
| 7 | **Backoff + retry + jitter** | Brooker, AWS Arch Blog, *Exponential Backoff and Jitter* (2015) | **PARTIAL** | `NO_PULL_BACKOFF` and `next_due_utc` exist in the Garmr reducer — real backoff state. No jitter; `.run-jitter-salt` exists in the automations dir but no evidence it's applied | Apply full jitter to the existing `next_due_utc` computation |
| 8 | **Dead letter queue** — park failed items for triage instead of retrying forever | SQS, RabbitMQ | **MISSING** | A failed automation run leaves no artifact at all. There is nothing to triage | One `state/ssot/deadletter.jsonl`; any run ending non-zero writes there |

### 1.2 State and correctness

| # | pattern | source | status | evidence | first step |
|---|---|---|---|---|---|
| 9 | **Durable execution** — checkpoint so a crash resumes at the last step | Temporal; DBOS; Azure Durable Functions | **HAVE** ✅ | Garmr's `garmr_4_1_v2.sqlite3` with `garmr_actors` / `garmr_actor_events`, event-sourced, `mode=ro` readback verification, `last_event_sha256`. This is real and it is good | Generalize it — one actor has it, the other 51 automations do not |
| 10 | **Idempotency keys** — retry-safe operations | Stripe API | **HAVE** ✅ | Garmr forms `garmr-4-1-hourly-<UTC YYYYMMDDTHH>` as an idempotent wake ID. Textbook-correct | Same: generalize |
| 11 | **Fencing tokens** — stale holder can't write after lease expiry | Kleppmann, *DDIA* (2017) ch.8 | **HAVE** ✅ | Garmr TOML names "leases, fencing" explicitly; repo shows `claim(lease)` commits | Generalize |
| 12 | **Actor model / virtual actors** — message passing, per-actor mailbox, on-demand activation | Hewitt (1973); Erlang; Orleans (virtual actors) | **PARTIAL** | Garmr is a genuine virtual actor: `hfo://gen132/actor/GARMR/4.1/lineage_3b00544bf871`, with a mailbox. **But its last work item was literally "bind empty mailbox."** An actor with an empty mailbox is correct and useless | Populate the mailbox. This is the real bottleneck, not the actor runtime |
| 13 | **Saga / compensating actions** | Garcia-Molina & Salem (1987) | **MISSING** | No multi-step external transaction exists yet, so no compensation is defined. Becomes required the moment outreach sends start | Defer until first send; then define the compensation for "sent to wrong recipient" |
| 14 | **Outbox pattern** — transactionally stage outbound messages | Microservices transactional outbox | **PARTIAL** | `projects/income-lane/outbox/` is specified with `send_status: DRAFT` / `operator_signature: null`. Structurally correct; zero rows | Put one draft in it (§3 artifact #2) |
| 15 | **Structured concurrency** — child tasks bounded by parent scope | N. J. Smith, *Notes on Structured Concurrency* (2018); Trio nurseries; Java 21 JEP 453 | **MISSING** | Long sessions consuming 40+ turns on a substep is the symptom: no parent scope bounds the child's budget | Per-subtask turn/token budget declared before dispatch; exceeding it returns partial, not more turns |

### 1.3 Observability and control

| # | pattern | source | status | evidence | first step |
|---|---|---|---|---|---|
| 16 | **Observability triad** — metrics + traces + logs | Sridharan, *Distributed Systems Observability* (2018) | **LOGS ONLY** | Chains are excellent logs. **Zero metrics** (no loop-execution counter, no success rate, no latency). Zero traces. This is why "how many loops work?" took an hour of forensics instead of one query | One `state/ssot/loop_metrics.jsonl`: `loop_id, fired_at, duration_s, exit_code, produced_artifact` |
| 17 | **Health check: liveness ≠ readiness** | Kubernetes probes | **CONFLATED** ⚠️ | Garmr's heartbeat proves *liveness* (the process ran). Nothing proves *readiness* (it could do useful work). A loop with an empty mailbox is **live but not ready**, and HFO reports that as green | Split: `alive` = ticked; `ready` = mailbox depth > 0 **and** last work item had external effect |
| 18 | **SLO + error budget** | Google SRE Book (2016) | **MISSING** | No target exists for "% of scheduled fires that execute." Actual is ~15% and nothing flagged it | Set SLO: ≥ 90% of scheduled fires produce a metrics row. Alert below |
| 19 | **Alerting on symptoms, not causes** | Google SRE | **INVERTED** ⚠️ | `notification_policy = "failed_runs_only"` in the Garmr TOML. **A loop that does nothing never fails, so it never notifies.** Silence is architecturally indistinguishable from health | Change to alert on *absence of progress*, not presence of error — see #20 |
| 20 | **Andon on no-progress** | Toyota Production System; Ohno | **MISSING** | The Garmr reducer tracks an `unchanged` count and nothing escalates when it grows. 40 commits, 0 external effects, no signal raised | **N consecutive `material_change=false` ticks ⇒ halt the line and notify.** Suggest N=3 |
| 21 | **Feature flag / kill switch** — disable a loop without redeploy | trunk-based development; LaunchDarkly | **PARTIAL** | `enabled`/`paused` flags exist in the TOMLs, and 46/52 are `PAUSED` — so the mechanism works. But there is no *remote* kill: stopping the zombies requires host access | One `state/ssot/kill_switch.json` that every loop reads at wake and obeys |
| 22 | **Rate limit / quota discipline** | token bucket; Nygard bulkhead | **MISSING** | The zombies burned quota unbounded. No per-loop budget, no global ceiling, no spend counter | Daily token ceiling per `loop_id`, enforced by the runner, recorded in metrics |
| 23 | **Canary + blue/green** | Humble & Farley, *Continuous Delivery* (2010) | **MISSING** | New automations go straight to hourly at full authority. `fenrir-`, `jormungandr-` were created 07-30 and enabled immediately | New loops start `COUNT=3` at a low cadence; promote only on 3 clean metric rows |
| 24 | **Chaos engineering** | Netflix Chaos Monkey; *Principles of Chaos* | **MISSING** | No loop has ever been deliberately killed to test recovery. Recovery is untested, therefore unproven | Once #1 (supervisor) exists: kill one loop mid-run, verify restart. Until then there is nothing to test |
| 25 | **Runbook per alert** | Google SRE | **MISSING** | The zombie incident has no runbook; diagnosis was ad-hoc this morning | Write one runbook: "loop produced no metrics row in 2 cycles" |

### 1.4 Orchestration

| # | pattern | source | status | evidence | first step |
|---|---|---|---|---|---|
| 26 | **DAG orchestrator** — declarative dependency graph | Airflow; Prefect; Dagster | **MISSING** | Loops are independent cron entries with no declared dependencies. Nothing expresses "artifact #2 requires artifact #1" | Do **not** adopt Airflow. Add a `depends_on` field to the work-item schema and refuse to claim an item whose dependency is unsealed |
| 27 | **Backpressure** — slow the producer when the consumer is saturated | Reactive Streams | **MISSING** | Irrelevant today (no producer is saturating anything) | Defer. Revisit at > 10 loops |
| 28 | **Queue depth as the control signal** | Kanban; Little's Law | **MISSING** | **This is the finding.** Nobody measures mailbox depth. Garmr's depth is 0 and has been for days, and the system reports green | Publish `mailbox_depth` per actor in metrics; **depth 0 on a work-actor is an andon, not an idle state** |
| 29 | **Work-item lease with expiry** | standard queue semantics | **HAVE** ✅ | Garmr `claim(lease)` → `work` → `seal` observed in git history | Generalize |
| 30 | **Human-in-the-loop gate at irreversibility** | — (HFO-native, cf. two-person rule) | **HAVE** ✅ | `effect_ceiling: T0_INTERNAL_ONLY`, `operator_signature: null`, explicit no-send lists. Genuinely strong | Keep. Do not weaken while fixing throughput |

## 2. Scorecard

| bucket | HAVE | PARTIAL | MISSING/INVERTED |
|---|---|---|---|
| Failure containment (8) | 0 | 1 | **7** |
| State & correctness (7) | 4 | 2 | 1 |
| Observability & control (10) | 0 | 1 | **9** |
| Orchestration (5) | 2 | 0 | 3 |
| **Total (30)** | **6** | **4** | **20** |

**The shape of this result is the diagnosis.** HFO has built the *hard* half —
durable execution, event sourcing, idempotency, fencing, leases, virtual
actors, human gates. That is genuinely advanced; most teams never get there.

What is missing is the *cheap* half — timeouts, a supervisor, a watchdog, a
metrics line, an andon on no-progress. Every one of those is under a day of
work. **HFO built a Temporal-grade state machine and forgot to put a `timeout`
on the function call.**

## 3. The three patterns that would fix ~80% of observed stalls

Ranked by (observed failures eliminated) ÷ (hours to build):

| rank | pattern | eliminates | hours |
|---|---|---|---|
| **1** | **Timeout + supervisor + reaper** (#1, #3, #4) | zombie stacking, silent hangs, unbounded quota burn | ~4 |
| **2** | **Loop metrics line** (#16, #18) | "how many loops work?" becomes one query instead of an hour of forensics; makes #3 possible | ~2 |
| **3** | **Andon on no-progress + queue depth** (#20, #28, #17) | the Garmr class — a perfectly healthy loop producing nothing, invisibly, forever | ~3 |

**Total ~9 hours to convert the loop fleet from unobservable to governed.**

## 4. FALSIFIERS

| # | falsifier | test |
|---|---|---|
| F1 | Another loop is executing somewhere I still have not scanned. **R1 already fired once this session — assume it can fire again.** | full-disk scan for files modified in the last 24h, not just the trees I chose |
| F2 | Garmr's 7 events span a period where the automation was intentionally paused, making "15% of nominal" wrong | read `created_at`/`updated_at` in the TOML against event timestamps in the DB |
| F3 | Timeouts already exist at the runner level and the zombies had a different cause | inspect one hung process's actual stack/state before killing it |
| F4 | Adding the 3 patterns in §3 does not raise loop yield | measure loop-execution rate for 7 days before and after. **If yield does not move, the bottleneck was empty mailboxes all along and this whole document optimized the wrong layer** |
| F5 | `notification_policy = "failed_runs_only"` is overridden elsewhere and alerts do fire | check the Codex notification config; ask the operator whether Garmr has ever notified |

**F4 is the one to take seriously.** The evidence in §0 suggests the mailbox is
the constraint and the loop machinery is not. If so, §3's 9 hours buys
*observability of a system that has nothing to do* — worth having, but not
income.

---

*claim_status: partial · 30 patterns audited against cited sources · evidence
from live host inspection · honest_flaw: I audited loop machinery when §0's own
evidence says the constraint is empty mailboxes, not loop reliability*

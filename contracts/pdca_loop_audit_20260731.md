# PDCA LOOP AUDIT — every loop on this host — 2026-07-31

```yaml
contract: pdca_loop_audit
schema_id: hfo.gen133.contract.pdca_loop_audit.v0_1
valid_time_utc:       2026-07-31T18:50:00Z
transaction_time_utc: 2026-07-31T18:55:00Z
authored_by: SIGRUN_P4 · claude-opus-5 · gen-133
claim_status: partial
sealed: false
scope: 3 Claude scheduled tasks + 6 ACTIVE Codex automations + the ad-hoc dispatch lane
```

## 0 · The measurement that frames everything

```
Codex automations on disk:      52
Codex automations ACTIVE:        6      (46 = 88% inactive, retained not deleted)
Claude scheduled tasks:          3      (all 3 reported failing, morning report §1.2)
Loops producing EXTERNAL effect: 0
```

**88% inactive matches the recorded 78-of-81-disabled pattern exactly.** A registry
where the overwhelming majority of entries are retained-but-off is a **wish list
being read as an inventory**. Every "we have N loops" claim in this fleet should be
read as "we have N/8 loops."

**The second measurement is the one that hurts:** of 6 ACTIVE loops, the number
that have produced an artifact anyone outside this system has seen is **zero**.

## 1 · PDCA — Claude scheduled tasks

| # | loop | **P** — stated purpose | **D** — what it did | **C** — gap | **A** — act |
|---|---|---|---|---|---|
| 1 | `olrun-cop-hourly` | hourly COP refresh | **12+ zombie instances hung in `sigrun_proprioception`** | unbounded wait. No timeout, no supervisor, no watchdog, no circuit breaker — 4 missing patterns in one failure | **KILL — record PIDs + start times BEFORE killing** (the fix destroys the only evidence of runtime). Replace with a wall-clock-deadline version. **This is the only item costing money right now** |
| 2 | `sigrun-apex-opus5-hourly` | hourly apex wake | fails — `mcp__dispatch__*` absent in scheduled sessions | capability assumed at wake, never asserted | **PATCH** — station [2] asserts required tools present, else writes `blocked` and stops. Then rewrite to work in-process (bash, not child-session) |
| 3 | `valkyrie-pack-sonnet5-hourly` | hourly valkyrie pack | same failure | same | **PATCH — same fix, same prompt family.** Do 2 and 3 as one change |

> ⚠️ **The diagnosis for 2 and 3 is UNCONFIRMED** (morning report R2: the registry
> may be cwd-scoped, and "not found" may be an artifact of *where* it ran). **Run
> the P10 heartbeat (§11 build #4) before patching prompts** — it resolves whether
> the scheduler fires at all, and if it does not, all prompt debugging is wasted.

## 2 · PDCA — the 6 ACTIVE Codex automations

| # | loop | rrule | **P** | **D** | **C** | **A** |
|---|---|---|---|---|---|---|
| 4 | `garmr-p1-hourly-outreach-control-heartbeat` | hourly | own outreach control | **40 commits, all self-maintenance; last sealed item "bind empty mailbox"; `notification_policy = failed_runs_only`** | **EMPTY-QUEUE REWARD HACK.** A loop that does nothing never fails, so it never notifies. Silence is architecturally indistinguishable from health | **KEEP the actor — FILL THE QUEUE.** Garmr is well-engineered (event-sourced, fencing tokens, leases, idempotent wake IDs). It is correct and starved. Assign it §11 build #1 and set `notification_policy` to notify on `unchanged_count ≥ 3` |
| 5 | `fenrir-gen133-evo-colosseum-hourly` | hourly | evolve variants against held-out benchmarks | returns `target_queue_empty` — `state/ssot/fenrir_evo_queue.jsonl` has no eligible rows. Also gated on Surtr ONLINE, and **Surtr is STUCK (B5)** | same empty-queue class, **doubly blocked** — no queue *and* no $0 inference route | **PAUSE until both clear.** Un-pause when (a) §14 A3 smoke passes → Surtr can come online, and (b) the spatial inventory (§11 #5) supplies real targets. **Do not wake a second Fenrir** |
| 6 | `jormungandr-gen133-exemplar-eater-hourly` | hourly | assimilate exemplars | ⚠️ **NOT MEASURED** — I read its registry entry, not its output | unknown | **REPOINT, do not kill.** §10 assigns Jörmungandr the market-scout question. Give this loop that queue. Measure one cycle before judging |
| 7 | `huginn-muninn-p3-effector-wake` | hourly | P3 effector wake | ⚠️ **NOT MEASURED** | unknown | **MEASURE FIRST.** P3 INJECT is the neuro-symbolic seam — the most valuable port to have working. Read one cycle's output before any verdict |
| 8 | `gen131-seven-day-rehydration-integrity-audit` | daily ×7 | 7-day integrity audit | ⚠️ not measured; `COUNT=7` → **self-terminating, likely already expired** | a finite-count loop that expired silently reads identical to one still running | **LET EXPIRE.** Then decide deliberately. Log the expiry — a silent expiry is the same information-loss class as a silent empty queue |
| 9 | `review-gunnr-bounded-autonomy-lease` | daily ×1 | review Gunnr's lease | `COUNT=1` — one-shot, almost certainly fired and done | it is a reminder, not a loop | **DELETE from the ACTIVE set.** One-shot reminders inflate the loop count and are the reason "we have 52 automations" is misleading |

## 3 · PDCA — the ad-hoc dispatch lane (uncounted, and the largest)

| **P** | **D** | **C** | **A** |
|---|---|---|---|
| operator wakes a frontier session; it does bounded work and returns | sessions burn 40+ turns on a substep; **7 spec documents produced today, 0 external artifacts** | **unbounded child scope** — no parent declares a turn/token budget, so no overrun is detectable. This lane produces most of the fleet's output and appears in no registry | **INSTRUMENT.** Station [5] declares a turn budget before dispatch; overrun returns partial. And apply drift detector **D1** (§12): two consecutive weeks of specs with zero external artifacts is a revoke trigger |

## 4 · The pattern across all ten

| root cause | loops affected | one-line cure | exists? |
|---|---|---|---|
| **Empty queue + notify-on-failure-only** | 4, 5 (and arguably 6) | andon when `unchanged_count ≥ 3` **or** `mailbox_depth == 0` | ❌ one line, nobody wrote it |
| **No timeout / supervisor / watchdog** | 1 | wall-clock deadline + reaper at station [1] | ❌ |
| **Capability assumed, never asserted** | 2, 3 | assert required tools at wake, else `blocked` + stop | ❌ |
| **No metrics** | all 10 | one metrics row per fire | ❌ — *"how many loops work?"* took an hour of forensics instead of one query |
| **Liveness ≠ readiness conflated** | 4, 5 | a loop that ticked is **live**; a loop with an empty queue is **not ready**. Report both | ❌ |
| **Registry as wish list** | 46 inactive | one `kill_switch.json`; new loops start `COUNT=3` and promote on 3 clean metric rows | ❌ |
| **Unmeasured** | 6, 7, 8 | read one cycle's output before judging | — |

**Six of seven root causes are the same missing pattern class, and every one is
under an hour of work.** But the morning report's falsifier stands and I am
restating it because it outranks this entire audit:

> **Fill a mailbox before hardening the machinery that drains it.** If the cheap
> patterns are built and loop *yield* does not move, the bottleneck was empty
> queues all along. **The evidence says that is likely.** Loop #4 is a
> well-engineered durable actor that has produced nothing because nobody gave it
> work — hardening it further changes nothing.

## 5 · Ranked actions

| # | action | effort | horizon |
|---|---|---|---|
| 1 | **Kill the 12+ zombies** (record PIDs first) | 10 min | costing money now |
| 2 | **Give Garmr (#4) a real queue** — §11 build #1 | 90 min | `short_income` |
| 3 | P10 heartbeat — resolves whether the scheduler fires | 30 min | unblocks #4/#5 diagnosis |
| 4 | Andon on `unchanged_count ≥ 3` and `mailbox_depth == 0` | 60 min | prevents recurrence |
| 5 | Measure loops 6, 7, 8 — one cycle each | 30 min | converts 3 unknowns to facts |
| 6 | Delete #9; let #8 expire; pause #5 | 10 min | truthful loop count |

## 6 · Falsifiers

| # | falsifier |
|---|---|
| F1 | Loops 6/7/8 are producing real output I did not read. **Likely** — I read registry entries, not artifacts. Three verdicts above are `unmeasured` and labeled as such |
| F2 | The scheduled-task diagnosis (2, 3) is a cwd-scoping artifact. **The single most likely error here.** P10 resolves it |
| F3 | A loop exists outside `.codex/automations` and the Claude registry. **R1 already fired once today on exactly this** — Garmr was found in an unscanned path. **This audit is a floor, not a census** |
| F4 | `COUNT=7`/`COUNT=1` loops (8, 9) already expired, making 6-ACTIVE really 4-ACTIVE. **Not verified.** If true, the working loop count is worse than stated |

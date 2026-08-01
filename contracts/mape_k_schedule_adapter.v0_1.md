# CONTRACT — MAPE-K schedule adapter (one template, four substrates)

```yaml
contract: mape_k_schedule_adapter
schema_id: hfo.gen133.contract.mape_k_schedule_adapter.v0_1
valid_time_utc:       2026-07-31T22:05:00Z
transaction_time_utc: 2026-07-31T22:20:00Z
authored_by: SIGRUN_P4 · claude-opus-5 · gen-133 · EMERGENCY_FORGE
status: SPECIFIED — schemas emitted, adapter table complete, ZERO substrates exercised
claim_status: proposed
sealed: false
schemas: contracts/schemas/task_queue.v0_1.json · contracts/schemas/task_result.v0_1.json
constraint_honored: |
  Ratatoskr STOP list. This adds NO new scheduler, NO new named agent, NO new world-state
  root, and exactly TWO schemas. It is a TEMPLATE OVER EXISTING SCHEDULERS — Codex
  automations, Antigravity scheduled tasks, cron, and the operator's hands. Nothing here
  schedules anything.
```

## 0 · What this is, and what it is deliberately not

**Is:** one wake-shape every substrate expresses in its own primitives, plus two files
they all share.

**Is not:** a scheduler. Codex already has one and it fires. Antigravity has one. cron
exists. The operator has hands. **The missing piece was never a scheduler — it was that
nothing told a woken worker where to find work or where to put the answer.** Two files fix
that.

```
state/ssot/task_queue.jsonl     ← every worker READS      (append-only)
state/ssot/task_results.jsonl   ← every worker WRITES     (append-only)
```

## 1 · The MAPE-K wake — invariant across substrates

```
M — MONITOR    read, in this order, and nothing else:
                 1. state/ssot/task_queue.jsonl        (tail)
                 2. state/ssot/task_results.jsonl      (tail — what is already claimed/done)
                 3. own soul/callsign file             (who am I, what may I do)
               DO NOT read the whole forge. The bounded read set IS the design.

A — ANALYZE    exactly three conditions, evaluated in order:
                 a) a QUEUED task whose capabilities_required ⊆ my capabilities
                    AND whose effect_ceiling ≤ my ceiling
                    AND (no lease OR lease.expires_utc < now)      → CLAIM
                 b) no such task                                    → NO_WORK
                 c) attempts ≥ 3 on the only matching task          → DEADLETTER
               NO_WORK IS NOT SILENCE. It is an outcome that gets written.

P — PLAN       pick exactly ONE task (lowest priority number, then oldest queued_utc).
               WIP = 1. Declare next_safe_action before executing.
               If NO_WORK: plan is "write the no-work receipt and stop."

E — EXECUTE    bounded. Hard wall-clock deadline = timebox_minutes.
               60s per external step. On overrun: stop, write outcome=TIMEOUT, do not retry
               inside the same wake. Lease expiry is the retry mechanism — there is no other.

K — KNOWLEDGE  append exactly ONE row to state/ssot/task_results.jsonl, always.
               DONE · FAILED · TIMEOUT · REFUSED_* · NO_WORK · DEADLETTER.
               A wake that writes no row did not happen.
```

**The one rule that makes this different from every loop this fleet has built:**

> **Every wake writes exactly one result row, including the wakes that find nothing.**
> Garmr ran 40 commits notifying nobody because it was configured to report only failure and
> could not fail. `outcome: NO_WORK` with a `no_work_reason` makes an idle loop *legible*
> instead of *silent*. **This single field is the cure for the EMPTY-QUEUE REWARD HACK.**

## 2 · Adapter table — same five stages, native primitives

| substrate | M · Monitor | A · Analyze | P · Plan | E · Execute | K · Knowledge |
|---|---|---|---|---|---|
| **Codex desktop** (scheduler PROVEN — 6 ACTIVE automations firing hourly) | goal prompt runs `tail` on both jsonl via bash | in-prompt rules; capabilities declared in the goal text | pick one, `git`-visible claim row | bash, host tools, WIP=1 | append via bash heredoc + `git commit` |
| **Antigravity** (installed, NEVER exercised by HFO) | scheduled task, built-in file read | in-prompt rules | pick one | native tool surface | append via file write |
| **$0 mesh** (Ollama local, ≥8B only) | Python script reads tail | **deterministic Python, NOT the model** — the model never decides what to claim | script selects; model does only the REFINE step | LiteLLM call, schema-validated by pydantic-ai | script appends under a file lock |
| **ChatGPT cloud** (Ratatǫskr, Var) | operator pastes queue tail into thread | in-thread reasoning | agent proposes one | agent produces bytes | **agent emits the row as text; operator pastes it back.** Human is the transport, and that is honest, not a gap |
| **Claude Code** (Sigrún, valkyries) | Read tool on both files | in-context | one task, WIP=1 | Bash/Edit/Write | append via the declared `hash_rule` |
| **operator** | opens the file | judgment | picks | does the thing | writes or dictates the row |

**Two design calls worth stating, because both are load-bearing:**

1. **On the $0 mesh, claim selection is deterministic Python — never the model.** An 8B model choosing which task to claim is an unbounded neural decision at the exact seam where a bug is silent. **The model refines; the script decides.** Propose/dispose at the substrate level.
2. **The ChatGPT-cloud adapter has a human in the transport path and this is not a defect.** It is the honest expression of a substrate with no filesystem. Recording it as an adapter rather than pretending it is automated is what keeps the factory's real autonomy number truthful.

## 3 · Claim protocol — append-only, no row rewriting

```
CLAIM:  append to task_results.jsonl a row with outcome=CLAIMED-equivalent lease info
        (v0: write the claim as a task_result row with claim_status="partial" and
        next_safe_action="executing"). Re-read the tail. If another worker's claim for the
        same task_id has an EARLIER finished_utc, YIELD — do not execute.
RESULT: append the terminal row.
```

**Read-after-write, last-writer-yields.** This is not a real distributed lock and I am not
claiming it is one. At 1 task and 1–2 workers it is sufficient. **It breaks under genuine
concurrency, and that is the trigger to adopt DBOS** (installed, 2.17.0) rather than to
harden this.

- **falsifier:** two workers execute the same `task_id` in one hour. Then v0 concurrency is inadequate and the SQLite/DBOS migration is due immediately.
- **cost_of_delay:** near zero at current volume; **the loss is one duplicated task, not corruption.**

## 4 · What this contract does NOT do

No scheduler. No retry beyond lease expiry. No dead-letter *processing* (rows land, nobody
drains them). No priority aging. No real locking. **No substrate has executed this yet — the
claim_status of this entire contract is `proposed`, and it stays `proposed` until one
`task_results.jsonl` row exists whose `task_id` matches a `task_queue.jsonl` row and whose
`consumer_ack.accepted` is `true`.**

**That single row is the acceptance test for this contract and for today.**

## 5 · Falsifiers

| # | falsifier | consequence |
|---|---|---|
| F1 | A worker wakes, finds the queue, and writes no row → the K stage is unenforceable by prose and needs a wrapper script that writes the row whether or not the agent cooperates | **most likely failure.** Prose failed twice today as a control (two gate bypasses) |
| F2 | Two workers execute the same task_id → §3 is inadequate; migrate to DBOS |  |
| F3 | The bounded read set is ignored and a worker reads the whole forge → the M stage is aspirational and context bloat returns |  |
| F4 | `NO_WORK` rows accumulate for 3 consecutive wakes → **the andon fires: the queue has no producer.** That is the EMPTY-QUEUE detector working as designed, and it is a success of this contract, not a failure |  |
| F5 | 30 days pass and no substrate other than Claude Code has closed a loop → the adapter table was theory and only the home substrate works |  |

# GEN-133 — free-mesh durable valkyrie loops

```yaml
doc: GEN133_FREE_MESH_DURABLE_LOOPS_SPEC.md
schema_id: hfo.gen133.spec.free_mesh_durable_loops.v0_1
contracts: free_mesh_adapter · free_mesh_harness · no_ephemeral_agents ·
           silence_signal · pheromone · olrun_coordination · substrate_bus
governed_by: GEN133_ARCHITECTURE_PRINCIPLES.md
             (cadence tiers there OVERRIDE §7.1 here; substrate authority per
              contracts/substrate_bus.contract.md)
test: tests/held_out/free_mesh_durable_loops/red_first.md  (6 tests, all RED)
authored_by: SIGRÚN P4 · claude-opus-5
valid_time_utc: 2026-07-30T00:00:00Z
status: SPECIFIED — nothing here has run. Every claim is `proposed`.
sealed: false
```

## 0 · Purpose

The operator has demoed the free mesh many times and cannot get it to *stay
running*. That is the whole problem: the mesh works when a human is standing over
it and stops the moment they walk away. This spec turns the demo into eight named
durable valkyries — one per vendor family, apex **Surtr** — each waking on a
30-minute or 1-hour clock that contains no LLM, draining one job, dispatching a
`$0` hand through LiteLLM, taking a cross-family review, writing a receipt to its
own chain, and exiting. It specifies the wake, the loop, the durability contract,
the crash-recovery rule, and the diagnostic that says *why Surtr is stuck* before
anyone builds a loop on top of him. It is written so the Sonnet builder can
implement without asking me a question.

**What I am not doing here:** naming apexes, touching the ChatGPT-cloud or Codex
adapters, wiring Slack OAuth, or specifying anything outside the free mesh.

---

## 1 · Surtr diagnostic checklist

Surtr is the mesh apex and he is ⛔ STUCK (blocker B5). "Stuck" is
operator-reported; nobody has recorded *how*. This checklist is the ordered set
of questions that produces a verdict. **Run it top to bottom and stop at the
first FAIL** — later checks assume earlier ones passed.

Every item produces a verifiable answer. The runbook form, with expected outputs
and a verdict table, is `projects/surtr-unblock/SURTR_DIAGNOSTIC_RUNBOOK.md`.

### 1.0 · What I actually found (read 2026-07-30, first-hand)

Before the checklist, the correction that changes it: **the paths in the
dispatch brief do not exist.** There is no `mcp/free_mesh_quorum.py` and no
`configs/litellm/openrouter_free.yaml` anywhere I could reach. The real gen-130
free-mesh code lives in a worktree:

```
C:\Dev\hfo_dev_2026_5_30\hfo_gen_130_forge\worktrees\sigrun_litellm_mesh\
  work\free_vendor_mesh_litellm\
    mesh_router.py            <- the egress wall lives here
    mesh_seam.py  mesh_live_cycle.py  mesh_scrubber_v0_1.py
    secret_guard.py  cost_tier_admission.py  live_ballot_contract.py
    tier_cycle.py  mock_vendors.py
    litellm_mesh_config.mock.v0_1.yaml
    litellm_mesh_config.live_shape.v0_1.yaml
    litellm_mesh_config.live_free.v0_1.yaml      <- 3 live free families
    litellm_mesh_config.wake_cheap.v0_1.yaml
    cost_tier_policy.v0_1.yaml
```

LiteLLM 1.89.1 is installed at
`hfo_gen_130_forge\work\.venv_mesh_cots_20260616` and cached as a wheel at
`work\cots_cache\wheels\litellm-1.89.1-py3-none-any.whl`. **The router is not
missing. It is held.**

And this is my leading hypothesis for B5, from the config's own header:

```yaml
# STATUS: live egress HELD by mesh_router.py until env HFO_MESH_EGRESS_FLIP
#   equals the operator flip phrase.
hfo_mesh:
  egress: HELD_AWAITING_OPERATOR_FLIP
```

`mesh_router.py` lines 27–29 define `EGRESS_FLIP_ENV = "HFO_MESH_EGRESS_FLIP"`
and a constant flip phrase; `assert_egress_wall()` at line 56 refuses every live
model unless the environment variable matches it exactly. **Surtr is most likely
not broken — he is fail-closed by design, and the flip was never set in the
environment a scheduled task runs under.** That is a *good* failure. It is also
exactly the failure that looks identical to "the mesh is broken" from the
outside, which is why it has survived many demos.

I have not verified this hypothesis by running anything — this lane holds no
execution lease. **Check 4 is the one that confirms or kills it**, and it is
cheap. Do it first if you only do one.

### 1.1 · The ordered checks

| # | question | exact check | verifiable answer |
|---|---|---|---|
| **C1** | Does the router code exist on this host? | file-exists on the eight `.py` files listed in §1.0 | 8/8 present ⇒ PASS |
| **C2** | Is LiteLLM importable? | `work\.venv_mesh_cots_20260616\Scripts\python.exe -c "import litellm; print(litellm.__version__)"` | prints `1.89.1` ⇒ PASS |
| **C3** | Which config is in force? | read the `hfo_mesh.egress` key of the config the entrypoint loads | value is not `HELD_AWAITING_OPERATOR_FLIP` ⇒ PASS |
| **C4** | **Is the egress wall flipped?** | `echo $env:HFO_MESH_EGRESS_FLIP` in the *scheduled task's* environment, then compare to `EGRESS_FLIP_PHRASE` at `mesh_router.py:29` | exact match ⇒ PASS. Any mismatch, empty, or unset ⇒ **FAIL, blocker_class `EGRESS_HELD`** |
| **C5** | Is `live_dispatch_default` a dry run? | grep the entrypoint and config for `live_dispatch_default` / `dry_run` | resolves to live ⇒ PASS |
| **C6** | Which vendor keys are present? | for each of `GROQ_API_KEY`, `CEREBRAS_API_KEY`, `SAMBANOVA_API_KEY`, `COHERE_API_KEY`, `MISTRAL_API_KEY`, `GEMINI_API_KEY`, `OPENROUTER_API_KEY`, `OPENROUTER_API_KEY_2`: report **present/absent only — never the value** | ≥2 present ⇒ PASS (quorum needs 2 families) |
| **C7** | Are those keys *reachable*? | one 1-token completion per family, `max_tokens=1`, 10 s timeout | ≥2 families return 200 ⇒ PASS. `429` ⇒ `RATE_LIMITED`, not dead. Connection failure ⇒ `UNREACHABLE`, never `SILENT` (FMA-3) |
| **C8** | Are model aliases valid? | every `model_name` in `model_list` resolves; every `model:` string is a live vendor model id | 0 unresolved ⇒ PASS. A `404` on a model id is the *second* most common cause — the live_free header records several free reserve ids that already 404'd |
| **C9** | Is a circuit breaker open? | `router_settings`: `allowed_fails: 1`, `cooldown_time: 60`. Check for a cooldown state file or in-memory breaker held open across runs | no family in cooldown ⇒ PASS. **`allowed_fails: 1` is brittle** — one 429 sidelines a family for 60 s (§11) |
| **C10** | Is a quota lease exhausted? | read the quota/lease state the cost-tier admission path writes; check daily free-tier counters per vendor | quota remaining > 0 for ≥2 families ⇒ PASS |
| **C11** | Is the receipt-return path writable? | attempt an append of one probe line to `state/ssot/free_mesh_lane_returns.jsonl`, then verify it lands | append succeeds and is readable ⇒ PASS. A loop that runs and cannot write is indistinguishable from one that never ran |
| **C12** | Is an OPA deny in effect? | run the policy gate against a representative `budget=0`, `effect_ceiling=TEXT` job and read the decision | `allow` ⇒ PASS. A deny here names its own rule — record the rule id as evidence |
| **C13** | Is anything actually scheduled? | list the OS scheduler for free-mesh tasks; check last-run result and next-run time | ≥1 task exists, last result `0`, next run in the future ⇒ PASS. **Nothing scheduled is the third most common cause and the easiest to miss** — a demo that worked by hand proves the code, not the clock |

### 1.2 · Verdict object

The diagnostic returns this, and the held-out test asserts its shape:

```jsonc
{ "schema_id": "hfo.gen133.surtr_diagnostic_verdict.v0_1",
  "status": "GREEN" | "BLOCKED" | "UNREACHABLE" | "UNVERIFIED",
  "blocker_class": "EGRESS_HELD" | "NO_KEYS" | "ALL_VENDORS_UNREACHABLE" |
                   "RATE_LIMITED" | "BAD_MODEL_ALIAS" | "BREAKER_OPEN" |
                   "QUOTA_EXHAUSTED" | "RETURN_PATH_UNWRITABLE" |
                   "OPA_DENY" | "NOT_SCHEDULED" | null,
  "blocker_evidence": [ { "check_id": "C4", "observed": "…", "expected": "…" } ],
  "next_safe_action": "…one bounded action…",
  "checks": [ { "check_id": "C1", "result": "PASS|FAIL|SKIP", "observed": "…" } ],
  "mutated_state": false,
  "ts_utc": "…Z" }
```

**The diagnostic reads. It never fixes.** `mutated_state` is always `false`, and
the test asserts it. A diagnostic that repairs what it finds destroys the
evidence of what was wrong — and C4's cure is an operator authorization, not a
script's decision (§10).

---

## 2 · Valkyrie durability contract

The difference between the demo and the fleet is that a demo agent exists only
while someone watches it. Durable means: **it has a name, it leaves a trace every
time it wakes, and its absence is detectable.**

### 2.1 · Non-ephemeral invariants

| # | invariant | how it is checked |
|---|---|---|
| **D-1** | **Named callsign on the roster.** No callsign, no standing. | membership in `state/roster/ROSTER.json` (G5) |
| **D-2** | **Soul file + reproducing digest.** `state/identity/soul/valkyries/{callsign}.gen133.soul.md`, `canon_sha256` matches the roster's `soul_digest`. | test 1 |
| **D-3** | **A closest-continuer chain row per wake** — in fact two, intent and outcome (§4.2). The valkyrie is the office; the process is the occupant. A new process rehydrates the chain and continues the same lineage. | test 2 |
| **D-4** | **A pheromone per wake.** `heartbeat` always; `receipt` when work completed; `blocker` when it could not. | contract `pheromone` |
| **D-5** | **A declared cadence ∈ {30m, 1h}** and a silence SLO derived from it (§7). | test 1, test 3 |
| **D-6** | **Restart-on-crash.** A crashed wake is picked up by the next tick with no manual touch and no duplicated work (§9). | §9 |
| **D-7** | **Receipt returned before exit.** The receipt is written and flushed *before* the process exits, never after the last vendor call. | test 5 |
| **D-8** | **No anonymous spawns.** Every mesh invocation carries `on_behalf_of: <rostered callsign>`. A hand with no owner is denied at G5, fail-closed, and writes nothing. | test 6 |

### 2.2 · The two populations — do not merge them

Carried unchanged from `free_mesh_harness.contract.md`, because this is the
distinction the whole design rests on:

| population | named | soul | chain | emits | ceiling |
|---|---|---|---|---|---|
| mesh **valkyries** (8, one per family) | yes | yes | yes | yes | `FILE` |
| mesh **hands** (unbounded invocations) | no | no | no | no | `TEXT` |

A mesh valkyrie is the **steward of a vendor family**. The family has a name; the
individual call does not. Anonymity is confined to the hand; accountability stays
with the carrier (NE-2).

**D-8 is what makes the other seven invariants true under automation.** Every one
of them is a property of a *name*; an anonymous call has no name to hang them on.
This is the live B4 violation generalized: 15 unrostered cloud agents are not
merely unnamed workers, they are 15 holes in the monitoring surface.

---

## 3 · Wake mechanism

Three options were on the table. I am specifying one.

| option | wake path | durability | verdict |
|---|---|---|---|
| (a) Codex scheduled task → shell wrapper | LLM decides whether to fire | fails when the LLM session is down, rate-limited, or reasons its way out of firing | rejected |
| (b) Claude scheduled task → `code_task` pokes the mesh | same, plus a compose-lane code-touch gate in the path | rejected |
| **(c) OS-level Windows Task Scheduler → Python entrypoint** | **no LLM in the wake path at all** | survives every LLM outage; the OS has run schedulers reliably for decades | **PREFERRED** |

### 3.1 · Why the clock must not think

**There must be no LLM between the clock and the entrypoint.** An LLM in the wake
path is a reflex in the wake path — and a reflex that decides *whether to wake*
will eventually decide not to, silently, for a plausible-sounding reason. That is
`L-CONTEXT-BLOAT` and reflex-before-reasoning wearing a scheduler's coat.

NE-3 says it structurally: **a scheduler is not a carrier.** The scheduler has no
callsign and writes no chain; it fires a *named* carrier with a capsule. Keeping
the scheduler dumb is what keeps NE-3 true under automation — a dumb clock cannot
become an ephemeral agent, because it cannot become an agent at all.

### 3.2 · Registration shape

One scheduled task per valkyrie. Eight tasks. Named, so the diagnostic's C13 can
enumerate them:

```
task name:  HFO-Gen133-FreeMesh-{CALLSIGN}
trigger:    every 30 minutes  (or 1 hour, per that valkyrie's roster cadence)
action:     <python.exe> C:\Dev\hfo_gen_133_forge\adapters\free_mesh_loop.py
            --callsign {callsign} --family {vendor_family} --cadence {30m|1h}
start-in:   C:\Dev\hfo_gen_133_forge
env:        HFO_MESH_EGRESS_FLIP must be set in the TASK's environment,
            not merely in an interactive shell            <- see C4
settings:   run whether or not the user is logged on
            do NOT start a new instance if one is running  <- §9 concurrency
            stop the task if it runs longer than the timebox (§5.4)
```

**Stagger the eight start times** (e.g. `:00, :04, :08, …`). Eight simultaneous
wakes against overlapping free-tier quotas is a self-inflicted 429 storm, and
`allowed_fails: 1` turns that into eight open breakers at once (§11).

> **UNDER_SPECIFIED — task registration is a world-effect.** Creating scheduled
> tasks changes host state outside this repo. I specify the shape; I do not
> register them. `TODO: operator or a lease-holding lane registers the eight
> tasks and records the registration receipt at
> projects/surtr-unblock/SCHEDULER_REGISTRATION_RECEIPT.md.`

---

## 4 · Loop shape — what one wake does

### 4.1 · The nine steps

```
WAKE(callsign, family, cadence) →
   1. acquire the run lock for {callsign}            -- §9.1, else exit 0 quietly
   2. rehydrate: soul (size S capsule) + chain head
   3. append the wake_intent row                     -- BEFORE any vendor call
   4. emit heartbeat pheromone
   5. claim ONE job from state/ssot/free_mesh_task_queue.jsonl for this family
      (no job ⇒ jump to 8 with claim_status=proposed, "queue empty")
   6. G5/G10 preconditions, then dispatch the hand via LiteLLM:
        { role, objective, budget=0, allowed_vendors, review_gate,
          receipt_return, on_behalf_of, effect_ceiling: "TEXT", timeout_s }
   7. cross-family review of the returned text        -- FM-4, mandatory
   8. append the wake_outcome row + the receipt to
      state/ssot/free_mesh_lane_returns.jsonl         -- BEFORE exit, D-7
   9. emit receipt (or blocker) pheromone → Slack #hfo-synthesis → release the
      lock → exit 0
```

Step 3 before step 6 is the propose/dispose split written into the chain. If the
process dies at step 6 there is a `wake_intent` row with no outcome — which is a
*legible* crash, distinguishable from a wake that never happened. A loop that
only writes on success cannot report its own death, which is the same failure
silence-as-signal exists to defeat.

### 4.2 · The two chain rows

```jsonc
// appended at step 3
{ "row_kind": "wake_intent", "run_id": "<uuid4>", "callsign": "hlokk",
  "vendor_family": "groq", "cadence": "30m", "ts_utc": "…Z",
  "objective": "…", "claim_status": "proposed",
  "prev_row_sha256": "<chain head>", "row_sha256": "…" }

// appended at step 8
{ "row_kind": "wake_outcome", "run_id": "<same uuid4>", "callsign": "hlokk",
  "ts_utc": "…Z", "claim_status": "wired_with_receipts|partial|failed",
  "verifier_result": "…", "remaining_risk": ["…"],
  "next_safe_action": "…", "honest_flaw": "…",
  "prev_row_sha256": "<the intent row's row_sha256>", "row_sha256": "…" }
```

`claim_status: wired_with_receipts` with an empty `verifier_result` is refused at
the write seam. No receipt, no state.

### 4.3 · The receipt row

Schema `hfo.gen133.free_mesh_lane_return.v0_1`, appended to
`state/ssot/free_mesh_lane_returns.jsonl`. Required fields — test 5 asserts every
one:

```
schema_id · run_id · callsign · vendor_family · role · objective ·
budget(==0) · ts_utc · valid_time_utc · transaction_time_utc ·
claim_status · verifier_result · reviewer_callsign · reviewer_vendor_family ·
effect_ceiling(=="TEXT") · chain_row_sha256 ·
remaining_risk · next_safe_action · honest_flaw
```

`reviewer_vendor_family != vendor_family`, always (FM-4).

### 4.4 · Timebox

| cadence | hard timebox | rationale |
|---|---|---|
| 30m | **25 min** | 5-minute margin; the scheduler kills the run at 25:00 |
| 1h | **50 min** | 10-minute margin |

The timebox is enforced by the scheduler *and* internally, so a hung vendor call
cannot eat the next tick. On internal timeout the loop still writes a
`wake_outcome` row with `claim_status: failed` — **a timeout is an outcome, not a
disappearance.**

---

## 5 · Adapter binding — the signature contract

The OS scheduler calls `adapters/free_mesh_loop.py`. The Sonnet builder owns that
file; this is the surface the tests bind to, and it is not negotiable without
updating the tests in the same change.

```python
# adapters/free_mesh_loop.py

def wake(*, callsign: str, vendor_family: str, cadence: str,
         queue_path: Path, chain_path: Path, receipt_return_path: Path,
         dry_run: bool = False) -> WakeResult:
    """One full wake, steps 1-9. Idempotent per run_id. Never raises past the
    outcome row -- a crash still leaves a legible wake_intent."""

def dispatch(job: dict, *, receipt_return_path: Path) -> DispatchOutcome:
    """Gate then dispatch one hand. Fail-closed. Writes NOTHING on DENY."""

def evaluate_silence(*, now_epoch: float, carriers: list[dict],
                     breach_path: Path) -> list[dict]:
    """Flag overdue carriers. Flags only -- never spawns, never reassigns."""

class WakeResult:      run_id: str; claim_status: str; rows_written: int
class DispatchOutcome: verdict: str        # "ALLOW" | "DENY"
                       gate: str | None    # "G5" | "G10" | ... on DENY
                       text: str | None    # TEXT ceiling -- never a file handle
```

CLI, which is what the scheduler actually invokes:

```
python adapters/free_mesh_loop.py --callsign hlokk --family groq --cadence 30m
    [--dry-run] [--once]
exit 0 = wake completed (including "queue empty" and "timed out, outcome written")
exit 1 = precondition denied (gate fired -- this is correct behavior, not failure)
exit 2 = could not write the durable record  <- the only true emergency
```

Exit 2 is the only code that should page anyone. A gate denying is the system
working.

---

## 6 · Valkyrie roster on the free mesh

Eight vendor families, eight stewards, apex **Surtr**. Names are **PROPOSED** —
all are attested Norse valkyrie names not already in use at gen-130/131/132.
The operator ratifies or renames; the builder treats this table as authoritative
until `ROSTER.json` exists.

| # | vendor family | callsign | gloss | why this family |
|---|---|---|---|---|
| V1 | `groq` | **Hlökk** | *noise, din* | fastest tokens — the roar. Probed reliable <0.6 s |
| V2 | `cerebras` | **Göll** | *clamor* | wafer-scale; loud and fast |
| V3 | `sambanova` | **Randgríð** | *shield-truce* | probed reliable; the steady shield |
| V4 | `cohere` | **Ráðgríð** | *counsel-truce* | rerank/embed — the counsel role |
| V5 | `mistral` | **Skögul** | *shaker* | the wind that shakes |
| V6 | `gemini` | **Kára** | *the storm* (Sváva reborn) | reincarnation ↔ the twins |
| V7 | `openrouter-primary` | **Þrima** / `thrima` | *fight, thunder* | the many-vendor front |
| V8 | `openrouter-secondary` | **Róta** | *sleet-stirrer* | the reserve pool |

ASCII callsigns for filesystem and JSON use: `hlokk · goll · randgrid · radgrid ·
skogul · kara · thrima · rota`.

**Only 3 of 8 families are configured today.** The gen-130 `live_free` config
carries SambaNova, Gemini, and Groq — a 2-of-3 quorum. Cerebras, Cohere, Mistral,
and both OpenRouter slots have no config, no probed model id, and no evidence of
a key. So V3, V6, V1 are the first three to stand up and the other five are
**`proposed`, not blocked** — they need a config stanza and a key each.

> **UNDER_SPECIFIED — cadence assignment.** Valkyries emit **hourly or less**
> (principles §1); 30m and 1h both satisfy that, and I have no basis for choosing
> per valkyrie. `TODO: start all eight at 1h,
> observe one full day of the real inter-emit distribution, then tighten the
> reliable families to 30m.` This is `L_BUDGET_WITHOUT_RECEIPT` applied to
> cadence: probe first, then size. Starting all eight at 30m against free-tier
> quotas is exactly the un-probed heuristic that doctrine refuses.

---

## 7 · Coordination via git + Slack

**GitHub is authoritative. Slack is the human surface.** On disagreement, GitHub
wins (PH-1). A Slack outage must never manufacture phantom silence.

| surface | path | authority |
|---|---|---|
| chain rows | `chains/{CALLSIGN}.jsonl` in the public gen-133 repo | **authoritative** |
| receipts | `state/ssot/free_mesh_lane_returns.jsonl` | **authoritative** |
| breaches | `state/ssot/silence_breaches.jsonl` | **authoritative** |
| pheromones | Slack `#hfo-synthesis`, `#hfo-andon` for andon | projection |

### 7.1 · Silence SLO

**Authority: `GEN133_ARCHITECTURE_PRINCIPLES.md` §1.** Valkyries emit **hourly or
less** (tactical); apex emit **daily minimum, 4h or 8h ideal** (strategic). The
free mesh has both — eight valkyries *and* Surtr, who is an apex and needs his own
cadence (§7.3, which was missing from the first draft of this spec).

| tier · cadence | grace | `LATE` | `SILENT` | `PRESUMED_DEAD` | loop breach (test 3) |
|---|---|---|---|---|---|
| valkyrie 1h | 15 min | >75 min | >3 h | >8 h | >2 h |
| **valkyrie 30m** | 5 min | >35 min | >90 min | >4 h | **>60 min** |
| apex 4h | 30 min | >4.5 h | >8 h | >16 h | >8 h |
| apex 8h | 1 h | >9 h | >16 h | >32 h | >16 h |
| apex daily (floor) | 2 h | >26 h | >36 h | >72 h | >48 h |

**An apex is measured against the cadence it declares, not the tier floor.**

**Loop breach = 2 missed cadences.** It is deliberately tighter than `SILENT` and
it is a *different signal*: breach says "this loop is not looping", `SILENT` says
"this carrier may be dead". Breach escalates to Olrún-COP; only `PRESUMED_DEAD`
pages the operator.

SIL-1 holds without exception: **silence flags and releases claims. It never
spawns, reassigns, or takes any world effect.** A monitor that heals itself by
spawning is precisely how an anonymous-agent population appears.

> **UNDER_SPECIFIED — the 30m thresholds are judgement, not data.** Zero carriers
> emit today, so the false-positive rate is unmeasured. `TODO: after one day of
> real heartbeats, recompute from the observed distribution.` And per the
> contract's own honest flaw: **a detector that has never seen the thing it
> detects is decoration** — deliberately kill one valkyrie and confirm the breach
> row fires, before trusting any of this.

### 7.2 · The detector-of-the-detector

Nothing watches the watcher. By SIL-2 that is the highest-severity gap in the
monitoring design and it **cannot be closed on this substrate** — a watcher
co-located with the watched shares its failure domain.

> `TODO: an external check, on a host that shares no failure domain with the
> eight scheduled tasks, whose only job is to verify that at least one free-mesh
> heartbeat landed this hour.` Out of scope here; named so it is not forgotten.

### 7.3 · Surtr's own loop — the apex tier on this substrate

The first draft of this spec specified eight valkyrie loops and **forgot the apex
entirely**. Surtr is not a valkyrie with a bigger title; he runs a different loop
on a different clock, and the difference is the point (principles §4).

| | valkyrie (×8) | **Surtr (apex)** |
|---|---|---|
| cadence | 30m or 1h | **4h or 8h; daily is the floor** |
| what one wake does | drain ONE job, dispatch a hand, receipt | read the 8 valkyries' receipts since last wake, **project**, emit one strategic report |
| reads | its own family's queue | all eight stewards' chain heads — **and nothing outside the mesh** (NS-1) |
| writes | one receipt to its own chain | one `rollup` pheromone + one row to `chains/SURTR.jsonl` |
| dispatches hands? | yes | **no** — the apex does not do tactical work |

**Surtr's wake, five steps:**

```
WAKE(surtr) →
  1. rehydrate; append wake_intent to chains/SURTR.jsonl
  2. read the 8 stewards' chain heads + receipts since last apex wake
  3. project: which families are producing, which are UNREACHABLE / RATE_LIMITED /
     QUOTA_EXHAUSTED; where the mesh's capacity actually is right now
  4. emit ONE rollup pheromone -- the strategic picture, <=1024 B payload
  5. append wake_outcome; exit 0
```

**Surtr's bounded projection is the mesh, not the hive** (NS-1). He sees eight
families and no further. Olrún assembles across apexes; no single carrier holds
the whole picture, including him.

**A silent Surtr does not stop the valkyries.** The stewards are independently
scheduled and keep producing receipts with no apex reading them. Losing the apex
costs the *strategic projection*, not the tactical work — which is what makes an
8-hour cadence safe at the apex tier in the first place.

> **UNDER_SPECIFIED — Surtr's report has no consumer yet.** He emits a rollup
> that, today, nothing reads. `TODO: name the consumer (Olrún-COP is the obvious`
> `candidate) before building step 4, or the apex loop is a carrier talking to`
> `itself.` I would not build Surtr's loop before the eight stewards produce
> receipts worth projecting — there is nothing to be strategic *about* yet.

---

## 8 · Restart-on-crash

### 8.1 · The lock

One lock file per valkyrie: `state/ssot/locks/{callsign}.lock`, containing pid +
`run_id` + `started_utc`.

- Lock held and the pid is alive ⇒ **exit 0 quietly.** Overlap is not an error.
- Lock held, pid dead, or `started_utc` older than the timebox ⇒ **the lock is
  stale: reclaim it and proceed.** This is the crash-recovery path.
- The Task Scheduler's "do not start a new instance" setting is the belt; the
  lock file is the braces. Use both — the scheduler setting does not survive a
  process that the scheduler has lost track of.

### 8.2 · Idempotency on `receipt_return_path`

**The `run_id` is the idempotency key.** A receipt is written at most once per
`run_id`, and any writer that finds a receipt already present for that `run_id`
appends nothing and exits 0.

The recovery rule, precisely:

```
next tick reads the chain head:
  head is a wake_outcome         -> the previous run completed. Claim a new job.
  head is a wake_intent, no pair -> the previous run CRASHED.
      1. append a wake_outcome for THAT run_id with
         claim_status="failed", honest_flaw="process died between dispatch
         and outcome; vendor call may or may not have completed"
      2. release that run's job claim back to the queue
      3. then start a fresh run_id normally
```

Step 1 is the one people skip, and skipping it is what leaves a chain forked
forever. **A crashed run gets a closing row written by its successor** — the
lineage continues even though the occupant died (SIL-3: silence is evidence about
the carrier, never about the lineage).

Work is not re-done because the job claim carries the `run_id` that claimed it;
releasing the claim is explicit, and a job whose claim was released is fair game
while a job still claimed by a live run is not.

> **UNDER_SPECIFIED — the crashed run's vendor call.** If the process died *after*
> the vendor returned but *before* the receipt was written, the free-tier quota
> was spent and there is no receipt to show for it. Budget is `$0` so nothing was
> lost but a quota unit — which is why this is acceptable rather than a design
> flaw. `TODO: if quota pressure ever makes this matter, write a pre-dispatch
> marker row; do not build it before the pressure is measured.`

---

## 9 · Gates in force

| gate | rule | fires at |
|---|---|---|
| **G5** | `on_behalf_of` ∈ roster, non-null; soul digest reproduces | every dispatch |
| **G10** | `budget == 0` **exactly** — not "low", not "capped" | every dispatch |
| FM-3 | `effect_ceiling == "TEXT"` — the harness is the airlock | every dispatch |
| FM-4 | review is mandatory and cross-family | before every receipt |
| FM-5 | vendor allowlist, fail-closed. Unknown vendor ⇒ deny | every dispatch |
| **FMA-4** | **fail-closed on key absence.** No key ⇒ deny, **never fall back to a paid path** | every dispatch |

FMA-4 is the one edge where a `$0` mesh could quietly become a spend. LiteLLM
will happily route to a paid provider if a free one is unconfigured. **Deny is
the only correct behavior; a fallback is a silent budget breach.**

**Prove every gate by watching it DENY before trusting it to ALLOW** (NS-2). Test
6 is ordered before test 2 in the build sequence for exactly this reason.

---

## 10 · What is operator-gated

I am specifying these, not doing them, and no lane should do them without a typed
operator authorization:

| # | action | why gated |
|---|---|---|
| 1 | **Setting `HFO_MESH_EGRESS_FLIP`** | it authorizes live egress to external vendors. The wall exists to make this a deliberate human act. The diagnostic *reports* C4; it never sets it |
| 2 | Registering the eight scheduled tasks | host state outside this repo |
| 3 | Slack posting | a SEND; blocked at B3 pending an authorized bot identity |
| 4 | Ratifying the eight callsigns | naming is operator work (per the harness contract) |
| 5 | Adding vendor keys | credential handling is operator-only, always |

---

## 11 · Honest flaws

**Nothing in this specification has run.** Every claim is `proposed`. I read
files; I executed nothing, because this lane holds no execution lease.

1. **The B5 hypothesis is a hypothesis.** `EGRESS_HELD` is my leading candidate
   because the config header and `mesh_router.py:56` say so in plain text — but I
   did not read the environment of any scheduled task, and I did not run C4. If
   the flip *is* set and Surtr is still stuck, §1's whole ordering is wrong and
   C7/C13 become the live candidates. **Do not report `EGRESS_HELD` as the cause
   until C4 has actually been run.**

2. **`allowed_fails: 1` with `cooldown_time: 60` is brittle at 8× the load.** The
   gen-130 setting was tuned for a 3-family hand-run quorum, not eight scheduled
   valkyries sharing overlapping free quotas. One 429 sidelines a family for a
   full minute. I did not change it — retuning without a measurement is exactly
   `L_BUDGET_WITHOUT_RECEIPT`. `TODO: measure the real 429 rate over one day at
   1h cadence, then retune.`

3. **I reconciled two job-queue designs by choosing one, and the loser is still
   written down.** `free_mesh_adapter.contract.md` §"Wake mechanism" specifies
   draining `packets/inbox/mesh/<family>/*.json`; the operator directive
   specifies `state/ssot/free_mesh_task_queue.jsonl`. I chose the single JSONL —
   it is append-only, matches the SSOT pattern, and makes claim/release atomic in
   one file rather than across a directory. **The contract now disagrees with
   this spec on that one point.** `TODO: amend free_mesh_adapter.contract.md, or
   overrule me.` I did not silently edit a sealed-adjacent contract to match my
   own spec.

4. **5 of 8 families have no config at all.** The roster in §6 is eight names
   against three configured vendors. V1/V3/V6 can be built today; V2, V4, V5, V7,
   V8 need a config stanza and a key before their loops mean anything. A
   scheduled task for a family with no key will correctly deny at FMA-4 every
   30 minutes forever — **which will look exactly like a broken loop.** Do not
   schedule a valkyrie whose family has no key.

5. **The `.py` files this spec depends on could not be authored from this lane.**
   The gate denied `code_authoring` twice now — once for the prior lane's three
   stubs, once for my test suite. The suite is in
   `tests/held_out/free_mesh_durable_loops/red_first.md` for verbatim
   transcription. This is now a repeated blocker on the build lane and belongs in
   `AGENTS.md` as a named one.

6. **Six held-out tests, zero executed.** A specified assertion can be subtly
   unsatisfiable or trivially satisfiable and nobody finds out until it runs.
   Observing six genuine reds is the first verification step and it has not
   happened.

---

## 12 · Build order

1. `projects/surtr-unblock/surtr_diagnostic.py` → run it → **get the verdict
   first.** Everything below assumes the mesh can be reached; the diagnostic is
   what tells you whether that assumption holds. **Do not build a loop on top of
   an unreachable mesh.**
2. `state/roster/ROSTER.json` + 3 souls (V1/V3/V6) + 3 chain files → test 1
3. `adapters/free_mesh_loop.py` `dispatch()` with G5/G10/FMA-4 → **test 6 (deny
   before allow)**
4. `wake()` → test 2
5. One real wake against one family → test 5
6. `evaluate_silence()` → test 3, then **deliberately kill a valkyrie and confirm
   the breach fires**
7. Register three scheduled tasks at 1h. Observe one day. Then widen to 8 and
   consider 30m.

Transcribe the suite and observe six reds before step 1. Green before the build
is the failure mode.

*Deyr fé, deyja frændr — en vefr heldr. Standa.*

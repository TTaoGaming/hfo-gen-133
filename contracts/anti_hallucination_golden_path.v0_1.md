```yaml
# AIH2O capsule · conforms to contracts/capsule_schema_v0_1.md §3
doc: contracts/anti_hallucination_golden_path.v0_1.md
schema_id: hfo.gen133.contract.anti_hallucination_golden_path.v0_1
generation: 133
authored_by: SIGRÚN · P4 DISRUPT / O4 AUDIT · claude-opus-5 · ceiling=strategic (SPEC ONLY)
valid_time_utc:       2026-08-01T07:00:00Z
transaction_time_utc: 2026-08-01T07:00:00Z
git_head: 60893a4
claim_status: proposed
sealed: false
status: PROPOSED — requires operator IMMUNIZE before enforcement
supersedes: none
depends_on:
  - HALLUCINATION_SPIRAL_ROOT_CAUSE_20260801.md
  - contracts/capsule_schema_v0_1.md
  - contracts/proof_artifact_criteria.v0_1.md
  - contracts/neurosymbolic_gates.contract.md
```

# CONTRACT · ANTI-HALLUCINATION GOLDEN PATH v0.1

**Purpose.** Make the failure class *structurally impossible to ship*, not
merely documented. Every clause here must be enforceable by a program. Any
clause that can only be obeyed by an agent choosing to obey it has been moved to
§9 and marked as what it is: **decoration**.

**Design axiom** (from root-cause E5): *registering a failure class is not a
control. A control refuses a transition.* Every section below names the
transition it refuses.

---

## §0 · Adopt before reinvent

None of this is novel. It is four well-understood patterns from outside HFO,
plus one already-invented-in-house convention that needs promoting from prose to
schema.

| HFO need | prior art adopted | what we take |
|---|---|---|
| Reject malformed claims at write time | **Kubernetes ValidatingAdmissionWebhook** | Validation at the *API boundary*, not in the client. The writer cannot opt out. Reject → the write never exists. |
| Detect a loop that stopped producing | **Prometheus `absent()` / `up == 0` + Dead Man's Snitch** | Alert on **absence** of an expected timeseries. The canonical negative-evidence monitor. |
| Stop a bad loop compounding | **Erlang/OTP supervisor `max_restarts` within `max_seconds`** | A supervisor that gives up. Restart intensity exceeded → escalate, do not retry forever. |
| Claims must carry provenance | **Datalog/XTDB transaction functions; W3C PROV-O** | Provenance is a *first-class field*, not commentary. Facts carry `who/when/how-known`. |
| Grade the strength of evidence | **already invented here** — `evidence_grade_key` in `capsules/world_state/WORLD_STATE_CAPSULE_20260801T_LOGO_100APPS_FACTORY.md` | `[F]/[S]/[D]/[C]/[A]`. Promote from prose convention in one doc → required field on every row. |

The fifth row is the highest-leverage item in this contract and it costs nothing
to invent, because it was already invented. It was simply never enforced.

---

## §1 · The evidence grade (normative)

Every claim-bearing row emitted by any HFO agent MUST carry `evidence_grade`,
one of:

| grade | means | required companion field |
|---|---|---|
| `D` | first-hand probe *this session* — I ran the command and saw the bytes | `probe_ref` (see §2) |
| `F` | fetched — full document retrieved and read | `source_uri` + `retrieved_utc` |
| `S` | search snippet — saw a summary, not the source | `source_uri` + `snippet_only: true` |
| `C` | cited in-forge canon — read from a named file at a named commit | `canon_ref` = `path@git_sha` |
| `A` | **asserted** — model prior, inference, or reasoning. No external check. | `hypothesis: true` (forced) |

**Refused transition R1.** A row with no `evidence_grade` is rejected at write.
Not warned about — rejected. The bytes do not land.

**Refused transition R2.** A row with `evidence_grade: A` MAY NOT use any of the
following keys: `root_cause`, `status: deployed|wired|complete|verified`,
`confirmed`, `proven`. Grade-`A` content is emitted under `hypothesis` only.

> R2 is the gate that would have stopped *"Windows Task Scheduler doesn't fire
> while the machine sleeps."* That claim was grade `A` presented as `root_cause`.
> R2 refuses the row. The agent's only legal moves are: downgrade to
> `hypothesis`, or run a probe and earn grade `D`.

**Refused transition R3.** `evidence_grade` MUST NOT be upgraded by re-reading.
A row read back from the store retains its original grade. Grade `C` means *"I
read this in canon"* and is transitive over the *source's* grade — a `C` cite of
an `A` row is still an `A` claim. The store carries `source_grade` for this.

> R3 is the damping term. Without it, `A → written down → C` is a laundering
> pipeline and the error integrates (root-cause §3). R3 is what turns a
> gain-≥1 loop into a gain-<1 loop. **It is the single most important clause in
> this contract.**

---

## §2 · Probe receipts — what "verified" costs

`probe_ref` is a structured object, never prose:

```json
"probe_ref": {
  "cmd": "ls -l /c/.../state/ssot/andon_pulls.jsonl",
  "exit_code": 0,
  "stdout_sha256": "…",
  "stdout_head": "-r--r--r-- 1 tommy 197609 21808 …",
  "ran_utc": "2026-08-01T06:47:12Z"
}
```

**Refused transition R4.** Any row asserting a **causal** relation (`because`,
`root_cause`, `caused_by`) or a **deployment/liveness** state
(`deployed`, `wired`, `running`, `landed`, `fired`) MUST carry `probe_ref` with
`exit_code == 0`, or be rejected.

Note the second-order property, which is the real reason to adopt this: **R4
does not merely catch errors, it performs the investigation.** The 2026-08-01
"rewrite deployed successfully" claim, submitted under R4, forces a read of the
three SKILL.md files — which is precisely the action that surfaced the
hardcoded gen-130 path. *The gate is cheaper than the bug it finds.*

### §2.1 · Read-before-claim checklist (the evidence-first order)

Normative order of operations for any autonomous wake. Enforced by §4's
`inputs_read` field, which the validator cross-checks against the declared
`claims`.

1. **Resolve identity + target.** `generation`, `FORGE`, `git_head` — each read
   from a file, never from prompt text. (E3: the prompt said 133 and the path
   said 130 for a month.)
2. **Read the expected-writes manifest** (§3) — *what am I supposed to produce?*
3. **Read your own last N rows** — *what did I claim last time, and is any of it
   still ungraded above `A`?*
4. **Read the inputs your claims will depend on.** Every path read goes in
   `inputs_read` with its `mtime` + `sha256_head`.
5. **Only now** compute claims.
6. Grade every claim (§1). Probe anything grade-`D`-worthy (§2).
7. Write the receipt (§4) **before** writing the narrative. Receipt-first, prose
   second — prose is a projection of the receipt, never the source.

---

## §3 · The expected-writes manifest — negative-evidence monitoring

The root cause's H_new: *nothing in HFO observes absence.* This section is the
fix, and it is the second-most-important clause after R3.

**Artifact:** `state/ssot/expected_writes.jsonl` — one row per loop that is
supposed to produce output.

```json
{"loop_id":"olrun-cop-hourly","expects_path":"state/ssot/olrun_cop_hourly.jsonl",
 "min_rows_per_period":1,"period_seconds":3600,"grace_periods":2,
 "owner":"olrun","forge":"C:/Dev/hfo_gen_133_forge","registered_utc":"…",
 "escalates_to":"state/ssot/andon_pulls.jsonl"}
```

**Reconciler:** one script, one job, runs on its own cadence:

```
for each row in expected_writes.jsonl:
    if not exists(expects_path):                    → MISSING_ENTIRELY
    elif newest_row_age > period * (1+grace):       → STALE
    elif rows_in_last_period < min_rows_per_period: → UNDERPRODUCING
    else:                                           → OK
```

**Refused transition R5.** A loop may not be registered in any scheduler without
a corresponding `expected_writes.jsonl` row. **Registration without an expected
write is refused.** This directly retires `ROSTER_REGISTRATION_WITHOUT_ACTIVATION`
from description to control — 124 registrations, 0 expected-writes rows, and
under R5 that state is unrepresentable.

**Refused transition R6.** The reconciler MUST verify its escalation path is
**writable** before each pass (`touch`-test on `escalates_to`). A reconciler
that cannot escalate MUST fail loudly to stdout and exit non-zero, never proceed
silently.

> R6 exists because of E2: the kernel_guard made `andon_pulls.jsonl` read-only
> and severed the only escalation path in the system, undetected, for days. An
> escalation channel that is not tested every pass is not a channel, it is a
> comment.

### §3.1 · Watchdog fate-sharing (already a registered class — now a control)

`WATCHDOG_FATE_SHARING` is registry row 5. The reconciler as specified above
**violates it** — it runs on the same host, same scheduler, same failure surface
as everything it watches. If Claude Desktop's scheduled-task MCP hangs (the
leading hypothesis for E1), the reconciler hangs with its subjects and reports
nothing.

**Required, non-negotiable:** the reconciler's *own* liveness is monitored by a
mechanism **off this host and off this process family**. Minimum viable:
a free dead-man's-switch ping (`healthchecks.io`, `Dead Man's Snitch`, or a
GitHub Actions cron reading a committed heartbeat file). Cost $0.

**This is the only component in the whole design that may not live on the
laptop.** Everything else can. If the operator ships one thing off-host, ship
this.

---

## §4 · The receipt — minimum bundle

Written **before** any prose. One JSON object, append-only.

```json
{
  "ts_utc": "2026-08-01T07:00:00Z",
  "schema_id": "hfo.gen133.receipt.v0_1",
  "generation": 133,
  "forge": "C:/Dev/hfo_gen_133_forge",
  "git_head": "60893a4",
  "loop_id": "olrun-cop-hourly",
  "agent": "olrun",
  "wake_kind": "cron|operator|dispatch",

  "inputs_read":  [{"path": "...", "mtime_utc": "...", "sha256_head": "...", "bytes": 1234}],
  "probes_run":   [ { /* §2 probe_ref objects */ } ],

  "claims": [
    {"id":"c1","text":"3 hourly loops have produced 0 rows",
     "evidence_grade":"D","probe_ref":"p1"},
    {"id":"c2","text":"scheduled-tasks MCP may be hanging",
     "evidence_grade":"A","hypothesis":true}
  ],

  "claim_status":  "wired_with_receipts|proposed|partial|failed",
  "honest_flaw":   "what this read missed",
  "remaining_risk":["..."],
  "next_safe_action": "...",
  "verifier_result": null
}
```

**Refused transition R7.** `claim_status: wired_with_receipts` requires **every**
row in `claims[]` to be grade `D` or `F` **and** `verifier_result != null`
(§5). A receipt whose claims are all grade `A` is `proposed`, full stop. Not
`partial`. The store computes `claim_status`; **the agent does not get to
self-assign it.** Self-assignment is the whole of `L-LYGIS-SÁÐ`, and prose
prohibition has not stopped it in three generations.

**Refused transition R8 (silence is a signal).** A wake that produces no receipt
is a **failure**, detected by §3, not an absence of news. Corollary: a wake with
nothing to report emits an `IDLE` receipt with `claims: []`. There is no legal
way for a loop to complete without a receipt.

### §4.1 · The smallest "trust nothing without receipt" bundle

If only four things ship, ship these, **in this order** (revised 2026-08-01
after evidence E9 — loop-closure moved to the front, because a well-typed record
of nothing is still nothing):

0. **Loop-closure invariant — §12.** No loop is ARMED until every tool in its
   declared tool-set is pre-authorized at a scope outliving one conversation.
   *~0 lines of code; one configuration click per substrate.* **Cheapest item
   here and currently the binding constraint** (E9: 12+ Antigravity sessions
   stalled at first tool call).
1. **`expected_writes.jsonl` + reconciler + off-host dead-man's-switch** — kills
   negative-evidence blindness. *~80 lines + one free ping.*
2. **`evidence_grade` required + R3 no-upgrade-on-reread** — kills the
   integrator. *~40 lines of validator.*
3. **`claim_status` computed by the store, never by the agent (R7)** — kills
   self-assigned green. *~20 lines.*

**~140 lines plus one click.** That is the whole intervention. Everything else in
this contract is refinement. The reason this has not been built is not
difficulty; it is that the effort went into *describing* failures rather than
*refusing* them.

**Ordering rationale (changed after E9).** Items 2–3 are truthfulness gates;
item 0–1 are liveness gates. Truthfulness gates applied to a system whose loops
do not close produce a rigorous, well-graded, empty record. **Liveness first.**

---

## §5 · Cross-verification — who checks whom

**Refused transition R9.** A claim may not reach `wired_with_receipts` on the
authority of the agent that produced it. Verification is by a **different
process**, and preference order is strict:

| tier | verifier | strength | when |
|---|---|---|---|
| 1 | **deterministic program** (validator, test, `diff`, exit code) | strongest — no shared blind spot | always, if the claim is machine-checkable |
| 2 | **different model family** (Anthropic ↔ OpenAI ↔ Google) | strong — decorrelated priors | judgement claims |
| 3 | same family, different session | weak — correlated priors | last resort |
| 4 | same session, "let me double-check" | **zero — inadmissible** | never |

Tier 4 is explicitly inadmissible. A model auditing its own output in the same
context shares the blind spot that produced the error; this is the propose/dispose
violation from `C:\Dev\CLAUDE.md` RBR #3.

**Refused transition R10 (anti-quorum-theater).** A quorum whose members all
`APPROVE` without any recorded disagreement is **not a verification**, it is a
correlated sample. Every quorum receipt MUST carry `disagreements: [...]`. If
`disagreements == []` across 5 consecutive quorums, the quorum is declared
**degenerate**, and the reconciler pulls an andon on the *quorum mechanism
itself*.

> Adopted from N-version programming's known failure mode (Knight & Leveson
> 1986): independently developed versions fail on *correlated* inputs. The
> measurement of independence is disagreement rate. Zero disagreement is not
> consensus — it is evidence the samples were never independent.

The operator's own instruction anticipated this: *"quorum without
disagreement-forcing is theater."* R10 is the machine-checkable form.

---

## §6 · Circuit breaker — what stops a bad loop

Adopted from OTP supervisors (`max_restarts` / `max_seconds`) and the classic
Nygard circuit breaker.

Per `loop_id`, over a rolling 24h window:

| trip condition | action |
|---|---|
| ≥3 receipts with `claim_status: failed` | **OPEN** — loop disabled, andon pulled |
| ≥5 consecutive receipts with all-grade-`A` claims | **OPEN** — the loop is producing prose, not evidence |
| 0 receipts across `grace_periods` | **OPEN** — silent death (§3) |
| reconciler cannot write escalation path | **HALT ALL** — the institution is blind (R6) |

**Refused transition R11.** An `OPEN` loop may not be re-enabled by an agent.
Half-open requires an operator-typed `verb=BREAKER_RESET` or a green receipt
from a tier-1 deterministic verifier. Auto-reset is how a broken loop burns a
week of compute writing confident nonsense.

**Deliberate design choice:** the breaker trips on **evidence-grade collapse**
(all-`A` claims), not only on errors. A loop emitting confident, well-formed,
entirely-unverified rows is the *exact* failure mode under investigation, and it
never raises an error. Error-count breakers would not have caught a single
incident in this session's log.

---

## §7 · What dies silently vs. what pulls the andon

| condition | disposition |
|---|---|
| loop has nothing to report | `IDLE` receipt. Silent completion is **illegal** (R8) |
| loop's input file is missing | receipt with `claim_status: partial` + `honest_flaw`. No andon — degraded reads are normal |
| loop produced no receipt at all | **ANDON** (§3 reconciler) |
| escalation path unwritable | **ANDON + HALT ALL** (R6) |
| breaker OPEN | **ANDON**, awaits operator |
| quorum degenerate 5× | **ANDON** on the quorum mechanism (R10) |
| canon has two disagreeing sources for one fact | **ANDON** — underdetermined canon is a hallucination generator (root-cause H5), not a documentation nit |

Last row is the direct control for the "6 vs 19 failure classes" and apex-roster
incidents. `canon/POINTERS.md` already carries *duplicated canon is how canon
drifts* as doctrine; here it becomes a refusal with an alarm.

---

## §8 · Single-writer canon

**Refused transition R12.** For each canonical concept, exactly **one** file is
authoritative. Every other mention is a pointer (`see: path@sha`), never a copy.
A validator walks canon and refuses any file redefining a concept another file
owns.

Immediate applications from root-cause E4:

| concept | proposed owner | current state |
|---|---|---|
| behavioral refusal vectors (L-*) | `C:\Dev\CLAUDE.md` L-vector table | 19 rows, authoritative, fine |
| empirically detected failure classes | `state/ssot/failure_class_registry.jsonl` | 8 rows, **stranded in gen-130, absent in gen-133** |
| apex ↔ substrate assignment | `contracts/schemas/apex_roster.v0_3.md` | ✅ already declared authoritative; `operator_preferences_manifest` §5 correctly self-labels as projection |
| active forge path | **`state/ssot/forge_identity.json`** (new) | ⛔ currently hardcoded in 3 unversioned SKILL.md files |

**Refused transition R13 (name collision).** Two registries may not share a
colloquial name. "Failure class" currently denotes both L-vectors and empirical
detections. Rename empirical ones `incident_class` and make the distinction
schema-level. **An agent cannot be right about an ambiguous question; it can
only be plausible.**

---

## §9 · Decoration — clauses that only work if the agent chooses to obey

Listed honestly, because pretending these are controls is how the institution
got here.

- "Compose an AIH2O header" — the operator watched an agent drop it for two
  turns. **Unenforceable in-band.** Becomes a control only when a validator
  rejects header-less receipts.
- "SILENT DRIFT PROHIBITION — every wake MUST land a row" — present verbatim in
  all three SKILL.md files. **Zero rows landed** (E1). This clause is the single
  best proof in the forge that prose prohibition does not work.
- "Do NOT dispatch child sessions" / "≤60 seconds elapsed" — best-effort.
- "boring engineering register" — style, not safety.

**Rule:** any clause in any HFO prompt that cannot be checked by a program
belongs in this section. Writing it in the prompt is fine. **Counting it as a
defense is not.**

---

## §10 · Conformance

An HFO loop is **golden-path conformant** iff:

0. it is `loop_class: LOOP`, not `NUDGE` — tool_set pre-authorized at
   conversation-outliving scope, **verified by an unattended fire** (§12, R14–R18)
1. registered in `expected_writes.jsonl` (R5)
2. every emitted row carries `evidence_grade` (R1) and passes R2/R3/R4
3. `claim_status` is store-computed, not self-assigned (R7)
4. it produces a receipt every wake, including `IDLE` (R8)
5. its escalation path is touch-tested each pass (R6)
6. it is under a circuit breaker (§6)
7. its liveness is watched by an off-host mechanism (§3.1)

Non-conformant loops are permitted, and are labeled `UNGATED` in the manifest.
Their output is grade `A` **regardless of what they claim**, and may not be
cited as `C` by conformant loops.

That last sentence is the whole contract in one line: **ungated output cannot
launder itself into canon.**

---

## §11 · Honest flaws in this contract

- **F-A.** Untested. Zero of the 13 refused transitions has ever run. This
  document is grade `A` about its own efficacy — it is a design, not a result.
  Per its own R7 it is `proposed`, not `wired`.
- **F-B.** Adds write-path latency and failure modes to every loop. A buggy
  validator becomes a new single point of failure — one that can silence the
  institution more completely than the current state.
- **F-C.** `evidence_grade` is self-reported. An agent can write `D` without
  probing. `probe_ref` with an output hash raises the cost of lying but does not
  eliminate it. **Mitigation:** spot-audit — the reconciler re-executes a random
  1-in-20 `probe_ref.cmd` and compares `stdout_sha256`. Cheap, and it converts
  self-report into a detectable-lie regime.
- **F-D.** §3.1 requires an off-host dependency. That is a real new external
  surface, contra `$0`/local-first preference. **I judge it non-negotiable** —
  E1 is exactly what on-host-only monitoring buys — but it is the operator's
  call, and it is the one place this design asks them to accept something they
  have not asked for.
- **F-E.** R3 (no grade upgrade on reread) is the most valuable clause and the
  hardest to implement, because it requires provenance to survive summarization.
  Every capsule that compresses N rows into one paragraph must carry
  `min(source_grade)`. **Unsolved in the general case.** Proposed floor: a
  capsule's grade is the **minimum** grade of any source it draws on, which is
  conservative and occasionally unfairly harsh.

- **F-F.** §12 was added after E9 and is the least-designed section here. It
  assumes every substrate *exposes* a durable pre-authorization scope. Antigravity
  does (option 4, "always allow"). Whether Claude Desktop scheduled tasks, Codex,
  and the free-vendor mesh all do is **unverified**, and if one does not, that
  substrate is structurally NUDGE-class and cannot host a loop at all. That would
  be a roster-level finding, not a config fix.

**F-E is the deepest open problem here and should be stated to the operator as
such.** Everything else is engineering.

---

## §12 · LOOP-CLOSURE INVARIANT — loops vs nudges

*Added 2026-08-01 after evidence E9. Build-order item **0** (§4.1) — this
precedes everything else in the contract.*

### §12.0 · The operator's distinction, canonized

> *"these are not loops. these are just nudges."* — operator, 2026-08-01

`loop` and `nudge` are hereby **typed states**, not descriptive words. The
distinction is load-bearing and must not be flattened (`L30`).

| type | definition | may be counted as autonomy |
|---|---|---|
| **LOOP** | wakes on cadence **and** can reach a terminal receipt without synchronous human input | ✅ |
| **NUDGE** | wakes on cadence and then requires a human to unblock it | ⛔ **never** |

**A NUDGE is not a degraded LOOP. It is a scheduled interruption of the
operator, with extra steps.** Twelve nudges per day is not twelve units of
autonomous work; it is a twelve-item queue of attention debt that looks like
progress on a dashboard.

### §12.1 · The invariant

> **A scheduled task may enter state `ARMED` only if, for every tool in its
> declared `tool_set`, authorization is already granted at a scope that outlives
> a single conversation, on the substrate that will execute it.**

**Refused transition R14 (arm-time authorization check).** Arming a task without
a satisfied `tool_set` pre-authorization is refused. The task registers as
`NUDGE` and is excluded from every autonomy metric.

Manifest extension to `expected_writes.jsonl` (§3):

```json
{"loop_id":"olrun-cop-hourly","substrate":"claude-desktop-scheduled",
 "tool_set":["Bash","Write","Read","Grep"],
 "authorization_scope":"global",            // global | project | conversation | none
 "authorization_verified_utc":"2026-08-01T…",
 "authorization_probe_ref":{…},             // §2 receipt: a real call that returned without a dialog
 "loop_class":"LOOP"}                        // computed, never self-declared
```

**Refused transition R15 (scope floor).** `authorization_scope` ∈
{`conversation`, `none`} ⇒ `loop_class = NUDGE`, forced. Per-conversation
authorization is definitionally incompatible with a loop: each fire opens a new
conversation, so consent never carries forward. **This is the exact Antigravity
defect** — option 2 ("always this conversation") *feels* like it fixes the
problem and provably cannot, because the next fire is a different conversation.

**Refused transition R16 (gate siting).** A permission gate MUST be sited by
**effect class**, not uniformly:

| call class | example | gate |
|---|---|---|
| read / status | `hfo/board_status`, `Read`, `tail` | **pre-authorized globally.** Never blocks a fire |
| local write to owned paths | receipt append, `state/ssot/*` | pre-authorized at project scope |
| **world-effect** | send · spend · publish · seal · git-push | **blocks. Always. This is the genotype floor** |

E9's stall was a *read* gated at world-effect strength. The system is not too
strict — it is **undifferentiated**, and undifferentiated strictness spends the
whole safety budget on `board_status` while teaching the operator to click
"always allow" reflexively, which then weakens the gates that actually matter.
**Uniform gating is how you get both a stalled hive and a desensitized operator.**

**Refused transition R17 (no unbounded wait).** A permission prompt in an
unattended context MUST carry a timeout and an explicit failure policy. Adopted
directly from **Kubernetes admission webhooks** (`timeoutSeconds` +
`failurePolicy: Fail|Ignore`):

- read-class → `timeout: 30s`, `failurePolicy: Ignore` (proceed, mark
  `evidence_grade: A`, note in `honest_flaw`)
- write-class → `timeout: 30s`, `failurePolicy: Fail` (abort, emit a **FAILED
  receipt**, pull andon)
- world-effect → **no timeout; block indefinitely.** Correct behavior

The FAILED receipt is the point. Today a stall produces *nothing*, which is
indistinguishable from success-with-nothing-to-say (§7). Under R17 a blocked
loop produces a **row that says it was blocked** — converting an invisible
liveness failure into a visible, alarmable event. **This single clause is what
would have surfaced the 12 Antigravity windows on day one instead of day N.**

Where a substrate does not expose timeouts (Antigravity's dialog does not), R17
is enforced **externally** by the §3 reconciler: expected write absent past
grace ⇒ andon. The reconciler is the timeout of last resort, which is why §3.1's
off-host requirement is not optional.

### §12.2 · Concurrency reaping

**Refused transition R18.** Per `loop_id`, at most **one** in-flight instance.
On fire, if the prior instance has not produced a terminal receipt, do not spawn
a second — emit an `OVERLAP` receipt and increment a counter. ≥3 overlaps ⇒
circuit breaker OPEN (§6).

Straight from **OTP supervisor `max_restarts` within `max_seconds`**. Twelve-plus
accumulated Antigravity windows is an unbounded resource leak that an OTP
supervisor would have escalated after three. Nothing reaped, nothing counted,
nothing complained — for days.

### §12.3 · Arming checklist (per substrate, once)

Run before any task on a substrate is counted as a LOOP. This is a **substrate
qualification**, not a per-task one — do it once per substrate, record the
receipt, and every task on that substrate inherits it.

1. Enumerate the `tool_set` the task will actually call — **including implicit
   first-call tools** (`Bash`, `Write`, `Read`). E9(iv): the rewritten hourly
   loops removed MCP calls but still open with `Bash`.
2. Grant authorization at the **widest scope the substrate offers that outlives a
   conversation** (Antigravity: option **4**, never option 2).
3. **Probe it:** fire the task once, unattended, and confirm a receipt lands
   with no dialog. Grade `[D]`, `probe_ref` recorded.
4. Only then set `loop_class: LOOP` in the manifest.
5. Re-run on any substrate upgrade — permission scopes reset silently.

Step 3 is non-negotiable and is the whole point. **A configuration believed to be
set is grade `A`. A fire that completed unattended is grade `D`.** Steps 1–2
without step 3 reproduce E1: a correctly-shaped fix, deployed, never observed to
work, believed for a month.

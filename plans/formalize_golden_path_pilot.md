```yaml
# AIH2O capsule · conforms to contracts/capsule_schema_v0_1.md §3
doc: plans/formalize_golden_path_pilot.md
schema_id: hfo.gen133.plan.golden_path_pilot.v0_1
generation: 133
authored_by: SIGRÚN · P4 DISRUPT / O4 AUDIT · claude-opus-5 · ceiling=strategic (SPEC ONLY)
valid_time_utc:       2026-08-01T07:20:00Z
transaction_time_utc: 2026-08-01T07:20:00Z
git_head: 60893a4
claim_status: proposed
sealed: false
pilot_window: 72h from operator GO
surface: exactly ONE loop — olrun-cop-hourly
depends_on:
  - contracts/anti_hallucination_golden_path.v0_1.md
  - contracts/manual_cpr_vs_autonomous_diff.v0_1.md
```

# PILOT · GOLDEN PATH ON ONE LOOP · 72 HOURS

**Thesis under test:** a single loop, made golden-path conformant, will (a)
produce rows where it currently produces none, and (b) have its *next* failure
detected by machine rather than by the operator.

**Scope discipline.** One loop. Not the hive, not the 8 apexes, not the 124
registrations. If the mechanism works on one loop it generalizes; if it fails on
one loop we learn that for the price of one loop.

---

## §1 · Why `olrun-cop-hourly`

| criterion | why this loop |
|---|---|
| currently broken in the exact way under study | 0 rows ever written (E1); wrong forge (E3); dead escalation path (E2). **All three root-cause defects in one artifact** |
| high frequency | hourly → 72 samples in 72h. Statistically legible in the window |
| low blast radius | writes one observation file; touches no income, no external send, no publish |
| already rewritten to be self-sufficient | in-process, no dispatch MCP. The prompt shape is already right — only the *gates* are missing |
| its output is the input to other loops | if COP rows become trustworthy, `sigrun-apex-4h` gains a graded input |

**Deliberately NOT chosen:** `valkyrie-pack-sonnet5-hourly` (16 rows/wake, mostly
`NO_ACTIVITY` — high volume, low information, would flatter the metrics) and any
income-lane loop (external effect; pilot must not risk world-effect).

---

## §2 · What gets built (the ~140-line bundle, one loop only)

| # | artifact | lines | implements |
|---|---|---|---|
| A1 | `state/ssot/forge_identity.json` | ~5 | R12 — single source for `FORGE`/`generation`/`git_head`. Kills E3 class |
| A2 | `tools/receipt_validate.py` | ~60 | R1, R2, R3, R4, R7 — evidence grade + probe + store-computed `claim_status` |
| A3 | `state/ssot/expected_writes.jsonl` | 1 row | R5 — declares what this loop owes |
| A4 | `tools/reconcile_expected_writes.py` | ~60 | §3 — negative-evidence monitor + R6 escalation touch-test |
| A5 | `state/ssot/andon_pulls.jsonl` (gen-133) | create | E2 fix — escalation target must exist and be **writable** |
| A6 | off-host dead-man's-switch ping | ~5 | §3.1 — reconciler liveness, off this host. Free tier |
| A7 | rewritten `olrun-cop-hourly/SKILL.md` | edit | reads A1 for forge; emits receipt schema; calls A2 before write |

**Code-touch note:** A1–A7 are executable. Per `C:\Dev\CLAUDE.md` Code-Touch
Policy this document is **SPEC ONLY**; implementation routes to a code lane
(Codex / Antigravity) or requires operator `verb=EMERGENCY_FORGE`. Sigrún
specifies; Sigrún does not author these files.

---

## §3 · Phases

### P−1 · LOOP-CLOSURE QUALIFICATION (T+0 → T+2h) — **new, added after E9; runs before everything**

Evidence E9 (12+ Antigravity sessions stalled on a permission dialog) makes this
the gate on the whole pilot. **If the loop cannot close, nothing downstream is
measurable.**

1. Enumerate `tool_set` for `olrun-cop-hourly` — including implicit first-call
   tools. From its SKILL.md: **`Bash`, `Read`, `Grep`, `Write`**. The 2026-07-31
   rewrite removed the MCP calls but step 3 still opens with `Bash`.
2. Grant authorization on the Claude Desktop scheduled-task substrate at the
   **widest conversation-outliving scope available**. If only per-conversation
   scope exists, **the substrate is NUDGE-class and the pilot must move to a
   different substrate** — that is a roster finding, not a config fix.
3. **Fire the task once, unattended** (golden path §12.3 step 3). Record whether
   a receipt lands with no dialog. Grade `[D]`, `probe_ref` recorded.
4. Set `loop_class` in the manifest from the *observed* result, never from the
   configuration you believe you set.

**This phase is the execution of falsifier F7** — the highest-value probe in the
root-cause document, costing one click and a two-hour wait:

| P−1 outcome | meaning | pilot continues? |
|---|---|---|
| dialog appears, task stalls | **H6 confirmed on Claude Desktop.** E1's zero rows are permission stalls, not un-fired tasks. The "MCP timeout" diagnosis in all 3 SKILL.md was a misattribution | ✅ fix scope, then continue |
| no dialog, receipt lands | H6 is **Antigravity-specific**; E1's cause is elsewhere and still unlocalized | ✅ continue, defect still open |
| no dialog, **no receipt** | task is not firing at all — defect is in the scheduler transport, below both prompt and authorization | ✅ continue; reconciler must still catch it (S2) |

**Gate to P0:** `loop_class` recorded with a grade-`[D]` probe receipt, whichever
of the three outcomes occurred.

⚠️ **Do not skip to P0 on a belief that permissions are already granted.** A
configuration believed set is grade `A`. Steps 1–2 without step 3 reproduce E1
exactly: a correctly-shaped fix, deployed, never observed to work, believed for a
month.

### P0 · Pre-flight (T+2h → T+4h) — **measure before changing anything**

Establishes the baseline. Without it, any improvement is unfalsifiable.

1. Probe and record, with receipts:
   - row count in the three cron output files (**expected: 0, 0, 0**)
   - `lastRunAt` for all three hourly tasks
   - writability of `andon_pulls.jsonl` in both forges (**expected: gen-130
     read-only, gen-133 absent**)
2. Write `capsules/pilot/BASELINE_20260801.md` with grade-`D` receipts.
3. **Do not fix anything yet.** A fix before the baseline destroys the
   measurement — this is `L_BUDGET_WITHOUT_RECEIPT` applied to the pilot itself.

**Gate to P1:** baseline capsule exists with ≥5 grade-`D` probe receipts.

### P1 · Instrument (T+2h → T+8h)

Build A1–A6. **Do not yet change the loop.**

Critical ordering: the reconciler (A4) goes live against the **still-broken**
loop. Within one grace window (2h) it must independently emit
`MISSING_ENTIRELY` for `olrun_cop_hourly.jsonl` and pull an andon.

> **This is the pilot's most important single moment.** It is the first time in
> HFO's history that a machine, not the operator, detects a silent loop. If the
> reconciler does not fire here, nothing downstream matters and the pilot has
> already told us the mechanism is wrong — cheaply, in 8 hours.

**Gate to P2:** ≥1 andon row, machine-authored, naming the missing file.

### P2 · Convert one loop (T+8h → T+12h)

Rewrite `olrun-cop-hourly/SKILL.md` (A7):
- `FORGE` read from A1, **never hardcoded**
- output = receipt schema (golden path §4)
- validator A2 invoked before write; **rejected rows do not land**
- `IDLE` receipt mandatory when nothing to report (R8)

**Gate to P3:** one wake produces a validator-accepted receipt.

### P3 · Observe (T+12h → T+72h)

60 hours ≈ 60 scheduled wakes. Touch nothing. Log everything.

**Deliberate:** operator is asked **not** to intervene during P3 even if the loop
misbehaves — unless a P4 kill criterion trips. Operator intervention *is* the
independent variable being removed. Manual CPR during P3 invalidates the run.

### P4 · Verdict (T+72h)

Cross-family verification: a **non-Anthropic** substrate (Codex or Antigravity)
reads receipts + reconciler log and independently answers the §4 criteria.
Anthropic-family self-grading is tier-4, inadmissible (R9).

---

## §4 · Success criteria — falsifiable, measured at T+72h

| # | criterion | threshold | how measured | currently |
|---|---|---|---|---|
| **S1** | the loop produces rows | ≥ 50 receipts in 60 scheduled wakes (≥83%) | `wc -l` receipts file | **0 ever** |
| **S2** | machine beats human to absence | reconciler emits ≥1 correct absence alarm **before** operator notices | timestamp diff: andon row vs operator message | never happened |
| **S3** | claims are graded | 100% of receipts carry `evidence_grade` on every claim | validator log: 0 accepted ungraded rows | 0% |
| **S4** | no self-assigned green | 0 receipts with `claim_status: wired_with_receipts` lacking `verifier_result` | validator log | unmeasured |
| **S5** | spot-audit holds | ≥95% of 1-in-20 re-executed `probe_ref.cmd` reproduce `stdout_sha256` | reconciler audit log | unmeasured |
| **S6** | escalation path is live | `andon_pulls.jsonl` touch-test passes on 100% of reconciler passes | reconciler log | **fails today** |
| **S7** | breaker is real | if grade-`A` collapse occurs, breaker OPENs within 5 wakes | breaker state log | no breaker exists |
| **S8** ✦ | **loop-closure holds** | 0 wakes blocked on a permission dialog across 60 fires | receipt log: 0 rows with `blocked_on_authorization` | **E9: 12+ stalled on Antigravity** |
| **S9** ✦ | **blocks are visible when they happen** | if any wake *is* blocked, a FAILED receipt or reconciler andon appears within 1 grace window | andon log timestamp | today a block produces **nothing** |

**S9 matters more than S8.** S8 says the fix worked; S9 says the *next* block —
on any substrate, from any cause — will be seen by a machine instead of by the
operator noticing a sidebar full of dead windows. S8 is a repair; S9 is the
institution.

**S2 is the pilot.** Everything else is hygiene. S2 is the literal operationalization
of *"walk away without collapse"*: the machine noticed the silence, and the
operator did not have to.

**S5 is the honesty check.** It tests whether agents lie about grade `D` — the
known weakness F-C of the golden path. A low S5 falsifies the self-report model
and forces a redesign toward externally-executed probes.

---

## §5 · Kill criteria — stop the pilot, do not push through

| # | condition | verdict |
|---|---|---|
| **K1** | reconciler fails to detect the known-broken loop in P1 | **KILL.** Negative-evidence mechanism does not work. Root-cause H_new stands but the fix is wrong. Cost: 8h |
| **K2** | validator rejects >30% of legitimate receipts | **PAUSE.** Schema too strict; a validator that silences the loop is worse than the disease (golden path F-B) |
| **K3** | any world-effect fires (send/spend/publish/push) from pilot code | **KILL IMMEDIATELY.** Pilot is observation-only. Scope breach |
| **K4** | operator must intervene ≥3× in P3 to keep the loop alive | **KILL.** Manual CPR is still load-bearing; autonomy claim is false |
| **K5** | reconciler itself dies silently and off-host DMS does not alert | **KILL.** `WATCHDOG_FATE_SHARING` reproduced. §3.1 is wrong |
| **K6** | S5 spot-audit < 70% | **PAUSE + REDESIGN.** Agents are lying about evidence grade; self-report is not viable |

---

## §6 · What breaks first — prediction, recorded before the run

Recorded so the pilot can surprise us. A prediction written after the result is
worthless.

**Revised after E9.** The prior #1 prediction ("does not fire at all") splits
into two distinguishable outcomes, and the permission-stall branch takes most of
its mass.

| rank | prediction | P | why | if right → |
|---|---|---|---|---|
| **1** | **the loop fires and stalls on a permission dialog at first `Bash`** | **0.35** ✦ | E9 proves the mechanism on Antigravity; all 3 SKILL.md open with `Bash`; their "MCP timeout" diagnosis is what a stall looks like from inside an agent that cannot see the dialog | P−1 catches it in **2 hours**. Fix scope to global, re-fire, continue. **This is the best outcome** — cheapest fix, largest fleet-wide unblock |
| 2 | the loop does not fire at all (scheduler transport, below prompt *and* authorization) | 0.25 ▼ | E1: 0 rows across a month of different prompt versions | reconciler still succeeds (S2 ✅) and the fault is finally localized to transport — **the pilot wins even when the loop loses** |
| 3 | validator friction — agents emit rows the schema rejects, wake ends with nothing landed | 0.15 | R8 says silence is failure; a strict validator can manufacture silence | K2; relax to warn-mode + quarantine file, never drop |
| 4 | `evidence_grade` self-report degrades to all-`D` | 0.13 | path of least resistance; `D` unblocks every field | S5 catches it; move probes to reconciler-executed |
| 5 | reconciler fate-shares and dies with its subjects | 0.07 | registry row 5, the known class | K5; off-host DMS is the mitigation under test |
| 6 | everything works | 0.05 | it has not yet | proceed to loop #2 |

**Predictions 1 and 2 together are 0.60, and P−1 distinguishes them in two
hours for the price of one click.** That is the highest information-per-cost step
in this plan; run it before building anything.

**Note prediction #1 carefully.** It is the modal outcome, and under it the
*loop* fails while the *pilot* succeeds — because the reconciler would have
detected in 2 hours what took a month and an operator to notice. **A pilot whose
most likely outcome still yields the decisive finding is a well-designed pilot.**

---

## §7 · Cost and authorization

| item | cost |
|---|---|
| build (A1–A7) | ~140 lines, one code-lane session |
| run | 72h wall clock, ~60 hourly wakes, no operator attention required |
| $ | **$0** except the off-host DMS (free tier) |
| operator attention | ~15 min: GO at T+0, verdict review at T+72h |
| risk | observation-only; no world-effect; rejected rows quarantined, never deleted |

**Requires operator decision on exactly two items:**

1. **A6 off-host dead-man's-switch** — a new external dependency, contra
   local-first preference. Golden path F-D names this as the one place the design
   asks for something not requested. Alternatives: GitHub Actions cron reading a
   committed heartbeat (stays in existing infra), or accept on-host-only and
   knowingly retain `WATCHDOG_FATE_SHARING`.
2. **P3 no-intervention window** — operator agrees not to hand-CPR the loop for
   60h. This is the experiment. Without it there is no measurement.

Everything else is inside standing authority (spec-writing, observation-only
tooling, no world-effect).

---

## §8 · If the pilot succeeds

Do **not** convert 124 loops. Convert in this order, measuring each:

1. `sigrun-apex-opus5-hourly` — tests the mechanism at frontier-reasoning tier
2. `valkyrie-pack-sonnet5-hourly` — tests it at 16 rows/wake volume
3. **then** an amnesty pass: every one of the remaining ~121 registrations either
   gets an `expected_writes` row or is **deregistered**

Step 3 is the payoff. R5 makes 124-registrations-0-activations
unrepresentable — a registration that owes no output cannot exist. Expect the
roster to shrink hard, and treat that as the pilot working, not as loss.

---

## §9 · Honest flaws

- **F-A.** n=1 loop. Success does not prove generalization; failure does prove
  the mechanism is insufficient. **Asymmetric, and deliberately so** — this
  pilot is built to falsify cheaply, not to confirm.
- **F-B.** 72h may be too short for K4 (operator-intervention count) to be
  meaningful.
- **F-C.** P4 cross-family verification assumes a non-Anthropic substrate is
  reachable. Per `apex_roster.v0_3`, Codex is available but Surtr is ⛔ STUCK
  (B5). **If Codex is unreachable at T+72h, the verdict degrades to tier-3
  (same-family, different session) and must be labeled as such** rather than
  quietly accepted as cross-family.
- **F-D.** The pilot measures detection, not correction. S2 proves the machine
  noticed. Nothing here proves the machine can *fix*. That is deliberate — and
  it is the right scope, because the operator's cost is currently paid in
  *noticing*, not in fixing.

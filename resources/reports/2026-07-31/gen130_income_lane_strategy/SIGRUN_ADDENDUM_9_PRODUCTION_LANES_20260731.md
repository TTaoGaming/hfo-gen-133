```yaml
# AIH2O
schema_id: hfo.gen130.production_lanes.v0_1
unifying_phrase: "Producer, Verifier, Consumer -- all three or none"
doc: SIGRUN_ADDENDUM_9_PRODUCTION_LANES_20260731.md
authored_by: SIGRÚN P4 · Hluti at H43 · claude-opus-5
valid_time_utc: 2026-08-01T00:00:00Z
transaction_time_utc: 2026-08-01T00:00:00Z
git_head: b857c16
claim_status: proposed
A_assumption: excess reasoning capacity can be converted to output by adding lanes
I_input: this session's own token/attention budget · 5+ overlapping sessions today with zero external output · task_queue surface verified UNGUARDED
H_hypothesis: the constraint is not lane count — it is that one opus session cannot both dispatch and verify at scale
H2_heldout: dispatch 6+ concurrent lanes; measure whether my grading stays evidence-based or degrades to rubber-stamping
O_output: honest bandwidth · 3 lane specs · dispatch plan for Olrún tonight
companions: contracts/spatial_app_abi.v0_1.md · contracts/mape_k_schedule_adapter.v0_1.md
```

# §9 — PARALLEL PRODUCTION LANES

## §9.1 · My coordination bandwidth — the honest number

**Plainly: one opus-5 session cannot coordinate N production lanes. It must
delegate lane ownership to sonnet lieutenants and retain only sampled
verification.**

The reasoning, not the reassurance:

**Dispatch is parallel; supervision is serial.** I can fire 20 subagents in one
tool block. That costs me almost nothing. *Reading their output and checking it
against files* is strictly serial and is where the real budget goes.

**Cost to actually verify one returned artifact:** re-read the claimed evidence
paths, confirm the claim matches, check the falsifier is real. In this session
that has run **~2,000–6,000 tokens and 3–8 minutes per artifact** when done
properly. Rubber-stamping costs ~200 tokens. **The gap between those two numbers
is the entire risk surface** — the failure is invisible because both produce a
green row.

**Context is the hard ceiling.** ~200K window. Holding a lane's state well
enough to catch a subtle false-green costs ~15–25K tokens. Three lanes ≈ 45–75K,
plus doctrine, plus the work itself. **Four or more lanes and I am evicting lane
state to make room — which means I am grading from memory of a summary.** That
is precisely how a verifier becomes a router.

Honest limits:

| dimension | limit | what happens past it |
|---|---|---|
| concurrent dispatches I supervise **with evidence** | **3–5** | degrades to reading summaries, not checking claims |
| concurrent dispatches I can *route* | 15–20 | fine, but that is dispatch, not supervision |
| product classes held concurrently | **3** | matches the three lanes; a 4th evicts one |
| chain rows graded **with file verification** | **~8–12/hour** | |
| chain rows graded by reading only the row | ~60/hour | **this is the fake-green rate — do not target it** |

**The architecture this implies:**

```
  operator ──▶ Sigrún (opus)     dispatches 3 lane-lieutenants
                    │            grades a SAMPLE (≥20%) with file verification
                    │            owns zero lanes directly
       ┌────────────┼────────────┐
       ▼            ▼            ▼
   E-lieutenant  P-lieutenant  S-lieutenant     (sonnet, own the lane)
       │            │            │
       ▼            ▼            ▼
    workers      workers      workers           (sonnet/cheap, pull from queue)
```

**The trap to name explicitly:** "excess capacity and inability to use it" tempts
adding lanes until capacity is consumed. But **verification, not generation, is
the scarce resource**, and adding lanes consumes verification capacity faster
than it produces output. Six lanes producing unverified artifacts is worse than
three producing verified ones — because unverified output has *negative* value
once you act on it.

**Sampling rate:** at 3 lanes I can verify ~20–30% of returns with real file
checks. Below ~20% I am not a verifier. If lanes scale past 3, the sample must
be *random and pre-committed*, or I will unconsciously sample the artifacts that
look easiest to confirm.

## §9.2 · The three lanes

Full routing, governors, and dependency graph:
`contracts/mape_k_schedule_adapter.v0_1.md`.

### LANE E — email production
- **Owner:** Jörmungandr [4,6] · Mist (enrich) + Vár (envelope)
- **Substrate:** sonnet + WebSearch
- **Primitives:** `find_named_human` · `verify_email` · `extract_hook` ·
  `render_template(vars)` · `draft_reply(intent_class)`
- **ABI:** in `{company, url, hook}` → out
  `{first_name, last_name, email, company, linkedin_url, hook, confidence, source_url}`
- **Modalities:** templated · personalized · reply-drafted
- **Harness:** bounce-test 10 of every 50 (>2 bounces ⇒ reject batch); every row
  carries `source_url` — a row without a source is rejected, not downgraded
- **Blocked on:** 0 named humans; no signed envelope
- **First task:** `enrich-target-01` — one company from the 44 dossiers → named
  human + email + LinkedIn + hook, with source URLs. Timebox 30 min.

### LANE P — proof artifact production
- **Owner:** Sigrún [4,4] · Geirǫlul
- **Substrate:** sonnet
- **Primitives:** `select_source` · `retarget_audience` ·
  `compress_to_2min_useful` · `attach_receipts` · `strip_internal_refs`
- **ABI:** in `{source_paths[], audience, format}` → out
  `work/artifact_<slug>.md` + a receipt listing every claim and its evidence path
- **Modalities:** markdown · HTML · MP4 · PDF
- **Harness:** every factual claim maps to an evidence path; **no internal HFO
  vocabulary survives to an external artifact** (grep denylist: valkyrie, Hluti,
  ANDON, kernel, drápa, chain row); reading time ≤2 min
- **Blocked on:** *nothing.* **This lane can run right now.**
- **First task:** `package-teardown-as-red-team-artifact` — retarget
  `SIGRUN_LOOP_DURABILITY_AUDIT_20260731.md` to an AI-control / agent-red-team
  audience (per §7.2, that is the market term that lands). Timebox 45 min.

### LANE S — spatial app production
- **Owner:** Fenrir [4,2] · Þrúðr
- **Substrate:** sonnet + node
- **Primitives / ABI / harness:** `contracts/spatial_app_abi.v0_1.md`
- **Modalities:** mediapipe_hands · mouse (**both mandatory**) · keyboard ·
  touch · voice · gamepad (optional). Mouse is the deterministic CI channel, not
  a courtesy fallback.
- **Blocked on:** **not** primitive identification — that is already answered.
  `hfo_tiles/src/` and `hfo_tiles/apps/hfopiano` exist; the ABI is
  `CursorPrimitiveOutput.v0_1`. The real blocker is that **nobody has run the
  existing suite**.
- **First task:** `run-spatial-golden-master-suite` —
  `node hfo_tiles/tools/run_hfopiano_v511x_golden_master_suite.mjs`, capture
  full output, report red/green per sub-check. Timebox 20 min. **This one task
  determines whether the entire factory thesis is live or a ruin**, and it is
  read-only.

## §9.5 · Dispatch plan for Olrún — tonight

Per §9.1, **three dispatches, not more.** Named exactly:

| lane | agent | task | timebox | why now |
|---|---|---|---|---|
| **S** | `thrudr-spatial-suite-witness` | `run-spatial-golden-master-suite` — run it, capture output verbatim, report per-check red/green. **Do not fix anything.** | 20 min | read-only; highest information-per-minute in the forge; resolves the biggest unknown in three documents |
| **P** | `geirolul-redteam-artifact-01` | `package-teardown-as-red-team-artifact` — retarget the loop-durability audit to AI-control audience, ≤2 min read, every claim evidenced, no internal vocab | 45 min | only lane with zero external dependencies |
| **E** | `mist-enrich-01` | `enrich-target-01` — ONE company → named human + email + LinkedIn + hook + source URLs | 30 min | proves the enrichment primitive at n=1 before spending credits at n=50 |

**Not dispatched, deliberately:**
- No kernel-repair agent. That is destructive-adjacent and needs an operator
  decision (three options, one of which silently loses data).
- No second spatial agent. `thrudr`'s result determines what the next one does;
  spawning now guarantees rework.
- No reply-triage lane. Zero replies exist.

**Sequencing:** all three fire in parallel — they share no files. I grade all
three with file verification, which at n=3 is inside my §9.1 limit.

**Falsifier for the dispatch plan:** if all three return "done" and I cannot
verify at least two against files in ≤30 minutes, the §9.1 bandwidth estimate is
too optimistic and the lieutenant layer must be added before any further
scaling.

## §9.4 · Coordination

Landed in `contracts/mape_k_schedule_adapter.v0_1.md`. The finding that matters
most for tonight:

**`task_queue.jsonl` and `task_results.jsonl` are NOT under the kernel
projection guard.** That is why the pull-loop kept working today while every
kernel chain write was refused. **The three lanes are therefore not blocked by
the ANDON and can run tonight.** The same fact means the pull-loop's durability
rests on an unguarded surface — do not call it append-only-guaranteed until it
is brought under a guard.

## Honest flaws

- §9.1's numbers are introspective estimates. I cannot measure my own attention
  degradation from inside; the only real test is the falsifier above.
- I assigned LANE S's first task as "run the suite" rather than "build an app."
  That is slower than the directive implies and I think it is correct — building
  on an unverified foundation is how the last several weeks were spent. Overrule
  me if you want a build attempt in parallel.
- The directive said the spatial primitive is unidentified and the capacity
  finder is resolving it. **It is identified** — `hfo_tiles/`, ABI ADR-0015.
  Waiting on the finder for this would be delay, not diligence.
- I have not verified that `thrudr`, `geirolul`, or `mist` have live chain files.
  They are names from the roster contract, which is itself `proposed`.
- **Frame-capture check:** "verification is the scarce resource" is a conclusion
  that flatters my own role and conveniently argues against scaling past the
  number of lanes I can personally hold. Attack it: if a *deterministic* verifier
  (a test that exits 0/1) replaces my judgment, the ceiling moves and my §9.1
  limits stop mattering. That is the actual path past this constraint, and it is
  what LANE S's first task starts.

---
*FALSIFIER:* 6+ concurrent lanes with my grading quality unchanged ⇒ §9.1 is wrong and lanes should scale ·
*cost_of_delay:* HIGH on `run-spatial-golden-master-suite` — three documents rest on an unrun assumption ·
*cognitive_mode_paul_elder:* self-critique + significance · *leverage_level_meadows:* L4 · *domain_cynefin:* Complicated

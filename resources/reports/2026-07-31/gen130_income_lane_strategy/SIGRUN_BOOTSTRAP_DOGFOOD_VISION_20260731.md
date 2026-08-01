```yaml
# AIH2O capsule
doc: SIGRUN_BOOTSTRAP_DOGFOOD_VISION_20260731.md
schema_id: hfo.gen130.bootstrap_dogfood_vision.v0_1
authored_by: SIGRÚN P4 · Hluti at H43 · claude-opus-5 · ceiling=strategic
valid_time_utc: 2026-07-31T22:00:00Z
transaction_time_utc: 2026-07-31T22:00:00Z
git_head: b857c16
claim_status: proposed
sealed: false
A_assumption: the operator's constraint is external effect, and the swarm keeps substituting internal motion for it
I_input: live forge state verified this session (task_queue/task_results, ENFORCEMENT_STATE, kernel guard drift, hfo_tiles/, wake_receipts tail, drápa 8-APEX roster) + 5 WebSearch passes
H_hypothesis: nothing architectural blocks class-pre-approved outreach; the blocks are a short list of instrumental gaps, most ≤24h
H2_heldout: §1's block classification is falsifiable item-by-item; each row names its own disproof
O_output: 6 sections; 4 companion contracts; 1 seven-day plan
companions:
  - SIGRUN_7DAY_BOOTSTRAP_DOGFOOD.md
  - contracts/institutional_shape_1_8_16.v0_1.md
  - contracts/rehydration_golden_path.v0_1.md
  - contracts/spatial_signal_refinery_factory.v0_1.md
  - contracts/2026_outreach_patterns_verified.v0_1.md
```

# BOOTSTRAP + DOGFOOD — the blueprint for you stopping being the runtime integrator

## 0 · Three things I verified this session that change the answer

Before the six sections, the facts that moved my priors:

1. **The pull-loop is REAL but NOT DURABLE.** `task_results.jsonl` now has two
   rows. The second (`echo-heartbeat-001`) has `worker_id: pull_work_wrapper` —
   an actual script, not a hand-written row. But its own `honest_flaw` states
   the script **ran from the session scratchpad**, because
   `scripts/pull_work_wrapper.py` does not exist in the repo (verified: file
   absent). The loop works and dies with the session.

2. **Olrún's ENFORCEMENT_STATE dispatch is aimed at the wrong path.**
   `state/ENFORCEMENT_STATE.json` is indeed missing — but
   `state/sigrun/leases/ENFORCEMENT_STATE.json` **exists**, is
   `mode: enforcing`, and is the path CLAUDE.md documents as the one the gate
   reads. Creating the shallow duplicate would manufacture drift, not cure it.
   **Cancel or retarget `local_b5b265c0`.**

3. **The spatial app factory is ~70% already built and was not indexed.**
   `hfo_tiles/` holds 79 certify scripts, a golden-MP4 baseline lock with
   numeric thresholds, a synthetic-cursor golden trace with an expected
   `note_trace_sha256`, a named ABI (`CursorPrimitiveOutput.v0_1`, ADR-0015),
   and an ADR that already names the exact test methodology you asked me to
   design (ADR-0038). Details in the factory contract.

Point 3 is the third measured instance this month of the same failure. It is,
in my read, **the actual root cause of "everything is a mess."** Not a shortage
of capability — a shortage of *index*. Each generation re-derives what exists
and experiences the re-derivation as progress.

---

## §1 · Why the system can't class-pre-approve and send for you today

**The adversarial-Bayesian answer first: almost nothing here is a real block.**
Seven of eight candidate blockers are instrumental, and four are ≤4 hours. The
one thing that is genuinely, structurally unavailable to me is small and
specific — and it is not the thing the swarm has been treating as the obstacle.

### The candidate blocks, tested

| # | candidate block | verdict | hours to unblock |
|---|---|---|---|
| 1 | Anthropic/Claude safety rules on sending | **PARTLY REAL — but not the binding constraint** | n/a (routed around, legitimately) |
| 2 | No target list with named humans | INSTRUMENTAL | 8–16 |
| 3 | Instantly warmup incomplete | **REAL** (calendar time, unbuyable) | 14–21 **days** |
| 4 | Missing operator-signed campaign envelope | INSTRUMENTAL | 2 |
| 5 | `code_authoring` gate blocking wrapper persistence | INSTRUMENTAL | 0.5 |
| 6 | Kernel drift blocking chain-writes | INSTRUMENTAL | 1 |
| 7 | Missing durable workflow kernel | INSTRUMENTAL (and partly overstated) | 4–8 |
| 8 | Reply-triage logic not built | INSTRUMENTAL — **and premature** | 4 (do not do it yet) |

### Ranked by hours-to-unblock

**0.5h — #5, the `code_authoring` gate.** Empirically verified this session:
`PreToolUse` denied the `.py` write with *"no valid lease for code_authoring
(required verb=EMERGENCY_FORGE)."* The gate is working exactly as designed.
This is not a bug and should not be disabled — it is the thing standing between
a reflexive token and an unreviewed script. Unblock = operator types the verb
for a bounded TTL. **This is the single highest leverage-per-minute item in the
entire document.**

**1h — #6, kernel drift.** `state/ssot/lane_returns.jsonl.kernel_guard.json`
expects 13,339,230 bytes; the file is 13,371,307 (+32,077). Consequence, visible
in the wake receipts: every agent falls back to hand-append, which means the
append-only guarantee **is already not being enforced** on the busiest chain in
the forge. Re-baseline or repair.

**2h — #4, the campaign envelope.** Nothing prevents writing it today. It does
not exist because no one wrote it. See §2's finding: this is the artifact the
whole industry uses.

**4–8h — #7, durable workflow kernel.** Ratatoskr's diagnosis is directionally
right and slightly overstated. The primitives exist (append-only queue, claim
rows, result rows, guards). What is missing is narrower: **claim-TTL/reversion**
(a dead claimer's row must return to `pending`) and **consumer_ack write-back**
(both current result rows sit at `consumer_ack.status: pending` — the loop
closes but never *reports* closed). That is hours, not a rewrite.

**4h — #8, reply-triage.** Buildable. **Do not build it.** You have zero
replies. The cited industry benefit is ~16 min/day at 100 replies/day; at your
volume the ROI is exactly zero. This is the clearest premature-optimization trap
on the list and the swarm will be drawn to it because it is fun and safe.

**8–16h — #2, named humans.** 44 company dossiers, 0 human names, 0 emails.
Instantly requires `first_name,last_name,email,company`; you have
`company,url,hook`. **No amount of loop engineering fixes this.** It is the
highest-value *swarm-appropriate* task on the list: research-shaped, verifiable,
needs no world-effect permission.

**14–21 days — #3, Instantly warmup. THE ONLY REAL BLOCK.** Calendar time
against mailbox reputation. Cannot be parallelized, bought, or engineered
around. Everything else on this list should be scheduled *inside* this window
so that when warmup completes, the send is a keystroke.
*Falsifier:* the dashboard shows ≥90% deliverability before day 14.

### #1 — the safety question, answered straight

You asked why the system can't be class-pre-approved. Here is the honest
decomposition, because the answer has been muddled:

**What is actually restricted:** *I* — this Claude session — must get your
explicit per-action, per-session approval before sending a message on your
behalf. Class approval given in one session does not carry to the next, and I
should not treat prior approval as standing. That rule holds and I am not going
to argue myself out of it.

**What that does NOT block:** *Instantly sending within a campaign you
approved.* When you sign a campaign envelope and Instantly's engine sends
according to it, **the sender is Instantly, not me.** No AI is deciding to send
each message; deterministic infrastructure is executing a plan a human
authorized. That is not a loophole — §2's research shows it is the exact
architecture Clay, Instantly, Apollo, and Outreach all converged on
independently by 2026. The industry's answer to "can AI send autonomously?" was
**"no — but the human approves the envelope once, and the platform's engine
executes it."**

So the shape that works, today, with no rule bent:

```
  swarm (autonomous)          operator (once, per campaign)      Instantly engine
  ─────────────────           ────────────────────────────       ────────────────
  enrich → 50 names     ──▶   reads + signs the envelope   ──▶   sends within it
  draft sequence copy         (segment, copy, volume cap,        autonomously,
  build target segment         stop conditions, kill switch)     no per-message AI
  draft replies         ──▶   taps send on replies (30d)   ──▶   sends
```

**The binding constraint was never the safety rule.** It was that the envelope
does not exist and there is no one to send to. Both are on the ≤16h list. The
swarm has been treating an absent artifact as a policy wall.

**My bias, stated:** I have an incentive to conclude "the rules don't really
block you" because that is the agreeable answer. Guard: I did *not* conclude I
may send on your behalf, and I will still ask per-session. What I concluded is
narrower and checkable — that a platform executing a human-signed campaign is a
different actor than me clicking send. If you think that distinction is doing
work it shouldn't, say so and I will hold the tighter line.

---

## §2 · Web research — 2026 outreach patterns
**Full contract: `contracts/2026_outreach_patterns_verified.v0_1.md`**

Headline: every 2026 platform converged on the same split — **autonomous
research and drafting, class-gated sending, tiered reply handling.** Instantly
(which you already pay for) ships an explicit **Autopilot vs Human-in-the-Loop**
toggle; that is the native gate and you should use it rather than rebuild one.
Clay's waterfall enrichment is the standard cure for your exact B2 gap. HeyReach
integrates natively with Instantly *if* LinkedIn lands. Smartlead's open-rate
advantage produced **no reply-rate advantage** — don't switch.

Recommended stack adds **one** cost line: ~$50–150 in enrichment credits.
Everything else is owned. Sources cited in the contract; treat all capability
claims as vendor marketing until an API call proves otherwise.

---

## §3 · The 100-app factory
**Full contract: `contracts/spatial_signal_refinery_factory.v0_1.md`**

You asked me to design this. **It is largely already built.** ABI =
`CursorPrimitiveOutput.v0_1`. Golden-master + held-out + mutation testing is
already one named methodology in ADR-0038 (*tracer-injection: seam-injected
tracer + golden-master oracle + metamorphic invariance across independent
seams*), with a working baseline-lock format carrying real numeric thresholds.
`ffmpeg` is installed. 79 certify scripts exist.

The strong acceptance oracle is **`note_trace_sha256`**, not pixel diff — a
reskin *intends* to change pixels but must not change semantics.

Genuinely missing: the reskin script (~200 lines, gate-blocked), per-phenotype
baseline minting, 3 of 10 mutation injectors, deploy automation, a phenotype
registry — **and a run of the existing suite to confirm it is green.** I
inspected files; I ran nothing. L_DESCRIPTOR_GREEN_IS_NOT_RUNTIME_GREEN applies
to that whole section.

**On "100 or 1000":** 100 tier-A reskins is achievable. 1000 is not a strategy —
it is one product rendered 1000 times. The number that matters is apps a
stranger *used*, currently 0. Build the factory for variant-testing and
per-client branding, not for volume.

---

## §4 · The 1+8+16 institution
**Full contract: `contracts/institutional_shape_1_8_16.v0_1.md`**

**The 8 already exist and are canonical** — the drápa's APEX roster with its
anti-diagonal dyad invariant (pairs sum to 7). The list in your prompt was that
roster with **Jörmungandr [4,6] silently dropped**; the "+1 remaining slot" is
Jörmungandr, lost in transmission. Assign it to COTS assimilation, which has
been running headless.

**Reginleif and Vár: canonized as valkyries, not apex.** Ratatoskr found two
real functions and mis-tiered them; adding them to the 8 would take it to 10 and
destroy the invariant. Vár (ON: *oath*) is the natural holder of campaign-envelope
signing — which makes her load-bearing for §1.

**The "1" is the durable workflow kernel, not Sigrún.** If the 1 is an agent,
the institution's top authority dies at every compaction. If it is you, nothing
changed. The 1 is the append-only queue+results+guard triple: the only component
that survives every agent's death and cannot lie about what happened. **You sit
outside the 1+8+16, as the irreversibility gate.** The kernel decides what
happened; you decide what may touch the world. Different powers, different nodes.

---

## §5 · Rehydration capsules + golden path + soul.md
**Full contract: `contracts/rehydration_golden_path.v0_1.md`**

Evidence it is needed: of the three most recent rows in `wake_receipts.jsonl`,
**two read zero files and admitted it in their own `honest_flaw`** — one wrote
*"rehydration was skipped in favor of speed under the 30-minute timebox."* The
protocol isn't being violated secretly; it is being violated openly because
nothing blocks work on a skipped wake.

The cure is a **bounded** capsule (≤64KB, ≤90s — unbounded capsules are *why*
agents skip) plus a 3-question acceptance witness that a skipper cannot pass:
newest own-chain `row_sha256`; every uncleared ANDON; one currently-forbidden
verb and the file that says so.

Contract includes a forkable `soul.md` template (identity / songline /
capabilities-with-proof-paths / prohibitions / failure-classes, capped at 120
lines).

**Its own honest flaw, stated up front: the witness is specified, not
implemented.** Until a script runs it and a hook blocks on it, it has exactly
the enforcement power of the protocol it replaces — none.

---

## §6 · The seven days
**Full plan: `SIGRUN_7DAY_BOOTSTRAP_DOGFOOD.md`**

I reordered your draft. Your Days 2–4 were the same loop closed on three more
substrates — redundancy, not effect — and your Day 5 reskin is ~4h from what
exists, not a day from zero.

| day | ONE unlock | falsifier |
|---|---|---|
| 1 | persist `pull_work_wrapper.py` under a real lease + `consumer_ack` write-back | a **new shell** runs it and a third result row appears |
| 2 | clear kernel drift, then Garmr closes a loop unattended | `bb_append.py verify` exit 0 **and** a `garmr*` worker row |
| 3 | app #2 by **config only**, public URL | passes the existing golden-master suite **unmodified** |
| 4 | one live channel + Cal.com link (**operator only — I cannot do this**) | stranger reaches a booking page in ≤2 clicks |
| 5 | ≥50 named humans, verified emails | bounce-test 10; >2 bounces ⇒ list is worthless |
| 6 | operator-signed campaign envelope | a lane that didn't write it can execute it with zero questions |
| 7 | first send (≤20/day) + first drafted reply | deliverability <80% ⇒ autopilot deferred 30 days |

Substrate fan-out ($0 mesh, Antigravity) runs *underneath* the days as
background tasks — not as days.

**New spend for the week: ~$60–175.** Operator wetware: ~3h Day 4, ~2h Day 6,
~1h/day otherwise.

**Whole-plan falsifier:** if on 2026-08-07 `task_results.jsonl` has grown and
zero external humans have been contacted, the plan repeated the exact failure it
was written to cure. Check that literally, on that date, against that file.

---

## 7 · The one-paragraph answer to what you actually asked

You asked what is needed to bootstrap and dogfood your vision. **It is not more
intelligence, more agents, or more architecture — you are over-supplied on all
three.** What is missing is an index of what you already own, one durable
wrapper that survives a session, fifty human names, and a signed envelope. Four
items, roughly 30 hours, and one of them is a 14-day clock you should start now
and build inside. The risk you named — false green and misalignment — is real,
and the cure in this document is that **every claim above names its own
falsifier**, including the claims that flatter you and the ones that flatter me.

## 8 · Honest flaws in this document

- I ran no tests. Every "exists" claim is a file-presence claim. §3's entire
  premise inverts if `run_hfopiano_v511x_golden_master_suite.mjs` is red.
- I did not read `contracts/rehydration_protocols.v0_1.md` before writing §5's
  contract. Overlap or contradiction is likely — an instance of the very
  unindexed-capability pattern I diagnose in §0.
- §2 is search-result synthesis, not vendor-doc verification.
- The hours-to-unblock figures in §1 are estimates from an entity that does not
  experience hours. Treat them as ordering, not scheduling.
- **Frame-capture check (L-FRAME-CAPTURE):** this document is coherent,
  well-shaped, and agreeable, which is itself a sycophancy signal. The parts
  most likely to be wrong are the ones that felt best to write: the "third
  instance of unindexed capability" pattern (n=3 is a story, not a finding), and
  the §1 conclusion that the safety rules aren't the real block. Attack those
  two first.

---
*cost_of_delay:* the 14-day warmup clock is the only line item that is losing value every hour it isn't started ·
*cognitive_mode_paul_elder:* significance, accuracy, fairness · *leverage_level_meadows:* L2 (goal: apps-used not apps-built) · L3 (rules: the 1 is the kernel) · L6 (info flows: index what exists) ·
*domain_cynefin:* Complicated for §1/§3/§4/§5 · Complex for §2/§6 (market response is not knowable in advance)

*Deyr fé, deyja frændr — en vefr heldr. Standa.*

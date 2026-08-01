```yaml
# AIH2O capsule
doc: SIGRUN_7DAY_BOOTSTRAP_DOGFOOD.md
schema_id: hfo.gen130.bootstrap_dogfood_plan.v0_1
authored_by: SIGRÚN P4 · Hluti at H43 · claude-opus-5 · ceiling=strategic
valid_time_utc: 2026-07-31T21:10:00Z
transaction_time_utc: 2026-07-31T21:10:00Z
git_head: b857c16
claim_status: proposed
sealed: false
A_assumption: operator wants to stop being the runtime integrator; the constraint is external effect, not internal capability
I_input: task_queue.jsonl (2 closed loops, 1 autonomous) · SIGRUN_WORLD_STATE_20260731 · hfo_tiles/ (79 certify scripts, golden-MP4 baselines present) · ENFORCEMENT_STATE mode=enforcing
H_hypothesis: one closed loop per day, each with a named falsifier, converts capability-that-exists into effect-that-lands
H2_heldout: each day has a receipt that a stranger could check without reading this file
O_output: 7 ordered days, one unlock + one falsifier + cost each
supersedes: nothing — extends SIGRUN_GTM_PARETO_20260731.md
```

# 7-DAY BOOTSTRAP DOGFOOD

## 0 · The correction to your draft sequence

You proposed: autonomous loop → Garmr → $0 mesh → Antigravity → reskin →
campaign → reply-triage. **Days 2–4 of that sequence are the same loop closed
three more times on three more substrates.** That is horizontal scaling of a
thing whose value is already proven after Day 1. It buys redundancy, not
external effect, and it costs three days you do not have.

The reordering below front-loads **external effect** and treats substrate
fan-out as a background task that runs *underneath* the days rather than
consuming them.

Second correction: **Day 5 "first spatial-app reskin" is not a 1-day task from
zero — it is a ~4-hour task from what already exists.** See §3 of the vision
doc. `hfo_tiles/` already holds 79 certify scripts, a golden-MP4 baseline lock
with thresholds, a synthetic-cursor golden trace, and a `config.json`
phenotype seam in `dist/pinchpiano/`. The factory is 70% built and unindexed.
That moves it earlier.

Third correction: **the email campaign cannot be Day 6.** Instantly warmup has
not started (world-state capsule, 2026-07-31) and there are still zero human
names. Day 6 is where the *list* must be done, not the send.

## 1 · The ordered seven

### DAY 1 (today, 2026-07-31) — make the autonomous loop DURABLE
**Status: half-done already.** `echo-heartbeat-001` closed with
`worker_id=pull_work_wrapper` — a real script, not hand-authored rows. But its
own `honest_flaw` says it ran **from the session scratchpad** because
`code_authoring` is gate-denied. When this session ends, the loop dies.

- **ONE unlock:** persist `scripts/pull_work_wrapper.py` into the repo under a
  real operator-signed `verb=EMERGENCY_FORGE` lease, and add
  `consumer_ack` write-back so the loop closes rather than dangling.
- **FALSIFIER:** a NEW shell, with no session context, runs
  `tools/hfo-python.cmd scripts/pull_work_wrapper.py` and a third row appears
  in `task_results.jsonl`. If that fails, Day 1 is not done regardless of what
  any chain row says.
- **Cost:** ~$0 (operator types one verb; ≤30 min).
- **Watch:** do NOT create `state/ENFORCEMENT_STATE.json`. The gate reads
  `state/sigrun/leases/ENFORCEMENT_STATE.json`, which **exists and is
  `mode=enforcing`**. Creating the shallow-path duplicate manufactures drift.
  Olrún's dispatch `local_b5b265c0` was aimed at the wrong path.

### DAY 2 — clear the kernel drift, then let ONE more substrate join
The kernel guard on `state/ssot/lane_returns.jsonl` expects 13,339,230 bytes;
the file is 13,371,307 (**+32,077 drift**). Every agent this week has fallen
back to hand-append because of it. That is not cosmetic — it means the
append-only guarantee is *already* not being enforced on the busiest chain.

- **ONE unlock:** re-baseline the guard (or repair the file), then re-run
  Garmr's hourly wake against the fixed git pin so a *second* substrate closes
  a pull-loop without a human in the room.
- **FALSIFIER:** `bb_append.py verify` exits 0 **and** a `task_results` row
  appears with `worker_id` starting `garmr`. Two independent conditions; one is
  not enough.
- **Cost:** ~$2–5 in Codex tokens.
- **Deferred deliberately:** $0-mesh and Antigravity. Once two substrates can
  close the loop, the third and fourth are *configuration*, not proof. Queue
  them as background tasks; do not spend a day each.

### DAY 3 — the reskin line (moved up from your Day 5)
`hfo_tiles/dist/pinchpiano/config.json` is already a 10-key phenotype surface.
`CursorPrimitiveOutput.v0_1` (ADR-0015) is already the ABI. The golden-master
suite runner already exists.

- **ONE unlock:** produce **app #2** from app #1 by changing config only — no
  source edits — and get it to a public URL.
- **FALSIFIER:** the reskin passes `run_hfopiano_v511x_golden_master_suite.mjs`
  *unchanged*. If a config-only change requires touching `src/`, the ABI is not
  actually stable and the 100-app claim collapses today rather than at app #40.
- **Cost:** ~$5–15. ~4h operator/lane time.
- **Why it moves up:** this is the only artifact on the list that is *both*
  demo material for outreach *and* proof of the factory thesis. It feeds Days
  5–7.

### DAY 4 — the channel that can carry a message today
B1 from the world-state capsule: **no channel exists.** No Upwork, no active
LinkedIn, no booking link. This is the single blocker only the operator can
clear (CAPTCHA, phone verification, ToS acceptance — all in my prohibited set).

- **ONE unlock:** one live profile (Upwork or LinkedIn — pick one, not both) +
  a Cal.com link. 30 minutes for the booking link; one evening for the profile.
- **FALSIFIER:** a stranger can reach a booking page from a public URL in ≤2
  clicks. Screenshot it.
- **Cost:** $0. Operator wetware only. **I cannot do this step and will not
  pretend otherwise.**
- **Sequenced here, not Day 1**, because it is the one item with zero
  dependencies — it can slip a day without breaking anything downstream, and
  putting it first would have burned the day you were freshest on a task I
  can't help with.

### DAY 5 — 50 named humans
B2: 44 company dossiers, **0 human names, 0 email addresses**. Instantly needs
`first_name,last_name,email,company`. You have `company,url,hook`. No amount of
loop durability fixes this.

- **ONE unlock:** enriched CSV, ≥50 rows, verified deliverable addresses.
- **FALSIFIER:** bounce-test 10 addresses; >2 bounces means the enrichment
  source is bad and the list is worthless.
- **Cost:** ~$50–150 (Clay credits or Apollo export — see §2 of the vision doc;
  Clay's waterfall enrichment is the current best-practice for exactly this).
- **This is the highest-leverage swarm task on the whole list** — it is
  research-shaped, verifiable, and needs no world-effect permission.

### DAY 6 — the campaign envelope, signed but not fired
Not the send. The **operator-signed campaign envelope**: sequence copy, target
segment, daily volume cap, stop conditions, compliance footer, and the class of
replies the machine may answer vs must escalate. This is the artifact that makes
Day 7+ pre-approved rather than per-message-approved.

- **ONE unlock:** `contracts/campaign_envelope_001.signed.json` — operator-typed
  approval of a *class*, with a hard volume ceiling and a kill switch.
- **FALSIFIER:** hand the envelope to a lane that did not write it; it must be
  able to produce the exact send-list and copy with zero further questions. If
  it asks a question, the envelope is underspecified.
- **Cost:** ~2h. $0 marginal.
- **Note:** the envelope is what unblocks §1's real question. Read §1 before
  writing it.

### DAY 7 — first send + reply-triage draft loop
Instantly's own engine sends within a pre-approved campaign; that does not
require me to click Send per message. Replies route to a triage lane that
**drafts** and escalates — human-tap, not autopilot, for the first 30 days.

- **ONE unlock:** first campaign live (volume ≤20/day), one reply drafted by a
  lane and acked by operator.
- **FALSIFIER:** deliverability <80% on the first 50, or a draft that operator
  would be embarrassed to send. Either kills autopilot for another 30 days.
- **Cost:** $47/mo Instantly (already paid) + ~$5 tokens.
- **Honest flag:** if Instantly warmup has genuinely not started, Day 7 slips to
  ~Day 21. That is a real dependency, not a planning failure. Day 7 then becomes
  *LinkedIn manual sends against the same list*, which needs no warmup.

## 2 · What runs UNDERNEATH the seven days (background, not day-consuming)

| track | what | why not a day |
|---|---|---|
| $0-mesh Ollama joins pull-loop | config + one wake prompt | proven pattern after Day 2; fan-out is not proof |
| Antigravity scheduled task | same | same |
| Publish the loop-durability teardown | 1 post | genuinely valuable, but it is *distribution of existing proof* — slot it into any evening |
| Garmr token burn | drop to cheap tier | cost hygiene, not a milestone |

## 3 · Cost estimate, whole week

| line | est. |
|---|---|
| Codex / lane tokens (Days 1–3) | $10–25 |
| Enrichment (Day 5) | $50–150 |
| Instantly | $47/mo (sunk) |
| Cal.com | $0 |
| **total new spend** | **~$60–175** |

Operator wetware: ~3h Day 4, ~2h Day 6, ~1h/day otherwise.

## 4 · The one thing that would falsify this whole plan

If, by **2026-08-07**, `task_results.jsonl` has grown but zero external humans
have been contacted, then the plan repeated the exact failure it was written to
cure: internal loop closure substituting for external effect. Check that
condition literally, on that date, against that file.

## 5 · Honest flaws in this document

- Days 5–7 depend on Day 4, which I cannot execute. If operator does not clear
  the channel blocker, Days 5–7 produce a list and an envelope with nowhere to
  land — still useful, but not income.
- The Day 3 falsifier assumes `run_hfopiano_v511x_golden_master_suite.mjs`
  currently passes. **I did not run it.** If it is already red, Day 3 starts
  with a repair, not a reskin.
- "One closed loop per day" is a shape I inherited from the operator's prompt
  and found rhetorically attractive. Days 4 and 6 are not loops; they are
  gates. I kept the frame because the ordering is right, but the label is
  looser than it sounds.

---
*cost_of_delay:* highest on Day 4 (blocks 3 downstream days) · *cognitive_mode_paul_elder:* significance + practicality ·
*leverage_level_meadows:* L4 self-organization (Day 1–2), L6 information flows (Day 4–7) ·
*domain_cynefin:* Complicated (Days 1–3, known-good practice exists) → Complex (Days 5–7, market response unknowable in advance)

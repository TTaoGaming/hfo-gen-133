```yaml
callsign: sigrun
ceiling: strategic
session_anchor_utc: 2026-07-30T22:35:00Z
chain_head_prev_sha256: UNANCHORED
soul_hash: ABSENT
substrate: claude-opus5
model_family: anthropic
arch_family: anthropic
model_id_at_dispatch: claude-opus-5
quota_bucket: anthropic.max5.acct1
cognitive_mode: [accurate, deep, fair]
leverage_level: meadows_4
andon_status: 1_pulled_0_confirmed
strategic_pheromone_ref: SP-015
pain_point_ref: PP-01
supersedes: SIGRUN_NEXT_4_BLOCKERS_20260730.md (B1-B4 answered)
rehydrated: true
```

# The next four blockers — B5 through B8

*B1–B4 are answered and off the board. The ICPs you asked for are written and
live in `SIGRUN_INTENT_MODEL_20260730.md` — v0 hypotheses, not questions back to
you. B5 is the one you named, and I rank it first too.*

---

## B5 — The $0 mesh isn't running. Do we fix throughput, or fix the work order?

**Analogy.** You hired a night shift, issued badges, unlocked the building — and
nobody wrote a work order. They clock in, stand around, clock out. Payroll is $0,
so nobody noticed for weeks.

**Best practice.** An autonomous loop needs four parts or it degenerates into a
heartbeat: a durable queue of pre-written items with acceptance criteria; a
worker that pops exactly one and is *forbidden* from inventing its own; an
external-effect assertion at the end; a dead-man switch. Free local models fail
almost entirely at part one — with no queue they self-generate plausible work and
produce documents. `chains/job_queue.jsonl` exists here; whether anything loads
it is unverified by me.

**Options.**
(A) **Queue-first, one loop.** Kill every loop but one. Pre-seed 20 job rows,
each with an acceptance witness. The Ollama worker pops one per cycle, may not
author its own job, must attach an artifact path. Zero new spend.
(B) **Model-first.** Wire more free tiers (Gemini, Groq, Cerebras) for throughput.
(C) **Scheduler-first.** Debug the Codex goal-loop and Task Scheduler plumbing so
the loops already asserted actually fire.
(D) **Accept it.** Run the mesh by hand when you're at the desk.

**My recommendation: A.** Throughput is not the constraint — a mesh producing
nothing faster still produces nothing. The missing part is a work order the free
model cannot wriggle out of.

**You pick:** whether I may kill the other loops. Queue seeding, worker prompt,
and the no-self-authored-jobs guard are the machine's.

**Signoff:** Codex on host — I cannot verify my own liveness, and it can read
whether those loops actually fire.

---

## B6 — How many domains and mailboxes. You asked for a number.

**Analogy.** Domains are the land; mailboxes are the rent. Land is cheap and
takes three weeks to turn fertile. Rent starts the day you sign.

**Best practice.** One primary that never sends cold, only receives. Two to three
lookalike sending domains, two to three mailboxes each, 20–30 sends per mailbox
per day after a two-to-three-week warmup. Exceeding that per-mailbox ceiling is
the most common way people burn a domain. Replace sending domains annually.

**Options.**
(A) **Land now, rent later.** Buy 2 more lookalikes tonight (~$20 one-time, 4
domains total). Open 2 mailboxes on `.dev` now, start warmup (~$12/mo). Add
mailboxes on the new domains only after reply #1. Full build-out later: 9
mailboxes ≈ 200–250/day, ~$55–70/mo.
(B) **Full build now.** 3 domains × 3 mailboxes. ~$70/mo from tonight, ~200/day
live in three weeks.
(C) **Minimum.** `.dev` only, 2 mailboxes, ~50/day, ~$12/mo.
(D) **Burn one of the twelve domains you already own** instead of buying.

**My recommendation: A.** Warmup is the long pole and domains are nearly free, so
buy the land tonight — but nine mailboxes before you know the message converts is
a bigger megaphone for an untested sentence, and the three warmup weeks are
exactly when you learn whether it converts.

**You pick:** yes on ~$20 tonight, and the recurring number you'll tolerate. DNS,
SPF/DKIM/DMARC, warmup ramp are Garmr's.

**Signoff:** Codex on host — it can read live Cloudflare state and tell us which
of the twelve are already authenticated, rather than taking my word.

---

## B7 — Life insurance: your carrier has a cold-accessible niche. Use it.

**Analogy.** You've been handed keys to a building and told to find people who
want in. There's a side door with a public directory of everyone who already uses
the building — and almost no other agent bothers to read it.

**Best practice.** For a new agent with no warm market, the move is a *niche with
a public roster*. National Life's structural strength is the K-12 403(b) teacher
retirement market — district vendor lists and staff directories are public
records, making it the rare insurance audience addressable cold at scale.
Colorado alone has tens of thousands of public school employees. **Hard gate:**
carrier advertising compliance — every outbound piece needs NLG review before it
sends, and New York's best-interest rule adds texture. Educational content clears
review far faster than product pitches.

**Options.**
(A) **CO K-12 403(b) niche, cold, $0.** Public district staff directories,
compliance-approved *educational* material only, run as a fourth phenotype on the
sending stack you're already building.
(B) **Buy internet leads,** $15–60 each, 3–8% close. Fast, cash-negative first.
(C) **CPA / estate-attorney partnerships.** Free, 8–16 weeks — and note this is a
warm-network play in a costume, which is the drift class I owe you.
(D) **Park it** until an AI lane pays.

**My recommendation: A.** The only option that is simultaneously $0, cold,
compliant-able, and reuses infrastructure you're building anyway. And on states:
**don't buy more yet.** Your constraint is pipeline, not geography — a licence
before a working message in CO is more orchard you can't pick.

**You pick:** whether every LI email routes through NLG compliance review first
(I think it's non-negotiable, but it's your licence, not mine).

**Signoff:** Ollama trio — I am outside my competence in a regulated industry and
a non-Anthropic dissent is worth more here than my confidence.

---

## B8 — What counts as "the swarm did something." You said you didn't know; here's my list.

**Analogy.** You asked for a punch clock. One that reads badge swipes measures
attendance. You want one that reads the loading dock.

**Best practice.** The predicate must be narrow, countable, falsifiable, and
involve a recipient outside the building. **T1** — a message left the building to
a human who did not ask for it (cold email, DM, application). **T2** — a public
artifact became fetchable at a URL by a stranger. **T3** — a reply came back. T1
and T2 are effort and count for the gate. T3 is outcome and must never be the
gate, because you don't control it.

**Proposed default week** (the "what" you handed me): Mon send batch · Tue publish
one public teardown artifact · Wed send batch · Thu compliance-cleared LI
outreach · Fri one public artifact plus a reply audit. One T1-or-T2 per business
day is the floor.

**Options.**
(A) **Daily counter, 2-strike, business-days-armed.** Two consecutive zero-effect
business days → 24-hour halt of all loops and a page. Weekends run but can't trip
it.
(B) **Your literal spec:** one zero day → immediate 24-hour halt.
(C) **Weekly quota,** 5 per week, halt on a missed week. Smoother, slower.
(D) **Advisory only.**

**My recommendation: A.** Your spec with a one-day noise filter — one zero day is
a bad Tuesday, two in a row is a broken machine. Flagging honestly that A is
softer than you asked for; say the word and it's B.

**You pick:** 2-strike or your original 1-strike, and whether T2 counts or only
T1. Predicate wiring, tests, and Rego are the machine's.

**Signoff:** Codex adversarial-Bayes — a halting gate I designed, and benefit
from passing, should not be graded by me.

---

**Honest flaw:** B6 and B8 both assume the sending stack exists this week. If it
doesn't, B5 is the only live blocker here and the other three are theatre. B7's
compliance gate is what I'm least certain of and the thing that can silently kill
the lane — verify it with National Life directly, not with me.

*Sending er sönnun. Allt annat er undirbúningr. Standa.*

```yaml
callsign: sigrun
ceiling: strategic
artifact: SIGRUN_NEXT_4_BLOCKERS_B5_B8_20260730.md
claim_ceiling: PROPOSAL — recommendations are Sigrún's picks; operator decides
blockers_surfaced: [b5_zero_dollar_mesh_loops, b6_domain_mailbox_sizing, b7_li_cold_niche, b8_external_effect_predicate]
operator_decisions_required: 4
recommendations: {b5: A_queue_first_one_loop, b6: A_land_now_rent_later, b7: A_k12_403b_cold_niche, b8: A_daily_2strike_24h_halt}
cross_family_signoff_requested: {b5: codex_host, b6: codex_host, b7: ollama_trio, b8: codex_adversarial_bayes}
icps_delivered_in: SIGRUN_INTENT_MODEL_20260730.md
external_receipt_count: 0
sealed: false
rehydrated: true
```

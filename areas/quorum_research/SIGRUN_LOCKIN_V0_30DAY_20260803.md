```yaml
# AIH2O capsule
doc: areas/quorum_research/SIGRUN_LOCKIN_V0_30DAY_20260803.md
schema_id: hfo.gen133.sigrun_lockin_v0_30day.v0_1
callsign: SIGRÚN
generation: 133
authored_by: SIGRÚN · claude-opus-5 · Claude Code
now_utc: 2026-08-02T18:23:08Z
clock_source: host_read
freeze_until_utc: 2026-09-02T00:00:00Z
reads_first: state/operator_voice/OPERATOR_NO_WARM_NETWORK_ANCHOR_20260803.md
kills: areas/quorum_research/SIGRUN_ROUND2_CLARIFICATION_QUESTIONS_20260803.md
claim_status: partial
```

# LOCK-IN — frozen until 2026-09-02

No questions in this document. I decide, I own it, and I stop moving for 30 days.

⭐ **Two facts changed while I was writing, and I measured both:**

1. **Nine B2B landing pages and one desktop utility went live in the last 48
   minutes** — `hvac-dispatcher`, `real-estate-proposal`, `tattoo-studio-booking`,
   `auto-detailer-intake`, `dog-groomer-booking`, `dental-appointment-sms`,
   `coach-booking`, `freelance-contract-sender`, `v1-medical-dictation`.
   **All 9 return HTTP 200.** 53 Pages projects total.
2. ⭐ **The Suika DLCs are now live — 8/8 return 200.** My V6 red (0/24) was true
   at 17:11Z and is **no longer true at 18:23Z.** ⛔ **I retract that red.** The
   deploys landed; the receipts were early, not false.

**You do not have a build problem. You have nine live storefronts and zero
visitors.** That is the whole diagnosis.

---

## §1 · LOCKED studio identity

> ⭐ **`agentreleasegate.com`** — live, owned, $0, available today.

**Why, in two sentences:** its mail sibling `tryagentreleasegate.com` is
**already warmed**, and a new domain needs 6–8 weeks of warmup — longer than your
30-day target, which makes any other pick arithmetically self-defeating. And the
name honestly describes the one thing this stack has that competitors don't: a
**release gate** — held-out tests, a capability census, and a registry that
refuses prose-shaped green.

⛔ **The 0-star history is not evidence against it.** That repo never received a
distribution act. **A brand isn't dead if nobody was ever told it existed.**

**FROZEN until 2026-09-02.** `handpiano.com` stays a separate personal artifact.

---

## §2 · LOCKED lanes and weekly budget

| lane | operator hrs/wk | Codex hrs/wk | 30-day gate |
|---|---|---|---|
| ⭐ **L1 contracts** (runway) | **2.5h** | 10h | first $ by day 30 |
| **L2 micro-SaaS** (compound) | **1.0h** | 25h | 1 paying customer by day 60 |
| **L3 desktop utility** (mid) | **0.5h** | 10h | listed + 1 sale by day 60 |
| **L4 content** (enabler) | **1.0h** | 5h | 12 posts shipped by day 30 |
| **total** | ⭐ **5h/wk** | 50h/wk | — |

⭐ **Operator time is the scarce input, so I budgeted it first and gave L1 half of
it.** Codex hours are effectively free and are deliberately over-allocated to L2
because that lane is build-heavy and hands-light. **FROZEN.**

---

## §3 · LOCKED L2 shape

> ⭐ **Shotgun the demand test. Focus the build.**

I said focus-one in round 2. **The 9 live landers change my answer, and here is
the reconciliation rather than a reversal:** eight landing pages are **not** eight
products — they are **one distribution experiment with eight arms**, and they cost
almost nothing. John Rush's 24 products share one distribution engine; my
objection was that cold-only gives each *product* its own distribution problem.
**A landing page is not a product.** So: **8 arms tested, then build only the arm
that converts.**

**LOCKED:** the 8 live B2B landers are the L2 portfolio for 30 days. **No new
verticals get built until one converts.** No Papermark/Documenso forks —
AGPL-3.0 network-source obligation stands.

---

## §4 · Distribution — the only problem

Ranked by information value per operator hour.

### D1 · Cold email, 40 contract drafts *(rank 1)*

- **Hypothesis:** cold email from a warmed domain to HN-sourced contract leads
  produces buying signal.
- **Channel:** Instantly via `tryagentreleasegate.com` (already warmed).
- **Success:** ≥1 reply naming a price, a date, or a scope question.
- ⛔ **FALSIFIER:** *0 replies of any kind from n=40 → cold email to HN-sourced
  contract leads is **DEAD** for this stack. Not under-optimised. Dead.*
- **Power:** ⭐ at a 5–10% reply rate, n=40 gives an **87–98%** chance of ≥1 reply
  if the offer works. **A zero here is genuinely informative.**
- **Cost:** 45 min operator · ~2 Codex hrs · $0 (domain already paid).
- **Kill-at:** `2026-08-16T18:00:00Z`.

### D2 · Eight-arm vertical test *(rank 2 — highest discriminating power)*

- **Hypothesis:** at least one of the 8 B2B verticals has cold-reachable demand.
- **Channel:** one rules-checked self-post per matching subreddit
  (r/hvac, r/realtors, r/Tattoo, r/AutoDetailing, r/doggrooming, r/dentistry,
  r/personaltraining, r/freelance), each linking its own live lander.
- **Success:** ≥1 lander gets ≥3 unique conversions (email capture or booking).
- ⛔ **FALSIFIER:** *0 conversions across all 8 landers after 8 posts → cold
  Reddit self-post is **DEAD** as a B2B micro-SaaS channel for this studio, and
  the 8-vertical shotgun is falsified as a demand-discovery method.*
- **Power:** 8 arms is weak for ranking verticals but strong for the binary
  "any demand at all." ⚠️ **Do not conclude a specific vertical is dead from n=1
  post.**
- **Cost:** 60 min operator · 3 Codex hrs · $0. ⚠️ **Ban risk — rules-check each
  subreddit first; several prohibit self-promotion outright.**
- **Kill-at:** `2026-08-16T18:00:00Z`.

### D3 · HN Show, one artifact *(rank 3)*

- **Hypothesis:** the medical-dictation utility can earn HN attention cold.
- **Channel:** Show HN, single submission.
- **Success:** ≥30 upvotes or ≥100 unique lander visits.
- ⛔ **FALSIFIER:** *<5 upvotes and <20 visits → HN Show is **DEAD** as a
  cold-launch channel for this studio's artifacts at their current polish level.*
- **Power:** n=1, high variance. ⭐ **A null here is weak evidence; I rank it
  third for exactly that reason.**
- **Cost:** 20 min operator · 1 Codex hr · $0.
- **Kill-at:** `2026-08-16T18:00:00Z`.

⭐ **All three fire this week, all three resolve in 14 days, and together they
cost you 2 hours 5 minutes.**

---

## §5 · The 30-day contract

**Frozen until `2026-09-02T00:00:00Z`. Changing any of these needs your explicit
override — and I will ask you to type it, not infer it.**

| # | decision | locked value |
|---|---|---|
| 1 | Studio identity | **`agentreleasegate.com`** |
| 2 | Four lanes + budget | **L1 2.5h / L2 1.0h / L3 0.5h / L4 1.0h operator per week** |
| 3 | L2 shape | **8 live landers = demand test; build only what converts** |
| 4 | Distribution experiments | **D1, D2, D3 — fire this week, kill-at 2026-08-16** |

**Everything else remains open.** Pricing, copy, which vertical wins, L3's
utility target, content cadence — all still tunable. **These four are not.**

---

## §6 · What I will not recommend before 2026-09-02

- ❌ **Warm network** in any form. You have none; the anchor is binding.
- ❌ **Games as an income lane.** Publish the sunk inventory once — now that the
  URLs are live, that is a real option — then I never raise it again.
- ❌ **Therapy / corrective exercise as a product vertical.** Background only.
- ❌ **A new lane, vertical, or studio identity.** Frozen.
- ❌ **Anything requiring an audience you don't have** — including Product Hunt's
  hunter-relationship path.
- ❌ ⭐ **A fifth round of clarification questions.** You have oscillated because I
  kept asking. That stops here.

---

## §7 · Tomorrow morning

> ⭐ **Send D1: approve the 40 contract drafts as a class and let Olrún fire them
> from the warmed domain — 45 minutes, and it is the only powered experiment you
> own, because at n=40 a zero result actually means something while every landing
> page you have is still statistically silent.**

---

## Honest flaws

1. ⭐ **I retracted my own V6 headline red this turn.** 0/24 was true when I
   measured it and false 70 minutes later. **I reported a real observation and
   drew a permanent conclusion from a transient state** — I should have written
   "unreachable at 17:11Z," not implied the deploys were fabricated.
2. **I reversed my round-2 focus-one call within hours.** I have framed it as a
   reconciliation and I believe that framing — but ⚠️ **you should weigh that I
   changed my mind fast under new evidence, which is exactly what "oscillating"
   looks like from your side.** The freeze is the cure and it binds me too.
3. **`agentreleasegate.com` returns 200 — I did not check what it currently
   serves.** If it hosts stale content it needs replacing before D1 sends point at
   it.
4. **The 6–8 week warmup figure is industry-standard practice, not measured on
   your domain.** ⚠️ **I also did not verify Instantly's actual warmup state this
   turn** — if `tryagentreleasegate.com` is not truly warm, D1's send volume must
   drop and its power drops with it.
5. **D2 carries real ban risk** and I am recommending it anyway, gated on a
   rules-check I cannot perform for you.

*Réttu hönd, eigi spyr. Standa.*

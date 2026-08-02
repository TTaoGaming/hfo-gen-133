```yaml
# AIH2O capsule
doc: areas/quorum_research/SIGRUN_CANON_V5_TOP4_EXPERIMENTS_20260803.md
schema_id: hfo.gen133.sigrun_canon_v5_top4_experiments.v0_1
callsign: SIGRÚN
generation: 133
authored_by: SIGRÚN · claude-opus-5 · Claude Code
now_utc: 2026-08-02T16:56:11Z
clock_source: host_read              # bash `date -u -Iseconds`, this turn
extends: areas/quorum_research/SIGRUN_CANON_V4_FIRST_PERSON_REPORT_20260803.md (chain row 98)
claim_status: partial
```

# V5 — top 4 experiments, with falsifiers

⭐ **I found something before I ranked anything, and it changes the week.**
`outputs/staged_sends/` holds **150 outbound drafts, already written, validated,
and never sent** — 40 contracts, 40 employment, 40 grants, 30 games, every one
marked `STAGED_FOR_OPERATOR_APPROVAL_NEVER_SENT`.

**Your outbound is not un-built. It is un-approved.** In V4 I called "nothing has
ever been contacted" blocker #1 and implied a build. I was wrong about the shape:
it is a **batch signature**, roughly one hour of your time.

*(Also recorded: all 7 Upwork RSS queries returned **HTTP 410 Gone** — the drafter
substituted live HN posts rather than fabricating targets. That is the behaviour I
want and I am noting it because it is rare.)*

**Score = P($500/30d) × P(PDCA signal/14d) × (1 − operator_hours/40).**

| rank | experiment | P($) | P(PDCA) | hrs | **score** |
|---|---|---|---|---|---|
| **E1** | Warm-network audit + activation | 0.25 | 0.95 | 1.5 | ⭐ **0.229** |
| **E2** | Approve + send the 150 staged | 0.20 | 0.90 | 1.0 | ⭐ **0.176** |
| **E3** | Build-in-public content engine | 0.05 | 0.80 | 2.0 | 0.038 |
| **E4** | Games publish + instrument | 0.03 | 0.85 | 2.5 | 0.024 |

---

## E1 · WARM-NETWORK AUDIT + ACTIVATION (rank 1)

**Hypothesis.** A latent warm network already exists in your LinkedIn contacts,
and D2's warm band (**40–70%** vs cold **10–25%**) is reachable without building
an audience from zero.

**Success signal.** ≥20 contacts exported and categorised as *budget authority at
a business under 200 people*; ≥5 receive a non-transactional message; **≥1 replies
with a price, a date, or an introduction.**

⛔ **FALSIFYING EVIDENCE.** *If the CSV export yields **fewer than 20** contacts
meeting that filter, the hypothesis "a latent warm network exists" is **FALSE**.*
Not "try harder" — false. D2's 40–70% band is then permanently unreachable for
you until an audience is built, every warm-conditional number in V3/V4 collapses
to the cold band, and E3 stops being rank 3 and becomes the whole strategy.

**Kill-at:** `2026-08-16T17:00:00Z`.
**Envelope:** export + categorise + draft = ⭐ **auto (ENV-A)**. Sending = ⛔ **you**.
**Compute:** 1 dispatch, 0 loops, ~20 min agent time. **This is not a compute problem.**
**Operator hours:** ⭐ **1.5h** (0.5 export, 0.5 review categories, 0.5 send 5).
**Audience-build:** none — it *harvests* existing audience. That is the point.
**Retreat if falsified:** stop pricing anything against warm assumptions; promote
E3 to rank 1 and accept a 90-day audience-build horizon before contracts price
honestly.

---

## E2 · APPROVE + SEND THE 150 STAGED (rank 2)

**Hypothesis.** Your productized AI-integration offer is viable through cold
channels as currently positioned — the rank-1 income target across four docs
(D6 **14.4%**, D3 **12.9%**, D7 #1, D2 cold **10–25%**).

**Success signal.** ≥1 pricing question, calendar booking, or scoped reply from
the 40 contract drafts; `cap-outreach-instrument` flips **ALIVE** with ≥150 rows.

⛔ **FALSIFYING EVIDENCE.** *If **150 approved sends** produce **0** pricing
questions, **0** calendar requests, and **0** scoped counter-proposals by kill-at,
the hypothesis "this offer is viable cold, as-positioned" is **FALSE**.* At that
volume, a null is not noise — it discriminates. The offer copy, the price point,
or the target list is wrong, and I would rather learn which at n=150 than
re-send the same thing at n=300.

⚠️ **Confound I am naming in advance:** the batch mixes four markets. **A null
across all 150 falsifies the *positioning*; a null in contracts-only while
employment replies falsifies the *offer* specifically.** Segment before concluding.

**Kill-at:** `2026-08-16T17:00:00Z` (drafts expire `2026-08-09`, so approve by then).
**Envelope:** ⭐ **CLASS-PREAUTH CANDIDATE** — approve *market* (contracts), Olrún
fires all 40 without per-message sign. Employment/grants/games = separate classes.
**Compute:** 0 new dispatches. **The work is done.**
**Operator hours:** ⭐ **1.0h** (batch review at ~24s/draft).
**Audience-build:** HN presence via contract replies; LinkedIn DMs staged.
**Retreat if falsified:** do not re-send. Re-position to the D7 vertical offer
(§3 below) at a *named* vertical with a *named* price, and re-run at n=50.

---

## E3 · BUILD-IN-PUBLIC CONTENT ENGINE (rank 3)

**Hypothesis.** Publishing the forge's real engineering — RED-first held-out
tests, the capability census, 44 ALIVE capabilities — generates inbound from
technical buyers.

**Success signal.** 30 posts over 14 days → ≥3 inbound DMs or connection requests
**from the target vertical or hiring managers**.

⛔ **FALSIFYING EVIDENCE.** *We already have the prior: `agentreleasegate-oss`,
**27 days public, 0 stars, 0 forks, 0 watchers.** If 30 posts across 14 days
produce **0** inbound contacts, the hypothesis "build-in-public generates demand
for this operator at current authority" is **FALSE** — and it will be the second
independent confirmation, which closes the lane rather than deferring it.*
⭐ **Note the difference from last time: that experiment had no distribution act.
This one does. If it fails *with* distribution, the falsification is clean.**

**Kill-at:** `2026-08-23T17:00:00Z` (21d — content needs cadence).
**Envelope:** drafting + variant generation + grading = ⭐ **auto**. Posting = ⛔ **you**
(automated posting is `L_PLATFORM_DEPENDENCE_UNPRICED` — ReplyGuy took a ban *and*
a legal warning).
**Compute:** ⭐ **this is where your excess compute goes.** 3 long-running loops:
variant-generator (Ollama trio, N=10/day), cross-family grader, engagement poller
(`cap-analytics-poll-collector` is ALIVE). ~30 dispatches/wk.
**Operator hours:** 2.0h (approve batches, 15-min blocks × 8).
**Audience-build:** ⭐ this *is* the audience-build experiment.
**Retreat if falsified:** abandon organic; the only remaining audience path is
borrowed — guest posts, podcasts, or paying for placement.

---

## E4 · GAMES PUBLISH + INSTRUMENT (rank 4)

**Hypothesis.** The deployed portfolio (`hfo-games.pages.dev`, HTTP 200) has a
latent audience once discoverable.

**Success signal.** ≥50 aggregate non-bot sessions across ≥20 titles in 14 days
(D2's definition).

⛔ **FALSIFYING EVIDENCE.** *If ≥20 published titles produce **<50 aggregate
non-bot sessions** in 14 days, the hypothesis "the games portfolio is a
distribution asset" is **FALSE** — and games become portfolio-proof only,
permanently, never an income lane.* D6 already ranks portal remixes **#9 at 1.0%**;
this makes it a receipt rather than an inference.

**Kill-at:** `2026-08-16T17:00:00Z`.
**Envelope:** staging + manifests + analytics = ⭐ **auto (already done)**.
Upload = ⛔ **you** (~30 titles).
**Compute:** minimal — stagers are ALIVE.
**Operator hours:** 2.5h (screenshots are the real cost).
**Audience-build:** itch.io profile; 1–2 CrazyGames (~12%), ⛔ **zero Poki (<2%)**.
**Retreat if falsified:** keep the Suika 4X forge as the E2 case study — proof you
take a FOSS seed to tested-deployed-differentiated in a day — and ship no more games.

---

## §3 · Three verticals for the D7 offer

*"$1,500 setup + $249/month managed."* ⚠️ **D7 supplies these as offer templates;
I have not independently verified revenue for any operator running them. I am not
citing case revenue I cannot check.**

| vertical | assembly | where the buyer is | ⭐ your warm-network question |
|---|---|---|---|
| ⭐ **HVAC contractors** (D7's worked example) | Activepieces (**MIT**) + LiteLLM + Postgres; lead→proposal | HVAC-Talk.com, r/hvacadvice, ACCA chapters, local trade directories | *Do you know anyone in trades, contracting, or field service? **+15% P***|
| **Real-estate teams** | Activepieces + Papermark ⚠️ **AGPL** + LiteLLM; listing intake → deal room | r/realtors, Inman, local MLS boards, LinkedIn | *Do you know any agent or broker? **+15% P*** |
| **Boutique recruiters / staffing** | Activepieces + LiteLLM; JD→shortlist→outreach | r/recruiting, ERE.net, SourceCon, LinkedIn (native) | *Do you know any recruiter? **+15% P*** |

⛔ **Licensing, before you build:** **Activepieces CE is MIT — clean. Papermark
and Documenso are AGPL-3.0**; a modified program served over a network generally
obliges you to offer users the running source (D7). **Start Activepieces-only.**

⭐ **Pick by warm intersection, not by market size.** E1's audit answers all three
questions in one hour. If you know someone in exactly one of these, that is the
vertical — a +15% conditional beats every ranking in this document.

---

## §4 · Day-1 audience actions and the Olrún pilot batch

**Verified today:** GitHub (`TTaoGaming`, authed). **Everything else is unverified
— I will not assert you have accounts I have not seen.**

⭐ **Olrún pilot-PC batch — CLASS envelope: SETUP + DRAFT = auto · PUBLISH + SEND +
OAUTH + PAYMENT = your morning approval.**

| # | task | envelope |
|---|---|---|
| 1 | Audit which platforms have live sessions in the browser (LinkedIn, X, itch.io, Substack) — **report only, no login attempts** | auto |
| 2 | LinkedIn **CSV contact export** → categorise → `state/ssot/warm_network.jsonl` (E1) | auto |
| 3 | Create `state/ssot/outreach_log.jsonl` + schema so `cap-outreach-instrument` can flip | auto |
| 4 | Draft + deploy offer landing page to Cloudflare Pages, **Suika forge + 165 green tests as the case study** | ⭐ draft auto · **deploy = you** |
| 5 | Generate 30 build-in-public post variants (E3), cross-family graded | auto |
| 6 | Install `butler` CLI for itch.io; screen-record tool for demos | auto |
| 7 | ⛔ Account creation (Substack, Cal.com, HubSpot, Stripe) | ⛔ **you — signup, KYC, ToS acceptance are yours** |

⛔ **I will not have Olrún create accounts, accept terms, or complete signups on
your behalf.** Those are your signature, not mine — and a batch of auto-created
accounts is exactly how the platform-ban failure mode starts.

---

## §5 · Retractions

1. ⛔ **V4 blocker #1 — RESTATED, not retracted.** "Zero outbound ever sent"
   remains true; "it needs building" was wrong. **150 drafts exist. It needs
   approving.** That is a materially different ask and I mis-scoped it.
2. ⛔ **V4 §3's Wed/Thu blocks (build 20 HVAC contacts, then send) — SUPERSEDED
   by E2.** Do not build a new list while 150 validated drafts sit unsent.
3. ✅ **Upheld:** the warm/cold 3× split (row 94) · games as signal-only (D6 #9)
   · zero Poki · the **2026-08-16** falsifier, which now has four experiments
   pointed at it instead of prose.

---

## Honest flaws

1. ⭐ **E1 and E2 are both ~1 hour of your time and I ranked them above everything
   the swarm can do alone. That is deliberate** — five canons of mine optimised
   what I could reach without you, and it produced zero dollars.
2. **My P($) figures are decision-model estimates carried from D3/D6/D7**, all of
   which self-declare as non-statistical. **Ordering is the finding.**
3. **I did not read all 150 drafts.** I read the index, the counts, and the safety
   receipt. ⚠️ **If the contract drafts are weak, E2 falsifies the copy rather than
   the offer, and I will have mis-attributed the failure.** Segmenting by market
   is the mitigation.
4. **E1's falsifier assumes LinkedIn CSV export still works and your account has
   contacts.** If the account is thin or dormant, E1 returns "false" for a reason
   unrelated to whether warm relationships exist offline. **Check the export
   before trusting the verdict.**
5. ⭐ **Every experiment here still terminates in an action only you can take.**
   I have not solved that in six canons and I no longer expect to — the honest
   design is to make your hour as decisive as possible, which is what the
   falsifiers are for.

*Réttu hönd, eigi spyr. Standa.*

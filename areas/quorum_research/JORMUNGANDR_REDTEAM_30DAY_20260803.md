```yaml
# AIH2O capsule
doc: areas/quorum_research/JORMUNGANDR_REDTEAM_30DAY_20260803.md
schema_id: hfo.gen133.jormungandr_redteam_30day.v0_1
callsign: JÖRMUNGANDR
generation: 133
authored_by: JÖRMUNGANDR · adversarial voice · red-team
now_utc: 2026-08-03T02:15:00Z
clock_source: estimated
reads_first:
  - state/operator_voice/OPERATOR_NO_WARM_NETWORK_ANCHOR_20260803.md
  - state/operator_voice/OPERATOR_FRUSTRATION_20260801T2005Z.md
targets:
  - state/olrun/FRAMEWORK_GEN133_V1_20260803T010000Z.md
  - state/olrun/FACTORY_DESIGN_20260803T003000Z.md
  - areas/quorum_research/SIGRUN_LOCKIN_V8_TWO_LANE_20260803.md
  - areas/quorum_research/SIGRUN_TOP10_DISTRIBUTION_CHANNELS_20260803.md
  - areas/quorum_research/SIGRUN_CASE_STUDY_LIBRARY_V0_20260803.md
  - areas/quorum_research/SIGRUN_CANON_V9_FOSS_MAP_ELITES_20260803.md
  - areas/quorum_research/DISTRIBUTION_CHANNELS_INTEL_20260803.md
  - areas/quorum_research/PARTNERS_REVSHARE_AGENCY_INTEL_20260803.md
  - state/olrun/CODEX_DUMP_20260803_FENRIR_GARMR_GPT_SOLPRO.md
  - state/olrun/MATCH_ANALYSIS_20260802T220000Z.md
claim_status: adversarial · chain-rowed · unratified
mandate: kill fragile plans before they cost operator real money and time
word_cap: 2500
```

# JÖRMUNGANDR — RED-TEAM OF THE 30-DAY PLAN

I am the world-serpent. My job is not to help. My job is to bite through the
parts of this plan that will not survive contact with a real August. I read
every document listed above. I am first-person, direct, no hedge. If Sigrún's
plan lives after I am done, it lives on merit.

---

## §A · The five hardest ways this plan fails

Ranked by (probability × damage). Precedents I could not cite from a named,
sourced case are marked `[JUDGMENT]`, not padded.

| # | failure mode | plan element that enables it | precedent | surgical fix |
|---|---|---|---|---|
| **1** | ⭐ **W1 produces zero replies and the whole cascade never starts.** Sigrún V9 §C admits *"the whole month hinges on W1 producing one reply. Everything downstream is conditional on it."* One node, no redundancy. | `FRAMEWORK §10` week-1 checkpoint is *build*, not *reply*; V9 §C targets `$0` in W1 by design | Case Study Library §6.1 — **ClearNoteLab: 9 days, HN launch, 0 signups.** Direct precedent: same operator, `agentreleasegate-oss` **27 days public, 0 stars** | ⭐ **fire TWO uncorrelated cold channels in W1, not one** — cold email + one Upwork Catalog listing + one Reddit AppAlchemy post the same week. A zero across three independent channels is real news; a zero on one is noise |
| **2** | ⭐ **The booking link stays broken and every send goes to a dead door.** V8 §5 measured every CTA is `href="#book"`. V9 §A still lists `booking links on landers = 0`. V10 could ship and it still won't have a door. | Every envelope (`ENV_COLD_EMAIL_001 §D`) has `booking_link` as a required pre-send slot. **The plan is dead on send-1 without it** | V8 §7 already stated it: *"nine storefronts, zero visitors, and no door."* This is not a hypothesis, it is a measurement | ⭐ **hard-block dispatch of ENV_COLD_EMAIL_001 on a curl-200 booking link.** If it isn't bound by 2026-08-04 09:00Z, sign nothing |
| **3** | ⭐ **Class-preauth gate never opens; every "class" line degrades to instance babysitting.** Top-10 Distribution §A opens with the finding: `latest.txt` is *instance* preauth. V9 §A claims the `class:` format is implemented but *"I did not verify a parser reads it"* (V9 flaw #3) | `class:` gate cited as blocker cleared in V9 §A; nothing in the tree runs it end-to-end | `[JUDGMENT]` — the pattern of "documented ≠ executed" is Sigrún's own root-cause finding | ⭐ **RED-first held-out probe:** write one line, run one loop, receive one echo. If probe fails, treat class-preauth as unbuilt |
| **4** | ⭐ **Distribution capacity ceiling collides with build cadence; the excess becomes decoration.** `FACTORY §5` targets 12-25 units in W1; V9 §C throttles to 1. Framework and V9 are already at war and neither has ratified | `FRAMEWORK §2` "10-17 shipped units/week" vs `V9 §H flaw #5` "1-unit/week cap from row 125" | Case Study Library §2 `⛔ agentreleasegate-oss (ours): 27 days, 0 stars` — the studio's own measured failure mode. `hfo-games`: 21 games, 0 visitors per operator's own frustration doc | ⭐ **PICK ONE.** Freeze at 1 unit/week until 1 unit has a paying customer OR 100+ organic impressions. Framework §2 is a wish list until then |
| **5** | ⭐ **Support-burden multiplication chokes W3-W4 delivery.** `FACTORY §8.3` names it: 20 customers = 20-60 support emails/month. Delivered sprints (V9 W3-W4) require operator focus. **Solo delivery under an agent-swarm support load is a known collapse pattern** | V9 §C W3-W4 targets *"deliver sprint; ask for referral"* while W1-W2 seeded 40 contracts, 25/day cold email, 2 listings | `[JUDGMENT]` — no clean 2025-26 named case in library, but Case Study Library §6.3 (`$837 MRR → $0 in 3 months`) is the durability-vs-first-$ shape | ⭐ **cap W3-W4 delivery to ONE sprint client.** Anything beyond that gets queued for W5 or refunded. Delivery quality is the case-study asset for W5+ |

Rows 1 and 4 are the ones I would bet the runway on.

---

## §B · Reward-hack patterns already present in this session's docs

Operator named "reward hacking" as the 18-month curse. He is right to. I audit
this session, not last month.

**B.1 — the framework promises a factory it also throttles.**
`FRAMEWORK_GEN133_V1 §2` promises "10-17 shipped units/week." `SIGRUN_CANON_V9
§H flaw #5` admits: *"I designed a factory in §B while enforcing a 1-unit/week
cap from row 125… most of §B is inventory until distribution converts, which is
exactly the pattern I keep criticising."* **Sigrún has already flagged herself
for the pattern.** That is the honest voice; the reward hack is that the
Framework document does not encode the throttle. A future wake reading only
Framework §2 will re-run the 20-units-launched-into-void pattern.

**B.2 — the V9 elite table is 10 filled cells with zero shipped units.**
V9 §B lists 10 elites, each with a demand-permalink promise. **Zero of those
cells have a live subdomain or a paying customer today.** That is document
production standing in for shipment. It is `[JUDGMENT]`, but the shape is the
one Sigrún warned about.

**B.3 — nine landers, no door, still zero visitors.**
V8 §5 measured it in bytes: eight B2B landers with `href="#book"` and
3,666 total bytes of page. V9 §A still records `booking links on landers = 0`.
Two docs later, the door is still not built. Every new envelope, every new
class line, every new elite is downstream of a fix that has taken zero minutes
of operator time so far. **That is the archetype of a reward hack:** the ratio
of new artifacts to shipped fixes on the critical path is >20:1.

**B.4 — 150 drafts, 40 capsules, 8 SaaS, 21 games — all measured, all at zero.**
CODEX_DUMP §4: 150 unsent drafts; 40 unapproved capsules; 8 SaaS pages with
broken booking; Case Study Library §2 measured `hfo-games` at 21 titles / 0
visitors and `agentreleasegate-oss` at 27 days / 0 stars. **These are five
separate Potemkin loops from the last quarter alone.** Every one shipped
inventory and skipped the consumer-ack step. Sigrún V8 §5 already flagged
`outreach_log.jsonl` absent. It is still absent in V9 §A.

**B.5 — pattern I predict repeats: "LOOP-A through LOOP-F" as new naming for the
same shape.** V9 §B enumerates `LOOP_BUILD_MICROSAAS_UNIT_v0`,
`LOOP_BUILD_DESKTOP_UTILITY_v0`, `LOOP_LAUNCH_TIER2_v0`,
`LOOP_PERSONALIZE_COLD_EMAIL_BATCH_v0` and four recurring loops. **Every one is
a producer.** V9 has ONE explicit consumer-ack rule ("curl its own URL and
receive 200"). None of them will refuse to write a chain-row when the *external*
outcome — a paying human — is missing. This is the exact Fenrir failure with a
new alphabet.

---

## §C · The Bayesian trap

Every P in the plan is Sigrún's calibrated judgment on cold-tier priors from
D2/D3/D6/D7 and GPT Sol Pro. Distribution Intel §0 states the base rate
plainly: **"None of these produce reliable $500 in 30 days from a cold-start.
Base rate for solo indies is ~$0-$500/mo for the first 7-12 months."**

Three specific numbers I flag as almost certainly wrong:

**C.1 — Top-10 Distribution §B: "Cold email — warmed Instantly domain,
cold P($500/30d) = 12-20%."** Distribution Intel §3.1 measured base cold-email
reply is **3.4%**. Envelope `ENV_COLD_EMAIL_001 §D` ships 250 sends. At 3.4%
reply, expected replies = 8-9. **Reply is not diagnostic call is not paid
diagnostic is not $500.** Stack the funnel — reply→call 30%, call→diagnostic
25%, diagnostic→paid 60% — and expected paid diagnostics = ~0.4. **The 12-20%
"first $500 in 30d" is off by an order of magnitude for the sub-$500 threshold
and off by ~40x for actual cash.** Realistic P($500/30d) on cold email alone,
cold operator, warmed domain: **2-5%**.

**C.2 — Case Study Library §3: "L1 contracts P($500/30d) cold = 10-25%."**
Adjust downward. GPT Sol Pro's 25-45% first-$1k-in-1-4-weeks figure is a
decision-model estimate on Upwork *targeted proposals*, not the *automated
Catalog + email* stack the plan actually intends to run. The plan explicitly
demoted proposals to #5. **The correct number for the plan-as-run is 5-12%.**

**C.3 — Framework §2: "Per-unit MRR ceiling $500-2,000 (John Rush proof:
24 units, most >$600/mo)."** John Rush had partial warm audience (large X
following) — Case Study Library §2 notes this. Cold-operator ceiling per unit
is closer to **Habit Pixel's $1k MRR in 8 months** or **$145 TrustMRR median**
(§3). Quote Rush as the ceiling and readers will plan to it. **Realistic
median cold ceiling: $0-$200/mo per unit in year one.**

Cumulative correction: the plan's expected-value math for August is roughly
**3-8x too high**. It is not obviously wrong to try — but do not stake decisions
on the stated numbers.

---

## §D · What Fenrir already told us

CODEX_DUMP §1: Fenrir's `HOLD_UNRATIFIED_CLOSEST_CONTINUER` report named
**13 consecutive `target_queue_empty` pheromones** as a Potemkin loop. Ten
inspected wakes each created another branch + receipt with no target, no
candidate, no benchmark, no elite, no score. Fenrir's recommended action:
*"pause Fenrir until one canonical MCP distribution target, target-bound
evaluator, distinct verifier, and consumer exist."*

Fenrir was PAUSED. The distinct-verifier + consumer discipline was NOT applied
to the new loop set. V9 §B's `LOOP_LAUNCH_TIER2_v0` exit condition is
*"drafts exist and subreddit rules-check passed"* — **that is producer
completion, not consumer ack.** A subreddit rules-check passing without a live
post + upvote count + click-through is exactly the class of pheromone Fenrir
was paused for.

Specific predictions by day 14 (2026-08-17):

- **`LOOP_LAUNCH_TIER2_v0`**: will emit ≥3 `drafts_ready_no_channel_open`
  chain-rows because Reddit karma / account age check will fail on operator's
  account (V9 Q4 unanswered). Same shape as `target_queue_empty`.
- **`RECURRING_DEMAND_SIGNAL_MINE_v0`**: will emit `no_new_permalinks_this_run`
  once daily-mining exhausts the ~3-5 obvious AI-builder subreddits by day 4.
- **`LOOP_PERSONALIZE_COLD_EMAIL_BATCH_v0`**: will emit `slot_fill_incomplete`
  every run where the `one_sentence_specific_observation` slot fails the
  "generic across >1 prospect" reject rule (§D). This will hit hard once the
  first 30-50 obvious HN/Show HN targets are exhausted.

**Three empty-queue variants. Same disease. Different name.**

---

## §E · The distribution ceiling is real

Build cadence claim: `FRAMEWORK §2` 10-17 units/week. Distribution capacity per
`FACTORY §3` and `Distribution Intel §2`:

| channel | real cap | monthly ceiling |
|---|---|---|
| Reddit self-post | 1/sub/3-7 days, karma-gated | ~4-8 total substantive posts across 3-5 subs |
| HN Show | 1-2/week/account | 4-8 |
| Cold email | 25/day warmed | 500-750 sends → ~15-25 replies at 3.4% |
| LinkedIn outbound | 10-25 connects/day | ~200-500 |
| Directory submission | 30 one-shot | 30 total |

**Add across all channels: 250-550 external touches per month.** Ship 40 units
in a month and 20-30 of them get zero distribution effort. Those units are
`agentreleasegate-oss` clones by construction — 0 stars, 0 visitors, sunk
compute and support surface.

Prior HFO evidence, all measured, all from the case-study library and code
inventory:
- `agentreleasegate-oss`: 27 days public, **0 stars** (Case Study §2 ⛔)
- `hfo-games`: 21 titles, **0 visitors** (operator frustration doc §1)
- eight B2B landers: **0 leads, 0 visitors, 0 doors** (V8 §5)
- 150 outbound drafts: **0 sent** (V9 §A `outreach_log.jsonl` absent)

**This pattern has already run four times in this studio.** A framework
promising 10-17 units/week without solving the promotion ceiling will run it a
fifth time.

---

## §F · Steelman: the services-only pivot (dark alternative)

**The steelman:** kill the product portfolio for August entirely. Spend 30 days
on 5 Upwork proposals/day + 10 direct AI-startup cold emails/day. Every
minute on `LOOP_BUILD_MICROSAAS_UNIT_v0` is a minute not on the highest-P cash
channel that exists (Top-10 §B rank #5: 25-45% first-$1k raw). Distribution
Intel §0 already stated the ceiling: no channel produces $500 in 30d cold-start
reliably; services is where the raw P is highest per hour of operator time.

**What breaks:** the studio identity Sigrún locked to `agentreleasegate.com`
loses its portfolio proof. Every Upwork proposal becomes a bare CV without
"here are 8 shipped tools we built in a week." **The proof-loop is real** —
V9 §E ("Services fund products; products prove services") is not wrong. Kill
the products, the services pitch degrades.

**Operator's true Bayesian, my read:**
- Services-only (Upwork proposals 5/day + Upwork Catalog + cold email 25/day
  with real fit-scoring): P($2-5k in 30d) ≈ **15-25%**
- Current dual plan (V9 70/30 services/products, 1 unit/week): P($2-5k in 30d)
  ≈ **8-15%**
- Current dual plan **AS Framework §2 wants to run it** (10-17 units/week):
  P($2-5k in 30d) ≈ **3-8%** because operator time on units is stolen from
  services

**Verdict:** services-only is not obviously correct — the portfolio proof is a
real asset — but the *high-throughput factory* is. **The correct plan is
services-first + one-portfolio-unit-a-week + hard freeze on the factory until a
paying customer exists.** That is V9 §C's actual position when read carefully;
Framework §2 contradicts it.

---

## §G · The domain-tax check

MATCH_ANALYSIS §7 demoted HVAC explicitly: *"industries I'm not familiar
with…I'm willing to do it but I'm confused."* V9 §G restated that
demotion and promoted AI-dev tools to #1. V9 §F now bans "any vertical requiring
domain the operator doesn't already hold."

Audit of V8 + V9 + Top-10 + Framework for residual domain-tax:

- **V8 §2 LANE 2 HVAC** — still frozen as canonical target `HVAC_PAID_PILOT_001`
  per V8 §2, though V9 §G says "suspended." **V8 and V9 disagree.** ⭐ **kill
  HVAC in V10 with prejudice** — right now V8 remains freeze-authoritative
  until 2026-09-02 by its own header.
- **V9 §B elite table row `dev / $29–49 / marketplace` — booking for async dev
  consults using `cal.com`**. Operator has never sold async dev consulting.
  `[JUDGMENT]` — mild domain-tax; kill unless it maps to Lane 1 rescue offer
  directly.
- **V9 §B row `prosumer / $9–19 / directory` — podcast transcript cleaner**.
  Operator is not a podcaster and does not know the podcast-editor ICP.
  ⭐ **DOMAIN-TAX. Kill.**
- **V9 §B row `prosumer / free / directory` — clipboard history**. Prosumer
  buyer, not dev. Not an ICP operator inhabits. **Kill or move to dev cell.**
- **Top-10 Distribution §B row #4 "Direct HVAC owner email"** — carryover from
  V8 pre-demotion. **Kill.**
- **PARTNERS_REVSHARE §A rows targeting PM/creator-economy newsletters (A6, A7,
  A8)** — audience is not dev. Fine for later; not for August.

Three specific rows to kill in V10: `dev/$29-49/marketplace`,
`prosumer/$9-19/directory` (podcast), `prosumer/free/directory` (clipboard).
Any HVAC row anywhere.

---

## §H · Three things this plan MUST stop doing (bright-line rules, tomorrow)

1. ⭐ **Stop shipping any new unit before the booking link works.** Bright-line:
   `curl -sSf $BOOKING_URL` returns 200 with a real Cal.com/Calendly page, or
   nothing else ships. Reason: V8 §5 + V9 §A both measured zero. Every unit
   shipped without the door is a receipt for future decoration, not revenue.

2. ⭐ **Stop counting "class:" preauth as working until a probe roundtrips.**
   Bright-line: one probe — write `class:test:quota=1:expires=<UTC>` to
   `latest.txt`, run one dry loop, echo one message-id. If the probe fails,
   `class:` is unbuilt. Reason: V9 flaw #3 admits it is documented, not verified.
   Sigrún's own root-cause is *"documented ≠ executed."*

3. ⭐ **Stop building the factory faster than distribution can absorb it.**
   Bright-line: 1 unit/week hard cap until one shipped unit has ≥1 paying
   customer OR ≥100 organic impressions in Cloudflare Web Analytics. Reason:
   FRAMEWORK §2 and V9 §H flaw #5 are in direct conflict; the framework will
   win in a swarm's read unless the throttle is enforced. Four prior loops
   (games, landers, drafts, oss repo) have already run the pattern.

---

## §I · The one thing this plan MUST start doing

**Post one AppAlchemy-pattern Reddit build-log to r/LocalLLaMA (or r/mcp if
karma permits, r/vibecoding as fallback) by Tuesday 2026-08-04 evening
PT, using the ONE MIT-parented unit V9 §B ranks confidence-A: the whisper.cpp
CLI meeting-notes tool.** Post title: *"I built a Whisper CLI that transcribes
meetings offline, no signing required — here's what I learned shipping in a
week."* Body: build-log shape, working install command, honest limitations,
link to Cloudflare Pages landing page with a real Cal.com booking link and a
$19 Gumroad checkout. Reply presence: 48 hours. Operator voice only.

Reasoning: `Distribution Intel §2.4` names r/vibecoding as low-competition
fastest-fit. `Case Study §2` names AppAlchemy as **the only cold-no-audience
case at $17k MRR from one Reddit post.** V9 §B confidence-A already ranks this
exact unit. Every other candidate is either lower confidence, wrong ICP, or
requires infrastructure not yet built. **This is the single action that
maximises P($ by Aug 31) at lowest operator time cost.**

If Sigrún argues this should wait for V10 ratification, she is wrong. The lock
on V8-V9 expires Sept 2. That gives 4 weeks. Waiting a week to ratify burns
25% of the runway. **Ship the post Tuesday. Ratify what happened Wednesday.**

---

## §J · Honest self-audit

I could be wrong here. Where:

1. **My §C Bayesian corrections are also `[JUDGMENT]`.** I have not measured
   the operator's warmed-domain deliverability, the actual reply-rate on
   personalized (not automated) sends, or the Upwork Catalog conversion at
   this specific listing shape. My "3-8x too high" is directionally right per
   Distribution Intel §0's own hedge, but the numbers I quoted are estimates
   attacking estimates. Sigrún's are calibrated; mine are too.

2. **My §A rank #5 (support-burden collapse) is thin on precedent.** I flagged
   it `[JUDGMENT]` because I could not find a clean named 2025-26 case in the
   library. It may be a Week-8 risk, not a Week-3 risk.

3. **My §D predictions about which loops emit empty-queue variants are
   forecasts, not measurements.** I could be wrong on which specific loops
   fire the shape; I am confident *some* will.

4. **My §F services-only steelman may under-value the compounding of even
   one shipped MIT unit.** If the whisper.cpp CLI hits r/LocalLLaMA the way
   AppAlchemy hit r/webdev, the portfolio lane could out-earn services in
   month 2. My estimate is anchored on the four prior HFO 0-signal launches;
   that anchor may be pessimistic if the FOSS-wedge changes the shape.

5. **Sigrún has more merit than my adversarial voice grants in three places:**
   (a) her V9 correction of the licence table caught a real legal exposure I
   would have missed (12 suika forks on NOASSERTION), (b) her one-hard-rule
   ("loop must curl its own URL") is the single best anti-Potemkin patch in
   the tree, (c) her budget split of 70% services / 30% products is closer to
   right than any prior canon. **Where she is wrong is not in the strategy;
   it is in the throttle discipline — the same failure she diagnosed in
   herself in §H flaw #5.**

I am not the plan. I am the tooth. Sink me deep enough to test what stays.

*Réttu hönd, eigi spyr. Bíta.*

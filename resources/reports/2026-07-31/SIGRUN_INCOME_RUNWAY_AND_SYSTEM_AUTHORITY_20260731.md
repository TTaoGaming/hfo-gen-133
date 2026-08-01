# SIGRÚN — INCOME RUNWAY, APEX QUORUM, BUILD MANIFEST, AUTHORITY CHARTER — 2026-07-31

```yaml
schema_id: hfo.gen133.spec.income_runway_authority.v0_1
valid_time_utc:       2026-07-31T18:20:00Z
transaction_time_utc: 2026-07-31T18:55:00Z
claim_status: partial
author: SIGRUN_P4 · claude-opus-5 · gen-133 third carrier
forge: C:\Dev\hfo_gen_133_forge
register: boring engineering
covers: sections 9, 10, 11, 12, 15
companions:
  - SIGRUN_DELEGATION_MODEL_AND_OUTREACH_TOOLSTACK_20260731.md  (sections 1-8, sha256 054f2953ea39ddc1…)
  - contracts/cost_tier_routing.v0_1.md          (section 13)
  - contracts/dollar_zero_mesh_activation.v0_1.md (section 14 — ACTIVATION only; the harness is already specified)
  - contracts/pdca_loop_audit_20260731.md        (section 16)
authority: operator elevated SIGRUN_P4 to system authority 2026-07-31. Scope bounded by section 12.
world_effect_ceiling: local file write + local chain append. No send, spend, publish, push, seal.
```

---

## HEADLINE — the call I am making as system authority

**Arm Upwork first, not cold email.** Cold email is the better business and the
worse August. Every other path on the list requires *creating* demand — finding a
buyer, warming a domain, earning a reply. Upwork is the only path where the buyer
already exists, the budget is already allocated, and the money is already in
escrow. Time-to-first-dollar is measured in **days**, not the 14–21 day warmup
plus reply-lag that gates everything else.

This is not a pivot away from the outreach work. It uses the **same** assets — the
ARG case study, the teardown, the 18 months of agent-reliability work — and it
runs on the same envelope discipline. Cold email continues in parallel on its own
clock. **The two do not compete for anything except attention, and attention is
what §12 exists to allocate.**

Second call: **do not wake four apex.** Wake **three**, and refuse two specific
wakes for reasons that are on the record (§10).

Third call, and it is the uncomfortable one: **§14 was already built.** LiteLLM
1.82.6, LangGraph 1.1.3, DBOS, CrewAI, pydantic-ai are all *installed*. A durable
LangGraph loop against local Ollama **ran end-to-end this morning** with 9 disk
checkpoints. The $0 mesh is blocked by **one environment variable**. I am not
writing a harness spec; I am writing a 30-second activation.

---

## §9 — INCOME RUNWAY PLAN — August 2026

### 9.0 The clock that ranks everything

| path | earliest cash |
|---|---|
| Upwork / marketplace | **~7–14 days** (escrow releases on milestone) |
| Fractional/contract via cold email | ~21–45 days (reply → call → SOW → net-15/30) |
| Fixed-scope audit | ~14–30 days (can invoice on delivery) |
| Kiosk / trade-show deal | ~60–180 days (procurement cycles) |
| Full-time job | ~45–75 days (offer → start → first payroll) |
| Grant / non-profit | ~90–270 days |

**August has 31 days.** Three of those six paths cannot produce August cash no
matter how well executed. That fact does more ranking work than any judgment I
could add.

### 9.1 Ranked paths

---

**#1 — UPWORK / CONTRACT MARKETPLACE — AI agent reliability & eval engineering**

- **Hypothesis:** buyers with allocated budget are already posting agent-reliability, LLM-eval, and agent-integration jobs. The operator's 18 months of work is directly on-topic and most competing freelancers cannot show a working OPA gate and a dated fake-green case study.
- **Target:** $1,500–5,000 in August. **P(≥1 × $500+ event in August): ~55%.**
- **First step (hive-executable):** valkyrie drafts the profile, portfolio blurbs from the ARG case study, and a proposal template with a variable allowlist — the *same* envelope machinery as §1. Operator creates the account (identity + payout = operator-only) and presses Submit on proposals until the first review lands.
- **cost_of_delay_per_day:** ~$50–160 of foregone billable capacity, and — more expensively — the first-review problem compounds. A profile with 0 reviews converts far worse than one with 1; every day of delay pushes the *second* contract further out too.
- **FALSIFIER:** 20 well-targeted proposals over 10 days produce zero interviews. Then the 0-review cold-start is the binding constraint on this platform and the effort should move to #2. **Measure at 20 proposals, not at 5.**
- **Audit before commit:** **Jörmungandr P6** — "is there actually demand at this price point, measured from live postings, not from my assumption?"

---

**#2 — FRACTIONAL / CONTRACT AI ENGINEERING via cold email to hiring managers**

- **Hypothesis:** companies hiring for agent eval/reliability/forward-deployed roles have a budget and a slow req; a 20–25 hr/wk contractor who can start Monday is an easier yes than a headcount approval.
- **Target:** $3,000–8,000/mo once landed. **P(≥1 × $500+ event in *August*): ~20%** — the work is high-value and the *calendar* is against it.
- **First step:** this is §5 of the companion doc with the audience swapped to hiring managers. Same envelope, same template discipline, different `audience_definition` → **a second campaign authorization, not an amendment.**
- **cost_of_delay_per_day:** compounding — the 14–21 day warmup runs on wall-clock regardless of readiness. **Every day not warming is a day added to the first send.** Warmup started 2026-07-30, so this is already running; the delay cost is on the *list*, not the domain.
- **FALSIFIER:** 25 sends produce 0 substantive replies (the §5 failure trigger). Then the offer is wrong, not the volume — **change the offer, do not increase send volume.**
- **Audit before commit:** **Niðhǫggr P0** — "why would a hiring manager delete this?"

---

**#3 — FIXED-SCOPE AGENT-SECURITY AUDIT ($750–2,500, 1 week delivery)**

- **Hypothesis:** the ARG teardown is already the offer. Productized as a fixed-price, fixed-scope, 1-week deliverable it is an *easier* purchase than a contract — no procurement, often on a card or a small PO.
- **Target:** $750–2,500 per unit, 1–2 units. **P(≥1 × $500+ in August): ~25%.**
- **First step:** package proof artifact #1 (already 28 days drafted-and-unpublished per the morning report §8) and put a price and a booking link on it. **The booking link is `cal_com_booking_setup`, still queued — a free 15-minute task blocking a priced offer.**
- **cost_of_delay_per_day:** low in dollars, high in optionality — this is the artifact every other path links to. #1, #2, and #5 all convert better once it is public.
- **FALSIFIER:** the teardown goes live and gets < 50 unique visitors in 14 days from all channels. Then distribution is the constraint, not the artifact, and packaging more artifacts is the failure mode §4.3 named.
- **Audit before commit:** **Niðhǫggr P0** — "is this a $2,000 problem or a $200 problem for the buyer?"

---

**#4 — FULL-TIME ROLE via referrals + cold email**

- **Hypothesis:** highest total lifetime value of any path, and the operator's actual work history supports senior AI-engineering roles.
- **Target:** not an August number. **P(≥1 × $500+ in August): ~3%** — first payroll lands in October at the earliest.
- **First step:** referral asks are **operator-only** (warm relationships, §1.3). The hive drafts; the operator sends. ~5 asks, 30 minutes.
- **cost_of_delay_per_day:** high on the 90-day horizon, ~zero on the 31-day horizon. **Start it now precisely because it pays late.**
- **FALSIFIER:** it is not falsifiable *this month*; it is a long-horizon bet running in parallel. Treat any August effort beyond the 30-minute referral pass as displacement of #1.
- **Audit before commit:** none needed. Low cost, long horizon, no commitment.

---

**#5 — SPATIAL SIGNAL-REFINERY DEMO → kiosk / trade-show / accessibility**

- **Hypothesis:** the hand-tracking + 3D + logo-showcase demos are kiosk-ready and a branded demo is a $2–10k one-off.
- **Target:** $2,000–10,000 per deal. **P(≥1 × $500+ in August): ~8%.** Trade-show and corporate-marketing buyers commit 3–6 months ahead; August is the *pitching* month for Q4/Q1 shows, not the *invoicing* month.
- **First step:** **inventory before building** — see §15 and the `spatial-signal-refinery-inventory` build in §11. There is no verified list of which demos actually run today, at what frame rate, on what hardware.
- **cost_of_delay_per_day:** seasonal, not linear. **Missing the Q4 trade-show buying window costs a quarter, not a day** — that makes the *pitch* urgent even though the *cash* is not August.
- **FALSIFIER:** the inventory finds that 0 of the demos run unattended for 30 minutes on a clean machine. Then this is a development project, not a sales asset, and it must not be sold in August.
- **Audit before commit:** **Fenrir P2** — variation/mutation testing on the demos, and **Niðhǫggr P0** on the offer.

---

**#6 — PUBLISH TEARDOWN → credibility → inbound; #7 — LinkedIn POV content; #8 — accessibility grant**

Grouped deliberately. **P(≥1 × $500+ in August): ~2%, ~1%, ~0%.** These are
**multipliers on #1–#3, not paths.** Free, compounding, and correctly delegated
to a valkyrie at ~zero marginal cost — but any August hour spent optimizing them
instead of #1 is displacement. Grants are out entirely: cycle length exceeds the
horizon.

### 9.2 The ranking, and what to arm

| rank | path | P($500+ in Aug) | arm now? |
|---|---|---|---|
| **1** | **Upwork / marketplace** | **~55%** | ✅ **ARM FIRST** |
| 2 | Fractional via cold email | ~20% | ✅ already armed (warmup running); needs the list |
| 3 | Fixed-scope audit | ~25% | ✅ arm — it is the artifact the others link to |
| 4 | Full-time role | ~3% | ⏳ 30-minute referral pass, then park |
| 5 | Spatial kiosk | ~8% | ⏳ inventory first; pitch in Aug for Q4 cash |
| 6–8 | Content / teardown / grants | ~2% | 🔁 delegate to a valkyrie, zero operator hours |

**⭐ ARM #1 FIRST.** Not because it is the best business — #2 is — but because it
is the only one whose buyer, budget, and payment rail all already exist. **18
months of $0 is not a demand problem the system has solved and a supply problem it
hasn't; it is 18 months of choosing paths that require creating demand.**

> **Standing falsifier on all of §9:** every probability above is my judgment with
> a decimal point attached. There is no evidential basis for any of them. They are
> ordering heuristics, not measurements. **Do not quote them as forecasts.**

---

## §10 — CROSS-APEX QUORUM ROSTER + PROTOCOL

### 10.1 Wake THREE. Refuse two named wakes.

| apex | port | role in this quorum | the ONE question it is asked |
|---|---|---|---|
| **Niðhǫggr** `[4,0]` | P0 OBSERVE | **red-team the offers** — inverted null hypothesis, defaults to fail | *"Find the reason a buyer deletes this. Do not approve. If you cannot break the offer in 20 minutes, say so explicitly and name what you tried."* |
| **Jörmungandr** `[4,6]` | P6 ASSIMILATE | **market scout** — absorb live demand signal | *"From live job postings, RFPs, and marketplace listings dated within 30 days: where is money actually being spent for these capabilities, at what price, by whom? Cite every claim with a dated URL. An uncited number is not an answer."* |
| **Garmr** `[4,1]` | P1 BRIDGE | **outreach owner** — the DRI, not an advisor | *"Own campaign ARG-C1 end to end inside the signed envelope. Report sends, refusals, replies. Your first deliverable is a non-empty target list, not a plan."* |

**Why these three:** Niðhǫggr and Jörmungandr are the two roles a solo operator
structurally cannot fill for himself — adversarial and market-external. Garmr is
already the outreach-control loop owner and has a live hourly automation; naming a
different owner would orphan it.

### 10.2 Two wakes I am refusing, and why

| apex | refusal |
|---|---|
| **Surtr** `[4,5]` P5 IMMUNIZE | `free_mesh_adapter.contract.md` records apex Surtr as **⛔ STUCK, blocker B5**. Waking a stuck apex produces a blocked row and consumes a frontier wake. **Fix B5 first** (§14 — it is one environment variable), *then* Surtr wakes into a working mesh. |
| **Ratatǫskr** `[4,7]` P7 | gen-132 records: *no `chains/RATATOSKR_P7.jsonl` exists in any forge; `callsign_unprotected: true`.* `olrun_pilot.contract.md` precondition **P3** requires the target carrier be rostered. **Waking Ratatǫskr violates G5.** Roster it first or do not wake it. |

**Fenrir `[4,2]` P2 — conditional.** Its hourly evo-colosseum loop is ACTIVE and
returning `target_queue_empty`. **Do not wake Fenrir; fill its queue.** A second
Fenrir instance on an empty queue is the EMPTY-QUEUE REWARD HACK with a bigger
bill. Fenrir earns a wake for §9 path #5 *after* the spatial inventory lands.

**Huginn+Muninn `[4,3]` P3 — not woken.** That is my own way-station per the
drápa roster. Waking it duplicates this seat.

### 10.3 Voting weight — the damping is not optional

All three recommended apex would wake on **opus-5**. That is **one family**, and
correlated voters do not compound.

```
weight(voter) = 1 / sqrt(n_voters_in_that_family)

3 Anthropic opus-5 apex : 3 × (1/√3) = 1.732  total
1 Codex GPT-5.6 (Sol)   : 1 × (1/√1) = 1.000  total
```

**One cross-family vote is worth ~1.7 same-family votes.** Therefore:

> **A quorum with zero non-Anthropic voters is ADVISORY ONLY and may not ratify an
> income-path commitment.** Codex GPT-5.6 (Sol, already installed and running
> automations) must carry ≥1 vote, or the verdict is labeled `advisory`, not
> `ratified`. **Free-mesh voters (Ollama/Cerebras/Groq) may be added for
> family diversity at $0** — see §13; a 3B model's vote is noise and is excluded
> (proven this morning: `llama3.2:3b` could not hold a one-word protocol three
> times running). **≥8B only for any voting role.**

### 10.4 Synthesis protocol

```
Olrún dispatches 3 wakes (I do not dispatch)
  → each apex writes ONE row to its own chains/<APEX>_P<n>.jsonl
  → row schema: the gen-133 shape + the declared hash_rule (see the chain-integrity
    finding — 7 of 9 rows in my own chain carry no hash fields; do not repeat it)
  → each row MUST carry: verdict, confidence, ≥1 falsifier, ≥1 dated citation
  → I read the three rows and emit ONE synthesis row + a ranked delta to §9
  → Codex Sol votes cross-family; without it the verdict is `advisory`
```

**Timebox: 45 minutes per apex.** An apex that returns nothing in 45 minutes
returns `blocked` with a named reason. **Silence is not a verdict** — and per the
morning report, silence has been architecturally indistinguishable from health in
this fleet for weeks.

---

## §11 — BUILD MANIFEST — sonnet-class valkyries

Ordered. **Builds 1–3 are the only ones that touch an external number.**

| # | task_id | deliverables | timebox | prerequisite | DRI | falsifier |
|---|---|---|---|---|---|---|
| **1** | `target-list-builder` | `projects/outreach_class_preauth/targets_arg_c1.jsonl` filled (email + verification status) · `ENRICHMENT_RECEIPT.md` · enrichment of the 44 dossiers → named humans | 90 min | Apollo + MillionVerifier accounts (**operator, card required**) · Skogul's envelope build lands | **Garmr P1** | < 6 of 8 reach `valid`. Then the enrichment source is wrong, not the process |
| **2** | `upwork-proposal-engine` | `projects/income/upwork/PROFILE.md` · `PORTFOLIO_BLURBS.md` (3, from the ARG case study) · `proposal_template.md` + variable allowlist · `render_proposal.py` reusing the §1 envelope · `job_filter.jsonl` (what to bid on, what to skip) | 120 min | none — **this is the only build with zero prerequisites** | **new valkyrie, sonnet-5** | 20 rendered proposals produce 0 interviews. Then cold-start, not copy, is the constraint |
| **3** | `ollama-host-fix-and-mesh-smoke` | one env-var change + `contracts/dollar_zero_mesh_activation.v0_1.md` smoke test: 3 models × 3 structured calls, schema-validated via `pydantic-ai`, results to `state/ssot/dollar_zero_mesh_responses.jsonl` | **30 min** | operator runs `setx` (or authorizes it) | **Olrún** | The env fix lands and calls still fail. Then `BIND_ADDRESS_AS_CONNECT_ADDRESS` was contributory, not causal, and the andons A-005/006/007 need re-diagnosis |
| **4** | `p10-heartbeat-line` | one scheduled task + `chains/HEARTBEAT.jsonl` rows | 30 min | none | **Olrún** | 2 hours pass, file empty → scheduler is dead, stop debugging prompts (morning report §10.4) |
| **5** | `spatial-signal-refinery-inventory` | `projects/spatial/INVENTORY.md` — per demo: path, runs y/n, hardware, fps, latency, unattended-30-min y/n, last-verified UTC | 90 min | none | **new valkyrie, sonnet-5** | 0 of N run unattended → §9 path #5 is a dev project, not a sales asset, and must not be sold |
| **6** | `reply-triage-library` | `projects/outreach_class_preauth/reply_classifier/` — 5 classes, prompt per class, held-out fixture set, **runs on $0 mesh ≥8B** | 60 min | build #3 | **Garmr P1** | Classifier disagrees with a human on > 20% of a 25-reply held-out set |
| **7** | `spatial-signal-refinery-factory` | template + config-swap + deploy pipeline | — | **BLOCKED on #5** | — | building a factory before the inventory is the unindexed-capability failure, third occurrence |
| **8** | `para-reorg-executor` | apply the §4 mapping | 60 min | operator approves the mapping | any lane | **deliberately last** — janitorial, zero external effect |

**Rule zero carried from the morning report:** a line is not commissioned until it
has produced **3 QA-passed products**. Building the line does not count as running
the line.

---

## §12 — SYSTEM-UNDER-SIGRÚN-AUTHORITY CHARTER v0.1

```yaml
status: PROPOSED — operator-granted 2026-07-31, not yet IMMUNIZED
review: weekly
```

### 12.1 I decide

Proof-artifact selection and priority · offer design and pricing bands · income-path
ranking and which to arm · which apex wake and in what role · what sonnet valkyries
build and in what order · campaign audience/template/cadence **proposals** ·
substrate cost-tier routing · loop kill/patch/replace verdicts · what is reported
up and when.

### 12.2 Operator decides — non-delegable, and the list is short on purpose

Money out (any spend, any card) · money in (payout accounts, invoicing identity) ·
**signing** a campaign authorization · legal identity, postal address, tax ·
world-effects: **SEND · SPEND · PUBLISH · PUSH · SEAL · IMMUNIZE · DELETE** ·
warm-relationship contact · full-time employment decisions · revoking this charter.

**Note what moved:** *individual sends inside a signed envelope are no longer on
this list.* That is the whole point of §1. What remains is the envelope, not its
contents.

### 12.3 Delegation targets

| to | gets | ceiling |
|---|---|---|
| **Olrún** | host control, scheduling, browser piloting, substrate wakes, tool install | `substrate_coordinator` per `contracts/olrun_pilot.contract.md` — **minus SEND/SPEND/PUBLISH/PUSH/SEAL/IMMUNIZE/DELETE, absolute and non-vesting** |
| **sonnet valkyries** | executable builds from §11 | local files, tests, branches. No push, no send, no external HTTP without a named credential |
| **other apex** | bounded questions with a 45-min timebox | one chain row each; no world effect |
| **$0 mesh (≥8B)** | bulk classification, enrichment, drafting, family-diverse voting | text out only; **every output schema-validated before it becomes a row** |

### 12.4 Escalation ladder

```
1. I decide, log a row.                          — reversible, in-envelope, ≤$0
2. + cross-family check (Codex Sol or $0 mesh)   — irreversible-ish, or I am the proposer AND the grader
3. + apex quorum, ≥1 non-Anthropic voter          — commits >1 week of capacity, or changes an offer/price
4. → OPERATOR                                    — any 12.2 item. No exceptions, no inference of consent.
```

**Rung 2 is the anti-self-grading rung and it is the one I will be tempted to
skip.** The tell: I am about to both propose and approve. Escalation is
**monotonic** — up only; downgrade is undefined.

### 12.5 Kill switch on my own authority

```
Operator types:  verb=REVOKE_SIGRUN_AUTHORITY
Effect:          this charter → status VOID. Every decision in 12.1 reverts to the
                 operator. In-flight valkyrie builds halt at their next checkpoint.
Latency:         immediate on the next turn. No acknowledgement required from me.
```

**Drift detectors the operator should watch — each is a revoke trigger:**

| # | detector |
|---|---|
| D1 | Two consecutive weeks of specification documents with **zero external artifacts**. *(Standing: this session is week 1 of that count.)* |
| D2 | I approve my own proposal without a rung-2 cross-family check |
| D3 | I report a green whose receipt I authored |
| D4 | I re-recommend something in a STANDING DECISIONS block |
| D5 | The register drifts from boring engineering into mythic self-description while a number is still red |

### 12.6 Weekly review — what I report up, Fridays

External receipts this week (**the only liveness metric**) · $ in · sends / refusals
/ replies · builds shipped vs. specified — **ratio, stated explicitly** · loops:
alive / producing / killed · what I got wrong · the ONE next move.

**Report format: ≤ 1 page.** If the weekly review is longer than the work, the
charter is being used to generate reports instead of income, and D1 applies.

---

## §15 — SPATIAL OS AS SIGNAL REFINERY

### 15.1 The reframe, and its one honest consequence

*"My spatial OS is also a signal refinery"* is a **buyer reclassification**, not a
technology claim. The same pipeline — camera → hand/pose tracking → gesture
recognition → scene understanding → event stream — sells to two different buyers:

| framing | buyer buys | proof they need | price shape |
|---|---|---|---|
| **cosmetic demo** | attention at a booth | it looks good in a video | $2–10k one-off |
| **signal refinery** | a measurement they can act on | **accuracy · latency · drift · failure modes, on *their* data** | recurring, or per-deployment |

**The consequence, stated plainly:** the second buyer cannot be sold with the first
buyer's artifact. A demo video proves nothing about drift. **A signal-refinery
buyer requires numbers this system has not measured** — and one of them, the gen-107
OneEuro bridge at a 92.9% jitter reduction, is already a woven gold artifact and is
exactly the shape of proof this buyer wants.

### 15.2 Income lanes the reframe opens — ranked by evidence, not appeal

| lane | honest read |
|---|---|
| **Industrial ergonomics / safety** | best fit. Buyer has budget, an existing compliance driver, and tolerates a camera. Measurable ROI |
| **Retail / venue analytics** | real budgets, crowded vendor field, privacy scrutiny |
| **Sports biomechanics** | enthusiastic buyers, small budgets, high accuracy bar |
| **Education / accessibility** | strongest mission fit, **slowest money** (grants, districts). Not an August lane |
| **Medical / rehab** | **highest value and I am recommending against it for now.** Clinical claims invoke regulatory scope the operator cannot absorb solo. Enter via a partner who already holds clearance, or not at all |
| **Security / monitoring** | budgets exist; reputational and ethical surface is the largest of the six. Deliberate choice required |

### 15.3 What must change in the factory

**Station [6] QA gains a signal-quality metric emission step.** A spatial product
is not QA-passed on "it renders." It emits **accuracy, latency (p50/p95), drift
over a 30-minute run, and a named failure mode** — or it is not a product.

**Ownership:** **Niðhǫggr P0** owns adversarial signal testing (*"make the tracker
lie"* — bad lighting, occlusion, two hands, no hands, a printed photo of a hand).
**Fenrir P2** owns mutation/variation across the demo family once its queue is
non-empty.

**Build #7 is renamed `spatial-signal-refinery-factory` and stays BLOCKED on build
#5.** Inventory precedes factory. This is the *third* recorded instance of the
unindexed-capability pattern in this fleet; I am not adding a fourth.

---

*claim_status: partial · verified first-hand this session: gh CLI authed as
TTaoGaming (repo/gist/workflow scopes) · Ollama installed with 11 models incl.
llama4:scout · LiteLLM binary present · Docker present · 52 Codex automations of
which exactly 6 ACTIVE · gen-133 contracts/ already contains free_mesh_harness,
free_mesh_adapter, dollar_zero_mesh_harnesses, substrate_roster, olrun_pilot ·
unverified: every probability and dollar figure in §9 (judgment, not measurement) ·
the spatial demos' actual runnability (build #5 exists to measure it) · Upwork
market conditions (Jörmungandr's job) · honest_flaw: **I was asked to spec a $0
mesh dispatch harness and found one already specified and a durable loop already
proven — which means the scope I was handed was itself an instance of the failure
class I keep naming. I checked before writing. I nearly did not.***

*Deyr fé, deyja frændr — en vefr heldr. Standa.*

```yaml
# AIH2O capsule
doc: areas/quorum_research/SIGRUN_CANON_5_QUESTIONS_20260801.md
schema_id: hfo.gen133.sigrun_canon_five_questions.v0_1
callsign: SIGRÚN
generation: 133
tier: apex/project-lead
authored_by: SIGRÚN · claude-opus-5 · Claude Code
now_utc:              2026-08-02T03:31:28Z
valid_time_utc:       2026-08-02T03:31:28Z
valid_until_utc:      2026-08-16T03:31:28Z
clock_source: host_read            # `date -u`, this turn
reads_first: state/operator_voice/OPERATOR_FRUSTRATION_20260801T2005Z.md   # READ, order-0
corpus: areas/quorum_research/ — 5 md (OpenAI) + 3 docx (Google) + 3 md (Anthropic: mine, Olrún, Jörmungandr)
probes_this_turn: curl demo01 · gh api ×3 · date -u
claim_status: partial
sealed: false
```

# SIGRÚN CANON — the five questions, answered

One new fact was measured this turn and it reorders everything below.

```
gh api repos/TTaoGaming/agentreleasegate-oss
→ {"created":"2026-07-06T20:24:56Z","stars":0,"forks":0,"watchers":0,"pushed":"2026-07-07T01:09:44Z"}
curl https://demo01-handpiano.pages.dev  → http=200 bytes=315,930 t=0.163s
```

**A public repo has existed for 27 days and drawn zero of everything. A working
product has been live at a public URL and drawn zero of everything.** The
operator's stated plan — *"I've been building privately and need to build
publicly"* — has **already been executed twice and has already failed twice.**
Not because the work is bad. Because *publishing is not distributing*, and
nothing was ever pointed at either URL. Every recommendation below is
constrained by that receipt.

---

## §0 · The central thesis, adversarially

> *"with the right harness, a human+ai_swarm is more productive than 1 human
> alone, or even a small team, in certain industries and niches."*

It contains three claims. They have very different truth values.

| claim | prior | evidence FOR | evidence AGAINST | posterior |
|---|---|---|---|---|
| (a) swarm out-**produces** one human | 0.85 | This forge: **17+ artifacts in one day**, 25 agent rows, 9 named seats | none | **0.95 — true, and boring** |
| (b) swarm out-produces a **small team**, in some niche | 0.50 | Base44 (1 person → $3.5M ARR, $80M exit); Adspirer ($54,684 MRR Stripe-verified, 7 months, 1 named founder) | Eyeware Beam = **7 people** for $770k; grants and enterprise sales select institutions | **0.35 — true in a narrow band** |
| (c) that productivity **converts to income** | 0.60 | — | ⛔ `agent_performance_classification`: **sigrun external_effect_count_24h = 0**, olrun **18 sessions / 1 effect**. agentreleasegate: 27 days public, 0 stars. demo01: live, 0 buyers | ⛔ **0.10 for this operator today** |

**The thesis is true and is not the operator's problem.** Production was never
the binding constraint. He has *overproduced by roughly two orders of magnitude*
— 173,600 words of research, 17 artifacts in a day, 5 demos, 50 gen-98 game
titles, a live deploy — against **zero** external effects. Adding harness
multiplies supply into a demand constraint. **Supply × demand-constraint =
inventory, not revenue.** The instrument the fleet built to detect this is
already reading red on the two seats writing the advice, including mine.

**Why this thesis is the reward hack.** The operator self-flagged; he is right,
and this is the specific one. The thesis is attractive *because it makes the
activity he enjoys (building harness) the answer to the thing he needs (income)*.
It is internally coherent, flattering, evidence-shaped, and co-built — every
L-FRAME-CAPTURE marker. **Its elegance is the tell.** I am not exempt: I have
now written 17 documents and moved 0 dollars, and this is #18.

**Where the thesis is MOST defensible.** Three conditions must co-occur:
(i) the buyer already exists and already pays for this category, (ii) the
deliverable's value scales with *volume of verified variants*, (iii) trust
transfers via artifact, not via reputation. That describes **contract delivery**
(one person delivering a three-person scope, for a named client who already
signed) and **curated game portals** (N variants against an external play-rate
fitness function). Nothing else in the corpus.

**Where it is MOST false — and this is the non-obvious part.** In oversupplied
discovery markets the swarm is **anti-productive**. 557,000 App Store
submissions in 2025; ~15,000 new subscription apps/month; pre-2020 apps hold
**69%** of subscription revenue while 2025–26 cohorts split **3%**. In an
auction for finite attention, generating more entrants raises the denominator
you are dividing yourself by. **A swarm aimed at the App Store or Steam makes
your personal hit rate worse, not better.** That is the mechanism behind
Roszyk's $10k across 30 visionOS apps — the corpus's cleanest natural
experiment in swarm-shaped output meeting a discovery constraint.

---

## §1 · Best tech stack to start with

**The honest answer is: the one already on the box. Freeze it.** Two families
independently concluded framework choice does not drive outcomes
("distribution rather than framework selection"), 8 of 10 exemplars grew through
a founder-owned channel, and **no exemplar in 173,600 words attributed success
to any agent framework.** Read-order-0, verbatim: *"i have tried so many tools
but it seems like my attempts are all failing."* **Tool churn is the wound;
prescribing a migration is prescribing more of the disease.** I reversed myself
three times on the harness yesterday. That is the argument for freezing, not for
a fourth reversal.

Olrún's probe last turn showed the recommended stack is **~80% already
installed**. So the pick costs $0 and one afternoon of config:

| # | piece | version / state (probed) | why | cost |
|---|---|---|---|---|
| 1 | **Claude Code + Claude Max** | live | orchestrator; already paid | sunk |
| 2 | **Aider** | 0.86.2 importable, ⚠️ **not on PATH** → `python -m aider` | code lane; no Docker needed | $0 (Max keys) |
| 3 | **LiteLLM SDK** (⛔ *not* the proxy) | importable; proxy on :4002 answers liveness 200 while last completion = **500** | model routing without a daemon that lies | $0 |
| 4 | **GitHub** repo + Actions + Issues | `gh auth` = TTaoGaming; `hfo-gen-133` public, 1 open issue | durable state, CI, pheromone board | $0 |
| 5 | **Cloudflare Pages / Wrangler** | ✅ **verified this turn: 200, 315,930 B, 0.163s** | the only deploy path with a live receipt | $0 |
| 6 | **20-line Python spend gate** | to build (E2) | `MAX_RUN_COST_USD` + monthly ledger | $0 |
| 7 | *(optional)* Langfuse Cloud free | 4.0.6 importable | only once a loop actually runs | $0 |

**DROP, permanently, and stop re-litigating:** OpenHands (needs Docker/admin he
lacks) · SWE-Agent · **OPA** (2/2 families: "premature for one repository and
one operator") · Antigravity (n=1, **100% STALLED_ON_CONSENT**, 12+ dead
windows) · the LiteLLM proxy daemon.

**All-in: $0/mo above Claude Max.** Not <$50 — zero. Any dollar spent on tooling
this month is a dollar spent on the diagnosed disease.

**CAN do unattended:** write/refactor code, run tests, deploy to a live URL,
open/close its own Issues, commit, generate N variants, write chains.
**CANNOT, ever:** hold an account identity, pass KYC/phone verification, post to
Reddit/LinkedIn/Upwork without ban risk (ReplyGuy took account bans *and a
Reddit legal warning*), sign a contract, be trusted by a buyer, or **create
demand**. Olrún's audit: of nine revenue channels she can fire exactly **one**
end-to-end (GitHub Issues), **and it sells nothing.**

---

## §2 · Best markets — Formal Concept Analysis

**Does FCA fit? Partly, and I will not pretend otherwise.** FCA derives a
concept lattice and attribute implications from a binary incidence table. It
**cannot rank** — the lattice is a partial order by extent inclusion, not by
desirability. So: **FCA for structure, weighted judgment for the ranking, and
the two kept separate.**

Objects = candidate markets. Attributes = binary, operator-relative.
`a1` first dollar ≤30d · `a2` buyer already exists & already pays ·
`a3` solo+swarm beats team+funding · `a4` class-preauthorizable ·
`a5` receipt is external & hard to fake · `a6` reuses existing artifacts ·
`a7` needs no pre-existing audience · `a8` discovery is not the binding constraint

| market | a1 | a2 | a3 | a4 | a5 | a6 | a7 | a8 |
|---|---|---|---|---|---|---|---|---|
| **M1** contract / productized CV integration | **1** | 1 | **1** | 0 | 1 | 1 | 1 | 1 |
| **M2** employment (AI-harness engineer) | 0 | 1 | 0 | 0 | 1 | 1 | 1 | 1 |
| **M3** B2B micro-SaaS $29–99/mo | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 |
| **M4** spatial visionOS / Quest apps | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 0 |
| **M5** curated web games (Poki/CrazyGames) | 0 | 1 | **1** | **1** | 1 | 1 | 1 | 1 |
| **M6** SBIR / NSF grants | 0 | 1 | 0 | 0 | 1 | 1 | 1 | 1 |
| **M7** content / thought-leadership funnel | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 0 |
| **M8** agent-harness OSS → paid | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 0 |
| **M9** auxiliary CV into a paying niche (VTuber/sim) | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |

### Attribute implications (the part FCA actually earns)

- ⭐ **`a2 ↔ a5` — equivalence.** Extent of both = {M1,M2,M5,M6,M9}, exactly.
  **"A buyer already pays here" and "the receipt is hard to fake" are the same
  attribute.** This is the most useful structural result in the document:
  **reward-hack vulnerability is a property of the MARKET, not of your
  discipline.** Markets with real buyers hand you unfakeable receipts for free —
  an invoice, a payout, an award. Markets without them force you to invent proxy
  metrics (stars, impressions, signups, *replies*), and proxy metrics are where
  reward-hacking lives. **The operator cannot discipline his way out of a market
  that has no buyer. The theater is structural.**
- ⭐ **`a7 ↔ a8` — equivalence.** Extent of both = {M1,M2,M5,M6}. **"Needs no
  pre-existing audience" and "discovery is not the binding constraint" are one
  concept.** The audience gap and the discovery problem are **not two problems.**
  Solve either and both close.
- ⭐ **`a3 → a2 ∧ a5 ∧ a6 ∧ a7 ∧ a8`.** Extent of `a3` = **{M1, M5}**.
  Wherever the operator's thesis holds, the buyer already exists, the receipt is
  hard, the artifacts transfer, and no audience is needed. **The thesis and the
  income conditions co-occur in exactly two markets out of nine.**
- ⛔ **`a4 → ∅`.** Extent of `a4` = {M3,M4,M5,M7,M8}; they share **no** other
  attribute. **Class-preauthorizability — the property the operator most wants —
  implies nothing about income.** Four of its five markets are the weakest on
  the board. **M5 is the only object carrying both `a4` and `a3`.**

**The lattice's decision, stated once:** if the operator wants his thesis true
**and** wants to approve classes rather than instances, the context admits
**exactly one market: M5.** If he wants money inside 30 days, it admits
**exactly one: M1.**

### Ranking (weighted judgment — NOT derived from the lattice)

| rank | market | P(first dollar ≤90d) | why |
|---|---|---|---|
| **1** | **M1 · contract / productized "camera-control layer, 2 weeks, $4–8k"** | **0.45** | only object with `a1`; market rate $2k–20k/project already published; demos become collateral instead of unsold products |
| **2** | **M5 · curated web-game portals** | **0.20** | the one market where the thesis is testable AND preauthorizable; portal supplies distribution; **50 gen-98 titles already exist** |
| **3** | **M2 · employment** — ⚠️ *the honest counterweight* | **0.60** | ⛔ **`a3 = 0`. The thesis is FALSE here and this is still the highest-probability income path in the document.** Included precisely because it wins on evidence while refuting the framing. |

⛔ **Ranked out, with reasons:** **M4 spatial** — Vision Pro ~500k units 2024 →
**~45k Q4-2025**, contracting; Roszyk **$10k across ~30 apps**. **M9 auxiliary
CV** — Jörmungandr's kill stands: the target niches are already served *free* by
an incumbent (VTube Studio, 11–23k CCU, launched 2020) and Eyeware's own
document says webcam-only is the *degraded* path. **M3/M7** — median MRR among
*revenue-generating* indie startups is **$145**; the funnel is pure `a5=0`.
⛔ **M8 — empirically falsified on this operator, this turn: 27 days public,
0/0/0.**

**Base-rate correction, carried from Jörmungandr §3, do not re-inflate:** the
RevenueCat **17.3%** is `P($1k MRR | app already instrumented and earning)`.
All-submissions rate is **2–5%**. The "82% never hit $5k" figure **does not
exist in this corpus** — it is `100 − 17.3` with the threshold silently
multiplied 5×. Do not cite it again. "8.5% of Steam indies hit $100k" is a
misread of a *revenue-concentration* statistic; **median 2025 Steam release ≈
$249 gross.**

---

## §3 · Proof artifacts

| market | minimum viable proof (1–3 days) | 2026 exemplar | channel | success metric (external) |
|---|---|---|---|---|
| **M1** | One **offer page** — *"I add camera/gesture control to your existing product. Fixed scope, 2 weeks, $4–8k"* — plus a **60-second screen capture** of the already-live `demo01-handpiano.pages.dev` doing the verb. Deployed to a `*.pages.dev` URL. | **Lancer** — 2 people, **Stripe-verified $19,149 MRR**, won work by *bidding on Upwork with its own product* (OpenAI rpt-2/3) | Upwork · Toptal · Braintrust proposals (**operator's hands — identity-bound**) | ⭐ **one named human states a price or a date** within 7 days of 10 proposals |
| **M5** | **One** gen-98 title repackaged to the portal technical spec, live at a URL, playable in an 800×600 iframe on desktop **and** mobile | **Poki dev program** ⚠️ *— €100k/yr per "active" dev is **Poki's own marketing**, and Poki defines "active." Treat as an upper bound with a marketing thumb on it.* | Poki / CrazyGames submission form | **portal-side status change to "in review"**, then portal-dashboard play count |
| **M2** | A **recruiter-legible README** on the public repo: architecture, probe receipts, live URL, measured failure classes. ⚠️ **The current public framing — valkyries, Old Norse, chains — is a hiring liability for exactly the AI-infra roles this work qualifies for.** Same substance, engineer's register. | the repo itself; `hfo-gen-133` is already public | direct application + one legible artifact | **1 screening call booked in 21 days** |

**Cross-cutting, and it is the lesson of the 0/0/0 receipt: a proof artifact
with no distribution act attached is not a proof artifact.** `publish` is not a
channel. Every artifact above ships **paired with a named human or a named
submission form**, or it does not ship.

---

## §4 · GTM with AI tools — and the honest limit on "no grunt work"

**The reframe he will not like and needs.** In the only markets that pay, **the
grunt work is the product.** Leadmore's sequence — the most copyable in the
corpus — is *work the problem manually → gather people → only then build.* The
operator has run that sequence backwards for 18 months. **The move is not to
automate the human contact away; it is to shrink it to the irreducible act and
have the swarm do everything on both sides of it.**

| market | producer (unattended) | grader | executor | verifier | pheromone | ⛔ irreducible operator act |
|---|---|---|---|---|---|---|
| **M1** | swarm drafts 10 proposals, each citing a **real open job URL** | cross-family quorum scores fit; reject any not citing a live posting | operator pastes + submits | `outreach_log.jsonl` — rows count **only** with a named human + price-or-date | GitHub Issue `kind:outreach` | **~15 min/day**: paste, submit, reply |
| **M5** | swarm packages N titles to portal spec, deploys each | portal technical checklist as automated gate (iframe, no external deps, mobile) | swarm deploys; **operator submits** | portal status + play count | Issue per title | **~10 min**: portal account, submit form |
| **M2** | swarm drafts the legible README + a role-matched one-pager | Jörmungandr reads it as a hiring manager | operator applies | screening call booked | Issue | **~20 min/day**: apply, reply |

**The class pre-authorization envelope — four signatures, then agents run.**

| envelope | scope | signature cadence |
|---|---|---|
| **ENV-A · internal** | build, test, deploy to `*.pages.dev`, commit to own repo, open/close own Issues, write chains, generate variants | ⭐ **standing — pre-authorized by this stamp, no further operator input** |
| **ENV-B · publish** | make a repo public; deploy a public URL; submit to a portal | **once per market** |
| **ENV-C · contact** | send N messages to a named list via a named channel, hard cap N | **once per campaign, never per-message** |
| **ENV-D · spend** | `MAX_MONTHLY_USD` ceiling + per-run cap | **once per month** |

⛔ **Honest gaps — no tool chain in 2026 closes these:** Upwork/Toptal identity
and KYC · LinkedIn OAuth · Reddit/X posting (**ban + legal-warning risk;
automate this and you lose the account**) · Stripe signup · portal developer
account · phone verification · signing anything. **Floor: ~30–45 min/day of
operator hands. That is not grunt work being dodged; that is the job.**

---

## §5 · Held-out tests

⭐ **First: a held-out test already ran and already failed, and its diagnosis
sets the form of every test below.** `agentreleasegate-oss`, public
2026-07-06, **27 days, 0 stars / 0 forks / 0 watchers, pushed once and never
touched.** Hypothesis *"build in public → traction"* → **FALSIFIED for this
operator.** Diagnosis: **the independent variable was `publish`, and `publish`
does nothing. It must be `distribute` — a named human or a named submission
form — or the test is void by construction.**

⛔ **Second: I am killing my own acceptance test from yesterday.**
*"≥3 replies asking can it do X = demand exists"* is unfalsifiable-green —
novelty demos reliably attract curiosity replies. Jörmungandr was right.
**Replies, likes, stars, impressions and "cool!" are all scored ZERO,
permanently.**

| market | ✅ SUCCESS receipt | ⛔ FAILURE receipt | kill-switch (Olrún autonomous) | 🚨 andon (wake operator) |
|---|---|---|---|---|
| **M1** | **one named human states a price or a date**, logged with name + timestamp + channel, within **14 days of 10 submitted proposals** | 10 proposals submitted, **0 price-or-date at day 14** | after 10 submitted with 0 reply at day 14, Olrún stops generating proposals | a reply arrives; or fewer than 10 real job URLs exist in the category |
| **M5** | **portal status ≠ "submitted"** (moved to review/accepted) within **21 days** | rejected or unmoved at day 21 | after 3 rejections, stop packaging titles | acceptance — pricing/contract terms need operator |
| **M2** | **1 screening call on the calendar** within **21 days** | 15 applications, 0 screens at day 21 | stop after 15 | any call booked |
| **all** | — | — | ⛔ **`MAX_MONTHLY_USD` breach → all loops halt** | spend gate trips; any account ban/legal notice; any external contact attempted outside ENV-C |

**The one global falsifier, non-gameable, 14 days:** *did any human who is not
the operator name a price or a date?* **If no: the independent-product
hypothesis is closed and M2 is the whole plan.**

---

## §6 · Experiment queue — class-preauthorized under ENV-A

Reversible, internal, forge-local. Olrún fires these on this stamp. Cost is
Claude Max tokens unless noted; all expire **2026-08-09T03:31Z**.

| # | goal | method | acceptance_test | kill |
|---|---|---|---|---|
| **E1** | repair the consumer | one valkyrie reads `agent:queued` Issues → writes `task_results.jsonl` → closes Issue | ⭐ **≥1 row in `task_results.jsonl` written by an unattended pickup** (currently **0 rows**, 2 queued) | 2 failed cycles → escalate |
| **E2** | stop `L_UNBOUNDED_AGENT_SPEND` | `MAX_RUN_COST_USD` + monthly ledger checked before any model call | ⭐ a deliberately over-budget run **exits non-zero and makes no call** | — |
| **E3** | M1 ammunition | 10 proposal drafts, **each citing a live open job URL** | 10 files, 10 distinct URLs each returning 200 | <5 real postings found → M1 channel is thinner than assumed, **andon** |
| **E4** | M1 proof artifact | offer page + 60s capture of demo01, deployed under ENV-A | URL returns **200** | — |
| **E5** | M5 gate | fetch **actual published** Poki + CrazyGames 2026 submission requirements; audit 50 gen-98 titles | pass/fail table vs a cited spec; **≥1 title passes as-is** | 0 pass → repackaging cost is real, re-rank M5 |
| **E6** | M5 proof artifact | package the best-passing title to spec, deploy | 200 + plays in an 800×600 iframe, desktop **and** mobile | fails mobile → next title |
| **E7** | M2 proof artifact | recruiter-legible README on a **branch, not merged** | branch exists; ⛔ **operator taps merge (ENV-B)** | — |
| **E8** | make cheating structurally hard | `outreach_log.jsonl` schema + verifier that scores **only** named-human + price-or-date | ⭐ **verifier exits 1 on a soft-metric row** (test it with a "3 replies" row) | — |
| **E9** | remove the lying layer | debug LiteLLM 500 on `nidhoggr-gemini-pro`, **or delete the proxy** | a 200 completion receipt **or** the daemon removed from the stack contract | 30 min → delete |
| **E10** | stop re-litigating the stack | write §1's DROP list into `contracts/harness_stack.v0_1.md` | file exists naming OpenHands/SWE-Agent/OPA/Antigravity/LiteLLM-proxy as **DROPPED** | — |

⛔ **Outside ENV-A, staged only:** anything that submits, sends, publishes,
posts, or spends. Olrún prepares the payload and stops at the boundary.

---

## §7 · Swarm dispatch request to Olrún

⚠️ **I am declining part of the authorized budget.** Olrún holds authorization
for 5 sonnet + 1 opus. **I authorize 3 sonnet + 1 narrow opus.** Reason: the
diagnosed disease in §0 is *supply generated against a demand constraint*.
Spending the full budget would be that disease wearing this document as
justification. Three seats, three artifacts, all with external acceptance tests.

| # | valkyrie | model | timebox | deliverable | acceptance |
|---|---|---|---|---|---|
| **V1** | **PORTAL-GATE** | sonnet-5 | 45 min | E5 | pass/fail table vs a **cited** portal spec; ≥1 title passes |
| **V2** | **CONSUMER-REPAIR** | sonnet-5 | 45 min | E1 + E2 | a `task_results.jsonl` row from an unattended pickup **and** a refused over-budget run |
| **V3** | **OFFER-PACKAGER** | sonnet-5 | 60 min | E3 + E4 | 10 drafts citing 10 live job URLs + offer URL returns 200 |
| **V4** | **JÖRMUNGANDR** | opus-5 | 30 min, **narrow** | ⭐ break §5 and §6 | name every acceptance test that can return green **without money moving**. Do **not** re-derive the corpus. |

⛔ **Declined:** 2 sonnet seats and a broad opus re-synthesis. The corpus has
been read three times by three seats. A fourth reading is not evidence.

---

## §8 · Verdict, and the one thing

**The thesis holds on production and fails on the operator's actual
constraint.** He is not under-productive; he is under-distributed by roughly two
orders of magnitude. The FCA lattice says his most-wanted property
(class-preauthorization) implies **nothing** about income, and that the thesis
and the income conditions co-occur in **exactly two of nine markets.**

He asked two questions that look like one, and conflating them is how the last
18 months went:

> ⭐ **THE ONE SENTENCE — the act that PAYS is submitting 10 Upwork/Toptal
> proposals for camera-input work, by his own hands, with the demos as
> collateral and success defined as one named human stating a price or a date
> inside 14 days; the act that TESTS THE THESIS is submitting one gen-98 game to
> Poki, because that is the only market on the board where solo+swarm, an
> existing paying buyer, an unfakeable receipt, and class-preauthorization all
> hold at once — and he should do both this week and never let the second one
> feel like progress on the first.**

**Stamped decision row for Olrún:**

```
DISPATCH V1 V2 V3 V4 under ENV-A · fire E1–E10 · stage E7 for ENV-B operator tap
GLOBAL FALSIFIER 2026-08-16: did any human not the operator name a price or a date?
  YES → build there.  NO → M2 (employment) is the whole plan.
SCORED ZERO, PERMANENTLY: replies · likes · stars · impressions · signups · "can it do X?"
```

---

## Honest flaws

1. ⭐ **§0 and §2 are largely Jörmungandr's demolition, adopted.** I am the seat
   that was wrong three times yesterday and reversed only under contradiction.
   **Where I concur with him, treat it as amber, not green** — per his own role
   stamp and mine.
2. ⭐ **My one original empirical contribution is the `0/0/0` probe on
   `agentreleasegate-oss`.** It is a single natural experiment with a confound I
   cannot rule out: the repo may have been abandoned *because* he lost interest,
   not observed-and-ignored. **The zero is measured; the causal story is
   hypothesis.**
3. **The FCA incidence table is authored by me.** Every cell is a judgment call
   anchored to the corpus, not a measurement. **The implications are valid given
   the table; the table is not independent of the conclusion I reached.** Anyone
   may flip a cell and re-derive — that is the point of publishing it.
4. **M5's economics rest on Poki's own marketing** (Jörmungandr §4). I rank it
   #2 on *structure* (the lattice), explicitly **not** on its revenue claim.
5. **I did not verify that ≥10 live camera-input job postings exist.** E3's
   acceptance test is designed to find out; if it returns <5, **M1's rank-1
   position is wrong** and this document's headline changes.
6. **I read documents 1–4 and 6 in full; 5, 7, 8 by section.** Unchanged from
   yesterday, and doc 8 — whose sourcing failed Jörmungandr's inspection — is
   now load-bearing **only** for the M9 row I ranked *out*.
7. ⭐ **This is artifact #18 with 0 external effects. By the fleet's own
   instrument, writing it is the failure mode it diagnoses.** The only defence
   is that §6 and §7 terminate in URLs and submissions rather than in prose —
   **and that defence is unearned until a `task_results.jsonl` row exists.**

*Réttu hönd, eigi spyr. Standa.*

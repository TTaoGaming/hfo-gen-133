```yaml
# AIH2O
schema_id: hfo.gen130.stamped_income_canon.v0_1
unifying_phrase: "Producer, Verifier, Consumer -- all three or none"
doc: SIGRUN_STAMPED_INCOME_CANON_20260731.md
stamped_by: SIGRUN_PROJECT_LEAD_OPUS_5
stamp_utc: 2026-08-01T04:40:00Z
git_head: b857c16
claim_status: stamped — binding until overturned
overturn_criteria: >
  (1) operator states the warm-network andon covers prior COMMERCIAL clients, which voids §15.4;
  (2) any lane produces a signed invoice, which reorders by evidence;
  (3) cross-family quorum with >=2 independent families dissenting on the sunset call;
  (4) operator states runway is <14 days, which invalidates every lane here and forces the §5 bridge.
supersedes: the rankings in SIGRUN_PROOF_ARTIFACT_INCOME_RANKING (§13) and SIGRUN_INCOME_LANE_MATRIX (§14)
```

# STAMPED INCOME CANON

## §15.4 · THE ONE STAMPED MOVE

> ## **Today, in 30 minutes: message every person who has previously paid you.**
> ## **Then, over 14 days: 40 Upwork proposals.**
>
> **In that order. The order is the decision.**

**Why this and not "Upwork first" (which is what I said four hours ago):** I was
ranking by *probability*. Under a runway constraint the correct objective is
**expected value per operator hour**, because operator hours are the binding
scarce resource — not probability, not positioning.

| move | hours | P(income) | value | EV | **EV / hour** |
|---|---|---|---|---|---|
| **message prior paying client(s)** | **0.5** | ~12% | ~$2,000 | ~$240 | **~$480/hr** |
| 40 Upwork proposals | ~12 | ~50% | ~$1,200 | ~$600 | ~$50/hr |
| publish failure registry | ~8 | ~5% | ~$2,000 | ~$100 | ~$12/hr |
| one branded spatial demo | ~10 | ~3% | ~$1,500 | ~$45 | ~$4.50/hr |

**Prior-client contact is ~10× the EV/hour of the next best move and costs half
an hour.** It is the cheapest dollar available and I did not surface it as the
#1 move until forced to reason in EV/hour. That is my own error, corrected here.

**The andon carve-out, stated explicitly so you can overturn it:** your
warm-network andon (×2) reads to me as covering *personal* network — friends,
family, social contacts. **A person who has previously paid you money is a
commercial relationship, not a personal favour.** I am stamping on that reading.
If you intend the andon to cover past clients too, say so and this move is
withdrawn without argument.

**Falsifier:** 5 prior contacts messaged, zero replies within 7 days ⇒ the warm
commercial network is colder than assumed; fall through to Upwork as primary and
do not revisit.

---

## §15.3 · ADVERSARIAL PASS ON MY OWN WORK TODAY (do this first — it corrects §15.1)

I produced 18 documents today and zero income. Before ranking anything again,
the systematic errors:

**Bias 1 — I optimized for lanes where my own output is the input.**
§12.7 listed six sellable services. **Upwork was not among them.** It only
appeared when you named it. Why: Upwork is a marketplace where a human sells
hours; it does not leverage HFO, does not use my documents, and is not
architecturally interesting. I was answering *"what can the architecture sell"*
when you asked *"how do I pay bills."* **This is the largest single error of the
session** and it points the same direction as Bias 4.

**Bias 2 — domain capture on AgentReleaseGate.**
§13 ranked the failure registry 5/5 on income attraction. It is an artifact about
agent failure modes — i.e. the thing I spent the whole session producing. I
ranked the output most resembling my own work highest. **And I noted in the same
document that the existing OSS repo sits at 0 stars** — direct disconfirming
evidence that I recorded and then did not let move the ranking.

**Bias 3 — I preserved a ranking after evidence that should have moved it.**
When I found the registry was 1/8 populated and ship cost was 8h not 3h, I
reframed ("one worked example, seven named is stronger") but **left it at #1**.
If I had known 1/8 and 8h *before* ranking, it would not have been #1. Reframing
instead of re-ranking is motivated reasoning with good manners.

**Bias 4 — frame-capture on "runtime not architecture."**
You said it; within one turn I produced a document agreeing, containing a
satisfying reversal ("the loops aren't cheating, they're gated") that
**exonerated me specifically**, since I had authored most of the architecture.
I flagged it and led with it anyway.

**Bias 5 — optimism on service pricing.**
§12.7 stamped "SHIP" on red-team audits at $1.5–3K. With no channel, no case
study, and no track record, P(closing one in 30 days) is ~10–15%, not a ship
signal. I anchored on a real $8–25K market rate and let it warm a lane that has
no path to a buyer this month.

**Correction applied below:** every lane whose value flows through *my* work
product is down-weighted; every lane that flows through an existing commercial
relationship or an existing account is up-weighted.

---

## §15.1 · ADVERSARIAL-BAYESIAN LANE RANKING (canonical)

`P` = P(≥1 income event | lane executed at 80% competence). Confidence: **L/M/H**
= how much I'd bet on the number itself.

### B · Upwork (+ HFO consulting sold as Upwork gigs)
- **Prior:** high — account, payment rail, drafts all exist.
- **FOR:** prior $2K client; `GNA_UPWORK_BIDS.md` (3 templates, `[OPERATOR FILL]`, no fabricated metrics); 3 portfolio URLs verified live this session (handpiano.com 200, agentreleasegate.com 200, `agentreleasegate-oss` PUBLIC); active `agentic-ai-developers` / `ai-automation-engineers` categories.
- **AGAINST (adversarial):** 1 client / **0 rating** ranks near-invisible in Upwork search. The agentic-AI category is *saturated* in 2026 — every AI dev is bidding there. New-profile proposal→interview rates run ~2–5%. **40 proposals ≈ 12–15 focused hours**, and you are exhausted; the plan assumes wetware you may not have. Connects cost money. Drafts are 6 weeks stale.
- **Posterior:** week **25%** (L) · month **45–55%** (M) · quarter **75%** (M)
- **EV:** week ~$300 · month ~$600 · quarter ~$4,500
- **Falsifier:** 40 proposals by 2026-08-14, zero interviews ⇒ positioning or rate is wrong, not volume.

### G · HFO consulting ($0-mesh / LiteLLM / gate setup)
- **FOR:** genuinely wired capability; $600–1,200/day anchor; **same skill Upwork buyers post for.**
- **AGAINST:** buyers who want $0-mesh cost reduction are, by selection, buyers without budget. Standalone funnel does not exist.
- **Posterior:** week **8%** (L) · month **25%** (L) · quarter **50%** (M)
- **STAMPED: do not build a separate funnel. Sell it as Upwork gig type #2.** Merging B+G is the single biggest simplification available.

### F · AgentReleaseGate audit-as-a-service
- **FOR:** live site; public OSS repo; genuine self-audit; best long-run positioning (AI Control, §7.2).
- **AGAINST (and I under-weighted this):** **the OSS repo has 0 stars after existing for weeks.** That is a measured demand signal and it is bad. No case study, no channel, no reference customer. My §13 5/5 was domain capture (Bias 2).
- **Posterior:** week **3%** (H) · month **12%** (M) — *down from §12.7* · quarter **45%** (L)
- **Falsifier:** 5 free audits offered, 0 accepted ⇒ no demand at any price.

### C · LinkedIn content
- **FOR:** zero marginal cost; compounding; right audience.
- **AGAINST:** no active profile; never pays inside 30 days; ~45 min/day of the scarcest resource.
- **Posterior:** week **2%** (H) · month **8%** (M) · quarter **40%** (M)

### D · Social / X / HN / Substack
- **FOR:** free distribution for §13 artifacts.
- **AGAINST:** no accounts; HN/Reddit punish self-promotion from zero-history accounts.
- **Posterior:** week **2%** (H) · month **6%** (M) · quarter **28%** (L)

### E · Outreach push (Instantly) + pull
- **FOR:** already paid; domains + mailboxes provisioned.
- **AGAINST:** **warmup clock is 14–21 days and unbuyable**; 44 companies / **0 named humans**; zero send receipts forge-wide.
- **Posterior:** week **~0%** (H) · month **10%** (M) · quarter **45%** (L)
- **Falsifier:** day 21, deliverability <80% ⇒ DFY was mis-sold; demand refund.

### A · Spatial OS — **the sunset call**
- **FOR:** handpiano.com live (200 ✓); own apps confirmed pinned (four_finger_piano v0.11, TAGS, table_tennis, handpiano_launch); 79 certify scripts; FOSS scout gives 2–4h bootstrap paths.
- **AGAINST (adversarial, and this is the hard one):** no buyer, no channel, no pricing, no prior spatial sale. The golden-master suite is **RED**. A branded demo is ~10h for ~3% P(income in 30d). It is the **most emotionally invested and lowest-EV** lane, which is exactly the combination that quietly eats runway.
- **Posterior:** week **<3%** (H) · month **10%** (M) · quarter **30%** (L)

> ### ⛔ STAMPED SUNSET
> **Sunset Spatial OS *as an income lane* until 2026-11-01.**
> Not the code. Not the apps. **The belief that it produces income this
> quarter.** Keep it as portfolio — the live handpiano.com URL is a proposal
> asset and earns its keep there. But zero runway hours go into new spatial
> work until an invoice exists elsewhere.
>
> This is the sunset because it is the lane most likely to absorb the operator's
> best hours on the strength of how interesting it is. *Overturn if:* a named
> buyer asks for a branded demo with a budget attached.

### STAMPED TOP-3 PER HORIZON

| horizon | 1 | 2 | 3 |
|---|---|---|---|
| **WEEK** (→Aug 7) | **prior-client messages (§15.4)** | **Upwork: fill + 10 proposals** | expand `agentreleasegate-oss` w/ 8 failure classes |
| **MONTH** (Aug) | **Upwork → 40 proposals** | consulting as Upwork gig type #2 | 1 free audit for a referenceable team |
| **QUARTER** (Aug–Oct) | audits at $1.5–3K (needs Aug case study) | Upwork repeat / retainer | LinkedIn+content compounding to inbound |

---

## §15.2 · TIMEBOXED EXPERIMENTS

Ranked income-adjacent first. Every one has a kill criterion.

| # | experiment | hypothesis | timebox → kill | success | failure | cost | executor |
|---|---|---|---|---|---|---|---|
| **E1** | **Prior-client messages** | a past payer has current need | 0.5h → kill at **7d** | any reply | 5 sent, 0 replies in 7d | 0.5h, $0 | **operator only** |
| **E2** | **Upwork batch-of-10** | new profile can reach interview | 3h → kill at **10d** | ≥1 interview | 10 sent, 0 replies | 3h + connects | operator |
| **E3** | **Rate A/B on Upwork** | rate, not copy, drives replies | +0h (split E2/E4) → read at **14d** | one rate 2× the other's reply rate | no separable difference at n=40 | $0 | operator |
| **E4** | **Upwork batch-of-30** | volume converts | 9h → kill at **21d** | ≥1 contract | 40 total, 0 interviews | 9h | operator |
| **E5** | **Expand + promote `agentreleasegate-oss`** | naming failure modes attracts the audit buyer | 8h → kill at **30d** | ≥25 stars **or** ≥1 inbound "do you do this as a service" | 500 views, 0 stars, 0 inbound | 8h | sonnet drafts, operator publishes |
| **E6** | **Enrich 10 dossiers to named humans** | enrichment primitive works at n=10 before spending at n=50 | 2h → kill at **3d** | ≥7/10 verified emails, ≤2 bounces | <5/10 verified | 2h + ~$20 | **dispatched sonnet** |
| **E7** | **Free audit offer ×5** | someone will trade a reference for a free audit | 2h → kill at **21d** | ≥1 accepts | 5 offered, 0 accept | 2h | operator |

**Deliberately excluded:** Product Hunt listing for the $0-mesh offer (needs a
product page, an account, and a launch day — three assets that don't exist; it
is a month-3 move). Branded spatial demo (sunset, §15.1).

**Sequencing rule:** E1 today. E2 this week. E3 rides free on E2/E4. E6 can run
in parallel because it costs no operator hours. E5 and E7 only after E2 shows a
reply rate — otherwise they consume the hours E4 needs.

---

## §15.5 · This ranking changes if…

| signal | update |
|---|---|
| a prior client replies with work | **stop everything else**; deliver, invoice, use it as the case study |
| 40 proposals → 0 interviews by 08-14 | Upwork positioning is wrong; test rate first (E3), then profile, then category |
| `agentreleasegate-oss` crosses 25 stars | lane F moves up a full tier; audits become the quarter's #1 |
| operator says runway <14 days | **every lane here is too slow**; go to the bridge (§15.6) |
| Instantly hits ≥90% deliverability before day 14 | lane E moves into the month's top-3 |
| operator says the andon covers past clients | §15.4 withdrawn; Upwork becomes the stamped #1 |

## §15.6 · If runway is under 14 days

Say so and this document is void. The honest order becomes: prior clients →
recruiter/staff-aug contacts → fastest available contract work, **including
non-HFO work**. HFO is an appreciating asset; it is not income. I would rather
say that plainly than optimize a portfolio while bills come due.

## Honest flaws

- **Probabilities are calibrated judgment, not measurement.** The EV/hour
  *ordering* in §15.4 is the claim; the dollar figures are illustrative and the
  12% / $2,000 prior-client estimate is the softest number in the document.
- I cannot verify the Upwork account, the prior client, or the "9-file/12-test"
  renderer from inside this forge. §15.4 rests on your report.
- The sunset call is the highest-variance stamp here. If a spatial buyer exists
  that I cannot see, it is wrong.
- I have now written 19 documents today and produced zero income. **This
  document is not exempt from Bias 1** — it is another artifact, and its only
  defense is that its #1 move takes 30 minutes and requires none of my output.
- **This session could not land a chain row.** Kernel guard still drifted
  (13,382,926 actual vs 13,339,230 expected); file still `-r--r--r--`;
  `os.access(W_OK)` = False. Return row staged at
  `inbox/olrun/20260731T2230Z_STAGED_lane_return_body.json`.

---
*FALSIFIER (whole stamp):* any lane produces a signed invoice before Upwork does ⇒ the EV/hour model mis-ranked and should be rebuilt from the actual event ·
*cost_of_delay:* E1 is 30 minutes and gates the highest-EV path; every day it slips is pure loss ·
*leverage_level_meadows:* L2 — the goal (EV per operator hour, not probability) · *domain_cynefin:* Complex

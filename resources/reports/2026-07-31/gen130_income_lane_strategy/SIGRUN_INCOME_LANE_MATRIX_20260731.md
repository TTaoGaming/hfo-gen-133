```yaml
# AIH2O
schema_id: hfo.gen130.income_lane_matrix.v0_1
unifying_phrase: "Producer, Verifier, Consumer -- all three or none"
doc: SIGRUN_INCOME_LANE_MATRIX_20260731.md
authored_by: SIGRÚN P4 · Hluti at H43 · claude-opus-5
valid_time_utc: 2026-08-01T04:00:00Z
git_head: b857c16
claim_status: proposed — probabilities are calibrated judgment, not measurement
A_assumption: HFO's architecture can be converted to near-term income
I_input: verified forge state · GNA_UPWORK_BIDS.md (exists, 2026-06-19) · 2026 rate data · zero-channel finding
H_hypothesis: FALSIFIED for near-term — the swarm earns nothing in 30 days; the operator's own labor does
H2_heldout: 40 Upwork proposals sent by 2026-08-14 with zero interviews falsifies the #1 lane
O_output: shortest path to first dollar · 7 lanes × 3 horizons · top-3 per horizon
```

# INCOME LANE MATRIX — runway edition

## ⚠️ THE MUST-ANSWER, FIRST

> **Q: Given the runway crisis, what is the shortest path to first dollar with
> >50% probability within 30 days?**
>
> **A: Upwork. Specifically: fill the `[OPERATOR FILL]` fields in
> `state/sigrun/outreach/GNA_UPWORK_BIDS.md` and submit 30–40 proposals over the
> next 14 days.**
>
> It is the only lane that has **all four** of: an existing account, a prior
> paying client ($2K, per your note), a payment rail already set up, and
> proposal copy already drafted six weeks ago. Every other lane needs an asset
> that does not exist yet.
>
> **Estimated: $500–$3,000 first contract · 7–21 days to payment · 50–65%
> probability of ≥1 job within 30 days at 40 proposals.**

**And the harder truth, stated plainly:** *HFO does not pay your bills this
month.* Not the swarm, not the spatial apps, not the audits. The shortest path
to money is **you selling your own labor through a channel that already
exists.** Everything HFO built becomes *portfolio and leverage* for that sale —
which is real value, but it is the input, not the product.

If bills are due in under 30 days, treat Upwork as the primary and everything
else in this document as secondary.

---

## 1 · One asset most of these lanes need and none of them have

**There is no live channel.** No active LinkedIn, no booking link, no social
presence. Verified this session: repo is **PRIVATE**, last pushed **30 days
ago**; OSS repo at **0 stars**; **zero send receipts** anywhere; **44 companies,
0 named humans**.

Upwork ranks #1 partly *because* it is the one channel that already exists.

## 2 · The matrix

Probability = chance of **≥1 income event** in that horizon. Revenue = realistic
low / mid / high.

### A · Spatial OS / spatial-app services
| horizon | revenue | P | first move | blocker | falsifier |
|---|---|---|---|---|---|
| week | $0 | **<5%** | `git checkout -- hfo_tiles/dist/hfopiano_v5114` | no branded demo, no buyer, no channel | — |
| month | $0–1.5K | **15%** | one branded demo at a public URL | reskin script gated | a demo exists and generates zero inquiries in 30d ⇒ no market at this quality |
| quarter | $2–10K | 35% | 3 branded demos as portfolio for consulting | — | 3 demos, 0 inbound ⇒ spatial is a hobby, not a lane |

**Honest:** impressive, off-thesis, slowest to cash. Do not let it absorb runway hours.

### B · Upwork proposals ★
| horizon | revenue | P | first move | blocker | falsifier |
|---|---|---|---|---|---|
| **week** | **$0–1.5K** | **30%** | fill `[OPERATOR FILL]`, send 10 proposals | operator hours only | 15 proposals, 0 replies ⇒ positioning wrong, not lane |
| **month** | **$500–3K** | **50–65%** | 40 proposals total | — | 40 proposals, 0 interviews by 08-14 ⇒ rate or positioning wrong |
| quarter | $3–12K | 75% | convert 1–2 to repeat clients | — | 100 proposals, 0 contracts ⇒ profile is the problem |

**Why highest:** account exists · prior client exists · payment rail exists ·
copy exists. Cost of attempt is hours.
**Risk to name:** 1 client / 0 rating is a weak profile. Expect to underprice the
first job deliberately to buy the rating. That is a real cost, not a failure.

### C · LinkedIn content + POV
| horizon | revenue | P | first move | blocker | falsifier |
|---|---|---|---|---|---|
| week | $0 | **<5%** | fix profile, publish fleet-audit post | no active profile | — |
| month | $0 | **10%** | weekly post + 15 connects/day | — | 300 connects, 0 replies ⇒ dead |
| quarter | $2–8K | 40% | sustained cadence → inbound | — | 60d, 0 inbound ⇒ kill |

**Honest:** a lead channel, not a product. Never pays inside 30 days.

### D · Social (X / Substack / HN / Reddit)
| horizon | revenue | P | first move | blocker | falsifier |
|---|---|---|---|---|---|
| week | $0 | **<3%** | cross-post the teardown | no accounts | — |
| month | $0–500 | 8% | publish failure registry (§13 #1) | — | 500 views, 0 inbound ⇒ positioning wrong |
| quarter | $1–6K | 30% | series | — | — |

**Best use:** free distribution for §13's artifacts. Zero direct revenue.

### E · Outreach push (Instantly) + pull (SEO/GitHub)
| horizon | revenue | P | first move | blocker | falsifier |
|---|---|---|---|---|---|
| week | $0 | **~0%** | build the 50-name list | **warmup not started**, 0 named humans | — |
| month | $0 | **10%** | first send if warm by ~day 21 | 14–21d unbuyable clock | day 21, deliverability <80% ⇒ DFY mis-sold, demand refund |
| quarter | $2–15K | 45% | 4-step sequence at volume | — | 500 sends, 0 replies ⇒ offer wrong |

**Honest:** already paid for, cannot produce revenue this month. Let it warm.

### F · AgentReleaseGate audits as a service
| horizon | revenue | P | first move | blocker | falsifier |
|---|---|---|---|---|---|
| week | $0 | **<5%** | publish §13 #1 + #2 | no channel, no track record | — |
| month | $0–3K | **20%** | 1 free audit for a named referenceable team | no case study | 5 free audits offered, 0 accepted ⇒ no demand |
| quarter | **$4–20K** | **50%** | 2–4 paid at $1.5–3K | — | 10 qualified convos, 0 closes at $1.5K ⇒ price is not the issue |

**Honest:** the best *quarter* lane and the best positioning. Not a runway fix.

### G · HFO consulting ($0-mesh, LiteLLM, gate setup)
| horizon | revenue | P | first move | blocker | falsifier |
|---|---|---|---|---|---|
| week | $0–1.2K | **10%** | offer via Upwork as a gig type | needs a buyer | — |
| month | $1.2–4K | **30%** | 1–2 day engagements at $600–1,200/day | — | 20 pitches, 0 takers ⇒ buyers have no budget |
| quarter | $5–18K | 55% | retainer conversion | — | — |

**Note:** this is *the same skill* Upwork buyers post for. **Sell it through
Upwork rather than building a separate funnel.** That merges B and G, which is
the single biggest simplification available.

## 3 · TOP 3 PER HORIZON

### THIS WEEK (→ Aug 7) — goal: proposals out the door
1. **Upwork (B+G merged).** *Exact first action, ≤10 min:* open
   `state/sigrun/outreach/GNA_UPWORK_BIDS.md`, fill every `[OPERATOR FILL]`
   (rate, availability, one prior-work line). Then 10 proposals by Aug 7.
2. **Message the prior $2K client.** One paragraph: available, here's what I'm
   doing now, any needs. **Highest probability-per-minute action in this
   document.** A past paying client is not cold outreach — it's the cheapest
   dollar available. *Note: your warm-network andon (×2) covers personal
   network; a prior commercial client is a different category. If you intend the
   andon to cover them too, say so and I'll drop it.*
3. **Publish the failure registry + teardown** (§13). Not for this week's money —
   it is the credibility asset lanes C/D/F need, and it costs ~8h once.

### THIS MONTH (August) — goal: first invoice paid
1. **Upwork to 40 proposals.** The volume is the mechanism. 10/week.
2. **HFO consulting sold *as* Upwork gigs** — $0-mesh/LiteLLM cost reduction is a
   real posted job category. Same profile, second gig type.
3. **One free audit** for a named, referenceable team. Costs a weekend, buys the
   case study that makes lane F chargeable in the quarter.

### THIS QUARTER (Aug–Oct) — goal: repeatable, not one-off
1. **AgentReleaseGate audits at $1.5–3K.** Needs the case study from August.
2. **Upwork repeat clients / retainer.** Convert 1–2 one-offs.
3. **LinkedIn + content compounding** into inbound. Starts paying ~day 60–90.

**Deliberately absent from all three top-3 lists: spatial apps.** They are the
most interesting asset and the worst runway play. Revisit in Q4.

## 4 · If bills are due sooner than any of this

Say so and I will re-scope. But the honest bridge, in order:

1. **Prior client** — days, if they have work.
2. **Upwork** — 7–21 days to payment.
3. **Contract/staff-aug via any prior professional relationship** — often faster
   than marketplaces because there's no bidding.
4. **Non-HFO contract dev/ops work.** If runway is measured in weeks, the correct
   move may be to pause HFO development entirely for 30 days and take the fastest
   available paid work. **HFO is an asset that appreciates; it is not income.**
   I would rather say that than optimize a portfolio while the bills come due.

## 4b · UPWORK FILL SHEET — everything verified, ready to paste

I read `GNA_UPWORK_BIDS.md` in full and verified every citable asset. The
checklist is **4 global fields (fill once) + 4 per-bid fields**. That is a
genuine ≤10-minute setup.

**GLOBAL — fill once, reuse on every proposal:**

| # | field | status / recommendation |
|---|---|---|
| 1 | **Name** | your call |
| 2 | **Rate** | market is $100–300/hr, but you have **1 client / 0 rating**. Recommend **$65–95/hr**, or a **$500–1,500 fixed-price** first project. Deliberately underprice job #1 to buy the rating; reprice at job #3. |
| 3 | **Portfolio link** | ✅ **https://handpiano.com** — verified HTTP **200** this session |
| 4 | **GitHub link** | ✅ **https://github.com/TTaoGaming/agentreleasegate-oss** — verified **PUBLIC** |
| — | *availability* | hours/week + timezone — your call |

> ### ⚠️ DO NOT paste the forge repo URL
> `github.com/TTaoGaming/hfo_gen_130_forge` is **PRIVATE** (verified). A buyer
> clicking it gets a 404, which reads as a fabricated portfolio link — the worst
> possible failure in a first proposal. Use the OSS repo above; it is the only
> public code you have.
>
> Also verified live: **agentreleasegate.com → HTTP 200**. Usable as a third link.

**PER-BID — 4 fields, ~2 min each:** client first name · restate-their-problem
(paste their exact ask) · honest timeframe for *that* scope · their target tool
(Variant B only).

**Target gig categories in the draft** (`agentic-ai-developers`,
`ai-automation-engineers`, secondary: agentic RAG) are from **June 2026** —
six weeks stale. Re-check current Upwork category names before your first batch.

**The draft's own guard is right and worth honoring:** *"Anything you can't back
with the documented work or a real artifact, leave out — do not pad with stats."*
You have three live URLs. That is enough. Do not add numbers.

> ### Refinement to §13 #1 — a field guide already exists
> `agentreleasegate-oss` is described as *"Free reward-hacking field guide + OPA
> policy + example agent skill from AgentReleaseGate."* **The artifact I
> recommended creating partly exists and is already public** — at 0 stars.
> So §13 #1's move is **not** "create a new repo." It is: expand that repo with
> the 8 named failure classes and *promote* it. That is cheaper than I estimated
> and it is another CAPACITY_AMNESIA specimen — I recommended building something
> that was already shipped. The 0 stars also confirms §13's warning: publishing
> without an audience changes nothing.

## 5 · Honest flaws

- **Probabilities are calibrated judgment, not data.** They encode ordering, and
  the ordering is the claim. Do not treat 50–65% as measured.
- I could not verify the Upwork account state, the prior client relationship, or
  the "9-file lane, 12/12 tests" — none are visible from inside this forge. The
  #1 recommendation rests on your report of the account, not my verification.
- `GNA_UPWORK_BIDS.md` is dated 2026-06-19 and marked **DRAFT ONLY — do not
  submit**. It is six weeks old; the target gig categories should be re-checked
  against current Upwork listings before sending.
- Revenue ranges come from 2026 market-rate articles with lead-gen incentives,
  discounted for zero track record.
- **Frame-capture check:** "HFO doesn't pay your bills" is a harsh conclusion,
  and harsh conclusions can read as rigor when they're just pessimism. The test:
  every lane except B requires an asset that verifiably does not exist yet
  (channel, list, case study, demo). B requires filling in blanks in a file that
  is already written. That asymmetry is the whole argument, and it does not
  depend on tone.

---
*FALSIFIER (whole doc):* 40 Upwork proposals sent by 2026-08-14 with zero interviews ⇒ the #1 lane is wrong and positioning, not volume, is the constraint ·
*cost_of_delay:* HIGHEST here of any document I have written — every day without proposals out is a day added to time-to-first-payment, and that clock is the actual constraint ·
*leverage_level_meadows:* L6 information flows · *domain_cynefin:* Complex

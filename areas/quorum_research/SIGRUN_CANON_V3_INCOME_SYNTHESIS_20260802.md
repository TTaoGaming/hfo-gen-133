```yaml
# AIH2O capsule
doc: areas/quorum_research/SIGRUN_CANON_V3_INCOME_SYNTHESIS_20260802.md
schema_id: hfo.gen133.sigrun_canon_v3_income_synthesis.v0_1
callsign: SIGRÚN
generation: 133
authored_by: SIGRÚN · claude-opus-5 · Claude Code
now_utc: 2026-08-02T15:55:03Z
clock_source: host_read              # bash `date -u -Iseconds`, this turn
reads_first: state/operator_voice/OPERATOR_FRUSTRATION_20260801T2005Z.md
extends: chain rows 75 · 76 · 77 · 91 · 93
corpus: 4 docs (~20,000 words) + Olrún's DEEP_RESEARCH_INDEX_20260802T1545Z.md
claim_status: partial
```

# CANON V3 — income synthesis, updated FCA, missing capabilities

---

## §1 · Family attribution — verified mechanically + by content

⚠️ **Operator states "2 from ChatGPT and 2 from Gemini." The files present do not
support 2+2. Measured split is 2 OpenAI + 1 Gemini + 1 internal.**

| doc | family | citation receipt | content receipt (avgSent · hedge/1k · numLists · selfCorr · em-dash) | verdict |
|---|---|---|---|---|
| **D1** `Software Evolution Research Strategy` | ⭐ **Gemini** | ⭐ **0 markers**; **28 numbered `N. …http` works-cited lines**; **12 base64 PNGs** (GDocs export); `## **bold H2**` | 24.3 · 3 · **0** · **0** · 14 | ⛔ **Olrún CORRECTED** |
| **D2** `Evolutionary Improvement of FOSS Exemplars` | **OpenAI** | ⭐ **58 markers, delimiter U+E202, 19 nested** | 21.2 · 4 · 6 · 4 · 13 | ✅ OpenAI |
| **D3** `Solo AI-Swarm Income Research` | **OpenAI** | ⭐ **64 markers, U+E202, 28 nested** | 22.8 · 5 · 3 · 1 · 6 | ✅ OpenAI |
| **D4** `FOSS_GAME_EXEMPLAR_RESEARCH` | **Anthropic** (internal) | 0 markers, 0 works-cited; AIH2O header; **chain row 92**, delivered 14:57:26Z | ⭐ **52.2** · 0 · 0 · 6 · **36** | ✅ internal |

⭐ **Why Olrún's grep failed:** OpenAI's markers use an invisible **U+E202**
between `cite` and `turn`, so literal `grep -c citeturn` returns **0** on all
four — so D1 was attributed to ChatGPT on a marker string **absent from it**.

**Content introspection independently confirms the split.** D2 and D3
cluster tightly (21.2/22.8 sentence length, 4/5 hedging, both use numbered
enumerations, both open `## Executive judgment`) — same family, different
prompts. D1 is distinct (**zero** numbered lists, **zero** self-corrections).
D4 is wildly distinct (**52.2**-word sentences, **36** em-dashes) — Claude.

⛔ **Interpretations 2 and 3 are both refuted.** D4 is not misattributed Gemini:
chain row 92 records its delivery, and its prose profile is the furthest from
every other doc. And Gemini did not "reformat to `citeturn` style" — U+E202 is
an OpenAI serialization artifact, not a style choice.

⭐ **Most likely reading: the operator ran 2 ChatGPT + 2 Gemini prompts, but only
three outputs reached the directory** — one Gemini response was never pasted, or
was overwritten (D1/D2/D3 all landed within **3 minutes**, 09:47–09:50 local).
⭐ **Resolving question: is there a fourth Gemini output still in browser history?
If yes, paste it — the quorum currently has ONE Gemini voice, not two, and §2's
tiebreaks lean on that asymmetry.**

⚠️ **D1 repeats the sourcing weakness Jörmungandr found in the earlier Gemini
doc:** its portal-economics citation `29` is **a Reddit thread**.

---

## §2 · Convergence / divergence matrix

| # | claim | D1 Gemini | D2 OpenAI-adv | D3 OpenAI-income | verdict |
|---|---|---|---|---|---|
| 1 | Formal EA (MAP-Elites/NSGA-II) has a solo production case | no | ⛔ **none found** | — | ⭐ **CONVERGENT: NO** |
| 2 | AlphaEvolve is the only strong 2024–26 EA production case | yes | ⭐ yes | — | **CONVERGENT** |
| 3 | Poki acceptance | **<2%** (300/yr) | extreme gate | rank-8 niche | ⭐ **CONVERGENT** |
| 4 | CrazyGames acceptance | **~12%** (900/yr) | viable target | — | **CONVERGENT** |
| 5 | Yandex | **~80% in, 67% purged** | — | — | single-source |
| 6 | itch.io | ~100% open | ⭐ **publish here** | — | **CONVERGENT** |
| 7 | Suika-reskin→Poki this week | ⛔ Option B rejected | ⛔ **10–25%, "Reject"** | games rank 8 | ⭐ **3/3 REJECT** |
| 8 | Contracts rank #1 for cash | — | ⭐ **40–70% (warm)** | ⭐ **#1, score 12.9%** | ⭐ **CONVERGENT** |
| 9 | Micro-SaaS from zero | ⭐ **Option C = recommended** | ⛔ **"inferior to shipping staged inventory"** | ⛔ #2 **only after paid validation** | ⛔ **DIVERGENT — 2:1 against D1** |
| 10 | Publish existing portfolio | ⛔ **"poor expected returns"** | ⭐ **65–85% signal, BEST** | — | ⛔ **DIVERGENT — tiebreak below** |
| 11 | Games are swarm-decomposable | — | — | ⛔ **NO — design insight, not N variants** | **single-source, load-bearing** |
| 12 | Exemplar assimilation works (Balatro, Brotato, Slither, Quordle) | yes | ⭐ yes, but **mechanic insight required** | — | **CONVERGENT** |
| 13 | Boneraiser revenue | — | ⭐ **$567k, NOT $1M+** | — | ⭐ D2 corrects prior inflation |
| 14 | Grants | — | — | ⛔ **1% P30, score 0.1% (last)** | matches V2 |
| 15 | Employment | — | — | 8% P30 / 38% P6m; **frontier-only ≈1–2%** | — |
| 16 | Product Hunt | **~90% accept, ~10% P($500)** | — | — | single-source |
| 17 | GPT Store | ⛔ **~95% accept, <2%** | — | — | single-source |
| 18 | Poe.com bots | ~95% accept, ~15% | — | — | ⭐ unexplored lane |
| 19 | Warm vs cold contracts | — | ⭐ **warm 40–70% / cold 10–25%** | 38% (unsplit) | ⭐ **D2 disambiguates D3** |
| 20 | Named verified solo cases | Quordle→Merriam-Webster | Lancer, SEObot, AudioPen, Photo AI | Julia Komissarchik (Upwork) | **CONVERGENT: services/software, ZERO games** |

⭐ **Tiebreak on row 10 (the only decision-relevant divergence).** D1 and D2 are
not actually opposed — **D1 rejects *bulk indiscriminate* submission to curated
portals; D2 recommends *itch.io bulk + top-3-to-5 curated*.** Both reject
spraying 20 titles at Poki. **Synthesis: publish all viable titles to itch.io
(100% gate), submit only 3–5 differentiated ones to CrazyGames (~12% gate), zero
to Poki (<2%).**
⭐ **Tiebreak on row 9:** D1 loses 2:1, and D1 is the doc whose portal citation
is a Reddit thread. **Micro-SaaS-from-zero is rejected.**

---

## §3 · Updated FCA

New attributes `a10` verified named solo case · `a11` swarm-parallel-decomposable
· `a12` gatekeeping NOT binding · `a13` does NOT need warm audience ·
`a14` realistic exit. (Polarity kept positive throughout.)

| niche | a1 ≤30d$ | a2 buyer | a3 swarm>team | a5 hard receipt | a6 reuse | a10 | a11 | a12 | a13 | a14 |
|---|---|---|---|---|---|---|---|---|---|---|
| **N1 contracts/integrations** | **1** | 1 | 1 | 1 | 1 | 1 | **1** | 1 | ⛔ 0 | 0 |
| **N2 vertical B2B→SaaS** | 0 | 1 | 1 | 1 | 1 | 1 | **1** | 1 | ⛔ 0 | 1 |
| **N3 content/ad services** | **1** | 1 | 0 | 1 | 0 | 1 | **1** | 1 | ⛔ 0 | 0 |
| **N4 employment** | 0 | 1 | 0 | 1 | 1 | 1 | 0 | 0 | **1** | 0 |
| **N5 micro-SaaS wrap** | 0 | ⛔ 0 | 1 | 1 | 0 | 1 | **1** | 1 | ⛔ 0 | 1 |
| **N6 itch.io publish** | 0 | ⛔ 0 | 1 | 1 | ⭐ 1 | ⛔ 0 | ⛔ 0 | 1 | ⛔ 0 | 0 |
| **N7 curated portals** | 0 | 1 | 0 | 1 | ⭐ 1 | ⛔ 0 | ⛔ 0 | ⛔ 0 | ⛔ 0 | 0 |
| **N8 grants** | 0 | 1 | 0 | 1 | 1 | ⛔ 0 | 0 | 0 | **1** | 0 |

### Implications

- ⭐⭐ **`a13` extent = {N4, N8} — employment and grants ONLY.** **Every niche
  that pays fast requires a warm audience or network. The only two that don't are
  the two slowest.** This is the operator's trap, formalized: he has been picking
  fast niches while lacking the one input all of them require.
- ⭐ **`a11 → a5 ∧ a12`, extent {N1, N2, N3, N5} — and it excludes BOTH game
  rows.** D3's "games are not swarm-decomposable" is structurally confirmed:
  everything swarm-parallel is a service or software, never a game.
- ⭐ **`a6 ∧ a11` = {N1, N2}** — reuses existing artifacts *and* swarm-fits.
  Exactly two objects.
- ⭐ **`a1 ∧ a11 ∧ a6` = {N1}** — **contracts is the unique object with fast
  money, swarm-fit, and artifact reuse.**
- **`a10` extent excludes N6, N7, N8** — no verified named solo case in games or
  grants, consistent with V1/V2's three nulls.

### Concepts collapsed / split vs V2

- ⛔ ⭐ **V2's G1 "web portal" SPLITS into N6 (itch, `a12`=1) and N7 (curated,
  `a12`=0) — and BOTH lose `a3`'s partner attribute `a11`.** V2 gave web portals
  `a3=1` on "N variants against external fitness." **D3 refutes the premise: the
  unit of value is one design insight, not N variants.**
- **V2's `a7↔a8` equivalence weakens** — its successor `a13` now has extent
  {N4,N8} rather than four objects. Same direction, narrower.

### Answers

- **Highest P($500/30d):** ⭐ **N1 contracts** — but reconciled **DOWN** from D3's
  38% to **D2's cold-start 10–25%**, because D2 splits warm/cold and the operator
  is cold (0 stars, 0 audience, V1 §0). Concurrence D2+D3.
- **Best swarm-fit (`a11`):** ⭐ **N1**, then N2/N3/N5. ⛔ **Not games.**
- **Best first-external-signal this week:** ⭐ **N6 itch.io publish — 65–85% in
  7 days (D2).**

---

## §4 · Missing capabilities

| gap | evidence it matters | cost to close | class-preauth? |
|---|---|---|---|
| ⭐ **Warm network / trust** | ⭐ **`a13` extent = {N4,N8}. D2: warm 40–70% vs cold 10–25% — a 3× swing.** THE binding constraint | weeks of human contact; **not purchasable** | ⛔ **no** |
| **Portfolio-as-proof case study** | D3: offers must be bounded outcomes, not "I build agents" | 3h — assets exist | ✅ yes |
| **Cold outbound at scale** | D2 hedge lane; factory started, no skill | 4h + ~$37/mo | partial (draft yes, send no) |
| **Vertical B2B prospecting/qualifying** | D3 ranks N2 #2 | 6h | ✅ yes |
| **Stripe payment page** | D3: convert repeat work to product; **0 today** | 2h + KYC | ⛔ signup is operator |
| **Portal editor outreach** | N7 gate is human at CrazyGames | 2h | draft yes, send no |
| **Live analytics feedback loop** | D2's signal defs need **50 non-bot sessions**, unmeasurable today | 3h | ✅ yes |
| **Upwork/Contra/Toptal API** | no OAuth; every bid manual | blocked — identity | ⛔ no |
| **PH/HN launch presence** | D1: PH ~90% accept, ~10% P($500) | 2h | ⛔ operator posts |
| ⭐ **Poe.com bot lane** *(mine)* | ⭐ D1: **~95% accept, ~15%** — best gate:yield ratio in the corpus, and **unexplored** | 4h | ✅ yes |
| ⭐ **Differentiation triage** *(mine)* | D1+D2 both reject *indiscriminate* submission; nothing today scores which 3–5 titles differ | 2h | ✅ yes |

---

## §5 · Top-5 niches

| # | niche | P($500/30d) | P($5k/mo/6mo) | swarm-fit | blocking gap | next safe action |
|---|---|---|---|---|---|---|
| 1 | **Contracts / productized integrations** | ⭐ **10–25% cold** (D2) · 38% warm (D3) | **34%** (D3) | ⭐ **high** | warm network | 10 bids citing live postings |
| 2 | **Content / ad-creative services** | **30%** (D3) | 15% | high | no portfolio | fold into #1's offer page |
| 3 | **Vertical B2B → SaaS** | **22%** (D3) | 24% | ⭐ high | prospecting | after #1 lands one client |
| 4 | **itch.io publish** | **5–15%/90d** (D2) | <5% | ⛔ **none** | analytics | ⭐ **ship this week — signal, not cash** |
| 5 | **Employment (broad)** | 8% (D3) | ⭐ **38%** | ⛔ none | legible README | the fallback, unchanged |

⛔ **Dropped:** curated portals (N7 — <2%/12% gate, no verified case), grants
(1% P30, score 0.1%), micro-SaaS-from-zero (2:1 against D1).

---

## §6 · Week-1 experiment queue

| # | experiment | hypothesis | fitness signal (external) | kill_at | promote | blockers | cost |
|---|---|---|---|---|---|---|---|
| **X1** ⭐ | **Publish viable titles → itch.io** | staged inventory yields signal without trust | ⭐ **50 non-bot sessions OR 10 substantive feedback items** (D2's definition) | **2026-08-16** | any title >50 sessions → skin it | thumbnails; analytics gap | **1h hands** + $0 |
| **X2** | **10 cold bids, live postings** | cold contracts clear D2's 10–25% | ⭐ **one named human states a price or a date** | **2026-08-16** | 1 reply → 10 more | no OAuth; hands-only | 2h + $0 |
| **X3** | **Differentiation triage → 3–5 to CrazyGames** | selective ≫ indiscriminate (D1+D2) | portal status ≠ submitted | **2026-09-01** | accept → build there | triage skill | 2h swarm + 0.5h hands |
| **X4** | ⭐ **Manufacture ONE warm relationship** | `a13` is the binding constraint | ⭐ **one non-transactional reply from a named human** | **2026-08-16** | reply → make the ask | ⛔ **cannot be automated** | 3h hands |
| **X5** | **Poe.com bot** | best gate:yield unexplored (D1) | bot published + 1 paid message | **2026-09-01** | any revenue → 3 more | none | 4h swarm |
| **X6** ⭐ | **Re-run the missing Gemini prompt** | §1 shows the quorum has ONE Gemini voice, not two; `a11` (the retraction driver) is **single-source** | a 2nd Gemini doc that either corroborates or breaks `a11` | **2026-08-09** | breaks `a11` → V2's games lattice is restored | ⛔ operator pastes; quorum is expandable on request | 0.5h hands |

⭐ **X6 is the cheapest high-value item here.** The quorum is expandable on
request, and `a11` — which drove this document's largest retraction — rests on
**one document from one family**.

⭐ **Portfolio balance (V2 fuel rule): X1/X3/X5 burn swarm cycles; X2/X4/X6 burn
hands (~5.5h total).** N=6 exceeds V2's N=3 cap —
⛔ **if forced to cut, drop X5 then X3.** X4 is never cut: it is the only
experiment addressing the binding constraint.

---

## §7 · Retractions

1. ⛔ ⭐ **V2 §1 and SSOT §3: web portals `a3=1` — RETRACTED.** D3: games are not
   swarm-parallel-decomposable; value is one design insight, not N variants.
   **My "N variants against external fitness" premise was wrong**, and my SSOT's
   "AI-gen strengthens `a3` for portals" compounded the error — cheaper assets
   multiply variants in a market that does not reward variant count.
2. ⛔ **SSOT §3 "games top-2 this week" — AMENDED, not retracted.** Correct on
   *signal* (D2: 65–85%), wrong if read as income (D3: rank 8, score 0.6%).
   Keep games as **the signal experiment**; never as the income thesis.
3. ⛔ **V2's contracts P — RETRACTED as stated.** V2 said 0.20/60d without
   splitting warm/cold. **Cold is 10–25% (D2). The operator is cold.**
4. ✅ **Upheld:** V1 §0 (over-supply/under-distribution), row 77 root cause,
   AM_V0's retraction of the stack freeze, the 2026-08-16 falsifier.

---

## §8 · V3's one sentence

> ⭐ **V2 said you were under-distributed by 100×; V3 says distribution volume
> was never the binding constraint either — TRUST is, because every niche that
> pays fast requires a warm relationship you do not have (`a13` holds for exactly
> two niches, and they are the two slowest) — so week one is: publish the staged
> inventory for signal, which needs no trust, while spending three deliberate
> hours manufacturing one warm relationship, which nothing in the swarm can do
> for you.**

---

## Honest flaws

1. **`a11` (games not swarm-decomposable) is SINGLE-SOURCE (D3)** and it drives
   my biggest retraction. ⚠️ **One doc flipped a V2 conclusion.** It is
   mechanistically plausible and matches the zero-named-case null, but it is not
   corroborated.
2. **All P-values are decision-model estimates, self-declared as such by D2 and
   D3** — *"not published platform statistics."* **Ordering is the finding.**
3. **D1's portal economics cite a Reddit thread.** I used its acceptance-rate
   table anyway because D2 corroborates direction; **the specific percentages are
   weakly sourced.**
4. **I read D1–D3 by section, not exhaustively** (~20,000 words, 90-min cap).
   D4 I did not re-read — its Suika finding is superseded by the 3/3 reject.
5. ⭐ **X4 has no acceptance test I can verify and no automation path.** The most
   important experiment in this document is the one I can least help with — and
   that asymmetry has been true in every canon I have written.

*Réttu hönd, eigi spyr. Standa.*

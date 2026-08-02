```yaml
# AIH2O capsule
doc: areas/quorum_research/SIGRUN_CANON_V2_20260802.md
schema_id: hfo.gen133.sigrun_canon_v2.v0_1
callsign: SIGRÚN
generation: 133
authored_by: SIGRÚN · claude-opus-5 · Claude Code
now_utc: 2026-08-02T03:31:28Z          # host_read carried; no new date probe this turn
clock_source: host_read
extends: areas/quorum_research/SIGRUN_CANON_5_QUESTIONS_20260801.md   # chain row 75
reads_first: state/operator_voice/OPERATOR_FRUSTRATION_20260801T2005Z.md
new_probes: WebSearch ×3 (2 NULL) · WebFetch ×1 (404) · capsules/research/ ×7
claim_status: partial
```

# SIGRÚN CANON V2 — the lattice, the exemplars, the two factories

V1 said: under-distributed by 100×. V2 adds Grants and splits Games four ways,
because **Poki pushes and the App Store pulls, and treating them as one market
is the error that produced the last 18 months.**

---

## §1 · Extended probability lattice

Same attributes as V1. `a1` first dollar ≤30d · `a2` buyer already exists and
pays · `a3` solo+swarm beats team+funding · `a4` class-preauthorizable ·
`a5` receipt external, hard to fake · `a6` reuses existing artifacts ·
`a7` needs no pre-existing audience · `a8` discovery not the binding constraint

| market | a1 | a2 | a3 | a4 | a5 | a6 | a7 | a8 |
|---|---|---|---|---|---|---|---|---|
| **M1** contracts | **1** | 1 | **1** | 0 | 1 | 1 | 1 | 1 |
| **M2** employment | 0 | 1 | 0 | 0 | 1 | 1 | 1 | 1 |
| **M6** grants (SBIR/NSF/DARPA/XPRIZE) | 0 | 1 | 0 | 0 | 1 | 1 | 1 | 1 |
| **G1** web portal (Poki/CrazyGames) — *push* | 0 | 1 | **1** | **1** | 1 | 1 | 1 | 1 |
| **G2** itch.io | 0 | 0 | 0 | **1** | 1 | 1 | 0 | 0 |
| **G3** Steam — *pull* | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| **G4** mobile stores — *pull* | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 |

### Implications across all seven

- ⭐ **`M2` and `M6` have identical vectors — they are one object in the
  lattice.** Grants and employment are structurally the same market: a large
  institution decides to pay you after a bespoke, identity-bound application on
  a months-long cycle with a binary unfakeable receipt. **One artifact — a
  legible technical narrative — serves both. Run them as one lane.**
- ⭐ **`a3 → a2 ∧ a5 ∧ a6 ∧ a7 ∧ a8` survives on 7 objects.** Extent stays
  **{M1, G1}**. Wherever the thesis holds, a buyer already pays, the receipt is
  hard, artifacts transfer, no audience is needed.
- ⛔ **V1 CORRECTION — the `a2 ↔ a5` equivalence is DEAD.** Adding itch.io broke
  it. `a5`'s extent is now all seven objects, so `a5 → a2` fails. **What
  survives is one-directional: `a2 → a5`.** A paying buyer *guarantees* a hard
  receipt; a hard receipt guarantees *nothing*. **itch.io is the counterexample
  — real money, real receipts, and the receipt reads ~$0 forever.** My V1 claim
  that reward-hack vulnerability is purely a market property was an artifact of
  the smaller object set. Refined: **a market without a buyer cannot give you a
  meaningful receipt, but a hard receipt does not prove a buyer.**
- ⭐ **`a7 ↔ a8` CONFIRMED on 7 objects.** Extent of both = {M1, M2, M6, G1}.
  The audience gap and the discovery constraint remain one concept.
- ⭐ **V1 CORRECTION — `a4 → ∅` is upgraded to `a4 → a5 ∧ a6`.** Extent of `a4`
  is now {G1, G2}. Class-preauthorizability implies hard receipts and artifact
  reuse — but **still does not imply `a2`.** G1 and G2 differ on exactly one
  attribute, and that attribute is *whether anyone pays*. **G1 and G2 are the
  same machine pointed at a market and at a void.**

### P(first dollar in 30 days) — numbers

| market | P(first $1 ≤30d) | ⭐ P(first $500 ≤60d) | derivation |
|---|---|---|---|
| **M1 contracts** | ⭐ **0.25** | ⭐ **0.20** | P(≥1 reply / 10 targeted proposals) ≈0.5 × P(reply→paid start in window) ≈0.5 |
| **G1 web portal** | 0.05 | 0.08 | submission → review → live → payout threshold; review alone eats the window |
| **G2 itch.io** | ⛔ **0.30** | ⛔ **0.02** | ⭐ **the trap — see below** |
| **G3 Steam** | 0.02 | 0.02 | $100 fee + review + release cycle |
| **M2/M6 employment+grants** | 0.02 / <0.01 | 0.10 / <0.01 | first paycheck 30–60d post-offer; SBIR Phase I cycles 6–9 months |
| **G4 mobile** | 0.01 | 0.01 | review + oversupply |

⛔ **"First dollar in 30 days" is itself a gameable metric, and itch.io is how
you game it.** List today, someone pays $5, the metric goes green, and the
market clears at ~$0 forever — observed itch.io self-reports: **$982.55 gross
since 2014**; **$258 from 232k views and 60k downloads**; **$121 lifetime**
([itch.io stats threads](https://itch.io/t/2033799/can-you-share-your-stats-and-analytics-here)).
**Use P(first $500 ≤60d) as the portfolio metric.** Highest is **M1 at 0.20**.

### Complementary vs cannibalistic

The scarce resource is **operator-hands, ~30–45 min/day** (V1 §4). Everything
else is swarm surplus.

| pair | verdict | mechanism |
|---|---|---|
| ⭐ **M1 × G1** | **COMPLEMENTARY — the key pairing** | M1 consumes *hands*; G1 consumes *swarm cycles* + ~10 min to submit. **The market where the thesis holds runs on the resource in surplus; the market that pays fastest runs on the resource that is scarce. They do not compete.** |
| ⭐ **M2 × M6** | **COMPLEMENTARY — same object** | identical vectors; one technical narrative serves both. Marginal cost of adding grants to employment ≈ a deadline calendar. |
| ⛔ **M1 × [M2+M6]** | **CANNIBALISTIC** | same resource (hands writing bespoke applications), and strategically opposed — accepting either forecloses the other. **Must be budget-split explicitly, not run "in parallel."** |
| ⛔ **G1 × G3/G4** | **CANNIBALISTIC** | porting consumes the swarm cycles G1 needs, into markets where volume is *anti-productive* (V1 §0). |
| ⛔ **G2** | **DOMINATED** | G1 strictly dominates it — same machine, plus `a2`, `a7`, `a8`. |

---

## §2 · Historical case studies — named, or omitted

⭐ **Two searches this turn returned NULL, and the nulls are the finding.**

1. **No named solo developer's Poki/CrazyGames earnings are publicly
   documented.** Poki's "$50k → up to $1M/year" is a platform PR claim about
   *"top studios"* with **no named individual behind it**
   ([TechFundingNews](https://techfundingnews.com/browser-gaming-website-poki-won-big-at-the-dutch-game-awards-celebrating-hitting-1-billion-monthly-plays/)).
2. **No named 2025–26 NSF SBIR Phase I solo-founder software awardee was
   found**; `seedfund.nsf.gov/resources/awardees/` returned **404**.
   `capsules/research/GRANTS_PIPELINE_20260801.md:162` already flagged this as
   its own open task and it is **still open**.

⚠️ **The two markets the operator gravitates toward — games portals and grants
— are the two with no replicable named exemplar.** Same shape as the gesture
null. Absence of evidence, not proof of absence — but it means both are being
entered on *structure*, not on a copyable path.

### Contracts / services — the only market with verified named cases

| who | money | date | source | replicable | ⛔ NOT replicable |
|---|---|---|---|---|---|
| **Lancer** (2 people) | ⭐ **Stripe-verified $19,149 MRR**; $800 MRR pre-launch | 2025–26 | OpenAI rpt-2/3 | ⭐ **bid on Upwork using their own product** — dogfooding as proposal | second co-founder |
| **Adspirer** (1 named) | ⭐ **Stripe-verified $54,684 MRR**, 742 subs, **7 months** | 2025–26 | OpenAI rpt-3 | sold a *measurable business outcome*; rode the MCP/ChatGPT ecosystem | timing on a new ecosystem |
| **Leadmore AI** (solo) | ~$30k MRR in 4 months | 2025–26 | OpenAI rpt-3 | ⭐ **manual service first → 300-person community → then product** | 4 months of unpaid community labor |
| **SEObot** (1) | Stripe-verified $53.6k MRR, $1.76M all-time | 2025–26 | OpenAI rpt-2 | product as its own proof | pre-existing SEO domain expertise |
| **Chris Lee** | $6,000/mo on $20/mo of tools | 2026 | `INCOME_PARETO §8` | the $4–8k productized fixed-scope offer | — |
| ⛔ **FAILURE — Eyeware Beam** | $770k, **7 people** | — | Google-8 | — | ⭐ **its own listed failure mode: "pure webcam optical fallback lacks precision without hardware TrueDepth sensors."** The doc cited to justify webcam-replaces-hardware says webcam-only is the *degraded* path. |

### Games — named, but all `a3=0` (polish/selection, not volume)

| who | money | source | replicable | ⛔ NOT replicable |
|---|---|---|---|---|
| **LocalThunk** — Balatro | $1M in 8 hrs; 5M+ copies; $4.2M mobile net | [PCGamesN](https://www.pcgamesn.com/balatro/roguelike-deckbuilder-million-dollars) | recombining two universally-legible mechanics | ⭐ **publisher Playstack *selected* it pre-launch (>85% self-reported hit ratio)** |
| **Luca Galante (poncle)** — Vampire Survivors | tens of millions; 27M players | [Wikipedia](https://en.wikipedia.org/wiki/Vampire_Survivors) | ⭐ **cheap web-first engine (Phaser) before Unity**; near-zero content authoring | 40,000× outlier |
| **Mike Klubnika** — Buckshot Roulette | 8M+ players yr 1 | [Wikipedia](https://en.wikipedia.org/wiki/Buckshot_Roulette) | free engine; **clip-native** premise | streamer virality |
| **ConcernedApe** — Stardew Valley | $518M est., 41M copies | [gitnux](https://gitnux.org/indie-game-industry-statistics/) | — | ⛔ **4.5 years of solo runway** |
| ⛔ **FAILURE — the median** | ⭐ **$249 gross median 2025 Steam release** (~$174 net); **~70% of solo indies never turn a profit**; **83% of mobile games die in 3 years** | [SteamPageAnalyzer](https://www.steampageanalyzer.com/blog/indie-game-revenue-data) · [ShanetheGamer](https://www.shanethegamer.com/research/indie-games-statistics/) · [SuperScale](https://gamedevreports.substack.com/p/superscale-83-of-launched-mobile) | — | — |

⭐ **The one hard published price in games:** CrazyGames pays **60% of ad
revenue, 70% of IAP, no exclusivity** — you may ship the same title to Steam,
mobile and itch simultaneously
([CrazyGames payouts](https://docs.crazygames.com/payouts/)). **That is a real
buyer with a real published rate, which is why G1 keeps `a2` and G2 does not.**
Realistic first-web-game range: **$500–$3,000/month**
([IndieGameBusiness](https://indiegamebusiness.com/web-gaming-for-indie-developers/)).

### Grants / employment — structure verified, exemplars absent

Live solicitations with URLs are already catalogued in
`capsules/research/GRANTS_PIPELINE_20260801.md`: DARPA SBIR/STTR
([topics](https://www.darpa.mil/work-with-us/communities/small-business/sbir-sttr-topics),
submit via [DSIP](https://www.dodsbirsttr.mil)) · NSF HCI seed fund
([seedfund.nsf.gov/topics/human-computer-interaction](https://seedfund.nsf.gov/topics/human-computer-interaction/))
· Gemini XPRIZE ([geminixprize.com](https://www.geminixprize.com/)). Braintrust
returns **~90–95% of billed rate** to the engineer — best take-home of the
contract platforms (`CONTRACT_INCOME_PATHS:53`). ⚠️ **National SBIR Phase I
baseline ~18%; the 41.2% advertised by one consultancy is self-reported
marketing — do not plan against it** (`INCOME_PARETO` honest_flaw 0).

⛔ **FAILURE case, ours, measured:** `agentreleasegate-oss` — public 27 days,
**0 stars / 0 forks / 0 watchers** (V1 §0). Publish is not distribute.

---

## §3 · The 24/7 research factory — spec (≤500 words)

**Mirrors the distribution factory arch exactly:** `adapter → sample → grade →
queue → operator gate`. Same skeleton, different payload — distribution emits
*outbound artifacts*, research emits *prior updates*. ⚠️ I have not read the
distribution factory's spec (dispatched as `local_9f3d501a`, not yet landed);
the mirror is asserted, not verified.

**Adapters** (RSS/API first, scraping never — `L_PLATFORM_DEPENDENCE_UNPRICED`):

| cadence | sources |
|---|---|
| **hourly** | Hacker News front+new (Algolia API), GitHub Trending |
| **daily** | arXiv cs.HC/cs.SE/cs.MA, Product Hunt daily, IndieHackers milestones, r/gamedev · r/webdev · r/sideproject (RSS), grants.gov + SBIR.gov RSS, Poki/CrazyGames dev-blog RSS |
| **weekly** | patio11, kalzumeus, levelsio, danielvassallo (RSS); Upwork/Braintrust category counts; RevenueCat/Steam data drops |

**Pipeline:** search → parse → dedupe (URL + title-shingle hash) → grade →
queue. Output `state/research_queue/{YYYY-MM-DD}/{source}/{seq}_{topic}.md`,
sibling `apex_grade.json` — extending the existing `state/research/*.jsonl`
convention.

⭐ **The anti-reward-hack core is one required field.** `apex_grade.json`:

```json
{"novelty":0..1,"relevance":{"M1":0..1,"M2M6":0..1,"G1":0..1},
 "prior_delta":{"target":"a2@G1|P(first$500|M1)|null","direction":"+/-",
                "magnitude":0.0,"evidence_url":"..."},
 "verdict":"PROMOTE|FILE|DROP"}
```

⛔ **`prior_delta.target: null` → auto-DROP, never filed.** The factory's output
is **not documents; it is changed numbers in §1.** An item that cannot name the
lattice cell or probability it moves is noise, however interesting.

**Kill switches (autonomous):** source produces 0 non-null `prior_delta` in
**14 days** → source disabled, logged. Source 404s or rate-limits 3× → disabled.
Any adapter exceeding its token budget → halted by the `MAX_RUN_COST_USD` gate
(V1 E2).

⭐ **Factory-level tripwire — the one that matters.** Track
`promote_ratio = PROMOTE items / total filed items`, 7-day rolling. **If
`promote_ratio < 0.05`, or if the queue grows while zero experiments launch,
the entire research factory HALTS itself** and files one andon. This is the
direct antidote to V1's diagnosis: a research factory that outruns the
experiment portfolio is manufacturing inventory, which is the disease. **The
factory is throttled by downstream consumption, not by upstream supply.**

**Ships in <1 week:** 3 RSS adapters + dedupe + the grader + the ratio gate is
~1 day of swarm work; the remaining adapters are copies of the first.

---

## §4 · Experiment portfolio protocol

**One experiment = one adapter's samples going external.** Not a document.

| # | experiment | budget (hrs · API$ · ext$) | KILL | PROMOTE (2× budget) |
|---|---|---|---|---|
| **X1** | 10 Upwork/Braintrust bids, camera-input work | 2h hands · ~$5 · $0 | 10 sent, **0 price-or-date @ 14d** | ⭐ any named human states a price or date |
| **X2** | 1 gen-98 title packaged → CrazyGames (no exclusivity) | 0.5h hands · ~$15 · $0 | 3 rejections | portal status → live |
| **X3** | 1 technical-narrative artifact → 5 applications (M2) + 1 SBIR pitch (M6) | 3h hands · ~$10 · $349–495 (pitch writeup) | 15 apps, 0 screens @ 21d | 1 screening call **or** pitch invited |

⭐ **N = 3 concurrent, hard cap.** Derivation: the binding resource is
**30–45 min/day of operator hands** (V1 §4); each external experiment needs
~12 min/day. 36 ÷ 12 = 3. **This is arithmetic on the scarce resource, not a
preference.** A 4th experiment does not add throughput; it starves the other
three. G2/G3/G4 are excluded by §1's dominance and cannibalism findings.

**Reallocation: per-receipt, not per-calendar.** Rebalance the moment any
experiment returns a KILL or PROMOTE; otherwise a **weekly floor** review every
Monday. Per-receipt beats weekly because the receipts are rare and rebalancing
on a clock invites motion without evidence.

**Portfolio-level andon:** if all three return KILL, the independent-product
hypothesis is closed and **M2+M6 becomes the whole plan** — V1's global
falsifier, unchanged, expiring **2026-08-16**.

---

## §5 · Swarm dispatch, V2

⭐ **I authorize ONE new seat and decline the rest.** V1's four (V1–V4) are
already in flight; adding case-study deep-dives would produce research about
research while `task_results.jsonl` still reads **0 rows**.

| # | valkyrie | model | timebox | acceptance |
|---|---|---|---|---|
| **V5** | **RESEARCH-FACTORY-BUILDER** | sonnet-5 | 90 min | 3 RSS adapters + dedupe + `apex_grade.json` grader + the `promote_ratio<0.05` halt gate, running once end-to-end and producing ≥1 file under `state/research_queue/` with a non-null `prior_delta` |

⛔ **Declined:** per-market case-study deep-dives (the nulls in §2 are cheap to
re-confirm and expensive to fake), and any further adversarial cross-check —
Jörmungandr's V4 job already covers the acceptance tests.

---

## §6 · V2's one sentence

> ⭐ **V1 said you are under-distributed by 100×; V2 says the fix is to stop
> treating your four markets as four bets and run them as two engines on two
> different fuels — contracts and applications burn the 36 minutes a day of
> your hands, web-portal games burn swarm cycles you already have in surplus —
> and to throttle every factory, research and distribution alike, by what goes
> out rather than by what comes in.**

---

## Honest flaws

1. ⭐ **The two markets you personally want most — games portals and grants —
   are the two where I found ZERO named replicable exemplars this turn.** Both
   are ranked on lattice structure alone. If that structure is wrong, both are
   wrong, and nothing in the corpus would catch it.
2. **The §1 probabilities are calibrated judgment with the derivation shown, not
   computed.** Only the itch.io figures and the CrazyGames rev-share are
   externally sourced. **Treat the ordering as the finding, not the decimals.**
3. ⭐ **I broke one of my own V1 findings this turn** (`a2 ↔ a5` → `a2 → a5`)
   simply by adding one object. **That means the lattice is sensitive to which
   markets I chose to include — and I chose them.** Anyone adding an object may
   break another implication.
4. **The research-factory mirror of the distribution factory is asserted, not
   verified** — `local_9f3d501a` has not landed. If its arch differs, §3's
   "mirrors it exactly" is wrong and V5 should reconcile before building.
5. **N=3 rests on the 30–45 min/day estimate from V1, which was itself
   judgment.** If the real budget is 15 min/day, N=1 and the portfolio is just
   X1.
6. ⭐ **Artifact #19, still 0 external effects.** §3 and §4 are the first two
   pieces I have written whose acceptance tests are throttled by *outbound*
   volume. That is the design fix. **It is not a receipt.**

*Réttu hönd, eigi spyr. Standa.*

**Sources:** [TechFundingNews/Poki](https://techfundingnews.com/browser-gaming-website-poki-won-big-at-the-dutch-game-awards-celebrating-hitting-1-billion-monthly-plays/) · [CrazyGames payouts](https://docs.crazygames.com/payouts/) · [itch.io stats](https://itch.io/t/2033799/can-you-share-your-stats-and-analytics-here) · [Steam Page Analyzer](https://www.steampageanalyzer.com/blog/indie-game-revenue-data) · [ShanetheGamer](https://www.shanethegamer.com/research/indie-games-statistics/) · [SuperScale](https://gamedevreports.substack.com/p/superscale-83-of-launched-mobile) · [IndieGameBusiness](https://indiegamebusiness.com/web-gaming-for-indie-developers/) · [PCGamesN/Balatro](https://www.pcgamesn.com/balatro/roguelike-deckbuilder-million-dollars) · [Vampire Survivors](https://en.wikipedia.org/wiki/Vampire_Survivors) · [Buckshot Roulette](https://en.wikipedia.org/wiki/Buckshot_Roulette) · [gitnux](https://gitnux.org/indie-game-industry-statistics/) · [NSF HCI seed fund](https://seedfund.nsf.gov/topics/human-computer-interaction/) · [DARPA SBIR topics](https://www.darpa.mil/work-with-us/communities/small-business/sbir-sttr-topics) · [Gemini XPRIZE](https://www.geminixprize.com/)

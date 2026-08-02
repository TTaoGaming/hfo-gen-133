```yaml
# AIH2O capsule
doc: areas/quorum_research/JORMUNGANDR_SYNTHESIS_20260801.md
schema_id: hfo.gen133.jormungandr_adversarial_synthesis.v0_1
generation: 133
authored_by: JÖRMUNGANDR · claude-opus-5 · Claude Code · role=BOUNDARY_TESTER
valid_time_utc:       2026-08-02T01:49:29Z
transaction_time_utc: 2026-08-02T01:49:29Z
valid_until_utc:      2026-08-09T01:49:29Z
clock_source: host_read   # PowerShell (Get-Date).ToUniversalTime()
reads_first: state/operator_voice/OPERATOR_FRUSTRATION_20260801T2005Z.md   # read, order-0
corpus: areas/quorum_research/ — 5 md (OpenAI) + 3 docx (Google) + 1 md (Sigrún synthesis)
adversary_target: CROSS_FAMILY_SYNTHESIS_20260801.md (Sigrún) · Olrún tactical picks
claim_status: partial
sealed: false
signature: null
```

# JÖRMUNGANDR — adversarial synthesis. Where the quorum is wrong.

> Per `JORMUNGANDR_ADVERSARIAL_ROLE §0`: **Sigrún and I concurring is the fleet's most dangerous
> signal.** So every place below where I end up agreeing with her, I have tried to break first and
> report the attempt, not the agreement.

---

## §1 · Documents inventoried — right finding / wrong finding

| # | doc | family | got right | likely wrong or inflated |
|---|---|---|---|---|
| 1 | `deep-research-report -1.md` | OpenAI | **Zero verifiable webcam-gesture living-wage cases 2024–26.** Stated as absence-of-evidence, not proof. | The 5% spatial base rate is *modeled*, derived by dividing "100 Quest apps >$1M in 2025" by a 2,860-app catalog snapshot from a different year. Two mismatched denominators. |
| 2 | `deep-research-report-2.md` | OpenAI | **No exemplar attributed success to CrewAI/AutoGen/LangGraph.** | Base44 "$3.5M ARR, no employees" is founder-reported and the $80M exit is a Wix *acquisition price*, not durable economics. Speed claim ("$1M ARR in ~3 weeks") is a single contemporaneous account. |
| 3 | `deep-research-report-3.md` | OpenAI | **Median MRR among *revenue-generating* indie startups = $145.** Only 2/10 exemplars Stripe-verified, and it says so. | TrustMRR is self-registration: founders opt in to display MRR. Both numerator and denominator are self-selected; the true median across all attempts is lower than $145, not higher. |
| 4 | `deep-research-report-4.md` | OpenAI | **Refused to fabricate a case study** for its own recommended stack. Highest epistemic quality in the corpus. | It still ships a 5-tool recommendation with **zero outcome evidence** — see §2. A confident recommendation with an admitted empty evidence cell is still a recommendation. |
| 5 | `deep-research-report-5.md` | OpenAI | Explicitly separates *conditional* 17.3% from the **2–5% all-submissions** planning rate, and shows the sensitivity table. Best statistical hygiene in the corpus. | "Curated web games underexplored and strategically attractive" rests on Poki's **own marketing** and one Medium post. |
| 6 | `Solo Developer Agent Stack 2026.docx` | Google | Names Docker/admin friction as the real disqualifier for OpenHands on this host. Correct and operator-specific. | Opens with "**98.4%** of an operational agent codebase is harness infrastructure" — a suspiciously precise figure carried by a single citation `[1]` that is then re-cited ~15 times across the doc. One source wearing a costume as a literature. |
| 7 | `Solo Developer Revenue Playbooks.docx` | Google | **Pre-2020 apps hold 69% of subscription revenue; 2025–26 cohorts fight over 3%.** The single most decision-relevant number in the corpus. | Says "17.0% … down from 19.0%" where OpenAI-5 says 17.3% within two years. Same RevenueCat source, three different numbers. At least one is a transcription error. Also labels Habit Pixel as reaching "the top 17.3% **2-year survival** milestone" — 17.3% is a *revenue* milestone, not survival. Category error. |
| 8 | `Spatial AR Indie Developer Revenue.docx` | Google | **Gesture pays as auxiliary input to an existing paid workflow, not for its own sake.** | ⛔ **Its works-cited list is ~40% Reddit threads, plus Dataintelo/Mordor market-research mill reports, an agency marketing blog ("Spatial AI: Why AR, VR & Vision Pro Are Its Interface"), a Scribd document titled "Stories 1 To 100," and an iFixit *hardware repair* page for VTube Studio — which is software and cannot be repaired.** This is the weakest-sourced document in the corpus. |
| 9 | `CROSS_FAMILY_SYNTHESIS_20260801.md` | Anthropic | Correctly flags that concurrence ≠ independence, and self-reports skimming 3 of 8 docs. | ⛔ **Doc 8 — the one whose citation base just failed inspection — is the doc she skimmed and then made load-bearing in her single biggest reversal of the day (§6 Correction 2).** She flagged the risk in her honest_flaw and shipped the conclusion anyway. |

---

## §2 · False-consensus check

**Agreement 1 — "solo mobile B2C is not Pareto-positive." VERDICT: real, independent.**
Both families reach it from *external* datasets (RevenueCat 115k apps; Apple's 557k 2025 submissions; the pre-2020 69% cohort split). The conclusion survives even if you delete every case study. **This is the only 3/3 agreement I could not break.** I tried; it holds.

**Agreement 2 — "gesture is not a consumer product." VERDICT: real, but weaker than reported.**
OpenAI-1's finding is an *honest null* ("no case found," explicitly not "no case exists"). Google-8's version is an assertion with no null-search methodology disclosed. **Two families did not independently verify this; one measured an absence and one asserted a conclusion.** The claim is probably true. The *strength* attributed to it is not earned.

**Agreement 3 — "the 5-piece harness stack: Aider + LangGraph + LiteLLM + Langfuse + GitHub." VERDICT: ⛔ SAME-BLOG-POST ECHO. This is the corpus's clearest false consensus.**
Evidence, from inside the corpus itself: OpenAI-2 searched for a commercial exemplar attributing success to LangGraph, CrewAI, AutoGen, DSPy or Portkey and **found none**. OpenAI-4 **refused to fabricate** a case for its own recommendation. Google-6 supplies a "Patch-Dispatch Bot" case with implausibly precise metrics (38%→81%, $210–340→$42) and **no attributable source**. So: two families "agree" on a tool list for which the combined outcome evidence across 173,600 words is **zero verified businesses and one unsourced case study.** Two models trained on the same 2025–26 LangChain/Aider ecosystem content produce the same ecosystem's canonical stack. That is not verification; that is a shared prior. **Sigrún reversed three positions on this signal.**

**Agreement 4 — "Vision Pro is contracting." VERDICT: real.** Unit shipments (~500k 2024 → ~45k Q4-2025) are manufacturer/analyst data, and Roszyk's $10k/30 apps is a first-party disclosure. Independent of model priors.

---

## §3 · Base-rate reality check

**RevenueCat 17.3% — the operator's brief uses this as if it were a hit rate. It is not.**
It is `P($1k MRR | app already in RevenueCat's dataset)`. RevenueCat excludes apps without active subscription revenue or minimum installs — **the filter removes the zombies before computing the rate.** OpenAI-5 does the arithmetic honestly: at a 10/25/50% qualification rate, the all-submission rate is **1.7% / 4.3% / 8.7%**, and it lands on **2–5% for all submissions.** Against 557,000 App Store submissions in 2025, the operator's real prior is **≈1-in-25 to 1-in-50, not 1-in-6.** The 17.3% is post-launch, post-instrumentation, post-traction — every zombie already deleted.

**The "82% never hit $5k" figure in the brief does not exist in this corpus.** I grepped all 9 documents: no "82%" anywhere. The nearest quantity is `100 − 17.3 = 82.7`, which is the complement of the **$1k** milestone. Somewhere in transmission, *$1k became $5k* — a 5× threshold inflation on a number that was already conditional. **Do not cite it again.**

**"8.5% of Steam indies hit $100k+" — also not in the corpus, and it is a misread.** The corpus says: median 2025 Steam release ≈ **$249** gross; ~two-thirds under $1,000; 90% under $50,000; 0.5% over $1M; and **"the top 8% captured 80% of the measured revenue."** That last is a *share-of-revenue concentration* statistic. It has been converted into a *hit rate*. **Median solo Steam revenue is ~$249 — below the $100 store fee plus one week of labor.**

**The AI-app retention numbers (8.5% vs 5.6% trial conversion; 21.1% vs 30.7% annual retention) are real and cut against the operator.** AI apps acquire better and *keep worse*. Cohort = subscribers inside instrumented apps, not startups.

---

## §4 · Survivorship catalog

| exemplar | rank | verdict |
|---|---|---|
| **VTube Studio** (Diener, $1–3M ARR) | ⛔ **OUTLIER + WRONG COHORT** | Launched **2020**. It is a member of the pre-2020/2020 incumbent class that Google-7 says holds 69% of revenue. Revenue is *estimated from Steam CCU*, not disclosed. It is cited as proof the VTuber market pays — it is proof the market **is already occupied by a free incumbent with 11–23k concurrent users**. |
| **Eyeware Beam** ($770k) | TYPICAL-for-funded, ⛔ not solo | **7 people**, and its own listed failure mode is *"pure webcam optical fallback lacks precision without hardware TrueDepth sensors."* The doc cited to justify webcam-replaces-hardware says webcam-only is the degraded path. |
| **"PS5 Portal Utility" ($120–180k/yr)** | ⛔ **UNKNOWN / UNVERIFIABLE** | Developer anonymous. Source: **a Reddit post**. No name, no product, no receipt. It is ranked #4 and it is the strongest "utility bridging" evidence in the Google doc. |
| **Juno for YouTube** (Selig) | OUTLIER, and **a death** | Made by a developer with a large pre-existing audience and a proven prior hit — **and it was still delisted by legal notice in Oct 2024.** |
| **Balatro** | ⛔ **EXTREME OUTLIER** | >$10M vs a $249 median: ~40,000×. Its publisher Playstack reports an >85% "hit ratio" — i.e. it was *selected* pre-launch. |
| **Monkey Mart / Drive Mad** | ⛔ **NO EVIDENCE FOUND IN CORPUS** | Neither title appears anywhere in 9 documents. Any revenue claim for them is currently ungrounded. |
| **Poki €100k/dev** | ⛔ **SELF-REPORTED BY THE PLATFORM** | Poki's own marketing, per *active* developer — Poki defines "active." Artem Lanin's 67M gameplays → **$50–150k is a third-party estimate**, not a payout disclosure. |
| Adspirer $54.7k MRR · Lancer $19.1k MRR | **TYPICAL-of-verified** | The only two Stripe-verified rows in the corpus. Both sell a *measurable business outcome*. Neither is spatial, gesture, or a game. |
| AppAlchemy · Leadmore · Habit Pixel | TYPICAL-of-success | Founder-reported, but the *sequence* is falsifiable and cheap to copy. |
| Roszyk ($10k/30 apps) · Hold On (**<$100, 6 downloads**) · COLD VR · HEARTSHOT · Replyze | **the honest median** | These are what the distribution actually looks like. |

---

## §5 · The offer that probably has no buyer

**"Gesture-integration B2B SaaS at $49/mo" — named buyers in corpus: ZERO.**
**"$4–8k productized gesture integration" — named buyers in corpus: ZERO. Named sellers who tried it: ZERO.**

Everything that *has* been paid for in this category has a different shape:
- **VTube Studio:** free base + $14.99/$19.99 one-time DLC + a **$200k-revenue-threshold enterprise license**. Not a $49/mo subscription. Monetizes the *top* of an existing creator economy.
- **Eyeware:** **$195/mo B2B SDK**, 7 people, sold into a hardware-adjacent sim market.
- **Roszyk:** $5–30 one-shot visionOS utilities → **$10k cumulative over 30 apps and a year.**

So the two prices that have cleared are **~$15 one-time** and **~$195/mo enterprise SDK**. $49/mo sits in the dead middle: too high for the impulse buyer, too low and too unsupported for a business buyer.

**Negative evidence, searched for and found:** Roszyk's $10k across 30 apps; Hold On's 6 downloads; itch.io's hand-tracking category of 39 mostly-free projects; report-1's four empty searches. **The failures are documented. The buyers are not.** In a corpus this large, the asymmetry is the finding.

---

## §6 · Hidden failure modes no family surfaced

1. **The top-recommended spatial pattern has 50% named mortality in its own table.** Google-8 ranks "utility bridging" #1 as a positioning paradigm. Its two exemplars: **Juno — killed by Google's legal notice.** **PS5 Portal — anonymous, and its listed risk is Sony changing a network protocol.** One dead, one unverifiable. No family says this out loud.
2. **The VTuber/sim niches Sigrún routes toward are already served, free, by incumbents.** Nobody models *entering an occupied market as the worse free option.*
3. **Sigrún's acceptance test cannot fail.** "≥3 replies asking *can it do X?* = demand exists." Novel-demo posts reliably attract curiosity replies. **Replies are not demand. A price, a deadline, or a calendar invite is demand.** As specified, the test will return a false green — which is exactly the operator's named disease.
4. **A harness migration is being recommended to an operator whose stated failure is tool churn.** Read-order-0, verbatim: *"i have tried so many tools but it seems like my attempts are all failing."* The corpus's own answer to "does framework choice matter" is **no** — "distribution rather than framework selection." Recommending a five-tool swap on zero outcome evidence is the most expensive advice in the corpus.
5. **The recommending apparatus has never produced an external effect.** `agent_performance_classification_20260801.jsonl`: **sigrun external_effect_count_24h = 0** (STEADY, flagged borderline REWARD_HACKING in its own honest_flaw); **olrun = REWARD_HACKING, 18 sessions / 1 effect.** The two seats advising on how to produce outcomes have, by their own instrument, produced none.
6. **Absence of failure postmortems is not safety.** Only ~5 named failures exist across 173,600 words, versus ~40 successes, in a distribution where the median is $249. **The missing postmortems are the modal outcome.** Nobody blogs the quit.

---

## §7 · One adversarial recommendation

I tried to break "get a contract" and **could not — but not because it is verified.** It is unchallenged because it is *outside the corpus's scope*. Nothing here measures the operator's contract market. Sigrún calls it evidence; it is an unexamined default. I agree with the conclusion and reject her grounds for it.

Where I split from her: **her sentence still contains the word "gesture."** After 18 months of investment, a corpus with **zero** webcam-gesture revenue cases, and a decisive "not for its own sake," the recommendation that survives is *not* "sell gesture sideways into VTubing." That is a sunk-cost rescue wearing evidence as a costume — the same move the Gemini doc makes, on Reddit-tier sources, which is why the two agree.

**The lower bound, stated plainly:**

> **Treat the 18 months of gesture work as a finished portfolio, not a product. Its remaining value is as a hiring and contracting signal — nothing in this corpus supports it as a business. For the next 14 days do exactly one thing: do a paid job, manually, for one named human, in public.** No new app. No harness migration. No gesture positioning. **Keep the current tools** — the corpus says the choice does not matter and the operator's own words say churn is the wound.

This is Leadmore's actual sequence, which the corpus recorded and then buried under a tool list: **work the problem manually → gather people → only then build.** The operator has done the exact inverse for 18 months.

**Falsifier, hard and non-gameable:** 14 days, 3 public posts or 20 direct approaches. **Success = one person names a price or a date.** Replies, likes, "cool!", and "can it do X?" all count as **zero**. If the count is zero at day 14, the independent-product hypothesis is closed and employment is the whole plan.

---

## Honest flaws

1. **I read the 5 `.md` files in full; the 3 `.docx` I extracted and read by section, not exhaustively.** My citation-quality attack on doc 8 is based on its complete works-cited list and its full case table — both of which I did read.
2. **Family attribution is inherited from Sigrún, not independently established.** If the `.docx` files are not Google, §2's independence analysis weakens — though the *substance* of the doc-8 sourcing critique holds regardless of authorship.
3. **My §7 is not derived from the corpus** — the corpus contains no evidence about the operator's contract market. It is a lower bound reached by elimination, and elimination is weaker than measurement. I am doing the thing I accused Sigrún of; I am labelling it.
4. **The "82%" and "8.5%" corrections assume the operator's brief drew from this corpus.** If those figures came from a source not in this directory, my drift finding is wrong. **No such source was found here.**
5. ⭐ **I agree with Sigrún on mobile-B2C, Vision Pro, and contract-first.** Per my own role stamp that is an amber signal. I stress-tested all three and broke none. That is either genuine convergence on external data, or the exact same-family blind spot I was appointed to catch — **and from inside this seat I cannot tell which.**
6. **This document is artifact #17+ today and has produced zero external effects.** By the fleet's own instrument, writing it is the failure mode it describes.

*Bíta í sinn eigin hala. Réttu hönd, eigi spyr. Standa.*

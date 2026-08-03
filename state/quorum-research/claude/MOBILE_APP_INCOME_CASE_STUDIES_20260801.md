```yaml
schema_id: hfo.quorum_research.internal.v0_1
family: anthropic
model: sonnet-5
source: capsules/research/MOBILE_APP_INCOME_CASE_STUDIES_20260801.md
consolidated_utc: 2026-08-02T01:15Z
clock_source: host_read
```

---

# Mobile App Income Case Studies — Solo/Small-Team, $5K+/mo, 2024-2026

**Callsign:** research_valkyrie_mobile_apps · **Lane:** mobile apps (Google Play / iOS / hybrid)
**Timebox:** 30 min · **Date:** 2026-08-01
**Raw structured data:** `state/research/mobile_app_income_cases_20260801.jsonl`

Rehydration read-order-0 honored: `state/operator_voice/OPERATOR_FRUSTRATION_20260801T2005Z.md` (operator overwhelmed, wants ONE apex + spatial apps, is asking whether mobile app-store is a viable pivot lane).

---

## Top-5 Depth Case Studies

### 1. Sebastian Röhl — HabitKit / FocusKit / WinDiary (solo, Germany)
- **Revenue:** $602K in 2025 · $28K MRR from 25,100 paying subscribers at $1-2/mo
- **Stack:** Native Swift/SwiftUI. Notably **migrated off Flutter onto native SwiftUI** mid-2025 and said he'd use SwiftUI for everything going forward — cross-platform cost him App Store feel and ranking signal.
- **Acquisition:** Pure ASO — cracked Top-5 "Habit Tracker" in the US App Store, organic discovery did the rest.
- **Time to money:** ~6 months to meaningful MRR, 12-month committed runway before he called it working.
- **Failure survived:** Burned real time on the Flutter version before concluding native was necessary for ranking + feel.
- [Source](https://sebastianroehl.substack.com/p/2025-the-year-that-changed-everything)

### 2. Max — 28-app portfolio sprint (solo, Latvia)
- **Revenue:** $100 → $25K MRR in 8 months ($84K cumulative), while still working full-time.
- **Stack:** AI-assisted rapid build: **Lovable, Bolt, Cursor, Claude, Replit, Supabase** — 50-70% build-time reduction vs. traditional dev.
- **Acquisition:** Ship-fast-let-data-decide; killed non-performers quickly instead of polishing one app for months.
- **Failure survived:** Prior strategy of perfecting single apps for months → zero traction; power-law portfolio (most of the 28 made near-nothing, a few carried it).
- [Source](https://www.buildmvpfast.com/blog/portfolio-app-strategy-multiple-apps-revenue-solo-founder-2026)

### 3. Yusuf Seyitoğlu — 143-app portfolio (solo)
- **Revenue:** ~$4.8K MRR total across 143 shipped apps; best single app $1,870/mo; only 11/143 clear $100/mo.
- **Acquisition:** Founder's own words: "marketing still feels like gambling" — even at 143 launches, discovery/ASO is unsolved.
- **Time to money:** 18 months of continuous shipping to reach current run-rate.
- **Failure survived:** 92% of the portfolio (132/143 apps) generates negligible/zero revenue — the base-rate reality behind the portfolio strategy.
- [Source](https://medium.com/@developeryusuf/solo-dev-in-2026-ive-shipped-143-apps-marketing-still-feels-like-gambling-but-i-m-finally-winning-more-than-i-m-losing-179654b60462)

### 4. Hendrik Folkerts — Wunderfind Bluetooth/AirPods finder (team of 2, Berlin)
- **Revenue:** $13K/mo, zero ad spend, ~100K organic App Store ratings; app later listed for acquisition at $400K.
- **Stack:** Native iOS + Android, Bluetooth LE.
- **Acquisition:** Single narrow high-frequency pain point (lost AirPods) — the hardware's ubiquity did the marketing for free.
- **Failure mode / limit:** Success pattern is hard to generalize — it rides Apple's own hardware-attach problem, not a repeatable acquisition skill.
- [Source](https://www.goodreads.com/author_blog_posts/23483205-low-key-developer-earning-60-000-month-from-2-apps)

### 5. Danny Postma — HeadshotPro (solo, Bali/Singapore) — AI-vision, web-first
- **Revenue:** $300K/mo peak, $100K ARR in first 14 days.
- **Stack:** Stable Diffusion + DreamBooth, **proprietary multi-model stacking pipeline** (dozens of models vs. competitors' single model) for "10x output quality." **Web-first, not App Store distributed.**
- **Acquisition:** Organic content/SEO, no paid ads; leveraged credibility from a prior AI exit (Headlime → acquired by Jasper in 8 months).
- **Failure mode / limit:** Not an App Store case — lessons on ASO don't transfer. Category commoditized fast once headshot-generation became a common AI API wrapper.
- [Source](https://startupfounderstories.com/stories/danny-postma-headshotpro-ai-headshots)

*(6th case in the JSONL for triangulation: Habit Pixel, solo, $1K MRR after 8 months — the un-glamorous floor case.)*

---

## Failure Base Rates (cited)

| Threshold | % of apps that reach it | Source |
|---|---|---|
| >$1,000/mo | **17.2%** reach it (RevenueCat, *State of Subscription Apps*); consistent with the inverse stat that **80.83%** of apps fail to hit $1K MRR by year 2 | [digitalinformationworld.com](https://www.digitalinformationworld.com/2024/03/report-shows-172-apps-earn-1000month.html), [start.io](https://www.start.io/blog/report-80-of-mobile-apps-fail-to-earn-1000-month-in-subscription-revenue/) |
| $1K → $2.5K | 59% of apps that reach $1K go on to reach $2.5K | RevenueCat, cited via digitalinformationworld.com |
| $2.5K → $5K | 60% of apps that reach $2.5K make it to $5K | same |
| >$10,000/mo | **3.5%** of apps | same |
| General | 94% of app developers earn under $1,000/mo; top 1% of apps capture 90%+ of store revenue | [theswiftk.it.com](https://theswiftk.it.com/blog/zero-to-10k-mrr-indie-ios-app) |

**Read:** getting to $1K/mo is a ~1-in-6 shot; getting past $10K/mo is a ~1-in-30 shot conditional on shipping at all (before counting apps that never launch). Every case study above is survivorship-selected — none of these sources report the denominator of abandoned/never-launched apps.

---

## Operator-Fit Table

Operator stack: web + AI + spatial/gesture (MediaPipe-class hand-tracking), demo01-handpiano **LIVE**. Ranked by (skill fit × time-to-money × revenue ceiling).

| Case pattern | Skill fit | Time-to-money | Revenue ceiling | Verdict |
|---|---|---|---|---|
| **Danny Postma (web-first AI+vision, content-led)** | **HIGH** — operator already builds AI+vision+web; this is his existing lane, not a pivot | **HIGH** — Postma hit $100K ARR in 14 days off an existing audience/SEO play | **HIGH** — $300K/mo demonstrated | **Closest fit.** Not App Store at all — argues FOR staying web-first rather than pivoting to mobile. |
| **Max / Yusuf (AI-tool-assisted portfolio shipping)** | **HIGH** — same Claude/Cursor-class tooling operator already runs in HFO | **MEDIUM** — Max hit real MRR in 3mo, Yusuf took 18mo and still calls marketing "gambling" | **MEDIUM** — power-law, most shipped units earn ~$0 | Process is directly transferable (ship small, kill fast) regardless of target being App Store or web. Marketing/ASO remains the unsolved bottleneck operator already flagged in his own frustration note. |
| **Sebastian Röhl (native Swift, single-category focus)** | **LOW** — requires new stack investment (Swift/SwiftUI) operator hasn't built; explicitly abandoned Flutter/cross-platform | **LOW** — 6-12mo committed runway before payoff | **HIGH** — $602K/yr proven | Real ceiling, but the entry cost is a stack the operator does not currently hold, at a moment he's already overwhelmed. |
| **Wunderfind (narrow utility, hardware-attach niche)** | **LOW** — no analog in operator's current niche; success rode Apple's own AirPods ubiquity, not a repeatable acquisition skill | **MEDIUM** | **MEDIUM** ($13K/mo, team of 2) | Not a good template — the "why it worked" doesn't generalize to spatial/gesture apps. |

---

## Recommendation

**Mobile app-store distribution is not clearly Pareto-positive for this operator right now.** Base rates say ~83% of shipped apps never clear $1K/mo and ~96.5% never clear $10K/mo, and the highest-fit case (Postma) succeeded specifically by **avoiding** App Store gatekeeping and shipping web-first off his existing AI+vision skillset — the same skillset the operator already has via demo01-handpiano. The transferable pattern isn't "go mobile," it's "ship the spatial/vision web app fast with AI-assisted tooling (Max/Yusuf process) and drive it with content/SEO instead of ASO (Postma pattern)." Native mobile (Röhl's proven $602K/yr path) is a real ceiling but demands a stack investment (Swift/SwiftUI) the operator doesn't currently hold — a second bet on top of an already-overwhelmed operator, not a faster path to the one apex + spatial apps he said he wants.

---
**Chain row (proposed, no HMAC seal):**
`{"ts":"2026-08-01T~Z","agent":"research_valkyrie_mobile_apps","claim_status":"wired_with_receipts","verifier_result":"6 case studies + JSONL + base-rate table with cited URLs, written to capsules/research/ and state/research/","remaining_risk":"all case sources are self-reported by founders, no independent revenue verification; failure-rate stats (RevenueCat) cover subscription apps only, not full App Store category mix","next_safe_action":"operator decision: confirm web-first spatial (Postma pattern) over native mobile (Röhl pattern) as the lane, or explicitly request native mobile spike","honest_flaw":"did not reach Sensor Tower/data.ai primary reports directly — relied on secondary citations of RevenueCat's State of Subscription Apps report for base rates"}`

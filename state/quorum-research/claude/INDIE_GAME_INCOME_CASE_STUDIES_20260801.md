```yaml
schema_id: hfo.quorum_research.internal.v0_1
family: anthropic
model: sonnet-5
source: capsules/research/INDIE_GAME_INCOME_CASE_STUDIES_20260801.md
consolidated_utc: 2026-08-02T01:15Z
clock_source: host_read
```

---

# Indie Game Income Case Studies — Solo/Small-Team Revenue Reality 2024-2026

- agent: sonnet-5, HFO gen-133, research valkyrie (compose lane, no code-touch)
- callsign: research_valkyrie_indie_games
- date: 2026-08-01
- clock_source: host_read
- timebox: 30 min
- data file: `state/research/indie_game_income_cases_20260801.jsonl`
- rehydration read-order-0: **read [[operator-recurring-context]] and `state/operator_voice/OPERATOR_FRUSTRATION_20260801T2005Z.md` first** if picking this back up cold. Operator wants ONE apex + spatial apps, is weighing whether game-building is a viable revenue lane vs a distraction from productized-service work.

⚠️ UNVERIFIED-CLASS NOTE: figures are aggregator/self-reported, not independently audited. Steam/Vampire-Survivors/Balatro-scale numbers trace to press coverage of dev/publisher claims, not audited financials. Web-game (Poki/CrazyGames) per-title dollar figures are platform-published *ranges*, not individually verified per-developer receipts. Treat as directional. Truthful-red > false-green.

## Top-5 Depth Studies

| Case | Dev | Tech | Monetization | Revenue | Why it worked |
|---|---|---|---|---|---|
| [Vampire Survivors](https://en.wikipedia.org/wiki/Vampire_Survivors) | Luca Galante (poncle), solo start | Phaser → Unity | Paid $4.99 | Tens of millions cumulative, 27M players | Zero-risk nights/weekends side project, cheap web-friendly engine first, addictive near-zero-content-authoring loop |
| [Balatro](https://www.pcgamesn.com/balatro/roguelike-deckbuilder-million-dollars) | LocalThunk, solo | LÖVE (Lua) | Paid | $1M in 8hrs, 5M+ copies, $4.2M mobile net | Recombined two universally-legible mechanics (poker + roguelike deckbuilder); publisher (Playstack) scaled it post-proof |
| [Buckshot Roulette](https://en.wikipedia.org/wiki/Buckshot_Roulette) | Mike Klubnika, solo | Godot | Paid, low price | 8M+ players in year 1 | Free engine, real-object premise, streamer/clip-native discovery loop |
| [Schedule I](https://www.shanethegamer.com/research/indie-games-statistics/) | TVGS, solo | Unity | Paid, Early Access | $151M gross in 2025 | Taboo niche (drug-kingpin sim) major studios won't touch; EA let revenue compound pre-launch |
| [Stardew Valley](https://gitnux.org/indie-game-industry-statistics/) | ConcernedApe, solo | XNA/MonoGame | Paid | $518M est., 41M copies | 4.5yr solo runway, self-taught art+code+music, nostalgia hook (Harvest Moon successor) |

**Honest gap:** despite targeted searches, no single *named* solo web-game (Poki/CrazyGames) developer surfaced with an audited or even self-reported individual dollar figure in this pass — only platform-level aggregate ranges (below). That itself is a signal: web-game solo success stories are far less publicly documented than Steam ones.

## Base Rates — the part that matters more than the outliers

**Steam (solo/small indie):**
- Median indie game gross revenue on Steam in 2025: **$249** (developer nets ~$174 after Valve's cut). [Steam Page Analyzer](https://www.steampageanalyzer.com/blog/indie-game-revenue-data)
- Broader median (multi-year): **$5,000-$15,000** lifetime gross → **$3,500-$10,500** net.
- **~10-15%** of indie games clear **$50K+ net** (the rough "was this a reasonable use of a year" threshold — requires ~$80-100K gross).
- **~7-10%** hit **$100K+ gross** (2025 cohort: ~8.5%). Split across a 5-person team that's $14K/head/year.
- **~70%** of solo indie developers **never turn a profit**. [ShanetheGamer](https://www.shanethegamer.com/research/indie-games-statistics/) / [Steam Page Analyzer](https://www.steampageanalyzer.com/blog/how-much-do-indie-game-developers-make)
- Marketing now eats **30-50%** of total project spend (up from 10-20% historically) — the discoverability crunch is getting worse, not better.

**Mobile hyper-casual:**
- Typical 3-month ARPU **$0.30-$0.70**; at 10-20M installs, lifetime profit tops out around **$700K total**, split between publisher and dev (~$350K each) — and that install volume is itself a rare outcome requiring publisher UA spend most solo devs don't have. [GameAnalytics](https://www.gameanalytics.com/blog/the-metrics-behind-hyper-casual-games-industry-report)
- **24%** of hyper-casual studios are on the verge of bankruptcy; **32%** have done layoffs. [PlayDucky](https://playducky.com/recentpress/5-myths-about-hyper-casual-hit-games)
- **83%** of launched mobile games (all categories) die within 3 years. [SuperScale via gamedevreports](https://gamedevreports.substack.com/p/superscale-83-of-launched-mobile)
- Industry is actively shifting to "hybrid-casual" (IAP + live-ops) because pure ad-only hyper-casual monetization has hit a ceiling — leading 2025 titles earned **3x** their 2024 equivalents by adding IAP/live-events, meaning pure ad-hypercasual is being deprecated as a solo-viable model.

**Web games (Poki/CrazyGames):**
- First web game realistic range: **$500-$3,000/month**, highly dependent on genre, update cadence, and time live. [IndieGameBusiness](https://indiegamebusiness.com/web-gaming-for-indie-developers/)
- CrazyGames revenue share: developers keep **60%** of ad revenue, **70%** of IAP revenue, no exclusivity required (can also list on Steam/mobile/itch simultaneously). [CrazyGames dev docs](https://docs.crazygames.com/payouts/)
- Poki claims top studios that earned ~$50K/year five years ago now earn **up to $1M/year** — but this is a platform PR claim about "top studios," not a solo-dev median, and no named individual case backs it. [TechFundingNews](https://techfundingnews.com/browser-gaming-website-poki-won-big-at-the-dutch-game-awards-celebrating-hitting-1-billion-monthly-plays/)
- HTML5/web game market overall: **$6B+ by 2026**, growing — but growth in the aggregate market does not mean growth in per-solo-developer odds.

**itch.io:**
- Most of the **900,000+** projects hosted earn **under $100 lifetime**.
- Active-marketing launches: **$500-$5,000**. Sustained community engagement: **$5,000-$50,000** over time. [GeneralistProgrammer](https://generalistprogrammer.com/tutorials/how-to-make-money-on-itchio-indie-game-guide)
- itch.io's flexible revenue-share (dev sets 0-100% cut) beats Steam's fixed 30% at low sales volume, but only matters once there's meaningful traffic — which most projects never get.
- Notable niche outlier: **TTRPG creators** clear $1K-$10K+/month on itch — a content/community-driven niche, not a game-loop niche.

## Novel-Input Angle — Gesture/Webcam-Controlled Games

Operator has a working hand-tracking demo01. Searched directly for monetized gesture-controlled web games.

**Verdict: UNPROVEN revenue territory, real prototype activity.**

- Multiple hobby/prototype-grade gesture games exist (MediaPipe-based Pong, Bubble Shooter, Fruit Ninja clones, a webcam-hand 3D particle toy), documented on GitHub and itch.io tag pages ([itch.io hand-tracking tag](https://itch.io/games/tag-hand-tracking), [IEEE conceptual paper](https://ieeexplore.ieee.org/document/10951073/)) — but these are demos/student projects, not revenue-generating products.
- Zero named cases surfaced (across 3 targeted search queries) of a gesture/webcam-controlled game with any public revenue figure — self-reported or audited.
- The one commercial angle found is generic (hand-tracking SDK vendors licensing for "monetizable content creation"), not a game-specific monetization proof.
- **Read honestly:** this is a genuine white-space / differentiator (none of the Top-5 exemplars above use novel input), but "differentiator" and "proven monetizable" are different claims — there is no base rate to point to here, only zero.

## Operator-Fit Rank

1. **Web game on CrazyGames/Poki (ads, no exclusivity)** — lowest time-to-first-dollar signal ($500-3K/mo range for a first title is a real, checkable number within weeks, not years), stacks with operator's existing web/WebGL stack, and can be listed alongside Steam/itch simultaneously at zero extra dev cost. Best-fit **first probe**, not a retirement plan.
2. **itch.io as a free discoverability/community test bed** — cheap way to get the hand-tracking demo in front of real players and collect signal before betting real build-time on a full game.
3. **Steam solo paid release** — highest ceiling (the Top-5 above) but also the highest variance/lowest base rate (70% never profit) and the longest runway (Stardew: 4.5yr; even the "fast" outliers assume years of prior skill-building). Not a near-term Pareto move for an operator explicitly trying to reduce scope and stop the burnout spiral.
4. **Mobile hyper-casual** — worst fit: requires either a UA/publisher budget the operator doesn't have, or reach the top decile organically; pure ad-only hyper-casual is itself being deprecated industry-wide in favor of hybrid-casual IAP models that need more design/live-ops sophistication than a solo build affords.
5. **Gesture/webcam-controlled game as the sole differentiator** — do not treat this as a revenue thesis by itself; it is unproven territory with zero comparable cases. Use it as a *feature* layered onto a web/itch game (item 1/2), where downside is capped, not as the product's whole bet.

## Bottom Line

**Game-building is a Pareto-plausible SIDE lane for fast, cheap, capped-downside experiments (web/itch, days-to-weeks feedback loop) — it is NOT a Pareto-positive PRIMARY lane compared to productized-service/client work at the operator's current stage.** The base rates are unambiguous: 70% of solo Steam devs never profit, median Steam revenue is $249, and even "fast, cheap" web-game income tops out at $500-3K/month for a first title with no guarantee of repeatability. The named wins in this report (Vampire Survivors, Balatro, Buckshot Roulette, Schedule I, Stardew Valley) are survivorship-biased extreme outliers, most requiring either years of unpaid runway or a lightning-strike premise/mechanic recombination that cannot be planned for. If the operator wants revenue this quarter, client/productized-service work (per prior micro-SaaS and contract-income capsules) has a shorter, more controllable path than game-building; if the operator wants a low-cost, low-risk build-in-public artifact to pair with the hand-tracking demo, ship it to CrazyGames/itch as a free side-channel experiment, not as the main bet.

## Chain row

```json
{"row_class":"research_receipt","agent":"sonnet-5_research_valkyrie","task":"indie_game_income_case_studies","clock_source":"host_read","date":"2026-08-01","claim_status":"proposed","verifier_result":"5 named case studies (Vampire Survivors, Balatro, Buckshot Roulette, Schedule I, Stardew Valley) + Steam/mobile-hypercasual/web/itch base rates + gesture-input verdict, all URL-sourced from WebSearch","remaining_risk":["all revenue figures are press/aggregator-reported, not audited financials","zero named solo web-game (Poki/CrazyGames) case with individual $ figure found despite 3 targeted queries — platform-level PR claims used instead, flagged as such","gesture-controlled-game monetization verdict is a negative result (absence of evidence) not a definitive absence-of-opportunity proof","survivorship bias in the Top-5: all are extreme outliers, explicitly labeled as such in the bottom-line synthesis"],"next_safe_action":"if operator wants to probe the web-game lane, next step is scoping ONE small game (reusing hand-tracking demo01 as the control scheme) sized for a 1-2 week build, ship free to CrazyGames+itch simultaneously, and read real installs/revenue after 30 days before committing further build time","honest_flaw":"30-min timebox meant no primary-source verification (no direct dev interviews, no Stripe/Steamworks dashboard access); this is a synthesis of public secondary sources only"}
```

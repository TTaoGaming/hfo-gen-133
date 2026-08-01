```yaml
# AIH2O
schema_id: hfo.gen133.ship_readiness_marketplaces_income_roadmap.v0_1
unifying_phrase: "You are not blocked on building. You are blocked on one deploy and one named human."
doc: SIGRUN_SHIP_READINESS_MARKETPLACES_INCOME_ROADMAP_20260801.md
authored_by: SIGRÚN · claude-opus-5 · project lead
carrier: claude-opus-5 · Claude Code · gen-133 forge root
valid_time_utc: 2026-08-01T00:00:00Z
transaction_time_utc: 2026-08-01T00:00:00Z
generation: 133
claim_status: >
  §3.1 falsifier result is wired_with_receipts (disk probe, this session).
  §4 is research-grounded, sources cited, snippet-grade unless marked [F].
  §5 is proposed — every row carries a falsifier and a cost-of-delay.
builds_on: SIGRUN_SPATIAL_GESTURE_SWARM_INCOME_CASE_STUDIES_20260801.md (does not supersede it)
roster_source: areas/substrate_health/SUBSTRATE_ROSTER.md v0_2 + OLRUN_ROSTER_AND_CLASS_RECONCILIATION_20260801.md
evidence_grade_key: "[F] = page fetched in full · [S] = search-result snippet · [D] = first-hand disk probe this session"
sealed: false
```

# SHIP READINESS · MARKETPLACES · INCOME ROADMAP — 2026-08-01

---

# §3 · CAN WE PRODUCE SPATIAL APPS TODAY?

## §3.0 · The answer

> ## **Yes. Production is not the blocker and has not been for months. The blocker is that nothing you produce ever leaves the building, and no named human is waiting to receive it.**

Two receipts make this a claim rather than an encouragement:

1. A complete, deployable gesture PWA exists on disk right now, with its
   configuration already factored out of the bundle (§3.1, probed this session).
2. `handpiano.com` returns HTTP 200 — you have already done the whole loop once,
   end to end, including hosting.

Everything below is about the gap between those two facts and a dollar.

## §3.1 · ⭐ THE §4.2 FALSIFIER — RUN. IT PASSES.

The prior case-studies doc ranked `hfopiano_v512` as the #1 reskin candidate and
staked that rank on an unrun 20-minute check: *"if the config surface turns out
to be entangled with `index.html`'s 315KB bundle such that a brand swap requires
editing the bundle by hand, the reskin-factory claim is wrong."*

**I ran it. [D]**

### Already external — swap without touching the bundle

| file | size | what it is |
|---|---|---|
| `settings_profiles.v512.json` | 49,380 B | the settings/preset profile, loaded via `SETTINGS_PROFILE_URL = "./settings_profiles.v512.json"` (index.html:889). `app_id: handpiano_v512_omega` |
| `tile_descriptors.v512.mjs` | 21,949 B | UI tile descriptors |
| `refinery_presets.mjs` + `signal_refinery.mjs` | 6,846 + 3,224 B | **your signal refinery, as a module** |
| `vendor/handpiano-sample-packs/`, `vendor/smplr-samples/` | dirs | **soundpacks are directories.** Swap = swap a folder |
| `icon-192.png`, `icon-512.png`, `manifest.webmanifest`, `assets/models/` | — | icons, PWA manifest, ML models |
| `i18n.mjs` | 9,044 B | copy strings |

### Still inside the 315KB bundle — the honest cost

| location | constant |
|---|---|
| index.html:886–888 | `APP_VERSION`, `APP_CHANNEL`, `APP_LINEAGE_LABEL = "HandPiano Omega v512 Alpha"` |
| index.html:912 | `const CONFIG = { launchPreset, hands:{max,modelDelegate,mp:{…}} … }` |
| index.html:2558–2559 | `HANDPIANO_SAMPLE_PACK_ADAPTER`, `HANDPIANO_SYNTH_ADAPTER` |
| index.html:2741, 2850 | `BLACK_CHROMA`, `OVERLAYS` (palette / overlay surface) |

> ### **VERDICT: rank 1 SURVIVES.** A brand swap is **three string constants, one palette block, one folder swap, two icons, and one JSON file** — not a hand-edit of 315KB of logic. The falsifier's failure condition is not met.

**Bonus finding, and it is worth more than the falsifier.** The bundle documents
four named injection seams:

```js
window.HandPiano.setVideoSource(urlOrStream)    // mp4 / stream
window.HandPiano.injectRawLandmarks(hands, ts)
window.HandPiano.injectNoisyLandmarks(hands,ts) // same refinery path
window.HandPiano.injectCursorDTO(dto)           // bypasses refinery
```

That is **a real, already-shipped external ABI** — the thing the Sigrún ABI spec
was proposing to design. It also means the app is *testable without a camera and
without a human*, which is exactly what an automated factory needs.

## §3.2 · Inventory — what exists, what state it is in

| asset | located? | state | buildable | deployable | demoable |
|---|---|---|---|---|---|
| **`hfopiano_v512`** (handpiano) | ✅ [D] `hfo_gen_130_forge/hfo_tiles/dist/hfopiano_v512/` | complete static PWA, 30 files, `_headers` + `sw.js` + 404 | **already built** (it is a `dist/`) | ✅ static-host drop | ✅ **live at handpiano.com, HTTP 200** |
| `pinchpiano` | ✅ [D] same `dist/` | present, **not inspected this session** | unknown | unknown | unknown |
| `hfopiano_omega_v502` | ✅ [D] `hfo_tiles/apps/` | source lineage, superseded by v512 | n/a | n/a | reference only |
| **TAGS v25.7.15** | ✅ [D] `C:\Dev\archive\archive_pre_hfo_to_gen_84\Tectangle TAGS v25.7.15` | pre-gen-84 archive: `index-modular-monolith.html`, `hand-tracking-reality-prototype.html`, `package.json`, `sw.js`, `vendor/`, `piano-genie-clone/`, `prototypes/` | needs npm install | unknown | **prototype-grade, older lineage** |
| `four_finger_piano v0.11` | ⛔ **NOT LOCATED** this session (depth-5 scan of `C:\Dev`) | unknown | — | — | — |
| `table_tennis v29` | ⛔ **NOT LOCATED** this session (depth-5 scan) | unknown | — | — | — |
| `hfo_gen_131_mediapipe_repair` | ⛔ not probed | — | — | — | — |

**Correction to prior canon:** the case-studies doc ranked `four_finger_piano`
#2 and `table_tennis` #3 without either being located on disk in this session.
I could not confirm they exist at the paths implied. **Do not plan around them
until someone points at the directory.** TAGS, which that doc refused to rank,
*is* now located — and the answer is that it is a pre-gen-84 prototype with an
npm build step, i.e. materially further from shipping than `hfopiano_v512`.

**This changes the ranking:** it is not a four-app portfolio. It is **one
shippable app, one unknown sibling in the same `dist/` (`pinchpiano`), and an
archive.** Which is fine — you only need one — but plan on one.

## §3.3 · What is actually blocking — the honest list

| # | blocker | severity | who clears it |
|---|---|---|---|
| B1 | **No second deployed property.** One reskin has never been put on the internet. Every income move downstream needs a *second* URL that is not handpiano.com. | ⛔ **the real one** | operator (deploy is a world-effect) |
| B2 | **Deploy mechanism not documented in-forge.** `_headers` + `404.html` + `sw.js` is the **Cloudflare Pages / Netlify** convention, so a static-drop path almost certainly already exists — but I did not find the deploy script or the account, and I will not assert it. | ⚠️ HIGH — unknown, probably 10 minutes | operator names the host; Codex writes the script |
| B3 | **`brand.json` not extracted.** Until the 4 in-bundle constants are lifted out, each reskin is a manual edit and "N per week" stays a hope. | ⚠️ MEDIUM | **Codex lane only** — Claude's `code_authoring` gate has denied `scripts/` writes 4× |
| B4 | **Zero named humans to send anything to.** Recorded defect: 44 companies enriched, **0 named contacts.** A demo with no recipient is comb, not honey. | ⛔ **co-equal with B1** | garmr (Codex apex) queues; operator sends |
| B5 | **No invoice/payment rail verified in-forge.** You have been paid before (Upwork), so a rail exists — it is not documented here. | ⚠️ MEDIUM | operator confirms in one line |
| B6 | **Nobody can loop long enough to run a factory** except Codex (9h+, confirmed). | ⚠️ MEDIUM | see §5 — adopt a harness, do not build one |
| B7 | `four_finger_piano` / `table_tennis` unlocated | LOW | anyone with the path |

**Note what is NOT on this list:** skill, tooling, model capability, tracking
quality, architecture. None of those are blocking. The blockers are *one deploy*
and *one named human*.

## §3.4 · ⭐ FIRST APP TO SHIP THIS WEEK — pick one, and it is this one

> ## **Ship ONE reskin of `hfopiano_v512` under an invented brand, to a static host, as a pitch asset. Not a product. A pitch asset.**

Named path, step by step:

| # | step | owner | est. | gate |
|---|---|---|---|---|
| 1 | `cp -r hfopiano_v512 brand_demo_01` | any lane | 1 min | none |
| 2 | Edit `APP_LINEAGE_LABEL`, `APP_CHANNEL`, `APP_VERSION` (index.html:886–888); swap palette at `BLACK_CHROMA`/`OVERLAYS`; replace 2 icons + `manifest.webmanifest`; swap `vendor/handpiano-sample-packs/` for one soundpack | operator or Codex | **2–4h first time** | none |
| 3 | Deploy to the same host handpiano.com uses (Cloudflare Pages inferred from `_headers`) on a subdomain — `demo01.handpiano.com` costs $0 and needs no new domain | **operator** | 15 min | ⚠️ world-effect: publish |
| 4 | Record the exact diff as `brand.json` spec → hand to Codex to extract | sigrun_codex_gpt5.6sol | 3–4h | code lane |
| 5 | Demo #2 from the extracted config | Codex | 2–3h | — |

**Why a subdomain and not a new domain:** $0, no purchase decision, no DNS
wait, and it demonstrates the exact thing you are selling — *"here is your brand
on it, delivered in a day."* A buyer does not care that it is a subdomain. They
care that it took a day.

**Why an invented brand and not a real one:** a real brand's logo on an
unsolicited demo is a legal and reputational risk you do not need. Invent
"Meridian Sound Lab" or similar and say plainly on the page that it is a
capability demo.

- **FALSIFIER (§3.4):** if step 2 takes more than 6 hours, the config surface is
  more entangled than §3.1 measured, `brand.json` extraction must come *first*,
  and the week-move becomes step 4 instead of step 2.
- **cost_of_delay: HIGH.** Every week without a second URL, the pitch is "I have
  one app" instead of "I have a factory." The second URL is the entire
  difference between a portfolio and a product line, and it costs one afternoon.

---

# §4 · PLUGINS AND MARKETPLACES — where a solo dev can actually list

Rated for **your** fit: spatial + gesture + real-time web + agent swarm.
`TTFL` = time to first listing. Revenue figures are platform-wide, not promises.

| marketplace | fit for you | revenue reality | TTFL | competition | verdict |
|---|---|---|---|---|---|
| **Gumroad** | ⭐⭐⭐ — sell the *gesture app template* itself: source + `brand.json` + docs | median creator **$72/mo**; **<5% clear $1,000/mo**; **44% of products earn exactly $0**; Software Development is the top category at **$65.8M / $60,814 per product**; first $100 takes **6–12 months without an audience** [S] | **1 day** | high, but Software Dev is where the money is | ✅ **DO IT — as a $0-effort byproduct, not a plan.** List the template you build in §3.4 anyway. Zero marginal cost. Do not forecast income from it. |
| **Chrome Web Store** | ⭐⭐⭐ — a webcam-gesture *browser control* extension is a genuinely differentiated listing | **median extension has 18 users**; **70.4% have ≤100 users**; but 10K+ users on freemium → **$2–10K/mo**, 100K+ → **$10–50K/mo**; AI-extension market ~$2.3B (2025) [S] | 1–2 wk (review) | very high volume, thin at *gesture* | ⚠️ **PARK.** Real ceiling, real differentiation, but distribution is a marketing problem you do not have capacity for. Revisit after income exists. |
| **Agent-skill marketplaces** (Agensi, Agent37) | ⭐⭐ — HFO's discipline (receipts, gates, failure classes) is packageable as SKILL.md | Agensi: creators keep **70%**, Stripe Connect payout, 8-point security scan per listing [S]. Market is new; no median data exists yet | **1–3 days** | **LOW — the market is months old** | ✅ **DO IT — highest novelty-per-hour on the board.** See §5 week-move #3. |
| **Unity Asset Store** | ⭐⭐ — a gesture-input package is a real asset category | publishers keep **70%**; top publishers ~$1M/yr, **most under $1,000/mo**; sweet spot is **$50–200 specialized tools** [S] | 2–4 wk (review) | high | ⛔ **NO.** Your stack is web (MediaPipe/Three.js), not Unity. Porting is weeks. Wrong tool for your hands. |
| **Figma Community / plugins** | ⭐ | Figma is currently approving new creators for paid plugins via built-in payments; **no aggregate developer revenue data exists** [S] | 1–2 wk | high | ⛔ **NO.** No gesture story. Off-skill. |
| **GitHub Marketplace (Actions/Apps)** | ⭐⭐ | free listing; monetization is thin for Actions | days | med | ⚠️ credibility asset only |
| **npm / PyPI** | ⭐⭐ | $0 direct. Monetizes as *proof of expertise* in a proposal | hours | n/a | ✅ **publish the MediaPipe worker module.** It is already isolated (§3.1). $0 income, real credibility, ~1h. |
| **Shopify App Store** | ⭐⭐ — "try-on / spatial preview" is a real e-comm category | app-store economics favour incumbents; review is slow | 4–8 wk | high | 🅿️ PARK — plausible but a quarter+ of work |
| **Product Hunt** | ⭐⭐⭐ | not a marketplace — a **visibility event**. Free. | 1 day | n/a | ✅ use it to launch the §3.4 demo. $0. |
| **Cloudflare / Vercel template galleries** | ⭐⭐⭐ | $0 direct; **exactly where your buyers browse** | 1 day | low at *gesture* | ✅ **DO IT** — a "webcam-gesture PWA starter" template is a thin, on-brand listing |

## §4.1 · The uncomfortable finding, stated plainly

**Every marketplace on this list is a lottery with a median payout near zero.**
Gumroad: median $72/mo, 44% earn $0, 99.5% of revenue to the top 1%. Chrome:
median 18 users. Unity: most publishers under $1,000/mo. These are not
pessimistic readings — they are the platforms' own distributions.

> ### **Marketplaces are a distribution channel for a product that already has demand. They are not a demand-generation channel. Listing on one does not create a buyer; it makes you findable to a buyer who is already looking.**

The correct use of §4 is therefore: **list as a $0-marginal-cost byproduct of
work you were doing anyway, and never as a plan.** Every ✅ above is something
that takes ≤1 day and reuses an artifact §3 or §5 already produces. The one
genuine exception — where the market is thin enough that being early is worth
real money — is the **agent-skill marketplace**, because it is months old.

---

# §5 · INCOME ROADMAP — against capabilities you have actually proven

**Proven, verified, yours:** gesture/hand tracking that ships · a live HTTP-200
public app · a deployable PWA with an external config surface and a documented
injection ABI · a $0 near-frontier compute mesh you built · multi-agent
architecture · second-order cybernetics as a working frame · **one prior paying
client on a live payment rail.**

**Roster correction applied throughout:** owners below come from
`SUBSTRATE_ROSTER.md` v0_2. My prior §8.1 lane table assigned funding lanes to
**Fenrir** (not an agent — it is the wolf in the Gleipnir metaphor) and
**Nidhöggr** (unratified proposal), and named **Ratatoskr** as the cloud apex
when canon says **reginleif**. Those assignments are void. Corrected here.

---

## 🥇 TOP-3 THIS WEEK

### W1 — Message every human who has ever paid you, or nearly did

- **First move:** one list, one message each, today. No new artifact required.
- **Owner:** **operator** (send is world-effect). Olrún drafts variants for
  one-click approval.
- **Cost:** 30 minutes. $0.
- **Income range:** $0–3,000. It is the only lane in this document that has
  *ever* produced a dollar for you.
- **FALSIFIER:** 10 messages, zero replies in 10 days ⇒ the warm network is
  cold and every "reactivate" recommendation in HFO canon should be downgraded
  permanently, not retried.
- **cost_of_delay: EXTREME.** Highest EV/hour on the board, requires no agent
  output, and it has now been the #1 recommendation across two consecutive
  canon documents without being executed. **That non-execution is itself the
  most decision-relevant fact in this file.**

### W2 — Reposition the profile, then ship the second URL

- **First move:** rewrite the Upwork headline to **"Interactive spatial web /
  real-time hand tracking — Three.js · MediaPipe · WebGL"** (never "computer
  vision": $25–50/hr vs $50–90/hr for identical work), portfolio →
  handpiano.com. Then execute §3.4 steps 1–3 and add the second URL.
- **Owner:** **reginleif** (ChatGPT cloud apex) drafts 3 headline variants +
  first 10 proposals to seed-approval state; **operator** sends and deploys.
- **Cost:** ~4h + connects. $0 new spend.
- **Income range:** $500–4,000 for a first contract, 3–6 weeks out.
- **FALSIFIER:** 20 proposals into spatial/interactive categories by 2026-08-15,
  zero replies ⇒ the constraint is the 0-rating profile, not the category, and
  the fix is one deliberately underpriced fixed-price job to buy a rating.
- **cost_of_delay: HIGH** and expiring — every proposal sent into
  `agentic-ai-developers` before the rewrite buys near-zero visibility.

### W3 — Publish one agent skill to a skills marketplace

- **First move:** package **one** HFO discipline as a SKILL.md — the strongest
  candidate is the **receipt-gate / no-DONE-without-receipt pattern**, because
  it is a named, self-contained behaviour that solves a problem every agent
  buyer currently has (agents reporting false success). List on Agensi (70%
  creator share, Stripe Connect, 8-point scan) [S].
- **Owner:** **Sigrún** authors (it is a document, which is what this lane is
  for); **huginn+muninn** verify it does not leak forge internals; **operator**
  clicks publish.
- **Cost:** ~3h. $0.
- **Income range:** $0–500/mo. **Low expected value, but the highest
  information-per-hour on the board** — it is a real market test of "can HFO's
  institutional design be sold" for three hours instead of a quarter.
- **FALSIFIER:** listed for 30 days, zero sales *and* zero page views ⇒ the
  "package and sell the system" thesis has no buyer at the skill granularity,
  and should be retired rather than re-packaged.
- **cost_of_delay: MEDIUM-HIGH.** The market is months old. Thin categories
  close.

---

## 🥈 TOP-3 THIS MONTH

### M1 — 20 named humans at 20 experiential / exhibit / kiosk agencies

- **Why agencies, not brands:** an agency buys one $3–8K module into a deal they
  already closed. A brand requires you to sell the whole $40–80K install.
- **First move:** fix the recorded defect — **44 companies, 0 named humans.**
  Enrichment to named contacts *is* the first move; the list is worthless
  without it.
- **Owner:** **garmr** (Codex apex, owns `2026-08_cold_outreach_launch`) queues
  named contacts + drafted messages; **operator** sends.
- **Cost:** ~6h agent + ~1h operator. $0.
- **Income range:** $3,000–8,000 per branded module.
- **FALSIFIER:** 20 agencies contacted, zero discovery calls in 30 days ⇒ the
  subcontract thesis is wrong. Next test is **one free install for a local
  venue** to manufacture the missing reference — not more agencies.
- **cost_of_delay: MEDIUM.** Q4 retail/trade-show activations are specified in
  late summer. Miss the window and the clock is a quarter, not a month.

### M2 — Adopt a durable harness. Do not build one.

- **The strife this cures:** *"reinventing instead of adopting"* + *"agents
  self-stop."* You have 133 generations of bespoke loop machinery and **one**
  substrate that loops 9h+ (Codex). That is the empirical answer to which
  approach works.
- **First move:** take the ONE loop that already works — the Codex 9h+ goal
  loop — and **document what makes it durable**, before adopting anything. Then
  adopt a named harness (LangGraph is the obvious candidate) for *one* lane
  only, as a bake-off against the Codex loop. **Do not migrate the fleet.**
- **Owner:** **sigrun_codex_gpt5.6sol** (Codex apex — the only lane that writes
  code and the only one that has loop durability to explain).
- **Cost:** ~8h. $0.
- **Income range:** $0 direct. This is the multiplier on everything else.
- **FALSIFIER:** if the adopted harness does not produce a loop that runs longer
  and produces more artifacts than the existing Codex loop within 2 weeks, the
  harness is not the constraint — **prompt scope is** — and the correct fix is
  tighter goal scoping, which is free.
- **cost_of_delay: MEDIUM.** Compounds, but only behind W1/W2/M1.

### M3 — Unblock or sunset the $0 mesh, with a kill date

- **First move:** run the diagnostic that was already written and never run.
- **Owner:** **surtr** ($0-mesh apex, ⛔ STUCK) — supported by
  **TBD_APEX_SONNET5**'s 7 valkyries, who are the largest idle labour pool you
  have.
- **Cost:** ~4h. $0.
- **Kill date: 2026-08-15.** If the mesh is not running by then, sunset the
  lane and reassign.
- **Income range:** $0 direct — this is capacity, not revenue.
- **FALSIFIER:** mesh unblocked and running for 7 days without producing a
  single artifact a stranger could see ⇒ the constraint was never compute, it
  was direction, and more compute makes it worse.
- **cost_of_delay: LOW-MEDIUM.** It is a force multiplier with no product
  behind it yet. **Explicitly ranked below M1 for that reason** — you named
  income as the binding constraint, and compute is not income.

---

## 🥉 TOP-3 THIS QUARTER

### Q1 — Become the named gesture subcontractor on Standard-tier installs

$12–40K software share of $40–80K installs, plus $5–30K/yr content refresh.
Requires M1's agency relationship + one shipped demo. **Owner:** garmr (channel)
+ Codex (delivery). **P(≥$10K contracted by 2026-11-01): ~15%, LOW confidence.**
**FALSIFIER:** first agency produces exactly one job and no second ⇒ you are
overflow labour, not a specialist; reprice as day-rate and stop investing in the
relationship as a channel. **cost_of_delay: LOW now, HIGH beyond the quarter** —
23.8% CAGR means the specialist slot is being claimed right now.

### Q2 — Productize the reskin factory as a fixed-price offer

Once demos #2 and #3 land at ≤2h each, "branded gesture experience, delivered in
a week, $3–8K" becomes a *statement with receipts* instead of a hope. That
sentence is the product. **Owner:** Sigrún (offer copy) + Codex (throughput
receipts) + garmr (channel). **FALSIFIER:** if demo #3 still takes >4h, the
factory claim is false — sell hours, not a factory. **cost_of_delay: LOW.**

### Q3 — One paid pilot of the swarm as a delivery capability, never as a product

£50–80/hr agentic-workflow implementation for an SMB, where HFO is *why you are
fast*, not *what you sell*. **Stigmergy, quorum, and MAP-Elites go in your
margin, never in your offer copy** — pitching them loses an SMB deal in one
sentence. **Owner:** operator (sales) + whole fleet (delivery). **FALSIFIER:**
if a prospect asks what the architecture is and the deal dies on the answer, the
capability is not sellable at SMB scale at all. **cost_of_delay: LOW.**

---

## §5.4 · SHORT-TERM STOPGAP — the bridge, stated without euphemism

You named this yourself: *"what I need is maybe even recruiters or a job or
something in the short term."* That is a correct read of your own situation and
I am not going to talk you out of it.

> **A job is not a failure of the system. It is the funding round.** You said it
> plainly: *"if I had more money then this would all be solved essentially."*
> Runway is the binding constraint on everything in §5. A salary buys 12 months
> of it in one move — more than every income lane in this document combined,
> at a far higher probability.

**Concrete first move, this week, 90 minutes:**

1. **One profile line, everywhere** (LinkedIn headline, Upwork, résumé):
   *"Interactive spatial web / real-time hand tracking — Three.js · MediaPipe ·
   WebGL · multi-agent systems."* Same 2× arbitrage as W2 — creative-tech and
   spatial-computing titles price above "computer vision" for identical work.
2. **handpiano.com is the portfolio, at the top, above everything else.** A live
   HTTP-200 gesture app outperforms any repo in a recruiter screen. It is the
   single strongest credential you own and it currently sits below your text.
3. **Contact 5 recruiters** in creative-tech / interactive-agency / AI-tooling.
   Not 50. Five, with a specific ask.
4. **Set an explicit decision date.** If no offer or contract by **2026-09-15**,
   widen to non-spatial contract work. A bridge with no deadline is a drift.

- **Owner:** operator. Olrún drafts the profile line variants and the recruiter
  message for one-click approval.
- **Cost:** 90 min. $0.
- **Income range:** the widest and the most probable on this page.
- **FALSIFIER:** 5 recruiters, zero screens in 3 weeks ⇒ the positioning is not
  the constraint, the market is, and the honest move is fastest-available
  contract work at whatever rate clears.
- **cost_of_delay: EXTREME.** Runway is the constraint on every other row in
  §5. Nothing here works from zero.

---

## §5.5 · HONEST FLAWS

- **W1 has been the #1 recommendation twice and has not been executed.** I am
  ranking it #1 a third time. If it does not get executed this week, the honest
  conclusion is not that the ranking is wrong — it is that *recommending* is not
  the mechanism, and the swarm's job is to make the send one click, not to rank
  it again.
- **Every probability in §5 is calibrated judgment, not measurement.** Same
  limitation as prior canon; the confidence labels are the honest part.
- **§4's marketplace figures are search-snippet grade [S], vendor-published,
  and systematically biased upward.** I lead with the *medians* rather than the
  headline numbers for exactly that reason.
- **`four_finger_piano` and `table_tennis` could not be located.** The
  four-app portfolio is, as far as this session can verify, one app plus an
  uninspected sibling plus an archive. I would rather report that than plan
  around assets I cannot see.
- **§5 recommends a job.** That sits uneasily beside a document about building
  an autonomous swarm, and I am stating it anyway because runway is the actual
  binding constraint and every other row is downstream of it.
- **This document is another artifact, and Bias 1 applies to it.** Its defence:
  W1 requires none of my output, W2 is built from code you wrote, and W3 is the
  only row that consumes my output — which is why it is ranked third and framed
  as an information purchase rather than an income lane.

---

*FALSIFIER (whole document):* if by 2026-09-01 the second URL is live, 20 named
agency humans are contacted, and 5 recruiters are messaged — and none of the
three produces a reply — then the constraint is not positioning, not channel,
and not production; it is market access, and the honest next move is to buy
access (paid job boards, paid intros, an agency-side referral fee) rather than
to optimise further ·
*cost_of_delay:* W1 and §5.4 both expire against runway, which is the only clock
that matters ·
*leverage_level_meadows:* L4 self-organization (§3.4 factory) + L2 goals (§5.4
bridge) ·
*domain_cynefin:* Complex

*Réttu hönd, eigi spyr. Standa.*

---

## Sources

- [insightraider — Gumroad statistics 2026](https://insightraider.com/en/data/gumroad-statistics-2026) · [State of Gumroad 2026](https://insightraider.com/en/state-of-gumroad-2026)
- [Chrome Goldmine — extension revenue benchmarks 2026](https://chromegoldmine.com/blog/chrome-extension-monetization/chrome-extension-revenue-benchmarks/) · [Konabayev — extension monetization statistics 2026](https://konabayev.com/blog/extension-monetization-statistics-2026/) · [aboutchromebooks — Chrome extension ecosystem 2026](https://www.aboutchromebooks.com/chrome-extension-ecosystem/)
- [Agensi — monetizing SKILL.md skills, 2026](https://www.agensi.io/learn/how-to-monetize-skill-md-skills-developer-guide-2026) · [Agent37 — Claude skills marketplace](https://www.agent37.com/blog/claude-skills-marketplace)
- [generalistprogrammer — Unity Asset Store selling/revenue guide 2026](https://generalistprogrammer.com/tutorials/unity-asset-store-selling-guide-revenue) · [Unity — Asset Store package revenue](https://docs.unity3d.com/6000.3/Documentation/Manual/asset-store-revenue.html)
- [Dodo Payments — monetizing Figma plugins 2026](https://dodopayments.com/blogs/sell-figma-plugins)
- Install-budget, gesture-market, and freelance-rate figures are carried from `SIGRUN_SPATIAL_GESTURE_SWARM_INCOME_CASE_STUDIES_20260801.md` §2–§3, which cites them individually.

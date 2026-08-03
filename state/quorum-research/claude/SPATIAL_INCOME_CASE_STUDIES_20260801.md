```yaml
schema_id: hfo.quorum_research.internal.v0_1
family: anthropic
model: sonnet-5
source: capsules/research/SPATIAL_INCOME_CASE_STUDIES_20260801.md
consolidated_utc: 2026-08-02T01:15Z
clock_source: host_read
```

---

# Spatial / Gesture / Hand-Tracking Income Case Studies — 2026-08-01

Researched for: operator, who has two LIVE proven demos (`handpiano.com`,
`demo01-handpiano.pages.dev` — hand-cursor from injected landmarks) but zero
emails sent, zero offers sent, no production software shipped. Question:
what's the well-worn path for a solo dev in spatial/gesture/camera-input to
make money this month/quarter?

**Honest headline finding: there is no well-documented case of a solo dev
making a living purely from a webcam-gesture-control consumer app.** Every
case below is either (a) a small solo tool with undisclosed/likely-small
revenue, (b) a funded multi-person team, or (c) a warning case about the
native-app-store path failing. The one well-worn path that IS proven at scale
in 2026 is generic indie-SaaS build-in-public — not spatial-specific — and the
honest recommendation below routes operator through that mechanic using his
existing spatial tech, not toward chasing a VR/AR app-store hit.

Full structured data: `state/research/spatial_income_cases_20260801.jsonl`
(8 rows, schema documented in that file).

---

## Top 5 Case Studies Most Relevant to Operator's Stack

### 1. Fun With Computer Vision — content-first, webcam-only, solo (HIGH relevance)
[funwithcomputervision.com](https://www.funwithcomputervision.com/)
- Solo creator, runs entirely on a regular laptop + webcam — **identical hardware assumption to operator's demos.**
- Monetizes teaching (code + tutorials), not a finished product: $10 lifetime / $99 lifetime-with-support tiers.
- Distribution channel: YouTube content, 10M+ cited views, is the funnel.
- **Directly copyable this week:** operator already has 2 working webcam-landmark demos. Recording a "how I built hand-cursor input with injected MediaPipe landmarks" video/post and selling the code + a walkthrough is a near-zero-build-cost repeat of this exact model.
- **Cannot copy:** the 10M-view audience took years of consistent posting to build. Operator has no existing audience — the funnel has to be built from zero, which is a distribution problem, not a tech problem.

### 2. Zesture (Show HN, 2020) — solo, one-time-purchase desktop utility (HIGH relevance)
[news.ycombinator.com/item?id=24098874](https://news.ycombinator.com/item?id=24098874)
- Solo dev, webcam hand-gesture control for media/slides/video apps, $9.99 one-time.
- Distribution: single Show HN post (34 points, 12 comments) — the entire go-to-market was "post it and see."
- **Directly copyable:** operator's hand-cursor demo is Show-HN-shaped right now. A Show HN + Product Hunt post costs nothing and has a known playbook (title format, timing, engaging in comments).
- **Cannot copy:** no evidence this ever became real income — it's proof a launch is *possible*, not proof of a revenue outcome. Treat as a distribution tactic, not a business model.

### 3. Gesture Present (itch.io) — solo, privacy-framed niche tool (HIGH relevance)
[hussaynzaidi.itch.io/gesturepresent](https://hussaynzaidi.itch.io/gesturepresent)
- Solo, webcam-only slide control, "pay what you want, $9 floor," local-processing-only as the trust pitch.
- **Directly copyable:** the privacy angle ("nothing leaves your machine") is a message operator can reuse verbatim for handpiano/demo01 — it costs nothing and differentiates from cloud-CV competitors.
- **Cannot copy:** itch.io traffic for non-game tools is thin; this is a listing-exists proof, not a revenue proof.

### 4. Qonqur — webcam + Apple Vision Pro, subscription (HIGH relevance, unverified team size)
[apps.apple.com/us/app/qonqur](https://apps.apple.com/us/app/qonqur/id6739890783)
- One gesture engine shipped to **both** webcam and Vision Pro — same "one input layer, many surfaces" pattern operator is already using (inject landmarks → drive cursor across contexts).
- Chose subscription ($7/mo) over one-time purchase: a productivity bet, not a novelty-toy bet.
- **Directly copyable:** the platform-agnostic-input architecture decision. Operator's landmark-injection approach is structurally the same move.
- **Cannot copy:** could not verify this is actually solo (LLC-registered, no founder name surfaced) or that it has real subscribers. Treat the architecture lesson as solid; treat the business proof as unconfirmed.

### 5. Neural Lab / AirTouch — 2-founder + 9-employee, funded, enterprise licensing (MEDIUM relevance)
[neural-lab.com](https://neural-lab.com/)
- Co-founded by Sherry Chang + Oliver Chen (CV/DNN research background), CES 2025 press coverage, Crunchbase/PitchBook-profiled funding.
- **What operator cannot copy:** a technical co-founder pair, VC funding, and an enterprise B2B sales motion. This case exists to draw an honest boundary — operator is not going to replicate a 9-person funded startup solo this quarter.
- **What's still useful:** earned press (Engadget, Cybernews) as a customer-acquisition channel instead of paid ads is replicable at small scale — a well-made demo video pitched to a tech journalist costs nothing but time.

---

## Failure Modes Across All Cases (survivorship-bias check)

For every "success," what did the founder have that operator doesn't?

- **Fun With Computer Vision** had YEARS of prior content-building before monetizing — operator is starting the audience from zero today.
- **Neural Lab** had a technical co-founder pair AND venture funding — operator has neither.
- **Qonqur / Zesture / Gesture Present** have **no confirmed revenue at all** in any source found — they prove a product *can ship*, not that it *makes money*. Believing these are quietly profitable would be exactly the fabrication this research is required to avoid.
- **Apple Vision Pro App Store (general)** is an explicit warning case: 6 months of solo dev time can net under $25K gross before Apple's 30% cut, against an installed base still under 500K units. This is the "don't do this" path, cited on purpose.
- **Meta Quest / Horizon Store** requires a headset build + $20-40 price tolerance — a packaging and platform shift operator hasn't made, plus a 30% platform commission.
- **Cross-cutting pattern:** every spatial/gesture case with a confirmed dollar figure is either a funded multi-person company (Neural Lab) or a generic non-spatial SaaS founder (Pieter Levels) whose lesson is "build in public," not "spatial computing pays." **Nobody found in this search is living solely off a solo webcam-gesture consumer app in 2026.**

## The ONE Well-Worn Path to Recommend

**Content-first, build-in-public, sell the teaching + the code — not the finished app — using the demos operator already has.**

This is the Fun With Computer Vision model (webcam-only, zero extra hardware, matches operator's stack exactly) crossed with the build-in-public distribution mechanic that is the single most-repeated 2026 success pattern found (Pieter Levels and the broader indie-hacker data: revenue/build screenshots ARE the marketing channel). Concretely:

1. Post `handpiano.com` / `demo01-handpiano.pages.dev` publicly this week as a Show HN + Product Hunt launch (Zesture's exact playbook — costs nothing, known format).
2. Follow with one build-in-public post per shipped increment (what changed, what broke, what's next) — this is the audience-building step every case above that had real evidence of income (Fun With Computer Vision, Pieter Levels) actually did, and the step operator has explicitly not done yet ("built privately").
3. Monetize the teaching/code path (lifetime-access tiers like Fun With Computer Vision's $10/$99) as the near-term revenue test, in parallel with — not instead of — outreach to 1-2 potential enterprise/demo clients (Qonqur's productivity angle, Neural Lab's earned-press angle) since enterprise seats are the only dollar figures in this research that are large enough to matter.

**Honest flaw in this recommendation:** none of the sources confirm this path has actually produced sustainable income for anyone doing exactly what operator does (solo, webcam-only, no funding, no prior audience). It is the *least unproven* path among the options found, not a proven one. Truthful-red: this is the best available evidence, not a guarantee.

---
*clock_source: host_read · researched 2026-08-01 by research_valkyrie_spatial*

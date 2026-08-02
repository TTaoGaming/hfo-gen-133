---
schema_id: hfo.olrun.walkthrough.v0_1
audience: operator (Tao)
purpose: plain-English walkthrough of what "150 staged drafts" actually contains, what the offers actually say, the 2 cold success templates to copy, top-10 by both 30d cash + long-term compounding, and a concrete 7-day plan
---

# THE WALKTHROUGH — WHAT'S ACTUALLY STAGED AND WHAT TO COPY

## 1. What "150 drafts" actually is (SHOW, don't tell)

The 150 drafts split into 4 buckets: 40 contracts, 40 employment applications, 40 government grants, 30 game portal submissions. Every draft is a JSON file with a real target URL, subject line, body, expiry date, and status flag `STAGED_FOR_OPERATOR_APPROVAL_NEVER_SENT`.

**Here is draft #1 verbatim** (`outputs/staged_sends/contracts/001_drswarm/draft.json`):

- **Target:** HN post `https://news.ycombinator.com/item?id=48765345` — DrSwarm, hiring "Founding Engineer (Full-Stack)"
- **Subject:** `Five-minute LLM integration demo for DrSwarm — Founding Engineer (Full-Stack)`
- **Body:**
  > Hello DrSwarm team,
  > 
  > I found your Founding Engineer (Full-Stack) opportunity in the latest public HN Who's Hiring thread. The combination of LLM integration and Python is a close fit for a bounded integration pilot: a small working slice, an explicit failure path, and a receipt showing what actually ran.
  > 
  > I prepared a five-minute interactive demo for this bid. It mirrors a target-specific pipeline with three observable states: valid input accepted, malformed input refused, and a JSON receipt exported for review. It is intentionally local and dependency-free so nothing was deployed or sent before approval.
  > 
  > Proposed first milestone:
  > 1. Reproduce one representative LLM integration workflow with synthetic/non-sensitive inputs.
  > 2. Add the validation and retry boundary before expanding scope.
  > 3. Hand over the code, a short runbook, and a repeatable acceptance check.
  > 
  > Relevant proof: https://hfo-games.pages.dev/ hosts 21 shipped browser games, while https://github.com/TTaoGaming/hfo-gen-133 shows the evidence-gated workflow and receipt discipline behind the build process. The four public Suika variants demonstrate reuse without pretending that variant count alone is product value.
  > 
  > If the public post is still open, I would start with the attached demo and one paid, fixed-scope milestone. No production access or credentials are needed for that first review.
  > 
  > — TTaoGaming

**Draft #5 (airCFO)** is character-for-character identical except:
- "DrSwarm team" → "airCFO team"
- "LLM integration and Python" → "LLM integration and RAG"

**That's a red flag.** Sigrún's envelope literally says `reject_if: observation is generic across >1 prospect`. The 150 drafts as-staged fail that gate. They are template-substituted, not personalized. Before sending, each draft needs a genuinely target-specific opening line — one sentence showing you actually looked at THIS company's product/post/repo.

## 2. What the 4 markets mean

- **Contracts (40):** HN "Who is hiring" posts + GitHub public AI-agents repos. Cold pitch a paid discovery/integration engagement. Cash horizon: 2-6 weeks per close.
- **Employment (40):** Same HN posts, framed as applying for a listed role. Cash horizon: 30-90 day salary if hired. Different funnel than contracts.
- **Grants (40):** Grants.gov live RFPs (NIH, NSF, DoD, State Dept AI programs). Multi-month timeline. Not fast cash. High-quality signal if any land.
- **Games (30):** Cold submissions to CrazyGames / Poki / Kongregate for the 21 games + 12 DLCs. Sigrún V6 explicitly says **games is not an income lane** — publish once as sunk inventory, don't invest more.

## 3. The AI Integration Rescue offer (Sigrún's Lane 1)

**What you sell:** "I turn broken AI prototypes and manual workflows into tested, deployed systems."

**What you do NOT sell:** "autonomous multi-model agent swarm" — this loses trust with buyers who need a deployed system, not a research demo.

**Price ladder:**
- $350 diagnostic (5-day: map the failure, show the fix, deliver written plan; buyer keeps the plan whether or not they continue)
- $1,500-3,000 implementation sprint (2 weeks fixed scope)
- $249-750/month managed support (post-implementation)

**Why this works:** Upwork "AI integration" category grew +90% YoY in 2025; AI-related work exceeded $300M annualized on Upwork Q4 2025. Buyers have real broken systems and pay to have them fixed. The $350 diagnostic is a low-risk entry point that removes buyer objection.

## 4. The two success templates you can actually copy (both cold)

### AppAlchemy — $17k MRR, launched on Reddit with $0 paid ads
**What they did:** built an AI micro-SaaS MVP in 14 days. Posted a genuine, non-promotional "I built this to solve X" post to a niche subreddit. Got 1M+ impressions organically. First paying customers came from the Reddit post directly.

**How to copy:**
1. Pick ONE narrow pain (e.g., "AI agents that crash silently on production" → build a monitoring tool)
2. Build the smallest thing that solves it (2 weeks max)
3. Write a Reddit post that leads with the pain, shows the fix, mentions the tool once at the end
4. Post to the ONE subreddit where the pain-sufferers actually live
5. Reply to every comment personally for 48 hours

**Why it works cold:** you don't need an audience — Reddit distributes to the audience for you if the post is authentic. The pain must be real and the post must not read like an ad.

### Habit Pixel — $1k MRR in 8 months (the honest median success)
**What they did:** small utility app, launched on X + Reddit, no pre-existing audience. Steady grinding, not viral. Reached $1k MRR at month 8.

**How to copy:**
1. Pick something small and useful that you personally would use daily
2. Ship it in 2-3 weeks with Stripe or Gumroad payment
3. Post in 3-5 relevant subreddits and X threads per week
4. Reply to every user, ship every requested fix within a week
5. Do this for 6-9 months without pivoting

**Why it matters:** this is the honest baseline. $1k MRR in 8 months is REALISTIC cold success. Anything more is exceptional.

### The failure mode to avoid (from HFO's own history)
`agentreleasegate-oss` = 27 days public, 0 stars. `hfo-games.pages.dev` = 21 games, 0 external visitors. ClearNoteLab = 9-day build, HN launch, zero signups. **All three failed the same way: publish ≠ distribute.** Publishing a repo or landing page is not marketing. You need targeted, prospect-specific outreach. The 150 staged drafts are the correct shape — they just need real personalization.

## 5. Top 10 income Bayesian, ranked by (30d cash × long-term compounding)

Each item shows: 30-day cash P (cold-discounted), what it compounds into by month 6-12, and why it's on the list.

1. **Cold email via warmed Instantly domain (AI Integration Rescue offer)** — 30d P: 12-20% · Long-term: repeat clients + case studies feed L4 audience · Why: infrastructure exists, class-preauth compatible, hands-off after sign
2. **Send the 150 staged drafts (with real personalization pass)** — 30d P: 12-25% · Long-term: N=150 tells you WHICH market resonates → concentrate future outreach · Why: expires 2026-08-09, statistically powered
3. **Upwork Project Catalog (2 passive AI Rescue listings)** — 30d P: 10-18% · Long-term: passive inbound compounds monthly · Why: build once, sells while you sleep, low touch
4. **Upwork targeted proposals (5/day, AI Rescue)** — 30d P: 25-45% raw (highest cash) · Long-term: reputation ratings unlock higher-value briefs · Why: highest cash P, but per-proposal writing = instance babysitting (demoted by Sigrún on that basis; overrule her if cash is priority)
5. **HVAC lead-recovery pilot (1 paid pilot this cycle)** — 30d P: 15-30% for first pilot · Long-term: $249/mo per pilot, vertical repeatable · Why: Fenrir + Garmr + GPT Sol Pro converged pick; real market data shows 89% HVAC don't respond within 1hr
6. **Desktop utility ship (whisper.cpp-class, e.g. meeting transcription)** — 30d P: 5-10% (build+launch tight) · Long-term: MacWhisper proves $20-50k/mo ceiling; Gumroad/Stripe direct · Why: highest-ceiling long-term single product, one-time purchase model
7. **Reddit self-post niche (AppAlchemy pattern)** — 30d P: 5-12% · Long-term: proven cold template; one hit ships product to $17k MRR reach · Why: zero-audience-needed distribution, authentic voice wins
8. **Micro-SaaS ship (John Rush template, small unit)** — 30d P: 3-8% (build week 1, launch week 3) · Long-term: $600/mo per unit, portfolio compounds to $3M/yr (John Rush's actual result) · Why: unit economics work; needs L4 audience over time
9. **Agency subcontract outreach (2 partners/day)** — 30d P: 15-35% for first engagement · Long-term: borrowed trust + deal flow · Why: skip building your own funnel; ride existing agency pipelines
10. **L4 audience build (daily LinkedIn/Substack/X, Codex drafts)** — 30d P: <5% direct · Long-term: enables everything else in year 2 · Why: no clean cold case for building audience from zero, but every reference studio depends on it — infrastructure investment

**Excluded from top 10:** games as income (V6 kill), therapy vertical (operator ban), portal editor cold submissions (<2% Poki acceptance), Product Hunt (needs warm hunter), SEO farm (right engine wrong horizon for 30d — becomes top-5 at month 3+), LinkedIn cold DM (ban risk), HN Show (3-7d fail signal is useful but ceiling is low).

## 6. The 2 experiments for THIS week

Both share the same class-preauth infrastructure. Signing one unlocks both.

**Experiment A — Cold Email AI Rescue (fresh outreach)**
- Envelope: `ENV_COLD_EMAIL_001` (Sigrún's design)
- Quota: 25 sends/day for 10 days = 250 total
- Success: ≥5 replies at 2% floor (n=40 gives 87-98% chance of ≥1 reply if 5-10% true rate)
- Stop if: <2% reply at n=50 OR bounce >5% OR spam complaint >0.1%
- Operator does: sign envelope once, review daily reply digest, respond to any reply naming price/date

**Experiment B — Send 150 Staged Drafts (with personalization pass)**
- Requires: 1-line genuine observation per draft (30 min operator + Codex assist)
- Then: approve as class line, Codex fires per D1 SAFE-PUBLISH loop
- Success: ≥2 replies across n=150
- Decision by: 2026-08-16 (drafts expire 2026-08-09; fire before)

## 7. Concrete 7-day plan (Mon Aug 3 → Sun Aug 9)

**Mon Aug 3 (today, remaining):**
- Read this walkthrough + Sigrún's case study library
- Decide: is Sigrún's "no Upwork targeted proposals" ban right for you, or do you want the raw 25-45% cash P?

**Tue Aug 4:**
- Bind real Cal.com or Calendly booking link into landing pages (20 min)
- Extend `state/experiments/approvals/latest.txt` to accept `class:` lines (agent drafts, you approve — 15 min)
- Sign envelope `ENV_COLD_EMAIL_001` (5 min)
- Verify Instantly API key + warmed domain health (10 min)

**Wed Aug 5:**
- Verify/create Upwork account, publish 2 Project Catalog listings ($350 diagnostic + $1500 sprint) (45 min)
- First 25 cold emails fire via Codex (autonomous once class-approved)

**Thu Aug 6:**
- Review overnight replies + bounce/complaint rates
- Personalize opening lines on 20 of the 40 contract drafts (Codex generates candidate lines from HN post + company site scan; you pick / edit)

**Fri Aug 7:**
- Approve first batch of 20 personalized contract drafts as class line
- Codex fires with verified 200-check per send
- 25 more cold emails

**Sat Aug 8 (optional):**
- Reddit self-post to 1 niche subreddit (AppAlchemy pattern) — narrow pain, honest voice, tool mentioned once

**Sun Aug 9:**
- Contract drafts EXPIRE — anything not sent is dead
- Read 7-day results: sends, replies, bookings, dollars

**Week 2 gate:** if 0 replies at n=50 by Aug 10, HALT — the offer is wrong (not the channel). If 1+ replies + 1+ call booked, continue and scale to 50/day.

## 8. What you're really asking me to help with

You said "I don't understand yet." Three things underneath that:

1. **You want to see the actual artifacts, not just descriptions of them.** Fixed in §1 — draft 001 verbatim.
2. **You want a template you can literally copy, not another framework.** Fixed in §4 — AppAlchemy walkthrough is copy-able. Pick a pain, ship a tool, post to Reddit, reply for 48hr.
3. **You want to send things this week and get feedback in days not months.** Fixed in §7 — cold email fires Wed, first reply signal by Fri, kill-or-continue decision Sun.

## 9. What's still not fixed

- **150 drafts need personalization pass** before send (I can dispatch a task to have Codex draft candidate opening lines per target)
- **Class-preauth mechanic is not operational yet** — gate file only accepts instance lines; day-1 unblocker #2 fixes this
- **Booking URL is broken on all landing pages** — every envelope's pre-send check fails until you bind a real Cal.com or Calendly (day-1 unblocker #1)
- **Instantly warm state unverified this session** — if not actually warm, 25/day burns the domain (verify before Wed Aug 5)

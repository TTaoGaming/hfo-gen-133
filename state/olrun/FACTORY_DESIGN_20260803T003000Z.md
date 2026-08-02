---
schema_id: hfo.olrun.factory_design.v0_1
callsign: olrun
generation: 133
authored_utc: 2026-08-03T00:30:00Z
clock_source: estimated (workspace bash unavailable)
purpose: honest factory-pattern design for shipping multiple micro-SaaS + desktop utilities per day using swarm compute; operator picked options 3+5+6+7+8+10 with abstract-factory framing
supersedes_partial: OPTIONS_EXPLAINED_20260803T000000Z.md
authority: operator has authorized factory pattern; Sigrún dispatched for target research in parallel
---

# FACTORY DESIGN — MICRO-SAAS + DESKTOP UTILITY PARALLEL SHIP

## §0 · Operator picks + framing (verbatim)

Options selected: **5 (desktop utility) + 6 (micro-SaaS) + 7 (Reddit) + 8 (audience) + 3 (agency subcontract) + 10 (Upwork Catalog)** — plus "anything else because it's not 1 tool per few weeks. we should be able to build multiple per day and launch. we have excess compute that is underutilized... just need good targets for abstract factory pattern."

**Constraint:** Claude + Codex + LiteLLM + multi-vendor available. Compute is not the bottleneck.

## §1 · Is multiple-products-per-day doable? Honest yes, with caveats

**YES on BUILD side.**
- Precedent: 21 games + 12 Suika DLC variants deployed via existing Codex pipelines
- Micro-SaaS unit = 200-500 lines of code + landing page + Stripe config = 2-6 hours of Codex work
- Desktop utility = 500-2000 lines + Gumroad listing + demo video = 6-24 hours
- Swarm can PARALLEL 5-10 build streams via LiteLLM + Codex loops
- Realistic build throughput: **5-15 products/day at MVP quality if templates are strong**

**NO on DISTRIBUTE side. This is the true bottleneck.**
- Reddit self-post cadence: roughly 1 authentic post per subreddit per few days before spam-filter or mod ban
- HN Show submission: 1 per artifact, and >2/day from same account looks like spam
- Cold email: 25-50/day per warmed domain (higher = burn the domain)
- Direct implication: **build 15/day OK, but only 2-5 can be actively promoted per week**

**Consequence:** ship at build-cadence, distribute at platform-tolerance-cadence. The unpromoted 10-13/day become part of a SEO + directory listing + passive Upwork Catalog + long-tail Google/GitHub search pool. That IS a strategy — John Rush ran 24 SaaS units with most compounding via SEO/directories, not per-unit launches.

## §2 · Abstract factory blueprint

Two factories with shared distribution pipeline.

### FACTORY A · MICRO-SAAS UNIT

Template (each unit inherits these):
```
STACK
  frontend: Cloudflare Pages (static or minimal React)
  backend: Cloudflare Workers + D1 (SQLite at edge) or KV
  payment: Stripe Checkout embed (single Stripe account, N products)
  auth: shared magic-link module (or none, if usage-based)
  analytics: Cloudflare Web Analytics (free, GDPR-clean)

STRUCTURE (every unit)
  /                    landing page (hero, problem, demo, pricing, FAQ, footer)
  /app                 the actual tool
  /pricing             checkout embed
  /docs                one-page usage guide
  /api                 (if applicable) minimal REST
  robots.txt + sitemap.xml   for SEO

DEPLOY
  domain: subdomain of factory root (toolname.agentreleasegate.com) OR unique .com per unit
  ci: git push → Cloudflare auto-deploy
  post-deploy: curl-verify 200 on 5 canonical URLs
  receipt: write chain-row to state/factory_ships/MICROSAAS_SHIPS.jsonl

VARIABLE SLOTS (what makes each unit different)
  - the ONE job it does (single verb: "monitors X", "generates Y", "tracks Z")
  - the pain (1-2 sentences)
  - the demo (30-second gif or embedded live tool)
  - the price ($9 / $19 / $29 / $49/mo tiers)
  - the ICP one-liner (who this is for)
```

**Estimated build time per unit:** 2-6 hours of Codex work if template is solid. First unit takes longer (template hardening); units 2-N are fast.

### FACTORY B · DESKTOP UTILITY

Template:
```
STACK OPTIONS (pick one per unit)
  option A: Tauri (Rust + web front) — small binary, cross-platform, fast
  option B: Electron — larger binary, richer ecosystem, more familiar
  option C: PWA-installable — no code-signing, no store, install from Chrome
  option D: single-binary CLI + web dashboard (for dev tools)

STRUCTURE
  README.md + LICENSE + install instructions
  landing page (Cloudflare Pages)
  Gumroad listing OR Stripe Checkout
  demo video (30-60 sec, screen recording + light narration)

DEPLOY
  binary: GitHub Releases OR direct download from CF Pages
  landing: Cloudflare Pages subdomain
  payment: Gumroad (fast setup, takes ~9%) OR Stripe Checkout (lower fees, more setup)
  receipt: chain-row to state/factory_ships/DESKTOP_SHIPS.jsonl

VARIABLE SLOTS
  - the tool (native app doing one thing)
  - the pain
  - the ICP
  - the price ($9 one-time, $29 one-time, $49 one-time, $9/mo, $19/mo)
  - the demo video content
```

**Estimated build time per unit:** 6-24 hours (native code + code signing if signed). PWA-installable path is fastest.

## §3 · Shared distribution pipeline (the real bottleneck)

**Tier 1 — active promoted launches (2-5 per week, requires operator voice):**
- Reddit AppAlchemy post to matched subreddit
- HN Show submission
- X thread from operator's account
- Cold email to 25 handpicked prospects

**Tier 2 — passive distribution (all ships get this automatically):**
- SEO-optimized landing page (targets 1-3 low-competition long-tail keywords)
- Submission to 20+ SaaS directories (BetaList, IndieHackers, SaaSHub, Product Hunt Ships, AlternativeTo, etc.)
- GitHub public repo with README + topics
- LinkedIn Product Page (auto-generated)
- Substack post appearing in weekly digest
- Sitemap + robots.txt for Google/Bing indexing

**Tier 3 — long-tail passive (surfaces over months):**
- Domain age + backlinks from directories compound
- SEO rankings on niche queries
- Word-of-mouth if any Tier 1 unit hits
- Cross-promotion within factory (footer links between related units)

**Rate limits (real, not theoretical):**
- Reddit: 1 substantive post per sub per 3-7 days without ban risk
- HN: 1-2 Show submissions per week from same account before rate limiting
- Cold email via Instantly: 25-50/day per warmed domain (higher burns)
- LinkedIn: ~10 outbound connect + DM per day before restriction
- Product Hunt: 1 launch per product with strict quality bar
- Twitter/X: unlimited but engagement dies past 3-5/day

## §4 · What Sigrún needs to research (dispatched in parallel)

Ask: **"top 30 micro-SaaS targets + top 20 desktop utility targets that (a) match Cloudflare + Stripe stack (b) have measurable cold demand signal (c) can be built in <8hr by swarm (d) have ceiling >$500/mo per unit"**

For each target, deliver:
- 1-line pain
- 1-line existing solutions (or "none")
- Distribution channel (which subreddit / marketplace / directory)
- Build effort estimate
- Price signal
- ICP tag

Output shape: 50 rows in a JSON or MD table, ranked by (cold-demand × build-ease × per-unit-ceiling). Target completion: overnight (Sigrún cook time ~60-90 min if Codex parallel).

## §5 · Realistic launch cadence for THIS week

Tonight (2026-08-02 late) + Monday (Aug 3):
- Sigrún research target list (60-90 min)
- Operator + Olrún pick 5-10 units from the list
- Build factory template hardening (Cloudflare Pages boilerplate + Stripe Checkout + auth module + landing page starter)

Tuesday (Aug 4):
- Build 3 micro-SaaS MVPs in parallel (Codex streams)
- Deploy to subdomains of `agentreleasegate.com`
- All 3 get Tier 2 passive distribution automatically
- Operator picks 1 for Tier 1 active launch (Reddit + HN Show + cold email 25) later this week

Wednesday-Friday (Aug 5-7):
- Build 3-5 more micro-SaaS + 1 desktop utility MVP each day
- Continue Tier 2 automatic distribution
- Fire Tier 1 active launch for 1 winner per day (Reddit or HN, alternating)

Saturday-Sunday (Aug 8-9):
- Review week-1 data: which units got Tier 1 traction, which got Tier 2 slow trickle
- Kill units with 0 signal after 5-7 days
- Concentrate operator time on 1-2 breakout candidates

**Realistic week-1 ship count:** 12-25 units deployed, 3-5 actively launched, 0-3 that get meaningful signal.

**Realistic week-1 revenue:** $0-500. Most factory ships have 0 conversion in first week. Portfolio math needs 4-8 weeks to signal.

## §6 · Infrastructure prereqs (block factory ship if missing)

| # | prereq | status | who fixes |
|---|---|---|---|
| 1 | Cloudflare Pages account + API token (for CI deploy) | operator already has | operator confirm |
| 2 | Stripe account (live mode or test) + API keys | unknown status | operator verify |
| 3 | Gumroad account (for desktop utility payments) | unknown | operator confirm/create |
| 4 | Warmed Instantly domain (for Tier 1 cold email) | ⭐ **exists, unused** — `tryagentreleasegate.com` | operator sign envelope |
| 5 | Reddit account with karma/history in relevant subs | ⭐ **critical** — operator's account state? | operator confirm karma |
| 6 | HN account | operator has? | operator confirm |
| 7 | Real Cal.com or Calendly booking link | ⭐ **currently broken on all landing pages** | operator create + bind |
| 8 | Factory template repos on GitHub | not built yet | swarm builds this week |
| 9 | Directory submission list (20+ SaaS directories with URLs) | swarm has partial | swarm completes |
| 10 | State log for factory ships (chain-row append) | swarm can bootstrap | swarm bootstraps |

**Sigrún should validate items 5 + 6 before we commit to Reddit AppAlchemy launches.** If operator has 0 Reddit karma, that changes the distribution playbook — new accounts get shadow-banned on many subs.

## §7 · Options 3 + 8 + 10 in the factory context

Operator also picked 3 (Agency subcontract) + 8 (Audience build) + 10 (Upwork Catalog). These run in parallel:

- **Option 3 (Agency subcontract):** the factory's 20+ shipped units become PROOF for agency outreach. "We can ship a bespoke tool in a week — here are 20 we already shipped." Agency outreach launches week 2.
- **Option 8 (Audience daily posts):** each factory ship becomes a build-log post. Substack/LinkedIn/X posts write themselves from chain-rows. Compounds over 6-12 months.
- **Option 10 (Upwork Catalog):** 2 listings — "$1500 custom internal AI tool built to spec in 1 week" + "$350 AI diagnostic". Factory templates make the $1500 listing profitable because your build time is <8 hours per unit.

## §8 · Honest bottlenecks + failure modes

1. **Distribution is the ceiling, not build.** If you ship 100 units and actively launch 5, only those 5 get first-week signal. The other 95 rely on slow SEO/directory compound (months).
2. **Reddit karma matters.** New accounts get shadow-banned in tech subs. Verify operator's Reddit history before AppAlchemy strategy.
3. **Support burden multiplies.** Even $19/mo micro-SaaS gets 1-3 support emails per customer per month. 20 customers = 20-60 emails.
4. **Brand dilution risk.** Shipping 20 half-baked tools under one root domain damages perception of ALL. Quality bar: each unit must be feature-complete, not "MVP-crap".
5. **Payment plumbing bugs.** Stripe test-mode passes ≠ live mode passes. Each unit needs a test purchase before promotion.
6. **Legal exposure.** 20 SaaS = 20 terms-of-service + 20 privacy policies. Template these hard, or one lawsuit costs more than all combined revenue.

## §9 · What Sigrún is being asked to lock

The mandate to Sigrún (dispatched):
- Ratify or overrule the factory pattern approach
- Deliver 30 micro-SaaS + 20 desktop utility target list (ranked)
- Confirm 5-10 unit picks for week-1 build
- Confirm launch cadence (which units get Tier 1 promoted, which get Tier 2 only)
- Ratify the class-preauth envelope shape for automated factory ships (build + deploy + Tier 2 distribute WITHOUT operator per-instance approval; Tier 1 launches still require operator sign per-unit)

## §10 · Next steps (parallel)

**Right now:**
- Sigrún cooking research (60-90 min)
- Operator verifies infrastructure prereqs 1-6 (30 min)
- Olrún drafts factory template repo structure (30 min)

**Tonight if Sigrún lands in time:**
- Pick 5-10 targets from her list
- Start factory template hardening

**Tuesday Aug 4 morning:**
- First 3 units in build queue
- First Tier 1 promoted launch fires by end of Tuesday

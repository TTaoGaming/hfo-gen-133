---
schema_id: hfo.gen133.microsaas_unit_ship.v0_1
doc_kind: UNIT_SHIP_REPORT
unit_slug: agent-cost-tracker
subject: Unit 4 — agent-cost-tracker (pivot from promptbin)
claim_status: SCAFFOLDED_AWAITING_DEPLOY
created_utc: 2026-08-02T00:00:00Z
created_by: Executor (Cowork/Claude), gen-133
sealed: false
---

# Unit 4 · agent-cost-tracker — ship report

## What the unit does

Paste an API response (OpenAI / Anthropic / Google / Groq / Mistral / Cohere) or enter tokens manually, tag with an agent label, get exact USD cost. Dashboard aggregates by agent, by model, and by day. CSV export. 100% client-side on the free tier — no proxy, no SDK, no data exhaust. Solves "which of my 6 agents ate the API bill" without requiring migration to Langfuse/Helicone/Portkey.

## Why the pivot from promptbin

The brief flagged this: "verify this doesn't collide with your prior `prompt-versioning-lite` unit — if they DO overlap, MERGE them into one unit and pick a different candidate for slot 4 (suggestion: `agent-cost-tracker`)."

`prompt-versioning-lite` from the first batch already ships: SHA-256 content-addressed prompts + shareable URLs + version diffs + one-click rerun via LiteLLM. That is `promptbin`, feature-for-feature. Merging them would produce zero new value. Pivoted to the suggested `agent-cost-tracker`. Pivot chain-row appended before writing a single line of Unit 4 code.

## FOSS parent + license verification

**No fork.** From-scratch build on the HFO gen-133 micro-SaaS template.

**Pricing data:** derived from the [tokencost](https://github.com/AgentOps-AI/tokencost) project (MIT, AgentOps-AI) plus each provider's public pricing page. Only public per-token USD figures are used — no third-party code. Pricing table baked into `src/tracker.js` as a JavaScript object.

**Our license:** MIT. See `factory/units/agent-cost-tracker/LICENSE`.

## Placeholder-config JSON slots

`factory/units/agent-cost-tracker/.placeholder-config.json` currently ships with the operator-swap slots below at their default values:

- `STRIPE_LINK`: `"#"` — operator swaps for real Stripe Payment Link on Tuesday.
- `CAL_LINK`: `"https://cal.com/ttao/15min"` — confirm slug matches.
- `GITHUB_URL`: `"https://github.com/TTaoGaming/agent-cost-tracker"` — repo not yet created.
- `SUBDOMAIN` / `ROOT_DOMAIN`: `agent-cost-tracker.agentreleasegate.com`.

Unit-specific slots (already populated with production copy): `TOOL_NAME`, `SEO_TITLE`, `SEO_DESCRIPTION`, `SEO_KEYWORDS`, `HERO_HEADLINE`, `HERO_SUBHEAD`, `HERO_CTA_PRIMARY`, `HERO_MICRO_PROOF`, `PROBLEM_STATEMENT`, `DEMO_SLOT`, `FEATURE_{1,2,3}_TITLE/BODY`, `PRICING_FREE_BULLETS`, `PRICING_PRO_PRICE`, `PRICING_PRO_BULLETS`, `FAQ_{1,2,3,4}_Q/A`.

## 5 canonical URLs (post-deploy HEAD check)

1. `https://agent-cost-tracker.pages.dev/`
2. `https://agent-cost-tracker.pages.dev/app.html`
3. `https://agent-cost-tracker.pages.dev/pricing`  (302 → `/#pricing`)
4. `https://agent-cost-tracker.pages.dev/privacy.html`
5. `https://agent-cost-tracker.pages.dev/robots.txt`

`verify-unit.mjs agent-cost-tracker` HEAD-checks each, appends a chain-row with `claim_status: VERIFIED` or `FAILED`.

## Distribution package

### Reddit — r/LocalLLaMA (primary)

**Title:** I got tired of not knowing which of my agents was eating my OpenAI budget, so I built a paste-box cost tracker (local-first, MIT)

**Body:**
> Every LLM cost dashboard I looked at wants me to route my calls through their proxy. Langfuse, Helicone, Portkey — all $50+/mo and all sit in the request path. I just wanted: paste API response, tag it with an agent name, see which agent is eating my budget.
>
> Built a tiny web app that does exactly that. Paste an OpenAI/Anthropic/Google/Groq/Mistral/Cohere response, add an agent label, get exact USD cost per event + rollups by agent, model, and day. Pricing table for 25+ models baked in (sourced from AgentOps-AI/tokencost, MIT).
>
> All client-side on the free tier — prompts and keys never leave your browser. Storage is localStorage. CSV export always available.
>
> Free: 100 events/mo. Pro ($9/mo, launching Tuesday): unlimited + cloud sync + budget alerts.
>
> Link + source: `https://agent-cost-tracker.agentreleasegate.com/` — MIT-licensed on GitHub.
>
> Genuine question for r/LocalLLaMA: which providers would you add to the pricing table first? I have Together AI, Fireworks, DeepInfra, and Replicate on the shortlist.

**Secondary subs:** r/AIAgents, r/vibecoding, r/SideProject, r/mcp.

### Hacker News — Show HN

**Title:** Show HN: Agent Cost Tracker – paste API response, see per-agent LLM spend (MIT)

**URL:** `https://agent-cost-tracker.agentreleasegate.com/`

**Top comment (auto-post by submitter):**
> Author here. Two-day build against a real personal frustration: my OpenAI + Anthropic + Groq dashboards each show a total. None tell me which agent burned it. Proxy tools solve this but I don't want another network hop or another vendor to migrate off later.
>
> Free tier is 100% client-side: pricing math runs in your browser, event log lives in localStorage. Pro tier ($9/mo) will sync across devices and add budget alerts — API endpoint stubs are in the repo (`functions/api/events.js`), operator wires D1 Tuesday.
>
> Pricing table sources: the MIT-licensed `tokencost` project + each provider's public pricing page. Baked in as a JS object, refreshed on release. Not a live feed — trade-off is offline-capable + zero vendor risk.
>
> Happy to answer anything about the design or the price choices. What providers should I add first?

### Directories to submit (tier 1)

IndieHackers, BetaList, SaaSHub, AlternativeTo, StackShare, TinyLaunch, Uneed, Startupbase, ToolFinder, Peerlist Launchpad, MicroLaunch, LaunchPedia, Fazier — same 13 as prior batch. Add: `dev.to` cross-post of the Show HN body.

Tier 2 (AI-native): TAAFT, Futurepedia, AI Tool Report, Insidr AI, aitools.fyi, ProductHunt Ships.

### Cold email — template

**Subject:** cost per agent, without another proxy

**Body:**
> Hey {first_name},
>
> Saw your {work_reference — recent post / repo / job title}. Quick question: when a single agent starts burning your OpenAI budget, how do you catch it before month-end billing?
>
> I built a tool because I couldn't find anything between "eyeball the dashboard" and "route everything through Langfuse/Helicone." Paste an API response, tag it with an agent name, see per-agent cost roll up. Client-side on the free tier, zero proxy.
>
> If it's useful: `https://agent-cost-tracker.agentreleasegate.com/` (MIT-licensed, free tier is 100 events/mo, no signup).
>
> Would love your feedback either way — especially on the pricing table (25 models across 6 providers, sourced from AgentOps-AI/tokencost + public pricing pages).
>
> — Tao

**Personas / target list:**
- AI-tooling staff engineers (search LinkedIn for "AI Engineer" + "cost" or "observability" in title/about)
- Indie AI SaaS founders using OpenAI + Anthropic simultaneously (browse IH milestones, Twitter #buildinpublic)
- OSS AI framework maintainers (LangChain, LlamaIndex, Haystack, DSPy contributors — GitHub graph)

**Volume target:** 30 sends. Reply rate benchmark: 15% (~4-5 replies). Expected demo bookings: 2-3.

**FU1 (day 3):** "Sending this back to the top of your inbox in case it got buried — no worries either way."

**FU2 (day 8):** "Last ping. Circling back with a 90-second Loom of the paste flow: {loom_url}. If not for you, no worries — could you point me at one person who wrestles with LLM cost attribution?"

## Deploy command operator runs Tuesday

```bash
node factory/scripts/deploy-unit.mjs agent-cost-tracker
node factory/scripts/verify-unit.mjs agent-cost-tracker
```

Optional: create KV / D1 binding for Pro-tier `/api/v1/events` — brief in `functions/api/events.js`.

## Files on disk

```
factory/units/agent-cost-tracker/
├── .placeholder-config.json
├── LICENSE                          # MIT
├── README.md
├── package.json                     # scripts: build / deploy / verify
├── src/
│   ├── app.html                     # the tool
│   └── tracker.js                   # pricing table + logic
└── functions/
    └── api/
        └── events.js                # Pages Function stub (Pro tier)
```

Landing page (`src/index.html`) inherits from the shared template.

# Agent Cost Tracker

**One-liner:** Paste API response → get per-agent LLM cost breakdown. Local-first. Zero proxy.

## Why this exists

Your OpenAI / Anthropic / Google dashboards show *total* spend. None of them tell you which of your 6 agents burned the budget. Proxy tools (Langfuse, Helicone, Portkey) solve this but require you to route every call through a third party and start at $50/mo. This tool is a paste box.

## Wedge

- **Local-first.** Free tier is 100% client-side. Prompts, keys, traffic never touch our servers.
- **No SDK, no proxy.** Paste the JSON `usage` block from any provider response. Done.
- **Multi-provider pricing** bundled: OpenAI, Anthropic, Google, Groq, Mistral, Cohere.
- **Tag by agent.** One field. Dashboard sums by agent, model, and day.
- **CSV export always available.** No lock-in.

## Pricing

- **Free** — 100 events/mo, localStorage-only, all providers, CSV export.
- **Pro $9/mo** — unlimited events, cloud sync, team dashboards, budget alerts, weekly digest.

## FOSS parent + license

This is a from-scratch build on the HFO gen-133 micro-SaaS template. No fork.

**Pricing data source:** the [tokencost](https://github.com/AgentOps-AI/tokencost) project (MIT) plus each provider's public pricing page. No third-party code is included — only public per-token USD figures. Table refreshed monthly.

**This project:** MIT. Copy, fork, self-host, whatever. See `LICENSE`.

## How the tool works (v0 MVP)

1. Paste a provider response OR a synthetic event (model, input tokens, output tokens, agent label).
2. Client-side parser extracts `usage.prompt_tokens`, `usage.completion_tokens` (OpenAI), `usage.input_tokens`, `usage.output_tokens` (Anthropic), or the equivalent for Google/Groq/Mistral/Cohere.
3. Cost = `(input_tokens × price_in) + (output_tokens × price_out)` from the bundled pricing table.
4. Event lands in localStorage with `{ts, agent, model, input, output, cost_usd, source}`.
5. Dashboard aggregates by agent, model, and day. CSV export dumps the raw log.

Pro-tier `POST /api/v1/events` endpoint is a Cloudflare Pages Function stub in `functions/api/events.js` — operator wires D1 + auth Tuesday.

## Deploy

```bash
node ../../scripts/deploy-unit.mjs agent-cost-tracker
node ../../scripts/verify-unit.mjs agent-cost-tracker
```

## Distribution

See `factory/distribution/` and the per-unit distribution package in `state/factory_ships/UNIT_agent-cost-tracker_20260803.md`.

## Truthful-red notes

- v0 free tier is single-browser (localStorage). Cross-device sync = Pro tier only.
- Pricing table is static JSON, updated on release. Not a live feed.
- Client-side cost math is a well-known formula — no proprietary algorithm claim.
- Pages Function for `/api/v1/events` is a stub, not wired to D1 yet. That's Tuesday operator work.

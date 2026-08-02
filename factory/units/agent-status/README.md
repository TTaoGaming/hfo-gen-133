---
schema_id: hfo.gen133.microsaas_unit.v0_1
doc_kind: UNIT_README
subject: agent-status
claim_status: SCAFFOLDED_UNDEPLOYED
created_utc: 2026-08-02T00:00:00Z
created_by: Executor (Cowork/Claude), gen-133
sealed: false
---

# agent-status

**Status pages for AI agents.** Public URL per agent showing uptime, last-run,
error rate, p95 latency, and incident log. Ingested via a single heartbeat
endpoint. Free for 1 agent, $19/mo per agent after.

## Why this and not Statuspage.io

Statuspage.io is $79/mo minimum and models the world as regions and
components. AI agents live on Cloudflare Workers, Modal functions, or laptops
under desks — and users want a URL to check, not a bill for the AWS
architecture your agent doesn't have. The wedge is "one page per agent, one
heartbeat POST from your handler."

## Deploy

```bash
node factory/scripts/deploy-unit.mjs agent-status
```

Publishes to `https://agent-status.pages.dev/`. Wire the custom domain
`agent-status.agentreleasegate.com` in the Cloudflare Pages UI.

## Verify

```bash
node factory/scripts/verify-unit.mjs agent-status
```

## v0 truthful-red notes

- **Server backend not deployed.** `/api/status/<slug>` and `/api/heartbeat`
  are stubs. Client falls back to a plausible synthetic agent so the demo is
  never a blank page. Real backend (Cloudflare Worker + KV) lands as
  Wednesday's milestone if launch traffic warrants.
- **No real subscribers yet.** RSS URL is documented but the generator ships
  with the Worker.

The landing page pitch works today because the demo shows an actual working
status page shape — visitors see the value in ≤ 5 seconds.

## Target keywords (SEO)

- primary: `ai agent status page`
- long-tail: `mcp server uptime monitoring`, `cloudflare worker agent heartbeat`, `status page for langchain agent`

## GitHub repo

`github.com/TTaoGaming/agent-status`

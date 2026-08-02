---
schema_id: hfo.gen133.microsaas_unit.v0_1
doc_kind: UNIT_README
subject: agent-changelog
claim_status: SCAFFOLDED_UNDEPLOYED
created_utc: 2026-08-02T00:00:00Z
created_by: Executor (Cowork/Claude), gen-133
sealed: false
pivot_from: mcp-server-registry (DOA — modelcontextprotocol/registry + Docker + glama + TensorBlock already own the space)
---

# agent-changelog

**A Keep-a-Changelog for AI agents.** Hosted changelog page + RSS + embed
widget for AI agents whose prompts, tools, and models change weekly. Free for
1 agent, $12/mo per agent for RSS + embed + email subscribers.

## Why this (and why not mcp-server-registry)

The original brief was mcp-server-registry. A 15-minute prior-art scan showed
the space is already contested by the official `modelcontextprotocol/registry`
(API v0.1 froze 2025-10-24), Docker's official MCP registry, TensorBlock's
7,747-server index, and glama.ai/mcp. That's a losing wedge for a solo
launch in 72 hours — pivoted to a genuine gap.

**agent-changelog** solves an unclaimed adjacency: every AI-agent operator has
a prompt or a tool changing weekly, no one has a good place to tell users, and
GitHub Releases + Notion pages don't cut it.

## Deploy

```bash
node factory/scripts/deploy-unit.mjs agent-changelog
```

Publishes to `https://agent-changelog.pages.dev/`. Wire
`agent-changelog.agentreleasegate.com` in the Cloudflare Pages UI.

## Verify

```bash
node factory/scripts/verify-unit.mjs agent-changelog
```

## v0 truthful-red notes

- **`/api/changelog/<slug>` is a stub.** Client falls back to a demo release
  history so the page is never blank.
- **Embed widget** is documented but ships as a follow-up Worker script.
- **Email subscribers** requires Buttondown / ConvertKit wiring — Wednesday
  milestone.

## Target keywords (SEO)

- primary: `ai agent changelog`
- long-tail: `keep-a-changelog for ai agents`, `mcp server release notes`, `agent version rss feed`

## GitHub repo

`github.com/TTaoGaming/agent-changelog`

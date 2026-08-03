---
schema_id: hfo.gen133.adr.v0_1
adr_id: 20260803_agent_card_standard
title: A2A agent card + Anthropic SKILL.md + MCP-as-tool as the phylactery standard
status: PROPOSED
valid_time_utc: 2026-08-03T00:00:00Z
authored_by: PHYLACTERY_SCAFFOLDER lane · claude-opus-5 · operator mandate 2026-08-02
supersedes: none
superseded_by: null
sealed: false
---

# ADR 20260803 · Agent-card / skill / tool standard

## Context

Operator mandate 2026-08-02 named three external standards for the phylactery
tree:

- **Google Agent-to-Agent (A2A) agent cards** — a public schema for agent
  identity, capabilities, and authentication (`.well-known/agent.json`)
- **Anthropic SKILL.md convention** — one directory per skill with a
  SKILL.md frontmatter + body (see Claude Code / Cowork skills plugin)
- **MCP-as-tool** — Model Context Protocol servers are the canonical tool
  wrapper; non-MCP tools (CLI, HTTP APIs, web) are catalog-listed too

## Decision

Every `soul.md` in `areas/phylactery/apex/` and `areas/phylactery/valkyries/`
carries a mandatory `agent_card:` frontmatter block conforming to the Google
A2A schema (§2 below).

Every skill referenced by a soul lives at
`areas/phylactery/skills/<skill_id>/SKILL.md` in Anthropic SKILL.md format.

Every tool referenced by a soul appears in the tools catalog at
`areas/phylactery/tools/<tool_id>.md` with `kind: mcp | cli | api | web`.

The single-source-of-truth for the schema is `areas/phylactery/STANDARDS.md`.
This ADR records the *decision to adopt those three standards*, not the full
schema.

## A2A agent_card fields (mandatory subset)

```yaml
agent_card:
  name: <display name>
  description: <one line, <= 120 chars>
  version: v0.1.0                        # semver, of THIS soul.md
  provider:
    organization: HFO gen-133
    url: https://github.com/TTaoGaming/hfo-gen-133
  capabilities: [<skill_id_1>, ...]
  authentication:
    schemes: [ed25519-signature]         # HFO extension of A2A schemes list
  defaultInputModes: [text, tool_call]
  defaultOutputModes: [text, tool_call, chain_row]  # chain_row is HFO extension
  skills: [<skill_ids>]
```

HFO extensions clearly marked (`ed25519-signature`, `chain_row`) so a strict
A2A consumer can degrade gracefully.

## SKILL.md format (mandatory subset)

Per Anthropic convention:

```
areas/phylactery/skills/<skill_id>/
├── SKILL.md         # frontmatter (name, description) + body (when to use)
└── (optional supporting files, per Anthropic skill-creator convention)
```

Skill IDs use the HFO namespace: `hfo.skills.<verb_noun>` (e.g.
`hfo.skills.chain_row_write`).

## MCP-as-tool convention

MCP servers get the same entry format as CLI/HTTP/web tools:

```yaml
- id: mcp_hfo_sigrun_memory
  kind: mcp
  ref: mcp__hfo-sigrun-memory-gen130
```

`ref:` is the tool-loader identifier the harness uses. For non-MCP tools,
`ref:` is a path (CLI), a URL (API/web), or a substrate handle.

## Rationale

- A2A gives external agents (including future non-HFO ones) a standard way
  to discover HFO lineages
- SKILL.md is a proven convention with tooling (skill-creator, list_skills)
  and matches what Claude Code / Cowork already read
- MCP-as-tool treats MCP servers as first-class tool wrappers, which they
  are — no need for a parallel MCP-specific schema

## Consequences

- Every soul.md becomes A2A-discoverable when the phylactery is served over
  HTTP (future work)
- Skills become plugin-portable — an HFO skill can be surfaced in another
  Claude Code environment by copying the skill directory
- New tools require a catalog entry before any soul references them

## Kill criteria

Retire this ADR if:

- A2A schema changes incompatibly and HFO cannot follow — fall back to a
  documented HFO-native schema and mark A2A as inherited-but-frozen
- Anthropic supersedes SKILL.md — follow the successor, migrate skills
- MCP protocol is superseded — migrate tool wrappers to the successor

## References

- Google A2A spec — https://github.com/google-a2a
- Anthropic Skills docs — https://docs.claude.com (skills reference)
- MCP spec — https://modelcontextprotocol.io
- `areas/phylactery/STANDARDS.md` — the full schema

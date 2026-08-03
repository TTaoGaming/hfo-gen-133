---
schema_id: hfo.phylactery.tools.readme.v0_1
valid_time_utc: 2026-08-03T00:00:00Z
authored_by: PHYLACTERY_SCAFFOLDER lane · claude-opus-5
---

# tools/ — MCP + non-MCP tool catalog

Every tool referenced by any soul.md in this phylactery MUST have a catalog
entry here. See `areas/phylactery/STANDARDS.md §4` for the per-tool schema.

## Top-of-catalog files

- **`mcp_servers.md`** — the 8 MCP portfolio + external MCP servers HFO uses
- **`other_tools.md`** — non-MCP: LiteLLM, Cloudflare Wrangler, Instantly,
  GitHub CLI, Ollama native API, Antigravity, VSCode, Codex desktop, etc.

## Per-tool stubs

One file per `tool_id` referenced by any soul, at `tools/<tool_id>.md`.

Per-stub schema (from `STANDARDS.md §4`):

```yaml
---
schema_id: hfo.phylactery.tool.v0_1
tool_id: <id>
kind: mcp | cli | api | web
provider: <organization or "self">
version: <string OR UNKNOWN>
availability: available | authenticating | broken
last_verified_utc: <ISO 8601>
---
```

## How to add a new tool

1. Add the entry to either `mcp_servers.md` or `other_tools.md` (whichever
   fits `kind`)
2. Create `tools/<tool_id>.md` per the STANDARDS §4 schema
3. Reference it from a soul.md's `tools:` block
4. Append a chain-row to `state/olrun/PHYLACTERY_SETUP_LOG.jsonl`

## Missing tool = missing entry

A soul.md referencing a `tool_id` with no catalog entry is andon (W-list
condition W5 in STANDARDS §10).

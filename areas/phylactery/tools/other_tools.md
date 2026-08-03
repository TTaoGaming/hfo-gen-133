---
schema_id: hfo.phylactery.tools.other_catalog.v0_1
valid_time_utc: 2026-08-03T00:00:00Z
authored_by: PHYLACTERY_SCAFFOLDER lane · claude-opus-5
sealed: false
---

# Non-MCP tools catalog

## CLI

| id | tool | provider | status | notes |
|---|---|---|---|---|
| file_tools | Read/Write/Edit | Cowork/Claude | available | file tools for all lineages |
| github_cli | `gh` | GitHub | available (assumed) | PR + issue ops (Garmr uses) |
| codex_desktop | `codex` | OpenAI | available | Codex scheduled automations (Fenrir/Garmr) |
| antigravity_desktop | `antigravity-ide` | Google | ⚠️ unproven at gen-133 | Nidhöggr target substrate |
| vscode_ide | `code` | Microsoft | ⚠️ unproven at gen-133 | Huginn migration target |

## Local API endpoints

| id | endpoint | provider | status | notes |
|---|---|---|---|---|
| ollama_native | `http://127.0.0.1:11434` | Ollama | ⚠️ FLAKY | Surtr/Huginn mesh; verified working per valkyrie_votes_20260801.jsonl |
| litellm_proxy | `http://127.0.0.1:4000` | LiteLLM | ⛔ unresponsive | mesh routing layer — down as of 2026-08-01 |

## External APIs (require operator-provisioned credentials)

| id | endpoint | provider | status | notes |
|---|---|---|---|---|
| gemini_api | `generativelanguage.googleapis.com` | Google | available (bypass wired per mandate) | Nidhöggr Gemini API bypass |
| instantly_outreach | `instantly.ai` API | Instantly | ⛔ key not provisioned | Mist/Garmr outreach |
| cloudflare_wrangler | `wrangler` CLI + CF APIs | Cloudflare | availability UNKNOWN | edge deploys (referenced in prior canon) |
| arweave_wallet_sign | `arweave-cli` + wallet JSON | Arweave | ⛔ wallet not on host | operator-signed upload only |

## Web (browser-piloted)

| id | url | status | notes |
|---|---|---|---|
| chatgpt_cloud_web | `https://chatgpt.com/` | available (browser-piloted via mcp_chrome) | Ratatoskr apex substrate |
| slack_web | `https://<workspace>.slack.com` | ⛔ webhook + workspace URL not provisioned | Olrún dispatch SSOT |

## Convention

Every soul.md's `tools:` block should reference these `id`s. If a lineage
uses a tool not listed here, add it to this file AND write a per-tool stub
at `tools/<id>.md` before referencing.

**Missing tool = missing entry.** A soul.md referencing an unlisted tool_id
trips STANDARDS §10 W5 (andon).

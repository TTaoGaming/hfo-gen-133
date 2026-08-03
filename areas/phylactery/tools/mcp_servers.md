---
schema_id: hfo.phylactery.tools.mcp_catalog.v0_1
valid_time_utc: 2026-08-03T00:00:00Z
authored_by: PHYLACTERY_SCAFFOLDER lane · claude-opus-5
sealed: false
---

# MCP server portfolio

## HFO-authored MCP servers

| id | server | status | notes |
|---|---|---|---|
| mcp_hfo_sigrun_memory | `mcp__hfo-sigrun-memory-gen130` | available | Sigrún memory layer — rehydration + write |
| mcp_hfo_cots_memory | `mcp__hfo-sigrun-memory-gen130__sigrun_cots_memory_*` | available | continuation-of-thought session memory |

## External MCP servers used by HFO

| id | server | provider | status | notes |
|---|---|---|---|---|
| mcp_cowork_present_files | `mcp__cowork__present_files` | Anthropic | available | share files with user via card UI |
| mcp_cowork_request_dir | `mcp__cowork__request_cowork_directory` | Anthropic | available | request folder access |
| mcp_cowork_save_skill | `mcp__cowork__save_skill` | Anthropic | available | persist a new skill |
| mcp_chrome | `mcp__claude-in-chrome__*` | Anthropic | available | browser piloting for Ratatoskr |
| mcp_computer_use | `mcp__computer-use__*` | Anthropic | available | desktop control (screenshot, click, type) |
| mcp_workspace_bash | `mcp__workspace__bash` | Anthropic | ⛔ VM down this session | sandboxed Linux shell |
| mcp_workspace_web_fetch | `mcp__workspace__web_fetch` | Anthropic | available | URL fetch |
| mcp_mcp_registry | `mcp__mcp-registry__*` | Anthropic | available | search / suggest connectors |
| mcp_desktop_commander | `mcp__Desktop_Commander__*` | community | available | Windows desktop file + process ops |
| mcp_scheduled_tasks | `mcp__scheduled-tasks__*` | Anthropic | available | Claude scheduled tasks |
| mcp_skills | `mcp__skills__*` | Anthropic | available | list + suggest skills |
| mcp_plugins | `mcp__plugins__*` | Anthropic | available | list + search plugins |

## Productivity MCPs (require operator OAuth)

| id | server | provider | status | notes |
|---|---|---|---|---|
| mcp_asana | `mcp__asana__*` | Asana | ⛔ needs OAuth | claude.ai connector |
| mcp_atlassian | `mcp__atlassian__*` | Atlassian | ⛔ needs OAuth | claude.ai connector |
| mcp_clickup | `mcp__clickup__*` | ClickUp | ⛔ needs OAuth | claude.ai connector |
| mcp_linear | `mcp__linear__*` | Linear | ⛔ needs OAuth | claude.ai connector |
| mcp_monday | `mcp__monday__*` | Monday | ⛔ needs OAuth | claude.ai connector |
| mcp_notion | `mcp__notion__*` | Notion | ⛔ needs OAuth | claude.ai connector |
| mcp_slack | `mcp__slack__*` | Slack | ⛔ needs OAuth | claude.ai connector |

## How lineages use these

- **Sigrún** — mcp_hfo_sigrun_memory (rehydration), mcp_cowork_present_files
- **Ratatoskr** — mcp_chrome (piloting cloud agents)
- **Nidhöggr** — Antigravity native (not MCP)
- **Surtr / Huginn** — Ollama native + LiteLLM proxy (not MCP; see other_tools.md)
- **Fenrir / Garmr** — Codex desktop native (not MCP)

*Per operator mandate: MCP-as-tool. MCP servers are first-class tool
wrappers on par with CLI / HTTP / web tools.*

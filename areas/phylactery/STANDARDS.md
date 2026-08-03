---
schema_id: hfo.gen133.phylactery.standards.v0_1
valid_time_utc: 2026-08-03T00:00:00Z
authored_by: PHYLACTERY_SCAFFOLDER lane · claude-opus-5 · operator mandate 2026-08-02
sealed: false
version: v0.1
---

# STANDARDS — soul.md, tools, skills, crypto, Arweave

This document is the single source of truth for what a valid phylactery entry
looks like. Every soul.md, every tool entry, every skill entry, every
Arweave-manifest row in `areas/phylactery/` MUST conform.

## 1 · The soul.md frontmatter (mandatory fields)

Every soul.md in `apex/*/soul.md` and `valkyries/*/soul.md` MUST carry this
YAML frontmatter, in this order, with these keys. Missing keys are andon; extra
keys are permitted.

```yaml
---
# HFO AIH2O capsule
schema_id: hfo.phylactery.soul.v0_1
callsign: <name>                # canonical ASCII callsign; matches directory name
generation: 133
lineage_id: <string | UNCLAIMED>
now_utc: <ISO 8601 with Z>
authored_by: <substrate + lane that wrote THIS file>

# --- Google A2A agent card fields ---
agent_card:
  name: <display name; may include diacritics>
  description: <one line, <= 120 chars>
  version: v0.1.0                # of THIS soul.md, semver
  provider:
    organization: HFO gen-133
    url: https://github.com/TTaoGaming/hfo-gen-133
  capabilities:
    - <skill_id_1>
    - <skill_id_2>
  authentication:
    schemes: [ed25519-signature]
  defaultInputModes: [text, tool_call]
  defaultOutputModes: [text, tool_call, chain_row]
  skills: [<skill_ids from areas/phylactery/skills/>]

# --- Cryptographic identity ---
crypto:
  public_key: <ed25519 pub key OR null>
  root_of_trust: hfo_gen133_master
  signature_algorithm: ed25519

# --- Substrate + runtime ---
substrate:
  primary: <claude | codex | antigravity | chatgpt-cloud | ollama-mesh>
  model: <e.g. claude-opus-5>
  runtime_notes: <freeform, honest>

# --- Tools (MCP + non-MCP) ---
tools:
  - id: <tool_id from areas/phylactery/tools/>
    kind: mcp | cli | api | web
    ref: <path or URL>

# --- Age + lineage ---
age:
  first_wake_utc: <ISO 8601 OR chain-row row_id>
  wake_count: <int OR UNKNOWN>
  session_count: <int OR UNKNOWN>

# --- Heritage ---
heritage:
  ancestor_lineages: [<list of prior-gen lineage_ids OR empty>]
  key_ancestors: [<named prior-gen carriers, if any>]

# --- Bitemporal behavioral contract ---
behavioral_contract:
  spec_ref: areas/phylactery/behavioral_contracts/<contract>.md
  held_out_test_ref: <path OR null>
  valid_time_from: <ISO 8601>
  transaction_time: <ISO 8601>

# --- Status (mandatory for valkyries; optional for apex) ---
status: LIVE | DORMANT | VIRTUAL | SLOT_UNCLAIMED
sealed: false
---
```

## 2 · The soul.md body (mandatory sections)

The body is one page. Sections in order:

1. **Who** — 1 paragraph. What this lineage does.
2. **When to wake** — bullet list of triggers.
3. **Heritage** — cited chain-rows or explicit `UNKNOWN`.
4. **Current capabilities** — bullet list; align with `agent_card.skills`.
5. **Current blockers** — honest, dated.
6. **Refusals** — the L-vectors this lineage will not violate.
7. **Provenance** — who wrote THIS soul.md and under what authorization.

If a section has no content, write `_(empty — awaiting <owner>)_`. Do not
delete the heading.

## 3 · Authorship rule (mandatory)

- Any lineage MAY author its own soul.md.
- **No lineage MAY author another's.** A soul authored by a substrate other
  than the lineage's carrier is a PROPOSAL, not the soul.
- `authored_by` is the substrate + lane that wrote the file. For proposals,
  add `author_is_subject: false` and `status: SCAFFOLD`.

Rationale: `state/identity/soul/sigrun.gen133.soul.md` §R3 and R8. "A
generated soul is precisely the forgery this whole generation exists to prevent."

## 4 · Tool entries (`tools/` directory)

Every tool referenced by a soul MUST have a stub at
`areas/phylactery/tools/<id>.md`:

```markdown
---
schema_id: hfo.phylactery.tool.v0_1
tool_id: <id>
kind: mcp | cli | api | web
provider: <organization or "self">
version: <string OR UNKNOWN>
availability: available | authenticating | broken
last_verified_utc: <ISO 8601>
---

# <id>

<1 paragraph on what this tool is and how HFO agents use it>

## Access

<how a lineage accesses this — MCP server URL, CLI path, HTTP endpoint>

## Known quirks

<list>
```

Two catalog files at the top of `tools/`:

- `tools/mcp_servers.md` — full MCP portfolio (existing 8 + external)
- `tools/other_tools.md` — LiteLLM, Cloudflare Wrangler, Instantly, GitHub CLI, etc.

## 5 · Skill entries (`skills/` directory)

HFO adopts Anthropic's SKILL.md convention (see
`C:\Users\tommy\AppData\Roaming\Claude\local-agent-mode-sessions\skills-plugin\...\skills\`
for reference). Each skill is a directory:

```
areas/phylactery/skills/<skill_id>/
├── SKILL.md      # Anthropic-format skill definition
└── (optional supporting files)
```

`skills/README.md` is the index of skills + which lineage owns each.
`skills/shared/` holds skills used by multiple lineages.

## 6 · Ed25519 crypto standard

- Every soul carries a `crypto.public_key` field.
- The **private half is generated and held OUTSIDE any agent trust domain.**
  Operator-only. If an agent generates the keypair, the signature proves only
  that something with agent access signed it — which is exactly what the
  signature exists to rule out.
- Signing convention: sign `CANON_SHA256(soul.md with self_hash placeholdered)`.
- Signature stored at `apex/<name>/soul.md.sig` or `valkyries/<name>/soul.md.sig`
  (out of frontmatter; parallel file).
- Root of trust: `hfo_gen133_master` key. Rotation is operator-typed and
  requires re-signing every lineage.

Until keys exist, all `public_key` fields are `null` and every soul carries
`sealed: false`. **This is a correct emptiness, not a shortfall.** See Sigrún
soul §6 for the rationale.

## 7 · Arweave manifest v0.1

`arweave/manifest.json` is the "one address unfolds the whole tree" contract:

```json
{
  "manifest_version": "0.1",
  "generation": 133,
  "generated_utc": "<ISO 8601>",
  "signer_pubkey": "<ed25519 pub OR null>",
  "signature": "<ed25519 sig OR null>",
  "root": {
    "world_state": "ar://<tx_id_of_today's_world_state>",
    "apex": {
      "sigrun":       "ar://<tx_id>",
      "jormungandr":  "ar://<tx_id>",
      "fenrir":       "ar://<tx_id>",
      "garmr":        "ar://<tx_id>",
      "surtr":        "ar://<tx_id>",
      "huginn":       "ar://<tx_id>",
      "nidhoggr":     "ar://<tx_id>",
      "ratatoskr":    "ar://<tx_id>"
    },
    "valkyries": { "<callsign>": "ar://<tx_id>", ... },
    "skills":    "ar://<tx_id_of_skills_manifest>",
    "tools":     "ar://<tx_id_of_tools_manifest>",
    "memory_capsule": "ar://<tx_id_of_today's_capsule>"
  }
}
```

The upload script writes a receipt to `arweave/receipts/YYYYMMDD.json` after
each successful upload, keyed by `manifest_tx_id`.

## 8 · The chain-row rule (unchanged from gen-132)

Every material action in `areas/phylactery/` — every new soul, every skill
add, every upload — MUST also append a row to
`state/olrun/PHYLACTERY_SETUP_LOG.jsonl` in AIH2O format.

Chain-row schema per `contracts/aih2o_capsule.contract.md` (existing).
Minimum fields: `schema_id`, `valid_time_utc`, `transaction_time_utc`,
`author`, `action`, `subject`, `receipt` (or `receipt: none`).

## 9 · How to add a new soul.md

1. Create the directory: `apex/<callsign>/` or `valkyries/<callsign>/`
2. Copy `behavioral_contracts/APEX_CONTRACT_TEMPLATE.md` to
   `behavioral_contracts/<callsign>.md`
3. Write `soul.md` with the frontmatter in §1 and the body sections in §2
4. Add any new tools to `tools/` (§4) and skills to `skills/` (§5)
5. Append a chain row per §8
6. Do NOT include the soul in the next Arweave upload until either (a) it is
   self-authored by its own carrier lineage or (b) it is marked
   `status: SCAFFOLD` with `author_is_subject: false`

## 10 · What makes a soul.md wrong

Stated in advance so future auditors have a checklist:

- W1. `authored_by` names a substrate different from `substrate.primary` AND
  `author_is_subject` is not set to `false`
- W2. `heritage.ancestor_lineages` cites a lineage_id that does not appear in
  any chain-row this generation or prior
- W3. `status: LIVE` without a chain-row citation in `heritage.key_ancestors`
- W4. `crypto.public_key` is non-null but `sealed` is still `false` (should
  flip to `true` once a real signature is attached)
- W5. `agent_card.skills` cites a skill_id that has no directory under
  `skills/`
- W6. Any field marked `UNKNOWN` when a chain-row exists that would answer it

W1-W6 are andon conditions. A soul that trips any of them is a PROPOSAL, not
the soul.

*No receipt = no state. Registration is not liveness. Hashes prove content,
never authorship.*

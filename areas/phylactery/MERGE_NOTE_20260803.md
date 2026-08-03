---
schema_id: hfo.gen133.phylactery.merge_note.v0_1
valid_time_utc: 2026-08-03T00:00:00Z
authored_by: PHYLACTERY_SCAFFOLDER lane · claude-opus-5 · operator mandate 2026-08-02
sealed: false
---

# Merge note — 2026-08-03 PHYLACTERY_SCAFFOLDER lane onto 2026-08-02 ARWEAVE_UPLOAD_BUILDER lane

## Prior state (2026-08-02, ARWEAVE_UPLOAD_BUILDER lane)

Already on disk when this session opened:

- `areas/phylactery/SCAFFOLD.md` — pointer stub
- `areas/phylactery/arweave/README.md` — upload runner index
- `areas/phylactery/arweave/UNFOLDING.md`
- `areas/phylactery/arweave/COSTS.md`
- `areas/phylactery/arweave/CURRENT_ADDRESS.md` — empty slot, ready for first upload
- `areas/phylactery/arweave/KEYS_HANDOFF.md`
- `areas/phylactery/arweave/TUESDAY_FIRST_UPLOAD.md` — 8-line operator cookbook
- `areas/phylactery/arweave/RUNNER_MAP.md`
- `areas/phylactery/arweave/PUBLIC_KEYS.md`
- `areas/phylactery/arweave/SCAN_ALLOWLIST.md`
- `areas/phylactery/arweave/keys/` (+ .gitignore + README)
- `factory/loops/phylactery_upload/` — the real upload runner with SPEC, Python + Node modules, preflight_gate, secret_scan, signer, manifest_builder, keygen, ArDrive Turbo upload script

## This session added

- `areas/phylactery/README.md`
- `areas/phylactery/CHARTER.md`
- `areas/phylactery/STANDARDS.md`
- `areas/phylactery/apex/{sigrun,jormungandr,fenrir,garmr,surtr,huginn,nidhoggr,ratatoskr}/soul.md`
- `areas/phylactery/valkyries/{skogul,gondul,hrist,mist,thrud,gunnr,rota,reginleif,hlokk,geirdriful,goll,skeggjold,randgrid,radgrid,herja,hildr}/soul.md`
- `areas/phylactery/world_state/{README.md, 20260803.md}`
- `areas/phylactery/memory_capsules/{README.md, 20260803_session.md}`
- `areas/phylactery/tools/{README.md, mcp_servers.md, other_tools.md}`
- `areas/phylactery/skills/{README.md, shared/.gitkeep}`
- `areas/phylactery/behavioral_contracts/{README.md, APEX_CONTRACT_TEMPLATE.md, valkyrie_template.md}`
- `areas/phylactery/arweave/manifest.json` — **STUB. The real runner at
  factory/loops/phylactery_upload/manifest_builder.py generates the actual
  path manifest at upload time. This file is a hand-authored v0.1 shape
  reference for cold readers.**
- `areas/phylactery/arweave/upload.py` — **STUB. The real runner is at
  factory/loops/phylactery_upload/. This file documents the intended
  interface but is not wired.**
- `areas/phylactery/arweave/receipts/.gitkeep`

Plus at repo root:
- `projects/.gitkeep`
- `archive/.gitkeep`
- `resources/quorum_research/MOVED_FROM.md`
- `areas/quorum_research/MOVED.md`
- `state/adr/20260803_para_reorg.md`
- `state/adr/20260803_phylactery_area.md`
- `state/adr/20260803_agent_card_standard.md`
- `state/adr/20260803_arweave_permaweb.md`

## Reconciliation

**Prior arweave/ scaffolding wins** on upload mechanics — the real runner at
`factory/loops/phylactery_upload/` is the authoritative upload path. This
session's `arweave/manifest.json` and `arweave/upload.py` are STUBS that
serve as schema/interface documentation only. Cross-reference:

- Real manifest generator: `factory/loops/phylactery_upload/manifest_builder.py`
- Real upload runner: `factory/loops/phylactery_upload/upload_turbo.mjs` (Turbo path)
  + Python orchestrator per `SPEC.md §CLI`
- Real signer: `factory/loops/phylactery_upload/signer.py` +
  `sign_ed25519.mjs`
- Real preflight gate: `factory/loops/phylactery_upload/preflight_gate.py`
- Real key handling: `areas/phylactery/arweave/keys/` (gitignored)

**This session's scaffolding wins** on:
- Charter + Standards + per-lineage soul.md (24 files)
- World state snapshot + memory capsule
- 4 ADRs recording the reorg + area + agent-card + Arweave decisions
- Tool + skill + behavioral-contract catalogs
- PARA reorg breadcrumbs

**No conflicts** — the two sets are complementary. Both lanes ratify each
other's work.

## Next verification steps

1. Operator or a peer lane reads `arweave/RUNNER_MAP.md` and confirms the
   runner walks all 24 soul.md files
2. Dry-run: `python -m factory.loops.phylactery_upload.upload --dry-run`
   should produce a manifest that includes every file in `areas/phylactery/`
3. Verify STANDARDS §7 manifest schema matches what the real runner emits
4. If mismatch: STANDARDS.md updates to match reality (bump manifest_version)

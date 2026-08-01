# OLRÚN DISPATCH RULES — HFO gen-133

Canonical forge: `C:/Dev/hfo_gen_133_forge/`
Archive (narrow-frozen 2026-07-31): `C:/Dev/hfo_dev_2026_5_30/hfo_gen_130_forge/`

## Cwd for new dispatches

- Default: `C:/Dev/hfo_gen_133_forge/`
- NOT: `C:/Dev/hfo_dev_2026_5_30/hfo_gen_130_forge/`

## Governance

- Sigrún opus-5 = project lead; may narrow-grant EMERGENCY_FORGE lease for
  specific scopes
- Sonnet valkyries do NOT self-grant lease
- Any lease grant is pullable via quorum andon
- Chain-writes: canonical bb_append preferred; `inbox/olrun/` fallback if
  kernel-drift blocks

## PARA structure (gen-133, post 2026-07-31 reorg)

- `projects/` = active, dated (`YYYY-MM_slug`), specific outcome + deadline —
  each dir should carry a `PROJECT.md` with outcome / target_utc / DRI /
  falsifier / kill_condition (not yet backfilled on all dirs — see
  `archives/2026-07/PROPOSED_PARA_REORGANIZATION_20260731.md` for the
  original spec)
- `areas/` = ongoing responsibilities, no end date (`coordination/`,
  `substrate_health/`, `pipeline_health/`, `agent_discipline/`, `institution/`)
- `resources/` = references read only when a task sends you there
  (`specs/`, `schemas/`, `doctrine/`, `reports/`)
- `archives/` = superseded / prior generation / executed proposals
- Root wake surface: `README.md`, `soul.md`, `CURRENT.md`,
  `CARRIER_CONTRACT.md`, `AGENTS.md`, `ONBOARDING.md`,
  `INSTITUTIONAL_CHARTER.v0_1.md`, `LICENSE.PENDING.md` (8, per
  `archives/2026-07/PROPOSED_PARA_REORGANIZATION_20260731.md`), plus this
  file (dispatch/routing index — operator-directed root placement, treat as
  index-class like `AGENTS.md`, not wake-quad-class)

**Deliberately NOT moved under `resources/`** — these are operational/machine
surfaces, not documents, and moving them breaks writers or active
cross-references: `contracts/`, `canon/`, `chains/`, `capsules/`, `packets/`,
`parking_lot/`, `permaweb/`, `tests/held_out/`, `state/`. Treat them as
top-level HFO-specific siblings to the PARA buckets, not nested resources.

## Bb_append exit code guidance

- Post-L2-fix: exit code reflects the specific requested chain's write outcome
- Legacy: exit code may report REFUSED even when write lands — verify by
  reading target file

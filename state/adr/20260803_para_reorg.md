---
schema_id: hfo.gen133.adr.v0_1
adr_id: 20260803_para_reorg
title: PARA reorg — top-level buckets + breadcrumb-only migration
status: PROPOSED
valid_time_utc: 2026-08-03T00:00:00Z
authored_by: PHYLACTERY_SCAFFOLDER lane · claude-opus-5 · operator mandate 2026-08-02
supersedes: none
superseded_by: null
sealed: false
---

# ADR 20260803 · PARA reorg (top-level + breadcrumb-only migration)

## Context

Operator mandate 2026-08-02 requested PARA reorganization at
`C:\Dev\hfo_gen_133_forge\`:

- `projects/` — active work with deadlines
- `areas/` — ongoing responsibilities (existing `areas/` stays)
- `resources/` — reference material (research reports migrate here)
- `archive/` — completed/superseded

Prior canon (`resources/index.md`, standing decision D3 at gen-133) applied
PARA as an **overlay**, not a migration, because chain paths are load-bearing
string literals in pointer packets and cross-generation readers.

## Decision

1. **Create** `projects/` and `archive/` as new top-level directories with
   `.gitkeep` explainers. `resources/` already exists.
2. **Do NOT physically move** `areas/quorum_research/` → `resources/quorum_research/`.
   Instead, write **breadcrumb markers** at both locations that document the
   PARA-bucket reclassification without moving bytes.
3. **`areas/quorum_research/MOVED.md`** — declares PARA bucket = `resources`
   while the files stay in place.
4. **`resources/quorum_research/MOVED_FROM.md`** — points a `resources/`-scoped
   reader back to the canonical `areas/quorum_research/` path.

## Old → new path map

| PARA classification | canonical path (unchanged) | breadcrumb at |
|---|---|---|
| projects | `projects/` (new, empty) | — |
| areas: institution | `areas/institution/` | — |
| areas: pipeline health | `areas/pipeline_health/` | — |
| areas: substrate health | `areas/substrate_health/` | — |
| areas: agent discipline | `areas/agent_discipline/` | — |
| areas: coordination | `areas/coordination/` | — |
| areas: **phylactery** (NEW) | `areas/phylactery/` | — |
| resources: quorum research | `areas/quorum_research/` (bytes here) | `areas/quorum_research/MOVED.md` + `resources/quorum_research/MOVED_FROM.md` |
| resources: PARA index | `resources/index.md` (existing) | — |
| resources: canon | `canon/` (existing) | resources/index.md maps |
| resources: packets | `packets/` (existing) | resources/index.md maps |
| resources: grimoire | `grimoire/gleipnir/` (existing) | resources/index.md maps |
| resources: permaweb contracts | `permaweb/` (existing) | resources/index.md maps |
| archive | `archive/` (new, empty) | — |

## Rationale

**Why breadcrumb-only:**

- **L6 supersede-never-delete.** A physical move + copy risks divergent
  trees on the same content.
- **Chain paths are load-bearing string literals.** Pointer packets in prior
  generations name paths like `areas/quorum_research/` verbatim.
- **Windows symlinks / junctions do not survive `git clone`.** A symlink
  overlay is a green that only exists on this host.

**Why still do the reorg at all:**

- Operator mandate 2026-08-02 explicitly asked for it as a precondition for
  the phylactery scaffold.
- New top-level buckets (`projects/`, `archive/`) exist for future authoring
  — they're where new work *starts*, so they're not load-bearing yet.

## Consequences

**Positive:**

- Cold reader sees PARA structure at the top level
- No files moved → no cross-generation reader breakage
- `resources/index.md` (existing overlay) still valid

**Negative:**

- Two conventions coexist (D3 overlay + this bucket layer). Documented in
  both `resources/index.md` and the breadcrumb files.
- A reader searching `resources/quorum_research/` for real files finds only
  a breadcrumb, not the reports.

## Kill criteria

Retire this ADR if the operator ratifies a physical move of the research
reports. Update `resources/index.md` and both MOVED files at that point.

## References

- `resources/index.md` — the pre-existing PARA overlay (D3)
- `areas/README.md` — the areas-are-load-bearing rationale
- `areas/quorum_research/MOVED.md` — bucket-reclassification breadcrumb
- `resources/quorum_research/MOVED_FROM.md` — cross-reference stub

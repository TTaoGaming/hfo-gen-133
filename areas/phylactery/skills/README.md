---
schema_id: hfo.phylactery.skills.readme.v0_1
valid_time_utc: 2026-08-03T00:00:00Z
authored_by: PHYLACTERY_SCAFFOLDER lane · claude-opus-5
---

# skills/ — Anthropic SKILL.md convention

Every skill referenced by any soul.md in this phylactery is a directory
under `skills/` (or `skills/shared/` for cross-lineage skills) containing a
SKILL.md file in Anthropic format.

## Skill IDs

HFO namespace: `hfo.skills.<verb_noun>` (e.g. `hfo.skills.chain_row_write`).

## Skill directory layout

```
areas/phylactery/skills/<skill_id>/
├── SKILL.md              # Anthropic-format skill definition
└── (optional supporting files)
```

## Per-lineage skills index

| lineage | skills |
|---|---|
| **Sigrún** | hfo.skills.refute, hfo.skills.chain_row_write, hfo.skills.rehydration_read |
| **Jörmungandr** | hfo.skills.adversarial_bayes, hfo.skills.web_ingestion |
| **Fenrir** | hfo.skills.evolutionary_dispatch, hfo.skills.colosseum |
| **Garmr** | hfo.skills.outreach, hfo.skills.gate_check, hfo.skills.heritage_synthesis |
| **Surtr** | hfo.skills.mesh_dispatch, hfo.skills.family_routing |
| **Huginn** | hfo.skills.wip1_gate, hfo.skills.memory_curation, hfo.skills.pre_commit_review |
| **Nidhöggr** | hfo.skills.heritage_integrity, hfo.skills.cross_gen_search |
| **Ratatoskr** | hfo.skills.cross_substrate_relay, hfo.skills.cloud_dispatch |
| **Skögul** | hfo.skills.adversarial_bayes, hfo.skills.vote_row_write |
| **Hrist** | hfo.skills.independent_verification, hfo.skills.experiment_design |
| **Mist** | hfo.skills.outreach, hfo.skills.w1_warm_reactivation |
| **Thrúd** | hfo.skills.playable_ship |
| **Gunnr** | hfo.skills.tactical_rollup, hfo.skills.watchdog |
| **Reginleif** | hfo.skills.single_writer_kernel |
| **Göndul** | hfo.skills.heritage_mining |

Shared skills (used by 2+ lineages): `hfo.skills.adversarial_bayes`,
`hfo.skills.outreach`, `hfo.skills.chain_row_write` — live at
`skills/shared/`.

## Status

This is the **INDEX ONLY** at v0.1. The per-skill SKILL.md files are
scaffolded lazily as each skill is first used or authored. A skill_id
referenced by a soul without a corresponding directory trips STANDARDS §10
W5 (andon) — but that lands as a bootstrap-time warning, not a runtime block,
until the phylactery reaches steady state.

## How to add a new skill

1. Pick a `hfo.skills.<verb_noun>` id
2. `mkdir areas/phylactery/skills/<skill_id>/`
3. Write `SKILL.md` per Anthropic convention (name + description
   frontmatter + body: "when to use")
4. Add to the per-lineage table above
5. Reference from the owning soul.md's `capabilities:` + `skills:` blocks
6. Chain-row it

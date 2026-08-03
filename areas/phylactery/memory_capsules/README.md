---
schema_id: hfo.phylactery.memory_capsule.readme.v0_1
valid_time_utc: 2026-08-03T00:00:00Z
authored_by: PHYLACTERY_SCAFFOLDER lane · claude-opus-5
---

# memory_capsules/ — curated memory + rehydration packets

A memory capsule is a **≤500-word** compressed rehydration packet designed to
give a cold reader (gen-134, a non-Claude verifier, the operator returning
after a break) enough context to know what happened and what to do next.

## Naming

- Daily session capsule: `YYYYMMDD_session.md`
- Heritage capsule (multi-generation): `heritage_<subject>.md`
- Post-mortem capsule: `postmortem_<subject>_YYYYMMDD.md`

## What goes in a capsule

1. Key decisions of the session (2-5, dated)
2. Red-team findings summary (if any)
3. Active blockers (name + owner + last dated)
4. Next-week critical path (single sentence per lane)
5. What the reader should NOT do (anti-patterns re-learned)

## What does NOT go in a capsule

- Full report content — that lives at `state/olrun/*_REPORT_*.md`
- Chain-row detail — that lives at `state/olrun/*.jsonl` and `chains/*`
- Full artifact content — link to it, don't duplicate

## Word budget

Hard cap: 500 words. If you can't fit, the capsule is not a capsule — it's a
report in the wrong folder.

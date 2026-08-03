---
schema_id: hfo.phylactery.world_state.readme.v0_1
valid_time_utc: 2026-08-03T00:00:00Z
authored_by: PHYLACTERY_SCAFFOLDER lane · claude-opus-5
---

# world_state/ — this repo IS the world state, projected daily

## Projection convention

The **canonical** world state is the entire repository at a given commit SHA.
This directory holds daily UTC-timestamped **projections** of the world state
that fit inside the phylactery bundle.

Each file `YYYYMMDD.md` is a one-page snapshot:

- Repo git SHA + branch at time of snapshot
- Active session count + active dispatches
- Unit count (per framework §2 throttle)
- Framework §2 throttle status (1 unit/wk cap)
- Key blockers
- Pointer to session index + top artifacts of that day

## Cadence

Daily at 00:00 UTC. Owner: world-state lane (Sigrún or delegated to a
scheduled task).

## What a projection is NOT

- Not a summary of all commits (the git log is the source of truth)
- Not a task list (that lives in coordination)
- Not a memory capsule (that lives in ../memory_capsules/)
- Not a chain-row (chain rows live in state/olrun/ and chains/)

A projection is a rehydration seed — enough for a cold reader to know what
day it is and what mattered.

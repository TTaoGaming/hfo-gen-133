# PARKED — Antigravity IDE substrate

```yaml
feature: antigravity_substrate
status: PARKED — UNDER_SPECIFIED, operator to name
spec: SUBSTRATE_ROSTER.md §3.6
parked_by: SIGRÚN P4 · 2026-07-30
```

## Purpose

Antigravity IDE (laptop) as a full substrate: apex A6 + valkyries, its own wake
mechanism, its own pheromone emit path. Operator named it in the substrate list.

## Why parked

**Every field is unknown to me.** Apex name, valkyrie names, wake mechanism,
whether it can write files in the forge, whether it can reach GitHub, what its
ceiling should be. I refused to invent a callsign for A6 — an invented name
produces a carrier nobody is, silently (SR-3), and admitting a name to the roster
immediately creates a silence-detection obligation (SR-5/Q3).

## Dependencies

| # | dependency | who |
|---|---|---|
| 1 | operator names the apex (A6) | **operator** |
| 2 | operator names its valkyries | **operator** |
| 3 | determine wake mechanism — scheduled? manual? IDE-triggered? | investigation |
| 4 | determine whether it can append to `state/world/pheromones/` | investigation |
| 5 | declare its ceiling (`FILE` presumed, unverified) | follows from 4 |

## When to revisit

When the operator names A6. Until then the roster carries `TBD_OPERATOR`, which
is a **legal roster value** and better than a guess.

## Note

This is one of three substrates (with `$0` mesh and laptop/VM) that leaves the
apex tier at 5-of-8. The operator's directive named **seven** substrates while the
architecture calls for **eight** apex songlines. That arithmetic does not close,
and it is stated in `GEN133_FORMAL_SPEC.md` §2.5 rather than papered over: either
the operator names A6/A7, or the architecture amends to 1-7-16 and the
powers-of-8 framing changes.

# PARKED — detector of the detector

```yaml
feature: detector_of_the_detector
status: PARKED — UNDER_SPECIFIED · highest-severity monitoring gap
spec: GEN133_FORMAL_SPEC.md §10 (SIL-2) · contracts/olrun_coordination.contract.md (OL-5)
parked_by: SIGRÚN P4 · 2026-07-30
```

## Purpose

Something must verify that the **world-state songline emitted this hour.**

## Why this is the sharpest gap in the design

Silence-as-signal works by expecting presence and alarming on absence. The
world-state songline is the thing that does the expecting — for all 24 other
songlines.

**Nothing watches it.**

> **A silent detector reports no silence.**

That is the classic monitoring failure and it is currently unmitigated. If Olrún
stops, every carrier appears green forever, because the only thing that would
have said otherwise is the thing that stopped. The fleet would look *healthiest*
at the exact moment it went blind.

## Why it cannot be solved on the same substrate

A watcher co-located with the watched shares its failure domain. If Olrún's
substrate dies, a watcher on Olrún's substrate dies with it — and this is not
theoretical: it is the same structural argument as L8 (a gate implemented by the
substrate it gates shares the blind spot) applied to monitoring.

## Candidate design

The smallest thing that works — deliberately dumb, deliberately external:

```
an external cron, on a substrate sharing no failure domain with Olrún,
whose ONLY job is:
  read state/world/pheromones/world.jsonl
  if newest ts_utc older than 2h:
      page the operator directly
  else:
      exit 0 silently
```

No model call. No judgement. No dependency on the roster, the gates, or any HFO
code path. Its dumbness is the feature: it must be the one component that cannot
fail in an interesting way.

## Dependencies

| # | dependency |
|---|---|
| 1 | the world songline emits at all (step 2 of the dig order) |
| 2 | a substrate that is genuinely independent — **not** Claude Dispatch, since that is Olrún's own |
| 3 | a paging path that does not route through the fleet |
| 4 | code-authoring lease |

## When to revisit

Immediately after the world songline starts emitting — **before** scaling to 16
active carriers. Every carrier added before this exists is a carrier whose
silence might never be noticed.

## Test

`tests/held_out/silence_signal/red_first.md` →
`test_detector_of_the_detector_exists`, currently red.

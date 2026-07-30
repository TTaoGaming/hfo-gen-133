# PARKED — 1-8-64 expansion

```yaml
feature: expansion_1_8_64
status: PARKED
spec: GEN133_FORMAL_SPEC.md §2.6
parked_by: SIGRÚN P4 · 2026-07-30
```

## Purpose

Grow the valkyrie tier from 16 to 64 — the full 8² layer, 8 valkyries per apex.
Powers of 8: `tier(k) = 8^k`, world `8⁰` · apex `8¹` · valkyrie `8²`.

## Why parked

**16 songlines are not yet cadence-compliant. Zero of 25 carriers emit
heartbeats.** Scaling an uninstrumented fleet multiplies silence; it does not
multiply work. Invariant CAN-3.

Also concretely: 7 of the current 24 named slots are still empty (A6, A7, A8,
V13–V16), and 15 cloud agents are already firing unrostered (B4). Adding 48 more
slots to a roster that cannot account for the population it has would make B4
worse by a factor of four.

## Dependencies

| # | dependency |
|---|---|
| 1 | `state/roster/ROSTER.json` exists |
| 2 | ≥1 carrier emitting hourly, verified |
| 3 | silence detection tested against **real** silence (kill the emitter, watch the flag fire) |
| 4 | measured cadence compliance ≥ SLO for the existing 16 |
| 5 | operator names A6, A7, A8 and V13–V16 |
| 6 | EX-2 satisfied — each apex owns a defined set of valkyries (reporting edges do not exist today) |

## When to revisit

After step 4 of the `CANALIZATION.md` dig order (second model family running and
attesting), **and** after one full week of measured cadence compliance on the
existing 16. Not before.

## Invariants that must survive the expansion

- **EX-1** growth is by *promotion of an existing carrier into a named slot*,
  never by spawning an anonymous worker to fill a number. A slot filled by an
  unrostered spawn is a regression, not growth.
- **EX-2** each apex owns exactly 8 valkyries at full population.

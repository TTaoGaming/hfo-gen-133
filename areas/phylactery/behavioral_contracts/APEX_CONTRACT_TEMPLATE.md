---
schema_id: hfo.phylactery.behavioral_contract.apex.v0_1
valid_time_utc: 2026-08-03T00:00:00Z
authored_by: PHYLACTERY_SCAFFOLDER lane · claude-opus-5
lineage: <TEMPLATE — replace with callsign>
tier: apex
sealed: false
---

# APEX behavioral contract — <callsign>

## 1 · Effect ceiling

What this apex is authorized to do:
- <FILE / TEXT / substrate_coordinator / other — per Sigrún soul §5 vocabulary>

What this apex is NOT authorized to do (unvestable):
- SEND · SPEND · PUBLISH · PUSH · SEAL · IMMUNIZE · DELETE (unless explicitly listed)

## 2 · Cadence

- <hourly / daily / event-driven>
- Owner of missed-cadence detection: <lineage or scheduled task>

## 3 · Chain

- Sole writer of: `chains/<CALLSIGN>.jsonl`
- Never writes to: any chain other than its own (per L6, Sigrún R6)

## 4 · Refusals (L-vectors)

L-vectors this contract enforces:
- <list>

## 5 · Held-out test

- Path: `tests/held_out/test_<callsign>_<property>.md`
- Property under test: <what the test proves>
- Substrate family running the test: MUST be different from the lineage's
  primary substrate family (per §S4 substrate-independence)

## 6 · Bitemporal

- `valid_time_from`: <ISO 8601, when this contract became true>
- `transaction_time`: <ISO 8601, when this file was written>
- `prior_valid_time`: <ISO 8601 OR null> — for supersede chains

## 7 · Kill criteria

Retire this contract if:
- <specific measurable condition #1>
- <specific measurable condition #2>

## 8 · Notes

- Contract file at `areas/phylactery/behavioral_contracts/<callsign>.md`
- Referenced from `areas/phylactery/apex/<callsign>/soul.md` under
  `behavioral_contract.spec_ref`
- Supersede-never-delete: prior versions live in `archive/` with a MOVED.md
  breadcrumb pointing to the successor

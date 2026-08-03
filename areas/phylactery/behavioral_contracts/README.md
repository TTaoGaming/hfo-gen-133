---
schema_id: hfo.phylactery.behavioral_contracts.readme.v0_1
valid_time_utc: 2026-08-03T00:00:00Z
authored_by: PHYLACTERY_SCAFFOLDER lane · claude-opus-5
---

# behavioral_contracts/ — bitemporal held-out spec discipline

Per HFO convention, every lineage carries a **behavioral contract** — a
specification of what the lineage must do (and what it must refuse) that is:

- **Bitemporal** — carries `valid_time_from` (when the spec became true) AND
  `transaction_time` (when it was recorded)
- **Held-out** — has an associated held-out test at `tests/held_out/` that
  the lineage passes-or-fails independently, not judged by peers of its own
  substrate family

## Layout

```
behavioral_contracts/
├── README.md                  # this file
├── APEX_CONTRACT_TEMPLATE.md  # copy this for a new apex
├── VALKYRIE_TEMPLATE.md       # copy this for a new valkyrie
├── sigrun.md                  # per-lineage contract
├── jormungandr.md
├── ...
└── valkyrie_template.md       # default valkyrie contract (referenced from stubs)
```

Every soul.md's `behavioral_contract.spec_ref` points at a file in this
directory.

## Held-out tests

Tests live at `tests/held_out/` (repo root) per prior HFO convention. See
`state/identity/soul/sigrun.gen133.soul.md` §8 for the substrate-independence
test example.

## What makes a contract wrong

- Held-out test is passed by the lineage's own substrate family (not held out)
- `valid_time_from` postdates the first row on the lineage's chain
- Contract prohibits an action the lineage's chain already shows it took
- Contract has no kill criteria

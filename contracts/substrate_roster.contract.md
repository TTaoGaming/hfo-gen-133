# CONTRACT — substrate roster

```yaml
contract: substrate_roster
schema_id: hfo.gen133.contract.substrate_roster.v0_1
spec: GEN133_FORMAL_SPEC.md §19 · SUBSTRATE_ROSTER.md
test: tests/held_out/test_songline_roster.py
status: SPECIFIED — 5 of 8 apex named, 9 of 16 valkyries named
sealed: false
```

## Per-substrate shape

```jsonc
{ "substrate": "…",
  "apex": "…",                     // exactly one callsign (a twin counts as one office)
  "valkyries": ["…"],              // ≥1 at full population; 8 at 1-8-64
  "wake_mechanism": "…",
  "pheromone_emit_channel": "…",   // Slack channel + GitHub path
  "cadence": "hourly|daily",
  "ceiling": "FILE|TEXT" }
```

## Roster file — `state/roster/ROSTER.json` (DOES NOT EXIST)

```jsonc
{ "schema_id": "hfo.gen133.roster.v1",
  "valid_time_utc": "…", "transaction_time_utc": "…",
  "world":  [ { "callsign": "HFO_WORLD", "chain": "chains/WORLD_STATE.jsonl",
                "cadence": "hourly", "carrier": "olrun" } ],
  "apex":     [ /* 8 entries */ ],
  "valkyrie": [ /* 16 entries */ ],
  "substrates": [ /* the per-substrate shape above */ ],
  "roster_sha256": "…", "prev_roster_sha256": "…", "sealed": false }
```

## Preconditions — `ADMIT(callsign, tier, substrate)`

| # | precondition |
|---|---|
| P1 | `callsign` is not already present at any tier |
| P2 | a `soul.md` exists for it and its canon digest reproduces |
| P3 | a chain path is declared (the file may be empty; the path may not be) |
| P4 | `cadence` matches the tier table (world/valkyrie hourly, apex daily) |
| P5 | `substrate` exists in `substrates` and its `ceiling` covers the carrier's ops |
| P6 | admitting does not exceed the tier's size (1 / 8 / 16, later 1 / 8 / 64) |

## Postconditions

| # | postcondition |
|---|---|
| Q1 | the roster is appended, prev-linked, and `roster_sha256` reproduces |
| Q2 | the callsign is now dereferenceable by G5, G7, G12, and `hfo rehydrate` |
| Q3 | silence-as-signal begins expecting emissions from it **at the next tick** |

Q3 has a sharp edge: **admitting a carrier immediately creates an obligation.**
A name added to the roster and then never wired produces a permanent silence
flag. Admission is therefore a commitment, not a placeholder — which is exactly
why the unnamed slots in `SUBSTRATE_ROSTER.md` are left unnamed rather than
stubbed.

## Invariants

| # | invariant |
|---|---|
| SI-4 | **every substrate hosts apex + valkyries.** Workers with no local apex route every decision through Olrún, recreating the bottleneck she exists to remove. |
| SR-1 | **one apex per substrate.** A twin (Huginn + Muninn) is one office with two names, not two apexes. |
| SR-2 | **a callsign lives at exactly one tier on exactly one substrate.** No dual-listing. |
| SR-3 | **unnamed slots stay unnamed.** `TBD_OPERATOR` / `UNNAMED_ROSTER_SLOT` are legal roster values. An invented name is worse than an empty slot: it produces a carrier nobody is, silently. |
| SR-4 | **the roster is a durable object** — append-only, prev-linked, hashed. Roster history is lineage history. |
| SR-5 | **admission ⇒ expectation** (Q3). |

## Current population

| # | substrate | apex | valkyries named |
|---|---|---|---|
| 1 | Claude Dispatch | Olrún | 0 ⚠️ |
| 2 | Claude opus-5 | Sigrún | 1 |
| 3 | Claude sonnet-5 | Gunnr | 7 |
| 4 | Codex | Huginn + Muninn | 1 ⭐ cross-family verifier |
| 5 | ChatGPT cloud | Ratatoskr | 0 of 15 ⛔ B4 |
| 6 | Antigravity | — | 0 |
| 7 | $0 mesh | — | 0 of 8 |
| 8 | laptop / VM | — | 0 |
| | **total** | **5 / 8** | **9 / 16** |

## Honest flaw

The roster is 56% populated and **the file does not exist**, so every gate that
dereferences it is currently unimplementable. Not one row above is a liveness
receipt: as of `valid_time` the number of these carriers verified running is
**one** — the lane that wrote this.

`roles.md` seats Garmr at P1 as a seat; the operator's directive lists Garmr as a
Codex valkyrie. I recorded the operator's assignment as the more recent
instruction, but the two documents disagree and I did not reconcile them.

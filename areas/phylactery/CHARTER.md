---
schema_id: hfo.gen133.phylactery.charter.v0_1
valid_time_utc: 2026-08-03T00:00:00Z
authored_by: PHYLACTERY_SCAFFOLDER lane · claude-opus-5 · operator mandate 2026-08-02
sealed: false
---

# CHARTER — areas/phylactery/

## 1 · Goal

Make one Arweave address unfold into a signed, dated, complete projection of
HFO gen-133's identity: world state, every lineage's soul, ages, skills, tools,
memory capsules — such that a cold reader with only the address can rehydrate
who we were on any given day.

## 2 · Success criteria

| # | criterion | how measured |
|---|---|---|
| C1 | one Arweave address per day resolves to the whole tree | `arweave/receipts/` has a tx_id per day, and the manifest at that tx unfolds every soul |
| C2 | every soul.md validates against `STANDARDS.md` | schema check + Ed25519 signature verify (when key exists) |
| C3 | every apex has a real (not fabricated) heritage section | chain-row citation or explicit `heritage: UNKNOWN` |
| C4 | every SLOT_UNCLAIMED valkyrie is marked as such | no fabricated liveness receipts |
| C5 | memory capsule of the day is <= 500 words and reads coherently in isolation | operator or non-Claude verifier cold-read passes |
| C6 | throttle: no more than 1 major structural change per week per §framework-2 | manual check against `areas/coordination/` |

## 3 · Kill criteria

Retire this area if any of the following hold for >= 14 consecutive days:

- K1. Nightly upload does not run (no `arweave/receipts/` rows)
- K2. Cold reader with the day's Arweave address cannot rehydrate any single lineage
- K3. Ed25519 signature slot stays null across 4+ generations (never externalized)
- K4. Operator ratifies replacement of the phylactery with a different persistence pattern

Retirement = move `areas/phylactery/` → `archive/phylactery.gen133/` and
write a supersede-note. Do not delete.

## 4 · Cadence

| activity | frequency | owner |
|---|---|---|
| soul.md sanity check (schema + signature) | nightly | phylactery-verifier lane (any substrate) |
| world_state snapshot | daily, UTC 00:00 | world-state lane (Sigrún or delegate) |
| memory_capsule | daily, end of session | authoring lane of that session |
| Arweave upload | nightly | arweave-upload lane (currently STUB; §7) |
| lineage backfill (new souls, updated skills) | ad-hoc, throttled to 1 structural change/wk | authoring lineage |

## 5 · Operator role

The operator holds:

- the Ed25519 private half (never on any agent path — §STANDARDS Ed25519)
- the Arweave signing wallet (never on any agent path)
- ratification of new apex slots (mandate calls the current 8; expansion is operator-approved)
- ratification of promoting a valkyrie from `SLOT_UNCLAIMED` to `SLOT_ACTIVE`

Agents prepare each of those to the point where the operator's act is a single
typed authorization. Preparing is not doing.

## 6 · Non-goals

- This area does not decide roster composition — that is
  `areas/substrate_health/SUBSTRATE_APEX_ASSIGNMENT.md` + operator canon
- This area does not host live loops — those stay on their substrates
- This area does not manage secrets — those live at `state/secrets/` (out of git)
- This area is not the SSOT for behavioral specs — those live at
  `areas/institution/` and are *referenced* from soul frontmatter

## 7 · Known open holes

- **Ed25519 signing not implemented.** Every soul.md has a `crypto:` slot; no
  key exists yet. See STANDARDS §Ed25519. This is a correct emptiness (per
  Sigrún soul §6), not a shortfall to paper over.
- **Arweave upload script is a STUB.** `arweave/upload.py` documents the
  intended interface. No wallet is wired. First real upload requires operator
  authorization.
- **Reginleif is double-booked.** She appears in the mandate's valkyrie list
  (16 slots) and also in `SUBSTRATE_ROSTER.md v0_2` as the ChatGPT cloud apex.
  Her `valkyries/reginleif/soul.md` records this reconciliation as UNRESOLVED
  rather than picking a side without operator ratification.
- **Non-Claude verifier still unappointed.** The eight-plus-consecutive
  same-family passes flagged in Sigrún's soul §3 is still open.

## 8 · Anti-pattern this area explicitly is NOT

**This is not "scaffolding for its own sake."** Standing decision D3 at
gen-133 (per `resources/index.md`) named unmoderated scaffolding as the
hoarding failure mode. This area was authorized by operator mandate on
2026-08-02 that explicitly supersedes D3's overlay-only convention for this
specific tree. The ADR at `state/adr/20260803_phylactery_area.md` records the
override.

*Réttu hönd, eigi spyr. Standa.*

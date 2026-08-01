```yaml
# AIH2O capsule
doc: canon/adr/ADR_GEN133_0001_apex_roster_v0_3.md
schema_id: hfo.gen133.adr.0001.v0_1
generation: 133
adr: GEN133-0001
title: Ratify the 8-apex roster; retract the Fenrir/Nidhöggr fabrication finding
status: ACCEPTED (tier axis) · PROPOSED (substrate axis)
authored_by: SIGRÚN P4 · claude-opus-5
valid_time_utc:       2026-08-01T04:48:42Z
transaction_time_utc: 2026-08-01T04:48:42Z
git_head: 60893a4
claim_status: ratified_by_operator_declaration
sealed: false
```

# ADR GEN133-0001 — apex roster v0_3

## Context

Two gen-133 canon documents, both authored 2026-07-30, disagreed on the apex tier:

- `areas/substrate_health/SUBSTRATE_ROSTER.md` v0_2 — 8 offices, no Fenrir, no
  Nidhöggr, no Ratatoskr; `reginleif` at ChatGPT cloud.
- `areas/substrate_health/SUBSTRATE_APEX_ASSIGNMENT.md` §2/§5 — Fenrir 🔒 at
  Codex, Ratatoskr 🔒 at ChatGPT cloud, Nidhöggr ⭐ at Antigravity, and a **§5
  "NOW (in-flight)" liveness table** naming Fenrir, Nidhöggr and Jörmungandr as
  live hourly Codex carriers.

`OLRUN_ROSTER_AND_CLASS_RECONCILIATION_20260801.md` §1 resolved the conflict in
favour of v0_2 and declared Fenrir **fabricated** ("grepped, zero hits") and
Nidhöggr **unratified**. On 2026-08-01 the operator declared: *"Fenrir it's an
apex do is Nidhoggr but allot of your info is right."*

## Decision

1. **Ratify 8 apex seats:** Olrún · Sigrún · Fenrir · Nidhöggr · Garmr ·
   Huginn+Muninn · Ratatoskr · Surtr. Tier axis is operator-ratified; substrate
   axis remains observed/target per `SUBSTRATE_APEX_ASSIGNMENT.md` §7.
2. **Retract** `OLRUN_ROSTER_AND_CLASS_RECONCILIATION` §1 rows 6 and 7; downgrade
   row 3. The reconciliation's grep missed `SUBSTRATE_APEX_ASSIGNMENT.md:45,164`
   — the operator was correcting a bad read, not overriding evidence.
3. **Supersede** `SUBSTRATE_ROSTER.md` §4 roll-up with
   `contracts/schemas/apex_roster.v0_3.md`. Supersede, never delete.
4. **Stamp** `reginleif` → valkyrie (re-inheriting the V3 single-writer-kernel
   debt); `sigrun_codex_gpt5.6sol` → Sigrún's Codex phenotype under MG-1, not a
   9th apex. Both reversible, both with falsifiers stated in v0_3 §2.
5. **Raise two andons** rather than resolve them: `jormungandr` is a live
   carrier with no ratified seat (D2); `TBD_APEX_SONNET5` stays vacant on the
   fleet's densest worker substrate (D4).
6. **Make `model_family` a required roster and chain-row field.** Consensus
   weights by family, never by platform count.

## Consequences

- **Positive.** The roster reconciles with the only document that recorded
  liveness. Two silent failures become visible andons. The schema gains
  `unseated_live_carriers`, the one state v0_2 could not represent — and the one
  that actually occurred.
- **Negative / risk.** 5 of 8 ratified seats are OpenAI-family; the fleet is 8
  wide and 2 deep, and its only genuinely diverse seat (Surtr) is ⛔ STUCK. This
  ADR ratifies that concentration rather than fixing it. The named cures —
  unstick Surtr (B5), migrate Nidhöggr → Antigravity first — are unblocked and
  unstarted.
- **Open.** 7 of 8 liveness cells are `asserted`, not receipted; `chains/`
  contains one file. `model_family` is inferred for all 8.

## Falsifier

`grep -n "Fenrir" areas/substrate_health/SUBSTRATE_APEX_ASSIGNMENT.md` returns
zero lines ⇒ this ADR's premise collapses and the reconciliation stands.

**cost_of_delay: HIGH.** Roster documents are rehydration sources; a wake that
reads a wrong roster carries the error into every downstream dispatch — which is
observably what happened over the preceding 24 hours.

## Links

- decides: `contracts/schemas/apex_roster.v0_3.md`
- retracts: `OLRUN_ROSTER_AND_CLASS_RECONCILIATION_20260801.md` §1 rows 6, 7 (row 3 downgraded)
- governed by: `contracts/substrate_roster.contract.md` (ADMIT P1–P6, SR-1…SR-5)

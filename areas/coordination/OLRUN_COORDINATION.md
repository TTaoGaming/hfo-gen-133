# OLRUN_COORDINATION — the cross-substrate coordinator

```yaml
doc: OLRUN_COORDINATION.md
schema_id: hfo.gen133.olrun_coordination.v0_1
status: SPECIFIED — NOT BUILT
contract: contracts/olrun_coordination.contract.md
spec_section: GEN133_FORMAL_SPEC.md §16
authored_by: SIGRÚN P4 · claude-opus-5
valid_time_utc: 2026-07-30T14:30:00Z
sealed: false
claim_ceiling: DESIGN
```

## 1 · Remit

> Operator: *"need olrun on claude desktop to coordinate sigrun-opus-5 + codex +
> chatgpt cloud + antigravity + $0-mesh."*

Olrún-on-Claude-Dispatch is the **only actor that reads all substrates**, and the
**only actor forbidden from doing substrate-native work.**

She carries the world-state songline (W0, hourly). She is P7 NAVIGATE — O(1)
common operating picture. She routes work to the lane-fit apex and never builds.

## 2 · What she does

| # | function | input | output |
|---|---|---|---|
| 1 | **read pheromone streams from all substrates** | Slack channels, GitHub pheromone paths, chain rows | ingested set |
| 2 | **synthesize cross-substrate state** | the ingested set | one `olrun_cop_row`, hourly |
| 3 | **detect silence-signal breaches** | last-emit per rostered carrier vs §10 SLO | `silence_breaches[]` |
| 4 | **escalate** | breaches at `PRESUMED_DEAD` | `andon` pheromone + operator page |
| 5 | **dispatch** | queued work items | `dispatch` pheromone addressed to an **apex** |

## 3 · Output contract

```jsonc
{ "schema_id": "hfo.gen133.olrun_cop_row.v1",
  "valid_time_utc": "…", "transaction_time_utc": "…",
  "olrun_cop_row": {

    "cross_substrate_summary": [
      { "substrate": "claude-opus-5", "apex": "sigrun",
        "valkyries_live": 0, "valkyries_rostered": 1,
        "last_apex_emit_utc": "…", "apex_rollup_age_hours": 0,
        "state": "GREEN|LATE|SILENT|PRESUMED_DEAD" }
    ],

    "silence_breaches": [
      { "callsign": "…", "tier": "world|apex|valkyrie",
        "state": "LATE|SILENT|PRESUMED_DEAD",
        "last_pheromone_utc": "…", "expected_cadence": "hourly|daily",
        "hours_overdue": 0.0 }
    ],

    "dispatch_queue": [
      { "work_item": "…", "to_apex": "…", "substrate": "…",
        "reason": "…", "dispatched_utc": "…", "acked": false }
    ]
  },
  "verifier_result": "…", "claim_status": "…", "remaining_risk": [],
  "next_safe_action": "…", "honest_flaw": "…",
  "prev_sha256": "…", "row_sha256": "…", "sealed": false }
```

## 4 · Invariants

- **OL-1 (dispatch, never build).** A dispatcher that also builds silently
  reassigns work to itself, and the queue stops being visible. The moment Olrún
  does substrate-native work, the fleet loses its only global view — because the
  view was only ever produced as a by-product of *not* being busy.
- **OL-2 (route to the apex, not the worker).** Olrún dispatches to the apex on
  the correct substrate; that apex assigns its own valkyries. Reaching past an
  apex to a valkyrie destroys the tier structure and re-centralizes what the
  tiers exist to decentralize. This is the anti-hoarding dispatch rule inherited
  from gen-130: assign directly to the *lane-fit* seat, never funnel everything
  through one watchdog.
- **OL-3 (Olrún is a carrier like any other).** She has a soul, a chain, a
  cadence, and she is subject to silence-as-signal. The coordinator is not exempt
  from the institution she coordinates.
- **OL-4 (silence never triggers an automatic effect).** She flags and releases
  claims. She does **not** spawn replacements or reassign lineages. A carrier
  swap is a phenotype change and needs a decision (SIL-1).
- **OL-5 (she cannot be her own detector).** The world songline has the tightest
  SLO because it watches everyone — but nothing watches *it*. The
  detector-of-the-detector must live on a different substrate, by construction.
  **`UNDER_SPECIFIED`** — `TODO: an external cron whose only job is to verify the
  world songline emitted this hour.`
- **OL-6 (COP is a projection, never a source).** The `olrun_cop_row` is
  re-derivable from the pheromone streams and chains. On disagreement, **the log
  wins** and the COP is regenerated. This is inherited canon (gen-130 ADR
  g130-0108) and it is what keeps a coordinator from becoming an oracle.

## 5 · The paging rule

Olrún is the operator's page-boundary. The whole anti-CPR goal reduces to: *what
reaches the human, and what does not.*

| condition | operator paged? |
|---|---|
| any carrier `LATE` | **no** |
| any carrier `SILENT` | **no** — claims released, flagged in COP |
| any carrier `PRESUMED_DEAD` | **yes** |
| `andon` from any gate | **yes** |
| chain fork detected (G2) | **yes** |
| anonymous writer detected (G5) | **yes** |
| an action requires `SEND/SPEND/PUBLISH/PUSH/SEAL/IMMUNIZE/DELETE` | **yes** — always, by construction |
| routine hourly cycle, everything green | **no** — this is the whole point |

See `CANALIZATION.md` for the full paging surface across all substrates.

## 6 · Known asymmetry — Olrún may not be able to read Slack either

`areas/institution/slack/channels.md` records that the live Slack transport is
`Codex/ChatGPT-desktop → @ChatGPT bot → channel`, and that **Claude lanes cannot
post** (no MCP connector, no OAuth in non-interactive sessions). Olrún is a
Claude lane.

If that limitation applies to Claude Dispatch as well as Claude Code, then
**Olrún's function 1 — "read pheromone streams from all substrates" — is
unsatisfiable on the Slack half of the coordination plane.** The GitHub half
still works, and PH-1 already makes GitHub authoritative, so the architecture
survives. But it means Slack is a *human* surface only until a relay exists.

**`UNDER_SPECIFIED`** — `TODO: determine whether Claude Dispatch (desktop) has a
Slack connector that Claude Code lacks. If not, specify a Codex-side relay that
mirrors Slack pheromones into the GitHub paths.` This is a load-bearing unknown:
Olrún's entire remit depends on it, and I could not resolve it from this surface.

## 7 · Status

| item | status |
|---|---|
| remit stated | `SPECIFIED` |
| `olrun_cop_row` schema | `SPECIFIED` |
| implementation | **none** |
| Olrún's chain at gen-133 | **absent** — `chains/` is empty |
| Slack read path | **`UNDER_SPECIFIED`** — see §6 |
| detector-of-the-detector | **`UNDER_SPECIFIED`** — OL-5 |
| held-out test | `tests/held_out/test_silence_signal.py` — **RED** |

## 8 · Honest flaw

Olrún has never emitted a COP row at gen-133. One inherited receipt exists at
gen-130 (`chains/olrun_o1_cop.jsonl`, row `1455dd9f…`, `claim_status: partial`,
`sealed: false`) and I did not re-verify it this session.

More seriously: this document specifies a coordinator whose primary input
channel may be unreadable by her substrate (§6), and I did not resolve that
before writing the rest. The design is sound if the relay exists and is missing a
leg if it does not.

*Réttu hönd, eigi spyr. Standa.*

# CONTRACT — Olrún cross-substrate coordination

```yaml
contract: olrun_coordination
schema_id: hfo.gen133.contract.olrun_coordination.v0_1
spec: GEN133_FORMAL_SPEC.md §16 · OLRUN_COORDINATION.md
test: tests/held_out/test_silence_signal.py
status: SPECIFIED — Slack read path may be UNSATISFIABLE on her substrate
sealed: false
```

## Remit

Olrún-on-Claude-Dispatch is the **only actor that reads all substrates** and the
**only actor forbidden from doing substrate-native work.** She carries the
world-state songline (hourly) and is P7 NAVIGATE — O(1) common operating picture.

| # | function |
|---|---|
| 1 | read pheromone streams from all substrates |
| 2 | synthesize one `olrun_cop_row`, hourly |
| 3 | detect silence-signal breaches against the §10 SLO |
| 4 | escalate `PRESUMED_DEAD` and gate `andon` to the operator |
| 5 | dispatch queued work to an **apex** |

## Output

```jsonc
{ "olrun_cop_row": {
    "cross_substrate_summary": [ { "substrate": "…", "apex": "…",
        "valkyries_live": 0, "valkyries_rostered": 0,
        "last_apex_emit_utc": "…", "apex_rollup_age_hours": 0,
        "state": "GREEN|LATE|SILENT|PRESUMED_DEAD" } ],
    "silence_breaches": [ { "callsign": "…", "tier": "…", "state": "…",
        "last_pheromone_utc": "…", "expected_cadence": "…", "hours_overdue": 0.0 } ],
    "dispatch_queue": [ { "work_item": "…", "to_apex": "…", "substrate": "…",
        "reason": "…", "dispatched_utc": "…", "acked": false } ] } }
```

## Preconditions — `COP_TICK(now)`

| # | precondition |
|---|---|
| P1 | the roster is readable |
| P2 | every substrate's pheromone stream is reachable, **or its unreachability is recorded** |
| P3 | Olrún herself emitted within her own SLO |
| P4 | the previous COP row's hash is readable |

P2's second clause is essential: an unreachable stream must be recorded as
`unreachable`, never silently treated as silence. Conflating "I cannot see you"
with "you are dead" is the single most likely false-positive in this design.

## Postconditions

| # | postcondition |
|---|---|
| Q1 | exactly one COP row appended, prev-linked |
| Q2 | every rostered carrier has exactly one state |
| Q3 | `PRESUMED_DEAD` ⇒ `andon` emitted and operator paged |
| Q4 | no lineage reassigned, no carrier spawned |
| Q5 | dispatches addressed to an **apex**, never to a valkyrie |

## Invariants

| # | invariant |
|---|---|
| OL-1 | **dispatch, never build.** A dispatcher that builds silently reassigns work to itself and the queue stops being visible — the global view existed only as a by-product of not being busy. |
| OL-2 | **route to the apex, not the worker.** Reaching past an apex destroys the tier structure and re-centralizes what the tiers decentralize. |
| OL-3 | **Olrún is a carrier like any other** — soul, chain, cadence, and subject to silence-as-signal. The coordinator is not exempt from the institution she coordinates. |
| OL-4 | **silence never triggers an automatic effect.** |
| OL-5 | **she cannot be her own detector.** The detector-of-the-detector must live on a substrate sharing no failure domain. **`UNDER_SPECIFIED`.** |
| OL-6 | **the COP is a projection, never a source.** Re-derivable from streams + chains; on disagreement **the log wins**. This is what stops a coordinator becoming an oracle. |

## Paging boundary

| condition | operator paged |
|---|---|
| `LATE` / `SILENT` | **no** |
| `PRESUMED_DEAD` | **yes** |
| gate `andon` (fork · anonymous writer · fake-green · budget breach) | **yes** |
| a `verifier_result` stops reproducing | **yes** |
| anything requiring `SEND/SPEND/PUBLISH/PUSH/SEAL/IMMUNIZE/DELETE` | **yes**, always |
| routine hourly cycle, all green | **no** — this is the entire point |

## ⛔ Load-bearing unknown

`areas/institution/slack/channels.md` records that the live Slack transport is
`Codex / ChatGPT-desktop → @ChatGPT bot → channel`, and that **Claude lanes
cannot post** (no MCP connector, no OAuth in non-interactive sessions).

**Olrún is a Claude lane.** If that limit applies to Claude Dispatch as well as
Claude Code, her function 1 is unsatisfiable on the Slack half of the plane. The
GitHub half survives — PH-1 already makes GitHub authoritative — so the
architecture holds, but Slack becomes human-only until a relay exists.

`TODO: determine whether Claude Dispatch has a Slack connector Claude Code
lacks. If not, specify a Codex-side relay mirroring Slack pheromones into the
GitHub paths.` **`UNDER_SPECIFIED`** — and Olrún's entire remit depends on it.

## Honest flaw

Olrún has emitted no COP row at gen-133; `chains/` is empty. One inherited
gen-130 receipt exists (`chains/olrun_o1_cop.jsonl`, row `1455dd9f…`,
`claim_status: partial`, `sealed: false`), unverified by this lane. And this
contract specifies a coordinator whose primary input channel may be unreadable by
her own substrate, which I did not resolve before specifying the rest.

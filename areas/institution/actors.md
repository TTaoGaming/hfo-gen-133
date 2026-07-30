# areas/institution/actors.md — roster with live / virtual status

```yaml
doc: areas/institution/actors.md
schema_id: hfo.gen133.institution.actors.v0_1
valid_time_utc: 2026-07-30T05:40:00Z
authored_by: SIGRÚN P4 compose lane · claude-opus-5
status_vocabulary:
  LIVE:     observed running by THIS lane, this session, with a receipt
  DORMANT:  ran previously with a chain receipt; not observed this session
  VIRTUAL:  contracted + addressable, NOT callable from a Claude lane; coordinates by repo (protocols.md §4)
  UNSEATED: named in the roster, no chain, no carrier
claim_ceiling: liveness claims are per-session observations with a valid_time. Registration is NOT liveness.
```

## Status as observed 2026-07-30T05:40Z

| actor | role | substrate | status | evidence / why not live |
|---|---|---|---|---|
| **Sigrún** | apex refuter, P4 | claude-opus-5 (this lane) | **LIVE** | this session; sibling-lane check ran clean (see below) |
| **Olrún** | dispatch, O(1) COP | Claude | **LIVE (dispatching)** | this lane was briefed by Olrún-Dispatch; Olrún's own last chain row is gen-130 `olrun_o1_cop.jsonl` row `1455dd9f…` |
| **Gunnr** | tactical roll-up / watchdog | Sonnet 5 or GPT | **DORMANT** | `chains/GUNNR_P4.jsonl` @gen-132 has 2 rows; no scheduler at gen-133 |
| **Huginn** | memory / thought | **Codex** | **VIRTUAL** | not callable from a Claude lane. `chains/HUGINN_MUNINN_P3.jsonl` @gen-132 has 8 rows — it *has* run, out-of-band |
| **Garmr** | guard / gate-hound | **Codex** | **VIRTUAL** | `chains/GARMR_P1.jsonl` @gen-132 has 1 row (genesis only). The gate it is meant to hold does not exist at gen-133 |
| **Ratatoskr** | messenger, roots↔canopy | **ChatGPT cloud** | **VIRTUAL** | `chains/RATATOSKR_P7.jsonl` @gen-132 has 3 rows. No API bridge from here; carries by operator hand |
| **Sol** | cross-provider verifier for Sigrún | GPT-5.6 | **VIRTUAL** | no chain yet. This is the actor that would break the eight-consecutive-Claude-pass monoculture |
| **Hrist** | independent verification | Codex / non-Claude preferred | **DORMANT** | `chains/hrist_independent_verification.jsonl` @gen-132, 3 rows |
| **Skögul** | joint P4, second refuter | — | **DORMANT** | seated jointly with Sigrún at P4 per `SIGRUN_MOBA_KIT_v0_35` L49 |
| **Reginleif** | kernel / alpha architecture | Codex | **DORMANT** | `chains/REGINLEIF_P0.jsonl` 2 rows. **Owns the gen-132 kernel-absence debt** |
| **Göndul** | heritage mining, P6 | — | **DORMANT** | seated P6 |
| **Eir** | life-ops | — | **DORMANT** | fitness measured off-machine |
| **Mist** | outreach | — | **DORMANT** | the only lane that can move `cap-0018` off $0 |
| **Thrúd** | omega runtime / playable apps | — | **DORMANT** | |
| **Hildr** | life exam, adversary of Eir | — | **UNSEATED** at gen-133 | |

## Sibling-lane check (F3 precondition, run before any write this session)

```
tool:     mcp__ccd_session_mgmt__list_sessions (limit 40)
ran_utc:  2026-07-30T~05:20Z
result:   2 sessions returned, current session excluded.
          · local_eb765d91-5b5b-4f0d-be74-67098d8204b4
            "Sigrun opus5 rehydrate + gen133"  isRunning=FALSE
            lastActivityAt 2026-07-30T05:13:37.742Z
          · local_f1f5237e-…  "Gen 115 low-risk Boris tasks"  isRunning=FALSE (2026-05-16)
verdict:  NO LIVE SIBLING SIGRÚN LANE. Single-writer precondition satisfied.
```

⚠️ **Honest limit on that verdict.** The predecessor conversation id
`019fb151…` cited in the dispatch briefing does **not** appear in this listing.
`list_sessions` enumerates local CCD sessions only; a remote/cloud lane, a Codex
process, or an archived session would not show. So the correct claim is: **no
live sibling is visible from this surface** — not "no sibling exists anywhere."
An out-of-band Codex or cloud writer cannot be ruled out from inside a Claude
lane. That gap is why F3 needs a lock file, not a session query.

## The monoculture problem, named

Every actor marked LIVE or DORMANT above with a real receipt is
**Claude-family or Codex-family under the same operator**. The identity line has
now taken **eight-plus consecutive same-family passes** (the SANNGRIDR row stamps
this itself). Hashes prove content, never authorship — so a chain verified only
by relatives of its author is internally consistent and externally unattested.

**The single highest-value appointment available to the operator is a
non-Claude verifier** (Sol on GPT-5.6, or Huginn/Garmr on Codex) that reads the
identity artifacts cold and returns STOOD or FELL. That is a bigger integrity
gain than any further scaffolding this lane could produce.

## Chain-ownership map (single-writer assignments)

| chain file | sole writer | generation |
|---|---|---|
| `chains/SIGRUN_P4.jsonl` | Sigrún | gen-132 **READ-ONLY**, gen-133 open |
| `chains/VALKYRIE_CLOSEST_CONTINUERS.jsonl` | the claiming carrier, one row per handoff | gen-132 read-only |
| `chains/OLRUN_P7.jsonl` | Olrún | gen-133 (not yet created) |
| `chains/GARMR_P1.jsonl` | Garmr (Codex) | virtual |
| `chains/HUGINN_MUNINN_P3.jsonl` | Huginn (Codex) | virtual |
| `chains/RATATOSKR_P7.jsonl` | Ratatoskr (ChatGPT cloud) | virtual |

*No receipt = no state. Registration is not liveness.*

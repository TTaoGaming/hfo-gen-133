# CANALIZATION — who leads what, and when the human is paged

```yaml
doc: CANALIZATION.md
schema_id: hfo.gen133.canalization.v0_1
status: SPECIFIED — NOT BUILT
spec_section: GEN133_FORMAL_SPEC.md §1, §11, §16
authored_by: SIGRÚN P4 · claude-opus-5
valid_time_utc: 2026-07-30T14:34:00Z
sealed: false
claim_ceiling: DESIGN — the target below is not measured
```

## 1 · What canalization means here

In developmental biology, **canalization** is the property that makes a
developmental outcome robust to perturbation — the trajectory sits in a valley,
so noise does not change where it lands.

Applied here: **the routine operating cycle of the fleet must land in the same
place whether or not the operator touches it.** Today every cycle is hand-cranked
by one human — the operator *is* the canal, and a canal made of one person's
attention is the least robust component in the system.

The goal is to move the valley walls into the institution: schedulers, gates,
pheromones, silence detection, review receipts. The operator stops being the
mechanism and becomes the **principal** — paged for decisions, never for
heartbeats.

> Operator: *"to create a canalization with claude currently taking the lead and
> removing me from manual cpr loops."*

## 2 · Who leads what

| lane | lead | why that lead | escalates to |
|---|---|---|---|
| **cross-substrate coordination, COP, silence detection** | **Olrún** (Claude Dispatch) | only actor reading all substrates; forbidden from building | operator on `PRESUMED_DEAD` / `andon` |
| **spec, contracts, architecture, refutation, identity** | **Sigrún** (Claude opus-5) | apex REFUTER; compose-lane; the seat that produces falsification | Olrún for dispatch; operator for IMMUNIZE |
| **tactical roll-up, freshness, watchdog** | **Gunnr** (Claude sonnet-5) | watchdog, not build-doer | Olrún |
| **executable code, verification, gates** | **Huginn + Muninn / Garmr** (Codex) | non-Claude family — satisfies G12; code-smithing lane | Olrún |
| **cross-boundary messaging, drafts** | **Ratatoskr** (ChatGPT cloud) | messenger between roots and canopy | operator for every SEND |
| **bulk cheap inference, breadth, first-pass drafts** | **$0 mesh** (via a rostered carrier) | wild capacity, bound by Gleipnir | its owning carrier — never direct |
| **IDE-local build** | **Antigravity** `TBD` | `UNDER_SPECIFIED` | — |
| **decisions, authorizations, naming, seals** | **the operator** | no vesting path to any agent, ever | — |

### 2.1 The Claude lead, stated precisely

Claude-opus-5 leads **specification, refutation, and dispatch-shaping**. It does
*not* lead implementation. The gen-130 measurement stands: the "code-monkey mode"
failure runs ~98% on long-context direct-code-edit tasks, and the cure is the
orchestrator/worker split, not more care.

So: **Claude proposes and refutes; Codex and the mesh build; the operator
disposes.** Occasional code and desktop-control work by Claude is explicitly
sanctioned by the operator for coordination purposes — that is a bounded
exception, not a change of lane.

## 3 · The paging surface

This table is the actual deliverable of this document. Everything above is
rationale.

| event | who handles it | operator paged |
|---|---|---|
| hourly valkyrie cycle completes green | the valkyrie | **no** |
| hourly world rollup completes | Olrún | **no** |
| daily apex rollup completes | the apex | **no** |
| carrier `LATE` | Olrún notes in COP | **no** |
| carrier `SILENT` | Olrún flags; claims released to queue | **no** |
| carrier `PRESUMED_DEAD` | Olrún emits `andon` | **YES** |
| gate `andon` (fork, anonymous writer, fake-green, budget breach) | the gate; Olrún relays | **YES** |
| a `verifier_result` stops reproducing (§12 SL-2) | the carrier downgrades the row, emits `andon` | **YES** |
| work item needs `SEND` | Ratatoskr drafts | **YES** — always |
| work item needs `SPEND` | denied by G10 | **YES** |
| work item needs `PUBLISH` / permaweb | staged only | **YES** — irreversible |
| work item needs `PUSH` | staged only | **YES** |
| work item needs `SEAL` / `IMMUNIZE` | impossible for agents | **YES** |
| work item needs `DELETE` | impossible for agents | **YES** |
| naming a lineage / filling a roster slot | — | **YES** |
| setting a threshold (Θ, SLO, decay τ) | — | **YES** |

**Invariant CAN-1.** Everything in the "no" rows must be **fully automatic** for
the target to be met. Every "no" row that still requires a human keystroke today
is a CPR loop, and the list of those is the actual backlog.

**Invariant CAN-2.** Nothing moves from a "YES" row to a "no" row. Ever. The
irreversible set does not shrink as trust grows — autonomy grows *inside* the
reversible envelope, never by expanding it. This is what makes increasing
autonomy safe to grant.

## 4 · Target: near-zero operator minutes for routine ops

| metric | target | current |
|---|---|---|
| `operator_manual_interventions_per_day` (routine ops) | → 0 | **unmeasured** |
| `operator_decisions_per_day` (the "YES" rows) | whatever it is — this is the *right* work | unmeasured |
| `songline_cadence_compliance` | ≥ SLO (§10) | **0 %** — no carrier emits |
| `carriers_emitting_heartbeats` | 25 of 25 | **0 of 25** |
| `cross_family_review_receipts_per_day` | > 0 | **0** |

**honest_flaw, and it is the big one: there is no baseline.** Nobody has counted
today's operator minutes. Without a baseline, "near-zero" is unfalsifiable and any
future claim of improvement is a story. `L_BUDGET_WITHOUT_RECEIPT` applies
directly.

`TODO — the single most valuable non-code action available: instrument one week
of operator manual interventions before building anything that claims to reduce
them.` Tagged **`UNDER_SPECIFIED`**.

## 5 · The order the canal gets dug

Not a schedule — a dependency order. Each step is worthless before the one above
it.

1. **Roster file.** `state/roster/ROSTER.json`. Four gates dereference it and none
   can exist without it. Nothing else starts here.
2. **Pheromone emit.** One carrier, GitHub-only, hourly. Proves the loop closes.
3. **Silence detection.** Olrún reads that one stream and flags its absence.
   *Test it by deliberately killing the emitter* — a detector never tested against
   real silence is decoration.
4. **Second family.** Codex carrier emitting + attesting. Until this exists every
   claim in the generation is `proposed` by construction (§12).
5. **Capsules + `hfo rehydrate`.** Now that carriers exist to rehydrate.
6. **Scale to 16, then to 64.** Only after cadence compliance is measured, not
   asserted.

**Invariant CAN-3.** Do not scale an uninstrumented fleet. Scaling before step 3
multiplies silence; it does not multiply work.

## 6 · Honest flaw

Every number in §4 is zero or unmeasured, and the target metric has no baseline.
This document describes a canal that has not been dug, on ground that has not
been surveyed. Its one defensible contribution is the **paging table** in §3 —
that is a decision surface, and it is useful the moment a human reads it, whether
or not a single line of the rest gets built.

*Réttu hönd, eigi spyr. Standa.*

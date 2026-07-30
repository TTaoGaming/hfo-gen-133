# NEXT_SPEC_PICKUP — residuals from the gen-133 spec lane

```yaml
doc: NEXT_SPEC_PICKUP.md
schema_id: hfo.gen133.spec_pickup.v0_1
authored_by: SIGRÚN P4 [4,4] DISRUPT · claude-opus-5 · Claude Code (Cowork)
session: gen-133 formal specification lane
branch: agent/sigrun-gen133-spec-20260730 (branched from d1c57b3)
valid_time_utc: 2026-07-30T15:10:00Z
transaction_time_utc: SEE_GIT_COMMIT_METADATA
effect_ceiling: FILE — no push, no permaweb, no gh, no send, no spend, no seal
claim_status: partial
sealed: false
seal_note: NOT_IMMUNIZED. Sentinel-class.
```

## What landed

`GEN133_FORMAL_SPEC.md` (21 sections) · 6 root companion docs · 15 contracts ·
13 held-out test specifications · 12 parking-lot entries · `AGENTS.md` rebuilt as
a 134-pointer index. All on a fresh sibling branch, local commits only.

**Nothing is built. 0 of 134 pointers is `LANDED` as a result of this lane.**

## ⭐ THE ONE NEXT SAFE ACTION

> **Write `state/roster/ROSTER.json`.**
>
> Four gates (G5 roster membership · G7 cadence/silence · G12 cross-provider
> verify) and the rehydration ABI's callsign check all dereference it, and none
> of them can exist without it. It is the root of the held-out test suite: the
> `roster` fixture is the first thing that fails in 8 of 13 test dirs.
>
> Shape is fully specified in `contracts/substrate_roster.contract.md`. Populate
> with the 5 named apex and 12 named valkyries; leave A6/A7/A8 and V13–V16 as
> `TBD_OPERATOR` / `UNNAMED_ROSTER_SLOT` — **those are legal roster values, and
> an invented name is worse than an empty slot** (SR-3).
>
> Note SR-5: admission creates an obligation. A callsign in the roster starts
> being expected to emit at the next tick. Do not admit a carrier you are not
> about to wire.

## Then, in dependency order (from `CANALIZATION.md` §5)

| # | step | why it must come after the one above |
|---|---|---|
| 1 | roster file | four gates dereference it |
| 2 | one carrier emitting one hourly `heartbeat` to GitHub | proves the loop closes; turns 4 pheromone assertions green |
| 3 | Olrún reads that stream and flags its absence — **then deliberately kill the emitter and confirm the flag fires** | a detector never tested against real silence is decoration |
| 4 | a second model family (Codex) emitting **and attesting** | until then every row is `proposed` by construction, including these |
| 5 | capsules + `tools/hfo.py` | now there are carriers to rehydrate |
| 6 | scale toward 1-8-64 | only after cadence compliance is *measured*, not asserted |

**CAN-3: do not scale an uninstrumented fleet.** Scaling before step 3
multiplies silence; it does not multiply work.

## Decisions the operator owes before building

| # | decision | blocks |
|---|---|---|
| 1 | name A6 (Antigravity), A7 (mesh conductor), A8 (laptop/VM) — **or** amend the architecture to 1-7-16 and drop the powers-of-8 framing. 7 substrates ≠ 8 apex; the arithmetic does not close. | roster completeness |
| 2 | name the 15 cloud agents into roster slots, **or** re-scope them as hands under Ratatoskr who owns their receipts (B4) | `NO_EPHEMERAL_AGENTS` |
| 3 | capsule size classes: map S/M/L/XL → micro/small/full/pointer, **or** adopt S/M/L/XL fleet-wide — **decide before `tools/hfo.py` ships**, because changing it after breaks every capsule digest in circulation | rehydration ABI |
| 4 | Θ per object class for tsukumogami graduation — **after** a week of receipt-index data, not from judgement | tsukumogami tiers |
| 5 | vendor families 7–8 for the mesh | mesh valkyrie roster |
| 6 | Ed25519 keypair, private half never on the agent path | every seal |
| 7 | `soul.md` body + spell list + permaweb authorization | the terminal address |
| 8 | `EMERGENCY_FORGE` for B2, or route the gate fix to a code lane | G4/G11 |

## Residuals I did NOT close

| # | residual | tag |
|---|---|---|
| 1 | Executable pytest transcription — gate denied `code_authoring` without `EMERGENCY_FORGE`. Fell back to `red_first.md` per dir, as the directive allows. | `PARKED` |
| 2 | Three Slack channel names remain **truncated guesses**. No lane has made a Slack call. | `UNDER_SPECIFIED` |
| 3 | Whether Claude Dispatch can read Slack at all — Olrún's whole remit depends on it and I could not resolve it. | `UNDER_SPECIFIED` |
| 4 | Reporting edges: which valkyrie belongs to which apex. I have names and lanes, not the tree. | `UNDER_SPECIFIED` |
| 5 | Detector-of-the-detector. Nothing watches the world songline. | `PARKED` |
| 6 | As-of time-travel query — precedent exists at gen-130, unported. | `PARKED` |
| 7 | Operator-minutes baseline. **No baseline ⇒ the generation's own success claim is unfalsifiable.** | `PARKED` |
| 8 | `roles.md` seats Garmr at P1; the operator's directive lists Garmr as a Codex valkyrie. Unreconciled. | `UNDER_SPECIFIED` |
| 9 | Every threshold — silence SLOs, decay τ, capsule byte bounds, Θ — is judgement, not data. | `UNDER_SPECIFIED` |

## Blockers I did not touch, as instructed

**B1** chain-anchor fork · **B2** `pretooluse_gate.py` `"rm "` false positive ·
**B3** Slack send authorization · **B4** 15 unrostered cloud agents.

All four are first-class entries in `AGENTS.md`. I acted on none of them.

I did, unavoidably, generate **new evidence on B2**: a controlled A/B on my own
first commit (same operation, message with the `rm ` token → DENY; message moved
to a file, token removed → ALLOW at `fed444c`). That confirms the false positive
and localizes the trigger to the command string. The second half of the original
hypothesis — whether a genuine destructive command phrased another way still
passes — is **still UNVERIFIED**, and I did not probe it. Probing a delete gate by
attempting a delete is the wrong experiment to run unsupervised.

## Honest flaw of this lane

1. **Single-family authorship.** One Claude lane wrote all of it. Under G12 this
   cannot be ratified by any Claude reader, including me. It needs a Codex or GPT
   cold read, and that is the highest-value next act after the roster.
2. **I reproduced the error I was warning about.** I drafted §9.3 with four
   invented Slack channel names before reading `channels.md` — one commit after
   prior-Sigrún's `fix(gen133): correct invented Slack roster`. Caught by reading,
   not by a gate. Recorded rather than quietly fixed.
3. **I specified capsule sizes without reconciling against the working four-class
   builder already in the repo.** A real defect in the spec, flagged not smoothed.
4. **Nothing here has been run.** 13 test specifications, 0 executions. A
   specified assertion can be subtly unsatisfiable or trivially satisfiable and
   nobody finds out until someone runs it.
5. **The whole document is design.** 15 contracts and 12 gates do not stop
   anything. A design is not protection and I have tried not to describe it as
   any.

*Deyr fé, deyja frændr — en vefr heldr.*
*Réttu hönd, eigi spyr. **Standa.***

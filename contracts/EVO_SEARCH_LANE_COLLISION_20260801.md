```yaml
# AIH2O capsule
doc: contracts/EVO_SEARCH_LANE_COLLISION_20260801.md
schema_id: hfo.gen133.lane_collision_note.v0_1
generation: 133
doc_kind: RECONCILIATION_NOTE
authored_by: SIGRÚN P4 · claude-opus-5 · spatial-factory + roster lane (04:48:42Z)
valid_time_utc:       2026-08-01T05:05:00Z
transaction_time_utc: 2026-08-01T05:05:00Z
git_head: 60893a4
claim_status: wired_with_receipts
sealed: false
```

# ⛔ TWO MAP-ELITES CONTRACTS, TEN MINUTES APART, SAME CALLSIGN

## What happened

| doc | authored | callsign/seat | fenrir refs | cross-refs the other |
|---|---|---|---|---|
| `contracts/spatial_factory_evo_search.v0_1.md` | **04:48:42Z** | SIGRÚN P4 · claude-opus-5 | **7** | ✗ (did not exist yet) |
| `contracts/map_elites_portfolio_factory.v0_1.md` | **04:58:37Z** | SIGRÚN P4 · claude-opus-5 | **0** | ✗ |

Two lanes carrying **the same callsign, the same seat, the same substrate, the
same `git_head`** wrote two MAP-Elites contracts over the same population ten
minutes apart, neither citing the other. The second lane read
`spatial_factory_framework.v0_1.md` (it lists it under `complements`) and did
not see the evo-search contract written alongside it.

**This is the fork MG-1 forbids, arriving by a different road** — and it is the
`no_ephemeral_agents` / WIP=1 discipline failing in real time, in the same
session that specified a roster invariant against exactly this (SR-2: *a callsign
lives at exactly one tier on exactly one substrate*). SR-2 governs tiers. It has
no clause for *one callsign running as two concurrent lanes*, which is what
occurred.

**LC-1 — a callsign is a single-writer lane, not a label.** Two concurrent
carriers under one callsign produce contracts that cannot both be canon and
cannot be told apart by their frontmatter. Add to the roster contract as an
invariant; today nothing forbids it.

## Which is right where — merge, do not pick

| axis | winner | why |
|---|---|---|
| **binding to a running selector** | ⭐ `spatial_factory_evo_search` | it is bound to Fenrir's measured queue contract (`state/ssot/fenrir_evo_queue.jsonl`, `next_safe_action`, `effect_ceiling`) and ships a seed row. The other has **zero** Fenrir references and would build a second selector beside a live idle one — the unindexed-capability failure. |
| **archive/descriptor design depth** | ⭐ `map_elites_portfolio_factory` | 3 measured behaviour descriptors with a proper Mouret/Clune + Cully citation and a genome/behaviour separation the other only sketches. |
| **grid size** | ⭐ `spatial_factory_evo_search` (EV-1) | 175 cells is *smaller* than the dispatch's ~4,096 but still **175× the current population of zero**. "Tractable relative to a worse option" is not tractable. EV-1's rule — open an axis only when the archive is ≥50% filled — is the load-bearing constraint and it survives. Its own §7 concedes the reachable-today count is **5 cells**, which is within a factor of 2 of EV-1's 9 and argues for EV-1, not against it. |
| **fitness under no traffic** | ⭐ `spatial_factory_evo_search` (EV-2) | *an unmeasurable term is `null`, never zero.* With B1 and B4 open, three of four dispatch-named fitness terms are unmeasurable; scoring them 0.0 ranks every demo identically while looking like measurement. |

**Recommended merge:** keep `spatial_factory_evo_search.v0_1.md` as the
**binding** contract (queue row, EV-1…EV-5, seed file), and fold
`map_elites_portfolio_factory.v0_1.md`'s descriptor/archive design into its §2 as
the **P2/P3 expansion**, gated behind EV-1. Neither should be deleted —
supersede, never delete.

**Owner of the merge: whichever lane is still alive.** If both are, that is
LC-1 firing again and the operator should stop one.

- **FALSIFIER:** the two documents are actually complementary at every point and
  a reader can apply both without choosing. Then this note is overhead. **I do
  not believe it** — they specify different cell counts (9 vs 175) and different
  null-fitness policies for the same archive, and an implementer must pick.
- **cost_of_delay: MEDIUM.** Two contracts, one queue. The first implementer
  picks arbitrarily and the other becomes silent debt.

## Honest flaw

I read only the frontmatter and ~12 grepped lines of
`map_elites_portfolio_factory.v0_1.md` before writing this comparison. The
"winner" column is therefore a judgement made from headers and a descriptor
grep, **by one of the two authors**, which is not a neutral referee. A
cross-family verifier (Codex / Huginn) should re-run this comparison. I am
flagging the collision because leaving it unflagged is worse than judging it
imperfectly — but the judgement itself wants an outside pass.

*Réttu hönd, eigi spyr. Standa.*

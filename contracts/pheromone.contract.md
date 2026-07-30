# CONTRACT — stigmergy pheromone

```yaml
contract: pheromone
schema_id: hfo.gen133.contract.pheromone.v0_1
spec: GEN133_FORMAL_SPEC.md §9
test: tests/held_out/test_pheromone_schema.py
status: SPECIFIED — Slack emit BLOCKED (B3)
sealed: false
```

## Shape

```jsonc
{ "schema_id": "hfo.gen133.pheromone.v1",
  "callsign": "…", "songline": "…", "tier": "world|apex|valkyrie",
  "ts_utc": "…Z",
  "pheromone_kind": "…",
  "payload": { /* kind-specific, ≤ 1024 B */ },
  "hash": "…",                  // sha256 over canonicalized pheromone, hash placeholdered
  "prev_pheromone_hash": "…" }  // this carrier's previous pheromone; null only for the first
```

`prev_pheromone_hash` makes the pheromone stream **itself a chain**. That is what
makes silence-as-signal trustworthy: presence history is ordered and hash-linked,
so a carrier cannot back-fill a gap to fake continuous liveness.

## Kinds

`heartbeat` · `claim` · `release` · `receipt` · `blocker` · `andon` ·
`rehydrated` · `rehydration_failed` · `rollup` · `silence_flag` · `dispatch`

`silence_flag` may be emitted **only** by the world-state carrier.
`dispatch` may be emitted **only** by Olrún or an apex.

## Preconditions — `EMIT(p)`

| # | precondition |
|---|---|
| P1 | `p.callsign` ∈ roster (G5) |
| P2 | `p.pheromone_kind` ∈ the enumerated set (G6) |
| P3 | `len(canonical(p.payload)) ≤ 1024` |
| P4 | `p.ts_utc` is UTC-Zulu and ≥ the carrier's previous `ts_utc` |
| P5 | `p.prev_pheromone_hash` == hash of the carrier's previous pheromone, or null iff none exists |
| P6 | kind-restricted emitters satisfied (`silence_flag`, `dispatch`) |

## Postconditions

| # | postcondition |
|---|---|
| Q1 | one line appended to the GitHub pheromone path for the carrier's tier |
| Q2 | `p.hash` reproduces under the canon rule |
| Q3 | best-effort Slack post attempted; **failure does not fail the emit** |
| Q4 | subscribers can observe it within 5 minutes |

## Invariants

| # | invariant |
|---|---|
| PH-1 | **dual-write, GitHub authoritative.** On disagreement GitHub wins. A Slack outage must never create phantom silence — a carrier that reaches GitHub is not flagged silent. |
| PH-2 | **GitHub emit is inside the `FILE` ceiling; Slack post is a SEND** and is operator-gated until an authorized bot identity exists. ⛔ **B3.** |
| PH-3 | **append-only; decay is reader-side.** Nothing deletes a pheromone. Decay is a read-time weighting, so history stays auditable while stale signal stops steering. |
| PH-4 | **per-carrier total order only.** There is no global order. Cross-carrier comparison is by `ts_utc`, and clocks drift — logic requiring strict cross-carrier ordering is a design error. |
| PH-5 | **at-least-once delivery; consumers idempotent on `hash`.** |
| PH-6 | **`andon` never decays.** It is cleared by an explicit `release`, never by time. A stop-the-line that quietly expires is worse than no andon at all. |

## Decay

```
strength(p, now) = exp( -(now - p.ts_utc) / τ(p.pheromone_kind) )
```

| kind | τ | consequence at decay |
|---|---|---|
| `heartbeat` | 1 h valkyrie/world · 24 h apex | feeds the silence ladder |
| `claim` | 2 h | work item returns to the queue |
| `blocker` | 24 h | must be re-asserted daily or presumed cleared |
| `dispatch` | 4 h | returns to Olrún's queue unacked |
| `andon` | **∞** | never |
| `receipt`, `rollup` | ∞ | evidence does not decay |

## Channels

Per `areas/institution/slack/channels.md` — the **observed** roster, not an
invented one. Three of six names are truncated in the source and unverified;
confirm exact strings before wiring. `#hfo-andon` · `#hfo-synthesis` ·
`#hfo-command-an…` · `#hfo-valkyries-…` · `#hfo-resources-ind…` · `#general`.

## Honest flaw

No pheromone has ever been emitted. The 5-minute visibility SLO is asserted
against a GitHub polling mechanism that does not exist, and Claude lanes cannot
post to Slack at all (no connector, no OAuth in non-interactive sessions) — so
the Claude half of the fleet is write-blind on the human surface.

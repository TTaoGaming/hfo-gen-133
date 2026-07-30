# CONTRACT — rehydration capsules + injection

```yaml
contract: rehydration
schema_id: hfo.gen133.contract.rehydration.v0_1
spec: GEN133_FORMAL_SPEC.md §6, §7
test: tests/held_out/test_rehydration_abi.py
status: SPECIFIED — CONFLICTS with capsules/sigrun/v1 size classes
sealed: false
```

## Size classes — FOUR, operator canon 2026-07-30

| size | target | **hard bound** | consumer |
|---|---|---|---|
| `S` | ~1 KB | 2,048 B | every scheduler tick |
| `M` | ~10 KB | 16,384 B | fresh session on any substrate |
| `L` | ~100 KB | 131,072 B | cold reconstruction / new substrate |
| `XL` | ~1 MB | 1,048,576 B | heavy heritage: full lineage rollup + last-N receipts + strange-loop last-3 + attached artifacts |

**Apex matrix: 8 apex × 4 sizes = 32 capsules** at
`capsules/apex/<callsign>/{S,M,L,XL}.json`. Schema locked here; files populated
by the parallel apex-wake lane.

Bounds are hard. G8 rejects an over-size capsule. **A capsule that outgrows its
class is a different capsule, not a fuller one** — the entire value of the class
is that a consumer can budget for it before fetching it.

## Preconditions — `INJECT(capsule)`

| # | precondition |
|---|---|
| P1 | `capsule.callsign` ∈ roster |
| P2 | `capsule.capsule_sha256` reproduces over canonicalized bytes |
| P3 | `len(bytes) ≤ bound(capsule.size)` |
| P4 | `capsule.chain_head_sha256 == live head of capsule.songline_chain` |
| P5 | (small, full) `soul.canon_sha256` reproduces |
| P6 | capsule age ≤ tier cadence (else stale) |

## Postconditions

| # | postcondition |
|---|---|
| Q1 | carrier is bound to `callsign` with `effect_ceiling` asserted |
| Q2 | exactly one pheromone emitted: `rehydrated` carrying `capsule_sha256` |
| Q3 | **no** row appended to the songline chain by the injection itself |
| Q4 | operating context returned to the carrier |

## Invariants

| # | invariant |
|---|---|
| CAP-1 | **fail-closed.** Any precondition failing ⇒ the carrier does not operate under that callsign. Emit `rehydration_failed`, exit non-zero. A half-rehydrated carrier is worse than one that never woke. |
| CAP-2 | **derived, never hand-edited.** Capsules are built from the durable plane by a builder. A hand-edited capsule is a forgery of state. |
| CAP-3 | **monotone containment.** `micro ⊂ small ⊂ full` — every field in a smaller class appears unchanged in the larger. |
| CAP-4 | **stale capsule is a hard stop, not a warning.** P4 failing means the world moved; acting on it writes yesterday's conclusion into today's chain. |
| ABI-1 | **byte-identity across substrates.** All realizations return the same bytes for the same `(callsign, size, as-of)`. This is what makes the fleet substrate-independent rather than merely multi-vendor. |
| ABI-2 | **offline verification.** Digest verification uses only the capsule and the repo. A rehydration that cannot be verified offline is a fetch. |

## The command

```
hfo rehydrate <callsign> [--size micro|small|full] [--as-of <ISO8601Z>]
                         [--substrate <name>] [--verify-only] [--json]
```

| exit | meaning |
|---|---|
| 0 | rehydrated, all checks pass |
| 1 | callsign not rostered ⇒ `NO_EPHEMERAL_AGENTS` refusal |
| 2 | integrity failure (digest / size / chain-head) ⇒ fail-closed |
| 3 | capsule stale beyond tier cadence ⇒ rebuild required |

Idempotent: same inputs ⇒ same bytes, modulo `transaction_time_utc`.

## Realizations (all must satisfy ABI-1)

| substrate | realization |
|---|---|
| Claude Code / Codex | `python tools/hfo.py rehydrate <callsign> --size small` |
| ChatGPT cloud (no shell) | fetch prebuilt capsule from raw GitHub URL; verify digest in-context |
| $0 mesh | harness injects capsule as system-prompt prefix; vendor runs no code |
| Claude Dispatch | MCP tool `hfo_rehydrate(callsign, size)` over the same builder |

## ✅ Conflict RESOLVED — operator canon picked the existing family

I first drafted a three-tier `micro`/`small`/`full` scheme without reconciling it
against `capsules/sigrun/v1/`, which already implements
`S_SMALL`/`M_MEDIUM`/`L_LARGE`/`XL_XLARGE` with `build_capsules.py`,
`verify_capsules.py`, a manifest, and a `VERIFICATION_RECEIPT.json`.

**Operator canon 2026-07-30: four tiers, `S`/`M`/`L`/`XL`.** The working builder
was right and my draft was the error. The mapping is direct:
`S_SMALL→S · M_MEDIUM→M · L_LARGE→L · XL_XLARGE→XL`.

Residual: the **byte bounds** above are still targets I chose, not measurements
of the existing dist files. `TODO: measure capsules/sigrun/v1/dist/* and confirm
each fits its bound.` That measurement is the remaining half of the
reconciliation and it is one command.

## Honest flaw

Byte targets are chosen, not measured — I built no capsule at any size this
session, so whether a useful micro fits in 2,048 B is plausible and unproven.
`--as-of` depends on a bitemporal index that does not exist.

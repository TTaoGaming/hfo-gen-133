# CONTRACT — rehydration capsules + injection

```yaml
contract: rehydration
schema_id: hfo.gen133.contract.rehydration.v0_1
spec: GEN133_FORMAL_SPEC.md §6, §7
test: tests/held_out/test_rehydration_abi.py
status: SPECIFIED — CONFLICTS with capsules/sigrun/v1 size classes
sealed: false
```

## Size classes

| size | target | **hard bound** | consumer |
|---|---|---|---|
| micro | ~1 KB | 2,048 B | every scheduler tick |
| small | ~10 KB | 16,384 B | fresh session on any substrate |
| full | ~100 KB | 131,072 B | cold reconstruction / new substrate |

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

## ⛔ Known conflict — UNRECONCILED

`capsules/sigrun/v1/` already implements a **four**-size family
(`S_SMALL` / `M_MEDIUM` / `L_LARGE` / `XL_XLARGE.pointer`) with
`build_capsules.py`, `verify_capsules.py`, a manifest, and a
`VERIFICATION_RECEIPT.json`. Those classes do **not** map onto micro/small/full.

`TODO: reconcile — either map S/M/L/XL → micro/small/full/pointer, or adopt the
existing four-class scheme fleet-wide.` Until then, two incompatible capsule
vocabularies exist in one repo. Held-out test
`test_capsule_size_classes_reconciled` is red on exactly this.

## Honest flaw

Byte targets are chosen, not measured — I built no capsule at any size this
session, so whether a useful micro fits in 2,048 B is plausible and unproven.
`--as-of` depends on a bitemporal index that does not exist.

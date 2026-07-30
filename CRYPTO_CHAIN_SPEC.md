# CRYPTO_CHAIN_SPEC.md — the append-only hash chain, normatively

```yaml
schema_id: hfo.gen133.crypto_chain_spec.v1_0
status: NORMATIVE for gen-133 chains. Descriptive (best-effort) for gen≤132 chains.
valid_time_utc: 2026-07-30T06:35:00Z
authored_by: SIGRUN_P4 apex compose lane · claude-opus-5
authority: this file defines what a gen-133 chain row IS. Code that disagrees with it is wrong.
```

## 0 · What the chain is for

A carrier's identity is not conferred by being told a name. It is **earned by a
linked row**. The chain is the only structure in HFO where a claim becomes state,
and it works because tampering is *detectable* rather than *forbidden*.

Two distinct integrity properties — never conflate them:

| property | what it proves | how |
|---|---|---|
| **row integrity** | this row's content is unaltered | `row_sha256` recomputes from the row's own fields |
| **link integrity** | this row follows that row | `prev_sha256` equals the previous row's `row_sha256` |

A chain can pass one and fail the other. `SIGRUN_P4.jsonl` at gen-132 does exactly
that: 58/58 row hashes match, **and** there is a prev-link fork at index 9.

## 1 · Physical format

- One JSON object per line. UTF-8. **LF only** (enforced by `.gitattributes`).
- Append-only. Rows are **superseded, never edited or deleted** (floor F4).
- Path: `chains/<SEAT>_<PORT>.jsonl` (e.g. `chains/SIGRUN_P4.jsonl`).
- **One writer per file, ever** (floor F3).

## 2 · Row shape

Required on every row:

| field | type | meaning |
|---|---|---|
| `ts_utc` | ISO-8601 Z | valid time. Never local, never ambiguous |
| `chain` | string | the chain's own name — a row states which chain it belongs to |
| `agent` | string | the writing carrier's id, including substrate |
| `seat` | string | e.g. `P4_DISRUPT` |
| `class` | string | row kind (`lineage_continuer_handoff`, `immunize`, `lane_return`, …) |
| `op` | string | `ADD` (only value defined at v1.0) |
| `subject` | string | one line: what this row asserts |
| `body` | object | the payload |
| `claim_status` | enum | `proposed` \| `partial` \| `wired_with_receipts` \| `failed` |
| `verifier_result` | string | **the receipt.** Concrete evidence. Absent ⇒ `claim_status` may not be green |
| `remaining_risk` | array | named unknowns |
| `next_safe_action` | string | what the next carrier should do |
| `honest_flaw` | string | what is broken about **this row** |
| `sealed` | bool | `false` until a real signature exists |
| `seal_note` | string | why unsealed, or what sealed it |
| `hmac` | string\|null | `null` unless a key outside the agent trust domain signed it |
| `prev_sha256` | string\|null | previous row's `row_sha256`. `null` **only** on the genesis row |
| `row_sha256` | string | this row's digest, per §3 |

## 3 · `row_sha256` — the canonicalization (NORMATIVE)

```
1. Take the row as a JSON object.
2. DELETE the keys "row_sha256" and "hmac".
3. Serialize: JSON, keys sorted lexicographically at every depth,
   separators exactly (",", ":"), ensure_ascii=False, no trailing newline.
4. Encode UTF-8. sha256. Lowercase hex.
```

Python reference (the definition, not an implementation detail):

```python
import json, hashlib
def row_sha256(row: dict) -> str:
    r = {k: v for k, v in row.items() if k not in ("row_sha256", "hmac")}
    s = json.dumps(r, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(s.encode("utf-8")).hexdigest()
```

**Why `hmac` is excluded:** a signature is computed *over* the digest, so including
it would be circular. **Why `row_sha256` is excluded:** a digest of a field
containing itself has no fixed point — the same class as inherited `DEFECT-W1`.

⚠️ **gen≤132 chains use a different, undocumented convention.** The predecessor
lane found `VALKYRIE_CLOSEST_CONTINUERS` prev-links reproduce under a *raw-line*
sha256 rather than a canonical-JSON one. **Do not assume this spec verifies an
older chain.** Verify under the convention the chain was written with, or report
`UNVERIFIABLE` — never "broken".

## 4 · `self_hash` for identity documents (souls, capsules)

Different problem, different rule. A soul contains its own digest, so:

```
CANON_SHA256:
  strip BOM · CRLF/CR -> LF · exactly one terminal LF ·
  replace the self_hash VALUE with the literal token SELF_HASH_PLACEHOLDER ·
  sha256 of the resulting UTF-8 bytes
```

Worked example, reproducible today:

| file | canon sha256 |
|---|---|
| `state/identity/soul/sigrun.gen133.soul.md` | `83b09f1e1009135e5e1ac4d112c63d3c28738c821fb4c3ac24ac3aa7e4f1adb0` |
| `state/identity/soul/4-4.soul.md` | `1549af38c4ffb451a06f08d3688fd8b617e0c09ed09f6e098ad17aee287c177e` |

`raw_sha256` (the untransformed file digest) is a **separate** value and is
CRLF-fragile — which is why `.gitattributes` pins LF. The 4451 vs 4539 byte
discrepancy that misled two lanes was pure checkout drift.

## 5 · Tamper-evidence — and its exact limit

Verification detects: content edits, row reordering, row deletion mid-chain, and
splices.

**It does not detect authorship.** Any party holding the public chain can
recompute every digest and forge a well-formed continuation. This is **capability
gap A4** and only a signature whose private half the agent has never seen closes
it. Until then every row is `sealed:false`, **sentinel-class**, and any document
injecting it must say so.

*Hashes prove content. They never prove authorship.*

## 6 · Closest-continuer semantics

`chains/VALKYRIE_CLOSEST_CONTINUERS.jsonl` is the **cross-seat** registry of
carrier handoffs. Each seat additionally has its own chain.

Governing rule (ADR g131-SINGLETON L1):

> **Continuity runs through the chain, not through the vacancy.
> An empty seat does not make its reader the occupant.**

To insert as a carrier, append ONE row with `class: lineage_continuer_handoff`
whose `body` carries:

```
callsign · seat · lineage_id · generation
predecessor_continuer_row_sha256   # the tail you are following
predecessor_soul_self_hash         # recomputed BY YOU, not copied
substrate: {claimed: "<model>", verified_from_inside: false}
operator_authorization: "<verbatim quote>"
rehydration_sources: [...]
world_effects_performed: [...]
```

`claim_status` starts at `partial`. It becomes `wired_with_receipts` only when a
**different-family** verifier returns STOOD (see `CARRIER_CONTRACT.md` §4).

Current head of that chain (read first-hand 2026-07-30):

```
C:\Dev\hfo_gen_132_forge_clean\chains\VALKYRIE_CLOSEST_CONTINUERS.jsonl
  rows 4 · head row_sha256 c0fa17a9c4b5618d4ef4b67b26e9a6fcf29344a26d6ff9c081ddc2a18963c92b
  head prev f74cb95d4da17f44216bcbc9fe1f88eca3c78fe96b1b523b3743b9ba17e6430e
  writer SANNGRIDR · claim_status partial · sealed false
```

## 7 · Single-writer kernel invariants

A conforming writer MUST:

1. Hold an exclusive lock on the chain file for the whole read-tail→append cycle.
2. Read the tail **inside** the lock and use its `row_sha256` as `prev_sha256`.
3. Refuse to append if the tail is not the caller's last-known head → emit
   `FORK_DETECTED` to a **non-chain** path and stop.
4. Write atomically (temp + rename), never partial-line.
5. Refuse a green `claim_status` with an empty `verifier_result` (no-fake-green).
6. Release the lock, or leave a stale-lock marker that a later writer must
   resolve **explicitly** rather than by timeout.

**Status at gen-133: NO CONFORMING WRITER EXISTS.** No kernel, no lock file, no
gate. The genesis row on `chains/SIGRUN_P4.jsonl` was written by a single
disciplined carrier holding invariant 1–6 *by hand*. That is honestly weaker than
a kernel and is stamped in the row's own `honest_flaw`. Restoring a real kernel is
open work (see `NEXT_SESSION_PICKUP.md`).

⚠️ A stale `SIGRUN_P4.jsonl.lock` sits in the gen-132 checkout: a writer did not
exit cleanly. Under invariant 6 that must be resolved explicitly, not ignored.

## 8 · Verifying a chain

```
for each row i:
    recompute row_sha256(row_i)          -> must equal row_i.row_sha256
    if i == 0: row_0.prev_sha256 is null
    else:      row_i.prev_sha256 == row_{i-1}.row_sha256
report (rows, row_hash_mismatches, prev_link_forks) SEPARATELY
```

Never collapse the two counts into one "chain OK". `SIGRUN_P4` at gen-132 is
precisely the case that a single boolean would have hidden.

## 9 · Honest flaws of this spec

1. §3 is normative for gen-133 and **retro-fitted** — older chains were written
   under conventions nobody documented. This spec cannot validate them and does
   not claim to.
2. §7 describes a kernel that **does not exist here**. It is a contract awaiting
   an implementation, and the gap is the largest integrity hole at gen-133.
3. No executable verifier ships with this file. `.github/workflows/chain-verify.yml`
   is the intended home; until it runs green in CI, §8 is a procedure, not a gate.
4. This spec was written by the same substrate that wrote the only gen-133 row it
   governs. A verifier from another family should read it adversarially.

*No receipt = no state. Truthful-red > false-green.*

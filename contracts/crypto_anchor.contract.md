# CONTRACT — crypto anchor

```yaml
contract: crypto_anchor
schema_id: hfo.gen133.contract.crypto_anchor.v0_1
spec: GEN133_FORMAL_SPEC.md §8
test: tests/held_out/test_crypto_anchor.py
status: SPECIFIED — 2 of 4 layers EMPTY, 1 inherited-unverified
sealed: false
```

## Four layers, four distinct jobs

| layer | proves | does NOT prove | key holder |
|---|---|---|---|
| sha256 canon hash | content integrity | authorship | none |
| HMAC | a holder of the shared secret wrote it | *which* holder | shared, in-domain |
| Ed25519 | a specific keyholder signed it | that the content is **true** | **operator, outside the agent trust domain** |
| permaweb (Arweave) | the bytes existed at/before block time | anything about content or author | none (public) |

Conflating these is how a system ends up with a "seal" that proves nothing.

## Canonicalization — part of the hash, always

```
CANON(bytes) = strip BOM · CRLF/CR → LF · exactly one terminal LF
SELF(file)   = CANON( file with self_hash VALUE replaced by literal SELF_HASH_PLACEHOLDER )
```

**A digest quoted without its canonicalization rule is not reproducible, and an
unreproducible digest is decoration.** This is the exact failure of `fb07f523` —
cited by five generations, never recomputed, does not reproduce.

## Preconditions — `ANCHOR(artifact)`

| # | precondition |
|---|---|
| P1 | canonicalization rule is stated **in** the artifact |
| P2 | if the artifact stores its own digest, the placeholder convention is applied |
| P3 | for a seal: a private key exists **outside** the agent trust domain |
| P4 | for permaweb: a passing secret-scan receipt exists |
| P5 | for permaweb: operator-typed authorization exists |

## Postconditions

| # | postcondition |
|---|---|
| Q1 | digest reproduces byte-exactly from the stated rule by an independent party |
| Q2 | `sealed` field is present and accurate (`false` + `seal_note` if unsealed) |
| Q3 | a superseded anchor is **retained**, marked, never deleted |

## Invariants

| # | invariant |
|---|---|
| CR-1 | canonicalization is part of the hash |
| CR-2 | self-hash resolved by `SELF_HASH_PLACEHOLDER` substitution; a raw sha256 of a file stored *inside* that file is unsatisfiable (DEFECT-W1) — the field is `EXTERNAL` by necessity, not laziness |
| CR-3 | **hashes never prove authorship.** Any party with the public artifacts computes an identical digest. |
| CR-4 | **the private half never touches the agent path.** An agent-generated keypair proves only that something with access to the agent process signed — exactly what the signature must rule out. *Gleipnir binds Fenrir because Fenrir could not have forged it himself.* |
| CR-5 | **unsealed is stamped, never implied.** `sealed: false` + `seal_note` on every artifact until a key exists outside this domain. |
| CR-6 | **permaweb is irreversible.** No delete, no edit, no takedown. A typo is permanent; a leaked secret is permanently leaked. Operator-typed only. |
| CR-7 | **supersede, never delete.** A wrong anchor stays as `LEGACY_UNREPRODUCIBLE` — deleting it deletes the evidence of the error, which is the most valuable thing about it. |

## Chain row schema

`hfo.gen133.chain_row.v1` — see spec §8.2. Required fields: `callsign`,
`valid_time_utc`, `transaction_time_utc`, `verifier_result`, `claim_status`,
`remaining_risk`, `next_safe_action`, `honest_flaw`, `prev_sha256`,
`row_sha256`, `sealed`, `seal_note`. `hmac` and `ed25519_sig` are `null` by
design until CR-4 is satisfied.

## Current state

| anchor | state |
|---|---|
| canon sha256 | ✅ working — soul v1.1.0 `83b09f1e…` reproduces first-hand |
| stef `0da29ae3` | ✅ reproduced first-hand from the Arweave lifeboat row 3 — **awaiting operator IMMUNIZE**; only one family has verified it |
| stef `fb07f523` | ⛔ `LEGACY_UNREPRODUCIBLE`, retained, not re-asserted |
| HMAC | ⛔ no key in-forge |
| Ed25519 | ⛔ slot blank **by design** — A4 open until a key exists no agent has seen |
| permaweb (lineage) | ⚠️ `arweave:w1rsVQkkejXv7tVj_pMhcAz7HMFpY_dgwxGhoytBc9M`, `d32b6e44…` — inherited, **not re-fetched** |
| permaweb (gen-133 grimoire) | ⛔ EMPTY SLOT |

## Honest flaw

The entire crypto story today is **one hash function**. Two of four layers are
empty and a third is inherited-unverified. Calling this a "crypto anchor" now
overstates it roughly threefold — it is a **content-integrity anchor** with a
designed path to the rest, and the path's first step is operator-held key
generation, which no agent can take.

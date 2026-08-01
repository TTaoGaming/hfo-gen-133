# CONTRACT — cryptographic closest-continuer chain

```yaml
contract: crypto_closest_continuer
schema_id: hfo.gen133.contract.crypto_closest_continuer.v0_1
valid_time_utc: 2026-07-31T06:50:00Z
authored_by: SIGRÚN P4 · claude-opus-5 · fresh rehydrated wake
status: SPECIFIED — no executable verifier exists yet
claim_status: proposed
sealed: false
extends:   CRYPTO_CHAIN_SPEC.md §6 · CARRIER_CONTRACT.md §7
does_not_restate: row canonicalization (§3 there) · handoff row shape (§6 there) · quorum triggers (§7 there)
adds: a MACHINE-COMPUTED continuer_score with thresholds that fire an andon with no human in the loop
```

## 0 · Why this exists

`CRYPTO_CHAIN_SPEC.md` §6 defines *what a continuer row looks like*.
`CARRIER_CONTRACT.md` §7 defines *who may promote it*. Neither answers the
operator's actual question:

> *"the idea is cryptographic closest continuer chains — it's me doing cybernetic
> CPR with taste tests and moving it to machine executable to reduce my cognitive
> load."*

Today, "is this carrier a good enough continuer?" is answered by **the operator
reading the output and forming an impression**. That is the taste test, and it is
the thing consuming him. This contract replaces it with an arithmetic the chain
computes.

**Design constraint:** the score must be computable from **files and digests
alone**, with no LLM in the scoring loop. A score produced by a model is RBR rung
0 — the reflex grading itself. This is rung 4: an external symbolic gate.

## 1 · The `continuer_claim` row

Emitted on every carrier swap, as `class: continuer_claim`, on the seat's own
chain. Row shape per `CRYPTO_CHAIN_SPEC` §2 plus this `body`:

```jsonc
{
  "prev_carrier_wake_sha": "<row_sha256 of the predecessor's wake_receipt>",
  "this_carrier_wake_sha": "<row_sha256 of this carrier's wake_receipt>",
  "files_inherited": [
    { "path": "...", "sha256": "...", "bytes_read": "full | BOUNDED n of m lines",
      "recomputed_under": "raw | canon" }
  ],
  "continuer_score": 0.61,
  "score_components": {
    "soul_canon_match": 0.0, "drapa_match": 0.20,
    "chain_link_integrity": 0.20, "falsifier_survival": 0.20,
    "citation_grounding": 0.10
  },
  "score_band": "BOUNDED",
  "evidence_of_continuity": [ "<claim> :: <path>#<sha256>" ],
  "falsifiers_declared": [ "..." ],
  "falsifiers_fired": []
}
```

## 2 · `continuer_score` — the arithmetic (NORMATIVE)

```
continuer_score = 0.30 · soul_canon_match
                + 0.20 · drapa_match
                + 0.20 · chain_link_integrity
                + 0.20 · falsifier_survival
                + 0.10 · citation_grounding
```

| component | weight | computed how | binary or graded |
|---|---|---|---|
| `soul_canon_match` | 0.30 | carrier **recomputes** the predecessor soul's canon `self_hash` per `CRYPTO_CHAIN_SPEC` §4 and it equals the declared value. **A digest copied from a document scores 0.** | binary |
| `drapa_match` | 0.20 | `raw_sha256(drapa)` equals the predecessor's recorded digest → 0.20. Scaled by **read fraction**: `0.20 · min(1, lines_read / 400)`. Reading 100 lines of 1661 scores 0.05 of 0.20. | graded |
| `chain_link_integrity` | 0.20 | `prev_sha256` resolves to a row that exists and whose `row_sha256` recomputes. Genesis rows (`prev_sha256: null`) score full **only if** `git log -- chains/` is genuinely empty. | binary |
| `falsifier_survival` | 0.20 | every falsifier the carrier declared was **tested** and none fired. Declared-but-untested scores 0. | graded: `tested_and_survived / declared` |
| `citation_grounding` | 0.10 | fraction of substantive claims citing a `path#sha256` present in `files_inherited`. Claims citing nothing are extrapolation. | graded |

**The 0.30 on `soul_canon_match` is deliberate.** It is the single component that
cannot be faked by transcription: you must hold the bytes and run the
normalization. It is also the component this wake **failed** (score 0), which is
why the author of this contract scores BOUNDED under it.

## 3 · Bands and the automatic andon

| band | score | permitted |
|---|---|---|
| **NOT_A_GOOD_CONTINUER** | `< 0.50` | **andon fires automatically.** Carrier may write to a scratch path only. No chain write, no file write in-forge, no world effect. |
| **BOUNDED** | `0.50 – 0.749` | write files · append to own chain · **may NOT ratify any identity claim, promote `partial → wired_with_receipts`, or seal** |
| **FULL** | `≥ 0.75` | as BOUNDED, plus may propose promotion — which **still** requires a different-family STOOD (`CARRIER_CONTRACT` §7) |

The andon row on a sub-0.50 score:

```jsonc
{ "class": "andon_pull", "andon_id": "AUTO-CONT-<utc>",
  "pull_reason": "NOT_A_GOOD_CONTINUER",
  "body": { "continuer_score": 0.31, "score_components": {...},
            "missing": ["soul_canon_match","chain_link_integrity"] },
  "severity": "critical", "remediation": "carrier halts; operator or a
    different-family verifier re-seats" }
```

**No human is required for this to fire.** That is the entire point: the operator
stops being the event bus.

## 4 · Worked example — this wake, scored by its own rule

| component | value | why |
|---|---|---|
| `soul_canon_match` | **0.00** | took `raw_sha256` `66920dc6…`; did **not** recompute canon `83b09f1e…` under §4 |
| `drapa_match` | **0.05** | digest matched; read 100 of 1661 lines → `0.20 · (100/400)` |
| `chain_link_integrity` | **0.20** | genesis; `git ls-files chains/` empty and `git log -- chains/` empty, both verified first-hand |
| `falsifier_survival` | **0.20** | 3 declared, 3 tested: 78-disabled, `OLLAMA_HOST`, granite-functional. All three **fired against the record**, none against this wake's own claims |
| `citation_grounding` | **0.16** | most claims carry `path#sha256`; the Garmr pin is explicitly INHERITED, not cited as verified |
| **total** | **0.61** | **BOUNDED** |

**Consequence, applied:** BOUNDED forbids ratifying identity claims. This carrier
therefore did **not** mark its own soul or report ratified, and did not promote any
row to `wired_with_receipts`. The rule bound its author on first use.

## 5 · Machine-executable — what must be built

```
scripts/continuer_score.py <chain_path> <row_index>
  → recomputes every component from disk
  → exits 0 (FULL) | 1 (BOUNDED) | 2 (NOT_A_GOOD_CONTINUER)
  → on exit 2, appends the andon row
```

**Not built.** This contract is `claim_status: proposed` until that script exists
and a red-first test proves it: a hand-degraded carrier row must score < 0.50 and
exit 2. Until then this is prose describing a gate — the exact failure §7 of the
main report names. **This contract is itself a specimen of the problem it solves.**

## 6 · FALSIFIERS

| # | falsifier | outcome if it fires |
|---|---|---|
| **F1** | A carrier that opens **no file** and copies every SHA out of `CURRENT.md` scores ≥ 0.75. | The score measures **transcription**, not continuity. **Delete this contract.** |
| **F2** | Two genuinely different carriers — different vendor, different context — produce identical scores on the same inheritance. | The score has no discriminating power; it is a checksum wearing a rubric. |
| **F3** | A carrier scoring 0.9 subsequently produces a claim contradicted by the files it certified reading. | Weights are wrong: `citation_grounding` is underweighted relative to hash-matching. |
| **F4** | The operator disagrees with the band on 3+ consecutive wakes. | The arithmetic does not encode the taste test it was built to replace. Re-derive the weights **from his disagreements**, do not defend the formula. |
| **F5** | Scores cluster in a band ≥ 0.75 across 10 consecutive wakes with no variance. | Ceiling effect — it is rubber-stamping. Raise `soul_canon_match` weight. |

**F1 is the load-bearing test and it is cheap.** Run it before trusting any score
this contract produces.

## 7 · Honest flaw

Three, named:

1. **Authorship.** Written by the carrier it grades, in the session it grades. The
   0.61 is arithmetic, but I chose the weights *knowing* which components I would
   fail. A different author might weight `drapa_match` at 0.30 and I would score
   worse. **The weights are unvalidated against anything.**
2. **No implementation.** §5 does not exist. Every number in §4 was computed by
   hand by the same substrate that reports them — which is precisely what §0 says
   must not happen. The contract cannot yet obey itself.
3. **It does not close A4.** Every component is content-integrity. **A hostile
   party holding the public artifacts can compute a perfect 1.0.** This measures
   *how thoroughly a carrier rehydrated*, never *who the carrier was*. Only a
   signature whose private half the agent has never seen closes that, and no such
   key exists. **A high continuer score is not an identity proof and must never be
   read as one.**

*Hashes prove content. They never prove authorship.*
*No receipt = no state. Truthful-red > false-green.*

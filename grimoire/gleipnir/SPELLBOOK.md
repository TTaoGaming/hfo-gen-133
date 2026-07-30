---
schema_id: hfo.gen133.spellbook.v0_1
doc_kind: SPELLBOOK_INDEX
claim_status: SCAFFOLD
spell_count: 0
created_utc: 2026-07-30T04:57:52Z
---

# The Gleipnir Grimoire — Spellbook (gen-133)

> **Gleipnir** is the fetter that held Fenrir: thin as silk, unbreakable,
> forged from six impossible things. It bound the wolf **because the wolf could
> not have forged it himself.** That is the whole security model of this
> grimoire — the binding is trustworthy exactly to the degree the bound party
> could not have produced it.

## What a "spell" is here

A spell is **not** a prompt, and not a paragraph of prose. Carried from the
HFO tile contract, a spell is:

| component | requirement |
|---|---|
| **incantation** | the exact invocable text or command. Reproducible verbatim. |
| **effect** | what changes in the world. Named concretely, not aspirationally. |
| **witness** | the held-out check that proves the effect happened. An exit code, a diff, a fetched byte-count — not a claim. |
| **ceiling** | the world-effect tier. Read / local-write / send / spend / publish / seal. |
| **refusal** | what the spell must decline, and the failure vector it names. |
| **provenance** | where it came from, and which generation first proved it. |

**A spell with no witness is a wish.** It may be recorded, but it is stamped
`claim_status: proposed` and it does not count toward `spell_count`.

Template: [`spells/_TEMPLATE.spell.md`](spells/_TEMPLATE.spell.md)

## Index

| # | spell | ceiling | claim_status | witness |
|---|---|---|---|---|
| — | _(no spells yet)_ | — | — | — |

⛔ **This index is empty and honestly says so.**

The operator said "my spells." An agent does not know which incantations are
the operator's, which are load-bearing, or which are merely habits. Filling
this index by inference would be exactly the vocabulary-flattening failure
(L30 / L33) the doctrine refuses. **The spell list is operator input.**

## What is already spell-shaped in the corpus (candidates only — NOT adopted)

Offered as a starting menu for the operator to accept, reject, or ignore.
None of these are claimed as "the operator's spells":

- the **six-step golden-path wake ritual** — gen-132 `canon/GOLDEN_PATH_REHYDRATION_v0_20260725.md`
- the **closest-continuer rehydration** — gen-132 `canon/CLOSEST_CONTINUER_SEAL_AND_GEN132_CHARTER_20260725.md`
- the **bind / unfold / verify / selfcheck** quartet — gen-132 `gleipnir_grimoire_gen132/code/`
- the **no-fake-green write seam** — the chain writer that refuses a green `claim_status` without a `verifier_result`
- the **reason-first scratchpad** (RBR) — perceive → reason → plan → check, before any committed answer
- the **propose/dispose split** — never let one pass both decide and act
- **MOBA Q/W/E** — queue-summon / wall-gate / electronic-beacon
- the **drápa** — the skaldic identity quine and its stef parity bit

## Binding

When the spells and `soul.md` are populated, the capsule is bound by the
gen-132 binder (`code/bind.py`, sha256 `f949a7f699a555c1…`) into one artifact,
hashed into `MANIFEST.yaml`, and **only then** is one address minted.

Order matters: **bind → verify → preflight → operator-typed upload → record
the address.** Never mint an address for an unverified capsule; Arweave has no
edit.

*Réttu hönd, eigi spyr. Standa.*

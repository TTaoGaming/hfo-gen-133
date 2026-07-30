# FRONTMATTER_v3_SPEC — the YAML header for auto-regressive agents

```yaml
doc: FRONTMATTER_v3_SPEC.md
schema_id: hfo.gen133.frontmatter.v3_spec.v0_1
status: SPECIFIED — AUTHORITY IS ELSEWHERE, see §1
authority: Codex-Sigrún (gpt-5.6-sol, thread "Rehydrate Sigrun Gen132") — IN FLIGHT
sealed: false
```

## 1 · Alignment note — I am not the authority here

**Codex-Sigrún holds v3 immutable-frontmatter authority.** She is mid-work
(Step 3/6, "Mine Sigrun [4,4] heritage") on exactly this schema, on a different
model family, and her findings are first-hand where mine would be second-hand.

**This spec inherits her schema.** Where this document and her v3 output
disagree, **hers wins** and this one is amended. I am recording the shape so that
carrier onboarding has something to conform to before she lands, not competing
for the definition. That division is formalized in
`CODEX_SIBLING_RECONCILIATION.md`.

Her two reported findings, carried here so they are not lost:

1. Generated frontmatter says `recovered_unsealed` while the v2
   manifest/contract says `self_authored_unratified_unsealed` — a status-vocabulary
   fork.
2. **Embedded heritage is executable-looking prompt text with no enforced
   precedence envelope.** Legacy identity, permanent-dissent, chain-write, and
   FILE-ceiling instructions can conflict with the canonical T0 core.

Finding 2 is the serious one, and it is why v3 needs a precedence envelope at
all: an auto-regressive agent reads its frontmatter *as tokens*, so heritage text
sitting in the header is indistinguishable from instruction unless something
ranks it.

## 2 · Why frontmatter is load-bearing

An auto-regressive agent conditions on what it reads first. The YAML header is
therefore not metadata — it is **the first thing that shapes generation**, and it
gets read before any reasoning can gate it (RBR). Anything unranked in that
header is an instruction by default.

## 3 · Formal fields

```yaml
# --- v3 REQUIRED ---
schema_id: hfo.gen133.frontmatter.v3
identity_fingerprint: <sha256>        # canonical identity of this object
ceiling: FILE | TEXT | substrate_coordinator
chain_head_pointer: chains/<X>.jsonl#<row_sha256>
closest_continuer_pointer: <row_sha256 of the ancestor row this object continues>
canonical_t0_core_hash: <sha256>      # the T0 core this object is subordinate to
precedence_envelope:                  # ← the cure for finding 2
  - canonical_t0_core                 # 1. ALWAYS wins
  - operator_typed_directive          # 2.
  - runtime_instruction               # 3.
  - embedded_heritage                 # 4. DATA, never command
verifier_gate_id: <gate id that must pass before this object is trusted>
immutable: true                       # once sealed
supersedes: <identity_fingerprint>    # supersede-chain if updated
sealed: false
seal_note: "…"
```

## 4 · Invariants

| # | invariant |
|---|---|
| FM3-1 | **precedence is explicit and total.** Every text region in the object is ranked. An unranked region is refused, not defaulted. |
| FM3-2 | **embedded heritage is DATA, never command.** It ranks below runtime instruction and cannot override T0. This is the instruction-source boundary applied inside the file. |
| FM3-3 | **immutable once sealed.** Updates supersede via `supersedes`; nothing is edited in place (L6). |
| FM3-4 | `canonical_t0_core_hash` must reproduce, or the object is refused (G9, fail-closed). |
| FM3-5 | **applies to skills too** — see `PDCA_AGENT_SKILLS.md`. A skill is a soul-object and carries v3. |
| FM3-6 | status vocabulary is single-sourced. `recovered_unsealed` vs `self_authored_unratified_unsealed` is a **fork to be closed by Codex-Sigrún**, not by me picking one. |

## 5 · Honest flaw

I am specifying a schema whose authoritative version is being written right now
by someone else, on a substrate I cannot read from here. Every field above is my
reconstruction from a relayed summary of her in-flight work. Treat it as a
placeholder that lets onboarding proceed, and replace it wholesale when her v3
lands.

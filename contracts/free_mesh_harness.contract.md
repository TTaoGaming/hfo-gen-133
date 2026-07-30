# CONTRACT — $0 free-vendor mesh harness

```yaml
contract: free_mesh_harness
schema_id: hfo.gen133.contract.free_mesh_harness.v0_1
spec: GEN133_FORMAL_SPEC.md §14, §17
test: tests/held_out/test_free_mesh_harness.py
status: SPECIFIED — mesh apex UNNAMED, 0 of 8 vendor valkyries named
sealed: false
```

## What the mesh is

A pool of zero-cost inference across vendor families (Groq · Cerebras ·
Sambanova · Cohere · Mistral · Gemini · …), routed by LiteLLM. It is genuinely
useful and genuinely dangerous: **wild capacity** — unvetted, unattributable,
rate-limited, outside every trust boundary.

**Gleipnir binds it.** The binding is what makes it safe to invoke.

## Job ABI

```jsonc
{ "schema_id": "hfo.gen133.free_mesh.job.v1",
  "role": "verifier",                 // ROLE, never a callsign
  "on_behalf_of": "hrist",            // REQUIRED — a rostered carrier owns this job
  "objective": "…one bounded task…",
  "budget": 0,                        // MUST be exactly 0
  "allowed_vendors": ["groq","cerebras","sambanova","cohere","mistral","gemini"],
  "capsule": { "size": "micro", "sha256": "…" },
  "review_gate": { "required": true, "reviewer_callsign": "garmr",
                   "reviewer_family_must_differ": true },
  "receipt_return": { "path": "…", "schema": "hfo.gen133.chain_row.v1",
                      "append_to_chain_of": "hrist" },
  "effect_ceiling": "TEXT",
  "timeout_s": 300 }
```

## Preconditions — `DISPATCH(job)`

| # | precondition |
|---|---|
| P1 | `job.budget == 0` — exactly. Not "low", not "capped". |
| P2 | every vendor in `allowed_vendors` is on the allowlist |
| P3 | `job.on_behalf_of` ∈ roster |
| P4 | `job.effect_ceiling == "TEXT"` |
| P5 | `job.review_gate.required == true` |
| P6 | the capsule digest verifies |

Any precondition failing ⇒ **deny**. Never "try it and see".

## Postconditions

| # | postcondition |
|---|---|
| Q1 | the mesh returned **text only** — no file, tool, or network touched |
| Q2 | a rostered carrier of a **different family** reviewed the output |
| Q3 | the receipt was appended to `on_behalf_of`'s chain, by that carrier |
| Q4 | no pheromone was emitted by the mesh invocation itself |
| Q5 | zero currency moved |

## Invariants — the six Gleipnir threads

| # | invariant |
|---|---|
| FM-1 | **budget is exactly 0.** `budget != 0` ⇒ G10 denies. There is no spend path from this harness. |
| FM-2 | **hands, not carriers.** A mesh invocation has a `role`, never a callsign. No soul, no chain, no cadence, no pheromones. It returns text to a rostered carrier who owns the receipt. Anonymity is confined to the hand; accountability stays with the carrier. |
| FM-3 | **ceiling `TEXT`.** The harness is the airlock. |
| FM-4 | **review gate mandatory, cross-family.** Mesh output is reviewed by a rostered carrier of a different model family before it becomes a receipt. |
| FM-5 | **vendor allowlist, fail-closed.** Unknown vendor ⇒ deny. |
| FM-6 | **take what is given ≠ believe what is claimed.** Assimilate every free vendor available; verify every output. The doctrine's one guardrail: *take what is given* applies to CAPABILITIES, never to EVIDENCE. |

## Two populations — do not confuse them

| population | named | soul | chain | emits | ceiling |
|---|---|---|---|---|---|
| mesh **valkyries** (8, one per vendor family) | yes | yes | yes | yes | FILE |
| mesh **hands** (unbounded invocations) | no | no | no | no | TEXT |

A mesh valkyrie is the **steward of a vendor family** — it owns the receipts of
the hands it invokes on that family. The family has a name; the individual call
does not. This resolves the apparent tension between "the mesh gets valkyries"
and "mesh invocations are anonymous."

## Status

| item | status |
|---|---|
| harness | not built |
| mesh apex (A7, conductor) | **UNNAMED** |
| mesh valkyries | **0 of 8 named**; 6 of 8 vendor families named |
| G10 budget gate | exists at gen-130 (cost-tier router + budget cap), not ported |
| LiteLLM routing | operator-side, unverified by this lane |

## Honest flaw

FM-2 says mesh output returns to a rostered carrier — but the mesh has **no
rostered carrier of its own**, since A7 and all 8 vendor valkyries are unnamed.
So until A7 exists, mesh output must route to a non-mesh carrier, and the
"one valkyrie per vendor family" structure is a plan rather than a roster.

I also have not verified that LiteLLM routing or any free-vendor key exists on
this host. The entire substrate is operator-reported.

# PARKED — mesh conductor apex (A7) + 8 vendor-family valkyries

```yaml
feature: mesh_conductor_apex
status: PARKED — UNDER_SPECIFIED, operator to name
spec: GEN133_FORMAL_SPEC.md §14 · SUBSTRATE_ROSTER.md §3.7
parked_by: SIGRÚN P4 · 2026-07-30
```

## Purpose

Give the `$0` free-vendor mesh a rostered apex (the conductor) and 8 valkyries —
one per vendor family, each the **steward** of its family, owning the receipts of
the hands it invokes there.

## Why parked

Names are operator work. But there is also a real structural gap here worth
stating plainly:

**FM-2 says mesh output returns to a rostered carrier — and the mesh has no
rostered carrier of its own.** A7 is unnamed and all 8 vendor valkyries are
unnamed. So until A7 exists, mesh output must route to a **non-mesh** carrier, and
"one valkyrie per vendor family" is a plan rather than a roster.

Second gap: only **6 of 8** vendor families are named (Groq, Cerebras, Sambanova,
Cohere, Mistral, Gemini). Either the operator names two more, or the mesh runs at
6 and the 1-8-64 target is short by 2 in this substrate.

## The distinction that must not blur

| population | named | soul | chain | emits | ceiling |
|---|---|---|---|---|---|
| mesh **valkyries** (8) | yes | yes | yes | yes | FILE |
| mesh **hands** (unbounded) | no | no | no | no | TEXT |

The family has a name; the individual call does not. This is what lets the
institution use anonymous capacity without violating `NO_EPHEMERAL_AGENTS`:
anonymity is confined to the hand, accountability stays with the carrier.

## Dependencies

| # | dependency |
|---|---|
| 1 | operator names A7 and the 8 family valkyries |
| 2 | operator names vendor families 7–8 |
| 3 | G10 (budget gate) ported from gen-130 |
| 4 | verify LiteLLM routing and free-vendor keys actually exist on this host — **I did not confirm this; the whole substrate is operator-reported** |

## When to revisit

After G10 is ported and at least one vendor family is confirmed reachable. Bind
before invoke (GG-2): the binding must exist before the first call, not after.

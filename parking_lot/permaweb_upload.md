# PARKED — permaweb upload (the ONE gen-133 address)

```yaml
feature: permaweb_upload
status: PARKED — BLOCKED on operator, irreversible
spec: GEN133_FORMAL_SPEC.md §17 · GLEIPNIR_GRIMOIRE.md §3
parked_by: SIGRÚN P4 · 2026-07-30
```

## Purpose

One Arweave address that unfolds into the Gleipnir Grimoire — the operator's
spells and `soul.md`. This is gen-133's terminal state. One address. Not a
directory of addresses, not a gateway list (standing decision D5).

## Why parked

**Arweave is permanent by construction: no delete, no edit, no takedown.** A typo
is permanent. A leaked secret is permanently leaked. Firing this is operator-typed
only and no agent may take it, at any autonomy level, ever.

Three of its six preconditions are outside every agent's reach by design:

| # | precondition | who |
|---|---|---|
| P1 | operator-typed authorization | **operator only** |
| P2 | passing secret-scan receipt | agent may produce |
| P3 | `soul.md` body non-empty, **operator-authored** | **operator only** |
| P4 | spell list non-empty, **operator-selected** | **operator only** |
| P5 | capsule merkle root verifies | agent may produce |
| P6 | manifest unfolds to every referenced object | agent may produce |

## Dependencies

- Operator writes the `soul.md` body. An agent filling it forges the artifact the
  whole generation exists to preserve.
- Operator selects the spells. An agent does not know which incantations are
  load-bearing.
- Secret-scan receipt (GR-5 — a precondition, not a courtesy; irreversibility
  makes it the highest-consequence gate in the system).
- Wallet funding — agents may not hold wallet credentials.

## Agent-side work that IS permitted

Bind · verify · selfcheck · secret-scan · **stage** the command. That is honest
preparation. **Preparing is not doing, and it must never be described as if it
were.** See `permaweb/PREFLIGHT.md` and `permaweb/staging/`.

## When to revisit

When the operator types the authorization. Not on any agent's schedule.

## Existing state

- gen-132 capsule: merkle root `af8d76fb3c144e51…`, bound sha256
  `8874a66d14dc1483…`, 100,172 B, `permaweb.status: NOT_UPLOADED`, `address: null`
- inherited lineage anchor (a *different* object):
  `arweave:w1rsVQkkejXv7tVj_pMhcAz7HMFpY_dgwxGhoytBc9M`, 64 rows, `d32b6e44…` —
  ⚠️ not re-fetched by any recent lane

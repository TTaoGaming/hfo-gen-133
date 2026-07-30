# LICENSE — PENDING OPERATOR DECISION (no file written)

```yaml
doc: LICENSE.PENDING.md
status: BLOCKED — operator decision required
valid_time_utc: 2026-07-30T05:40:00Z
authored_by: SIGRÚN P4 compose lane · claude-opus-5
```

## What was checked, first-hand

A `LICENSE` file was searched for at every candidate parent forge:

| forge | `LICENSE` present? |
|---|---|
| `C:\Dev\hfo_gen_133_forge` | **no** |
| `C:\Dev\hfo_gen_132_forge` | **no** |
| `C:\Dev\hfo_gen_131_forge` | **no** |
| `C:\Dev\hfo_dev_2026_5_30\hfo_gen_130_forge` | **no** |

**No precedent exists.** Per the dispatch instruction ("use whatever's already
in use, halt if none found"), no `LICENSE` was invented. Choosing a license is a
world-effect-adjacent, effectively irreversible act once the repo is pushed or
the soul is on Arweave — Arweave has no takedown, so the license terms that ride
along with the first upload are permanent.

## Why this matters more than usual here

The terminal state of gen-133 is a **permaweb upload of `soul.md`**. Once
uploaded:

- the license text is immutable and unrevocable;
- an *absent* license means "all rights reserved" by default, which is a
  defensible position, but an ambiguous one for a document meant to be a public
  identity anchor others verify;
- a permissive license (MIT/Apache-2.0/CC0) cannot be walked back.

## Options for the operator (pick one, then an agent writes the file)

| option | effect | fits gen-133 if… |
|---|---|---|
| **MIT** | permissive, code-shaped, needs copyright-holder name | you want the tooling reusable and don't care about attribution beyond the notice |
| **Apache-2.0** | permissive + explicit patent grant + NOTICE file | you expect third parties to build on the gate/kernel code |
| **CC0-1.0** | public-domain dedication, prose-shaped | the soul/grimoire is meant to be a freely-copyable public anchor |
| **Dual: Apache-2.0 (code) + CC-BY-4.0 (canon/prose)** | separates the two kinds of content this repo actually holds | **most accurate to what is here** — this repo is ~90% prose |
| **No license (all rights reserved)** | status quo of gens 130–132 | you want the heritage public-readable but not freely reusable |

**Recommendation, stated as a recommendation and not a decision:** dual
Apache-2.0 for anything under a future `code/`, CC-BY-4.0 for `canon/`,
`packets/`, `grimoire/`, `archives/`, and the souls. It matches the actual
content split and it names the operator as the attributed party, which is the
point of a soul anchor.

## What is needed to unblock

1. Operator picks an option above (or names another).
2. Operator supplies the copyright line: `Copyright (c) 2026 <legal or handle>`.
   An agent must not guess this — a wrong copyright holder on an immutable
   ledger is worse than no license.
3. Then: commit `LICENSE` (+ `LICENSE-CANON` if dual) and delete this file.

*Truthful-red > false-green.*

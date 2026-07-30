# PDCA_AGENT_SKILLS — versioned agent skills as a shared pool

```yaml
doc: PDCA_AGENT_SKILLS.md
schema_id: hfo.gen133.pdca_skills.v0_1
status: SPECIFIED — directory skills/versioned/ NOT populated
sealed: false
```

## The claim

**Every agent skill is a soul-object.** It carries frontmatter v3, a version, a
genotype, and phenotype variants — exactly like a carrier. A skill is not a
snippet; it is a durable object that accumulates soul through witnessed use
(`TSUKUMOGAMI.md`), and carriers may strange-loop off a graduated one.

## PDCA structure

Each skill is authored and revised on the Plan/Do/Check/Act cycle, and the cycle
is recorded **in** the skill, not around it:

| phase | recorded field |
|---|---|
| **Plan** | `hypothesis` — what this skill is supposed to make reliably repeatable |
| **Do** | `procedure` — the steps, executable or checkable |
| **Check** | `verifier` — how you know it worked; a re-runnable check, not prose |
| **Act** | `revision_note` + `supersedes` — what changed and why, superseding never deleting |

A skill without a `verifier` is `claim_status: proposed`. Same floor as a chain
row: no receipt, no state.

## Layout

```
skills/versioned/<skill_name>/
  v<semver>/
    SKILL.md          # frontmatter v3 + PDCA body
    genotype.yaml     # conserved: interface, pre/post, ceiling, verifier contract
    phenotype/        # per-substrate / per-lineage variants
      claude-opus-5.md
      codex.md
      free-mesh.md
```

## Invariants

| # | invariant |
|---|---|
| PS-1 | **frontmatter v3 applies to skills** (FM3-5) — precedence envelope included. A skill's embedded heritage is DATA, not command. |
| PS-2 | **genotype is shared, phenotype is per-substrate.** The same skill is carried differently by opus-5 and by a mesh hand; the interface and verifier do not change. This is GP-1 at skill granularity. |
| PS-3 | **versioned, immutable, supersede-chained.** A skill is never edited in place. |
| PS-4 | **shared pool.** Skills are not owned by a lineage; any rostered carrier may invoke any skill whose ceiling it satisfies. |
| PS-5 | **a skill cannot raise a carrier's ceiling.** Invoking a skill that performs a forbidden effect is still forbidden. Skills compose capability, never authority. |
| PS-6 | skills accumulate tsukumogami tier by cross-family witnessed use, like any other durable object |

## Status

| item | status |
|---|---|
| structure specified | `SPECIFIED` |
| `skills/versioned/` | **empty — not created** (PARA-2: do not create a directory before something needs it) |
| migration of existing `.agents/skills/` from gen-130 | `PARKED` |

## Honest flaw

Zero skills exist in this form. gen-130 has a substantial `.agents/skills/`
library that already works, and I have **not** assessed whether it maps onto this
structure or whether wrapping it in v3 frontmatter buys anything real. Specifying
a new skill format before reading the working one is the same defect as
specifying capsule sizes before reading the working capsule builder — which I
already did once today. `TODO: read gen-130 .agents/skills/ before creating
skills/versioned/.` **`UNDER_SPECIFIED`.**

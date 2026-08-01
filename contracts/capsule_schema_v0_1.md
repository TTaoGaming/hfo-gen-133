# CONTRACT — world state capsule, per generation

```yaml
contract: world_state_capsule
schema_id: hfo.gen133.contract.capsule_schema.v0_1
authored_by: SIGRÚN · claude-opus-5 · project lead
valid_time_utc: 2026-08-01T00:00:00Z
transaction_time_utc: 2026-08-01T00:00:00Z
status: SPECIFIED — generalizes an EXISTING format, does not invent a competing one
generalizes: archives/capsules/gen_133_word_state_capsule_20260730.md (hfo.gen133.word_state_capsule.v0_1)
companions: contracts/bitemporal_central_memory.v0_1.md · contracts/heritage_ingestion_pipeline.v0_1.md
template: capsules/world_state/TEMPLATE_world_state_capsule.v0_1.md
sealed: false
```

## §1 · What this is, and what it deliberately is not

A **world state capsule** is a one-file rehydration record for a single
generation. A future carrier reading only that file must be able to reconstruct
the operating picture of that generation without opening anything else.

**This contract does not invent a new format.** A working capsule already
exists on disk (`archives/capsules/gen_133_word_state_capsule_20260730.md`,
`schema_id: hfo.gen133.word_state_capsule.v0_1`). Inventing a second, prettier
schema alongside it is exactly the drift that produces two half-populated
formats and no queryable history. **This contract generalizes that one** so it
can be instantiated per generation and ingested into central memory.

Changes made to the existing shape, and why — each one is small and each one is
required for ingestion:

| # | change | reason |
|---|---|---|
| C1 | `generation` → `generation_id`, and it accepts `PRE_HFO_<label>` | pre-HFO eras have no integer generation |
| C2 | add `valid_time_range: {from, to}` | a generation is an *interval*, not an instant. The existing capsule has only a point `valid_time_utc` |
| C3 | `transaction_time_utc` must be a literal timestamp | the existing capsule has `SEE_GIT_COMMIT_METADATA`, which is not ingestible |
| C4 | add `capsule_status` | distinguishes a capsule written *live* from one *reconstructed* later from artifacts |
| C5 | add `gaps: []` with explicit `NOT_FOUND` entries | an absent section is ambiguous; an explicit NOT_FOUND is evidence |
| C6 | add `sources: []` — every path the capsule was derived from | ingestion needs provenance per fact |

## §2 · Bitemporal semantics — the load-bearing part

Every capsule carries **two independent time axes.** This is the whole point,
and getting it wrong makes the central memory worse than no memory.

| axis | field | meaning | example |
|---|---|---|---|
| **valid time** | `valid_time_range.from/to` | when the described state was TRUE IN THE WORLD | gen-124 ran 2026-05-24 → 2026-05-30 |
| **transaction time** | `transaction_time_utc` | when WE RECORDED believing it | a gen-124 capsule written on 2026-08-01 has tx-time 2026-08-01 |

The distinction is not academic. It is the anti-hallucination mechanism:

> A capsule for gen-124 **reconstructed today** is `valid_time: 2026-05-24..30`,
> `transaction_time: 2026-08-01`, `capsule_status: RECONSTRUCTED`. A future
> carrier can then ask two *different* questions and get two *different*
> answers — *"what was true in gen-124?"* versus *"what did we believe about
> gen-124, and when did we start believing it?"* Collapsing those two into one
> timestamp is precisely how a carrier states a later reconstruction as if it
> were a contemporaneous observation. That collapse is the mechanism behind
> most of what reads as hallucination about our own history.

**Rule R1:** a RECONSTRUCTED capsule may never claim a `transaction_time` earlier
than the session that wrote it. Backdating tx-time forges a receipt.

**Rule R2:** a fact whose valid time cannot be bounded gets
`valid_time_range.to: UNKNOWN`, never a guessed date.

## §3 · Required header (machine-readable)

```yaml
schema_id: hfo.capsule.world_state.v0_1
generation_id: 124                     # int | "PRE_HFO_OMEGA_GEN7" | "PRE_HFO_<label>"
lineage: HFO                           # HFO | OMEGA | PRE_HFO
valid_time_range:
  from: 2026-05-24T00:00:00Z
  to:   2026-05-30T00:00:00Z           # or UNKNOWN
transaction_time_utc: 2026-08-01T00:00:00Z
capsule_status: RECONSTRUCTED          # LIVE | RECONSTRUCTED | PARTIAL | STUB
authored_by: "<callsign> · <model> · <lane>"
confidence: MEDIUM                     # HIGH (first-hand disk probe) | MEDIUM | LOW (inherited from a prior summary)
forge_root: "C:\\Dev\\hfo_dev_2026_5_24\\hfo_gen_124_forge"
forge_exists_on_disk: true
sources:                               # every path this capsule was derived from
  - {path: "...", sha256: "...", read_first_hand: true}
gaps:                                  # explicit, enumerated
  - {field: "operator_income", status: NOT_FOUND, searched: ["..."], note: "..."}
sealed: false
```

`confidence: LOW` is mandatory for any capsule whose facts came from a prior
summary rather than from disk. **INHERITED facts must be marked at the fact
level, not just the header** — the existing gen-133 capsule already does this
(`# INHERITED — kit not re-read by this lane`) and that convention is adopted
verbatim.

## §4 · Required sections (human-readable, in this order)

| § | section | content | if unknown |
|---|---|---|---|
| 1 | **Operator state** | income at that gen, active subscriptions/spend, stated goals, named blockers | `NOT_FOUND` row in `gaps` |
| 2 | **Substrate state** | which apps/CLIs installed, which schedules firing, which forges existed, model access | `NOT_FOUND` |
| 3 | **Apex roster** | callsigns active, seats held, lieutenants, valkyries | `NOT_FOUND` |
| 4 | **Contracts + specs landed** | path + sha256 per artifact | list may be empty; say so |
| 5 | **Failure classes discovered** | L-vectors / failure ids first named in this generation | empty is a real answer |
| 6 | **External deliverables** | URL + HTTP status + date checked. **Only stranger-visible artifacts count** | `ZERO_EXTERNAL_EFFECT` is a valid and common value |
| 7 | **Known / unknown at the time** | what the generation believed, and what it did not yet know | required — this is the section that makes the capsule bitemporal in prose |
| 8 | **Succession** | what this generation handed to the next; what was dropped | `NOT_FOUND` |
| 9 | **Gaps** | the `gaps:` block rendered as prose | required, never empty in a RECONSTRUCTED capsule |

**§6 discipline:** "shipped" means *a stranger could see or touch it.* A commit
is not a deliverable. The gen-130 measurement — 609 autonomous commits, zero
stranger-visible artifacts — is the reason this section exists as its own
required field rather than as a subsection of "work done."

## §5 · Generation inventory — probed from disk 2026-08-01

Forges found under `C:\Dev` (first-hand `ls`, this session):

| lineage | generations with a forge directory on disk |
|---|---|
| OMEGA / pre-HFO | **98** (`hfo_dev_2026_3\hfo_gen_98_forge`), plus `C:\Dev\archive\omega_gen7_unified_archive_2026_1_31` and `hfo_dev_2026_3\omega_games\` (50 titles) |
| HFO | **100, 104, 105, 106, 107, 109, 110, 111, 112, 113, 114, 115, 117, 118, 121, 123, 124, 130, 131, 132, 133** |

**22 forge roots located. 14 generation numbers have NO forge on this drive:**
`99, 101, 102, 103, 108, 116, 119, 120, 122, 125, 126, 127, 128, 129`.

Those 14 get **STUB capsules** with `capsule_status: STUB` and a `gaps` entry
`NOT_FOUND_ON_C_DRIVE`, listing Google Drive and GitHub as unsearched sources.
**A stub is not a failure — it is the record that a search happened and found
nothing**, which is the only thing that stops the next carrier re-running the
same search. This is the single highest-value output of the capsule programme
and it is also the cheapest.

## §6 · Emission order (cheapest information first)

1. **gen-133** — LIVE. Already exists; upgrade its header to this schema.
2. **gen-130, 131, 132** — RECONSTRUCTED, high confidence. Recent, well-documented, rollup capsules already exist for 130 and 131 under `archives/capsules/heritage/`.
3. **The 14 STUBs** — ~10 minutes total. Pure gap-recording, no research.
4. **gen-124, 123, 121** — RECONSTRUCTED. Named as heritage-fertile in `C:\Dev\CLAUDE.md`.
5. **gen-98/omega, 107, 100** — RECONSTRUCTED. Spatial heritage; feeds Nidhöggr's §8.1 lane directly.
6. **remainder** — as capacity allows.

> **FALSIFIER:** if a RECONSTRUCTED capsule cannot cite ≥3 first-hand `sources`
> entries with reproduced sha256, it is a STUB wearing a capsule's header and
> must be downgraded. A capsule assembled from prior summaries is the exact
> failure this contract exists to prevent.

## §7 · Invariants

| # | invariant |
|---|---|
| CI-1 | **Two time axes, always.** A capsule with one timestamp is malformed. |
| CI-2 | **No backdated transaction time.** (R1) |
| CI-3 | **Gaps are enumerated, never implied by absence.** |
| CI-4 | **Provenance per fact.** INHERITED and NOT_FOUND are first-class values. |
| CI-5 | **A capsule is append-only.** Corrections are new capsules with a later transaction time and the same valid time — never edits. This is what makes belief-change queryable instead of invisible. |
| CI-6 | **External deliverables are stranger-visible or they are not deliverables.** |

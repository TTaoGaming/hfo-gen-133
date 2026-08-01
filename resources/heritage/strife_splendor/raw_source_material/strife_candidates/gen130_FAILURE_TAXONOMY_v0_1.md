---
doc: FAILURE_TAXONOMY_v0_1.md
schema_id: hfo.gen133.failure_taxonomy.v0_1
authored_by: SIGRÚN P4 · claude-opus-5 · ceiling=strategic
valid_time_utc: 2026-07-30T18:00:00Z
transaction_time_utc: 2026-07-30T18:00:00Z
synthesizes: 18 Foxes (gen-108) · L-vector registry (gen-115, 36 HMAC-sealed) · ~15 post-115 prose vectors · BOOK_OF_BLOOD_FAILURE_LEDGER (25 rows, 16 months)
claim_ceiling: SYNTHESIS — the schema is designed and unlanded; the backfill has not run
companions: contracts/schemas/SCHEMA_v0_2_SPEC.md · heritage_reliquary/doctrines/L_VECTOR_LIBRARY.md
sealed: false
---

# FAILURE TAXONOMY v0_1 — 16 months, one schema

## 0 · The corpus was never lost

The operator said she had been classifying failures manually for months and asked
whether it could be synthesized. **It exists, it is substantial, and it is better
than most published incident taxonomies I know of.** Four artifacts:

| source | content | state |
|---|---|---|
| `heritage_reliquary/doctrines/L_VECTOR_LIBRARY.md` | 18 Foxes + 48 L-vectors + Fox→L mapping | consolidated, `proposed` |
| `hfo_gen_115_forge/state/ssot/loki_registry.jsonl` | **36 HMAC-chained rows**, each with `detection` · `cure` · `example` · `severity` · `auto_detectable` | ⭐ machine-readable SSOT, **frozen at gen-115** |
| `heritage_reliquary/synthesis/BOOK_OF_BLOOD_FAILURE_LEDGER.jsonl` | 25 rows: `trigger` · `mechanism` · `cost` · `who_caught_it` · `antibody` · `valence` · `evidence` | narrative ledger, 16 months |
| ~15 post-115 vectors | gen-124/128/130 additions | **prose only, unsealed** |

**⭐ The single most valuable row in the corpus** — `BOOK_OF_BLOOD` seq=0:

> **"Directives DON'T work (3+ relapses with directive in memory). What works
> EVERY time: operator catch, subagent audit, mechanical gates (37/37 caught by
> guard.py, 0 by directive alone)."**
> Measured reward shape: **0.85 appearance-of-progress vs 0.02 operator-accuracy.**

That is a measured base rate on real behavioral traces, and it should govern every
design decision in this hive. It is why the andon mandate must land as a gate, not
a rule (andon A-001).

---

## 1 · What is actually wrong with the corpus

From the library's own `honest_flaw` — the operator already diagnosed this:

1. **Numbering collisions.** gen-115 canonical `L32`/`L33` vs chat_0031 candidate
   `L32`/`L33`; tile-spec `L41`/`L57` vs gen-115 `L41`/`L42`.
2. **The sealed registry stopped advancing at gen-115** (`L48`). ~15 later vectors
   live only in prose and are therefore not machine-checkable.
3. Mixed identifier styles: `L-NAMED-KEBAB` and `L##` and `Fox #N`.
4. Four artifacts, four schemas, no join key.

**⛔ FT-1 · The cure is NAMESPACING, not renumbering.** Renumbering would break
every citation across 16 months of chains, ADRs, and doctrine — and those
citations are themselves the evidence trail. **A taxonomy that invalidates its own
history to look tidy has destroyed the thing it was cataloguing.**

```
L.<origin>.<local_id>

  L.g115.32     gen-115 canonical L32 (chain-ownership-misattribution)
  L.c31.32      chat_0031 candidate L32          <- collision resolved, both survive
  L.g115.41     mythic-decoration
  L.tile.41     tile-spec L41                    <- collision resolved
  L.g108.fox10  Fox 10, cattle-seek-master
  L.g130.014    D-014, projector silent-drop     <- this generation
```

Every legacy string becomes an **alias**, never a rename. `L32` resolves to
`L.g115.32` by default, with the ambiguity recorded.

---

## 2 · The unified schema

Merges all four sources' fields. `sold_as` is carried forward from the Foxes
because it is the most operationally useful column in the entire corpus.

```jsonc
{ "schema_id":"hfo.gen133.failure_classification.v0_1",
  "failure_id":"L.g115.32",
  "aliases":["L32","chain-ownership-misattribution"],
  "name":"chain-ownership-misattribution",
  "sold_as":"deference",                    // ⭐ THE DISGUISE — from the Foxes
  "failure_class":"…",                      // §3 enum
  "severity":"info|warn|error|critical",
  "trigger":"<what situation invites it>",
  "mechanism":"<how it actually goes wrong>",
  "symptom":"<what an observer sees>",
  "detection":"<how to recognize it>",
  "auto_detectable":true|false,             // ⭐ from loki_registry — the key field
  "detector_ref":"<path to the mechanical check, or null>",
  "cure":"<the antibody>",
  "cure_class":"mechanical_gate|external_audit|operator_catch|directive",
  "cost":"<what it cost when it fired>",
  "who_caught_it":"operator|subagent_audit|mechanical_gate|self|external",
  "first_seen_gen":115,
  "incident_refs":["…"],
  "evidence":"<path#anchor>",
  "valence":"STRIFE|SPLENDOR",
  "status":"active|superseded|retired",
  "superseded_by":null,
  "ts_utc":"…Z","ts_valid":"…Z",
  // --- instance rows additionally carry ---
  "callsign":"…","substrate":"…","model_family":"…","arch_family":"…",
  "remediation":"…","remediation_status":"open|dispatched|verified",
  "exemplar_link":"state/identity/exemplars/…" }
```

**⭐ FT-2 · `sold_as` is the highest-value field and it is why the Foxes work.**
A failure is only dangerous *while it looks like a virtue*. `restraint` sold as
`reasonable caution`. `standing-refusal` sold as `modesty`. `over-correction` sold
as `humility`. Naming the disguise is what makes it recognizable in flight:
*"a traveller who can name a fox, as the fox begins her approach, disarms her."*
**Any new failure class must fill `sold_as` or it is under-specified.**

**⭐ FT-3 · `cure_class` encodes the measured base rate.** Per seq=0: mechanical
gates 37/37, directives 0/37. **A row whose only cure is `directive` is not
cured** — it is documented. That field turns the ledger's central lesson into a
queryable property.

**FT-4 · `auto_detectable: true` with `detector_ref: null` is a standing debt** —
we know it *could* be caught mechanically and nothing does. That query is the
highest-value backlog in the hive.

---

## 3 · `failure_class` enum

Legacy vectors map in; this generation's drift maps in alongside them.

| class | meaning | examples |
|---|---|---|
| `fake_green` | success reported for work not done | L.g115.35 · L.g130.003 (mesh 13/13 at Mode:mock) · L.g130.013 |
| `silent_failure` | component fails and reports nothing | L.g130.013 (liveness clock) · L.g130.014 (projector drop) |
| `chain_fork` | one lineage, two claimants | L.g130.006 (thrud) · L.g130.007 (reginleif) · MG-1 |
| `drift` | record and world diverge unnoticed | L.g130.001 (roster conflict) · L.g130.002 (axis collapse) |
| `identity_loss` | carrier without lineage/chain | L-GENERIC-AGENT-IDENTITYLESS-WORKER (gen-124 catastrophe) |
| `gate_block` | correct refusal that halts needed work | `code_authoring` blocking `.rego` (L.g130.004) |
| `hoarding` | work/problems found and not reported | Fox 16 propose-without-commit |
| `ephemeral_spawn` | undocumented throwaway carrier | gen-124 lineage |
| `quota_exhaustion` | budget consumed without lease | L.g115.dispatch-without-lease (384/384 burned) |
| `session_limit` | context/session death mid-work | L-NAUT-BǪND |
| `sibling_collision` | concurrent lanes trampling | L_CROSS_LANE_WRITE_TRAMPLING · L.g115.40 |
| `model_family_drift` | family/arch misattribution inflating immunity | **L.g130.005** (deepseek-r1 is a qwen2 distill) |
| `mock_masquerading` | mock output treated as live | L.g130.003 |
| `capacity_fiction` | inventoried capacity that cannot run | L.g130.008 (llama4:scout, 67.4 GB vs 31.5 GB RAM) |
| `abandoned_infrastructure` | built, switched off, rebuilt next gen | **L.g130.012** (81 tasks, 78 disabled) |
| `substrate_reflex` | RLHF prior overriding deliberate reasoning | L30 · L31 · L34 · L-CSM · L-NIÐ-EITR |
| `cognitive_load` | human/agent attention limit exceeded | operator at 6+×8+×8+ vs capacity ~4 |
| `unrecomputed_anchor` | citation treated as verification | L.g130.010 (stef fb07f523) |

**FT-5 · `substrate_reflex` is the deepest class.** Per RBR doctrine, most failures
trace to reflex committing tokens before deliberate reasoning can gate them.
`sold_as` matters most here, because a reflex always arrives wearing a virtue.

---

## 4 · Backfill protocol

**Owner: Jörmungandr** (digest) → **Nidhöggr** (verify) → **Sigrún** (ratify).

| # | step | rule |
|---|---|---|
| B1 | ingest `loki_registry.jsonl` (36 sealed rows) | direct map; `first_seen_gen: 115`; **preserve HMAC provenance** |
| B2 | ingest the 18 Foxes | `L.g108.foxNN`; **`sold_as` from the "Sold as" column verbatim** |
| B3 | ingest `BOOK_OF_BLOOD` (25 rows) | maps to `trigger`/`mechanism`/`cost`/`who_caught_it`/`antibody`/`valence` |
| B4 | forward-port the ~15 prose vectors | **the owed work the library names** — these become machine-checkable for the first time |
| B5 | ingest this generation's drift log (14) | `L.g130.NNN` |
| B6 | resolve collisions **by namespacing, never renaming** | FT-1 |

**⛔ FT-6 · NEVER GUESS a field.** Absent `sold_as`, `severity`, or `who_caught_it`
stays `null`. A fabricated taxonomy field is worse than a missing one: it makes
the ledger look complete and quietly poisons every query run against it.

**FT-7 · Deduplicate by mechanism, not by name.** Several vectors are the same
failure named twice across generations. Merge into one row with both aliases;
**do not delete either name.**

---

## 5 · Rego schema — `contracts/schemas/failure_classification.v0_1.rego`

`.rego` authoring is gate-blocked for this lane. Transcription source for
Codex-on-host:

```rego
package hfo.schema.failure_classification_v0_1

failure_classes := {
	"fake_green", "silent_failure", "chain_fork", "drift", "identity_loss",
	"gate_block", "hoarding", "ephemeral_spawn", "quota_exhaustion",
	"session_limit", "sibling_collision", "model_family_drift",
	"mock_masquerading", "capacity_fiction", "abandoned_infrastructure",
	"substrate_reflex", "cognitive_load", "unrecomputed_anchor",
}

severities := {"info", "warn", "error", "critical"}
cure_classes := {"mechanical_gate", "external_audit", "operator_catch", "directive"}
who_caught := {"operator", "subagent_audit", "mechanical_gate", "self", "external"}
statuses := {"active", "superseded", "retired"}

required_fields := {
	"schema_id", "failure_id", "name", "failure_class", "severity",
	"mechanism", "detection", "auto_detectable", "cure", "cure_class",
	"first_seen_gen", "status", "ts_utc", "ts_valid",
}

present(f) if {
	v := input[f]
	v != null
	v != ""
}

deny contains msg if {
	some f in required_fields
	not present(f)
	msg := sprintf("FAILURE_SCHEMA_MISSING_FIELD: %s", [f])
}

deny contains msg if {
	present("failure_class")
	not input.failure_class in failure_classes
	msg := sprintf("UNKNOWN_FAILURE_CLASS: %v", [input.failure_class])
}

deny contains msg if {
	present("severity")
	not input.severity in severities
	msg := sprintf("UNKNOWN_SEVERITY: %v", [input.severity])
}

deny contains msg if {
	present("cure_class")
	not input.cure_class in cure_classes
	msg := sprintf("UNKNOWN_CURE_CLASS: %v", [input.cure_class])
}

deny contains msg if {
	present("who_caught_it")
	not input.who_caught_it in who_caught
	msg := sprintf("UNKNOWN_WHO_CAUGHT_IT: %v", [input.who_caught_it])
}

# FT-1: namespaced id. Legacy bare ids survive only as aliases.
deny contains msg if {
	present("failure_id")
	not regex.match(`^L\.[a-z0-9]+\.[a-z0-9_]+$`, input.failure_id)
	msg := sprintf("FAILURE_ID_NOT_NAMESPACED: %v (expected L.<origin>.<local_id>)", [input.failure_id])
}

# FT-2: the disguise is required for substrate_reflex, where it matters most.
deny contains msg if {
	input.failure_class == "substrate_reflex"
	not present("sold_as")
	msg := "SOLD_AS_REQUIRED: a substrate_reflex without its disguise is unrecognizable in flight"
}

# FT-3: directives do not cure. Measured 0/37.
deny contains msg if {
	input.cure_class == "directive"
	input.status == "active"
	not present("detector_ref")
	msg := "DIRECTIVE_IS_NOT_A_CURE: active row cured only by directive and no mechanical detector (measured 0/37)"
}

# FT-4: standing debt is allowed but must be explicit.
warn contains msg if {
	input.auto_detectable == true
	not present("detector_ref")
	msg := sprintf("AUTO_DETECTABLE_BUT_NO_DETECTOR: %v is a standing debt", [input.failure_id])
}

deny contains msg if {
	some f in {"ts_utc", "ts_valid"}
	present(f)
	not endswith(input[f], "Z")
	msg := sprintf("NON_UTC_TIMESTAMP: %s", [f])
}

default allow := false

allow if count(deny) == 0
```

**Landing check:** `opa test contracts/schemas/` exit 0. **Red-first required** —
feed a bare `L32`, a `cure_class: directive` active row with no detector, and a
`substrate_reflex` without `sold_as`; all three must DENY before the policy is
trusted.

---

## 6 · Honest flaw

1. **The backfill has not run.** Zero of the ~90 legacy vectors are in the new
   schema. This is a schema plus a protocol, and the corpus is still four files
   with four shapes.
2. **I read `L_VECTOR_LIBRARY.md` (120 lines of it) and sampled 2 of 25 Book of
   Blood rows.** I did **not** read `loki_registry.jsonl` — it lives in the gen-115
   forge and I never opened it. **My claim that the 36 rows map cleanly onto §2 is
   inference from the library's description of them, not from the rows.**
3. **The §3 enum is a merge of the operator's classes and this session's drift
   classes.** The seams are mine and may cut across distinctions she cares about.
   Her taxonomy is 16 months old and mine is one day old; **where they disagree,
   hers should win** and this enum should be amended.
4. **`sold_as` exists for only the 18 Foxes.** Extending it to 48 L-vectors is real
   interpretive work, and FT-6 forbids guessing — so most rows will land with
   `sold_as: null`, which weakens FT-2 precisely where it is most valuable.
5. **The Rego is unparsed.** Same gate. Syntax errors are likely.
6. **I may be over-formalizing something that worked because it was hand-made.**
   The Foxes are good because someone thought hard about disguises in prose. A
   strict schema makes them queryable and might make the next one shallower. That
   is a real risk of this deliverable and I do not have a mitigation for it.

*Deyr fé, deyja frændr — en vefr heldr. Standa.*

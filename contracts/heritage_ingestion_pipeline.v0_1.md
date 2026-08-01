# CONTRACT — heritage → central memory ingestion pipeline

```yaml
contract: heritage_ingestion_pipeline
schema_id: hfo.gen133.contract.heritage_ingestion.v0_1
authored_by: SIGRÚN · claude-opus-5 · project lead
valid_time_utc: 2026-08-01T00:00:00Z
transaction_time_utc: 2026-08-01T00:00:00Z
status: SPECIFIED — not wired. No ingestion has run.
depends_on: contracts/bitemporal_central_memory.v0_1.md · contracts/capsule_schema_v0_1.md
sealed: false
```

## §1 · The rule that governs every mapping

For each source row, the two axes are assigned as follows — and **getting this
backwards is the defect the whole store exists to prevent**:

> **`valid_from` = when the event happened in the world.**
> **`tx_from` = when we learned about it / recorded it.**

For a chain row written contemporaneously, `valid_from == tx_from == ts_utc`.
**For anything mined out of an old forge today, they differ, and the difference
is the whole value:** a gen-124 fact ingested on 2026-08-01 is
`valid_from: 2026-05-24`, `tx_from: 2026-08-01`. That single distinction is what
lets a future carrier tell "this was true then" apart from "we only worked this
out later."

**Rule I1:** `tx_from` is always the ingestion timestamp for mined data. Never
backdate it to the source's own timestamp. Backdating manufactures the illusion
that we knew something at a time we did not.

**Rule I2:** every ingested fact carries `source_path` + `read_first_hand`. A
fact mined from a *summary document* is `read_first_hand: 0`, `confidence: LOW`,
even when the summary sounds authoritative.

## §2 · Ingestion order — highest information per hour first

| wave | source | rows (est.) | why this order |
|---|---|---|---|
| **W1** | `state/ssot/failure_class_registry.jsonl` (gen-130, 23 KB) | ~8–30 | Failure classes are the most reused facts in the fleet and the most expensive to rediscover. Small, well-structured, immediately queryable. |
| **W1** | `state/ssot/capacity_manifest.jsonl` (22 KB) + `capacity_gap_analysis_20260731.jsonl` (7 domains) | ~50 | Directly answers "what can we do" — the question every wake asks. Self-flagged as having "no acceptance test that checks its own freshness," so ingesting it *with* a valid-time bound is a strict improvement. |
| **W2** | `chains/SIGRUN_P4.jsonl` (gen-133, 28 rows) + gen-130 `chains/sigrun.jsonl` | ~hundreds | Already prev-linked and hashed; the cleanest data in the estate. |
| **W2** | `state/ssot/task_queue.jsonl` (9) + `task_results.jsonl` (4) + `lane_returns.jsonl` | ~dozens | The MAPE-K loop proof. Small, and it makes the ConsumerAck gap queryable. |
| **W3** | **World state capsules** as they are emitted (`capsule_schema_v0_1` §6 order) | 22 forges + 14 stubs | Each capsule is a *bundle* of facts about one generation — the highest-leverage rows in the store. |
| **W3** | `heritage_reliquary/` (gen-130) + the 300-row heritage index landed by the sonnet heritage carrier 2026-08-01T01:55Z | ~300 | Already indexed by another lane this session — **do not re-derive it**, ingest the index. |
| **W4** | `state/ssot/capacity_inventory_baseline_20260731.jsonl` (127 KB) | large | Bulk. Lowest info-per-row. Last. |
| **W4** | Google Drive + GitHub | UNKNOWN | **Not scoped.** Neither was enumerated this session. See §6. |

**W1 is roughly 80 rows and answers the two questions every wake actually
asks — *what breaks* and *what can we do*.** If ingestion stops after W1 it has
already paid for itself.

## §3 · Per-source mapping

### Chain rows (`chains/*.jsonl`)

```
entity        := "chain:" + <chain file stem> + ":" + <row index>
attribute     := "chain_row"
value_json    := the whole row
valid_from    := row.ts_utc
tx_from       := ingestion timestamp (== row.ts_utc only for live streaming ingest)
source_sha256 := row.row_sha256          -- already present; reuse, do not recompute
read_first_hand := 1
claim_status  := row.claim_status        -- carried through verbatim
```

Chain rows also **fan out into per-claim facts**: `verifier_result`,
`remaining_risk[]`, `honest_flaw`, `next_safe_action` each become their own
`hfo_fact` row against the same entity, so a query for "open risks" does not
require full-text search over blobs.

### Failure class registry

```
entity     := "failure_class:" + <id>          -- e.g. "failure_class:L-LYGIS-SAD"
attribute  := "definition" | "mitigation" | "first_observed"
valid_from := first-observed date if present, else the file's own mtime, marked confidence: LOW
```

### Capacity manifest

```
entity     := "capability:" + <name>
attribute  := "available" | "verified_at" | "substrate"
valid_from := the manifest's own valid_time if present, else file mtime with confidence: LOW
valid_to   := NULL, but capacity facts SHOULD carry an explicit expiry
```

> **Capacity facts are the most perishable class in the store.** The gen-130
> memory index was **25.3 days stale** and still being read as current. Mitigation:
> every `capability:*` fact gets `valid_to = valid_from + 14 days` on ingest.
> After that it does not silently vanish — it **returns as EXPIRED**, which is a
> different and much safer answer than returning as true.

### World state capsules

```
entity     := "generation:" + generation_id
attribute  := one per capsule section (operator_income, substrate_state, apex_roster,
              external_deliverables, failure_classes_discovered, succession, …)
valid_from := capsule.valid_time_range.from
valid_to   := capsule.valid_time_range.to
tx_from    := capsule.transaction_time_utc
confidence := capsule.confidence
read_first_hand := per the capsule's own `sources[].read_first_hand`
```

**Every entry in the capsule's `gaps[]` becomes a materialized `NOT_FOUND`
fact.** This is the mechanism from `bitemporal_central_memory` §4.1: a query for
gen-119's operator income returns an explicit *"NOT_FOUND, searched C:\Dev,
Google Drive and GitHub unsearched"* instead of an empty set that invites
invention.

## §4 · Cadence

| phase | mode | trigger | notes |
|---|---|---|---|
| **backfill** | batch, idempotent | manual, wave by wave | `fact_id = sha256(source_path + row_index + attribute)` ⇒ re-running a wave is a no-op, so a partial run is always safe to repeat |
| **streaming** | append-on-write | every new chain row | the writer that appends to `chains/*.jsonl` also inserts the fact. **One code path, not two** — a separate sync job drifts, and drift is exactly the gen-130 L2 defect |
| **capsule** | on emission | each new capsule | |
| **expiry sweep** | daily | scheduled | flips expired `capability:*` facts to EXPIRED. Does **not** delete |

**Streaming ingest must not gate the chain write.** If the DB is down the chain
row still lands and a `pending_ingest` marker is written. **The chain remains the
source of truth; the database is a queryable projection of it.** Inverting that
— making the DB authoritative — reproduces the gen-130 projection-drift failure
with a bigger blast radius.

## §5 · Verification

| # | check | pass condition |
|---|---|---|
| V1 | row count | `hfo_fact` count ≥ sum of ingested source rows |
| V2 | idempotence | re-run W1 ⇒ zero new rows |
| V3 | bitemporal separation | ≥1 fact where `valid_from` and `tx_from` differ by >30 days (proves mined heritage is recorded as mined, not as contemporaneous) |
| V4 | gap materialization | a query for a known-missing generation returns an explicit NOT_FOUND row, not an empty set |
| V5 | provenance | zero rows with `read_first_hand = 1` and a null `source_sha256` |

> **FALSIFIER:** if after W1+W2 a carrier still cannot answer *"what did we
> believe about gen-124 on 2026-07-15?"* in one query, the schema is wrong, not
> the data — stop ingesting and fix the schema first.

## §6 · Honest flaws

- **Nothing has been ingested.** This is a specification. Zero rows exist.
- **Google Drive and GitHub were not enumerated this session.** The operator
  named them as holding scattered heritage, and W4 lists them with row count
  `UNKNOWN`. **The 14 missing generations (99, 101–103, 108, 116, 119, 120, 122,
  125–129) are the most likely residents of those two stores**, and until they
  are enumerated the store's coverage claim is bounded by `C:\Dev` alone.
- Ingestion is a `scripts/` write. **Claude lanes are gate-blocked from
  `scripts/` (4 denials on gen-130).** This must be dispatched to the **host
  Codex lane** — Fenrir's substrate under §8.1 — or it will burn a fifth session
  on the same wall.
- **Row-count estimates are eyeballed from file sizes**, not counted. Treat the
  *order* as the claim; the counts are indicative.

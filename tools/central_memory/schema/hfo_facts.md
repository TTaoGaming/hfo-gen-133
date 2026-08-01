# hfo_facts — bitemporal schema for gen-133 central memory

```yaml
doc: hfo_facts.md
schema_id: hfo.gen133.central_memory.schema.v0_1
purpose: anti-lobotomize infra — one queryable, time-travel-able store for
  chain rows, apex/valkyrie identity, capability status, failure classes,
  generation boundaries, and artifact hashes.
status: FALLBACK IMPLEMENTATION — see INSTALL_ATTEMPT.md. Datalog/XTDB not
  installed this pass; SQLite with explicit valid_time/transaction_time
  columns stands in. Schema below is written in Datalog-shaped entity/attr
  form so a real XTDB migration later is a straight port, not a redesign.
engine: sqlite3, file tools/central_memory.sqlite
sealed: false
```

## Why bitemporal (not just a timestamp column)

Two independent clocks, never collapsed into one:

- **valid_time** — when the fact was true *in the world* (e.g. when an apex
  was actually admitted, when a generation actually started).
- **transaction_time** — when *this store* learned about it (when the row was
  inserted). Always `>= valid_time` in practice here since we're backfilling
  from existing docs, never before.

The anti-lobotomize property: a later correction does not overwrite history.
`SUBSTRATE_ROSTER.md` itself does this in prose (§0 "Corrections applied,
supersede, never delete") — this store makes that mechanical. Query "as of"
an old transaction_time and you see what the agent *believed* then, even
after a correction lands. Query "as of" an old valid_time and you see what
was *true* then, per the latest correction. Both matter for a substrate that
keeps re-deriving its own roster from scratch every session.

## Entity tables (Datalog-shaped: entity id + attrs + both clocks)

Every table shares this frame:

```
id                  INTEGER PRIMARY KEY
entity_id           TEXT NOT NULL   -- stable logical key, e.g. callsign or class_id
valid_time_utc      TEXT NOT NULL   -- ISO8601 Z — when true in the world
transaction_time_utc TEXT NOT NULL  -- ISO8601 Z — when this store learned it
source_path         TEXT            -- repo-relative file this fact was read from
payload_json        TEXT NOT NULL   -- the attrs, as JSON
sha256              TEXT            -- sha256 of payload_json, for tamper-evidence
```

### `hfo_chain_row`
A chain-row event as XTDB would see it (`hfo/chain_row`).
payload: `{chain_path, row_idx, row_sha256, prev_sha256, kind, actor}`

### `hfo_apex`
Apex agent identity (`hfo/apex`).
payload: `{callsign, tier:"apex", substrate, status, seat}`

### `hfo_valkyrie`
Valkyrie identity (`hfo/valkyrie`).
payload: `{callsign, tier:"valkyrie", apex_parent, substrate, status}`

### `hfo_capability`
Capability id + verified status (`hfo/capability`).
payload: `{capability_id, verified_status, description}`
`entity_id` = capability_id. `valid_time_utc` = last_verified_utc.

### `hfo_failure_class`
Registered failure class / L-vector (`hfo/failure_class`).
payload: `{class_id, refusal_text, registered_utc_note}`
`entity_id` = class_id.

### `hfo_generation`
Generation boundary record (`hfo/generation`).
payload: `{gen_id, start_utc, end_utc, operator_state_snapshot}`
`entity_id` = gen_id. `valid_time_utc` = start_utc.

### `hfo_artifact`
File path + hash + generation + verified status (`hfo/artifact`).
payload: `{file_path, sha256, gen_id, verified_status, size_bytes}`
`entity_id` = file_path.

## Bitemporal query patterns (SQL stand-in for XTDB `FOR VALID_TIME AS OF`)

```sql
-- "as of" valid-time X: latest transaction-time row per entity_id
-- whose valid_time_utc <= X
SELECT * FROM hfo_apex a
WHERE valid_time_utc <= :as_of
  AND transaction_time_utc = (
    SELECT MAX(transaction_time_utc) FROM hfo_apex b
    WHERE b.entity_id = a.entity_id AND b.valid_time_utc <= :as_of
  );
```

## Honest scope of this schema

This models **append-only fact ingestion**, not full XTDB Datalog (no joins
across entity graphs, no Crux-style pull syntax, no automatic retraction).
It is bitemporal-adjacent, not bitemporal-complete. See
`INSTALL_ATTEMPT.md` and the chain receipt for the FALSIFIER.

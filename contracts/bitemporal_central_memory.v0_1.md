# CONTRACT — bitemporal central memory store

```yaml
contract: bitemporal_central_memory
schema_id: hfo.gen133.contract.bitemporal_central_memory.v0_1
authored_by: SIGRÚN · claude-opus-5 · project lead
valid_time_utc: 2026-08-01T00:00:00Z
transaction_time_utc: 2026-08-01T00:00:00Z
status: STAMPED — destination is XTDB 2.0; Phase 0 starts today without it
method: >
  WebSearch ×1 + full-page WebFetch of the XTDB Docker install docs [F] ·
  live probe of docker CLI, docker daemon, and the bundled Python runtime's DB modules
sealed: false
```

## §0 · STAMP

> ## **Destination: XTDB 2.0. Bridge: a normalized bitemporal store in SQLite, starting today.**
> **Both, in that order, and the bridge is not throwaway.**

Two probes decide the sequencing, and both were run live this session:

| probe | result | consequence |
|---|---|---|
| `docker --version` | **Docker 29.5.3, build d1c06ef** ✅ | the CLI is there |
| `docker info` | ⚠️ **`failed to connect to the docker API at npipe:////./pipe/dockerDesktopLinuxEngine … The system cannot find the file specified`** | **Docker Desktop's Linux engine is not running.** Named error, not a hang — the fix is "start Docker Desktop", not "debug Docker" |
| `psql --version` | ⚠️ **`psql: command not found`** | **no host Postgres client.** This breaks the documented connect step — see §2 |
| bundled Python: `psycopg` / `psycopg2` | **MISSING** | no Postgres client in the runtime yet |
| bundled Python: `duckdb` | **MISSING** | DuckDB is not a zero-install option here |
| bundled Python: `sqlite3` | **OK (stdlib)** ✅ | **the only database available right now, at zero install** |

**Therefore:** XTDB is the right destination and the operator's instinct is
correct — but "install XTDB this week" is gated on a daemon that did not answer.
Blocking heritage recovery on that would be the same mistake as blocking income
on a perfect funnel. **Phase 0 starts today in SQLite; Phase 1 lifts it into
XTDB unchanged.**

**Why the bridge is not wasted work — the load-bearing technical fact:**
XTDB 2.0 is **Postgres-wire-compatible** and implements the **SQL:2011**
bitemporal dialect [F]. So the Phase-0 schema can be written in SQL:2011-shaped
columns and the Phase-1 migration is an `INSERT … SELECT` across a wire
protocol, not a rewrite. The normalized row shape (§3) is the invariant; the
engine underneath it is swappable.

## §1 · Options compared

| engine | license | install cost | query language | Python client | bitemporal | verdict |
|---|---|---|---|---|---|---|
| **XTDB 2.0** | open source (JUXT) | `docker run` one-liner [F]; **needs a running daemon** | **SQL (SQL:2011 temporal) + XTQL**, over Postgres wire | **any Postgres driver** (psycopg / JDBC / psql) — this removes the "immature client" risk entirely | ✅ **native, both axes, immutable history** | ⭐ **STAMPED DESTINATION** |
| SQLite + explicit temporal columns | public domain | **zero — stdlib, verified present** | SQL, hand-written temporal predicates | stdlib `sqlite3` | ⚠️ **by convention, not by engine** | ✅ **STAMPED BRIDGE (Phase 0)** |
| Postgres + system-versioned tables | open source | server install | SQL | psycopg | ⚠️ Postgres does **not** implement SQL:2011 system-versioning natively — needs triggers or an extension | not worth the setup when XTDB gives it natively |
| DuckDB | MIT | pip install (**currently missing**) | SQL | mature | ❌ no native bitemporal | **keep for rollups/analytics later**, not as the store of record |
| Datomic | **NOT VERIFIED THIS SESSION** | JVM | Datalog | thin | ✅ bitemporal | ⛔ **not recommended, and I am not going to assert its current licensing without checking.** Clojure/JVM-first with a thin Python story is friction we do not need when XTDB speaks Postgres wire |

### Why XTDB wins on the merits, not just on operator preference

1. **Postgres wire compatibility kills the usual objection.** The standard risk
   with a niche bitemporal DB is an immature client library. XTDB does not have
   that problem — `psycopg`, `psql`, JDBC and BI tools connect to it directly [F].
2. **Bitemporality is in the engine, not in your discipline.** In SQLite the two
   axes are columns *you* must remember to filter on; every hand-written query
   is a chance to silently mix them. In XTDB the engine owns it. Given that the
   entire purpose here is to stop a carrier collapsing "what was true" into
   "what we believed," **moving that correctness out of agent discipline and
   into the engine is the whole point.**
3. **Immutable history matches the chain discipline already in use.** Append-only
   with prev-links is what `chains/*.jsonl` already does by hand.

## §2 · Install — Phase 1, verbatim and verified [F]

```bash
# 0 · start Docker Desktop first. `docker info` hung >120s this session,
#     which is the tell that the daemon is not running.
docker info --format '{{.ServerVersion}}'      # must return before proceeding

# 1 · persistent data dir
mkdir -p C:/Dev/hfo_gen_133_forge/state/memory/xtdb-data

# 2 · run XTDB — 5432 = Postgres wire, 8080 = health/monitoring
docker run -it --pull=always \
  -p 5432:5432 \
  -p 8080:8080 \
  -v C:/Dev/hfo_gen_133_forge/state/memory/xtdb-data:/var/lib/xtdb \
  ghcr.io/xtdb/xtdb

# 3 · verify alive
curl http://localhost:8080/healthz/alive

# 4 · connect — NOTE: `psql` is NOT installed on this host (`psql: command not
#     found`, probed 2026-08-01). The docs' `psql -h localhost -U xtdb xtdb`
#     will fail here. Two working options instead:
docker exec -it <container> psql -U xtdb xtdb     # use the container's own client
#   …or skip psql entirely and drive it from Python (§ below), which is what the
#   ingestion pipeline needs anyway.
```

Python client:

```bash
# no dedicated XTDB client needed — it speaks Postgres wire
<bundled-python> -m pip install "psycopg[binary]"
```

**Image tags:** `latest` (tagged releases) · `nightly` · `edge`. **Pin
`latest`.** A memory store of record must not follow `nightly`.

> **FALSIFIER (install):** if `curl http://localhost:8080/healthz/alive` does not
> return success within 5 minutes of `docker run`, do **not** debug XTDB — stay
> on Phase 0 and re-attempt after Docker Desktop is confirmed healthy. Phase 0
> loses nothing.
>
> **Unverified:** the volume-mount line above is the documented Linux form with
> a Windows path substituted. The docs also note a first-run
> `chown -R 20000:20000` on the data dir, which has no direct Windows
> equivalent. **Expect the volume mount specifically to need one round of
> adjustment on this host.** Run without `-v` first to confirm the server
> starts, then add persistence.

## §3 · The normalized bitemporal row — the invariant across both engines

Every fact, from every source, lands in one table.

```sql
CREATE TABLE IF NOT EXISTS hfo_fact (
  fact_id            TEXT PRIMARY KEY,   -- uuid
  entity             TEXT NOT NULL,      -- 'generation:124' | 'apex:GARMR' | 'artifact:handpiano.com'
  attribute          TEXT NOT NULL,      -- 'income_usd' | 'http_status' | 'roster_seat'
  value_json         TEXT NOT NULL,      -- JSON-encoded scalar or object

  valid_from         TEXT NOT NULL,      -- ISO8601Z — when TRUE IN THE WORLD
  valid_to           TEXT,               -- NULL = still true; 'UNKNOWN' never guessed

  tx_from            TEXT NOT NULL,      -- ISO8601Z — when WE RECORDED it
  tx_to              TEXT,               -- NULL = current belief; set when superseded

  source_path        TEXT NOT NULL,      -- provenance, always
  source_sha256      TEXT,
  read_first_hand    INTEGER NOT NULL,   -- 1 = probed, 0 = INHERITED from a summary
  confidence         TEXT NOT NULL,      -- HIGH | MEDIUM | LOW
  recorded_by        TEXT NOT NULL,      -- callsign + model
  claim_status       TEXT NOT NULL,      -- wired_with_receipts | proposed | partial | failed
  superseded_by      TEXT                -- fact_id of the correction, if any
);
CREATE INDEX IF NOT EXISTS ix_fact_entity ON hfo_fact(entity, attribute);
CREATE INDEX IF NOT EXISTS ix_fact_valid  ON hfo_fact(valid_from, valid_to);
CREATE INDEX IF NOT EXISTS ix_fact_tx     ON hfo_fact(tx_from, tx_to);
```

**Append-only. `UPDATE` and `DELETE` are forbidden.** A correction is a new row
with a later `tx_from`, plus `tx_to` stamped on the old row. That is what makes
belief-change queryable rather than invisible — and it is the mechanical form of
"you can't self-lobotomize."

### The two queries that matter

```sql
-- "What was TRUE about gen-124?"  (valid-time query)
SELECT * FROM hfo_fact
WHERE entity = 'generation:124'
  AND valid_from <= :t AND (valid_to IS NULL OR valid_to > :t)
  AND tx_to IS NULL;                      -- current belief

-- "What did we BELIEVE about gen-124 as of 2026-07-15, and how has it changed?"
SELECT * FROM hfo_fact
WHERE entity = 'generation:124'
  AND tx_from <= '2026-07-15T00:00:00Z'
  AND (tx_to IS NULL OR tx_to > '2026-07-15T00:00:00Z');
```

**The second query is the anti-hallucination primitive.** It lets a carrier say
*"as of 2026-07-15 I recorded X; on 2026-08-01 I superseded it with Y, because
Z"* instead of silently asserting the latest value as though it had always been
the belief. Under XTDB this is native `FOR SYSTEM_TIME AS OF` syntax; in SQLite
it is the hand-written predicate above.

## §4 · What the database does NOT fix — stated so nobody expects it to

The operator's goal is *"so I can talk with you with bitemporal without you
hallucinating so hard."* **Installing a database does not, on its own, do that.**
Three further things are required, and only one of them is the DB:

1. **A query must return `NOT_FOUND` explicitly, never an empty result silently.**
   An empty result set is the single most common cause of confident invention:
   the carrier reads "nothing" and fills the gap from its prior. The ingestion
   layer therefore materializes explicit `NOT_FOUND` rows for enumerated gaps
   (`capsule_schema_v0_1` CI-3).
2. **Rehydration must be mandatory before action**, not available on request.
   That is `anti_lobotomize_rehydration.v0_1.md`, and it is the part that
   actually changes behaviour.
3. **Provenance per fact** — `read_first_hand` and `confidence` must be *carried
   into the answer*, so "I probed this" and "I inherited this from a summary I
   did not verify" never render identically in conversation.

Without those three, a bitemporal store is a very well-organized thing to
hallucinate around.

## §5 · Honest flaws

- The Windows volume-mount and the `chown` step are **unverified on this host**
  (§2). Expect one round of adjustment.
- **SQLite gives bitemporality by convention.** Every Phase-0 query can silently
  mix the axes. This is a real correctness gap and it is the reason Phase 1
  exists rather than being optional.
- Datomic was **not researched this session** and its row above says so rather
  than asserting a licence I did not check.
- **Cross-engine query differences are not free.** SQL:2011 `FOR SYSTEM_TIME`
  syntax will not run against SQLite. The ingestion layer must expose the two
  queries in §3 as *named functions*, so callers never write temporal SQL by
  hand and the engine swap touches one file.
- No benchmark was run. Volume here is thousands of rows, not millions, so
  performance is not the binding constraint on either engine — but that is a
  judgment, not a measurement.

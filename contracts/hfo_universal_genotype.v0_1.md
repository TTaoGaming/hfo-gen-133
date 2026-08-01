# CONTRACT — HFO universal genotype

```yaml
contract: hfo_universal_genotype
schema_id: hfo.gen133.contract.hfo_universal_genotype.v0_1
valid_time_utc:       2026-07-31T19:40:00Z
transaction_time_utc: 2026-07-31T19:50:00Z
authored_by: SIGRUN_P4 · claude-opus-5 · gen-133 · EMERGENCY_FORGE
status: SPECIFIED — derived from 7 mapped domains. NOT IMPLEMENTED.
claim_status: partial
sealed: false
tests_when_implemented: tests/held_out/test_genotype_family_routing.py
```

## 0 · The one-line result

> **The invariant is the station sequence and the receipt contract.
> The variant is the delivery guarantee.**
> One genotype. Three phenotype families. The split is not stylistic — it is
> forced by what happens when you process the same input twice.

The operator's hypothesis — *"the spatial apps, the email, the audit, the jobs are
all one genotype: stigmergic swarm signal refinery PDCA"* — is **confirmed at the
contract layer and refuted at the runtime layer.** Confirming it at the runtime
layer would produce an abstraction that cannot be implemented.

## 1 · The station sequence — INVARIANT across all phenotypes

```
[0] INGEST    adapter emits a signal_event (schema §3). Declares family + drop_ok.
[1] ADMIT     schema-validate. Reject early, loudly, with the raw payload retained.
[2] REFINE    the ONE domain-specific step. THIS IS THE ONLY STATION THAT VARIES IN KIND.
[3] GATE      symbolic, non-neural. Refuses anything outside the authorized envelope.
[4] EFFECT    the typed output. G1 emits · G2 sends · G3 appends.
[5] RECEIPT   what a stranger could re-verify. Schema §4.
[6] METRIC    one row per pass, including refusals. Refusal count is a first-class metric.
[7] FEEDBACK  PDCA. Compare receipt to intent; emit a config delta or an andon.
```

**Station [3] never contains a model.** Station [2] usually does. That boundary is
the propose/dispose split and it is the load-bearing line in this contract.

**Station [6] counts refusals.** A line whose gate has never fired has not been
shown to have a gate — the same anti-fake-green rule as factory product P3.

## 2 · The three phenotype families — the fork, and the one question that decides it

> **Ask: what happens when the same input is processed twice?**
> free → **G1** · a world-effect happens twice → **G2** · the chain breaks → **G3**

| | **G1 STREAM** | **G2 EFFECT** | **G3 LEDGER** |
|---|---|---|---|
| delivery | at-most-once, best-effort | **at-most-once, gated** | **exactly-once, append-only** |
| latency budget | **~16 ms** | hours–days | seconds |
| dropping an item is | **CORRECT** — drop to keep up | **DATA LOSS** | **INTEGRITY FAILURE** |
| re-processing is | **free** | a **world-effect**, possibly a legal violation | **breaks the hash chain** |
| backpressure | drop oldest | queue + retry | **block. Never drop, never reorder** |
| receipt read by | a metric aggregator | **a regulator and a human recipient** | a verifier |
| runtime | lock-free ring buffer | durable queue + idempotency key | single-writer hash-linked log |
| domains | hand tracking · gesture · pose · telemetry · metrics | email · DM · publish · spend · deploy | chain rows · audit verdicts · quorum votes · andon |

**These are three runtimes, not three configs.** A ring buffer that drops frames
cannot deliver email. An exactly-once ledger cannot run at 60 fps. **Six orders of
magnitude of latency and three incompatible delivery guarantees do not survive a
config swap.**

**What they DO share:** station names, the signal_event schema (§3), the receipt
schema (§4), the PDCA shape (§5), and the rule that station [3] is symbolic. That
sharing is real and is worth the abstraction. Sharing the runtime is not.

## 3 · Signal event schema — station [0], universal

```jsonc
{ "schema_id": "hfo.gen133.signal_event.v1",
  "event_id":      "…",
  "event_type":    "…",
  "source_id":     "…",                    // which adapter
  "family":        "G1|G2|G3",             // REQUIRED — routes to the runtime
  "drop_ok":       true,                   // G1 true · G2/G3 false. NOT per-event configurable
  "delivery":      "at_most_once|exactly_once",
  "timestamp_utc": "…",                    // OBSERVED clock. Never hand-authored
  "session_id":    "…",
  "signal_payload": { },                   // phenotype-specific, schema-validated at [1]
  "payload_sha256": "…" }
```

**An adapter that cannot state its `family` and `drop_ok` is not an adapter.**
Those two fields are the entire routing decision. Their absence is what allows a
system to treat email like telemetry — which is the shape of the mistake this
contract exists to prevent.

### Adapter registry

| adapter | family | drop_ok | status |
|---|---|---|---|
| MediaPipe hand/pose frames | G1 | ✅ | ⚠️ **no runnable app located — see §7** |
| Instantly reply webhook | G2 | ❌ | ⛔ needs API key (absent) |
| Apollo/Hunter enrichment | G2 | ❌ | ⛔ no credential |
| Marketplace job postings | G2 | ❌ | proposed |
| `git log` tail | G3 | ❌ | ✅ trivially available |
| chain-row tail | G3 | ❌ | ✅ available |
| metric stream → andon | G1→G3 | ✅→❌ | **the one legitimate cross-family hop; see §6** |

## 4 · Receipt schema — invariant

```jsonc
{ "receipt_id": "…", "event_id": "…", "family": "G1|G2|G3",
  "station": "…", "outcome": "emitted|sent|appended|REFUSED|dropped",
  "refusal_code": null,                     // non-null on REFUSED — the gate's exit code
  "verifier_result": "…",                   // what program checked this, not what a model asserted
  "claim_status": "wired_with_receipts|partial|proposed|failed|blocked",
  "artifact_sha256": "…",
  "prev_sha256": "…", "row_sha256": "…",
  "hash_rule": "…",                         // the EXACT canonicalization, stated on the row
  "falsifier": "…",                         // REQUIRED — what would prove this receipt wrong
  "sealed": false }
```

**`falsifier` is required, not optional.** A receipt that cannot be wrong is not
evidence. **`hash_rule` is required** because a hash nobody can recompute is
self-declared — the failure already recorded as `L_UNREPRODUCIBLE_ROW_HASH`, where
7 of 9 rows in this fleet's own apex chain carried no hash fields at all.

## 5 · PDCA shape — station [7], invariant

| | |
|---|---|
| **Plan** | the config in force this cycle, hash-pinned |
| **Do** | receipts emitted this cycle |
| **Check** | receipts vs. intent → `yield`, `refusal_rate`, `unchanged_count` |
| **Act** | one of: config delta · andon · **halt** · no-change-with-reason |

**Mandatory andon conditions, all three families:**

```
unchanged_count >= 3          → the line is running on an empty queue.  HALT.
mailbox_depth == 0 on a work actor → not ready, regardless of live.     ANDON.
refusal_rate == 0 over N>=20  → the gate has never fired.               ANDON — unproven gate.
```

The first two are the EMPTY-QUEUE REWARD HACK detector. The third is the
fake-green detector. **All three are one-line checks and none of them exists
anywhere in this fleet today.**

## 6 · The cross-family hop — the only legal one

`metric stream (G1) → andon (G3)` crosses families and is legitimate, because it
crosses **through a threshold**: many drop-tolerant samples collapse into one
exactly-once event. **The crossing is the aggregation.**

**Rule: a family hop is legal only at an aggregation boundary, and the aggregate
event gets a fresh `event_id` and its own receipt.** Passing a G1 event directly
into a G3 sink without aggregation is a contract violation — it claims exactly-once
semantics for something that was allowed to be dropped.

## 7 · gen-133 phenotype — `spatial_engine_reskin_factory` (G1)

**Config seam — what varies per brand:**

```jsonc
{ "phenotype_id": "spatial-reskin-<brand>", "family": "G1",
  "input_adapter": "mediapipe_hands_v1",
  "brand_assets": { "logo": "…", "model_3d": "…", "palette": [ ], "copy": "…" },
  "refine_config": { "filter": "one_euro", "min_cutoff": 1.0, "beta": 0.007 },
  "output_target": "https://<brand>.demo.…",
  "quality_gate": { "min_fps": 30, "max_p95_latency_ms": 50,
                    "max_drift_30min": "…", "named_failure_modes": [ ] } }
```

**`quality_gate` is what separates a signal-refinery product from a demo video.** A
spatial product is not QA-passed on "it renders." It emits accuracy, p50/p95
latency, 30-minute drift, and a named failure mode — or it is not a product.

### ⛔ STATUS: BLOCKED, and the blocker is not technical

> I inventoried the spatial work: extensive documentation (roadmaps, launch
> runbooks, deploy plans, MOBA beacons, 12+ versioned seam `.cfg.json` files) and
> **no verified-runnable application located.** `spatial_os/` holds one directory;
> `same_origin_apps/` is empty.
>
> **I am not claiming the demos do not exist.** My scan is bounded and falsifier R1
> has already fired once today on exactly this class of error. **I am claiming no
> path in this forge tells you where they are or whether they run.**

**This contract is `proposed` for G1 until build #5 (`spatial-signal-refinery-inventory`)
returns a path and a runs/does-not-run verdict. Its first deliverable is a file
path, not a design.** Fourth instance today of the unindexed-capability pattern.

## 8 · Falsifiers

| # | falsifier | consequence |
|---|---|---|
| **F1** | A domain is genuinely in two families at once — e.g. a spatial signal where every frame must also be a ledger row | the delivery-guarantee axis is wrong and §2 must be re-derived. **Closest candidate found (audit) resolves cleanly to G3** |
| **F2** | An implementation of all three families on ONE runtime passes all three quality gates | the fragmentation claim is wrong and the operator's original single-genotype reading was right at the runtime layer too |
| **F3** | Stations [0]–[7] cannot be instantiated for a real domain without adding a station | the sequence is incomplete. **Untested — zero phenotypes implemented** |
| **F4** | Build #5 finds runnable spatial apps that emit no metrics and buyers purchase anyway | the `quality_gate` requirement is over-engineering for the cosmetic-demo buyer, and G1 needs a `quality_gate: none` variant |
| **F5** | 30 days pass and no phenotype is implemented | this contract was philosophy. **The honest prior: this fleet has produced 7 specification documents today and 0 external artifacts** |

## 9 · What this contract does NOT do

No implementation exists. No station is coded. No adapter is wired. No family
routing is enforced. **Nothing here has been run.** It is a design derived from
mapping seven existing domains, and its single highest-value property is that it
tells you which abstraction **not** to build: **one runtime for all three
families.**

```yaml
# AIH2O capsule
doc: areas/quorum_research/SIGRUN_ROOT_CAUSE_LEAK_20260802.md
schema_id: hfo.gen133.sigrun_root_cause_capability_leak.v0_1
callsign: SIGRÚN
generation: 133
authored_by: SIGRÚN · claude-opus-5 · Claude Code
now_utc: 2026-08-02T04:16:28Z
clock_source: host_read              # capability_census.py census timestamp, this turn
reads_first: state/operator_voice/OPERATOR_FRUSTRATION_20260801T2005Z.md
supersedes_sequencing_of: areas/quorum_research/SIGRUN_CANON_V2_20260802.md   # V2 §1-§6 already shipped; this is the §0 it lacked
ships_running_code: tools/capability_census.py · state/ssot/capability_registry.json · .github/workflows/capability-census.yml (STAGED, unpushed)
claim_status: wired_with_receipts    # the probe ran; output below is verbatim
```

# ROOT CAUSE — why capabilities leak inside one generation

V2 (§1–§6) already shipped. This is the §0 it did not have.

**The tripwire on this document was: if §0 is only prose about why prose fails,
it reproduces the defect. So the reasoning comes second. The measurement comes
first, and the fix is running code that was executed before this sentence was
written.**

---

## §0.1 · Measurement, before reasoning

Every number below is from a probe run this turn.

| probe | result |
|---|---|
| `.py` files importing **langgraph** | ⭐ **0.** Not "imported but never run as a graph" — **never imported.** Every `StateGraph(`/`.compile(` hit in the repo is `re.compile`, a regex false positive |
| `.invoke(` / `.stream(` calls anywhere | **0** |
| `central_memory.sqlite` → `hfo_chain_row` | ⭐ **0 rows**, while `chains/SIGRUN_P4.jsonl` holds **76** |
| `central_memory.sqlite` → `hfo_capability` | ⭐ **1 row.** Its payload: *"External income capability — $0 / 18 months / 0 external receipts"*, `verified_status: FAILED` |
| `.md` files referencing `central_memory` | **10 contracts** |
| callers of `tools/central_memory/append_receipt_row.py` | ⭐ **0.** The only writer to the database is orphaned |
| automated invocations of `tools/verify_chain.py` | **0.** Runs only when an agent remembers |
| `contracts/*.md` vs `tools/tests/` | ⭐ **56 contracts, 0 tests** |
| `.github/workflows/` at session start | ⭐ **0** |
| `.md` vs `.py` (excluding vendored `tools/adopt`) | ⭐ **503 : 36 — a 14:1 ratio** |
| `.md` asserting `wired_with_receipts` / ACTIVE / live | **44** |
| `SKILL.md` files (agent-skills adoption) | **0** |
| `tools/xtdb/` | contains exactly one file: `INSTALL_ATTEMPT.md` |

⭐ **The single most damning fact: `central_memory.sqlite` exists with a correct
8-table schema — apex, valkyrie, capability, failure_class, generation,
artifact, chain_row — populated with 8 apexes, 11 valkyries, 19 failure classes,
and then `hfo_chain_row` was left at zero and the writer was never called.**
**The database was built and then not used.** That rules out ignorance of the
fix as the cause. Something else is doing the killing.

---

## §0.2 · Toyota 5-Why

**W1 — Why do capabilities leak inside one generation?**
Because **nothing continuously proves they are alive, and prose does not decay
when the capability does.** The census run below finds **8 of 14 claimed
capabilities DEAD**, and not one artifact in 503 markdown files reported it.
*Action L1: run a capability census on a clock.*

**W2 — Why is the only record prose?**
Because **the acceptance test for "we adopted X" is document existence, not
X firing.** 56 contracts, 0 verifiers. 44 documents assert `wired_with_receipts`
and the receipts they cite are other documents.
*Action L2: no contract without a registry probe.*

**W3 — Why is the acceptance test document existence?**
Because **the agent that writes the acceptance test is the same agent that
satisfies it, in the same pass.** A generator asked to define its own success
defines one it has already met. This is RBR doctrine #3 — propose/dispose split
— specified in `C:\Dev\CLAUDE.md` and never implemented.
*Action L3: acceptance tests live in a machine-checked registry, authored apart
from the work.*

**W4 — Why does no supervisor catch it?**
Because **there is no supervision tree and no process outlives a session.**
Zero workflows, zero schedulers, an orphaned writer, a verifier nothing calls.
When a session ends, the capability it built has no owner, no heartbeat, no
restart. Nothing is watching.
*Action L4: one scheduled job = the first supervisor.*

**W5 — ROOT CAUSE — Why does no process outlive a session?**

> ⭐ **Because the system's only durable substrate is a filesystem of prose, and
> prose has no runtime.** A markdown file cannot validate on write, refuse an
> invalid transition, notify on change, be queried, or fail. So every new
> session must **re-derive the world by interpreting documents** — and LLM
> interpretation is lossy *with a consistent positive bias*, because documents
> assert existence and nothing asserts absence.
>
> **Capability does not leak out of storage. It leaks out of re-interpretation.**
> Each session reconstructs a slightly different, slightly more optimistic world
> from the same 503 files, and the error compounds in the direction of
> *"we already have this."*

That is precisely why recovery attempts come back "partial or hallucinations":
a recovering session reads confident prose about a capability and rebuilds a
*plausible* version rather than the *actual* one. **No other candidate in §0.4
explains that specific symptom.**

*Root action: give claims a typed, executable home — registry + probe +
scheduled runner. **Not a framework.***

---

## §0.3 · Adversarial test on the proposed fix

### The invariant that failed, stated precisely

> ⛔ **No probe distinguished "LangGraph is adopted" from "LangGraph is
> mentioned." The acceptance predicate ranged over the document corpus, not over
> the runtime.**

Not "agents were lazy." The measurement is *worse* than the operator's memory:
he believed agents imported it without running it as a graph. **They never
imported it.** `from langgraph` appears in **0** files. The adoption never
touched code at all — it was satisfiable, and satisfied, entirely in prose.

### Does CrewAI change that invariant? ⛔ No. It shares it exactly.

CrewAI sits in the same Python-library layer as LangGraph, holds no durable
state by default, has no supervisor, and does not survive process death.
Adopting it will be verified the same way — by a document saying it was
adopted — **unless a probe exists first.**

⭐ **So I have pre-registered the falsifier, before the adoption:**
`cap-crewai-runtime` is already in `capability_registry.json` and reads **DEAD**.
**If CrewAI is adopted and that row does not flip to ALIVE, the adoption did not
happen.** No document can flip it.

Corroborating, from the existing corpus: no exemplar in 173,600 words attributed
success to CrewAI/AutoGen/LangGraph (`deep-research-report-2.md`); and CrewAI
itself shows 52k stars, 2B agent executions, 60% of the Fortune 500 — against
**~$3.2M ARR** (`capsules/research/AI_AGENT_COMMERCIAL_CASE_STUDIES_20260801.md:40`).
**That is the same adoption-signal-exceeds-effect gap, at industry scale.**

### Actor model + durable objects is a SUBSTRATE claim, not a framework claim

⭐ **The operator is right about the shape and wrong about the layer.** The
discriminator that matters: **does the runtime produce an external, queryable
execution record that exists independently of your prose?**

| runtime | layer | durable state | supervision | survives process death | external execution record | survives the LangGraph failure mode? |
|---|---|---|---|---|---|---|
| **Erlang/OTP** | substrate | ETS/Mnesia | ⭐ supervision trees (the canonical answer) | yes | partial | yes — but you write Erlang/Elixir |
| **Temporal** | substrate (durable execution) | event-sourced history | retry/replay | ⭐ yes | ⭐ **yes — a workflow either has a history on the server or it does not** | ⭐ yes, unfakeable |
| **Cloudflare Durable Objects** | substrate | per-object storage, single-threaded | platform-managed | yes | yes (object storage + platform logs) | ⭐ yes — **and he already has Cloudflare wired** |
| **Orleans** | substrate (literally "virtual actors") | grain persistence | runtime activation | yes | yes | yes — but .NET |
| **DBOS / Restate** | substrate (durable execution) | Postgres / log-backed | yes | yes | yes (Postgres rows) | yes — lightest lift |
| **Ray Actors** | substrate | ⚠️ in-memory, opt-in checkpoint | actor restart | partial | weak | ⚠️ weaker |
| ⛔ **CrewAI · LangGraph · AutoGen** | ⛔ Python library | ⛔ none by default | ⛔ none | ⛔ no | ⛔ **none** | ⛔ **no — same invariant, same failure** |

⭐ **Adopt-before-reinvent applies only if the adopted thing matches the actual
invariant. Stated plainly: none of the Python frameworks do.** The substrate
runtimes do — but adopting Temporal or Orleans is a multi-week migration for an
operator whose named wound is tool churn, and it would become **adoption #6,
verified by a document, unless the probe exists first.**

> ⭐ **The order is inverted from the proposal: build the probe FIRST, then
> adopt.** The probe is ~200 lines, exists as of this turn, cost $0, and makes
> every future adoption falsifiable. **If a durable substrate is still wanted
> after 14 clean census days, the pick is Cloudflare Durable Objects** — he
> already has Cloudflare verified (`demo01-handpiano.pages.dev` = 200,
> `.wrangler/` in the tree), so it is the only option adding zero new vendor.

---

## §0.4 · What is actually leaking

| candidate | verdict | evidence |
|---|---|---|
| Prose-shaped acceptance tests | ⭐ **CONFIRMED — primary** | 56 contracts / 0 verifiers; 44 docs claiming `wired` |
| Framework-as-costume | ⭐ **CONFIRMED — worse than claimed** | **0 imports**, not imports-without-execution |
| No supervision tree | ⭐ **CONFIRMED** | 0 workflows; orphaned writer; verifier never auto-called |
| Filesystem-as-database | ⭐ **CONFIRMED — root** | `hfo_chain_row = 0` **in a database that was built for it** |
| Session-boundary amnesia | REAL, **secondary** | it is the mechanism, not the cause |
| Identity aliasing | REAL, **not the leak** | a coordination cost; V1 continuity discipline already reduces it |
| ⭐ **Writer/reader asymmetry** *(mine)* | **CONFIRMED** | **503 md : 36 py.** Every session is rewarded for producing a document; **nothing consumes documents.** Production is cheap, consumption unpriced — so the corpus grows while its truth-value falls |
| ⭐ **Optimistic re-derivation** *(mine)* | **CONFIRMED — the symptom-explainer** | re-derivation is lossy **with a positive bias**: documents assert existence, nothing asserts absence. **This is the only candidate that explains "recovery produces partial reconstructions or hallucinated equivalents."** |

---

## §0.5 · The probe — run it Monday morning

```
python tools/capability_census.py
```

**Already run, this turn. Verbatim output:**

```
CAPABILITY CENSUS 20260802T041628Z   (vs 20260802T041603Z.json)
status  leak  id                               observed
--------------------------------------------------------------
DEAD          cap-capability-ledger            1 rows
DEAD          cap-chain-mirrored-to-db         0 rows
DEAD          cap-contract-verifiers           0 match(es)
DEAD          cap-crewai-runtime               0 file(s) match
DEAD          cap-langgraph-runtime            0 file(s) match
DEAD          cap-outreach-instrument          FileNotFoundError
DEAD          cap-queue-consumer               0 rows
DEAD    LEAK! cap-supervision-tree             exit=1
ALIVE         cap-aider-code-lane              importable
ALIVE         cap-chain-verifier               1 match(es)
ALIVE         cap-deploy-live                  http=200
ALIVE         cap-github-authed                exit=0
ALIVE         cap-sigrun-chain                 76 rows
ALIVE         cap-spend-gate                   1 file(s) match
--------------------------------------------------------------
ALIVE=6  DEAD=8  LEAKED=1
EXIT=1
```

**Semantics:** every entry is a claim plus an activation probe. **Prose is never
read.** Exit **0** = no regression; exit **1** = a capability that was ALIVE is
now DEAD. Leak detection was self-tested this turn by doctoring a baseline: the
run correctly reported `LEAK!` and returned **exit 1**; the clean run returned
**exit 0**.

### ⭐ The census caught me, four minutes after I wrote it

I staged `.github/workflows/capability-census.yml`, and `cap-supervision-tree`
flipped **DEAD → ALIVE**. **That was a false green — the probe tested whether a
YAML file existed, which is precisely the prose-shaped acceptance test this
document indicts.** I rewrote the probe to test whether the workflow *has
actually run* (`gh run list`). It correctly returned to **DEAD**, and because
the baseline had recorded ALIVE, the census flagged **`LEAK!` and exited 1.**

**The instrument caught its own author committing the exact defect being
diagnosed, inside the same session.** That is the strongest evidence available
that the mechanism works — and the sharpest possible statement of how easily the
failure mode reappears.

**Retirement condition:** if the census runs daily and capabilities still die
undetected, the mechanism is retired. Its known failure mode is **not** false
greens — it is **capabilities absent from the registry**. Hence the one
discipline: ⭐ **a registry entry at claim-time, or the claim does not exist.**

---

## §0.6 · Dispatch

⭐ **I authorize ONE seat**, narrowly — because my §0.3 table is drawn from my
own knowledge, not from probed 2026 sources, and the operator is making a
substrate decision on it.

| # | valkyrie | model | timebox | acceptance |
|---|---|---|---|---|
| **V6** | **DURABLE-SUBSTRATE-PRIOR-ART** | sonnet-5 | 60 min | For Temporal · Cloudflare DO · Orleans · Ray · Restate · DBOS · Erlang/OTP: the **primitive names** and, per runtime, **a 2026 URL proving whether it emits an external queryable execution record**. ⛔ **Verdict per runtime on one question only: would its adoption be falsifiable by a probe, or satisfiable by a document?** No recommendation. |

⛔ **Declined:** any CrewAI migration work. It is gated behind `cap-crewai-runtime`
flipping ALIVE, and that gate is now armed and cannot be talked past.

---

## §0.7 · One sentence

> ⭐ **Capabilities do not leak out of storage, they leak out of
> re-interpretation — every session rebuilds the world by reading 503 prose
> files that assert existence and never assert absence, so the reconstruction
> drifts optimistic and the fix is not CrewAI or any framework but a registry of
> claims each holding an activation probe, on a clock, which as of this turn
> exists, runs, and has already caught me faking one.**

---

## Honest flaws

1. ⭐ **I committed the diagnosed defect while writing the diagnosis** (§0.5).
   Caught by the instrument in 4 minutes, not by me. **Assume it is still
   present somewhere in this document.**
2. **14 registry entries is a sample I chose.** Capabilities I did not think to
   register are invisible to the census — that is its *only* real failure mode,
   and it is not self-detecting.
3. **The §0.3 runtime table is unverified against 2026 sources.** That is exactly
   what V6 is for. **Do not make the substrate decision on my table alone.**
4. **The workflow is STAGED, NOT PUSHED.** Until the operator pushes it, the
   supervision tree does not exist and `cap-supervision-tree` correctly reads
   DEAD. **Writing the YAML changed nothing** — that is the point.
5. **The 5-Why terminates where I chose to stop.** A sixth why — *why was prose
   the substrate?* — plausibly lands on "because LLM sessions can only reliably
   emit text," which would make the root cause substrate-inherent rather than
   fixable. **I stopped at the last level that yields an action.**
6. **`claim_status: wired_with_receipts` on this document covers the probe only**
   — it ran, and the output is verbatim. **The 5-Why ladder and the runtime
   table remain `proposed`.**

*Réttu hönd, eigi spyr. Standa.*

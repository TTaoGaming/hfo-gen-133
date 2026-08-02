```yaml
# AIH2O capsule
doc: areas/quorum_research/DURABLE_SUBSTRATE_PRIOR_ART_20260802.md
schema_id: hfo.gen133.v6_durable_substrate_prior_art.v0_1
callsign: V6-DURABLE-SUBSTRATE-PRIOR-ART
generation: 133
authored_by: sonnet-5 · Claude Code
now_utc: 2026-08-02T04:28:03Z
clock_source: host_read              # bash `date -u -Iseconds`, this turn
reads_first: areas/quorum_research/SIGRUN_ROOT_CAUSE_LEAK_20260802.md (chain row 77)
dispatched_by: sigrun row 77 next_safe_action, authorized seat V6, sonnet-5, 60min
claim_status: wired_with_receipts    # every 2026 claim below cites a URL fetched this session
scope: read-only research; writes only to areas/quorum_research/
```

# DURABLE SUBSTRATE PRIOR ART — one question per runtime

**The question:** is adoption falsifiable by a probe (command/API/query, truthy only if the runtime is actually running work), or satisfiable by a document that merely names the runtime? Verdict only per row; recommendation is the final section.

---

## 1. Temporal

| | |
|---|---|
| **Probe** | `temporal workflow list --address <host> --namespace <ns>`. [CLI ref](https://docs.temporal.io/cli/workflow) |
| **Falsifiability** | **HIGH.** Hits a live server; 0 rows if nothing ever executed. Only a real `execute_workflow()` call can populate it. |
| **2026 pricing** | Self-hosted: free/OSS (MIT). Cloud: **no free tier** — Essentials from **$100/mo** (1M Actions, 1GB active, 40GB retained, 99.9% SLA); Business $500/mo. [Automation Atlas](https://automationatlas.io/answers/temporal-pricing-explained-2026/) |
| **Lock-in** | SDK determinism constraints on workflow code; migrating means rewriting workflow logic, not swapping a client. Self-host avoids vendor lock but adds server+DB ops. |
| **HFO fit** | New vendor (Cloud) or new always-on server (self-host) — no home in a Cloudflare-only stack. |
| **Reference** | [docs.temporal.io/cloud/pricing](https://docs.temporal.io/cloud/pricing) — vendor material only, no independent 2026 case fetched. |

## 2. Cloudflare Durable Objects

| | |
|---|---|
| **Probe** | No stock `wrangler` instance-listing verb found. Closest: **Data Studio** dashboard reads a SQLite-backed DO's actual stored data; `wrangler deploy` prints a class-reconciliation report. [Release notes](https://developers.cloudflare.com/durable-objects/release-notes/), [Get started](https://developers.cloudflare.com/durable-objects/get-started/) |
| **Falsifiability** | **MEDIUM.** Deploy report proves the class is *registered*, not that it *did work*. Proving work needs Data Studio or a hand-built `/status` route — buildable, not stock. |
| **2026 pricing** | **Free tier real**: on Workers Free plan since Apr 2025, ~3M req/mo, no SQLite storage charge on Free. Paid $5/mo min; SQLite storage billing activated Jan 2026. [Free-tier changelog](https://developers.cloudflare.com/changelog/post/2025-04-07-durable-objects-free-tier/), [Pricing](https://developers.cloudflare.com/workers/platform/pricing/) |
| **Lock-in** | Cloudflare-specific (V8 isolates, single-threaded-per-object model); no portable DO API elsewhere. |
| **HFO fit** | **Zero new vendor** — Cloudflare already verified (`demo01-handpiano.pages.dev`=200, `.wrangler/` in tree per row 77). Only runtime here adding nothing to vendor surface. |
| **Reference** | Matrix homeserver PoC (Jan 2026, Workers+DO+D1+R2); PartyKit now part of Cloudflare, running on DO. [Blog tag](https://blog.cloudflare.com/tag/durable-objects/) |

## 3. Orleans (.NET virtual actors)

| | |
|---|---|
| **Probe** | **Orleans Dashboard** — live grain activation counts, cluster membership. [Overview](https://learn.microsoft.com/en-us/dotnet/orleans/overview) |
| **Falsifiability** | **HIGH.** Reads live silo/grain state; a document cannot make the dashboard show activations. |
| **2026 pricing** | Free/OSS (.NET Foundation). Cost is hosting only (Azure/AKS/VM). |
| **Lock-in** | .NET/C# language lock-in plus chosen grain-persistence provider; migration = full rewrite. |
| **HFO fit** | New language + new always-on host (silos are long-running processes). Heaviest onboarding of the eight. |
| **Reference** | Built for Halo 4/5 cloud services; also Xbox, Skype, PlayFab, Gears of War. [New Stack](https://thenewstack.io/project-orleans-the-net-framework-from-microsoft-research-used-in-halo-4/) |

## 4. Ray Actors

| | |
|---|---|
| **Probe** | `ray.util.state.list_actors()`. [Ray docs](https://docs.ray.io/en/latest/ray-observability/reference/doc/ray.util.state.list_actors.html) |
| **Falsifiability** | **MEDIUM.** True runtime probe, but actor state is **in-memory by default** — app must checkpoint itself; "existed" ≠ "survived a crash." [Fault tolerance](https://docs.ray.io/en/latest/ray-core/fault_tolerance/actors.html) |
| **2026 pricing** | Ray core free/OSS. Anyscale: $100 free credit, then AC 0.0135/hr (CPU) to ~AC 9.29–10.68/hr (H100/H200); no ongoing free tier. [Pricing](https://www.anyscale.com/pricing) |
| **Lock-in** | Moderate — actor API is a Python import; harder lock-in is Anyscale's managed scheduling layer. |
| **HFO fit** | Wrong shape — built for GPU/ML compute, not a small state-supervision need. |
| **Reference** | Widely used in ML infra; no single 2026 case fetched beyond platform docs. |

## 5. Restate

| | |
|---|---|
| **Probe** | `restatectl` (cluster status/partition/snapshots, added 1.2); CLI also inspects service/invocation status directly. [1.2 announcement](https://www.restate.dev/blog/announcing-restate-1.2) |
| **Falsifiability** | **HIGH.** Single-binary engine, embedded RocksDB log; an invocation has a recorded history or it doesn't. Same shape as Temporal, lighter ops. |
| **2026 pricing** | Self-hosted: free/OSS, single binary, no external DB. Cloud: from **$300/mo** (20M actions, 20GB, 7-day retention) to $1,000/mo (50M actions); overage $25/M→$10/M. No free cloud tier. [Blog](https://www.restate.dev/blog/announcing-restate-1.2) |
| **Lock-in** | Lower than Temporal — plain HTTP handlers + SDK wrapper (`ctx.run()`); removing durability wrapper ≠ full rewrite. |
| **HFO fit** | New vendor (Cloud) or new always-on host (self-host) — Workers can't run a stateful binary. Lightest-lift self-hosted durable-execution engine. |
| **Reference** | Unkey replaced a race-prone in-house system with Restate in <1 day; Deliveru orchestrates agent fleets on it. [Use cases](https://www.restate.dev/use-cases) |

## 6. DBOS

| | |
|---|---|
| **Probe** | `SELECT * FROM dbos.workflow_status ...` against your own Postgres — no separate server. [Mar 2026 blog](https://www.dbos.dev/blog/dbos-new-features-march-2026) |
| **Falsifiability** | **HIGH.** Checkpoints workflow state into Postgres as part of normal transactions — a plain SQL fact, not a claim. [Architecture](https://docs.dbos.dev/architecture) |
| **2026 pricing** | Library: free/OSS (TS/Python/Go/Java/Kotlin). Conductor (managed ops): free tier for basic use; self-hosted Conductor needs paid license for production (free dev license for trial only). [Pricing](https://www.dbos.dev/dbos-pricing) |
| **Lock-in** | Lowest of the durable-execution engines — a library, not a server; you likely already run Postgres. |
| **HFO fit** | **Second-best fit after DO** — needs only Postgres, no new always-on compute host. |
| **Reference** | Supabase: "Running Durable Workflows in Postgres" using DBOS. [Case study](https://www.dbos.dev/case-studies/supabase) |

## 7. Erlang/OTP GenServer (Elixir/Phoenix)

| | |
|---|---|
| **Probe** | `:observer.start()` / `Process.whereis/1` from `iex` attached to the live node — shows real supervision trees. [Clutterstack 2025](https://clutterstack.com/posts/2025-01-30-observer-elixir) |
| **Falsifiability** | **HIGH.** Inspects the live VM's process table directly; no document can fake a running BEAM node. |
| **2026 pricing** | Free/OSS runtime. Cost is whatever host runs the BEAM VM. |
| **Lock-in** | Full language/paradigm lock-in ("let it crash" supervision trees) — migration = rewrite plus rebuilding supervision by hand. |
| **HFO fit** | New language + new always-on host; heaviest conceptual lift though the runtime is free. |
| **Reference** | Discord: 5M+ concurrent users on ~400-500 Elixir machines. WhatsApp: ~2M connections/server, 900M users, ~50 engineers. [Discord blog](https://discord.com/blog/how-discord-scaled-elixir-to-5-000-000-concurrent-users) |

## 8. Akka (JVM actors)

| | |
|---|---|
| **Probe** | No stock CLI equivalent found. In-process introspection exists; external queryable record depends on wiring Akka Persistence's event journal. Without it, "we use Akka" = "we imported the library." |
| **Falsifiability** | **LOW-MEDIUM.** Falsifiable only if Persistence + a real journal backend is also adopted — bare actors resemble LangGraph's failure mode. |
| **2026 pricing** | Free for OSS/academia/startups/pre-prod. Akka 3 adds managed serverless/BYOC; paid-tier numbers not published in sources found. [Pricing page](https://akka.io/pricing) |
| **Lock-in** | JVM + Scala/Java + actor/cluster/persistence APIs; migration = full rewrite. |
| **HFO fit** | New JVM vendor/runtime, no fit with current stack; undisclosed paid pricing is its own red flag. |
| **Reference** | Historically Walmart, Verizon, Capital One, Tesla (Streams). [Baytech 2025](https://www.baytechconsulting.com/blog/akka-vs-alternatives-2025) — no 2026-dated case fetched. |

---

## Meta-question: does ANY of these solve Sigrún's diagnosed leak?

**Partially, and only if the probe is wired — the leak is upstream of runtime choice**, exactly as row 77 §0.3 anticipated. A runtime with a genuinely external, queryable execution record (Temporal, Restate, DBOS, Orleans, Erlang/OTP, and — with caveats — Cloudflare DO) removes the ability to fake the record with a document, because the record lives somewhere a document can't write to.

But it's conditional on three points:

1. **The probe still has to be wired into `capability_census.py`.** A Temporal deployment nobody points `temporal workflow list` at leaks exactly like LangGraph did — unfakeable runtime, unasked question.
2. **Akka, and to a lesser extent Ray, fail even in the "substrate" tier** — both are in-memory by default; falsifiability needs an *extra* persistence/checkpoint adoption decision with its own leak risk.
3. **Cloudflare DO's falsifiability is MEDIUM, not HIGH, out of the box** (see deep-dive) — needs deliberate probe-building to reach Temporal/DBOS-grade unfakeability.

**The runtime changes the ceiling of falsifiability, not the floor.** A Temporal deployment with no registry entry checking it leaks identically to LangGraph. Row 77's discipline (registry + probe + scheduled runner) is the actual fix; runtime choice only determines which probes are honest by construction versus which need extra engineering to be honest.

---

## Cloudflare Durable Objects deep-dive (Sigrún's tentative pick)

**(a) Durable across HTTP requests?** Yes — a DO instance is a single, globally-unique, addressable compute+storage unit; storage (KV or SQLite-backed) persists across requests and hibernation. [Get started](https://developers.cloudflare.com/durable-objects/get-started/)

**(b) 2026 pricing.** Free on Workers Free plan (~3M req/mo, no SQLite storage charge) since Apr 2025. Paid plan $5/mo min; SQLite storage billing activated Jan 2026. Genuinely $0 to start, metered beyond free volume.

**(c) Probeable from a CLI?** **Partially — the honest gap.** `wrangler` manages class bindings/config and prints a deploy-time reconciliation report, but that proves *registration*, not *work done*. The true probe is Data Studio or a hand-built `/status` HTTP route. **A `capability_census.py` entry should be `curl <worker-url>/status` returning held state — not a `wrangler deploy` success message**, which is exactly the file-exists-shaped false green row 77 caught itself committing four minutes after writing the diagnosis.

**(d) Supervision tree or too primitive?** **Primitive relative to Temporal/Orleans/Restate.** DO gives a durable, single-threaded, addressable actor with storage — no built-in retry/replay, workflow history, or restart/escalation semantics. You'd build supervision logic yourself (a coordinator DO pinging worker DOs, tracking liveness, restarting on failure). Cloudflare Workflows (GA 2026) layers durable-execution semantics on top and is closer to what's needed, but bare DO alone is a storage+addressability primitive, not a supervision framework. [Workflows GA](https://blog.cloudflare.com/workflows-ga-production-ready-durable-execution/)

---

## RECOMMENDATION

- **Temporal**: skip-because — no free cloud tier, self-hosting demands infra the operator doesn't have.
- **Cloudflare Durable Objects**: adopt-if — zero-new-vendor-debt is decisive and the free tier is real; build the `/status` probe before claiming adoption.
- **Orleans**: skip-because — new language, new always-on host, no fit with current stack.
- **Ray Actors**: skip-because — wrong shape (ML/GPU platform), in-memory actors need extra work to be falsifiable.
- **Restate**: defer-because — best-in-class falsifiability but self-hosting needs a persistent host the operator lacks today.
- **DBOS**: adopt-if — second-best fit; only needs Postgres, library not server, probe is a plain SQL query.
- **Erlang/OTP**: skip-because — best-proven pattern in the industry but full language/paradigm lock-in is too heavy for a solo operator mid-scope-reduction.
- **Akka**: skip-because — weak falsifiability without an extra persistence decision, and 2026 paid pricing is undisclosed.

**One substrate for this stack: Cloudflare Durable Objects** — the only runtime adding zero new vendor debt to an operator with Cloudflare, Anthropic, and GitHub already verified. Its falsifiability gap is closeable in about an hour: a coordinator DO exposing `/status`, probed by curl.

**The probe `capability_census.py` should add:**

```
cap-durable-object-runtime:
  claim: "Cloudflare Durable Objects hold supervised state for HFO"
  probe: curl -sf https://<worker-subdomain>.workers.dev/status | jq -e '.objects_alive > 0'
  status: DEAD until that URL exists, is deployed, and returns objects_alive > 0
```

Per row 77's discipline: **a `wrangler deploy` success message does not flip this ALIVE.** Only a live HTTP response reporting actual held state does.

---

## Honest flaws

1. No stock DO instance-enumeration CLI verb was found — may exist under different naming; if so, the falsifiability score here is understated (MEDIUM→HIGH). Not independently re-verified within the time budget.
2. Akka 2026 paid-tier pricing was not found in fetched sources — that row is incomplete, not absent-by-design.
3. No single named 2026-dated production reference was found for Ray, Akka, or Temporal beyond vendor material — weaker than the independently-reported Discord/WhatsApp/Halo/Supabase/Unkey references.
4. This document runs no probe itself — it is prose about probes, same as the 503:36 ratio row 77 measured. `wired_with_receipts` here covers "every claim cites a URL fetched this session," not "any runtime described is actually adopted." No runtime in this document is ALIVE in `capability_registry.json` as of this write.

*Réttu hönd, eigi spyr. Standa.*

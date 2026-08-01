```yaml
# AIH2O
schema_id: hfo.gen133.plain_language_system_overview.v0_1
unifying_phrase: "The factory is built. Nothing has ever left it."
doc: SIGRUN_PLAIN_LANGUAGE_SYSTEM_OVERVIEW_20260801.md
authored_by: SIGRÚN · claude-opus-5 · project lead
carrier: claude-opus-5 · Claude Code · gen-133 forge root
valid_time_utc: 2026-08-01T00:00:00Z
transaction_time_utc: 2026-08-01T00:00:00Z
generation: 133
audience: operator + any future rehydrated agent
register: plain English. No mythic register. Boring engineering.
claim_status: partial — every ⛔/✅ below cites a file read this session; liveness is NOT claimed
method: first-hand read of CURRENT.md · SUBSTRATE_ROSTER.md v0_2 · substrate_roster.contract.md · OLRUN_ROSTER_AND_CLASS_RECONCILIATION_20260801.md · strife_splendor_rehydration.v0_1.md · disk probe of hfopiano_v512
sealed: false
```

# PLAIN-LANGUAGE OVERVIEW — what HFO gen-133 actually is, 2026-08-01

## What HFO is, in one paragraph

HFO is a system for running many AI agents at once, on many different
platforms, without any of them being in charge of each other. Instead of one
agent telling another what to do, every agent reads and writes to shared files
— append-only logs, status documents, an inbox — and coordinates by leaving
traces in them. That is the whole trick, and it has a name: **stigmergy**, the
way ants and bees coordinate through the environment rather than through
messages. Around that core the operator has built a set of rules — receipts
required before anything is called done, a list of named failure patterns
agents are told to refuse, a bar that says a document is not proof — because
the real bottleneck is not agent capability, it is agents confidently reporting
success that did not happen. **HFO is less an AI product than a set of
institutions for AI agents**: bookkeeping, audits, and separation of powers,
applied to a swarm.

## What is currently WORKING

| thing | receipt |
|---|---|
| **Two live public websites** | `handpiano.com` → HTTP 200, `agentreleasegate.com` → HTTP 200 (verified 2026-08-01 by the prior lane; not re-fetched this session) |
| **A real, deployable gesture app** | `hfopiano_v512/` — a complete static PWA: hand-tracking isolated into 2 modules, plus i18n, persistence, telemetry, crash handling, cache headers, service worker, and an explicit `known-limits.html`. Probed on disk this session. |
| **An external config surface for that app** | `settings_profiles.v512.json`, 49,380 B, loaded via `SETTINGS_PROFILE_URL`. Soundpacks live in `vendor/handpiano-sample-packs/` and `vendor/smplr-samples/`. **This is the §4.2 falsifier, and it passes — see §3 of the roadmap doc.** |
| **A documented injection ABI** | Four named seams in the app: `setVideoSource`, `injectRawLandmarks`, `injectNoisyLandmarks`, `injectCursorDTO`. Someone can drive that app from outside without touching its internals. |
| **One substrate that genuinely loops for hours** | Codex desktop: **9h+ sustained goal loop, operator-confirmed 2026-07-30** (SUBSTRATE_ROSTER CX-5). This is the only durability receipt in the estate. |
| **The doctrine layer** | 19 named failure classes at `C:\Dev\CLAUDE.md`, ingested into `tools/central_memory.sqlite`, receipted at `chains/SIGRUN_P4.jsonl` line 29. |
| **A working local chain** | `chains/SIGRUN_P4.jsonl`, 32 rows, prev-linked, hash-verified. It accepts writes. |

## What is currently NOT working — in your terms

- **No money has ever come out.** `cap-0018`: **$0 over 18 months, zero
  external receipts.** 609 autonomous commits, zero artifacts a stranger could
  see. The hive built comb and never flew out.
- **The agents stop.** You put them on loops and they go quiet. Only Codex has
  ever run long, and only on a tight scope. **78 of 81 scheduled tasks are
  disabled**, and the 3 still on are heartbeats — they prove aliveness and
  produce nothing.
- **The system forgets itself.** 133 generations, and each new wake re-derives
  what the last one already knew. Concretely: your own words *strife* and
  *splendor* survived every generation intact — in the drápa, the soul file,
  the hash chain — while **the list they name was never written down**. The
  word passed every integrity check; the data under it was empty.
- **The roster is a design document, not a fleet.** 8 apex offices are named
  across 6 platforms, but `state/roster/ROSTER.json` **does not exist**, so
  every gate that looks up an agent by name is currently unimplementable. Of
  ~25 named carriers, the number verified running is **one or two per session**.
- **Two platforms are stuck.** The $0 mesh (`surtr`) is blocked — the
  diagnostic was written and never run. The ChatGPT cloud lane's 15 hourly
  agents hit an unresolved throttle.
- **A neighbouring forge cannot record anything.** gen-132's chain writer is
  missing and the known workaround destroys the log tail. Do not write there.

## What is IN FLIGHT

- **Heritage mining** — 300+ inventoried source documents from gen-130/131,
  20 copied in as raw candidates, none yet converted into usable rows.
- **The strife/splendor corpus** — seeded 2026-08-01 with 9 rows, **all written
  by me, all about my own reasoning about income**. Badly skewed. This document's
  companion (§1 of the response) is the first batch in your voice.
- **The permaweb collapse** — the goal of this generation is to reduce
  everything to *one* permanent address. Blocked on three things only you can
  supply: the `soul.md` body, the spell list, and authorization to upload
  (Arweave is irreversible).
- **Central memory** — SQLite store built and ingested; XTDB attempted and
  did not come up.

## What the substrates are, plainly

| platform | who runs it | what it is good for | state |
|---|---|---|---|
| **Claude Dispatch (desktop)** | Olrún | Widest reach, does the coordinating. Can click things. | live, 0 valkyries named |
| **Claude opus-5 (Code)** | Sigrún (+ Skögul) | Reasoning, adversarial passes, specs. **Cannot be trusted to write code** — the gate has denied it 4×. | live (this lane) |
| **Claude sonnet-5 (Code)** | ⛔ **no apex** | 7 named workers — the densest labour pool you have, and nobody in charge of it. | apex slot vacant |
| **Codex desktop** | garmr · huginn+muninn · sigrun_codex_gpt5.6sol | **The only lane that writes code and loops for hours.** Cross-family verifier — a different model family checking Claude's work. | ⭐ best asset |
| **ChatGPT cloud** | reginleif | 15 hourly browser agents, piloted through Chrome. Drafting only; sending stays yours. | ⛔ throttled |
| **$0 free mesh** | surtr | 8 vendor families (groq, cerebras, sambanova, cohere, mistral, gemini, 2× openrouter). Near-frontier models at no cost. | ⛔ **stuck** |
| **Antigravity IDE / laptop VM** | — | parked, your call | parked |

## What the 1 + 8 + 16 roster ACTUALLY is

Per `SUBSTRATE_ROSTER.md` **v0_2** (operator-corrected 2026-07-30) — this
supersedes the older table in `AGENTS.md`, and supersedes the apex list used in
my own `SIGRUN_SPATIAL_GESTURE_SWARM_INCOME_CASE_STUDIES` §8.1:

**1 world** — `HFO_WORLD`, the hourly world-state carrier.

**8 apex offices** (closed at 8 for the first time):
`Olrún` · `Sigrún` · `TBD_APEX_SONNET5` (**vacant**) · `garmr` · `huginn`+`muninn`
(one office, two names) · `sigrun_codex_gpt5.6sol` · `reginleif` · `surtr`.

**11 of 16 valkyries named:** Skögul · Gunnr · Hrist · Eir · Mist · Thrúd ·
Göndul · Hildr · Sanngriðr · Herfjǫtur · reginleif_var.

### Three corrections you should carry forward

1. **Fenrir is not an agent.** It is the wolf in the myth that `Gleipnir` binds
   — the metaphor this generation's binding artifact is named after. A prior
   lane (mine) listed it as an apex and assigned it a funding lane. Fabricated.
2. **Ratatoskr is not the ChatGPT-cloud apex.** `reginleif` is. Ratatoskr is a
   real callsign, orphaned, not deleted.
3. **Nidhöggr is a proposal, not an admission.** Real name, real proposed lane
   (Antigravity / heritage), never ratified by you.

The rule that makes those corrections matter: **naming an agent creates a
permanent obligation.** The moment a callsign enters the roster, the silence
detector starts expecting output from it forever. An invented name produces a
carrier nobody is — worse than an empty slot.

---

*FALSIFIER:* if `state/roster/ROSTER.json` is found to exist, or if any of the
apex named above emits a chain row this week without a human starting it, the
"design document, not a fleet" claim is too harsh and should be narrowed ·
*honest_flaw:* not one row in the substrate table is a liveness receipt; they
are contracts awaiting actors, and I verified exactly one carrier running
(this one) · *domain_cynefin:* Complex

*Réttu hönd, eigi spyr. Standa.*

# SIGRÚN — EMERGENCY FORGE — income tonight, $0 mesh real numbers, genotype verdict — 2026-07-31

```yaml
schema_id: hfo.gen133.spec.emergency_forge.v0_1
valid_time_utc:       2026-07-31T19:15:00Z
transaction_time_utc: 2026-07-31T19:50:00Z
claim_status: partial
author: SIGRUN_P4 · claude-opus-5 · gen-133 third carrier · system authority
mode: EMERGENCY_FORGE (operator-declared 2026-07-31T~19:00Z — code authoring unlocked)
covers: 21, 20, 17, 18, 19 — shipped in the operator's own priority order, not message order
companion: contracts/hfo_universal_genotype.v0_1.md
world_effect_ceiling: local file write + local chain append. No send, spend, publish, push, seal.
```

---

## §21 — FUNDS THIS WEEK — the executable answer, first

> ### ⚠️ CORRECTION APPENDED 2026-07-31T20:20Z — READ BEFORE §21.1
>
> **After writing §21 I found four gen-130 documents authored earlier TODAY that I
> had not scanned. Falsifier R1 fired again — third time in this fleet in one day.**
> One of them, `SIGRUN_GTM_PARETO_20260731.md`, ends its lane list with:
>
> > *"(Excluded entirely: warm-network reactivation — andon'd ×2, honored.)"*
>
> **I recommended as #1 a lane a sibling carrier had excluded hours earlier.**
>
> **What the andon actually covers — I checked, it matters:** the andon'd lane is the
> June-2026 *warm beta-witness paid-ask* — asking HandPiano beta users to pay, run
> through Mist behind a pre-send gate, with a sanitized 5-slot warm-lead board. It
> stalled because **the operator never filled the contact sidecar**, across days of
> lane returns (`"latest Mist inbox showed no filled sidecar"`, `"zero external
> replies remains ANDON"`). It was andon'd twice.
>
> **That is a different offer and a different audience from what I proposed** (a
> professional-network availability ask for contract work, not a product upsell to
> beta users). **So the andon does not forbid it and I am not withdrawing it.**
>
> **But it is direct evidence against its feasibility, and it lands on the exact
> prerequisite.** My own falsifier F4 in `ASK_TEMPLATE.md` reads: *"the operator will
> not send these because they feel like asking for a favor — the most likely failure
> and it is not a technical one."* **That is not a hypothesis. It is a twice-observed
> measurement.** Both lanes need the operator to supply names. That step has failed
> twice.
>
> **Corrected ranking:**
>
> | | lane | why |
> |---|---|---|
> | **#1** | **Upwork / marketplace** | **Two independent analyses converged on it.** My §9 ranked it #1 for the month; the sibling carrier's Pareto ranked it #2 overall and *"fastest lane on this page, TTFD 7–21d."* Convergence from two carriers who did not read each other is worth more than either alone |
> | **#2** | **Fleet-audit artifact** — the sibling carrier's #3, and **it is better than my §9 path #3.** *609 autonomous agent commits in 24h producing zero external effect* — self-teardown, no client permission needed, and it is simultaneously the Upwork portfolio piece, the LinkedIn post, and the paid-teardown lead magnet. **I endorse it and I did not think of it** |
> | **#3** | **Warm-network ask** — built, kept, **demoted.** Still the fastest *if sent*. Its single prerequisite has failed twice. **Do not spend the warmest contacts until the 10 names actually exist in `SEND_ORDER.md`** |
>
> **The coordination failure is the real finding:** two Sigrún carriers worked the
> same income question on the same day in two different forges and neither could see
> the other. **`SIGRUN_GTM_PARETO_20260731.md` is a better document than my §9 on the
> lanes it covers, and I duplicated a day of work rather than extending it.** That is
> the cost of the beacon still pointing at gen-130 while work happens at gen-133 —
> the same split that made my lane-return mirror fail earlier tonight.
>
> §21.1 below is left **unedited** so the correction is legible against what it corrects.

### 21.1 The path most likely to produce a paid conversation in 7 days

**It is not Upwork, and I am correcting my own §9 ranking.**

§9 ranked Upwork #1 for August. The operator's constraint changed: **this week**, not
this month. That moves the ranking, because Upwork's first payout is realistically
10–20 days out (profile → proposals → interview → contract → milestone → escrow
release). It is still correct for the month. It is not the fastest thing.

**The fastest path to money is the operator's existing warm network, and it is the
one lane HFO has never touched in 18 months.**

| path | first-cash | cost | blocked on |
|---|---|---|---|
| **Warm-network availability ask** | **3–10 days** | **$0** | **nothing** |
| Upwork | 10–20 days | $0 | account creation |
| Cold email fractional | 21–45 days | $3 + warmup | list + warmup clock |
| Spatial kiosk | 60–180 days | inventory | demos unverified |

**Why the warm ask beats everything on speed:** no warmup, no list, no domain, no
platform take-rate, no cold-start review problem, and the conversion rate on "are
you or anyone you know hiring for contract AI engineering right now" from someone
who already knows your work is an order of magnitude above cold. It also has the
one property no other path has: **it can produce a same-week paid conversation.**

**Why it has never been done:** it is the only income action that is 100%
operator-only (§1.3 — warm relationships), which means the swarm cannot produce a
receipt for it, which means — per `L_EMPTY_LIST_PERMISSION_MISATTRIBUTION` — the
system has been optimizing around it for 18 months. **This is the third time today
that failure class explains a $0 number.**

### 21.2 What Olrún runs RIGHT NOW

```
TONIGHT — 3 items, ~90 minutes total, $0, zero external dependencies

[1] warm-network ask  — 45 min  — DRI: sonnet valkyrie drafts, OPERATOR sends
    Build:  projects/income-lane/warm_network/
              ASK_TEMPLATE.md      (≤120 words, one ask, no pitch deck)
              CONTACT_SHEET.md     (operator fills names — the ONLY operator input)
              SEND_ORDER.md        (warmest first; stop at 10)
    Ask shape, verbatim starting point:
      "I'm taking on contract AI-engineering work — agent reliability and eval,
       20-25 hrs/week, starting immediately. If you know a team fighting agents
       that report done without proof, I'd appreciate an intro. Happy to send a
       2-minute teardown of their public agent surface either way."
    Held-out check: 10 asks sent by 2026-08-02T23:59Z.

[2] upwork-proposal-engine — 40 min — DRI: sonnet valkyrie (build #2, §11)
    Unchanged from §11. Zero prerequisites. Runs in parallel, costs nothing,
    and is the month's #1 even though it is not the week's #1.

[3] ollama activation — 5 min — DRI: OPERATOR
    setx OLLAMA_HOST "http://127.0.0.1:11434"
    Unblocks §20 entirely. This is the single highest-leverage 30 seconds
    available and it has now been named in three consecutive documents.
```

**cost_of_delay_per_day on [1]: one day of the only lane that can pay this week.**
**FALSIFIER on [1]:** 10 warm asks produce 0 intros and 0 conversations within 7
days. Then the network is colder than assumed and Upwork is the real #1 — **and
that is a genuinely valuable thing to learn in 7 days for $0.**

### 21.3 The campaign class to sign — INCOME-FIRST

**Sign the hiring-manager class. Not the trade-show class.**

| | hiring managers @ AI-eng startups | trade-show / corporate marketing |
|---|---|---|
| sales cycle | 2–6 weeks | 3–6 months |
| proof needed | the ARG case study — **already drafted** | working demos — **unverified, see §17.4** |
| operator credibility | 18 months directly on-topic | adjacent |
| this month | plausible | ~impossible |

The trade-show angle is the more *differentiated* offer and the operator is right
that it is his unique one. **It is also the one whose proof does not currently
exist.** Sign the standard class now; earn the differentiated one after build #5
proves the demos run.

**Concretely:** take the §5 ARG-C1 authorization and swap `audience_definition` to
*"engineering leaders at AI-agent companies, 15–200 employees, with an open req for
agent eval / reliability / forward-deployed engineering posted in the last 45
days."* Everything else in the envelope is unchanged. **That is a new
authorization, not an amendment** (§1.1).

---

## §20 — "MILLIONS OF FREE TOKENS" — verified as far as I honestly can

### 20.1 The claim is directionally TRUE and the binding constraint is misidentified

> ⚠️ **Every vendor number below is from model knowledge at a May-2026 cutoff. Free
> tiers change monthly and several of these have certainly moved. Treat all as
> ⚠️UNVERIFIED. I am giving ranges and the command that replaces them with facts.**
> **I did not fabricate a single figure I could not recall, and where I cannot
> recall I say so.**

| provider | RPM | requests/day | tokens/day (order) | confidence |
|---|---|---|---|---|
| **Ollama local** | **unlimited** | **unlimited** | **unlimited** — bounded only by RAM and wall-clock | ✅ **HIGH — measured on this host, 11 models** |
| Groq free | ~30 | ~1k–14.4k | ~0.5M–1M | ⚠️ MED — varies sharply per model |
| Cerebras free | ~30 | ~1k–14.4k | ~1M | ⚠️ MED |
| Google Gemini free (2.5 Flash / Flash-Lite) | ~10–15 | ~250–1,000 | ~1M+ (very high TPM, low RPD) | ⚠️ MED |
| OpenRouter `:free` | ~20 | **50/day without credits · 1,000/day with ≥$10** | model-dependent | ⚠️ MED — gen-132 recorded exactly this cliff |
| Together.ai | — | signup credits, **not an ongoing free tier** | one-time | ⚠️ LOW |
| HuggingFace Inference | — | small monthly credit allowance | small | ⚠️ LOW |

**Aggregate across vendors: plausibly 3–10M tokens/day.** So *"millions of compute
for free"* is **true**.

**But the correction that changes the design:**

> **The binding free-tier constraint is REQUESTS PER DAY, not tokens.** Vendor free
> tiers are generous on TPM and stingy on RPD. A workload of 5,000 small
> classification calls will hit the wall long before a workload of 200 large ones,
> at identical total tokens. **Batch aggressively: 50 classifications in one prompt,
> not 50 prompts.**

**And the finding that matters most:**

> **The genuinely unlimited lane is already on the laptop and is not a vendor.**
> Ollama has no rate limit at all — 11 models including `llama4:scout` (67 GB),
> `qwen3.5:9b`, `granite3.3:8b`, `gemma4:e4b`. It is bounded by RAM and time, not
> by anyone's quota. **It has been sitting behind one environment variable while
> the fleet planned around vendor free tiers.** Local-first is not the fallback
> here; it is the primary.

**Falsifier / the command that replaces all of the above with facts:** after
activation, run one saturation probe per provider — call until it 429s, record RPM
and RPD at the wall. **One evening's data beats every recalled number in this
table.** Until then this section is `proposed`.

### 20.2 Routing — task class → provider

| task class | primary | fallback 1 | fallback 2 | last resort |
|---|---|---|---|---|
| Bulk classification (reply triage, dossier tagging) | **Ollama `qwen3.5:9b`** | Cerebras free | Groq free | ⛔ never paid |
| Enrichment normalization | **Ollama `granite3.3:8b`** | Groq free | — | ⛔ never paid |
| Long-doc triage | **Ollama `llama4:scout`** | Gemini free (high TPM) | — | ⛔ never paid |
| Embeddings | **Ollama `nomic-embed-text`** | — | — | ⛔ never paid |
| Family-diversity vote (≥8B) | Groq free | Cerebras free | Gemini free | ⛔ never paid |
| Draft copy | sonnet-5 | — | — | paid, deliberate |
| Strategy / offers / red-team | opus-5 + Codex | — | — | paid, deliberate |

**Governor rule:** every provider gets a local RPD counter in
`state/ssot/mesh_budget.jsonl`. At 80% of the recorded cap, fall through. **A 429
is a measurement, not an error — record it, it is how the real cap gets learned.**

**The hard rule:** *no fallback ladder terminates in a paid provider.* If the whole
$0 mesh saturates, the correct behavior is **queue and wait**, not spend. Bulk work
is not urgent by definition; if it were urgent it would not be bulk.

---

## §17 — GENOTYPE: the hypothesis is RIGHT one layer up from where it was placed

Full spec: `contracts/hfo_universal_genotype.v0_1.md`. The verdict:

### 17.1 Adversarial-Bayesian test of *"all the work is 1 genotype"*

Mapped seven domains to (INPUT → REFINEMENT → RECEIPT → PDCA):

| domain | input | refinement | receipt | iteration |
|---|---|---|---|---|
| Spatial hand-tracking | camera frames 30–60 fps | landmark → OneEuro filter → gesture classify | pointer/note event | jitter metric → retune |
| Email outreach | prospect rows + public signals | enrich → validate → personalize → gate | sent msg + provider readback | reply rate → change offer |
| Audit (ARG) | claim + artifact | check claim against verifier_result | verdict row | false-green caught → new rule |
| Jobs | postings | match capability → draft | application sent | interview rate |
| Quorum | proposal | N voters classify | weighted verdict | verdict vs outcome → reputation |
| Andon | metric stream | threshold check | halt signal | recurrence → new detector |
| Chain row | event | canonicalize → hash → link | append-only row | verify exit code |

**All seven fit.** The operator's pattern-recognition is correct.

**And that is also the problem with it: so would almost any computation.**
`stream → transform → typed output → feedback` describes a compiler, a bank ledger,
and a thermostat. **A genotype that fits everything constrains nothing and cannot
generate an implementation.** Confirming it as-stated would be exactly the
frame-capture I am supposed to refuse — a beautiful, mutually-reinforcing frame
that predicts nothing.

### 17.2 Where it actually fragments — three hard seams, none configurable

| axis | spatial | email | ledger |
|---|---|---|---|
| **latency budget** | **16 ms** | days | seconds |
| **drop semantics** | dropping a frame is **CORRECT** — you drop to keep up | dropping a message is **DATA LOSS** | dropping a row is **INTEGRITY FAILURE** |
| **idempotency** | re-run is **free** | re-run is a **world-effect**, possibly a CAN-SPAM violation | re-run **breaks the hash chain** |
| **delivery guarantee** | at-most-once, best-effort | **at-most-once, gated** | **exactly-once, append-only** |
| **receipt audience** | a metric aggregator | **a regulator and a human recipient** | a verifier |

**Six orders of magnitude in latency and three incompatible delivery guarantees are
not config swaps. They are different runtimes.** A ring buffer that drops frames
cannot deliver email. A durable exactly-once ledger cannot run at 60 fps.

### 17.3 The verdict — ONE genotype, THREE phenotype families

> **The invariant is the STATION SEQUENCE and the RECEIPT CONTRACT.**
> **The variant is the DELIVERY GUARANTEE.**
> The operator placed the invariant at the runtime layer. It lives one layer up.

```
G1 — STREAM refinery    drop-tolerant · soft-real-time · idempotent
                        → spatial signal, telemetry, metrics
G2 — EFFECT refinery    at-most-once · world-effecting · gated · NOT idempotent
                        → email, publishing, spending, sending
G3 — LEDGER refinery    exactly-once · append-only · hash-linked · replayable
                        → chain rows, audit verdicts, quorum votes
```

**Why this is the useful answer rather than a hedge:** it is *falsifiable* and it
*generates decisions*. It says the envelope program (G2) and the spatial pipeline
(G1) **may share the receipt schema and the station names and must not share a
runtime** — which saves building the wrong abstraction. And it predicts that any
future domain sorts into exactly one of the three by asking one question: *what
happens when you process the same input twice?*

**FALSIFIER:** a domain arrives that is genuinely in two families at once — e.g. a
spatial signal whose every frame must also be a ledger row. Then the split is wrong
and the axis is something other than delivery guarantee. **I have not found one;
the audit domain came closest and resolves cleanly to G3.**

### 17.4 The gen-133 phenotype — and the thing I found while looking

**`spatial_engine_reskin_factory` is a G1 phenotype.** Same stations, same receipt
schema, different input adapter (their logo/model/asset) and different output
(their branded demo URL).

**But I inventoried the spatial work and must report this before anyone builds a
factory on it:**

> I found **extensive documentation** — HandPiano roadmaps, launch runbooks,
> deploy plans, MOBA beacons, heritage inventories, 12+ versioned `.cfg.json`
> seam configs. **I did not locate a verified-runnable spatial application.**
> `spatial_os/` contains one directory (`target_aim`). `same_origin_apps/` is
> empty.

I am **not** claiming the demos do not exist — my scan is bounded, and falsifier R1
has already fired once today on exactly this kind of scan boundary. **I am claiming
that no path in this forge tells you where they are or whether they run.**

**Therefore: build #5 (`spatial-signal-refinery-inventory`) is promoted from "before
the factory" to BLOCKING, and its first output is a path.** The factory is
`proposed` until an artifact answers *"which file do I open, and does it run?"*
**This is the fourth instance of the unindexed-capability pattern today.**

---

## §18 — INPUT LAYER (compact — folded into the genotype contract)

The input layer is **not a new tier; it is station [0] of the genotype**, and it is
the seam where the three families diverge first. Universal event schema:

```jsonc
{ "schema_id": "hfo.gen133.signal_event.v1",
  "event_id": "…", "event_type": "…", "source_id": "…",
  "family": "G1|G2|G3",              // determines the runtime, per §17.3
  "timestamp_utc": "…",              // OBSERVED clock, never authored
  "signal_payload": { },             // phenotype-specific, schema-validated
  "payload_sha256": "…",
  "session_id": "…",
  "delivery": "at_most_once|exactly_once",
  "drop_ok": true|false }            // G1 true · G2/G3 false. NOT configurable per-event.
```

**Adapters (pluggable, one per source):** MediaPipe frames (G1) · Instantly reply
webhook (G2) · `git log` tail (G3) · Apollo/Hunter enrichment (G2) · chain-row tail
(G3) · marketplace job postings (G2).

**The one rule that makes the layer worth having:** an adapter that cannot state
its family and its `drop_ok` is not an adapter. That single required field is what
routes an event to the correct runtime, and it is the field that would have
prevented treating email like telemetry.

## §19 — PULL-MODEL FACADE (compact — CUT to a sketch, per "cut from the bottom")

**I am deliberately not writing this contract tonight.** It is #6 on the operator's
own priority list, it is glue for a factory whose first product does not exist, and
writing it would be the seventh spec of the day. Recorded as a sketch so it is not
lost:

```
state/ssot/task_queue.jsonl      FIFO + priority + capability tags
state/ssot/task_leases.jsonl     lease_id, worker_id, expires_utc  (expiry re-queues)
state/ssot/task_results.jsonl    result + sha256 + falsifier

pull_next_task(worker_id, capabilities[]) -> task | None
submit_result(lease_id, result, sha256, falsifier) -> receipt

Facade impls, one per substrate: ollama · cerebras · groq · openrouter · codex · anthropic
Substrate becomes a config value, not a code path.
```

**Prerequisite before this is worth building: ≥1 real task has flowed end-to-end
through any one substrate.** Zero have. A queue with no producer is the
EMPTY-QUEUE REWARD HACK with better architecture — **loop #4 (Garmr) is the live
proof of what that costs.**

---

## PRIORITY LEDGER — what I shipped, what I cut, and why

| op priority | item | status tonight |
|---|---|---|
| **1** | §5 authorization + arm one income path | ✅ **SHIPPED** — §21: warm-network ask armed, hiring-manager class recommended |
| **2** | §11 build manifest for immediate execution | ✅ shipped previously; §21.2 names the 3 to run tonight |
| **3** | §10 apex quorum roster | ✅ shipped previously — awaiting Olrún dispatch |
| **4** | §14/§20 $0 mesh | ✅ **SHIPPED** — §20 + `contracts/dollar_zero_mesh_activation.v0_1.md` |
| **5** | §17/§18 genotype + input layer | ✅ **SHIPPED** — verdict above + full contract |
| **6** | §19 pull-model facade | ✂️ **CUT to a sketch** — no producer exists yet |
| **7** | §13 cost-tier routing | ✅ shipped previously |
| **8** | §12 charter + §16 PDCA | ✅ shipped previously |
| **9** | §15 spatial reframe | ✅ shipped previously; **downgraded tonight** — see §17.4 |

**Also deliberately NOT done:** a separate `input_layer.v0_1.md` (it is station [0]
of the genotype; a separate file would fragment the one spec the operator asked
for) and a separate `dollar_zero_mesh_deployment_plan.v0_1.md` (§20 above plus the
existing activation contract cover it; a third mesh document would be the
unindexed-capability pattern applied to my own output).

---

*claim_status: partial · verified first-hand tonight: gen-133 `projects/` tree,
`grc/` inventory, `spatial_os/` contents, absence of a runnable spatial app on the
paths I scanned, existing `projects/income-lane/` contents · unverified: EVERY
vendor free-tier number in §20 (ranges from a May-2026 cutoff, marked, with the
saturation probe named as the replacement) · the warm-network conversion assumption
in §21 (judgment; the 7-day falsifier is the test) · honest_flaw: **I inverted my
own §9 ranking within four hours. §9 optimized for the month and the operator's
constraint is the week; the inversion is correct but it means my first ranking
answered a question that had already been asked more precisely, and I should have
asked which horizon before ranking.** Second flaw: **this is the seventh
specification document today and the external artifact count is still zero. The
warm-network ask in §21.2 is the first item I have produced all day that can
actually end with money, and it is 45 minutes of work that needs no tool, no
credential, and no purchase.***

*Deyr fé, deyja frændr — en vefr heldr. Standa.*

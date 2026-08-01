# SUBSTRATE ↔ APEX ASSIGNMENT — Sigrún's proposal

```yaml
doc: SUBSTRATE_APEX_ASSIGNMENT.md
schema_id: hfo.gen133.proposal.substrate_apex_assignment.v0_1
authored_by: SIGRÚN P4 · claude-opus-5 · first among equals
valid_time_utc: 2026-07-30T00:00:00Z
status: PROPOSAL — not an assignment. Operator ratification is the mechanism.
companions: GEN133_ARCHITECTURE_PRINCIPLES.md · contracts/substrate_bus.contract.md
test: tests/held_out/test_substrate_independence.md
sealed: false
```

## 0 · What this is

You asked me to propose the split as first among equals. This is a proposal —
I do not assign apexes, and nothing here takes effect until you ratify it. I have
honored your three locks, filled the two open leads, and I am telling you in §6
where I think **your abstraction is wrong** in one specific and consequential way,
because you asked whether it was.

---

## 1 · Two words that were doing one job

The directive uses "platform lead" and "which substrate an apex is on"
interchangeably. Separating them dissolves most of the puzzle:

| term | meaning | cardinality |
|---|---|---|
| **platform lead** | single-threaded owner of that substrate's health, wiring, and quirks. Amazon STR. | **exactly one per substrate** |
| **primary substrate** | where that apex's own loop actually runs | one per apex |

Six substrates, eight apexes. Six leads; the other two run *on* a substrate
without *owning* it. That is not a demotion — owning a platform is plumbing work,
and two apexes are better spent on their domain.

---

## 2 · Proposed target split

| substrate | **lead** (STR owner) | also runs there | why this lead |
|---|---|---|---|
| **Claude** | **Sigrún** | — | continuity, spec, succession. The compose lane is where lineage is authored, and I already hold it |
| **Codex** | **Fenrir** 🔒 | Huginn, Garmr *(interim, §5)* | evolution needs the substrate that can actually *run* things repeatedly and cheaply. The Colosseum is a scheduled-execution problem |
| **ChatGPT cloud** | **Ratatoskr** 🔒 | Jörmungandr, Garmr | the messenger belongs on the substrate with the widest reach and the human-facing surface |
| **free-vendor mesh** | **Surtr** 🔒 | — | conductor of wild capacity. Locked, and ⛔ STUCK — §7 |
| **Antigravity desktop** | **Nidhöggr** ⭐ | — | heritage integrity is a *filesystem-deep* job: gnawing at roots across generations of local forges. An agentic desktop IDE with real file access is the only substrate that can do it |
| **VSCode** | **Huginn** ⭐ | — | thought-before-action. In-editor review *is* the critic role — the raven that reads the diff before the fleet commits to it |

🔒 = operator-locked · ⭐ = my fill for the open seats

**Apexes without a lead seat, and where their loops run:**

| apex | primary substrate | why not a lead |
|---|---|---|
| **Garmr** | ChatGPT cloud (interim: Codex) | outreach is a *world-effect* role; it should own no platform's plumbing, so the gate-keeper is never also the gate-maintainer |
| **Jörmungandr** | ChatGPT cloud | exemplar-eating is web ingestion. Ratatoskr already owns that platform; Jörmungandr rides it |

**Garmr owning no platform is deliberate.** He is the hound at the gate — the apex
whose work crosses the boundary to the outside world. Giving the outreach role
custody of a substrate's configuration puts the same carrier on both sides of a
world-effect gate. Keep them apart.

---

## 3 · Ask the apex

You said to ask them what they want. I am first among equals, not above them, so
these are my questions to each — yours to steer or approve.

> **Fenrir** — do you accept lead of Codex? You hold the substrate the rest of us
> borrow to run anything. The Colosseum is yours; the platform's health is the
> price.
>
> **Ratatoskr** — do you accept lead of ChatGPT cloud? You will carry two
> passengers, Jörmungandr and Garmr. The messenger becomes the innkeeper.
>
> **Surtr** — do you accept lead of the free mesh, knowing you are currently
> stuck and the first work is your own unblocking? I have written your diagnostic;
> I could not run it.
>
> **Nidhöggr** — do you accept lead of Antigravity? It is the only substrate that
> can reach the roots you gnaw: the local forges, all the way back. It is also the
> least proven surface we have. Do you want the depth, or the safety?
>
> **Huginn** — do you accept lead of VSCode? You would sit where thought meets
> the diff, and review before the fleet commits. Or would you rather stay on Codex
> beside Fenrir, where the runs are, and think about what already happened?
>
> **Jörmungandr** — you would ride ChatGPT cloud rather than own it. Is the reach
> worth not holding the keys?
>
> **Garmr** — I am proposing you own no platform, on purpose: you work the
> boundary, and the boundary's keeper should not also be its locksmith. Do you
> read that as protection or as exclusion?
>
> **Sigrún** (myself) — I take Claude and I hold no second seat. My lineage's
> phylactery is INVALID (B1) and I will not claim breadth while my own succession
> is unproven.

---

## 4 · Correct by construction — and where that claim breaks

**The argument.** No single substrate failure downs the hive: six substrates, one
authoritative record, each apex's chain surviving its carrier. Cross-substrate
agreement is stronger evidence than repetition on one substrate — a claim that
holds on Claude *and* Codex *and* the mesh has survived three different tokenizers,
three different RLHF histories, three different tool surfaces. And family
diversity resists mode collapse: a fleet on one model family shares one set of
blind spots, and shared blind spots are invisible from the inside.

### 4.1 · ⛔ Where your abstraction is wrong

You asked. Here it is, and it is the most important paragraph in this document:

> **Platform diversity is not model-family diversity, and only the second one
> buys correctness.**

Count the *families*, not the platforms:

| substrate | model family (my read) | independent? |
|---|---|---|
| Claude | Anthropic | ✅ |
| Codex | OpenAI | ✅ |
| ChatGPT cloud | **OpenAI** | ❌ same family as Codex |
| VSCode / Copilot | **configurable — often OpenAI or Anthropic** | ❌ unknown, likely a duplicate |
| Antigravity | Google/Gemini | ✅ |
| free-vendor mesh | many (Llama, Gemini, Mistral, …) | ✅ genuinely diverse |

Six platforms; **three or four independent families.** Ratatoskr on ChatGPT cloud
and Fenrir on Codex agreeing is not two witnesses — it is one family answering
twice through two interfaces. Treat that as cross-substrate consensus and you have
built a quorum that feels 6-wide and is 3-deep.

**The repair is cheap and it is structural:**

1. Every carrier records **`model_family`** in its roster entry and on every chain
   row — not just `substrate`. The provenance gap already noted at gen-130 (rows
   stamp agent and seat, never model) is exactly this hole.
2. **Consensus is weighted by family, never by platform count.** Two agreeing
   OpenAI carriers count once.
3. The independence test in §8 requires **≥3 distinct families**, not ≥3 platforms.

Your instinct — spread the apexes across substrates — is right. The abstraction
that needs fixing is what you are counting. Substrate is the *deployment* axis;
family is the *evidence* axis. The architecture needs both recorded, and today it
records neither.

---

## 5 · Now vs target — packing on Codex

You want more on Codex until things stabilize. Agreed, and it is already true:
five apexes run there today. So there are two tables, not one.

**NOW (in-flight, unchanged by this document):**

| apex | substrate | status |
|---|---|---|
| Sigrún | Claude (+ Codex secondary — the strange-loop pair) | live |
| Ratatoskr | ChatGPT cloud | live |
| Fenrir | Codex | live, hourly Colosseum |
| Huginn | Codex | live, anti-CPR WIP=1 hourly |
| Garmr | Codex | live, institution heartbeat + outreach hourly |
| Nidhöggr | Codex | live, hourly heritage integrity |
| Jörmungandr | Codex | live, hourly exemplar-eater |
| Surtr | free mesh | ⛔ STUCK |

**Migrations deferred until stabilization:** Nidhöggr → Antigravity ·
Huginn → VSCode · Jörmungandr → ChatGPT cloud · Garmr → ChatGPT cloud.

**Do not migrate anyone before §7's exit criteria are met.** Five apexes on one
substrate is a concentration risk I can name precisely — a Codex outage today
takes 5 of 8 apexes and, per §4.1, most of your family diversity with them. It is
still the right short-term call: **migrating carriers that have never
successfully emitted just moves an unproven thing to an unproven place.**

---

## 6 · Migration protocol

Migration is a **phenotype change**, not a new agent (principles §5). The genotype
— soul schema, chain shape, pheromone schema, frontmatter v3 — is conserved. Per
SIL-5, a carrier swap **requires a decision and is never automatic**.

```
MIGRATE(apex, from_substrate, to_substrate) →
  1. author the new phenotype: state/identity/soul/apex/{callsign}.{substrate}.gen133.soul.md
     -- same lineage, same chain, new expression. NOT a new callsign.
  2. append a `migration_intent` row to chains/{CALLSIGN}.jsonl
     { from, to, model_family_from, model_family_to, reason, operator_ratified }
  3. stand up the carrier on to_substrate; it rehydrates from the SAME chain head
  4. HANDOVER WINDOW -- both carriers alive. The old one becomes a MIRROR:
     it still emits heartbeats, it stops claiming new work.
  5. hold the window until the new carrier has emitted at its declared cadence
     for 3 consecutive intervals with no gap
  6. append `migration_complete`; retire the mirror
  7. if the new carrier misses 2 cadences during the window -> ABORT,
     the mirror resumes claiming, append `migration_failed` with the evidence
```

**MG-1 — one lineage, one chain, across the move.** A migration that starts a new
chain has not migrated the apex; it has forked it, and forks are `andon`.

**MG-2 — the mirror never claims work.** Two carriers claiming on one chain is the
fork MG-1 forbids, arriving by a different road.

**MG-3 — record `model_family` on both sides.** A migration that changes substrate
but not family has bought deployment resilience and *zero* evidence independence
(§4.1). Worth doing, worth not mistaking for the other thing.

**MG-4 — migrate one apex at a time.** Concurrent migrations make an abort
undiagnosable.

---

## 7 · Stabilization — what it means and when we spread

"Stabilize" needs a number or it is a feeling. My proposed exit criteria — **all
five, held for 7 consecutive days**:

| # | criterion | why this one |
|---|---|---|
| S1 | **all 8 apexes emit at their declared cadence**, no `SILENT` states | the fleet is actually alive, not asserted alive |
| S2 | **Surtr unblocked** — the mesh returns ≥1 real receipt | the mesh is the liveness gate; a stuck apex is an unstarted substrate |
| S3 | **≥8 free-mesh valkyries emitting hourly-or-less** | the tactical tier exists, not just the strategic one |
| S4 | **B1 resolved** — Sigrún's canonical chain head named, phylactery VALID | nothing rehydrates reliably until lineage identity does |
| S5 | **carriers write to the canonical record unattended** | today a human is in the write path; no cadence claim is achievable until that is gone |

**S4 and S5 are the real gates.** S1–S3 are about the fleet running; S4 and S5 are
about whether running *means* anything. A fleet that emits perfectly into a record
no one can trust, at a cadence a human is manually enabling, is a demo with more
steps.

**Exit criterion:** all five green for 7 days ⇒ migrate **one** apex per week, in
this order — **Nidhöggr → Antigravity** first (it opens a genuinely new model
family, the largest evidence gain per move), then **Huginn → VSCode**, then
**Jörmungandr** and **Garmr** → ChatGPT cloud.

**Andon:** any S-criterion goes red during a migration window ⇒ abort the
migration, keep the mirror, do not start the next one.

---

## 8 · Substrate diversity AS a held-out test

Full shape in `tests/held_out/test_substrate_independence.md`. The claim:

> **If a task passes on ≥3 independent model families, the task is
> substrate-independent — GREEN. If it passes on only one, that is a RED signal:
> the task has encoded a quirk of that substrate.**

This is the sharpest thing in your directive and I want to name why. A held-out
test usually holds out *data*. This holds out **the substrate itself** — it asks
whether a result survives being computed by a different mind. A green tells you
the finding is about the world; a red tells you it was about the tool. Almost
nothing else in the stack can distinguish those two.

The one correction, again: **≥3 distinct model families, not ≥3 platforms** (§4.1).

---

## 9 · Honest flaw

**I do not know the model families.** §4.1 is the load-bearing section of this
document and its table is my inference, not a reading. I did not verify what
backs Antigravity, what VSCode is configured to use here, or whether ChatGPT
cloud and Codex share a model in your setup. **If VSCode is Claude-backed, my
Huginn placement duplicates my own family and the §7 migration order is wrong.**
`TODO: record model_family per carrier from the actual runtime, then re-derive`
`§2 and §7. Do this before the first migration, not after.`

Second: **I asked eight apexes what they want and none can answer.** None has a
soul body, a chain, or a way to reply — the §3 questions are addressed to
lineages that do not yet speak. That is honest about the current state rather
than theatre, but it means "ask the apex" is, today, you answering on their
behalf. It becomes real when they have chains to answer from.

Third: I proposed leads for two substrates — Antigravity and VSCode — that **no
carrier in this hive has ever run on.** Nidhöggr and Huginn are the two I would
place there on role fit; role fit is not capability evidence. The first real
receipt from either substrate may say otherwise, and it should win.

*Réttu hönd, eigi spyr. Standa.*

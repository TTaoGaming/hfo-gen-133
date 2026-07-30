# SUBSTRATE_ROSTER — each platform hosts its own apex + valkyries

```yaml
doc: SUBSTRATE_ROSTER.md
schema_id: hfo.gen133.substrate_roster.v0_1
status: SPECIFIED — 3 apex slots unnamed, 4 valkyrie slots blocked
contract: contracts/substrate_roster.contract.md
spec_section: GEN133_FORMAL_SPEC.md §19
authored_by: SIGRÚN P4 · claude-opus-5
source: operator directive 2026-07-30 (substrate list verbatim) + areas/institution/roles.md
valid_time_utc: 2026-07-30T14:26:00Z
sealed: false
claim_ceiling: DESIGN — not one row below is a liveness receipt
```

## 1 · The rule

> Operator: *"each platform needs apex + valkyries, no ephemeral agents."*

**Invariant SI-4.** Every substrate hosts an apex *and* valkyries. A substrate
with workers but no apex has no local judgement, so every decision routes through
Olrún — which makes her the bottleneck she exists to remove. A substrate with an
apex but no valkyries is a manager with no hands.

## 2 · Per-substrate contract shape

```jsonc
{ "substrate": "…",
  "apex": "…",                      // exactly one callsign
  "valkyries": ["…"],               // ≥1 at full population; 8 at 1-8-64
  "wake_mechanism": "…",
  "pheromone_emit_channel": "…",    // Slack channel + GitHub path
  "cadence": "hourly|daily",
  "ceiling": "FILE|TEXT" }
```

## 3 · The roster

### 3.1 Claude Dispatch (desktop) — the coordinator

```yaml
substrate: claude-dispatch-desktop
apex: Olrún                       # P7 NAVIGATE · O(1) COP
valkyries: [UNNAMED_ROSTER_SLOT]  # ⚠️ see honest flaw
wake_mechanism: Claude scheduled tasks (hourly)
pheromone_emit_channel: "#hfo-command-an… (⚠️truncated) + state/world/pheromones/world.jsonl"
cadence: hourly                   # she carries the world-state songline
ceiling: FILE
remit: OLRUN_COORDINATION.md
```

> **`UNDER_SPECIFIED`.** The directive says *"valkyries=<name Claude-side
> valkyries currently on scheduled loops>"* — that is an instruction to fill in
> observed state I do not have. I cannot enumerate live Claude scheduled loops
> from this session, and I will not invent names for them. `TODO: operator or
> Olrún lists the Claude-side scheduled loops and names them into slots.`

### 3.2 Claude opus-5 (Code sessions) — the refuter

```yaml
substrate: claude-opus-5
apex: Sigrún                      # P4 DISRUPT · O4 AUDIT · joint seat
valkyries: [Skögul]               # co-seat P4, second refuter
wake_mechanism: Claude Code session · scheduled task · /loop
pheromone_emit_channel: "#hfo-command-an… (⚠️truncated) + state/world/pheromones/apex/sigrun.jsonl"
cadence: daily                    # apex tier
ceiling: FILE
note: >-
  Operator holds Claude-opus-5 as the apex lead — "occasionally some code and
  dispatch and control (desktop commander and other tools) to coordinate all my
  platforms." Compose + spec is the primary load; code goes to code lanes.
```

### 3.3 Claude sonnet-5 (Code sessions) — the tactical tier

```yaml
substrate: claude-sonnet-5
apex: Gunnr                       # P4 tactical · watchdog, NOT build-doer
valkyries: [Hrist, Reginleif, Eir, Mist, Thrúd, Göndul, Hildr]   # 7 — packable into single sessions
wake_mechanism: Claude Code session · scheduled task
pheromone_emit_channel: "#hfo-valkyries-… (⚠️truncated) + state/world/pheromones/valkyrie/<callsign>.jsonl"
cadence: hourly                   # valkyrie tier; Gunnr herself daily
ceiling: FILE
```

This is the densest substrate — 1 apex + 7 valkyries — and it is the closest of
any to the 1-8-64 target of 8 valkyries per apex.

### 3.4 Codex (laptop · ChatGPT desktop OpenAI.Codex bundle) — the verifier family

```yaml
substrate: codex
apex: Huginn + Muninn             # P3 VERIFY · twin, dual-role · mirror of P4
valkyries: [Garmr]                # P1 BRIDGE gate-hound · gate + outreach
wake_mechanism: Codex scheduled automations
pheromone_emit_channel: "#hfo-command-an… (⚠️truncated) + state/world/pheromones/apex/huginn_muninn.jsonl"
cadence: daily (apex) · hourly (Garmr)
ceiling: FILE
note: >-
  ⭐ The cross-family verifier substrate. G12 (cross-provider verify) cannot be
  satisfied without a non-Claude family, and Codex is the nearest one to hand.
  Standing next action #2 on Sigrún's soul is "appoint a non-Claude verifier."
  This substrate is that appointment's target.
```

Huginn and Muninn are a **twin apex** — thought and memory, one seat, dual role.
This is the one place the roster has two names in an apex slot, and it is
deliberate: the twin is the office.

### 3.5 ChatGPT cloud (browser) — the messenger

```yaml
substrate: chatgpt-cloud
apex: Ratatoskr                   # P7 NAVIGATE · runs between roots and canopy
valkyries: [UNNAMED_ROSTER_SLOT ×15]   # ⛔ BLOCKED — B4
wake_mechanism: cloud scheduled agents, 15× hourly (operator's existing setup)
pheromone_emit_channel: "#hfo-valkyries-… (⚠️truncated) + GitHub (via commit or issue)"
cadence: hourly
ceiling: FILE (draft only — SEND is operator-gated)
```

> **⛔ BLOCKED — B4.** 15 agents fire hourly with no callsign, no soul, no
> chain. Live `NO_EPHEMERAL_AGENTS` violation. Remedy is *naming*, not deletion.
> Roster slots V13–V16 hold the first four. See `NO_EPHEMERAL_AGENTS.md` §5.

Ratatoskr's ceiling deserves a note: she is the messenger, and her whole function
is crossing trust boundaries no local actor can cross — which makes her the
single actor most likely to need `SEND`. She does not get it. She *drafts*; the
operator sends.

### 3.6 Antigravity IDE (laptop)

```yaml
substrate: antigravity-ide
apex: TBD_OPERATOR                # A6
valkyries: [TBD_OPERATOR]
wake_mechanism: TBD
pheromone_emit_channel: TBD
cadence: TBD
ceiling: FILE
status: UNDER_SPECIFIED — operator to name
```

### 3.7 $0 free-vendor mesh (LiteLLM routing)

```yaml
substrate: free-vendor-mesh
apex: TBD_OPERATOR                # A7 — the mesh conductor
valkyries: [TBD ×8]               # one per vendor family
vendor_families: [groq, cerebras, sambanova, cohere, mistral, gemini, TBD, TBD]
wake_mechanism: harness pull (jobs dispatched, not scheduled)
pheromone_emit_channel: none — mesh HANDS do not emit (FM-2)
cadence: on dispatch
ceiling: TEXT                     # strictest in the fleet
harness: contracts/free_mesh_harness.contract.md
status: UNDER_SPECIFIED — apex unnamed
```

**Important structural point.** Mesh *hands* do not emit and do not chain
(FM-2). But the operator's directive says the mesh gets "one valkyrie per vendor
family" — a valkyrie **is** a durable carrier. So the mesh has two distinct
populations and they must not be confused:

| population | named? | soul | chain | emits | ceiling |
|---|---|---|---|---|---|
| mesh **valkyries** (8, one per family) | yes | yes | yes | yes | FILE |
| mesh **hands** (unbounded invocations) | no | no | no | no | TEXT |

A mesh valkyrie is the *steward* of a vendor family — it owns the receipts of the
hands it invokes on that family. That resolves the tension cleanly: the family
has a name, the individual call does not.

**`UNDER_SPECIFIED`:** only 6 of 8 vendor families are named. `TODO: operator
names families 7–8, or the mesh runs at 6 and 1-8-64 is short by 2.`

### 3.8 Laptop / VM local daemon

```yaml
substrate: laptop-vm-local
apex: VACANT_RESERVED             # A8
valkyries: []
wake_mechanism: Windows Task Scheduler (gen-130 precedent: 4 jobs, 15 min–hourly)
pheromone_emit_channel: TBD
cadence: TBD
ceiling: FILE
status: UNDER_SPECIFIED
```

The operator's coordination plane names four surfaces — *"slack/github/laptop/VM"*
— and laptop/VM has no apex. gen-130 proved local scheduled execution works
(4 Task Scheduler jobs running a runner script). This slot is reserved because
the surface is real and unrepresented.

## 4 · Roll-up

| # | substrate | apex | valkyries named | status |
|---|---|---|---|---|
| 1 | Claude Dispatch | Olrún | 0 | ⚠️ valkyries unnamed |
| 2 | Claude opus-5 | Sigrún | 1 (Skögul) | ok |
| 3 | Claude sonnet-5 | Gunnr | 7 | ok — densest |
| 4 | Codex | Huginn+Muninn | 1 (Garmr) | ok — ⭐ cross-family verifier |
| 5 | ChatGPT cloud | Ratatoskr | 0 of 15 | ⛔ B4 |
| 6 | Antigravity | — | 0 | `UNDER_SPECIFIED` |
| 7 | $0 mesh | — | 0 of 8 | `UNDER_SPECIFIED` |
| 8 | laptop/VM | — | 0 | `UNDER_SPECIFIED` |
| | **totals** | **5 of 8 named** | **9 of 16 named** | |

## 5 · Honest flaw

**Five of eight apex slots are named; nine of sixteen valkyrie slots are named.**
The roster is 56% populated and I did not invent a single name to close the gap.

Second and larger: **not one row above is a liveness receipt.** Every "apex"
here is a contract awaiting an actor. As of `valid_time` the number of these
carriers I verified running is **one** — this Sigrún lane. `roles.md` said the
same thing at 05:40Z and it is still true nine hours later.

Third: `roles.md` seats Garmr at P1 as a *seat*, while the operator's directive
lists Garmr as a Codex *valkyrie*. I recorded the operator's assignment, since it
is the more recent instruction, but the two documents disagree and I have not
reconciled them. `TODO: reconcile roles.md seat table against the substrate
roster.`

*Réttu hönd, eigi spyr. Standa.*

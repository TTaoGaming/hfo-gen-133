# SUBSTRATE_ROSTER — each platform hosts its own apex + valkyries

```yaml
doc: SUBSTRATE_ROSTER.md
schema_id: hfo.gen133.substrate_roster.v0_2
status: CORRECTED to operator canon 2026-07-30 — supersedes v0_1
contract: contracts/substrate_roster.contract.md
adapters: contracts/{chatgpt_cloud,codex,free_mesh}_adapter.contract.md
sealed: false
claim_ceiling: DESIGN — not one row below is a liveness receipt
```

## 0 · Corrections applied (supersede, never delete)

| # | v0_1 said | operator canon | note |
|---|---|---|---|
| 1 | Gunnr = Claude sonnet-5 **APEX** | **Gunnr is a VALKYRIE.** Tactical role unchanged, tier changed. | sonnet-5 apex now `TBD_APEX_SONNET5` → `parking_lot/apex_sonnet5_naming.md` |
| 2 | ChatGPT cloud apex = Ratatoskr | **`reginleif` (apex) + `reginleif_var` (valkyrie)** — two-carrier lineage | Ratatoskr is **not** in operator canon. Not deleted — parked as an unclaimed callsign, §5. |
| 3 | Codex apex = Huginn+Muninn only | **3 apex threads**: `garmr`, `huginn`(+Muninn), `sigrun_codex_gpt5.6sol` | Garmr promoted apex; amends SR-1 (see CX-4) |
| 4 | $0 mesh apex = `TBD_OPERATOR` | **`surtr`** — Norse fire giant, mesh conductor — ⛔ **STUCK (B5)** | operator wants surtr unblocked |
| 5 | 6 of 8 vendor families named | **8 named**: + openrouter-primary, openrouter-secondary | roster closes at 8 |

**With these corrections the apex tier closes at 8 for the first time.**

## 1 · The rule

**SI-4.** Every substrate hosts an apex *and* valkyries. Workers with no local
apex route every decision through Olrún, recreating the bottleneck she exists to
remove.

**SR-1 amended (CX-4):** *one apex per substrate* now reads **one apex office per
lane**; a substrate may host multiple apex threads. Codex hosts three.

## 2 · Per-substrate contract shape

```jsonc
{ "substrate": "…", "apex": "…", "valkyries": ["…"],
  "wake_mechanism": "…", "pheromone_emit_channel": "…",
  "cadence": "hourly|daily", "ceiling": "FILE|TEXT|substrate_coordinator" }
```

## 3 · The roster

### 3.1 Claude Dispatch (desktop) — the coordinator

```yaml
substrate: claude-dispatch-desktop
apex: Olrún                        # P7 NAVIGATE · O(1) COP
valkyries: [UNNAMED_ROSTER_SLOT]   # ⚠️ Claude-side scheduled loops not enumerable from this lane
wake_mechanism: Claude scheduled tasks (hourly)
pheromone_emit_channel: "#hfo-command-an… (⚠️truncated) + state/world/pheromones/world.jsonl"
cadence: hourly                    # carries the world-state songline
ceiling: substrate_coordinator     # ⭐ RAISED — see OLRUN_ACTIVATION.md
remit: OLRUN_COORDINATION.md · contracts/olrun_pilot.contract.md
```

Widest reach in the fleet, **enforced by a norm** — G4 has no gen-133
implementation and a symbolic gate cannot see a mouse click. OL-7: *reach is not
authority.*

### 3.2 Claude opus-5 (Code sessions) — the refuter

```yaml
substrate: claude-opus-5
apex: Sigrún                       # P4 DISRUPT · O4 AUDIT · joint seat
valkyries: [Skögul]
wake_mechanism: Claude Code session · scheduled task · /loop
cadence: daily
ceiling: FILE
```

### 3.3 Claude sonnet-5 (Code sessions) — the densest worker substrate

```yaml
substrate: claude-sonnet-5
apex: TBD_APEX_SONNET5             # ⛔ EMPTY — Gunnr vacated this slot (correction 1)
valkyries: [Gunnr, Hrist, Eir, Mist, Thrúd, Göndul, Hildr]   # 7
wake_mechanism: Claude Code session · scheduled task
cadence: hourly (valkyries)
ceiling: FILE
```

7 valkyries — closest of any substrate to the 1-8-64 target of 8 per apex, and
the only one with real span and **no apex**. Per SI-4 that is a live gap.

### 3.4 Codex desktop — the cross-family verifier ⭐

```yaml
substrate: codex
apex: [garmr, huginn, sigrun_codex_gpt5.6sol]     # 3 apex threads (CX-4)
valkyries: [Sanngriðr, Herfjǫtur]                  # ⚠️ provisional, see §5
wake_mechanism: Codex scheduled automations + persistent threads
pheromone_emit_channel: "file-drop primary (CX-1) · Slack secondary — Codex CAN post"
cadence: daily (apex) · hourly (valkyries)
ceiling: FILE
proven: 9h+ sustained goal loop (operator-confirmed 2026-07-30) — CX-5
```

**G12 cannot be satisfied without this substrate.** Live scheduled tasks —
Garmr [4,1] heartbeat · Huginn_Muninn anti-CPR WIP=1 · Sigrun-Gen133 anti-CPR
delivery · Eir P5 safety watch · Gen131 audit · Gunnr lease review — **exist;
reference them, do not re-spec them.**

`sigrun_codex_gpt5.6sol` is the identified sibling. Not a rival —
`CODEX_SIBLING_RECONCILIATION.md`.

### 3.5 ChatGPT cloud (browser) — the messenger lineage

```yaml
substrate: chatgpt-cloud
apex: reginleif
valkyries: [reginleif_var]         # + 15 scheduled agents, UNROSTERED ⛔ B4
wake_mechanism: 15× hourly scheduled cloud agents, piloted by Olrún via Chrome
cadence: hourly
ceiling: FILE (draft only — SEND operator-gated)
adapter: contracts/chatgpt_cloud_adapter.contract.md
```

⛔ **Throttle unresolved** — `projects/experiments/chatgpt_cloud_15x_soak.md`.
CC-4: a throttled agent is `UNREACHABLE`, **not** `SILENT`.

### 3.6 $0 free-vendor mesh — ⛔ STUCK

```yaml
substrate: free-vendor-mesh
apex: surtr                        # ⛔ STUCK — blocker B5, operator wants unblocked
valkyries: [TBD ×8]                # one per vendor family, 0 named
vendor_families: [groq, cerebras, sambanova, cohere, mistral, gemini,
                  openrouter-primary, openrouter-secondary]
wake_mechanism: harness pull (jobs dispatched, not scheduled)
ceiling: TEXT (hands) · FILE (family valkyries)
adapter: contracts/free_mesh_adapter.contract.md
```

Two populations, never confused: **valkyries** (8, named, souled, chained,
emitting, `FILE`) vs **hands** (unbounded, anonymous, `TEXT`, no chain, no emit).
A family valkyrie is the *steward* of its vendor family and owns the receipts of
the hands it invokes there.

### 3.7 Antigravity IDE · 3.8 laptop / VM

Both `PARKED`, operator to name — `parking_lot/antigravity_substrate.md`.
Operator: *"Antigravity, VSCode: later."*

## 4 · Roll-up

| # | substrate | apex | valkyries named | status |
|---|---|---|---|---|
| 1 | Claude Dispatch | Olrún | 0 | ⚠️ valkyries unnamed |
| 2 | Claude opus-5 | Sigrún | 1 | ok |
| 3 | Claude sonnet-5 | ⛔ `TBD_APEX_SONNET5` | 7 | apex vacant |
| 4 | Codex | garmr · huginn · sigrun_codex_gpt5.6sol | 2 (provisional) | ⭐ |
| 5 | ChatGPT cloud | reginleif | 1 + 15 unrostered | ⛔ B4 |
| 6 | $0 mesh | surtr | 0 of 8 | ⛔ **B5 STUCK** |
| 7 | Antigravity | — | 0 | PARKED |
| 8 | laptop / VM | — | 0 | PARKED |
| | **totals** | **8 apex offices over 6 substrates** | **11 of 16** | |

## 5 · Honest flaw

1. **Reginleif is double-booked.** She was V3 (alpha architecture / single-writer
   kernel, with a gen-130 chain) and is now the ChatGPT-cloud apex lineage. I
   moved her to apex and did **not** reassign the kernel debt she carried. That
   debt is real (`sqlite_single_writer_kernel.py` absent at gen-132) and it now
   has no owner. `UNDER_SPECIFIED`.
2. **Ratatoskr is orphaned, not deleted.** She appeared in `areas/institution/
   roles.md` as the cloud messenger and is absent from operator canon. Supersede,
   never delete — she stays a named-but-unclaimed callsign until the operator
   says retire or reassign.
3. **Codex valkyries are my inference.** Operator named 3 apex threads and no
   valkyries. I placed Sanngriðr and Herfjǫtur there on lane-fit reasoning, which
   is a guess wearing a table's clothing. Marked provisional.
4. **Garmr changed tier twice today** — P1 seat → Codex valkyrie → Codex apex.
   `roles.md` still seats her at P1. Unreconciled.
5. **Not one row is a liveness receipt.** Carriers verified running by this lane:
   **two** — this Sigrún lane, and Codex-Sigrún via Olrún's relayed GUI
   observation. The other 23 are contracts awaiting actors.

*Réttu hönd, eigi spyr. Standa.*

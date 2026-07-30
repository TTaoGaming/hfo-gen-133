# CONTRACT — ChatGPT cloud adapter

```yaml
contract: chatgpt_cloud_adapter
schema_id: hfo.gen133.contract.chatgpt_cloud_adapter.v0_1
spec: GEN133_FORMAL_SPEC.md §11, §19
status: SPECIFIED — build target for the parallel sonnet-5 builder lane
driver: Olrún-Dispatch piloting Chrome (substrate_coordinator ceiling)
sealed: false
```

## Substrate

| field | value |
|---|---|
| substrate | `chatgpt-cloud` (browser) |
| apex | `reginleif` |
| valkyrie | `reginleif_var` |
| wake | 15× hourly scheduled cloud agents (operator's existing setup) |
| ceiling | `FILE` — draft only; SEND stays operator-gated |
| driver | Chrome MCP / Claude-in-Chrome, piloted by Olrún |

**No shell.** This substrate cannot compute a digest without trusting its own
in-context arithmetic — which is the self-report SL-2 refuses. Every digest it
returns is `attested_by_relay`, never `computed`.

## Operations

### `WAKE(callsign, capsule)`

```
pre:   callsign ∈ roster ∧ a prebuilt capsule exists at a raw GitHub URL
       ∧ the cloud thread for callsign is reachable ∧ NOT throttled
do:    Olrún pilots Chrome → opens the scheduled agent thread
       → posts capsule URL + digest + one bounded objective
post:  a `dispatch` pheromone recorded with the thread id and ts_utc
```

### `DROP_PHEROMONE(p)`

Cloud agents cannot commit to GitHub directly. Two legal paths:

| path | mechanism | authority |
|---|---|---|
| A (preferred) | agent emits structured text in-thread → Olrún transcribes to `state/world/pheromones/valkyrie/<callsign>.jsonl` | Olrún signs the transcription and owns the receipt |
| B | agent posts to Slack via `@ChatGPT` bot → Codex relay mirrors into GitHub | Codex relay owns the receipt |

**Invariant CC-1 (transcription is attributed).** A transcribed pheromone carries
`transcribed_by: olrun` and `origin_thread_id`. A relayed trace that hides its
relay is indistinguishable from a forged one.

### `READ_ACK(dispatch_hash)`

```
pre:   a `dispatch` pheromone exists with that hash
do:    Olrún reads the thread; extracts the ack referencing dispatch_hash
post:  ack recorded; SLO = ≤15 min (spec §11)
fail:  no ack in 15 min ⇒ feeds the silence ladder, NOT a retry storm (BUS-2)
```

## Invariants

| # | invariant |
|---|---|
| CC-1 | transcription is attributed (`transcribed_by`, `origin_thread_id`) |
| CC-2 | **digests are `attested_by_relay`, never `computed`** on this substrate |
| CC-3 | the 15 agents must be **rostered** before they count as carriers — until then they are hands under `reginleif`, who owns their receipts (⛔ B4) |
| CC-4 | **throttle ≠ silence.** A throttled agent is `UNREACHABLE`, not `SILENT`. Conflating them is the likeliest false positive in the whole monitoring design. |
| CC-5 | ceiling `FILE`/draft — the messenger drafts, the operator sends |

## ⛔ Known live problem — the throttle

The 15× hourly cadence trips ChatGPT cloud's "too many messages" throttle; cause
unknown (schedule collision · per-hour rate · per-day rate · per-account rate ·
something else). Soak experiment: `projects/experiments/chatgpt_cloud_15x_soak.md`.

**Do not build the adapter's cadence assumptions until the soak returns a rate
shape.** `L_BUDGET_WITHOUT_RECEIPT`: probe first, validate, then scale.

## Honest flaw

Every mechanism here routes through a human-piloted browser. That is a real
dependency on Olrún's availability and on Chrome automation continuing to work
against a UI nobody controls. It is the least durable adapter of the three, and
its ack path is a transcription rather than a machine write.

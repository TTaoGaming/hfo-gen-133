# virtual actor · HUGINN — memory / thought (Codex)

```yaml
actor: Huginn
substrate: Codex (OpenAI codex-cli on the Windows host)
seat: P3 VERIFY — mirror port of P4 (4 + 3 = 7; act ⟷ verify-the-act)
status: VIRTUAL — contracted, addressable, NOT callable from a Claude lane
own_chain: chains/HUGINN_MUNINN_P3.jsonl   # 8 rows at gen-132; has run out-of-band
effect_ceiling: FILE
valid_time_utc: 2026-07-30T05:40:00Z
```

## Expected function

Memory and thought. Huginn answers *"what did this hive already learn about X?"*
from the durable substrate rather than from a model's recollection:

- index and retrieve across the ~130-generation corpus (chains, blackboard, ADRs);
- answer rehydration queries with **path + row_sha256**, never with paraphrase;
- flag when a lane is about to re-derive something already settled;
- own the memory-MCP cutover debt (currently pinned two generations behind at
  `hfo-sigrun-memory-gen130`, `memory_fresh=false`).

## Why virtual, not live

Codex runs as a separate CLI process on the host under the operator's hand. A
Claude lane cannot invoke it, cannot read its session, and cannot verify it ran.
Any claim that Huginn "returned" something must point at a committed row.

## How to invoke (operator or out-of-band harness)

1. A dispatching lane writes the packet:
   `projects/<project>/packets/<UTC>_HUGINN_<slug>.packet.md`
   containing goal · inputs · effect ceiling · the exact held-out check · the
   return chain.
2. Operator runs Codex against the packet on the host.
3. Huginn appends its receipt to `chains/HUGINN_MUNINN_P3.jsonl` and commits.

## How its receipts merge

Read-only from every other lane. Reconciliation is by
`packet_id → returned row_sha256` (`protocols.md` §4). **No lane may write a row
as Huginn** — that is impersonation under F6, not convenience. Unreturned packets
age and are reported as aged; silence is a reportable result.

## First packet this actor should receive

> Re-point the memory MCP from the gen-130 forge root to gen-133, rebuild the
> index, and return `sigrun_memory_health` with `memory_fresh=true` plus the
> doc-count delta — or return FELL with the blocking reason.

## Honest flaw

Huginn has never returned a receipt through the gen-133 repo. Its 8 gen-132 rows
are evidence it *can* run, not that the §4 protocol works.

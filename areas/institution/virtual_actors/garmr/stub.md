# virtual actor · GARMR — guard / gate-hound (Codex)

```yaml
actor: Garmr
substrate: Codex (OpenAI codex-cli on the Windows host)
seat: P1 BRIDGE (guard posture)
status: VIRTUAL — contracted, addressable, NOT callable from a Claude lane
own_chain: chains/GARMR_P1.jsonl   # 1 row at gen-132 — GENESIS ONLY, never worked
effect_ceiling: FILE + gate verdict (its real output is DENY)
valid_time_utc: 2026-07-30T05:40:00Z
```

## Expected function

Garmr is the **deterministic, non-neural gate at the seam of irreversibility.**
Its job is to be un-persuadable:

- refuse a green `claim_status` that carries no `verifier_result`;
- refuse `send` · `spend` · `publish` · `seal` · `push` · `delete` without an
  operator-typed authorization present as data, not as prose;
- verify chain integrity (prev-link + row-hash) before any append is accepted;
- hold the door on the permaweb upload — Arweave has no takedown.

Garmr exists because the reflex cannot be cured. A fired reflex must be unable to
reach the consequence. Removing the consequence is the design; suppressing the
firing is not.

## Why it must NOT be a Claude lane

A gate implemented by the same substrate it gates shares the blind spot. If the
proposer and the disposer are the same model family, a persuasive frame passes
both. Garmr on Codex is a different failure surface — that difference *is* the
security property.

## Why virtual, not live

Codex is a separate host process under the operator's hand; a Claude lane cannot
invoke it. Worse: **at gen-133 there is no gate for Garmr to run.** No
`bb_append.py`, no OPA bundle, no PreToolUse enforcement. Garmr is unarmed here.

## How to invoke

1. Packet at `projects/<project>/packets/<UTC>_GARMR_<slug>.packet.md`.
2. Operator runs Codex against it.
3. Garmr appends to `chains/GARMR_P1.jsonl` and commits.

## How its receipts merge

Read-only from all other lanes. A DENY row is **not** a failure of the hive — it
is the institution working. Do not "fix" a deny by routing around it.

## First packet this actor should receive

> Port the gen-130/131 no-fake-green write seam into gen-133 as the sole chain
> append path, red-first: prove a green-without-receipt row is REFUSED (exit≠0)
> *before* proving a well-formed row is accepted (exit 0). Return both exit codes.

## Honest flaw

Genesis row only. Garmr has never gated anything. Every gate claim about gen-133
is therefore **convention held by one carrier's discipline** — the exact
arrangement the RBR doctrine says not to trust.

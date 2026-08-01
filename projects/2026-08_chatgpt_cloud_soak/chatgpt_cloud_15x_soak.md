# EXPERIMENT — ChatGPT cloud 15× hourly soak

```yaml
experiment_id: chatgpt_cloud_15x_soak
schema_id: hfo.gen133.experiment.v1
status: REGISTERED — pre-registered before the run (EV-3)
pilot: Olrún-Dispatch (substrate_coordinator, Chrome)
registered_utc: 2026-07-30T15:30:00Z
result: null
verdict: null
sealed: false
```

## Hypothesis — written before the run

> The 15× hourly cadence trips ChatGPT cloud's "too many messages" throttle.

**Cause is unknown.** Candidate shapes, none favoured:

| # | candidate | discriminator |
|---|---|---|
| 1 | schedule collision (all 15 fire on the same minute) | stagger them; does the throttle move? |
| 2 | per-hour message rate | throttle correlates with msgs/hour regardless of agent count |
| 3 | per-day message rate | throttle appears late in the day and persists |
| 4 | per-account concurrency | throttle correlates with simultaneous open threads |
| 5 | something else | none of the above correlate |

Registering the candidates in advance is the point: a result interpreted after
the fact is a story (EV-3).

## Method

1. Olrún pilots Chrome and re-enables the paused 15× hourly agents.
2. Observe over a soak window.
3. Record per agent: fire time, ack latency, throttle timestamp, error text.
4. Append one row per throttle event to `state/ssot/chatgpt_cloud_soak.jsonl`.

```jsonc
{ "ts_utc": "…", "agent_thread_id": "…", "event": "fire|ack|throttle",
  "ack_latency_s": 0, "concurrent_open_threads": 0,
  "msgs_this_hour": 0, "msgs_today": 0, "error_text": "…" }
```

Fields 6–8 are the discriminators. Logging only the throttle timestamp would
tell us *that* it happened and nothing about *which* candidate is right.

## Success criterion

**Identify the exact rate-limit shape** — msgs/hour, msgs/day, concurrent
threads, or other. Not "it throttles sometimes."

## Fallback

If 15× hourly is unsafe, drop to N× hourly where N is the **measured** maximum
stable rate. Not a guessed N.

## Why this experiment matters beyond the throttle

`contracts/chatgpt_cloud_adapter.contract.md` cannot have honest cadence
assumptions until this returns, and **CC-4 depends on it**: a throttled agent
must be classified `UNREACHABLE`, never `SILENT`. Without the rate shape, the
silence detector will report 15 dead carriers the first time the throttle fires —
the likeliest false positive in the entire monitoring design.

## Honest flaw

This is the **first pre-registered experiment in the fleet's history**, which
means the registry it belongs to does not exist yet
(`parking_lot/experiment_registry.md`). It also measures an *internal* property —
throttle behaviour is not fitness (EV-1). It is worth running anyway because it
unblocks an adapter, but it must not be counted as evidence that the fleet is
producing external value. `cap-0018` is still FAILED at $0.

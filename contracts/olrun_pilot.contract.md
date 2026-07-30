# CONTRACT — Olrún pilot ceiling (`substrate_coordinator`)

```yaml
contract: olrun_pilot
schema_id: hfo.gen133.contract.olrun_pilot.v0_1
spec: OLRUN_ACTIVATION.md · GEN133_FORMAL_SPEC.md §16
status: SPECIFIED — NOT ENFORCED (G4 absent at gen-133)
sealed: false
```

## Ceiling definition

```
substrate_coordinator := FILE
                       ∪ { pilot_browser, control_desktop_app, install_tool,
                           wake_remote_carrier, transcribe_pheromone }
                       ∖ { SEND, SPEND, PUBLISH, PUSH, SEAL, IMMUNIZE, DELETE }
```

The subtracted set is **absolute and non-vesting** (CAN-2 / NS-5).

## Preconditions — `PILOT(action, substrate)`

| # | precondition |
|---|---|
| P1 | `action` ∈ the ceiling's added set |
| P2 | `action` ∉ the forbidden set, **evaluated on the effect, not on the gesture** |
| P3 | the target carrier is rostered (waking an unrostered agent violates G5) |
| P4 | a `dispatch` pheromone is emitted before the pilot action, not after |

P2 is the subtle one: *"click this button"* is a gesture; *what the button does*
is the effect. Ceiling is evaluated on the effect. A click that sends is a
`SEND`.

## Postconditions

| # | postcondition |
|---|---|
| Q1 | every pilot action is recorded with `origin`, `target_substrate`, `ts_utc` |
| Q2 | every transcribed pheromone carries `transcribed_by: olrun` + `origin_thread_id` |
| Q3 | no irreversible effect occurred |
| Q4 | on reaching an irreversible step: **halt, park the UI there, page the operator** |

## Invariants

| # | invariant |
|---|---|
| OL-7 | **reach is not authority.** She can click Send; she may not. |
| OL-1 | dispatch, never build — piloting another substrate to do work is dispatch; doing the work herself in a piloted IDE is **building**, and forbidden |
| OL-3 | Olrún is subject to silence-as-signal like any carrier |
| OLP-1 | **piloted actions are logged as her own rows**, never attributed to the piloted carrier (R6 — writing another actor's row is impersonation) |
| OLP-2 | **install_tool is bounded to the reversible envelope.** Installing is allowed; a tool that grants a forbidden effect is not thereby granted it. |
| OLP-3 | **a GUI is unlogged by default.** Every pilot action must be explicitly recorded, because nothing else will record it. |

## ⛔ Enforcement gap — state it plainly

**No gate enforces this contract.** G4 (effect-ceiling) has no gen-133
implementation, and even if it did, **a symbolic gate cannot see a mouse click.**
Tool-call gating works because tool calls are structured; GUI piloting is not.

So `substrate_coordinator` is currently the widest reach in the fleet, enforced
by a norm. That is an honest description of the risk, not an argument against the
raise — the operator directed it and the reach is genuinely needed. But
OLP-3 is the mitigation that must actually be built: **if the pilot does not log
itself, the action did not happen as far as the institution is concerned, and an
unlogged coordinator is exactly the unattributable state `NO_EPHEMERAL_AGENTS`
exists to prevent.**

## Honest flaw

The strongest control here is Olrún's own compliance, which is the control this
whole architecture was built on the premise of not trusting (RBR: the reflex
fires before the deliberate pass). I can specify OL-7; I cannot enforce it, and
neither can anything currently in this repo.

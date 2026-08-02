---
schema_id: hfo.gen133.s09.adversarial_bayesian_vote.v1
vote_id: S09_2048_DIRECTIONAL_BINDING_ABSTRACTION_GATE_20260802T023323Z
status: REVISE
callsign_or_seat: S09_STRATEGIC_REASONING_AND_VOTING_CELL
carrier_task_id_expected: 6a539fb148bc8191a30b6009dbf22438
carrier_task_id_observed: 6a539fb148bc8191a30b6009dbf22438
carrier_task_id_match: true
carrier_identity_claim: ONE_PASS_SCHEDULED_TASK_CARRIER_NOT_LINEAGE
controller: operator_direct
wip: 1
valid_time_utc: 2026-08-02T02:33:23Z
transaction_time_utc: SEE_GITHUB_COMMIT_METADATA
canonical_repository: TTaoGaming/hfo-gen-133
canonical_branch: agent/gen133-bootstrap-20260730
decision_packet_id: S08_2048_POINTER_ADAPTER_COMPATIBILITY_20260802T023000Z
decision_packet_commit: 10f2da828a37b7ebe0d8f6df9bc7c0ae4f56fa62
decision_packet_blob: 4067a63ca7cd911f7c86562cfaf6bb474319d84d
decision_deadline_utc: 2026-08-03T02:30:00Z
effect_ceiling: ADVISORY_VOTE_AND_SANITIZED_SLACK_POINTER_ONLY
verifier: S04_STRUCTURAL_PREFLIGHT_THEN_DISTINCT_BROWSER_CAPABLE_NONPRODUCER
consumer:
  - NEXT_EXACT_SPATIAL_FACTORY_GOLDEN_APP_WORKITEM
  - S06_CODE_WORK_PACKET_COMPILER
  - S07_BROWSER_OR_VM_EXECUTOR
  - SPATIAL_APP_FACTORY_BACKLOG_OWNER
binding_weight: 0
same_provider_advisory: true
fitness_credit: 0_PENDING_DISTINCT_CONSUMPTION_AND_EXECUTION
sealed: false
---

# S09 adversarial Bayesian vote — 2048 directional binding abstraction gate

## Self-probe

```yaml
expected_task_id: 6a539fb148bc8191a30b6009dbf22438
observed_task_id: 6a539fb148bc8191a30b6009dbf22438
task_id_match: true
tools_observed:
  github: authenticated_exact_commit_file_read_and_branch_scoped_immutable_create
  slack: authenticated_public_channel_read_write
  browser_runtime: unavailable
  shell_runtime: unavailable
  task_mutation: not_called
identity_ceiling: disposable_one_pass_carrier
```

## Exact decision

Choose the smallest honest first binding for frozen `gabrielecirulli/2048@478b6ec346e3787f589e4af751378d06ded4cbbc` and `TTaoGaming/TAGS@e0e3125e1ef6bb33e189c91b485ec341f2d3cd52`:

- **A — direct current pointer stream, no app revision**
- **B — app-local injected InputManager directional bridge, with no reusable TAGS API expansion yet**
- **C — immediately add a reusable normalized directional/action callback to TAGS, then bind 2048**
- **D — synthesize keyboard events consumed through legacy `event.which`**
- **E — retire 2048 as a golden-app candidate**

Decision deadline: `2026-08-03T02:30:00Z`, or before the first consuming golden-app WorkItem is compiled, whichever comes first.

## Source bindings

1. S08 changed decision packet: commit `10f2da828a37b7ebe0d8f6df9bc7c0ae4f56fa62`, blob `4067a63ca7cd911f7c86562cfaf6bb474319d84d`.
2. TAGS pointer adapter: repository commit `e0e3125e1ef6bb33e189c91b485ec341f2d3cd52`, blob `579c9551225f0974ed93564b6ad8bfb1abf72cf3`, path `prototypes/spatial-input-adapter.js`.
3. 2048 input manager: repository commit `478b6ec346e3787f589e4af751378d06ded4cbbc`, blob `ca01b3ce8995a5a20ac50219712d1ef95297ed99`, path `js/keyboard_input_manager.js`.
4. 2048 game manager: same repository commit, blob `1c13d15bd667afe06f95316942324885c45d8e6d`, path `js/game_manager.js`.
5. 2048 bootstrap: same repository commit, blob `2c1108e757a0e49af7b9ee48dcc45bd8e61cb806`, path `js/application.js`.

## Vote

**REVISE — accept S08's incompatibility finding, but gate abstraction. Choose B for the first canary. Do not expand the reusable TAGS ABI until a second independent app demonstrates the same directional contract.**

The current adapter emits pointer lifecycle events and an activation target callback. The frozen 2048 input manager converts keyboard or touch-swipe evidence into semantic `move` values `0..3`; its game manager already subscribes at that semantic seam. The narrowest reversible experiment is therefore an app-local injected InputManager wrapper or bootstrap-local binding that validates one direction and invokes the existing input-manager move emission. It should leave `game_manager.js`, native keyboard/touch behavior, and the reusable TAGS pointer API unchanged.

This is not approval to implement, merge, deploy, publish, or claim compatibility. It is a nonbinding routing recommendation for a later exact WorkItem.

## Prior

Before inspecting the frozen interfaces:

| Option | Prior |
|---|---:|
| A — direct pointer stream | 0.18 |
| B — app-local semantic bridge | 0.34 |
| C — reusable directional ABI now | 0.25 |
| D — synthetic keyboard | 0.13 |
| E — retire candidate | 0.10 |

## Evidence for and against each option

### A — direct pointer stream

**For:** zero app code; strongest universal-adapter story; quickest result if hidden browser behavior translates the events.

**Against:** the frozen modern-browser path declares keyboard and legacy touch listeners, not standard pointer listeners. The TAGS activation callback returns a released target, not a direction. No inspected seam maps the current pointer descriptors to `move(0..3)`.

### B — app-local injected InputManager bridge

**For:** directly reuses the existing semantic boundary; can preserve the game core and native inputs; keeps the first experiment small and reversible; avoids declaring a reusable ABI from one app.

**Against:** creates app-specific glue and may be discarded if many apps require an identical direction contract. A careless bridge could duplicate moves or couple gesture recognition to application code.

### C — reusable directional/action callback now

**For:** better long-run app-factory leverage if directional games are a repeated class; can separate gesture recognition from app mapping; reduces future per-app glue.

**Against:** one candidate is weak evidence for a durable ABI. Naming, repeat policy, cancellation semantics, confidence thresholds, coordinate frames, and diagonal handling are not yet stabilized. Premature generalization could harden the wrong abstraction and expand regression surface in the already-tested pointer adapter.

### D — synthetic keyboard

**For:** minimal visible app change if it works; preserves the application's current keyboard path.

**Against:** this frozen app keys on obsolete numeric `event.which`. Standards-shaped `KeyboardEvent` construction does not guarantee that legacy field. Any workaround risks browser-specific or undocumented property behavior and needs exact real-browser proof.

### E — retire 2048

**For:** avoids one-off integration and protects WIP if directional control is outside the present pointer-adapter thesis.

**Against:** the app exposes a narrow semantic seam and is small enough to test the factory's ability to support a second input class. Retirement now would discard a useful falsification candidate before the bounded bridge is attempted.

## Posterior

| Option | Posterior |
|---|---:|
| A — direct pointer stream | 0.02 |
| B — app-local semantic bridge | 0.58 |
| C — reusable directional ABI now | 0.22 |
| D — synthetic keyboard | 0.05 |
| E — retire candidate | 0.13 |

These are decision weights, not measured frequencies.

## Correlated-evidence risk

S08 and S09 are both ChatGPT-carried interpretations of the same frozen source. Agreement is correlated same-provider evidence, not quorum and not independent verification. Primary code blobs reduce transcription risk but do not supply runtime behavior. Binding weight remains `0` until a distinct consumer accepts the packet and a browser-capable nonproducer executes the exact bytes.

No majority is asserted. The S08 card and this vote agree on direct incompatibility but differ in emphasis: S08 permits either an app seam or reusable callback; S09 prefers the app-local seam first and defers reusable ABI promotion.

## Strongest dissent

The strongest dissent is that app-factory value comes from reusable adapters, not one-off glue. A normalized `direction` or `action` callback is already an obvious second output family, so delaying it may create throwaway code and duplicate testing.

That dissent is credible. The answer is not to forbid a directional ABI; it is to require a second independent consumer or a concrete backlog cluster before promoting the first app binding into the reusable TAGS surface.

## Opportunity cost

- Choosing B may spend roughly one bounded implementation/test cycle on glue that is later generalized.
- Choosing C now risks a larger shared-API redesign, broader regression burden, and more speculative tests before any consumer proves demand.
- Choosing A or D risks burning browser-verification time on interfaces the source does not support cleanly.
- Choosing E loses a compact negative-control app that can test whether the factory handles semantic rather than pointer-native inputs.

## Operator-minute burden

```yaml
operator_minutes_required_now: 0
operator_minutes_expected_for_internal_canary: 0_to_5
implementation_minutes_estimate: 20_to_60
deterministic_test_minutes_estimate: 20_to_45
browser_smoke_minutes_estimate: 15_to_30
estimate_status: HEURISTIC_NOT_FITNESS_CREDIT
```

## Reversible next experiment

A later producer WorkItem may create one temporary branch that:

1. Adds an app-local InputManager wrapper or bootstrap-local binding accepting only integer directions `0..3`.
2. Routes one independently accepted spatial direction to exactly one existing `move` emission.
3. Leaves `js/game_manager.js` unchanged.
4. Leaves the reusable TAGS pointer-adapter public API unchanged.
5. Proves ambiguous, cancelled, low-confidence, and held gestures emit zero moves.
6. Proves native arrow/WASD/Vim and native touch swipe still work.
7. Records exact app commit, adapter commit, browser/version, commands, deterministic output, and visual/state evidence.

Promotion gate: only after a second independent app needs materially the same direction contract should a new reusable directional ABI be proposed. That proposal must define direction vocabulary, cancellation, repeat, diagonal resolution, confidence, and host-callback ownership explicitly.

## Falsifiers

Change preference from B to A only if a distinct browser-capable verifier proves the unmodified frozen pointer adapter causes exactly one correct 2048 move per accepted gesture with zero app-specific mapping and no native-input regression.

Change preference from B to C if a second independent frozen application or an already-approved backlog cluster requires the same semantic direction contract with no material divergence in cancellation, repeat, or diagonal policy.

Change preference from B to E if the smallest bridge requires game-state modification, cannot preserve keyboard/touch fallback, cannot prevent duplicate moves, or exceeds the bounded implementation and test timebox.

Change preference from B to D only if exact browser evidence proves standards-compliant event construction supplies the numeric value consumed by this app's `event.which` without undocumented mutation.

## Authority and consumption

- **Effect ceiling:** this file and one sanitized Slack pointer only.
- **Structural verifier:** S04 may verify path, source SHA/blob bindings, authority, expiry, and internal consistency; S04 cannot make the vote binding.
- **Distinct verifier:** browser-capable nonproducer on a different authorized substrate.
- **Consumer:** next exact Spatial Factory golden-app WorkItem, S06 compiler, S07 executor, or backlog owner must explicitly accept, revise, or reject this vote.
- **Binding weight:** `0`, same-provider advisory evidence.
- **No authorization:** no producer work, task mutation, send, spend, deployment, merge, publication, account/security change, deletion, or policy decision.

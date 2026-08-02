---
schema_id: hfo.gen133.s08.research_evidence_card.v1
card_id: S08_2048_POINTER_ADAPTER_COMPATIBILITY_20260802T023000Z
result: REVISE
callsign_or_seat: S08_RESEARCH_CANDIDATE_SCOUT
carrier_task_id_expected: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_observed: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_match: true
carrier_identity_claim: DISPOSABLE_SCHEDULED_CARRIER_NOT_LINEAGE
controller: operator_direct
wip: 1
valid_time_utc: 2026-08-02T02:30:00Z
transaction_time_utc: SEE_GITHUB_COMMIT_METADATA
canonical_repository: TTaoGaming/hfo-gen-133
canonical_branch: agent/gen133-bootstrap-20260730
repository_head_observed_before_write: 9520176164b912a1206c6f9f8d3a4d8663ef731f
research_lane: interaction_input_adapters
question_change_basis: PRIOR_WAKE_ADMITTED_EXACT_2048_CANDIDATE_CREATING_A_NEW_CONCRETE_ADAPTER_COMPATIBILITY_QUESTION
bounded_uncertainty: WHETHER_TAGS_E0E3125_POINTER_ADAPTER_DIRECTLY_DRIVES_2048_478B6EC_WITHOUT_A_BINDING_REVISION
candidate_app_repository: gabrielecirulli/2048
candidate_app_commit: 478b6ec346e3787f589e4af751378d06ded4cbbc
candidate_adapter_repository: TTaoGaming/TAGS
candidate_adapter_commit: e0e3125e1ef6bb33e189c91b485ec341f2d3cd52
privacy_class: PUBLIC_PRIMARY_REPOSITORY_AND_STANDARDS_SOURCES_ONLY
effect_ceiling: RESEARCH_CARD_AND_SANITIZED_SLACK_POINTER_ONLY
verifier: S04_STRUCTURAL_PREFLIGHT_THEN_DISTINCT_BROWSER_CAPABLE_NONPRODUCER
consumer:
  - NEXT_EXACT_SPATIAL_FACTORY_GOLDEN_APP_WORKITEM
  - S06_CODE_WORK_PACKET_COMPILER
  - S07_BROWSER_OR_VM_EXECUTOR
  - SPATIAL_APP_FACTORY_BACKLOG_OWNER
fitness_credit: 0_PENDING_EXACT_WORKITEM_CONSUMPTION
expiry_utc: 2026-08-09T02:30:00Z
sealed: false
---

# S08 evidence card — 2048 is not plug-compatible with the current pointer adapter

## Changed bounded question

The prior wake admitted exact upstream `gabrielecirulli/2048@478b6ec346e3787f589e4af751378d06ded4cbbc` as an internal branch/test candidate. That admission creates one new interaction-lane uncertainty:

> Can the existing `TTaoGaming/TAGS@e0e3125e1ef6bb33e189c91b485ec341f2d3cd52` spatial pointer adapter drive 2048 moves directly, without an app-specific semantic binding or input-manager revision?

## Decision — `REVISE`

Do not claim direct compatibility.

The exact TAGS adapter emits synthetic `pointermove`, `pointerdown`, `pointerup`, and `pointercancel` events and can call an activation callback after a successful release. The exact 2048 input manager does not consume that pointer stream in the normal modern-browser path. It listens for document `keydown` events keyed by legacy numeric `event.which`, or for a three-event legacy touch swipe sequence. Its game core receives movement only after the input manager emits semantic `move` values `0..3`.

Therefore a consuming WorkItem needs a **small explicit semantic binding**. Preferred boundary: preserve native keyboard/touch handlers and add an injected spatial-direction callback or adapter-specific `InputManager` bridge that calls the existing `emit("move", direction)` seam. Do not route through the game-state core. A synthetic-key fallback is secondary because 2048 depends on obsolete, implementation-dependent `which` behavior and requires an exact browser test.

## Self-probe

```yaml
expected_task_id: 6a526109ba348191b5f23ad3172ad568
observed_task_id: 6a526109ba348191b5f23ad3172ad568
task_id_match: true
tools_observed:
  github: authenticated_exact_file_read_and_branch_scoped_contents_write
  slack: authenticated_channel_write
  web_primary_sources: available_and_used_for_current_UI_Events_contract
  browser_runtime: unavailable
  shell_runtime: unavailable
  task_mutation: not_called
```

## Dated primary sources inspected

Observed `2026-08-02`:

1. TAGS adapter, exact blob `579c9551225f0974ed93564b6ad8bfb1abf72cf3`:
   `TTaoGaming/TAGS@e0e3125e1ef6bb33e189c91b485ec341f2d3cd52/prototypes/spatial-input-adapter.js`.
2. 2048 input manager, exact blob `ca01b3ce8995a5a20ac50219712d1ef95297ed99`:
   `gabrielecirulli/2048@478b6ec346e3787f589e4af751378d06ded4cbbc/js/keyboard_input_manager.js`.
3. 2048 game manager, exact blob `1c13d15bd667afe06f95316942324885c45d8e6d`:
   `gabrielecirulli/2048@478b6ec346e3787f589e4af751378d06ded4cbbc/js/game_manager.js`.
4. 2048 bootstrap, exact blob `2c1108e757a0e49af7b9ee48dcc45bd8e61cb806`:
   `gabrielecirulli/2048@478b6ec346e3787f589e4af751378d06ded4cbbc/js/application.js`.
5. W3C UI Events current Recommendation snapshot retrieved `2026-08-02`: the normative `KeyboardEventInit` surface defines `key`, `code`, `location`, `repeat`, and `isComposing`; `which`, `keyCode`, and `charCode` are documented in a non-normative legacy section as obsolete and implementation-dependent. https://www.w3.org/TR/uievents/
6. Prior candidate admission card, exact blob `29b4f61059c364ad978d2dceae4ac2406a063017`:
   `projects/spatial-app-factory/research/20260802T012843Z_S08_2048_UPSTREAM_LICENSE_INPUT_SEAM_EVIDENCE_CARD.md`.

## Supported claims

- The exact TAGS adapter produces pointer descriptors/events only; it does not expose a directional `move(0..3)` output.
- Its optional `activationCallback` receives the released DOM target, not a directional action, swipe delta, or 2048 move code.
- Exact 2048 maps keyboard numeric codes and touch-swipe deltas to semantic direction integers, then calls `self.emit("move", mapped)`.
- Exact `GameManager` subscribes to `inputManager.on("move", this.move.bind(this))`; this is the narrow application boundary that should be reused.
- Exact `application.js` constructs `GameManager` without retaining a globally accessible instance, so a clean bridge requires a small bootstrap/InputManager injection rather than assuming an external script can reach the live instance.
- A direct pointer stream alone has no demonstrated consumer that advances the 2048 game.
- A semantic binding can remain additive and preserve the game grid, score, persistence, and native fallback paths.

## Excluded claims

- No browser execution proves that all pointer events are ignored; this result follows from the inspected declared input listeners, not a complete runtime trace.
- No claim that no other historical branch, fork, browser quirk, or unrelated script can translate pointer events into keyboard/touch events.
- No claim that synthetic `KeyboardEvent` can never work. The claim ceiling is narrower: `key`/`code` alone do not standards-guarantee the legacy `which` value consumed by this exact app.
- No claim that the app-specific semantic binding is already implemented, tested, merged, deployed, or accepted by a consumer.
- No accessibility, trusted-input, user-activation, mobile-browser, performance, demand, publication, or marketplace claim.
- No second active spatial WorkItem is admitted by this card.

## Minimum revision gate

A consuming WorkItem should choose exactly one binding and freeze it in tests:

1. **Preferred — semantic InputManager binding:** add an additive method or injected adapter that accepts only direction integers `0..3` and invokes the existing `emit("move", direction)` path.
2. **Acceptable — normalized app action callback:** extend the reusable spatial layer with a host-supplied semantic callback, with the app binding responsible for converting an independently verified gesture into one direction.
3. **Fallback — synthetic keyboard:** dispatch `keydown` only after a real-browser test proves the exact event construction produces the numeric value consumed by `event.which`; retain native keyboard behavior and do not rely on undocumented property mutation.

Required acceptance tests:

- one spatial action emits exactly one legal move value;
- ambiguous or cancelled tracking emits zero moves;
- native arrow/WASD/Vim keyboard input remains functional;
- native touch swipe remains functional;
- game-state code is unchanged;
- repeated held pinch does not produce uncontrolled repeated moves unless an explicit repeat policy is declared;
- exact browser smoke test binds app commit, adapter commit, commands, output, and visual/state evidence.

## License and terms uncertainty

This compatibility revision adds no external package, account, credential, paid service, or terms acceptance. The prior MIT code-license ceiling remains unchanged: preserve the notice for copied/substantial code, and treat public branding, clone provenance, non-code assets, and marketplace terms as separate unresolved gates. This card is engineering evidence, not legal advice.

## Cost and operator-minute estimate

```yaml
direct_research_cost_usd: 0
operator_minutes_required_now: 0
estimated_binding_implementation_minutes: 20_to_60
estimated_deterministic_test_minutes: 20_to_45
estimated_browser_smoke_minutes: 15_to_30
estimated_operator_minutes_if_internal_only: 0_to_5
new_credentials_required: 0
new_packages_required: 0
estimate_status: HEURISTIC_NOT_FITNESS_CREDIT
```

## Strongest objection

The current pointer adapter was designed for cursor/pinch activation, while 2048 is fundamentally a directional-swipe application. Adding a semantic direction layer may weaken the claim that one universal pointer adapter can drive every app. That objection is valid: the reusable asset should be a small family of explicit output bindings—pointer activation and semantic direction—not a false universal event shim.

## Falsifier

Change this result to `ADMIT` for direct compatibility only if a distinct browser-capable verifier runs the exact frozen app and adapter bytes and proves that the unmodified TAGS pointer output causes one correct 2048 move per accepted gesture, with zero app-specific binding, zero native-input regression, and exact execution receipts.

Change to `RETIRE` the 2048 candidate if the smallest honest semantic binding requires game-state changes, breaks keyboard/touch fallback, cannot prevent duplicate moves, or exceeds the bounded implementation/test timebox.

## Verifier, consumer, expiry

- **Structural verifier:** S04 checks commit/path/blob bindings, authority, expiry, and that the proposed packet changes only the input boundary; same-provider binding weight remains zero.
- **Distinct verifier:** a browser-capable nonproducer on Codex, Claude host, VM, or another authorized substrate executes the exact bytes and tests.
- **Consumer:** the next exact Spatial Factory golden-app WorkItem may consume, revise, or reject this card. S06 may compile the packet; S07 may execute it; the backlog owner must record acceptance/rejection before fitness credit.
- **Expiry:** `2026-08-09T02:30:00Z`, or immediately on app commit, adapter commit, browser contract, or active WorkItem change.

## Honest flaw

This carrier had exact repository reads and current standards text but no browser or shell. It did not run the app, construct synthetic keyboard events, or inspect a recursive repository tree. The evidence is sufficient to reject a direct plug-compatibility claim from the declared interfaces; it is not runtime proof of the proposed revision. Fitness remains `0` until an exact WorkItem consumes the card and a distinct verifier executes the frozen bytes.

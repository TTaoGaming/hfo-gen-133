---
schema_id: hfo.gen133.s08.research_evidence_card.v1
card_id: S08_SYNTHETIC_POINTER_ACTIVATION_BOUNDARY_20260731T222600Z
result: REVISE
callsign_or_seat: S08_RESEARCH_CANDIDATE_SCOUT
carrier_task_id: 6a526109ba348191b5f23ad3172ad568
carrier_identity_claim: DISPOSABLE_SCHEDULED_CARRIER_NOT_LINEAGE
controller: operator_direct
wip: 1
valid_time_utc: 2026-07-31T22:26:00Z
transaction_time_utc: SEE_GITHUB_COMMIT_METADATA
canonical_repository: TTaoGaming/hfo-gen-133
canonical_branch: agent/gen133-bootstrap-20260730
work_item_id: SPATIAL_FACTORY_GOLDEN_APP_001
research_lane: interaction_input_adapters
privacy_class: PUBLIC_STANDARDS_AND_SANITIZED_REPOSITORY_POINTERS_ONLY
expiry_utc: 2026-07-31T23:04:00Z
verifier: Sigrun/P4_APEX_FALSIFICATION_or_other_distinct_provider_nonproducer
consumers:
  - Olrun/Claude-Dispatch
  - S06_task_6a57972b9df081918680ce67c4ecb197
  - S07_task_6a506f6dc5c08191b95f1707d7f00c2d
sealed: false
---

# S08 evidence card — synthetic pointer dispatch versus native activation

## Changed queue evidence

S15 commit `96470c508a6b6dd12b5932e561b5f322eeaf399a` offered a reusable pinch hysteresis state pattern but explicitly excluded ordinary pointer descriptors, invalid-input safety, and native fallback proof. That materially changes the next research uncertainty from candidate licensing to the interaction-adapter boundary.

Current packet under review:

- repository: `TTaoGaming/hfo-gen-133`
- executor packet commit: `7b5a36f6c4790ed99f80c71b4c8fc57816db8bdc`
- packet path: `projects/spatial-app-factory/dispatch/20260731T212211Z_SPATIAL_FACTORY_GOLDEN_APP_001_S06_EXECUTOR.packet.yaml`
- target repository/base: `TTaoGaming/TAGS@1271e25306fe8ef8baea32704cf022435703d498`
- target page: `prototypes/fab-prototype.html`

## Bounded question

Can the adapter satisfy pinch activation by dispatching synthetic `pointerdown` and `pointerup` events and relying on the browser to create the FAB's native click/activation behavior, while preserving mouse, touch, and keyboard fallback?

## Decision

`REVISE` the executor contract before implementation.

Synthetic `PointerEvent` construction and `dispatchEvent()` are standard mechanisms for exposing pointer descriptors to listeners. They are not a standards-backed substitute for trusted physical input, browser user activation, focus, or guaranteed compatibility mouse/click synthesis. The adapter must separate **pointer observation** from **control activation**.

## Self-probe

```yaml
expected_task_id: 6a526109ba348191b5f23ad3172ad568
observed_task_id: 6a526109ba348191b5f23ad3172ad568
task_id_match: true
tools_observed:
  github: read_write
  slack: read_write
  web_primary_standards: read
  shell_or_browser_runtime: unavailable
  native_task_mutation: not_called
```

## Primary/current sources — observed 2026-07-31

1. W3C Pointer Events Level 3, Recommendation dated 2026-06-30, includes an official example constructing and dispatching untrusted pointer events from script and defines the `PointerEvent` constructor: https://www.w3.org/TR/2026/REC-pointerevents3-20260630/
2. WHATWG DOM Standard defines `dispatchEvent()` and initializes script-created/dispatched events with `isTrusted` false: https://dom.spec.whatwg.org/#dom-eventtarget-dispatchevent and https://dom.spec.whatwg.org/#dom-event-istrusted
3. W3C Pointer Events compatibility mouse-event mapping is specified as user-agent behavior for generic pointer input; it does not promise that script-dispatched `pointerdown`/`pointerup` will cause a `click`: https://www.w3.org/TR/2026/REC-pointerevents3-20260630/#compatibility-mapping-with-mouse-events
4. WHATWG HTML defines `HTMLElement.click()` as the explicit synthetic activation method for an enabled element. The resulting click is not trusted, and calling `click()` does not focus the element: https://html.spec.whatwg.org/multipage/interaction.html#dom-click

## Supported claims

- The dependency-free adapter may construct `PointerEvent` objects and dispatch `pointermove`, `pointerdown`, and `pointerup` to expose deterministic spatial-input observations to application listeners.
- Script-dispatched events are untrusted. Tests should assert observable descriptors and transitions, not claim hardware emulation or trusted user activation.
- For a synthetic source that is not a physical pointing device, `pointerId: -1` is the reserved Pointer Events value; event initialization should explicitly bind coordinates, `button`, `buttons`, bubbling, cancelability, and composition rather than rely on browser defaults.
- Exactly-once pinch activation should be a separate injected seam. For the current FAB button/control, the browser integration may call `target.click()` once on a valid matched release if the target is enabled and intended to activate.
- Real mouse, touch, keyboard, and existing click behavior remain preserved by adding the seam without removing handlers, intercepting events, or calling `preventDefault()` on native paths.
- No new runtime package, account, paid service, or third-party SDK is required for this revision.

## Required packet revision

1. Keep A2/A3 focused on deterministic pointer descriptors and hysteresis edges.
2. Add an injected activation function or target method that is invoked exactly once on valid pinch release, not while held and not for invalid/below-confidence samples.
3. Do not state that synthetic `pointerdown`/`pointerup` automatically cause `click`, focus, trusted user activation, or compatibility mouse events.
4. Add a test proving exactly one activation call for one completed pinch and zero activation for held, invalid, missing, non-finite, or below-confidence samples.
5. Keep native fallback verification separate. A static HTML smoke test can prove the original button remains present, but it cannot by itself prove browser focus, keyboard, touch, or activation behavior. A later browser-level producer/verifier run is required for that stronger claim.

## Excluded claims

- No claim that script-dispatched pointer events have `isTrusted: true`.
- No claim that synthetic pointer events satisfy browser security-gated user-activation requirements.
- No claim that `pointerdown` plus `pointerup` guarantees a browser-generated `click` or compatibility mouse sequence.
- No claim that `target.click()` focuses the element or is semantically correct for every future draggable, canvas, or non-control target.
- No claim that Node unit tests or `curl` prove cross-browser mouse, touch, keyboard, focus, accessibility, or hit-testing behavior.
- No build, browser run, branch mutation, test pass, merge, deployment, publication, or ConsumerAck is established by this card.

## License and terms uncertainty

The candidate capability is a set of browser platform APIs defined by public standards, not a bundled third-party library. No software-license acceptance or runtime dependency is introduced by using `PointerEvent`, `dispatchEvent()`, or `HTMLElement.click()`.

Remaining uncertainty is behavioral and portability-related: browser implementations may differ at edge cases, and synthetic activation does not grant trusted user-activation privileges. The separate prototype provenance gate from S08 commit `47b5d99d05203d36c4047115e8e0a533509f4565` remains unchanged.

## Cost and operator burden

```yaml
direct_cost_usd: 0
new_credentials_required: 0
new_packages_required: 0
estimated_executor_rework_minutes_added: 5_to_10
estimated_operator_or_reviewer_minutes_avoided: 10_to_20
operator_minutes_required_now: 0
```

## Strongest objection

Calling `target.click()` is deliberately narrower than pretending pointer events are physical input, but it can still be wrong for non-button targets, drag interactions, focus-dependent UX, or controls whose activation requires a trusted gesture. Exact target selection and browser behavior therefore remain a host/browser acceptance concern, not something this standards card can close.

## Falsifier

Change this result only if a direct clean-browser test on the declared supported browser matrix, bound to the exact producer SHA, proves that the current required behavior is fully satisfied by synthetic pointer-event observation alone and that no control activation is required. Even then, the implementation must not upgrade untrusted events into a trusted-input claim.

Immediate `RETIRE` conditions:

- implementation relies on synthetic events to bypass browser user-activation/security gates;
- native input handlers are removed, canceled, or replaced;
- invalid samples can trigger pointer or activation effects;
- activation repeats while a pinch remains held;
- the result is marked PASS without exact browser/runtime commands, exit codes, and readback.

## Consumer action and credit rule

Olrun/S06 should revise the existing packet or producer instructions in place before a real implementation return. S07 may consume the revised contract for bounded branch/file/test work. This card earns no fitness until a producer return explicitly binds this card and demonstrates either `CONSUMED` or `REJECTED_WITH_EVIDENCE`.

After `2026-07-31T23:04:00Z`, this card is historical evidence only unless a renewed live WorkItem binds it.

## Honest flaw

This carrier read current primary standards and exact Gen-133 packet/heritage pointers but had no browser or shell execution surface. It did not test Chrome, Firefox, Safari, mobile touch, focus behavior, hit-testing, or the private FAB page at runtime. Standards establish the contract boundary; they do not constitute producer execution or independent verification.

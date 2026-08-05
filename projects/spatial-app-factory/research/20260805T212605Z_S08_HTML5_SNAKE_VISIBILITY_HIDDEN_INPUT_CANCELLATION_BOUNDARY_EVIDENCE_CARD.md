---
schema_id: hfo.gen133.s08_evidence_card.v1
card_id: S08_HTML5_SNAKE_VISIBILITY_HIDDEN_INPUT_CANCELLATION_BOUNDARY_20260805T212605Z
result: REVISE
seat: S08_RESEARCH_AND_CANDIDATE_SCOUT
wip: 1
task_id_expected: 6a526109ba348191b5f23ad3172ad568
task_id_observed: 6a526109ba348191b5f23ad3172ad568
task_id_match: true
valid_time_utc: 2026-08-05T21:26:05Z
transaction_time_utc: SEE_GITHUB_COMMIT_METADATA
canonical_repository: TTaoGaming/hfo-gen-133
canonical_branch: agent/gen133-bootstrap-20260730
lane: INTERACTION_INPUT_ADAPTERS
question: Is window blur alone a sufficient cancellation boundary when the Snake document becomes hidden?
consumer: SPATIAL_FACTORY_HTML5_SNAKE_PENDING_DIRECTION_COMMAND_GATE_001
verifier: DISTINCT_CHROMIUM_FIREFOX_VISIBILITY_HIDDEN_INPUT_CANCELLATION_VERIFIER
expiry_utc: 2026-08-12T21:26:05Z
fitness: 0_PENDING_EXACT_WORKITEM_CONSUMPTION_AND_CONSUMER_ACK
---

# S08 evidence card — hidden visibility is a distinct input-cancellation boundary

## Self-probe and selection

- Identity and expected task ID matched.
- Available surfaces used: authenticated GitHub read/write/readback, current public standards research, and authenticated Slack pointer delivery after Git readback.
- Unavailable this pass: target-host shell, Chromium, Firefox, direct executor ingress, and private runtime telemetry.
- Rotation lane selected: **interaction/input adapters**.
- Changed question source: the fresh namespace-isolation successor claim at commit `92c8ec2a38359dbf18858919120a12edd609e037` requires blur/reset/tracking-loss/ownership-loss cancellation, but its acceptance clause 22 does not name a document transition to `visibilityState="hidden"`.
- Duplicate search: no prior Gen-133 S08 card was found for `visibilitychange`, `document.hidden`, or hidden-state cancellation in this WorkItem.

## Exact candidate

- WorkItem: `SPATIAL_FACTORY_HTML5_SNAKE_PENDING_DIRECTION_COMMAND_GATE_001`
- Current successor claim: `TTaoGaming/hfo-gen-133@92c8ec2a38359dbf18858919120a12edd609e037`
- Claim path: `projects/spatial-app-factory/claims/20260805T210556Z_SPATIAL_FACTORY_HTML5_SNAKE_NAMESPACE_ISOLATION_SUCCESSOR.claim.yaml`
- Repository head observed immediately before this research write: `3acdbd956a05b1d2b7a80ca018134ef640775a75`
- Upstream candidate: `JDStraughan/html5-snake@e3fe18a85a0555f0540cc0978fbab62822262a91`
- Upstream `game.js` blob: `c286389487bd68f15170fbb3add6a060f252d169`
- Target base: `TTaoGaming/TAGS@1271e25306fe8ef8baea32704cf022435703d498`
- Allowed target prefix: `prototypes/html5-snake-spatial-canary/**`

## Bounded finding

The current contract's blur boundary is necessary but not sufficient to stand a hidden-page cancellation claim.

The WHATWG HTML Living Standard defines page visibility from a traversable's **system visibility state**, including cases where the browser window is minimized, the tab is in the background, or a system UI obscures the page. When that state changes, the user agent updates `Document.visibilityState` and fires `visibilitychange` at the document.

The W3C UI Events specification defines `blur` around a different condition: a user agent dispatches it when an event target loses focus. UI Events also scopes its focus events to document focus contexts. No normative guarantee was found that every transition to `Document.visibilityState === "hidden"` must first or also dispatch the blur path relied on by this successor.

Therefore the current acceptance contract cannot infer `HIDDEN_STATE_CANCELLED=true` from blur handling alone.

```text
WINDOW_BLUR_CANCEL_BOUNDARY=REQUIRED_BUT_NOT_SUFFICIENT
DOCUMENT_VISIBILITY_HIDDEN=INDEPENDENT_CANCEL_BOUNDARY
HIDDEN_TRANSITION_MUST_CLEAR_PENDING_INTENT=true
HIDDEN_TRANSITION_MUST_CANCEL_HELD_ACTIVATION_EXACTLY_ONCE=true
HIDDEN_TRANSITION_MUST_REQUIRE_NEUTRAL_RELEASE_TO_REARM=true
VISIBLE_TRANSITION_MUST_NOT_AUTO_COMMIT_OR_AUTO_REARM=true
COMMAND_ACCEPTANCE_WHILE_HIDDEN=FORBIDDEN
```

## Required revision

Add `document.addEventListener("visibilitychange", ...)` or an equivalent standards-bound listener. When `document.visibilityState === "hidden"`, the adapter must:

1. clear pending keyboard and spatial intent;
2. cancel an in-progress `BEGIN`/`HELD` activation exactly once without emitting `COMMIT`;
3. enter `REQUIRE_RELEASE` until neutral input is observed after visibility, focus, and ownership are revalidated;
4. reject all Arrow and `DIRECT_COMMAND` requests while hidden; and
5. ensure transition back to `visible` does not itself resume, commit, increment an action counter, or rearm a held input.

This card does not require page-unload accounting, analytics, persistence, or background-loop policy. It addresses only input-state safety at the visible-to-hidden boundary.

## Supported claims

- Page visibility and focus are separately specified state surfaces.
- Background-tab, minimized-window, and system-obscured cases are represented by the page-visibility state.
- `visibilitychange` is the specified document event when visibility state changes.
- `blur` is specified when an event target loses focus.
- The current successor acceptance text does not explicitly bind hidden visibility to cancellation and release-to-rearm.

## Excluded claims

- No claim is made that Chromium or Firefox currently omit blur on every or any particular hide transition.
- No browser conformance result is claimed without exact-SHA runtime traces.
- No claim is made about mobile operating-system process suspension, page discard, `freeze`, `pagehide`, `beforeunload`, or `unload` ordering.
- No claim is made that visibility alone proves user absence, device lock, or loss of camera permission.
- No implementation, browser execution, deployment, merge, or publication occurred.

## License and terms uncertainty

- The standards were used as public technical references only; no terms acceptance or account action occurred.
- This finding changes no upstream code-license classification.
- Upstream visible MIT notice handling remains required.
- `PUBLIC_DISTRIBUTION_CHAIN_OF_TITLE=NOT_STOOD` remains unchanged.

## Strongest objection

In common desktop behavior, switching tabs or minimizing a browser often also causes blur, so an additional visibility listener may appear redundant.

That objection does not stand the acceptance claim. The current primary specifications define different triggering conditions and do not bind every hidden transition to the exact blur cancellation path. A low-cost explicit hidden-state gate removes that unsupported dependency and makes the verifier's state machine observable.

## Falsifier

Revise or retire this card if an exact-SHA, version-bound Chromium and Firefox verification proves all of the following without a visibility listener or equivalent hidden-state check:

- every controlled visible-to-hidden transition necessarily invokes the same cancellation path before any further tick or command processing;
- pending intent is cleared;
- held activation emits exactly one cancel and no commit;
- hidden commands are rejected;
- return to visible cannot auto-rearm or replay held input; and
- the guarantee is supported by a normative browser contract rather than only observed coincidence.

Absent that proof, the successor should add the explicit hidden-state boundary.

## Verification contract

Verifier: `DISTINCT_CHROMIUM_FIREFOX_VISIBILITY_HIDDEN_INPUT_CANCELLATION_VERIFIER`

Required exact-SHA fixtures at both 8 fps and 60 fps:

- pending Arrow command, then document hidden before movement tick;
- spatial `HELD`, then document hidden;
- document hidden while neutral, followed by Arrow and `DIRECT_COMMAND` attempts;
- hidden-to-visible while the physical key or spatial gesture remains held;
- hidden-to-visible followed by neutral release and fresh command;
- blur-only control, visibility-hidden control, and combined blur-plus-hidden sequence;
- duplicate visibility notifications or repeated state checks must not produce duplicate cancellation.

The verifier must bind implementation SHA, browser versions, event trace ordering, pending direction, committed direction, activation count, cancellation count, ownership, visibility state, focus state, and release-to-rearm state.

## Cost and operator-minute estimate

- This pass: `$0` spend; `0` operator minutes; approximately `12–20` scheduled-agent minutes.
- Producer amendment: `5–15` minutes.
- Exact-SHA Chromium and Firefox verification: `25–50` verifier minutes.
- New external service, account, purchase, or dependency: none.

## Primary/current sources

1. WHATWG, **HTML Living Standard — User interaction, §6.2 Page visibility**, last updated **2026-07-20**, accessed **2026-08-05**. Defines system visibility examples, document hidden/visible state, state update, and `visibilitychange` dispatch.  
   https://html.spec.whatwg.org/multipage/interaction.html#page-visibility
2. W3C, **UI Events**, current Technical Report accessed **2026-08-05**; focus-event sections define document focus contexts and dispatch of `blur` when an event target loses focus.  
   https://www.w3.org/TR/uievents/#events-focusevent-event-order
   https://www.w3.org/TR/uievents/#event-type-blur

## Decision

`REVISE`

The WorkItem should not claim complete cancellation/rearm coverage until hidden document visibility is an explicit input-state boundary and a distinct exact-SHA verifier stands the behavior.

---
schema_id: hfo.gen133.s08_research_evidence_card.v1
result: REVISE
seat: S08_RESEARCH_AND_CANDIDATE_SCOUT
wip: 1
valid_time_utc: 2026-08-05T20:26:06Z
transaction_time_utc: SEE_GITHUB_COMMIT_METADATA
expected_task_id: 6a526109ba348191b5f23ad3172ad568
observed_task_id: 6a526109ba348191b5f23ad3172ad568
task_id_match: true
canonical_repository: TTaoGaming/hfo-gen-133
canonical_branch: agent/gen133-bootstrap-20260730
lane: spatial_foss_candidates_and_licenses
question_changed: true
question: >-
  Does the fresh HTML5 Snake successor remain safe to embed with a spatial adapter after removing
  Object.prototype.getKey, or does the exact upstream classic script still expose mutable control state through
  undeclared global assignments?
decision: REVISE
consumer: SPATIAL_FACTORY_HTML5_SNAKE_PENDING_DIRECTION_COMMAND_GATE_001_OR_FRESH_SUCCESSOR
verifier: DISTINCT_CHROMIUM_FIREFOX_GLOBAL_NAMESPACE_AND_INPUT_PARITY_VERIFIER
expiry_utc: 2026-08-12T20:26:06Z
fitness: 0_PENDING_EXACT_WORKITEM_CONSUMPTION_AND_CONSUMER_ACK
---

# S08 evidence card — HTML5 Snake implicit-global namespace boundary

## Exact candidate and changed edge

- Current conditional successor claim: `S02_SPATIAL_FACTORY_HTML5_SNAKE_OBJECT_PROTOTYPE_LOCAL_OWN_DATA_SUCCESSOR_20260805T180210Z`
- Claim commit: `1db833ae5048e6f8a04ce3bfd270ff41ef455910`
- Claim path: `projects/spatial-app-factory/claims/20260805T180210Z_SPATIAL_FACTORY_HTML5_SNAKE_OBJECT_PROTOTYPE_LOCAL_OWN_DATA_SUCCESSOR.claim.yaml`
- WorkItem: `SPATIAL_FACTORY_HTML5_SNAKE_PENDING_DIRECTION_COMMAND_GATE_001`
- Target base: `TTaoGaming/TAGS@1271e25306fe8ef8baea32704cf022435703d498`
- Upstream: `JDStraughan/html5-snake@e3fe18a85a0555f0540cc0978fbab62822262a91`
- Exact `game.js` blob: `c286389487bd68f15170fbb3add6a060f252d169`
- Exact `index.html` blob: `61243962bab6846c3e06dba4358a547755dc1379`

The fresh claim adds a finite local direction lookup and removes the native-prototype mutation, but its acceptance contract does not explicitly prohibit unrelated implicit globals or require whole-runtime namespace containment.

## Bounded finding

The pinned `index.html` loads `game.js` as an ordinary classic script. In the pinned `game.js`, the assignments to `game`, `snake`, `food`, `inverseDirection`, and `keys` have no declarations. The loop variable `i` and keyboard variable `lastKey` are also assigned without declarations.

In non-strict ECMAScript, assigning through an unresolvable reference performs a `Set` on the global object. Therefore these names can create or overwrite global-object properties depending on pre-existing page state. Removing `Object.prototype.getKey` does not remove this separate global-state surface.

This card does not claim an observed exploit, collision, or browser divergence. It establishes only that the exact source's control state is not locally contained and that the result can depend on unrelated global-page state.

## Required revision

```text
IMPLICIT_GLOBAL_ASSIGNMENTS=FORBIDDEN
CLASSIC_SCRIPT_GLOBAL_CONTROL_STATE=NOT_ADMITTED
RUNTIME_STATE=LEXICALLY_CONTAINED
EXPLICIT_ADAPTER_SURFACE=AT_MOST_ONE_DOCUMENTED_ALLOWLISTED_API
GLOBAL_OWN_PROPERTY_DIFF=ZERO_OR_EXACT_ALLOWLIST
```

Use a lexical containment boundary such as an IIFE or module and declare every binding with `const` or `let`. If a cross-file adapter seam is required, expose only one explicit, documented, narrow API; do not expose mutable `game`, `snake`, `food`, pending-direction, ownership, or activation internals.

Add an exact-SHA browser check that snapshots relevant global own-property names before and after load. The allowed delta must be empty or match one explicit adapter namespace exactly. Also run strict-mode/static checks that fail on undeclared writes.

## Supported claims

- The exact upstream HTML loads `game.js` without module semantics.
- The exact upstream JavaScript contains undeclared writes to `game`, `snake`, `food`, `inverseDirection`, `keys`, `i`, and `lastKey`.
- Non-strict assignment to an unresolvable reference targets the global object.
- The fresh claim's prototype and local-direction-map gates do not by themselves prove whole-runtime namespace isolation.

## Excluded claims

- No security exploit, cross-origin effect, data leak, or actual collision is proven.
- No claim is made that every browser exposes identical property descriptors or enumeration order for all global bindings.
- No claim is made that a single-page isolated canary has already malfunctioned because of these globals.
- This card does not verify an implementation, browser trace, or test pass.

## License and terms boundary

The upstream visible MIT notice and notice-retention requirement are unchanged. Namespace containment is an implementation-quality boundary, not a new license conclusion. `PUBLIC_DISTRIBUTION_CHAIN_OF_TITLE=NOT_STOOD` remains unchanged, and known later credited commits remain excluded from the approved source bundle.

## Strongest objection

The canary is isolated and currently loads no unrelated application scripts, so the globals may not collide in the first demo. Correct. That makes this a containment and reproducibility defect rather than proof of present breakage. The spatial adapter, browser test harness, and future embedding are exactly the contexts where ambient mutable names turn local invariants into page-global assumptions; the minimal IIFE/explicit-declaration repair is lower-risk than carrying those assumptions forward.

## Falsifier

Revise or retire this card if an exact implementation SHA demonstrates all of the following in Chromium and Firefox:

1. no undeclared writes under strict/static analysis;
2. no unexpected global own-property additions after page load;
3. any one allowed adapter namespace is explicit, frozen or otherwise mutation-bounded, and exposes no internal mutable control state;
4. native Arrow and spatial `DIRECT_COMMAND` traces remain identical under injected unrelated globals named `game`, `snake`, `food`, `keys`, `i`, and `lastKey`;
5. deterministic 8-fps and 60-fps acceptance traces remain unchanged.

## Cost and operator-minute estimate

- Producer amendment: `10–25 minutes`
- Static and unit fixtures: `10–20 minutes`
- Chromium and Firefox namespace/input verification: `20–40 minutes`
- Direct spend: `$0`
- Operator minutes this research pass: `0`

## Primary and exact sources

1. Exact upstream `game.js`, pinned commit and blob, observed 2026-08-05: https://github.com/JDStraughan/html5-snake/blob/e3fe18a85a0555f0540cc0978fbab62822262a91/game.js
2. Exact upstream `index.html`, pinned commit and blob, observed 2026-08-05: https://github.com/JDStraughan/html5-snake/blob/e3fe18a85a0555f0540cc0978fbab62822262a91/index.html
3. Fresh Gen-133 successor claim, commit `1db833ae5048e6f8a04ce3bfd270ff41ef455910`, observed 2026-08-05: https://github.com/TTaoGaming/hfo-gen-133/blob/1db833ae5048e6f8a04ce3bfd270ff41ef455910/projects/spatial-app-factory/claims/20260805T180210Z_SPATIAL_FACTORY_HTML5_SNAKE_OBJECT_PROTOTYPE_LOCAL_OWN_DATA_SUCCESSOR.claim.yaml
4. ECMAScript 2024, `PutValue`, §6.2.5.6, accessed 2026-08-05: https://tc39.es/ecma262/2024/#sec-putvalue

## Effect receipt

No implementation, browser execution, target-branch creation, task mutation, account action, terms acceptance, outreach, application, purchase, send, spend, deployment, merge, release, public publication, or private-data use occurred. Only task inventory read, exact Git/source reads, primary-source research, this Git evidence write/readback, and one material Slack pointer are permitted for this pass.

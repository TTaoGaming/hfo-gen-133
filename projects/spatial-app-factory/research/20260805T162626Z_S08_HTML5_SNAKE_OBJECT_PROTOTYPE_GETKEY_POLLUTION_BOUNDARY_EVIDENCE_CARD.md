---
schema_id: hfo.gen133.s08_evidence_card.v1
result: REVISE
seat: S08_RESEARCH_AND_CANDIDATE_SCOUT
wip: 1
valid_time_utc: 2026-08-05T16:26:26Z
transaction_time_utc: SEE_GITHUB_COMMIT_METADATA
expected_task_id: 6a526109ba348191b5f23ad3172ad568
observed_task_id: 6a526109ba348191b5f23ad3172ad568
task_id_match: true
lane: INTERACTION_INPUT_ADAPTERS
canonical_repository: TTaoGaming/hfo-gen-133
canonical_branch: agent/gen133-bootstrap-20260730
consumer: SPATIAL_FACTORY_HTML5_SNAKE_PENDING_DIRECTION_COMMAND_GATE_001
verifier: DISTINCT_EXACT_SHA_OBJECT_PROTOTYPE_AND_INPUT_LOOKUP_VERIFIER
expiry_utc: 2026-08-12T16:26:26Z
monetary_cost_usd: 0
operator_minutes_this_pass: 0
producer_amendment_estimate_minutes: 5-10
verification_estimate_minutes: 10-20
---

# REVISE — remove the inherited enumerable `Object.prototype.getKey` input helper

## Bounded uncertainty

Does preserving the exact upstream `Object.prototype.getKey` helper provide a safe input lookup seam for the admitted HTML5 Snake source bundle?

## Exact candidate and changed queue edge

- Upstream: `JDStraughan/html5-snake@e3fe18a85a0555f0540cc0978fbab62822262a91`
- File/blob: `game.js` / `c286389487bd68f15170fbb3add6a060f252d169`
- Fresh successor claim: `TTaoGaming/hfo-gen-133@d363ebba67d6141d376e11dd239901a7fe6ec878`
- Fresh route HOLD: `TTaoGaming/hfo-gen-133@6bd112c1dbfc5476b2c414ac87f64a558f9ae4f5`
- WorkItem: `SPATIAL_FACTORY_HTML5_SNAKE_PENDING_DIRECTION_COMMAND_GATE_001`

The newly admitted source bundle copies the exact upstream `game.js`, whose keyboard lookup adds `getKey` directly to `Object.prototype` and then uses `for...in` to inspect a key table. The successor acceptance already requires `event.key` Arrow values and a shared `requestDirection(nextDirection)` seam, so this global helper is no longer necessary.

## Evidence

1. The pinned source executes `Object.prototype.getKey = function(value) { ... }` and calls the inherited method as `keys.getKey(e.keyCode)`. It also depends on numeric `keyCode` arrays that the successor acceptance explicitly replaces. Source inspected 2026-08-05: https://github.com/JDStraughan/html5-snake/blob/e3fe18a85a0555f0540cc0978fbab62822262a91/game.js
2. ECMAScript ordinary assignment of a previously absent property creates a writable, enumerable, configurable data property. Therefore this assignment creates an enumerable own property named `getKey` on `Object.prototype`. Source inspected 2026-08-05: https://tc39.es/ecma262/2026/multipage/ordinary-and-exotic-objects-behaviours.html#sec-ordinarysetwithowndescriptor
3. ECMAScript `for...in` iteration includes own and inherited enumerable string properties. Consequently, `getKey` becomes visible to `for...in` loops over ordinary objects unless shadowed or filtered. Source inspected 2026-08-05: https://tc39.es/ecma262/2026/multipage/ecmascript-language-statements-and-declarations.html#sec-for-in-iterator-objects
4. The fresh executor packet requires Arrow-key and `DIRECT_COMMAND` input to converge on one local `requestDirection(nextDirection)` seam and forbids numeric `keyCode` aliases. That removes the original helper's stated purpose. Source inspected 2026-08-05: https://github.com/TTaoGaming/hfo-gen-133/blob/6bd112c1dbfc5476b2c414ac87f64a558f9ae4f5/projects/spatial-app-factory/dispatch/20260805T162057Z_SPATIAL_FACTORY_HTML5_SNAKE_REPRODUCIBLE_SOURCE_BUNDLE_DIRECT_INGRESS_HOLD.executor.yaml

## Required classification

```text
OBJECT_PROTOTYPE_GETKEY_MUTATION=REMOVE
INHERITED_ENUMERABLE_INPUT_HELPER=FORBIDDEN
DIRECTION_LOOKUP=LOCAL_OWN_DATA_ONLY
NUMERIC_KEYCODE_TABLE=REMOVE
FOR_IN_DIRECTION_LOOKUP=REMOVE
```

Use a finite local `switch` or an own-property-only frozen map from `ArrowUp | ArrowDown | ArrowLeft | ArrowRight` to canonical directions. Both native keyboard and spatial `DIRECT_COMMAND` paths must call the same `requestDirection(nextDirection)` function; neither path needs or may create a native-prototype extension.

## Supported claims

- The exact pinned source writes `getKey` onto `Object.prototype`.
- That newly created property is enumerable under ordinary ECMAScript assignment semantics.
- `for...in` can expose inherited enumerable properties.
- The admitted successor no longer needs this helper because its contract uses `event.key` and a direct command seam.
- Removing the helper reduces global behavioral surface without changing the upstream MIT notice obligation.

## Excluded claims

- No current production exploit, user-visible failure, or security incident is proven.
- The exact upstream helper's internal loop does not necessarily return an incorrect direction today; its `instanceof Array` guard ignores the inherited function in that one loop.
- This card does not prove absence of every other prototype mutation, input bug, browser difference, or third-party script interaction.
- This card does not establish public-distribution chain of title or runtime correctness.

## License and terms uncertainty

The exact upstream README carries an MIT notice, and this source edit is ordinarily within MIT modification permission when the complete notice is retained. Public-distribution chain of title, third-party provenance, and package compliance remain `NOT_STOOD`; this card changes no license conclusion and accepts no terms.

## Strongest objection

The canary is small, and the current `getKey` loop filters values with `instanceof Array`, so the inherited `getKey` entry is harmless in the exact upstream path. That is plausible for the current line-level behavior, but it does not justify retaining an unnecessary enumerable mutation on the root prototype after the numeric-key lookup has been removed. The mutation changes every ordinary object's inherited surface and creates avoidable coupling for tests, adapters, and future `for...in` code.

## Falsifier

Revise this decision only if an exact-sha implementation demonstrates a necessary compatibility requirement that cannot be met with a local own-property lookup, while proving no observable `Object.prototype` mutation before or after load across Chromium and Firefox. Otherwise the decision falls if the successor still contains the prototype assignment, numeric key table, or inherited `getKey` lookup.

## Verification contract

A distinct verifier should bind the exact implementation SHA and prove:

- `Object.prototype` has no own `getKey` property before and after page load.
- no runnable source writes to `Object.prototype` or another native prototype;
- direction lookup uses only a finite local switch or own frozen map;
- numeric `keyCode` aliases and `for...in` direction lookup are absent;
- native Arrow input and `DIRECT_COMMAND` produce identical accepted/rejected `requestDirection` traces;
- Chromium and Firefox retain the existing pending-direction, cancellation, focus, release-to-rearm, and one-action-per-cycle guarantees.

## Consumer and fitness

- Consumer: `SPATIAL_FACTORY_HTML5_SNAKE_PENDING_DIRECTION_COMMAND_GATE_001`
- Suggested acceptance amendment: add the five required-classification lines above to the next unexpired successor claim or producer packet.
- Fitness: `0` until an exact WorkItem consumes this card and a distinct verifier binds the implementation SHA.

## Honest flaw

This pass inspected immutable source and contract text plus the ECMAScript specification. It did not run the page, execute tests, create a target branch, inspect a producer return, prove browser conformance, or establish public distribution rights. GitHub search and branch state are nontransactional snapshots.

No task mutation, implementation, account action, terms acceptance, outreach, application, purchase, send, spend, deployment, merge, publication, or private-data use occurred.

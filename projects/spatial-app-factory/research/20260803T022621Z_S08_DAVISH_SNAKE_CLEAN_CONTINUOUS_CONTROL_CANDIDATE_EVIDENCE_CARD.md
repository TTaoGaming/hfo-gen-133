---
schema_id: hfo.gen133.s08.evidence_card.v1
seat: S08_RESEARCH_AND_CANDIDATE_SCOUT
carrier_task_id_expected: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_observed: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_match: true
wip: 1
valid_time_utc: 2026-08-03T02:26:21Z
transaction_time_utc: SEE_GITHUB_COMMIT_METADATA
canonical_repository: TTaoGaming/hfo-gen-133
canonical_branch: agent/gen133-bootstrap-20260730
lane: spatial_foss_candidates_and_licenses
question_changed_from: state/coordination/votes/20260802T213400Z_S09_LORECIONI_SNAKE_QUEUE_RECLASSIFICATION.vote.md
question: Does an exact licensed browser Snake candidate materially dominate lorecioni/snake as a future continuous-control stress-test specimen without creating a second active WorkItem?
candidate_repository: davish/snake
candidate_commit: 13989df94ce227cd6e3ba347e61d3c95ec0279da
candidate_commit_time_utc: 2015-06-17T03:57:51Z
decision: REVISE
classification: CLEANER_STATIC_CANDIDATE_BUT_REPAIR_BEFORE_ADMIT
fitness_credit: 0
sealed: false
privacy_class: PUBLIC_REPOSITORY_METADATA_AND_SOURCE_ONLY
expiry: 2026-09-01T00:00:00Z
---

# S08 evidence card — cleaner continuous-control Snake candidate

## Bounded result

**REVISE.** `davish/snake@13989df94ce227cd6e3ba347e61d3c95ec0279da` is materially cleaner than `lorecioni/snake@875bf961870abfa50c9e2a6564391ea4a85ff42a` for a future continuous-direction adapter test, but the exact current bytes should not be admitted as runnable evidence until one startup defect and one license-attribution uncertainty are resolved.

This changed question is grounded in the S09 vote's explicit falsifier: the dormant `lorecioni/snake` pointer should fall if a cleaner exact licensed continuous-control candidate is bound. Source decision packet: [S09 queue reclassification](https://github.com/TTaoGaming/hfo-gen-133/blob/agent/gen133-bootstrap-20260730/state/coordination/votes/20260802T213400Z_S09_LORECIONI_SNAKE_QUEUE_RECLASSIFICATION.vote.md).

## Exact candidate and source readback

Observed from primary GitHub sources on `2026-08-03`:

- Repository and exact head: [`davish/snake@13989df94ce227cd6e3ba347e61d3c95ec0279da`](https://github.com/davish/snake/tree/13989df94ce227cd6e3ba347e61d3c95ec0279da).
- Root surface observed: `LICENSE`, `README.md`, `index.html`, `init.js`, `snake.js`; no package manifest, bundled third-party library, image, audio, analytics file, ranking client, or backend client was present in the displayed root.
- Exact blobs read:
  - `LICENSE` blob `ffe85ee0e2942bf425089347b5774821c91ddbc2`
  - `README.md` blob `3248315eb2dfb93f84cd11111ca7a1621fabcfe7`
  - `index.html` blob `dccf9fdf8e49287becd9338a86f005ae75c51747`
  - `init.js` blob `08e446d54ba6055dcdfae8d002ef7b1ef9a07950`
  - `snake.js` blob `c9f82a880b19369f84847bab4121d7b4838f01f8`
- Exact files:
  - [LICENSE](https://github.com/davish/snake/blob/13989df94ce227cd6e3ba347e61d3c95ec0279da/LICENSE)
  - [index.html](https://github.com/davish/snake/blob/13989df94ce227cd6e3ba347e61d3c95ec0279da/index.html)
  - [init.js](https://github.com/davish/snake/blob/13989df94ce227cd6e3ba347e61d3c95ec0279da/init.js)
  - [snake.js](https://github.com/davish/snake/blob/13989df94ce227cd6e3ba347e61d3c95ec0279da/snake.js)

## Supported claims

1. **Substantially smaller static surface than the retired immediate candidate.** The page loads only two local scripts, and the inspected source contains no remote service call, social widget, analytics call, ranking/score endpoint, account flow, or third-party runtime dependency.
2. **Correct interaction class exists.** Arrow-key input sets persistent `add_x/add_y` direction, rejects immediate reversal once length is nonzero, and limits accepted direction changes to one per simulation step through `vals.pressed`.
3. **Simple adapter seam exists.** The game is constructed through `new Snake(canvasId, squareSize, speed, callbacks)` and binds directional input in one `onkeydown` handler on the canvas.
4. **MIT-form reuse terms are present.** The exact `LICENSE` grants use, copy, modify, merge, publish, distribute, sublicense, and sell rights subject to preserving the notice.
5. **The candidate is cheap enough for a bounded falsification probe.** No build system, install step, credential, account, server, or paid dependency is required by the inspected bytes.

## Excluded claims

- No browser checkout, execution, zero-network capture, camera/MediaPipe integration, synthetic-key event test, touch fallback test, accessibility test, mobile test, or deterministic gameplay test was performed.
- This card does not prove the current candidate boots, works on modern browsers, survives long play, is maintained, has demand, is distribution-ready, or should replace the frozen 2048 discrete-action WorkItem.
- This card does not establish that the repository owner and the named copyright holder are the same legal person.
- Static source absence is not a runtime network verdict.

## Blocking defect and license uncertainty

### Startup defect

The constructor stores callbacks as `this.callbacks`, then immediately calls `this.reset()`. The prototype `reset()` method calls unscoped `callbacks.updateScore(0)` rather than `this.callbacks.updateScore(0)`. In the exact demo, `init.js` defines `c`, not a global `callbacks`; ordinary initialization is therefore expected to throw a `ReferenceError` before a valid gameplay verdict. This is a source-level inference requiring browser confirmation.

### License/terms uncertainty

The exact MIT file names copyright holder `dbh937`, while the repository owner is `davish`. The notice is usable as written and must be preserved, but identity/provenance equivalence was not established. No separate asset licenses are needed for the inspected five-file surface because no external asset file was present.

## Comparative disposition

- `lorecioni/snake`: **RETIRE from the dormant continuous-control pointer** if the backlog owner accepts this source-bound comparison; its remote-service, bundled-library, notice, and cleanup burden is dominated.
- `davish/snake`: **REPAIR_BEFORE_ADMIT** as the cleaner dormant candidate; no active WorkItem, producer route, or fitness credit yet.
- Frozen 2048 discrete-action canary: unchanged. Continuous-control semantics are a later interaction class, not a replacement justification.

## Cost and operator burden

- Research direct cost observed: `$0`.
- Operator minutes consumed/requested: `0 / 0`.
- Estimated producer time for a bounded repair specimen: `15–30 minutes` for callback-scope repair, explicit direction API or event-target seam, and retained notice.
- Estimated distinct browser-verifier time: `20–35 minutes` for clean local load, zero-unexpected-network capture, keyboard fallback, reversal/duplicate-input behavior, reset, and exact-digest readback.
- Estimate status: planning estimate only; no implementation or execution occurred.

## Strongest objection

The exact repository is stale and currently appears broken at initialization. A one-line repair can make an old specimen look deceptively cheap while hidden browser-focus, timer, random-fruit, and testability debt remains. A tiny new in-house specimen could be simpler, but creating one would lose the FOSS-reuse test and would require its own provenance and independent verification.

## Falsifier

This `REVISE` falls to **RETIRE** if any of the following holds on exact bytes:

- the startup defect is not the only boot blocker within the bounded repair window;
- a clean browser run emits unexpected network traffic;
- the direction handler cannot be adapted without editing core gameplay broadly;
- retained MIT attribution cannot be accepted by the license reviewer; or
- a cleaner exact permissively licensed candidate is bound with a working boot path and lower verification burden.

It rises to **ADMIT_DORMANT_CONTINUOUS_CONTROL_SPECIMEN** only after an exact repair commit receives a distinct browser-capable nonproducer `STOOD` for boot, zero-unexpected-network, direction/reversal behavior, reset, fallback, and preserved license notice.

## Verifier, consumer, and expiry

- Structural preflight: S04, same-provider nonbinding, weight `0`.
- Binding verifier: distinct browser-capable nonproducer with exact checkout/digest and network capture.
- Immediate consumer: S09 product decision queue, exact decision object `20260802T213400Z_S09_LORECIONI_SNAKE_QUEUE_RECLASSIFICATION.vote.md`.
- Backlog consumer: Spatial App Factory backlog owner; no producer route until a named continuous-control WorkItem exists.
- Fitness credit: `0` until exact WorkItem consumption and ConsumerAck.
- Expiry: `2026-09-01T00:00:00Z`, or immediately on candidate commit/license change, a new continuous-control consumer, or a changed 2048 interaction objective.

## Self-probe and effect receipt

- Expected and observed task ID: `6a526109ba348191b5f23ad3172ad568`; exact match through native task inventory readback.
- Available surfaces used: native task inventory, GitHub repository/commit/file search and exact fetch, public web search, canonical branch create/readback, Slack post after Git readback.
- Unavailable/not used: host checkout, shell, browser execution, network capture, distinct-provider verification, legal review.
- No task mutation, account creation, terms acceptance, outreach, application, purchase, send beyond the required internal Slack pointer, spend, deployment, merge, public release, private-data use, or demand invention occurred.

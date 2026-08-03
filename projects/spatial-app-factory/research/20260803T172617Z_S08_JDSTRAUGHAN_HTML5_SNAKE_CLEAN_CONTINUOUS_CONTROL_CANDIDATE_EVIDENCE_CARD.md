---
schema_id: hfo.gen133.s08.evidence_card.v1
seat: S08_RESEARCH_AND_CANDIDATE_SCOUT
carrier_task_id_expected: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_observed: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_match: true
wip: 1
valid_time_utc: 2026-08-03T17:26:17Z
transaction_time_utc: SEE_GITHUB_COMMIT_METADATA
canonical_repository: TTaoGaming/hfo-gen-133
canonical_branch: agent/gen133-bootstrap-20260730
lane: spatial_foss_candidates_and_licenses
decision: ADMIT
decision_scope: DORMANT_CONTINUOUS_CONTROL_CLEAN_SPECIMEN_CANDIDATE_ONLY
fitness_credit: 0
sealed: false
---

# S08 evidence card — `JDStraughan/html5-snake` as cleaner continuous-control specimen

## Self-probe

- Native task inventory readback exposed exact task ID `6a526109ba348191b5f23ad3172ad568`; it matches the expected S08 carrier ID.
- Available surfaces used: native task readback, authenticated GitHub repository/branch/file/commit read, branch-scoped Git create/readback, public web primary-source read, and authenticated Slack post after Git readback.
- Unavailable or unused: host checkout, browser execution, network capture, recursive local license scanner, legal review, deployment, publication, account action, purchase, send, spend, or task mutation.

## Changed bounded question

The prior S09 queue vote reclassified `lorecioni/snake@875bf961870abfa50c9e2a6564391ea4a85ff42a` as a dormant continuous-control pointer and stated that its classification should fall to full retirement if a cleaner exact licensed continuous-control candidate is bound with materially lower cleanup and verification cost.

**Bounded uncertainty:** Does exact candidate `JDStraughan/html5-snake@4e3049553b316c05c53befab6a51ada88d14d41e` satisfy that cleaner-candidate condition strongly enough to enter the dormant continuous-control specimen queue?

## Exact candidate

- Repository: `JDStraughan/html5-snake`
- Exact commit: `4e3049553b316c05c53befab6a51ada88d14d41e`
- Commit date: `2013-03-07T02:25:46Z`
- Repository status checked `2026-08-03`: public, archived/read-only; GitHub states it was archived `2024-10-22`.
- Exact visible tree at the pinned commit: `README.md`, `game.js`, `index.html`, `page.css`.
- No release or package-manager version exists; the commit digest is the version boundary.

## Dated primary sources

1. GitHub repository and four-file tree, archive state, repository description, and README license, checked `2026-08-03`: <https://github.com/JDStraughan/html5-snake>
2. Exact pinned commit, checked `2026-08-03`: <https://github.com/JDStraughan/html5-snake/commit/4e3049553b316c05c53befab6a51ada88d14d41e>
3. Exact README with full MIT grant and copyright notice: <https://github.com/JDStraughan/html5-snake/blob/4e3049553b316c05c53befab6a51ada88d14d41e/README.md>
4. Exact application shell and startup resources: <https://github.com/JDStraughan/html5-snake/blob/4e3049553b316c05c53befab6a51ada88d14d41e/index.html>
5. Exact control and game loop implementation: <https://github.com/JDStraughan/html5-snake/blob/4e3049553b316c05c53befab6a51ada88d14d41e/game.js>
6. Exact local stylesheet: <https://github.com/JDStraughan/html5-snake/blob/4e3049553b316c05c53befab6a51ada88d14d41e/page.css>
7. Changed queue source, dated `2026-08-02`: `state/coordination/votes/20260802T213400Z_S09_LORECIONI_SNAKE_QUEUE_RECLASSIFICATION.vote.md`.

## Supported claims

- The repository-level README contains the complete MIT permission grant and requires preservation of the copyright and permission notice. Commercial use, modification, distribution, sublicensing, and sale are expressly permitted under that notice-retention condition.
- The exact visible tree is only four text files. No binary art/audio assets, package manifests, vendored libraries, analytics SDKs, ranking/leaderboard code, account surface, or build system are present in those pinned files.
- `index.html` loads local `page.css` and local `game.js`. Its only startup-reachable remote code reference is an obsolete Google Code HTML5 shiv inside an Internet Explorer conditional comment; modern browsers should not request it, but a strict zero-network specimen should delete that block rather than rely on conditional behavior.
- `game.js` implements continuous tick-based movement with four directional states, direct `snake.direction` mutation, opposite-direction rejection, restart, collision, score, and speed progression without a framework dependency.
- Relative to the source-bound `lorecioni/snake` packet, this candidate has materially lower visible cleanup burden: no jQuery, no bundled third-party libraries, no remote social/ranking/play-count surfaces, and no binary asset license inventory.
- The candidate is therefore suitable for a small continuous-control adapter specimen after a bounded input-seam and runtime gate.

## Excluded claims

- No browser run, mobile run, accessibility audit, touch/pointer test, performance test, or network capture was executed.
- No claim is made that the archived 2013 code works unchanged in every current browser or device.
- No claim is made that keyboard `keyCode` is a current portable input contract; it is legacy and should not be the spatial producer seam.
- No claim is made that the four-file GitHub view substitutes for a local object-level checkout, generated-file audit, commit-history authorship review, or legal opinion.
- No demand, buyer, revenue, originality, trademark, app-store acceptance, or product-market-fit claim is supported.
- This card does not authorize implementation, checkout, publication, distribution, deployment, or replacement of the prior queue pointer.

## License and terms uncertainty

- License signal: full MIT text in `README.md`, copyright `(c) 2013 Jason D. Straughan`.
- Required obligation: retain the exact copyright and permission notice in all copies or substantial portions.
- Uncertainty: there is no standalone `LICENSE` file at the pinned tree, and the merge commit includes an external contributor. No CLA, DCO, per-contributor license statement, trademark permission, or chain-of-title review was found in this bounded pass.
- Practical gate: preserve the README MIT text verbatim in any specimen; keep branding generic; require an exact local file/license inventory before any public distribution.
- Repository archival affects maintenance risk, not the text of the existing MIT grant.

## Strongest objection

The direct key handler can accept multiple perpendicular turns between movement ticks. Because opposite-direction rejection compares against the already-mutated `snake.direction`, a rapid `left -> up -> right` sequence can effectively permit a 180-degree reversal before `snake.move()` consumes the next tick. A high-frequency spatial producer would amplify this defect. The adapter must use one pending direction command per movement tick, preserve opposite-direction rejection against the last committed movement direction, and test duplicate/repeated frames.

Secondary objection: the current handler uses legacy numeric `event.keyCode`; synthetic keyboard dispatch must not be the integration seam. Native keyboard fallback and the spatial producer should call one shared guarded direction command.

## Cost and operator-minute estimate

- This research pass: `$0` external spend; `0` operator minutes; no checkout or execution.
- Proposed producer specimen: `30–60 minutes` to remove the obsolete IE shiv, extract a shared guarded direction command, add one-pending-direction-per-tick semantics, and preserve native keyboard fallback.
- Proposed distinct verification: `20–40 minutes` for exact file/license inventory, zero-unexpected-network capture, current desktop/mobile browser smoke run, and deterministic direction/restart/collision traces.
- Expected operator relay: `0 minutes` for internal specimen work; legal/operator review remains required only before public branded distribution.

## Falsifier

This `ADMIT` recommendation falls to `RETIRE` if any of the following occurs:

1. an exact checkout reveals required non-MIT or unattributed material outside the four bound files;
2. the clean specimen cannot achieve zero unexpected network requests after removing the IE shiv;
3. the pending-direction guard and deterministic four-direction traces cannot be produced and independently verified within `60 producer minutes + 40 verifier minutes`;
4. current browser execution exposes a foundational incompatibility that requires framework replacement or broad rewrite; or
5. a still-cleaner exact licensed continuous-control candidate is bound with lower combined producer and verifier burden.

It falls to `REVISE` if the MIT notice can be preserved and runtime works, but touch/accessibility or command semantics require a larger bounded WorkItem.

## Verifier

- Structural preflight: S04 may verify task binding, source pointers, exact candidate digest, decision scope, expiry, effect ceiling, and internal consistency; same-provider weight remains zero.
- Technical/license verifier: a distinct browser-capable nonproducer must inspect the exact checkout, produce the file/license inventory, execute the network baseline, and return digest-bound direction/restart/collision traces.
- This S08 card is research evidence, not independent verification or a quorum.

## Consumer

- Immediate: Spatial App Factory backlog owner and S09 product-decision queue.
- Proposed WorkItem consumer: `SPATIAL_FACTORY_CONTINUOUS_CONTROL_CLEAN_CANDIDATE_GATE_001`.
- Consumption rule: admit only as a dormant clean-specimen candidate. Do not activate producer work until a named continuous-control consumer, exact base digest, allowed paths, acceptance tests, verifier ingress, rollback, and expiry are bound.
- After distinct `STOOD` plus ConsumerAck, the backlog owner may retire the heavier `lorecioni/snake` dormant pointer as dominated. This card does not perform that retirement.

## Expiry

- Evidence expiry: `2026-08-10T17:26:17Z`.
- Immediate invalidation on change to the exact candidate commit/tree/license text, the continuous-control contract, the prior queue classification, or the named consumer.

## Disposition

**ADMIT — DORMANT_CONTINUOUS_CONTROL_CLEAN_SPECIMEN_CANDIDATE_ONLY.**

`JDStraughan/html5-snake@4e3049553b316c05c53befab6a51ada88d14d41e` is a materially cleaner licensed continuous-control candidate than the currently dormant `lorecioni/snake` pointer on visible dependency, asset, network, and verification burden. Admission is narrow: internal candidate queue only, no implementation or distribution authority, fitness credit `0` until a named WorkItem consumes the exact card and later receives distinct verification plus ConsumerAck.

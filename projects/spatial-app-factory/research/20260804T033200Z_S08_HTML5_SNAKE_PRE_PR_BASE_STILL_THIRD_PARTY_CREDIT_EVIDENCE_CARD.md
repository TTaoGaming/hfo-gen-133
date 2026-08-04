---
schema_id: hfo.gen133.s08.evidence_card.v1
task_id_expected: 6a526109ba348191b5f23ad3172ad568
task_id_observed: 6a526109ba348191b5f23ad3172ad568
task_id_match: true
seat: S08_RESEARCH_AND_CANDIDATE_SCOUT
wip: 1
valid_time_utc: 2026-08-04T03:32:00Z
transaction_time_utc: SEE_GITHUB_COMMIT_METADATA
canonical_repository: TTaoGaming/hfo-gen-133
canonical_branch: agent/gen133-bootstrap-20260730
lane: spatial_foss_candidates_and_licenses
question_id: HTML5_SNAKE_KNOWN_THIRD_PARTY_FREE_SOURCE_PIN_001
decision: REVISE
consumer: SPATIAL_FACTORY_HTML5_SNAKE_PENDING_DIRECTION_COMMAND_GATE_001
expiry_utc: 2026-08-11T03:32:00Z
fitness_credit: 0_PENDING_WORKITEM_CONSUMPTION_AND_CONSUMER_ACK
---

# REVISE — `ab188d...` is not a known-third-party-free source pin

## Bounded uncertainty

Does rebinding the Snake successor from merged snapshot `JDStraughan/html5-snake@4e3049553b316c05c53befab6a51ada88d14d41e` to the previously proposed pre-PR base `ab188d1328f1c38ac22ace820f614cac2122e3cf` remove the known contributor-license uncertainty?

## Evidence

1. The repository history has 15 commits. The merged head includes external commit `7d11cf1729e03be40916547d5c5f6a06ed5095e0` and merge commit `4e3049553b316c05c53befab6a51ada88d14d41e`; the proposed base `ab188d...` immediately precedes them. Primary history: <https://github.com/JDStraughan/html5-snake/commits/master>
2. `ab188d...` is authored and committed by `JDStraughan`, but its commit message is **“Updating for firefox - thanks simevidas for fix!”**. Its entire patch changes the `requestAnimationFrame` fallback from unqualified globals to `window.*`, with 3 additions and 5 deletions. Primary commit: <https://github.com/JDStraughan/html5-snake/commit/ab188d1328f1c38ac22ace820f614cac2122e3cf>
3. The parent is exact SHA `e3fe18a85a0555f0540cc0978fbab62822262a91`. That commit adds the complete MIT notice, copyright `2013 Jason D. Straughan`, and explicitly invites fork/fix/pull requests. Primary commit: <https://github.com/JDStraughan/html5-snake/commit/e3fe18a85a0555f0540cc0978fbab62822262a91>
4. Comparing `e3fe18...` to `ab188d...` changes only `game.js`, 8 lines total. Comparing `ab188d...` to merged head changes only `game.js`, 55 lines total. No README, HTML, or CSS bytes are required from either known post-license contributor-related change. Primary compares: <https://github.com/JDStraughan/html5-snake/compare/e3fe18a85a0555f0540cc0978fbab62822262a91...ab188d1328f1c38ac22ace820f614cac2122e3cf> and <https://github.com/JDStraughan/html5-snake/compare/ab188d1328f1c38ac22ace820f614cac2122e3cf...4e3049553b316c05c53befab6a51ada88d14d41e>
5. The initial code commit `b4b427141d34da3dbee3e96ba47cd70e8bcf966e` creates `game.js` and `index.html`; the later `e3fe18...` MIT notice covers the repository snapshot but does not independently prove absence of uncredited or borrowed code. Primary commit: <https://github.com/JDStraughan/html5-snake/commit/b4b427141d34da3dbee3e96ba47cd70e8bcf966e>

## Supported claims

- `ab188d...` avoids the explicit `themightychris` PR bytes but still contains a patch explicitly credited to `simevidas`; calling it a known-third-party-free base would be false green.
- `e3fe18a85a0555f0540cc0978fbab62822262a91` is the latest exact repository snapshot before both known contributor-related code changes and already contains the full MIT notice.
- The omitted Firefox fallback patch is tiny and mechanically reproducible from requirements without copying its post-`e3fe18...` bytes.
- The planned successor already replaces the input and loop control surfaces substantially, so rebasing the specimen source to `e3fe18...` is bounded rather than a new product build.

## Excluded claims

- This is not legal advice and does not establish complete chain of title.
- Owner-authored Git metadata does not prove every pre-`e3fe18...` line was independently authored.
- The commit message does not prove whether `simevidas` supplied copyrightable expression, an idea, a bug report, or separately licensed code.
- No public-distribution permission, browser compatibility, runtime correctness, demand, revenue, or production-readiness claim is admitted.

## Required revision

For any successor intended to preserve a path toward public distribution:

- pin upstream source to `e3fe18a85a0555f0540cc0978fbab62822262a91`, not `ab188d...` or `4e3049...`;
- preserve the complete MIT notice from `README.md`;
- record `ab188d...`, `7d11cf...`, and `4e3049...` as excluded provenance boundaries;
- independently implement the necessary `window.requestAnimationFrame` handling and all current tick-buffer, repeat-filter, and spatial activation-edge requirements from the WorkItem specification, without copying excluded diffs;
- keep distribution status `NOT_STOOD` until a distinct provenance verifier accepts the resulting byte inventory.

## License and terms uncertainty

The visible MIT grant at `e3fe18...` is strong repository-level evidence from the named copyright holder. Remaining uncertainty is provenance, not the wording of the MIT grant: repository history cannot rule out uncredited third-party expression, and the exact legal significance of the `simevidas` attribution is unknown.

## Strongest objection

Rebinding one commit earlier may be unnecessary conservatism because the credited Firefox change is only an obvious three-line namespace qualification and may not contain protectable expression. That is plausible, but the current system has no contributor declaration or legal acceptance; preserving `ab188d...` solely for eight replaceable lines gives little benefit and retains avoidable uncertainty.

## Falsifier

Revise or retire this card if primary evidence proves either: (a) `simevidas` merely reported the bug and supplied no code, with the implementation independently authored by the copyright holder; or (b) the exact contributed patch was licensed under the repository MIT terms by an agreement effective on March 6, 2013.

## Verifier

`S04_STRUCTURAL_PREFLIGHT_VERIFIER` plus one distinct provenance reviewer must confirm that the producer copies only files at `e3fe18...`, preserves the MIT notice, excludes the three later SHAs from copied bytes, and independently authors replacement behavior. A file-level diff and provenance manifest are required; commit-message inspection alone is insufficient.

## Cost estimate

- source-pin and provenance-packet revision: 10–20 producer minutes
- independent replacement of the excluded 8-line fallback behavior: 5–10 producer minutes
- distinct source/diff verification: 15–25 verifier minutes
- paid cost: `$0`
- operator minutes this research run: `0`

## Disposition

`REVISE`

The current internal quarantined specimen may continue under its existing ceiling, but the clean-source route must move from `ab188d...` to `e3fe18...`. Fitness remains zero until the WorkItem consumes this exact revision and receives distinct ConsumerAck.

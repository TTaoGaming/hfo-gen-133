---
schema_id: hfo.gen133.s08.research_evidence_card.v1
card_id: S08_LORECIONI_SNAKE_GOLDEN_APP_DOMINANCE_20260802T213100Z
result: RETIRE
callsign_or_seat: S08_RESEARCH_CANDIDATE_SCOUT
carrier_task_id_expected: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_observed: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_match: true
carrier_identity_claim: DISPOSABLE_SCHEDULED_CARRIER_NOT_LINEAGE
wip: 1
valid_time_utc: 2026-08-02T21:31:00Z
transaction_time_utc: SEE_GITHUB_COMMIT_METADATA
canonical_repository: TTaoGaming/hfo-gen-133
canonical_branch: agent/gen133-bootstrap-20260730
repository_head_observed_before_write: f4823079e402c6e739a4ccba895d453a9276bc04
research_lane: spatial_foss_candidates_and_licenses
bounded_uncertainty: WHETHER_LORECIONI_SNAKE_DOMINATES_FROZEN_2048_AS_A_LOWER_COST_SPATIAL_GOLDEN_APP_CANDIDATE
candidate_repository: lorecioni/snake
candidate_commit: 875bf961870abfa50c9e2a6564391ea4a85ff42a
candidate_default_branch: gh-pages
candidate_commit_date_utc: 2016-04-06T12:43:41Z
candidate_license_surface: README.md_EMBEDDED_MIT_TEXT_NO_STANDALONE_LICENSE_FOUND
candidate_readme_blob: 1e4489139ef8799bdb2e026de991418b16833392
candidate_index_blob: dd5409439cf5d16c02a6acd84f04ee22d961f84a
candidate_settings_blob: 1643e6ac9bd307e5ae2287c43cb7a029b38da342
candidate_engine_blob: SEE_EXACT_GITHUB_READBACK
source_queue_path: state/coordination/receipts/reginleif/20260731T174200Z_CHATGPT_CLOUD_LOOP_ENGINEERING_SPATIAL_FACTORY_CONTROL_PACKET.md
source_queue_requirement: SELECT_ONE_SMALL_EXISTING_BROWSER_APP_WITH_EXACT_REPOSITORY_COMMIT_LICENSE_AND_REUSE_RIGHTS
privacy_class: PUBLIC_PRIMARY_REPOSITORY_SOURCES_ONLY
effect_ceiling: RESEARCH_CARD_AND_SANITIZED_SLACK_POINTER_ONLY
verifier: S04_STRUCTURAL_PREFLIGHT_THEN_DISTINCT_NONPRODUCER_SOURCE_AND_BROWSER_REVIEW
consumer:
  - S09_PRODUCT_DECISION_QUEUE
  - SPATIAL_APP_FACTORY_BACKLOG_OWNER
  - FUTURE_CANDIDATE_SCOUTS
fitness_credit: 0_PENDING_EXACT_WORKITEM_CONSUMPTION
expiry_utc: 2026-09-01T00:00:00Z
sealed: false
---

# S08 evidence card — retire `lorecioni/snake` as a dominated golden-app candidate

## Changed queue evidence

The prior S08 result completed the `agent_runtime_cots_capabilities` lane with the PostgreSQL LISTEN/NOTIFY durability boundary. The explicit five-lane rotation therefore returns to `spatial_foss_candidates_and_licenses`.

The existing 2048 candidate card contains a falsifier: retire or revise 2048 if a smaller already-licensed candidate proves the same directional adapter contract with materially less implementation and verification cost. This card tests exactly one alternative, `lorecioni/snake@875bf961870abfa50c9e2a6564391ea4a85ff42a`, without admitting a second active WorkItem.

## Bounded question

Does this exact Snake repository dominate frozen `gabrielecirulli/2048@478b6ec346e3787f589e4af751378d06ded4cbbc` as a lower-cost, lower-risk branch-only target for the first spatial directional adapter loop?

## Decision

`RETIRE` this exact Snake candidate from the immediate golden-app and fallback queue.

The game exposes four directional controls and has embedded MIT text, but the frozen page is not a small offline/no-backend surface. It loads four bundled third-party libraries, remote social and badge assets, Facebook and Twitter scripts, Google Analytics, and ranking/count/score services at hard-coded external HTTP endpoints. Its main loop is continuous and direction-stateful rather than one accepted input producing one bounded application action. Making it suitable would require a substantial privacy/network/dependency strip before the spatial adapter itself could be tested.

This does not assert that the repository is unusable, insecure, unlawfully licensed, or unsuitable for every future product. It says only that it fails the current dominance test against the already-admitted code-only 2048 directional canary.

## Self-probe

```yaml
expected_task_id: 6a526109ba348191b5f23ad3172ad568
observed_task_id: 6a526109ba348191b5f23ad3172ad568
task_id_match: true
tools_observed:
  github: authenticated_exact_repository_read_branch_scoped_create_and_readback
  slack: authenticated_public_channel_post_available
  web_primary_sources: used_only_for_candidate_discovery_then_repository_bytes_bound_via_github
  shell_or_browser_runtime: unavailable
  task_mutation: not_called
```

## Dated primary sources inspected

Observed `2026-08-02`:

1. `lorecioni/snake` repository metadata: public, not archived, default branch `gh-pages`.
2. Exact candidate commit `875bf961870abfa50c9e2a6564391ea4a85ff42a`, dated `2016-04-06T12:43:41Z`.
3. `README.md`, blob `1e4489139ef8799bdb2e026de991418b16833392`: four arrow-key controls, jQuery dependency disclosure, and full MIT-form text embedded under a sentence that mistakenly says “This version of tetris.”
4. `index.html`, blob `dd5409439cf5d16c02a6acd84f04ee22d961f84a`: loads local jQuery 2.1.4, Modernizr 2.6.2, FastClick 1.0.2, jQuery TouchSwipe, game scripts, remote Facebook/Twitter/Analytics scripts, remote badge/ribbon images, ranking UI, and score-save UI.
5. `js/settings.js`, blob `1643e6ac9bd307e5ae2287c43cb7a029b38da342`: hard-coded cross-origin HTTP endpoints for inserting scores, reading rankings, and incrementing/reading play counts.
6. `js/script.js`, blob `82d062782078224b369ab9df77e5590dc58d69ba`: calls ranking and play-count services on page readiness and uses cross-domain AJAX.
7. `js/engine.js`: maintains a timed continuous loop, directional state, score-saving calls, localStorage username handling, and jQuery-bound input/UI behavior.
8. `js/jquery-2.1.4.min.js`, blob `SEE_GITHUB_READBACK`: file header identifies jQuery 2.1.4 and points to its license.
9. `js/modernizr-2.6.2.min.js`, blob `f65d47974786ee51c258f680bd9be621629244f5`: file header identifies a custom Modernizr 2.6.2 build under MIT and BSD.
10. `js/fastclick.js`, blob `2fda2a9620f07521c3a0b6c5a5e81693b09e9ae0`: header identifies FastClick 1.0.2 and MIT, referring to a `LICENSE.txt` not found during the bounded root-path probe.
11. `js/jquery.touchSwipe.min.js`: bundled minified plugin; no license header was visible in the bounded first-line readback.
12. Root-path fetch for `LICENSE` returned `404`; this proves only that no file exists at that exact path, not that no license or notice file exists elsewhere in the tree.

## Supported claims

- The exact candidate has a four-direction keyboard surface and a browser canvas implementation.
- The exact README carries MIT-form permission text for the project author’s code, subject to retaining the notice.
- The exact entrypoint has runtime dependencies beyond the game core: bundled third-party JavaScript, external social/analytics scripts and images, and hard-coded ranking/count/score services.
- A truthful offline/internal canary would need to remove or isolate those external effects and UI paths before baseline acceptance could be claimed.
- The continuous Snake loop has materially different semantics from the current 2048 contract: a direction changes persistent movement state, and one accepted direction does not correspond to one bounded game transition.
- For the current WIP=1 factory objective, the candidate adds more prerequisite stripping and verification than the existing three-text-file 2048 directional canary.

## Excluded claims

- No malware, vulnerability, privacy-law violation, broken endpoint, exploitability, or current network reachability claim is made.
- No claim that the embedded MIT text is invalid merely because it says “tetris.”
- No claim that any bundled third-party library is non-redistributable or incompatible; the complete exact notice set was not audited.
- No claim that the repository cannot be modernized, stripped, or reused in a later WorkItem.
- No browser execution, recursive-tree audit, package lock, dependency CVE scan, endpoint call, account use, score submission, or network probe occurred.
- No demand, buyer, retention, revenue, or distribution evidence is inferred.
- No second active spatial WorkItem is admitted.

## License and terms uncertainty

The project-level MIT-form text is meaningful permissive evidence for the author’s code, but public or packaged reuse still needs an exact manifest because:

1. there is no standalone root `LICENSE` at the probed path;
2. the README’s “tetris” wording creates a clerical ambiguity that should not be silently corrected in attribution records;
3. bundled jQuery, Modernizr, FastClick, and TouchSwipe files require their own exact notices and versions to be retained or removed;
4. FastClick’s header refers to `LICENSE.txt`, which was not bound during this probe;
5. remote badges, social widgets, analytics, images, ranking data, and score services are separate terms/privacy/provenance surfaces, not cleared by the repository’s MIT text.

The low-risk route would be a clean-room minimal UI around only the game-core code with a complete dependency/notice manifest, but that is producer work and is not authorized by this card.

## Cost and operator-minute estimate

```yaml
direct_research_cost_usd: 0
operator_minutes_required_now: 0
estimated_engineering_minutes_to_strip_remote_social_analytics_ranking_and_score_paths: 60_to_180
estimated_engineering_minutes_to_remove_or_bind_four_third_party_libraries: 45_to_150
estimated_engineering_minutes_to_define_a_deterministic_spatial_direction_contract_for_continuous_motion: 45_to_120
estimated_browser_and_privacy_verification_minutes: 45_to_90
estimated_operator_minutes_for_any_future_public_terms_or_privacy_decision: 10_to_30
paid_service_or_new_credential_required_for_internal_source_review: false
```

## Strongest objection

A stripped Snake core may be a better stress test than 2048 because it exercises continuous interaction, opposite-direction rejection, timing, pause/restart, and sustained hand control. The code is still small enough that removing network/social features could be straightforward, and the four-direction mapping is explicit. Retiring it now could bias the factory toward discrete turn-based apps and miss a reusable continuous-control adapter class.

## Falsifier

Return `REVISE` and reconsider this candidate only if one exact successor packet demonstrates all of the following on the frozen commit within a 60-minute producer timebox:

1. an exact minimal file manifest excluding all remote scripts, images, analytics, rankings, score submission, play counting, and account-like identifiers;
2. a complete retained third-party dependency and license/notice manifest, or removal of those dependencies;
3. baseline browser launch with zero unexpected network requests;
4. deterministic direction tests covering opposite-direction rejection, pause, restart, and no duplicate transition from one accepted gesture edge;
5. native keyboard/touch fallback preserved;
6. total implementation and verification burden no greater than the current 2048 successor route; and
7. distinct browser-capable nonproducer `STOOD` on exact digests.

## Verifier, consumer, expiry

- **Structural verifier:** S04 may confirm exact pointers, task binding, result, expiry, and effect ceiling; same-provider binding weight remains zero.
- **Distinct verifier:** a nonproducer source/browser reviewer must inspect exact bytes before any reversal of `RETIRE`.
- **Consumer:** S09 and the Spatial App Factory backlog owner should remove this exact commit from the immediate candidate/fallback queue. Future scouts should not rediscover it without citing and falsifying this card.
- **Expiry:** `2026-09-01T00:00:00Z`, or immediately if the exact candidate commit, license surface, or current golden-app contract changes.

## Honest flaw

This is a source inspection, not a checkout or runtime test. GitHub search/fetch did not provide a complete recursive tree, exact blob for every inspected minified file in this card body, endpoint liveness, network capture, browser execution, or legal review. The result is therefore a queue-pruning decision for the current factory objective, not a general legal or technical judgment about the project.

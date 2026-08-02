---
schema_id: hfo.gen133.s08.research_evidence_card.v1
card_id: S08_2048_UPSTREAM_LICENSE_INPUT_SEAM_20260802T012843Z
result: ADMIT
callsign_or_seat: S08_RESEARCH_CANDIDATE_SCOUT
carrier_task_id_expected: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_observed: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_match: true
carrier_identity_claim: DISPOSABLE_SCHEDULED_CARRIER_NOT_LINEAGE
controller: operator_direct
wip: 1
valid_time_utc: 2026-08-02T01:28:43Z
transaction_time_utc: SEE_GITHUB_COMMIT_METADATA
canonical_repository: TTaoGaming/hfo-gen-133
canonical_branch: agent/gen133-bootstrap-20260730
repository_head_observed_before_write: 7bbd83c1ec528c0faff67e1c0a2555f62c2921c7
research_lane: spatial_foss_candidates_and_licenses
bounded_uncertainty: WHETHER_EXACT_UPSTREAM_2048_COMMIT_IS_AN_ADMISSIBLE_INTERNAL_GOLDEN_APP_BASE
candidate_repository: gabrielecirulli/2048
candidate_commit: 478b6ec346e3787f589e4af751378d06ded4cbbc
candidate_default_branch: master
candidate_commit_date_utc: 2024-10-24T13:06:19Z
candidate_license_path: LICENSE.txt
candidate_license_blob: b0dbfa4d7526587bcc21a4883222b20805d5c065
candidate_license_spdx_family: MIT
source_queue_path: state/coordination/receipts/reginleif/20260731T174200Z_CHATGPT_CLOUD_LOOP_ENGINEERING_SPATIAL_FACTORY_CONTROL_PACKET.md
source_queue_blob: 0dc9a75e82eb854d4bee8f2be236f9e8e5f06d47
source_queue_requirement: SELECT_ONE_SMALL_EXISTING_BROWSER_APP_WITH_EXACT_REPOSITORY_COMMIT_LICENSE_AND_REUSE_RIGHTS
privacy_class: PUBLIC_PRIMARY_REPOSITORY_SOURCES_AND_SANITIZED_POINTERS_ONLY
effect_ceiling: RESEARCH_CARD_AND_SANITIZED_SLACK_POINTER_ONLY
verifier: S04_STRUCTURAL_PREFLIGHT_THEN_DISTINCT_NONPRODUCER_BROWSER_BUILD_AND_LICENSE_REVIEW
consumer:
  - S02_ADMISSION_PULL_AFTER_CURRENT_WIP_CLEARS
  - S06_CODE_WORK_PACKET_COMPILER
  - S07_BOUNDED_CODE_PATCH_BUILDER
  - SPATIAL_APP_FACTORY_BACKLOG_OWNER
fitness_credit: 0_PENDING_EXACT_WORKITEM_CONSUMPTION
expiry_utc: 2026-08-09T01:28:43Z
sealed: false
---

# S08 evidence card — upstream 2048 as an internal spatial golden-app candidate

## Changed queue evidence

The previous S08 result completed the `agent_runtime_cots_capabilities` lane. The explicit five-lane rotation therefore returns to `spatial_foss_candidates_and_licenses`.

The Gen-133 spatial-factory control packet leaves one bounded candidate question open: select one small existing browser app or prototype with an exact repository, commit, license, and reuse-right ceiling. Search of the current Gen-133 repository found no prior `2048` evidence card. This card evaluates one candidate only and does not admit a second active WorkItem while `SPATIAL_FACTORY_GOLDEN_APP_001` remains WIP=1.

## Bounded question

Is upstream `gabrielecirulli/2048` at exact commit `478b6ec346e3787f589e4af751378d06ded4cbbc` a sufficiently small, licensed, dependency-light browser application for one branch-only spatial-input adaptation experiment, without claiming public-brand clearance, demand, maintained compatibility, or production readiness?

## Decision

`ADMIT` the exact commit as an **internal branch/file/test candidate only**.

The inspected source has an MIT license, a static local-script entrypoint, native keyboard and touch fallbacks, and a narrow input-manager event seam that emits four directional moves. Those properties make it suitable for testing whether the existing spatial adapter can drive a real app without changing the game core.

This is not approval to publish, deploy, list in an app store, use the upstream project's “official” branding, or claim that a spatial 2048 derivative has buyer demand. Any later public distribution requires a separate branding, provenance, accessibility, browser-compatibility, and distribution decision.

## Self-probe

```yaml
expected_task_id: 6a526109ba348191b5f23ad3172ad568
observed_task_id: 6a526109ba348191b5f23ad3172ad568
task_id_match: true
tools_observed:
  github: authenticated_repository_read_and_branch_scoped_contents_write
  slack: authenticated_channel_read_write
  web_primary_sources: available_not_needed_for_repository_bound_question
  native_task_inventory: read_only
  shell_or_host_runtime: unavailable
  task_mutation: not_called
```

## Dated primary sources inspected

Observed `2026-08-02`:

1. GitHub repository metadata for `gabrielecirulli/2048`: public, not archived, default branch `master`.
2. Exact candidate commit `478b6ec346e3787f589e4af751378d06ded4cbbc`, dated `2024-10-24T13:06:19Z`.
3. `LICENSE.txt` at the candidate commit, blob `b0dbfa4d7526587bcc21a4883222b20805d5c065`: MIT license, copyright 2014 Gabriele Cirulli.
4. `README.md` at the candidate commit, blob `c947a03d4c63822e2ae79fd26de00fc4565e1292`: describes the project as a clone of 1024, based on another 2048 implementation, indirectly inspired by Threes, and calls its site/app the official version.
5. `index.html` at the candidate commit, blob `0da0ee0e1b142d886c9752fe9477058d3b4b5e83`: static markup loading local CSS and JavaScript files, with no external runtime script, authentication, backend, payment, or account dependency visible in the inspected entrypoint.
6. `js/keyboard_input_manager.js` at the candidate commit, blob `ca01b3ce8995a5a20ac50219712d1ef95297ed99`: maps arrow, Vim, and WASD keys plus touch swipes into four `move` directions through a local `on`/`emit` event seam; restart and keep-playing controls retain click/touch handlers.
7. `js/application.js` at the candidate commit, blob `2c1108e757a0e49af7b9ee48dcc45bd8e61cb806`: injects `KeyboardInputManager` into `GameManager` at startup.
8. Repository searches for package manifests and common test-framework terms returned no match. This is a limited search result, not an exhaustive tree or dependency audit.

## Supported claims

- The exact inspected commit carries an MIT code license permitting use, modification, distribution, sublicensing, and sale, subject to preserving the copyright and permission notice in copies or substantial portions.
- The inspected entrypoint is a small static browser surface that loads local scripts and exposes native keyboard and touch interaction without an observed account, backend, payment, or external-runtime-script dependency.
- The input manager has a narrow event boundary: four directional actions are normalized to integer directions and emitted through `move` callbacks.
- A spatial adapter can plausibly target the input-manager seam or equivalent keyboard/touch behavior while preserving the application core and native fallback paths.
- The candidate is exact enough for a branch-only experiment: repository, commit, relevant blobs, license notice, and initial adaptation seam are bound.

## Excluded claims

- No trademark, trade-dress, app-store identity, title, logo, screenshot, or “official” branding right is established by the MIT code license.
- No legal conclusion is made about the upstream clone lineage, conceptual similarity to 1024 or Threes, or public commercial distribution of a derivative.
- No claim that every asset or historical contribution has independently audited provenance beyond the repository-level license notice.
- No claim of current maintenance, modern-browser compatibility, accessibility conformance, mobile reliability, security hardening, performance, or production readiness.
- No claim that the repository has no dependencies or network behavior outside the inspected entrypoint and files.
- No claim that the repository has a working automated test harness; none was identified in the bounded inspection.
- No demand, buyer, download, revenue, retention, or distribution advantage is inferred from the existence or historical popularity of 2048.
- No public deployment, publication, fork push, app-store submission, or marketplace listing is authorized.

## License, terms, and provenance uncertainty

The MIT notice is adequate for an internal code adaptation provided the notice is preserved. Before any public artifact:

1. preserve `LICENSE.txt` and the original copyright notice;
2. rebrand the derivative and remove upstream “official” language;
3. audit icons, screenshots, fonts, copied text, and other non-code assets separately;
4. review the clone/provenance chain and third-party marks rather than treating the code license as brand clearance;
5. bind the exact public-distribution terms and target platform rules in a separate WorkItem.

This wake accepted no terms, created no account, forked no repository, and published nothing.

## Candidate adaptation boundary

A consuming WorkItem should freeze the exact upstream commit and limit changes to a dedicated branch or mirrored specimen. The preferred seam is additive:

- retain existing keyboard and touch handlers;
- translate spatial gesture state to one of four directional moves;
- avoid modifying grid, tile, score, persistence, or game-state logic;
- add a deterministic direction-mapping test, a native-fallback regression test, and a browser smoke test;
- preserve the MIT notice in the candidate artifact;
- label all execution honestly if no real browser/runtime is available.

## Cost and operator-minute estimate

```yaml
direct_research_cost_usd: 0
operator_minutes_required_now: 0
estimated_engineering_minutes_to_mirror_and_preserve_license: 10_to_20
estimated_engineering_minutes_for_minimal_spatial_adapter: 45_to_120
estimated_engineering_minutes_for_deterministic_and_browser_smoke_tests: 45_to_120
estimated_operator_minutes_for_public_brand_or_legal_decision_if_later_pursued: 10_to_30
custom_game_core_avoided_estimate: MATERIAL_BUT_UNMEASURED
paid_service_or_new_credential_required_for_internal_probe: false
```

## Strongest objection

The code is a legacy global-script application using dated input APIs such as `event.which`, MSPointer detection, and direct `preventDefault` calls. A clean tiny demo could be easier to test than modernizing this surface, and the project's clone lineage and “official” branding create public-release risk. The candidate is worthwhile only if the adapter remains additive and the first exact browser/test pass stays within the bounded timebox.

## Falsifier

Return `REVISE` or `RETIRE` for this candidate if any of the following is observed on the exact checkout:

1. baseline execution requires an unbound external service, account, paid dependency, or unavailable build chain;
2. any included asset needed for the candidate lacks usable provenance or conflicts with the repository license notice;
3. spatial control requires changing game-state logic rather than the input boundary;
4. keyboard or touch fallback regresses;
5. deterministic direction tests or the target-browser smoke test cannot be made to pass within the bounded work packet;
6. the derivative cannot be clearly rebranded without retaining disputed “official” identity or protected marks;
7. a smaller already-licensed candidate proves the same adapter contract with materially less implementation and verification cost.

## Verifier, consumer, expiry

- **Structural verifier:** S04 may verify exact pointers, blobs, license-notice preservation, authority, and expiry; same-provider binding weight remains zero.
- **Distinct verifier:** Sigrun/P4 or another authorized nonproducer browser/build runtime must inspect the exact candidate bytes and run the acceptance tests before any `STOOD` claim.
- **Consumer:** S02 may admit a new exact candidate WorkItem only after the current spatial WIP clears. S06/S07 may then compile or execute the bounded branch/file/test packet. The Spatial App Factory backlog owner must explicitly accept, revise, or reject the resulting reusable adapter/app specimen.
- **Expiry:** `2026-08-09T01:28:43Z`. Recheck the upstream commit state, license path, and any target-platform terms after expiry.

## Honest flaw

This is a repository-source inspection, not a checkout or runtime test. The connector did not expose a complete recursive tree, dependency graph, browser execution, asset provenance audit, or legal review. Search misses are not proof of absence. The card therefore admits only one internal branch/test candidate and earns zero fitness until an exact WorkItem consumes it and a distinct verifier tests the frozen bytes.

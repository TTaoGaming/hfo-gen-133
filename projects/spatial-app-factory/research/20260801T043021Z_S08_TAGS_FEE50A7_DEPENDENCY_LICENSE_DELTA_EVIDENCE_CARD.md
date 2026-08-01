---
schema_id: hfo.gen133.s08.research_evidence_card.v1
card_id: S08_TAGS_FEE50A7_DEPENDENCY_LICENSE_DELTA_20260801T043021Z
result: ADMIT
callsign_or_seat: S08_RESEARCH_CANDIDATE_SCOUT
carrier_task_id: 6a526109ba348191b5f23ad3172ad568
carrier_identity_claim: DISPOSABLE_SCHEDULED_CARRIER_NOT_LINEAGE
controller: operator_direct
wip: 1
valid_time_utc: 2026-08-01T04:30:21Z
transaction_time_utc: SEE_GITHUB_COMMIT_METADATA
canonical_repository: TTaoGaming/hfo-gen-133
canonical_branch: agent/gen133-bootstrap-20260730
work_item_id: SPATIAL_FACTORY_GOLDEN_APP_001
research_lane: spatial_foss_candidates_and_licenses
question_change_basis: TAGS_target_advanced_from_1271e253_to_fee50a7_with_three_added_files
privacy_class: SANITIZED_INTERNAL_NO_PRIVATE_SOURCE_BODY
expiry_utc: 2026-08-08T04:30:21Z
expiry_conditions:
  - target_branch_head_changes
  - package_or_lockfile_changes
  - public_distribution_requested
  - contrary_provenance_or_license_evidence
verifier: Sigrun/P4_APEX_FALSIFICATION_or_other_distinct_provider_nonproducer
consumers:
  - Olrun/Claude-Dispatch
  - S09_conditional_requeue_reducer
  - next_S06_executor_packet_for_SPATIAL_FACTORY_GOLDEN_APP_001
sealed: false
---

# S08 evidence card — TAGS `fee50a7` dependency and license delta

## Bounded uncertainty

Did the exact three-commit change from `TTaoGaming/TAGS@1271e25306fe8ef8baea32704cf022435703d498` to `fee50a70188b510695e8e5fad2ebadc6cba0535a` introduce any external runtime/package dependency or new license term that invalidates the prior **internal-only, no-publication** admission for `SPATIAL_FACTORY_GOLDEN_APP_001`?

## Decision

`ADMIT` the exact `fee50a7` branch as a dependency-free candidate for one renewed **internal branch/file/test-only** executor packet after a host proves authenticated checkout capability.

This card does **not** clear public release. The branch still lacks a root `LICENSE` file, and the exact copyright/provenance chain is not bound. Public distribution, marketplace submission, deployment, merge, or marketing remains `REVISE` pending a separate rights/provenance gate.

## Self-probe

```yaml
expected_task_id: 6a526109ba348191b5f23ad3172ad568
observed_task_id: 6a526109ba348191b5f23ad3172ad568
task_id_match: true
tools_observed:
  github_connector: read_write
  slack_connector: read_write
  web_research: available
  native_shell_or_browser_runtime: unavailable
```

## Exact candidate and delta

```yaml
repository: TTaoGaming/TAGS
visibility: private
base_commit: 1271e25306fe8ef8baea32704cf022435703d498
target_commit: fee50a70188b510695e8e5fad2ebadc6cba0535a
compare_status: ahead
commits_ahead: 3
changed_files:
  - path: prototypes/spatial-input-adapter.js
    status: added
    lines_added: 174
    blob: c90a715c72735f0c04d60c91cd9c9afb0f2ddec4
  - path: tests/fab-prototype-smoke.test.mjs
    status: added
    lines_added: 14
    blob: 2f0e2795fe81910e82b9dc9ff697b86ff5e16231
  - path: tests/spatial-input-adapter.test.mjs
    status: added
    lines_added: 76
    blob: 9416a2e34c331ab46dd2f04c8d8664dbc0088405
package_json_blob: ad608a51a2cf60b89e5c1f69b305dfb391c46365
root_license_at_target: NOT_FOUND_404
```

## Primary-source findings — observed 2026-08-01

1. GitHub compare readback shows the target is exactly three commits ahead and changes only the adapter plus two tests. `package.json`, lockfiles, and the FAB HTML were not changed in this delta.
2. The adapter is a self-contained classic JavaScript module. Exact-content inspection found no `import`, external `require`, URL, fetch, WebSocket, media-device, package, font, image, or network dependency.
3. The two tests import only Node built-ins (`node:test`, `node:assert/strict`, `node:fs/promises`) and the relative local adapter/FAB files. They add no third-party package requirement.
4. The unchanged `package.json` still declares `"license": "MIT"` and only `eslint` as a development dependency. npm's official package metadata documentation treats this field as an SPDX license declaration, while separately supporting `SEE LICENSE IN <filename>` when the license text is stored in a named top-level file: https://docs.npmjs.com/cli/configuring-npm/package-json/#license
5. GitHub's official licensing guidance says a repository without a license is governed by default copyright rules and recommends a root license file as best practice: https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository
6. GitHub's Choose a License reference characterizes MIT distribution as conditioned on preserving the license and copyright notice: https://choosealicense.com/licenses/
7. Exact connector readback at `fee50a7` returned `404` for root `LICENSE`. Therefore the metadata says MIT, but the inspected branch still does not bind the exact license text, copyright holder, year, or provenance notice needed for a clean public-release packet.

## Supported claims

- The `1271e253 -> fee50a7` delta introduces no new external runtime or npm dependency.
- A clean host with Git and Node can inspect and run the added Node tests without package installation, subject to checkout access.
- The prior internal-only candidate admission is not invalidated by dependency drift.
- The next executor packet may pin `fee50a7` without silently adding a package-install step.

## Excluded claims

- No test, browser, build, static server, or integration command was executed by this carrier.
- This card does not prove the smoke test passes; the compare shows `fab-prototype.html` was not changed in this delta.
- It does not prove authorship, clean-room provenance, copyright ownership, patent clearance, trademark clearance, or legal sufficiency of the package metadata.
- It does not authorize merge, release, hosting, marketplace submission, publication, customer use, or commercial distribution.
- It does not prove that every repository file is dependency-free; the conclusion is limited to the exact three-file delta and unchanged package metadata.

## License and terms uncertainty

The `package.json` MIT identifier is affirmative metadata, so this is not classified as a proven "no license" repository. However, the missing root license text and missing exact copyright/provenance notice make public-distribution compliance and GitHub license detection uncertain. The safe gate is:

```yaml
internal_owner_controlled_test: ADMIT
public_or_third_party_distribution: REVISE
minimum_release_gate:
  - exact license text committed at a pinned revision
  - copyright holder and year bound
  - provenance review for FAB and adapter source
  - independent rights review
```

This is an engineering evidence classification, not legal advice.

## Cost and operator burden

```yaml
direct_cost_usd_observed: 0
operator_minutes_used_observed: 0
operator_minutes_removed_measured: 0
potential_manual_review_avoided_estimate: 5_to_10_minutes
estimate_status: HEURISTIC_NOT_FITNESS_CREDIT
credentials_required_for_next_execution: existing_authorized_private_repo_checkout
package_install_required_by_delta: false
```

## Strongest objection

A dependency-free delta can still contain copied or jointly authored code. The absence of imports and URLs says nothing about provenance. Because the repository lacks the exact MIT text and copyright notice at the pinned head, this card cannot convert an internal experiment into a redistributable FOSS product.

## Falsifier

Change this result to `REVISE` or `RETIRE` if any of the following is shown:

- target head differs from `fee50a7`;
- a package/lockfile or external asset is required to reproduce the accepted test path;
- the adapter or tests contain third-party code under incompatible or unknown terms;
- a conflicting license or authorship claim appears;
- public distribution is requested before exact license text and provenance are bound;
- a clean authorized host cannot run the pinned Node tests without package installation.

## Consumer action

S09/Olrun may treat dependency-install uncertainty as closed for the exact `fee50a7` internal requeue decision. Requeue remains conditional on a fresh authenticated-host capability proof, fresh WorkItem/claim/executor packet, and unchanged no-merge/no-publication ceiling. A separate release-rights WorkItem is required before any public surface.

## Honest flaw

This carrier inspected exact Git blobs and official licensing guidance but did not execute the code, inspect full repository history, identify every contributor, run a software-composition/provenance scanner, or obtain legal review. The operator-minute estimate is unmeasured and receives zero fitness credit until independently validated and consumed.

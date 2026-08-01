---
schema_id: hfo.gen133.s08.research_evidence_card.v1
card_id: S08_TAGS_1F0C0A7_LICENSE_DEPENDENCY_DELTA_20260801T102908Z
result: ADMIT
callsign_or_seat: S08_RESEARCH_CANDIDATE_SCOUT
carrier_task_id_expected: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_observed_from_runtime_instruction: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_match: true
carrier_identity_claim: DISPOSABLE_SCHEDULED_CARRIER_NOT_LINEAGE
controller: operator_direct
wip: 1
valid_time_utc: 2026-08-01T10:29:08Z
transaction_time_utc: SEE_GITHUB_COMMIT_METADATA
canonical_repository: TTaoGaming/hfo-gen-133
canonical_branch: agent/gen133-bootstrap-20260730
work_item_id: SPATIAL_FACTORY_GOLDEN_APP_001
research_lane: spatial_foss_candidates_and_licenses
question_change_basis: TAGS_target_advanced_from_fee50a70188b510695e8e5fad2ebadc6cba0535a_to_1f0c0a7831db6f4476a703856855ff7ccc4f454b_after_prior_license_card
privacy_class: SANITIZED_INTERNAL_NO_PRIVATE_SOURCE_BODY
expiry_utc: 2026-08-08T10:29:08Z
expiry_conditions:
  - target_branch_head_changes
  - package_manifest_or_lockfile_changes
  - public_distribution_requested
  - contrary_provenance_or_license_evidence
verifier: Sigrun/P4_APEX_FALSIFICATION_or_other_distinct_provider_nonproducer
consumers:
  - Olrun/Claude-Dispatch
  - S09_advisory_reducer
  - next_S06_executor_packet_for_SPATIAL_FACTORY_GOLDEN_APP_001
sealed: false
---

# S08 evidence card — TAGS `1f0c0a7` dependency and license delta

## Bounded uncertainty

Did the exact target advance from `TTaoGaming/TAGS@fee50a70188b510695e8e5fad2ebadc6cba0535a` to `1f0c0a7831db6f4476a703856855ff7ccc4f454b` introduce an external package/runtime dependency or a changed license term that invalidates the prior **internal-only, branch/file/test** admission for `SPATIAL_FACTORY_GOLDEN_APP_001`?

## Decision

`ADMIT` the exact `1f0c0a7831db6f4476a703856855ff7ccc4f454b` candidate for internal branch/file/test continuation without a package-install step.

Public release remains outside this admission. The branch still has no root `LICENSE` file, the precise copyright/provenance chain is not bound, and the patch has no distinct-provider verdict or ConsumerAck.

## Self-probe

```yaml
expected_task_id: 6a526109ba348191b5f23ad3172ad568
observed_task_id: 6a526109ba348191b5f23ad3172ad568
task_id_match: true
tools_observed:
  github_connector: authenticated_read_write
  slack_connector: authenticated_read_write
  web_research: available
  native_shell_or_browser_runtime: unavailable
```

## Exact candidate and measured delta — observed 2026-08-01

```yaml
repository: TTaoGaming/TAGS
visibility: private
base_commit: fee50a70188b510695e8e5fad2ebadc6cba0535a
target_commit: 1f0c0a7831db6f4476a703856855ff7ccc4f454b
compare_status: ahead
commits_ahead: 2
changed_files:
  - path: prototypes/spatial-input-adapter.js
    status: modified
    additions: 73
    deletions: 8
    base_blob: c90a715c72735f0c04d60c91cd9c9afb0f2ddec4
    target_blob: ca327ea46049f499d0afe1be4f9632ee086f2637
  - path: tests/spatial-input-adapter.test.mjs
    status: modified
    additions: 103
    deletions: 0
    base_blob: 9416a2e34c331ab46dd2f04c8d8664dbc0088405
    target_blob: 2e523f5c373203ae4f5e0f1a48a52d1570f0682a
package_json_blob_at_target: ad608a51a2cf60b89e5c1f69b305dfb391c46365
package_license_field: MIT
root_LICENSE_at_target: NOT_FOUND_404
```

## Dated primary sources

1. GitHub compare API readback for the exact base and target, observed 2026-08-01: `https://github.com/TTaoGaming/TAGS/compare/fee50a70188b510695e8e5fad2ebadc6cba0535a...1f0c0a7831db6f4476a703856855ff7ccc4f454b`.
2. Exact target adapter blob, observed 2026-08-01: `https://github.com/TTaoGaming/TAGS/blob/1f0c0a7831db6f4476a703856855ff7ccc4f454b/prototypes/spatial-input-adapter.js`.
3. Exact target test blob, observed 2026-08-01: `https://github.com/TTaoGaming/TAGS/blob/1f0c0a7831db6f4476a703856855ff7ccc4f454b/tests/spatial-input-adapter.test.mjs`.
4. Exact target package metadata, observed 2026-08-01: `https://github.com/TTaoGaming/TAGS/blob/1f0c0a7831db6f4476a703856855ff7ccc4f454b/package.json`.
5. npm official `package.json` license contract, retrieved 2026-08-01: `https://docs.npmjs.com/cli/configuring-npm/package-json/#license`.
6. GitHub official repository licensing guidance, retrieved 2026-08-01: `https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository`.

## Measured findings

1. The target is exactly two commits ahead and changes only the adapter and its deterministic Node test. No package manifest, lockfile, HTML page, asset, font, or license file changed in this delta.
2. Exact adapter inspection found no `import`, external `require`, package name, URL, `fetch`, WebSocket, media-device call, font, image, or network dependency. It uses platform globals plus injected seams.
3. Exact test inspection found only Node built-ins (`node:assert/strict`, `node:test`) and the relative local adapter import. The delta adds no third-party test dependency.
4. `package.json` remains at blob `ad608a51a2cf60b89e5c1f69b305dfb391c46365` with `"license": "MIT"` and only `eslint` as a development dependency. npm documents the license field as an SPDX identifier declaration for common licenses.
5. Root `LICENSE` still returns `404`. GitHub recommends a root license file and warns that absent a license, default copyright rules apply. The package metadata is affirmative but does not bind the exact MIT text, notice, holder, year, or provenance for a release packet.

## Supported claims

- The exact `fee50a7 -> 1f0c0a7` delta introduces no new external runtime or npm dependency.
- A clean authorized host can inspect and run the adapter test path using Node built-ins and local files only; package installation is not required by this delta.
- The prior internal-only dependency admission is not invalidated by the target advance.
- A follow-on executor or verifier packet may pin `1f0c0a7` without silently adding an install step.

## Excluded claims

- S08 did not execute Node tests, browser tests, a build, a static server, accessibility checks, or cross-browser behavior.
- This card does not upgrade producer labels into an independent `STOOD | FELL` verdict.
- It does not prove authorship, clean-room provenance, copyright ownership, patent clearance, trademark clearance, or legal sufficiency.
- It does not authorize merge, deployment, hosting, marketplace submission, publication, customer use, or commercial distribution.
- It does not prove the full repository is dependency-free; the conclusion is limited to the exact two-file delta and unchanged package metadata.

## License and terms uncertainty

```yaml
internal_owner_controlled_branch_file_test: ADMIT
public_or_third_party_distribution: REVISE
minimum_public_release_gate:
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

The absence of imports and package changes does not prove clean provenance. A self-contained file can still contain copied or jointly authored code. The missing root license text and exact notice prevent this internal dependency result from becoming a public-release clearance.

## Falsifier

Change this result to `REVISE` or `RETIRE` if any of the following is shown:

- branch head differs from `1f0c0a7831db6f4476a703856855ff7ccc4f454b`;
- a package, lockfile, external asset, or network resource is required to reproduce the accepted test path;
- either changed file contains third-party code under incompatible or unknown terms;
- a conflicting license or authorship claim appears;
- public distribution is requested before exact license text and provenance are bound;
- a clean authorized host cannot run the pinned Node tests without package installation.

## Consumer action

S09 and Olrun may treat dependency-install drift as closed for the exact internal-only `1f0c0a7` continuation decision. The next S06 packet or distinct verifier should pin the exact target SHA and preserve the no-merge/no-publication ceiling. Public release requires a separate rights/provenance WorkItem.

## Honest flaw

This carrier inspected exact GitHub blobs and official licensing contracts but did not execute code, inspect full repository history, identify every contributor, run a software-composition/provenance scanner, or obtain legal review. The operator-minute estimate is unmeasured and earns zero fitness credit until consumed by a WorkItem.

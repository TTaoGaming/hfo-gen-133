---
schema_id: hfo.gen133.s08.research_evidence_card.v1
card_id: S08_TAGS_E0E3125_LICENSE_DEPENDENCY_DELTA_20260801T162603Z
result: ADMIT
callsign_or_seat: S08_RESEARCH_CANDIDATE_SCOUT
carrier_task_id_expected: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_observed: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_match: true
carrier_identity_claim: DISPOSABLE_SCHEDULED_CARRIER_NOT_LINEAGE
controller: operator_direct
wip: 1
valid_time_utc: 2026-08-01T16:26:03Z
transaction_time_utc: SEE_GITHUB_COMMIT_METADATA
canonical_repository: TTaoGaming/hfo-gen-133
canonical_branch: agent/gen133-bootstrap-20260730
repository_head_observed_before_write: fd73ff01cf68126d81cc674466f930837dff3a94
work_item_id: SPATIAL_FACTORY_GOLDEN_APP_001
research_lane: spatial_foss_candidates_and_licenses
question_change_basis: producer_candidate_advanced_from_1f0c0a7831db6f4476a703856855ff7ccc4f454b_to_e0e3125e1ef6bb33e189c91b485ec341f2d3cd52
privacy_class: PUBLIC_OFFICIAL_DOCS_AND_SANITIZED_PRIVATE_REPOSITORY_METADATA_ONLY
effect_ceiling: FILE_AND_SANITIZED_SLACK_POINTER_ONLY
expiry_utc: 2026-08-03T16:26:03Z
verifier: Sigrun/P4_APEX_FALSIFICATION_or_other_distinct_nonproducer
consumer: S03_or_next_exact_SPATIAL_FACTORY_GOLDEN_APP_001_WorkItem
fitness_credit: ZERO_UNTIL_EXACT_WORKITEM_CONSUMER_ACK
binding_weight: 0
sealed: false
---

# S08 evidence card — TAGS `e0e3125` dependency and license delta

## Changed question

The prior S08 wake completed `agent_runtime_cots_capabilities`, so the explicit lane rotation returns to `spatial_foss_candidates_and_licenses`. The newest changed spatial candidate is the preserved producer branch at `TTaoGaming/TAGS@e0e3125e1ef6bb33e189c91b485ec341f2d3cd52`, four commits beyond the last license-reviewed target `1f0c0a7831db6f4476a703856855ff7ccc4f454b`.

**Bounded uncertainty:** did the exact `1f0c0a7 -> e0e3125` producer delta add any external runtime/package dependency or changed license term that invalidates the earlier internal-only branch/file/test admission?

## Decision

`ADMIT` the exact `e0e3125e1ef6bb33e189c91b485ec341f2d3cd52` bytes for **internal preservation and a future exact verification WorkItem only**.

This does not revive the expired claim or verifier route, grant `STOOD`, authorize merge/publication, or clear public distribution. The source branch remains unverified by a distinct provider, and repository-level license/provenance remains unresolved.

## Self-probe

```yaml
expected_task_id: 6a526109ba348191b5f23ad3172ad568
observed_task_id: 6a526109ba348191b5f23ad3172ad568
task_id_match: true
tools_observed:
  native_tasks_inventory: read
  github_connector: authenticated_read_write_and_exact_file_readback
  slack_public_channel: authenticated_read_write
  web_primary_sources: read
  shell_or_browser_runtime: not_used
  private_bodies_externalized: false
  task_mutation: not_called
```

## Exact candidate and dated primary sources

Observed `2026-08-01`:

```yaml
repository: TTaoGaming/TAGS
branch: agent/spatial-golden-app-001-20260731
branch_head_readback: e0e3125e1ef6bb33e189c91b485ec341f2d3cd52
branch_head_compare_to_exact_sha: identical
base_commit: 1f0c0a7831db6f4476a703856855ff7ccc4f454b
final_commit: e0e3125e1ef6bb33e189c91b485ec341f2d3cd52
commits_ahead: 4
changed_paths_exact:
  - prototypes/spatial-input-adapter.js
  - tests/spatial-input-adapter.test.mjs
adapter_blob: 579c9551225f0974ed93564b6ad8bfb1abf72cf3
test_blob: 60ab9eb973db6e55824765e0f34005c6afb87ed9
package_json_blob: ad608a51a2cf60b89e5c1f69b305dfb391c46365
package_license_field: MIT
root_LICENSE: NOT_FOUND_404
```

1. Exact base-to-final compare: https://github.com/TTaoGaming/TAGS/compare/1f0c0a7831db6f4476a703856855ff7ccc4f454b...e0e3125e1ef6bb33e189c91b485ec341f2d3cd52
2. Exact final commit, created `2026-08-01T12:35:26Z`: https://github.com/TTaoGaming/TAGS/commit/e0e3125e1ef6bb33e189c91b485ec341f2d3cd52
3. Exact adapter blob: https://github.com/TTaoGaming/TAGS/blob/e0e3125e1ef6bb33e189c91b485ec341f2d3cd52/prototypes/spatial-input-adapter.js
4. Exact test blob: https://github.com/TTaoGaming/TAGS/blob/e0e3125e1ef6bb33e189c91b485ec341f2d3cd52/tests/spatial-input-adapter.test.mjs
5. Exact package metadata: https://github.com/TTaoGaming/TAGS/blob/e0e3125e1ef6bb33e189c91b485ec341f2d3cd52/package.json
6. GitHub official repository-licensing guidance, retrieved `2026-08-01`: https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository
7. npm official `package.json` license contract, retrieved `2026-08-01`: https://docs.npmjs.com/cli/configuring-npm/package-json/#license

## Measured findings

- The exact branch still resolves to `e0e3125`; it has not advanced beyond the producer return.
- The four-commit delta changes only the adapter and its deterministic Node test. No package manifest, lockfile, HTML, asset, font, or license file changed.
- Exact adapter readback contains no module import, external `require`, package name, URL, `fetch`, WebSocket, media-device call, or bundled asset reference. It uses platform globals and injected seams.
- Exact test readback imports only `node:assert/strict`, `node:test`, and the relative local adapter file.
- `package.json` is unchanged at blob `ad608a51a2cf60b89e5c1f69b305dfb391c46365`; it declares `MIT` and only `eslint` as a development dependency.
- A root `LICENSE` file remains absent at the exact final commit. GitHub documents that without a license default copyright rules apply, while npm documents the `license` field as the package's SPDX declaration. Those facts do not by themselves bind exact notice text, holder, year, or provenance for public release.

## Supported claims

- The exact `1f0c0a7 -> e0e3125` delta introduces no new external runtime or npm dependency.
- No package-install step is introduced by this producer delta for the bounded adapter/test path.
- The prior internal-only dependency admission is not invalidated by these exact bytes.
- A future verifier packet may pin `e0e3125` without silently broadening the changed-path or dependency surface.

## Excluded claims

- No claim that the expired claim, route, or lease is revived.
- No `PASS`, `STOOD`, browser-correctness, accessibility, integration, deployment, user, revenue, or ConsumerAck claim.
- No claim of original authorship, clean provenance, patent/trademark clearance, or legal sufficiency.
- No claim that the repository is generally dependency-free; this result is limited to the exact two-file delta and unchanged metadata.
- No merge, publication, distribution, deployment, account action, terms acceptance, or live execution occurred.

## License and terms uncertainty

```yaml
internal_owner_controlled_preservation_and_future_verification: ADMIT
public_or_third_party_distribution: REVISE
minimum_public_release_gate:
  - exact_license_text_at_a_pinned_revision
  - copyright_holder_and_year
  - provenance_review_for_FAB_and_adapter_source
  - independent_rights_review
```

This is an engineering evidence classification, not legal advice.

## Cost and operator burden

```yaml
direct_research_cost_usd: 0
operator_minutes_used: 0
operator_relay_minutes: 0
estimated_future_manual_recheck_avoided: 5_to_10_minutes
estimate_status: HEURISTIC_NOT_FITNESS_CREDIT
credentials_required_for_future_verification: existing_authorized_private_repo_checkout
package_install_required_by_delta: false
```

## Strongest objection

This card is useful only at the dependency/license-delta ceiling. A self-contained file can still contain copied or jointly authored material, and the missing root license text remains a public-release blocker. More importantly, the current workflow failure is missing distinct verification and ConsumerAck, not dependency uncertainty; another research card must not be mistaken for progress on that blocked edge.

## Falsifier

Change this result to `REVISE` or `RETIRE` if any one is shown:

1. branch head differs from `e0e3125e1ef6bb33e189c91b485ec341f2d3cd52`;
2. a package, lockfile, external asset, or network resource is required for the accepted adapter/test path;
3. either changed file contains third-party code under incompatible or unknown terms;
4. a conflicting license or authorship claim appears;
5. public distribution is requested before exact license text and provenance are bound;
6. a clean authorized checkout cannot execute the pinned Node test without package installation.

## Verifier, consumer, expiry, and honest flaw

- **Verifier:** Sigrun/P4 or another distinct nonproducer must independently challenge the exact bytes and claim ceiling.
- **Consumer:** S03 or a newly claimed `SPATIAL_FACTORY_GOLDEN_APP_001` WorkItem may consume this blob only as dependency/license input to a fresh, unexpired verifier route.
- **Expiry:** `2026-08-03T16:26:03Z`, or immediately on branch/package/license/provenance change.
- **Credit:** zero until a named WorkItem records exact consumption or evidence-backed rejection.

Honest flaw: this carrier inspected exact GitHub bytes and current official documentation but did not run code, inspect the full repository history, identify every contributor, perform software-composition/provenance scanning, or obtain legal review. The producer's Node results remain producer evidence, not an independent verdict. Same-provider advisory binding weight is `0`.

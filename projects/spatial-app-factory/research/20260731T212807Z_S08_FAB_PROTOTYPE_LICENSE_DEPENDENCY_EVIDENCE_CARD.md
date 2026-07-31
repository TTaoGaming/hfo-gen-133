---
schema_id: hfo.gen133.s08.research_evidence_card.v1
card_id: S08_FAB_PROTOTYPE_LICENSE_DEPENDENCY_20260731T212807Z
result: ADMIT
callsign_or_seat: S08_RESEARCH_CANDIDATE_SCOUT
carrier_task_id: 6a526109ba348191b5f23ad3172ad568
carrier_identity_claim: DISPOSABLE_SCHEDULED_CARRIER_NOT_LINEAGE
controller: operator_direct
wip: 1
valid_time_utc: 2026-07-31T21:28:07Z
transaction_time_utc: SEE_GITHUB_COMMIT_METADATA
canonical_repository: TTaoGaming/hfo-gen-133
canonical_branch: agent/gen133-bootstrap-20260730
work_item_id: SPATIAL_FACTORY_GOLDEN_APP_001
research_lane: spatial_foss_candidates_and_licenses
privacy_class: SANITIZED_INTERNAL_NO_PRIVATE_SOURCE_BODY
expiry_utc: 2026-08-03T17:57:17Z
verifier: Sigrun/P4_APEX_FALSIFICATION_or_other_distinct_provider_nonproducer
consumers:
  - Olrun/Claude-Dispatch
  - S06_task_6a57972b9df081918680ce67c4ecb197
  - S07_task_6a506f6dc5c08191b95f1707d7f00c2d
sealed: false
---

# S08 evidence card — pinned FAB prototype license and dependency seam

## Bounded question

Can the exact pinned `TTaoGaming/TAGS` FAB prototype be used for the internal branch/file/test-only `SPATIAL_FACTORY_GOLDEN_APP_001` experiment without an external runtime dependency or immediate license blocker?

## Decision

`ADMIT` for the current **internal, non-public branch/file/test experiment only**.

Do not interpret this card as permission to merge, publish, distribute, deploy, market, or represent the prototype as third-party-rights-cleared. Public redistribution remains gated on a repository-level license/provenance repair and independent review.

## Self-probe

```yaml
expected_task_id: 6a526109ba348191b5f23ad3172ad568
observed_task_id: 6a526109ba348191b5f23ad3172ad568
task_id_match: true
tools_observed:
  native_tasks_inventory: read
  github: read_write
  slack: read_write
  connected_private_repository_read: available
  web_or_public_github_research: available
  shell_or_browser_runtime: unavailable
```

## Exact candidate

```yaml
repository: TTaoGaming/TAGS
visibility: private
commit: 1271e25306fe8ef8baea32704cf022435703d498
prototype:
  path: prototypes/fab-prototype.html
  blob: 63e5bfe5a158781c207c5636537172bdbc838023
package_metadata:
  path: package.json
  blob: ad608a51a2cf60b89e5c1f69b305dfb391c46365
executor_packet:
  commit: 7b5a36f6c4790ed99f80c71b4c8fc57816db8bdc
  path: projects/spatial-app-factory/dispatch/20260731T212211Z_SPATIAL_FACTORY_GOLDEN_APP_001_S06_EXECUTOR.packet.yaml
```

## Primary-source findings — observed 2026-07-31

1. The pinned `package.json` declares `"license": "MIT"`, identifies the author as `Tommy`, and lists only `eslint` as a development dependency. It does not declare a runtime dependency required by the FAB page.
2. The exact pinned FAB page is a single HTML document with inline styling and script. Exact-content probes found no `<script src`, `src=`, CSS `url(`, `fetch(`, `WebSocket`, `mediaDevices`, `AudioContext`, or `navigator.` reference in that file.
3. A root `LICENSE` file was not present at the pinned commit through the exact GitHub contents path checked. The package metadata's MIT label therefore lacks a repository-level license text and copyright notice in the inspected surface.
4. The S06 packet's proposed adapter and tests can remain dependency-free: one new JavaScript adapter, Node built-in test runner, Python static server, and `curl`; no package install or lockfile modification is required.

## Supported claims

- The pinned FAB page is suitable for a **self-contained internal input-adapter experiment**.
- No external runtime script, network fetch, bundled image/font URL, camera API, audio API, or WebSocket dependency was detected in the exact pinned page.
- Adding the adapter under the S06 frozen path/test ceiling does not require accepting third-party terms, creating an account, or installing an application dependency.
- The current experiment may proceed without publication because its effect ceiling is isolated branch/file/test evidence only.

## Excluded claims

- This card does not prove original authorship of every line in the prototype.
- It does not prove that package metadata alone forms a complete MIT license grant for redistribution.
- It does not prove trademark, patent, music, icon, emoji-rendering, design, or other third-party rights clearance.
- It does not prove runtime correctness, accessibility, privacy, browser compatibility, build success, or test success.
- It does not authorize merge, deployment, release, marketplace listing, public hosting, or customer use.

## License and terms uncertainty

`package.json` says MIT, but no root `LICENSE` file was found in the exact pinned revision. For an internal owner-controlled experiment with no publication, this is not an immediate execution blocker. Before any public distribution or merge into a public factory product, add or identify the exact license text, copyright holder, year, and prototype provenance; then rerun an independent license/source scan.

This is an engineering evidence classification, not legal advice.

## Cost and operator burden

```yaml
direct_cost_usd: 0
operator_minutes_used_for_this_research: 0
estimated_operator_minutes_removed: 10_to_20
operator_minutes_required_before_internal_test: 0
operator_minutes_required_before_public_distribution: 5_to_15_for_rights_attestation_or_review
```

## Strongest objection

The prototype is private and self-contained, but a metadata field saying `MIT` is weaker than an exact license file plus provenance. If copied third-party code or assets exist inline, the absence of external URLs would not reveal that. The main remaining risk is **provenance**, not runtime dependency.

## Falsifier

Change this result to `REVISE` or `RETIRE` if any of the following is shown against the pinned bytes:

- a conflicting license or author claim;
- copied third-party code or assets without compatible rights;
- a hidden runtime dependency needed for the accepted behavior;
- a required modification outside the S06 allowed paths;
- public distribution is requested before license text and provenance are bound;
- the clean host test cannot reproduce the adapter behavior while preserving native fallback.

## Consumer action

Olrun/S06 may proceed with the exact internal executor packet at commit `7b5a36f6c4790ed99f80c71b4c8fc57816db8bdc`. The producer return must keep publication and merge forbidden. Before any later public-release gate, create a separate rights/provenance WorkItem rather than silently upgrading this evidence card.

## Honest flaw

This carrier inspected repository bytes and metadata but did not execute the page, run a formal software-composition scanner, inspect the full repository history, or verify authorship through an independent legal/provenance source. Exact host build/test evidence and distinct-provider verification remain required.

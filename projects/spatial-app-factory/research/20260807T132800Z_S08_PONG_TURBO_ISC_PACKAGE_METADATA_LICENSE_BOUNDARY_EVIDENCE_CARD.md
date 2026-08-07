---
schema_id: hfo.gen133.s08.research_evidence_card.v1
callsign: S08_RESEARCH_AND_CANDIDATE_SCOUT
expected_task_id: 6a526109ba348191b5f23ad3172ad568
observed_task_id: 6a526109ba348191b5f23ad3172ad568
task_id_match: true
wip: 1
queue_source: state/coordination/experiments/cots_connector_x13/CURRENT.md
queue_version_observed: 160
queue_transition: PRIOR_COTS_CAMPAIGN_CLOSED_START_NEW_CANDIDATE_PHASE1
lane: spatial_foss_candidates_and_licenses
question: "Can p-m-p/Pong-Turbo at exact ref 19dbdb6d0423b8b8bbc48616c09ed5215ca5d5cc be admitted as a clean ISC/permissive spatial-factory fork candidate when ISC is declared in package.json but no root LICENSE or LICENSE.md was found?"
decision: REVISE
candidate: p-m-p/Pong-Turbo
candidate_ref: 19dbdb6d0423b8b8bbc48616c09ed5215ca5d5cc
candidate_version: package.json_1.0.0
package_json_blob: 8717e9781e626af4101bffd8ebcd08e56470c869
readme_blob: 75ffeae9365f92da31ca1c39f3ad409998f88410
license_state: ISC_SPDX_IDENTIFIER_DECLARED_IN_PACKAGE_METADATA;FULL_LICENSE_TEXT_AND_PROJECT_COPYRIGHT_NOTICE_NOT_BOUND_AT_ROOT;ASSET_IP_UNAUDITED
consumer: SPATIAL_FACTORY_FOSS_CANDIDATE_ADMISSION_LICENSE_GATE
work_item_id: NOT_ASSIGNED
consumer_ack: false
fitness_credit: 0
paid_cost_usd_observed: 0
operator_minutes_removed_measured: 0
research_minutes_estimate: 8_to_15
verifier_minutes_estimate: 20_to_40
valid_time_utc: 2026-08-07T13:28:00Z
expiry_utc: 2026-09-06T13:28:00Z
---

# S08 evidence card — Pong-Turbo ISC package-metadata license boundary

## Bounded uncertainty

Can `p-m-p/Pong-Turbo` at exact observed ref `19dbdb6d0423b8b8bbc48616c09ed5215ca5d5cc` be admitted as a clean permissive-license fork candidate solely because `package.json` declares `"license": "ISC"`, when this pass found no root `LICENSE` or `LICENSE.md` file and no repository-wide copyright notice?

## Decision

`REVISE`.

Keep the repository as a **provisional permissive candidate**, but do not represent it as `ISC_CLEARED_FOR_REDISTRIBUTION` yet. The exact `package.json` declares the standardized SPDX identifier `ISC`; npm's current package metadata contract explicitly accepts SPDX expressions such as `"license": "ISC"`. That is meaningful evidence of licensing intent. However, the canonical ISC license requires the copyright notice and permission notice to appear in all copies. This pass could not bind an exact project copyright notice or committed full license text at the observed ref, so downstream redistribution compliance cannot yet be made reproducible from repository bytes alone.

This is a provenance/packaging gate, not a conclusion that the package metadata grant is invalid.

## Exact candidate evidence — observed 2026-08-07

1. `p-m-p/Pong-Turbo@19dbdb6d0423b8b8bbc48616c09ed5215ca5d5cc`, `package.json`, blob `8717e9781e626af4101bffd8ebcd08e56470c869`:
   - version `1.0.0`;
   - `private: true`;
   - `license: ISC`;
   - Vite/Vitest/ESLint/Wrangler development surface.
   - https://github.com/p-m-p/Pong-Turbo/blob/19dbdb6d0423b8b8bbc48616c09ed5215ca5d5cc/package.json
2. Same exact ref, `README.md`, blob `75ffeae9365f92da31ca1c39f3ad409998f88410`:
   - browser-based canvas game;
   - keyboard, mouse/touch drag, scroll-wheel, and gamepad controls;
   - responsive canvas with a 600x400 virtual coordinate space;
   - standard `pnpm install`, `pnpm dev`, `pnpm build`, `pnpm preview` workflow.
   - https://github.com/p-m-p/Pong-Turbo/blob/19dbdb6d0423b8b8bbc48616c09ed5215ca5d5cc/README.md
3. Root `LICENSE` fetch at that exact ref: `404 Not Found` during this pass.
4. Root `LICENSE.md` fetch at that exact ref: `404 Not Found` during this pass.
5. Repository-scoped search for `Copyright`: no result returned during this pass.

## Primary/current external contract evidence — observed 2026-08-07

1. npm `package.json` documentation says the `license` property uses SPDX license-expression syntax and gives `"license": "ISC"` as a valid example. If a custom/unidentified license is used, npm instead recommends `SEE LICENSE IN <filename>` with a top-level file.
   - https://docs.npmjs.com/cli/configuring-npm/package-json/
2. SPDX License List identifies `ISC` as the ISC License and OSI-approved. Its canonical text grants use/copy/modify/distribution subject to retaining the copyright notice and permission notice in all copies.
   - https://spdx.org/licenses/ISC
3. GitHub's licensing guidance says open-source licensing is what grants reuse/change/distribution rights and recommends making licensing clear in a repository, commonly through a root license file or README notice.
   - https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository

## Supported claims

- The exact observed `package.json` declares `ISC` using a recognized SPDX identifier.
- npm currently treats `"license": "ISC"` as valid package metadata.
- ISC is a permissive, OSI-approved license identifier in SPDX.
- The canonical ISC terms require retention of a copyright notice and the permission notice in distributed copies.
- The exact observed repository is technically attractive for a spatial-input experiment because it already supports keyboard, mouse/touch, and gamepad input over a browser canvas.
- No root `LICENSE` or `LICENSE.md` was found by exact-path fetch in this pass, and a repository-scoped `Copyright` search returned no result.
- Therefore candidate exploration is supportable, while a clean redistribution/compliance claim is not yet bound.

## Excluded claims

- No claim that the `package.json` license declaration is legally invalid or ineffective.
- No claim that absence of a root license file alone means the repository is unlicensed.
- No complete file-by-file, dependency, history, contributor, or asset license audit was performed.
- No trademark, trade-dress, character-art, title, or other IP clearance was performed for the README's Pac-Man, Space Invaders, Ball Blast, ghost, alien, or mothership references.
- No claim that all visual/audio/code assets are original or redistributable.
- No maintainability, security, performance, demand, monetization, customer, or browser-compatibility verdict is made.
- No WorkItem has consumed this candidate and no operator minutes have been measured as removed.

## License / terms uncertainty

`ISC_SPDX_IDENTIFIER_DECLARED_IN_PACKAGE_METADATA; EXACT_PROJECT_COPYRIGHT_NOTICE_NOT_FOUND_IN_THIS_PASS; FULL_COMMITTED_LICENSE_TEXT_NOT_FOUND_AT_ROOT_LICENSE_OR_LICENSE_MD; CONTRIBUTOR_AND_ASSET_PROVENANCE_UNAUDITED; TRADEMARK_AND_TRADE_DRESS_UNAUDITED`.

The repository's `private: true` package flag is an npm publication safeguard, not evidence that GitHub source redistribution is forbidden; this card makes no publication-policy claim beyond the exact metadata observed.

## Strongest objection

A separate `LICENSE` file is not inherently required for a valid SPDX package declaration: npm explicitly accepts `"license": "ISC"`, so the package metadata may already express the owner's intended license. That objection is valid. The reason for `REVISE` is narrower: the ISC redistribution condition requires preservation of a copyright notice plus the permission notice, and this pass did not bind the exact project notice needed for reproducible downstream packaging.

## Falsifier

Move toward `ADMIT` for the license-provenance gate if an authoritative owner-authored exact-ref source binds the project to ISC with the applicable copyright holder/notice, or a later repository revision adds an unambiguous license file/README notice and a bounded asset/dependency review finds no material incompatible content.

Move toward `RETIRE` from a permissive-distribution lane if exact-ref history or asset/dependency review finds material proprietary, noncommercial, no-derivatives, incompatible, or uncleared content that cannot be removed or replaced.

## Verifier

`S04_STRUCTURAL_PREFLIGHT_PLUS_DISTINCT_EXACT_REF_OWNER_LICENSE_NOTICE_AND_ASSET_PROVENANCE_REVIEW_BEFORE_ANY_DISTRIBUTION_WORKITEM`.

Structural verification should bind the exact candidate SHA, package blob, README blob, any owner-authored license/copyright notice, dependency/asset inventory, and the distribution subset actually proposed. Same-provider structural preflight remains nonbinding for legal provenance.

## Consumer

`SPATIAL_FACTORY_FOSS_CANDIDATE_ADMISSION_LICENSE_GATE`.

No named WorkItem or ConsumerAck currently consumes this card. Fitness credit remains `0` until an exact WorkItem binds and consumes the Git pointer.

## Cost / operator-minute estimate

- Direct spend observed: `$0`.
- Measured operator minutes removed: `0`.
- Bounded scout estimate: `8–15 min`.
- Exact-ref notice + dependency/asset provenance verification estimate: `20–40 min` before any distribution WorkItem.

## Expiry

`2026-09-06T13:28:00Z`, or immediately on a repository/license/asset provenance change.

## Effect ceiling

Evidence only. No task mutation, account creation, terms acceptance, outreach, application, purchase, send, spend, deployment, merge, publication, private-data use, or demand invention.
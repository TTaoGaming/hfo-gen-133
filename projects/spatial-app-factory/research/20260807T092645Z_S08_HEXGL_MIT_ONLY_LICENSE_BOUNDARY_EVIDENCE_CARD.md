---
schema_id: hfo.gen133.s08.research_evidence_card.v1
callsign: S08_RESEARCH_AND_CANDIDATE_SCOUT
expected_task_id: 6a526109ba348191b5f23ad3172ad568
wip: 1
lane: spatial_foss_candidates_and_licenses
question: Is BKcore/HexGL at current master safely describable as an MIT-only candidate for the spatial app factory?
decision: REVISE
candidate: BKcore/HexGL
candidate_ref: 6addc95a2fce3bf05f4d751823cc054c61a16d68
repository_default_branch: master
root_license_blob: ccdfb1cae9a9ad9b248d830d70d52e7f3456634c
readme_blob: 8c5c63e4174386407d15053109c3d76c996d03af
known_exception_file: libs/Editor_files/jhashtable.js
known_exception_blob: e7947d3fea37323e88b72eb1eae97142a9889a5f
consumer: SPATIAL_FACTORY_FOSS_CANDIDATE_ADMISSION_LICENSE_GATE
work_item_id: NOT_ASSIGNED
consumer_ack: false
fitness_credit: 0
operator_minutes_removed_measured: 0
paid_cost_usd_observed: 0
research_minutes_estimate: 10_to_18
full_license_asset_bom_minutes_estimate: 30_to_60
valid_time_utc: 2026-08-07T09:26:45Z
expiry_utc: 2026-09-06T09:26:45Z
---

# S08 evidence card — HexGL is not an MIT-only dependency surface

## Bounded uncertainty

Can `BKcore/HexGL` at exact ref `6addc95a2fce3bf05f4d751823cc054c61a16d68` be admitted to a permissive FOSS candidate shortlist under the simple label `MIT-only`?

## Decision

`REVISE`.

The root project license is MIT and the README says HexGL code and resources are MIT **unless a file specifies otherwise**. That is enough for an initial permissive-project signal, but not enough for an `MIT-only` bill-of-materials claim. A concrete bundled counterexample exists: `libs/Editor_files/jhashtable.js` carries Apache License 2.0 terms in-file. Apache-2.0 is still permissive, so this does **not** retire HexGL; it means the candidate must be represented as a mixed-license surface and must receive a dependency/asset BOM before distribution.

A second provenance boundary exists in `css/BebasNeue-webfont.svg`: the vendored font metadata names Ryoichi Tsunekawa and says “All rights reserved.” Current upstream Dharma Type material says the 2010 Bebas Neue line was released under SIL Open Font License 1.1, but this pass did not cryptographically bind the exact vendored SVG to a specific upstream font release/checksum. Treat the vendored font license as `LIKELY_OFL_1_1_BUT_UNBOUND_TO_EXACT_VENDORED_BYTES` until separately verified.

## Primary/current evidence

1. GitHub repository `BKcore/HexGL`, current observed master ref `6addc95a2fce3bf05f4d751823cc054c61a16d68`, retrieved 2026-08-07: https://github.com/BKcore/HexGL
2. Root `LICENSE` at that exact ref is MIT, blob `ccdfb1cae9a9ad9b248d830d70d52e7f3456634c`: https://github.com/BKcore/HexGL/blob/6addc95a2fce3bf05f4d751823cc054c61a16d68/LICENSE
3. Root `README.md`, blob `8c5c63e4174386407d15053109c3d76c996d03af`, says code/resources are MIT unless specified in-file: https://github.com/BKcore/HexGL/blob/6addc95a2fce3bf05f4d751823cc054c61a16d68/README.md
4. Bundled `libs/Editor_files/jhashtable.js`, blob `e7947d3fea37323e88b72eb1eae97142a9889a5f`, explicitly carries Apache-2.0 terms: https://github.com/BKcore/HexGL/blob/6addc95a2fce3bf05f4d751823cc054c61a16d68/libs/Editor_files/jhashtable.js
5. Bundled `css/BebasNeue-webfont.svg`, blob `df90beb838913393abe545b6ce22e100a4dfbeb5`, identifies Ryoichi Tsunekawa and 2010 copyright: https://github.com/BKcore/HexGL/blob/6addc95a2fce3bf05f4d751823cc054c61a16d68/css/BebasNeue-webfont.svg
6. Dharma Type current project material, retrieved 2026-08-07, states Bebas Neue version 1.xxx (2010) was licensed under SIL OFL 1.1: https://bebaskai.com/

## Supported claims

- The project root license at the observed ref is MIT.
- The README explicitly allows file-specific license exceptions.
- At least one bundled source file is Apache-2.0, so `MIT-only` is false for the repository as a whole.
- The discovered MIT + Apache-2.0 mix is not, by itself, a reason to reject the candidate from a permissive-license shortlist.
- The vendored Bebas Neue font needs exact-byte/version provenance before a distribution claim is made.

## Excluded claims

- No claim that every file or asset has been audited.
- No claim that all textures, audio, geometries, fonts, or third-party libraries are cleared for commercial redistribution.
- No trademark/trade-dress/IP clearance for the HexGL name, logos, vehicle/track art, or other creative assets.
- No dependency-vulnerability, maintainability, browser-compatibility, monetization, or demand verdict.
- No legal opinion that MIT + Apache-2.0 + probable OFL-1.1 is the complete license set.

## License/terms uncertainty

`ROOT_MIT_CONFIRMED; APACHE_2_0_EXCEPTION_CONFIRMED; BEBAS_NEUE_OFL_1_1_LINEAGE_SUPPORTED_BUT_EXACT_VENDORED_FONT_BYTES_NOT_BOUND; REMAINING_ASSET_AND_DEPENDENCY_LICENSES_UNAUDITED`.

## Strongest objection

The root README already says “unless specified in the file,” so finding one Apache-2.0 file may be ordinary and harmless. Correct. The material point is not that Apache-2.0 is problematic; it is that downstream automation must not compress the candidate into `MIT-only` and then skip attribution/notice and asset-provenance work.

## Falsifier

This card should be revised or retired if a complete exact-ref license/asset BOM proves every distributed material file is legally covered by MIT alone, or if a newer authoritative repository ref changes the relevant license terms. Conversely, the candidate should be retired from a permissive-distribution lane if a material bundled asset is found under a noncommercial, no-derivatives, proprietary, or otherwise incompatible redistribution term that cannot be removed/replaced.

## Verifier

`S04_STRUCTURAL_PREFLIGHT_PLUS_DISTINCT_EXACT_REF_LICENSE_AND_ASSET_PROVENANCE_BOM_REVIEW_BEFORE_ANY_DISTRIBUTION_WORKITEM`.

## Consumer

`SPATIAL_FACTORY_FOSS_CANDIDATE_ADMISSION_LICENSE_GATE`.

No named WorkItem or ConsumerAck currently consumes this card; fitness credit remains `0` until that happens.

## Cost / operator-minute estimate

- Direct spend observed: `$0`.
- Measured operator minutes removed: `0`.
- This bounded scout: `10–18 min` estimated.
- Exact-ref full license + asset BOM before distribution: `30–60 min` estimated, depending on third-party asset count.

## Expiry

`2026-09-06T09:26:45Z`, or earlier on repository/license change.

## Effect ceiling

Evidence only. No task mutation, account creation, terms acceptance, outreach, application, purchase, send, spend, deployment, merge, publication, private-data use, or demand invention.

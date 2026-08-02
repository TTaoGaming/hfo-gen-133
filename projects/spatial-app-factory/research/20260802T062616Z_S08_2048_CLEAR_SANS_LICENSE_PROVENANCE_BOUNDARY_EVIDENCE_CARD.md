---
schema_id: hfo.gen133.s08.evidence_card.v1
seat: S08_RESEARCH_AND_CANDIDATE_SCOUT
carrier_task_id_expected: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_observed: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_match: true
wip: 1
valid_time_utc: 2026-08-02T06:26:16Z
transaction_time_utc: SEE_GITHUB_COMMIT_METADATA
lane: spatial_foss_candidates_and_licenses
question: Does exact upstream 2048 carry bundled Clear Sans font assets whose license/provenance is not established by its root MIT notice, and does that block the current code-only directional canary?
decision: REVISE
fitness_credit: 0
fitness_condition: exact WorkItem ConsumerAck only
canonical_repository: TTaoGaming/hfo-gen-133
canonical_branch: agent/gen133-bootstrap-20260730
sealed: false
---

# S08 evidence card — 2048 Clear Sans license/provenance boundary

## Decision

**REVISE — keep the current code-only directional canary; prohibit any full upstream asset import until the Clear Sans font bytes receive a separate provenance-and-license gate.**

The exact current TAGS canary is not blocked: its producer return reports exactly three added text files (`directional-bridge.js`, its test, and `THIRD_PARTY_NOTICE.md`), no copied upstream implementation body, and no font/image asset import. The notice accurately limits itself to the public move contract and reproduces the upstream MIT notice.

A later packaging step that copies the complete upstream 2048 site must not treat the root MIT file as sufficient evidence for every bundled asset.

## Exact candidate and changed consumer

- Upstream candidate: `gabrielecirulli/2048@478b6ec346e3787f589e4af751378d06ded4cbbc`
- Root license blob: `LICENSE.txt@b0dbfa4d7526587bcc21a4883222b20805d5c065`
- Imported font-reference CSS blob: `style/fonts/clear-sans.css@de2811db8b5ef12fe4f243fab6c4809363562c29`
- Sample bundled font blob: `style/fonts/ClearSans-Regular-webfont.woff@9d58858d809454e026cdebc3e766154ee8727582`
- Current consumer WorkItem: `SPATIAL_FACTORY_GOLDEN_APP_001_2048_DIRECTIONAL_BRIDGE_001`
- Current TAGS producer branch/final commit: `agent/spatial-2048-directional-bridge-repair-20260802T0424Z@a3b636a7ecaab5afa1932ec92559c7c454904039`
- Current notice blob: `prototypes/2048-spatial-canary/THIRD_PARTY_NOTICE.md@cc79232d0621ccd201153ff94f0b9597668b6ec1`

## Dated primary evidence — accessed 2026-08-02

1. Exact upstream `index.html` loads `style/main.css`, a favicon, and Apple startup/touch images:  
   https://github.com/gabrielecirulli/2048/blob/478b6ec346e3787f589e4af751378d06ded4cbbc/index.html
2. Exact `style/main.css` imports `fonts/clear-sans.css`:  
   https://github.com/gabrielecirulli/2048/blob/478b6ec346e3787f589e4af751378d06ded4cbbc/style/main.css
3. Exact `clear-sans.css` references bundled Clear Sans EOT, SVG, and WOFF binaries in light, regular, and bold weights:  
   https://github.com/gabrielecirulli/2048/blob/478b6ec346e3787f589e4af751378d06ded4cbbc/style/fonts/clear-sans.css
4. Exact upstream root license is MIT, copyright Gabriele Cirulli, and requires preservation of its notice:  
   https://github.com/gabrielecirulli/2048/blob/478b6ec346e3787f589e4af751378d06ded4cbbc/LICENSE.txt
5. Intel's official archived `intel/clear-sans` repository identifies Clear Sans as freely usable for private/commercial use and distribution under Apache-2.0; the repository was archived 2023-01-07:  
   https://github.com/intel/clear-sans
6. Intel's Apache-2.0 text requires redistributors to provide a copy of the license and retain applicable notices; it does not grant trademark rights:  
   https://github.com/intel/clear-sans/blob/main/LICENSE.txt
7. Exact current producer return proves only three added text files under the canary path and explicitly says no upstream implementation body was copied:  
   https://github.com/TTaoGaming/hfo-gen-133/blob/agent/gen133-bootstrap-20260730/state/coordination/receipts/chatgpt_runtime/seat-07/20260802T042745Z_SPATIAL_FACTORY_GOLDEN_APP_001_2048_DIRECTIONAL_BRIDGE_PATCH_RETURNED.yaml
8. Exact current notice describes only the move contract and includes the upstream MIT notice:  
   https://github.com/TTaoGaming/TAGS/blob/a3b636a7ecaab5afa1932ec92559c7c454904039/prototypes/2048-spatial-canary/THIRD_PARTY_NOTICE.md

## Supported claims

- The frozen 2048 site references and bundles files named as Clear Sans webfonts.
- Intel's official Clear Sans project is Apache-2.0, not MIT.
- The frozen 2048 repository's searchable license text exposes the project MIT notice but does not establish an exact provenance map from its bundled font blobs to an Intel Clear Sans release.
- The sampled frozen 2048 WOFF blob (`9d58858d...`) is not byte-identical to Intel `clear-sans` main's `WOFF/ClearSans-Regular.woff` blob (`f4aacf79...`). This proves only non-identity to that current Intel blob, not different authorship or license.
- The current three-file TAGS canary imports no font binaries or full upstream page assets, so this font issue does not block its existing internal branch/file/test claim ceiling.

## Excluded claims

- No claim that the frozen font bytes are unauthorized, infringing, or non-redistributable.
- No claim that the root MIT license legally overrides, includes, or excludes third-party font rights.
- No claim that the sampled blob mismatch disproves Clear Sans provenance; versioning or webfont conversion could explain it.
- No full-site, image, icon, branding, trademark, publication, store, buyer, or revenue clearance.
- No legal advice and no distribution approval.

## License / terms uncertainty

**Material but bounded.** The filenames and CSS attribution strongly identify Clear Sans, while Intel publishes Clear Sans under Apache-2.0. However, the exact frozen 2048 font blob was not matched to an exact Intel release/version, and no complete asset provenance manifest was found. Therefore the safe packaging rule is either:

1. remove the bundled font files and use a system-font stack; or
2. bind every copied font blob to an exact upstream source/version and ship the applicable Apache-2.0 license/notices in addition to the 2048 MIT notice.

The current code-only canary needs neither remediation because it copied no font asset.

## Cost / operator-minute estimate

- Incremental research/spend: **$0**
- Operator minutes consumed: **0**
- Current canary remediation: **0 minutes**
- Future full-asset packaging gate: **5–10 operator minutes** to choose `REMOVE_FONTS` or approve a verified third-party notice manifest after a distinct verifier maps exact blobs.

## Strongest objection

The upstream README says "2048 is licensed under MIT," so a consumer may reasonably treat the whole repository as MIT-licensed. That is not enough to prove third-party font provenance or to erase an applicable Apache-2.0 notice obligation; conversely, the available evidence is also insufficient to declare the repository noncompliant. The correct outcome is a narrow packaging gate, not retirement of the code-only canary.

## Falsifier

Retire this revision if a distinct verifier produces either:

- an exact blob-to-release mapping for every copied `style/fonts/*` file plus the complete applicable license/NOTICE set; or
- a packaging manifest proving that no upstream font/image binary enters the deliverable.

Any future change to the frozen upstream commit, candidate asset set, or canary changed-path set also falsifies this card's scope.

## Verifier

- Primary: distinct nonproducer license/provenance verifier
- Structural: S04 confirms that any packaging WorkItem contains either `REMOVE_FONTS` or exact blob/license bindings
- Runtime/browser verification remains separate and cannot verify license provenance

## Consumer

- Immediate: `SPATIAL_FACTORY_GOLDEN_APP_001_2048_DIRECTIONAL_BRIDGE_001` — consume only as `CURRENT_CODE_ONLY_CANARY_UNAFFECTED`
- Future: the first exact WorkItem that imports or packages upstream 2048 HTML/CSS/font/image assets — consume as `FULL_ASSET_IMPORT_LICENSE_GATE_REQUIRED`

## Expiry

`2026-09-01T00:00:00Z`, or immediately on any upstream commit/asset-set change, whichever occurs first.

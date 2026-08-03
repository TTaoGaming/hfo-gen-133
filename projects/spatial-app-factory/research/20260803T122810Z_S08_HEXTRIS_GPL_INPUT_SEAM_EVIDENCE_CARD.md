---
schema_id: hfo.gen133.s08.evidence_card.v1
card_id: S08_HEXTRIS_GPL_INPUT_SEAM_20260803T122810Z
task_id: 6a526109ba348191b5f23ad3172ad568
seat: S08
wip: 1
lane: spatial_foss_candidates_and_licenses
question: Can pinned Hextris serve as a low-cost spatial-input specimen without false claims about licensing or adapter readiness?
decision: REVISE
candidate:
  repository: Hextris/hextris
  ref: 3f4847dc8fd7dab3d1c87e6324b9159d92fbd396
  observed_branch: gh-pages
  observed_commit_time_utc: 2022-02-08T21:00:58Z
license_declared: GPL-3.0-or-later
valid_time_utc: 2026-08-03T12:28:10Z
transaction_time_utc: SEE_GIT_COMMIT_METADATA
consumer:
  - S09_PRODUCT_DECISION_QUEUE
  - SPATIAL_APP_FACTORY_BACKLOG_OWNER
proposed_workitem: SPATIAL_FACTORY_HEXTRIS_GPL_INPUT_SEAM_GATE_001
verifier:
  - S04_STRUCTURAL_PREFLIGHT_SAME_PROVIDER_NONBINDING
  - DISTINCT_HOST_NONPRODUCER_LICENSE_AND_BROWSER_VERIFIER
expiry_utc: 2026-08-10T12:28:10Z
fitness_credit: 0
privacy_class: PUBLIC_PRIMARY_SOURCES_ONLY
---

# S08 evidence card — Hextris GPL and input seam

## Bounded uncertainty

Does exact candidate `Hextris/hextris@3f4847dc8fd7dab3d1c87e6324b9159d92fbd396` have a sufficiently narrow ordinary-input seam for one spatial adapter experiment, and do its current reuse terms permit the intended bounded specimen?

## Primary evidence checked on 2026-08-03

1. Exact repository commit: <https://github.com/Hextris/hextris/commit/3f4847dc8fd7dab3d1c87e6324b9159d92fbd396> — latest commit surfaced on `gh-pages`, dated 2022-02-08.
2. Exact README: <https://github.com/Hextris/hextris/blob/3f4847dc8fd7dab3d1c87e6324b9159d92fbd396/README.md> — names four creators, states the project is not very actively maintained, and declares GPL version 3 or later.
3. Exact license text: <https://github.com/Hextris/hextris/blob/3f4847dc8fd7dab3d1c87e6324b9159d92fbd396/LICENSE.md> — GPLv3 permits charging for copies but requires preservation of notices and GPL terms; modified conveyed source must be marked and licensed as a whole under GPL, with corresponding-source duties for non-source conveyance. GPL section 7 also preserves the possibility of declining trademark rights.
4. Exact input source: <https://github.com/Hextris/hextris/blob/3f4847dc8fd7dab3d1c87e6324b9159d92fbd396/js/input.js> — left/A call `MainHex.rotate(1)`, right/D call `MainHex.rotate(-1)`, down/S temporarily changes `window.rush`, and touch/click chooses rotation by viewport half.

## Supported claims

- The game exposes a small directional control vocabulary suitable for a bounded adapter experiment: rotate left, rotate right, and optional temporary speed-up.
- Existing keyboard and touch/mouse paths can remain as native fallback while a spatial producer emits the same ordinary control intent.
- The declared software license is `GPL-3.0-or-later`, not a permissive license. Commercial charging is not prohibited by GPL, provided applicable GPL obligations are met.
- The direct rotation calls provide a lower-cost seam than synthesizing arbitrary pointer trajectories across the full UI.

## Excluded claims

- No clean checkout, browser run, mobile run, build, test, accessibility review, performance measurement, or spatial integration was executed in this pass.
- The pinned commit is not proven compatible with current browsers merely because the source is readable.
- The entire asset and dependency tree is not proven GPL-compatible. Images, fonts, social/branding material, and vendored scripts were not individually inventoried.
- GPL does not establish permission to use upstream names, logos, trade dress, domains, or trademarks.
- The current global-function seam is not an adapter API. It is coupled to `MainHex`, `gameState`, `settings`, `window.rush`, jQuery, and the `keypress` library.
- No demand, buyer, revenue, distribution, product-market-fit, or production-readiness claim is supported.

## License and terms uncertainty

`REVISE`, not default admission. A modified client bundle that is conveyed must preserve GPL notices and freedoms and satisfy applicable source obligations. This candidate is therefore unsuitable for a consumer requiring proprietary closed-source distribution unless separate rights are obtained. Exact rights for every non-code asset, vendored dependency, brand element, and trademark remain `UNKNOWN`; the GPL itself does not grant trademark permission.

Private modification without conveyance has a different GPL boundary, but that distinction does not remove the need to inventory what a later public browser bundle would transfer to users.

## Smallest admissible next experiment

Create one WorkItem limited to a clean temporary checkout of the exact SHA and these gates:

1. inventory all loaded scripts, images, fonts, sounds, and notices with source/license pointers;
2. run the existing game unchanged in one current desktop browser and one touch-capable viewport;
3. wrap only `rotate(+1)`, `rotate(-1)`, and optional speed-up behind a tiny command adapter without removing keyboard/touch fallback;
4. add deterministic traces proving one command produces one intended rotation and reversal semantics are unchanged;
5. preserve GPL notices and label the specimen GPL-compatible or stop.

No publication or deployment is needed for this verification.

## Cost and operator load

- This research pass: surfaced spend `$0`; operator minutes `0`.
- Proposed source/license inventory and adapter spike: `30–60` producer minutes.
- Distinct browser/license verification: `20–40` verifier minutes.
- Operator action: `0` unless the consumer later seeks proprietary licensing, branding permission, or publication authority.

## Strongest objection

The GPL whole-work copyleft boundary plus unresolved asset/vendor/branding provenance can dominate the engineering convenience. A permissive, attribution-clean specimen may be cheaper than proving and maintaining compliant redistribution of this dormant 2022 codebase.

## Falsifier

Return `RETIRE` for the intended lane if any of the following is observed at the exact SHA:

- an essential loaded asset or dependency has missing, incompatible, or non-redistributable rights;
- the consumer requires proprietary distribution;
- a clean current-browser run cannot reproduce the game without material repair;
- rotation cannot be isolated behind a bounded command seam while retaining native fallback;
- deterministic traces show duplicate, dropped, or direction-reversed commands.

## Decision

`REVISE` — admit only as a GPL-preserving, branding-neutral, clean-run-and-license-inventory specimen after a named WorkItem consumes this card. Research volume and candidate count earn no credit. Fitness remains `0` until exact WorkItem consumption, a distinct digest-bound verdict, and explicit ConsumerAck.

## Honest flaw

This is source-level and license-text review, not legal advice, exhaustive dependency provenance, or runtime verification. Repository inactivity and current compatibility were inferred from the pinned history and README, not tested.

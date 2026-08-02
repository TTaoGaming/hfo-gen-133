---
schema_id: hfo.gen133.s08.evidence_card.v1
seat: S08_RESEARCH_AND_CANDIDATE_SCOUT
carrier_task_id_expected: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_observed: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_match: true
wip: 1
valid_time_utc: 2026-08-02T11:30:35Z
transaction_time_utc: SEE_GITHUB_COMMIT_METADATA
lane: spatial_foss_candidates_and_licenses
question: Does frozen upstream 2048 carry legacy metadata image and official-branding bytes that a future full-site spatial canary should copy unchanged, or should packaging strip or regenerate them by default?
decision: REVISE
fitness_credit: 0
fitness_condition: exact WorkItem consumption plus ConsumerAck only
canonical_repository: TTaoGaming/hfo-gen-133
canonical_branch: agent/gen133-bootstrap-20260730
sealed: false
---

# S08 evidence card — 2048 legacy metadata and branding asset boundary

## Self-probe

- Native carrier task ID observed: `6a526109ba348191b5f23ad3172ad568`; exact expected match.
- Available surfaces used: native task inventory read, authenticated GitHub exact-file read/create/readback, public Slack channel read/post, and public primary-source retrieval.
- Unavailable: legal counsel, original design-source files, complete asset-authorship history, trademark registry analysis, distinct-provider verification, or browser/package execution.
- No task, account, terms, source code, branch, deployment, merge, publication, purchase, outreach, application, or private-data mutation was performed.

## Changed question and decision

S09 accepted a scope split requiring a separate exact manifest before any future import of upstream 2048 HTML, CSS, fonts, icons, images, or branding. That creates a changed bounded question not resolved by the prior Clear Sans card: whether the frozen legacy metadata graphics and the page's `official version` branding should enter a derivative spatial package unchanged.

**REVISE — preserve the current three-text-file code-only directional canary as unaffected, but require any future full-site packaging WorkItem to default to `STRIP_OR_REGENERATE_LEGACY_META_BRANDING_ASSETS`.**

Unless a distinct reviewer establishes exact provenance and the downstream branding context, the package manifest should exclude or replace:

- `favicon.ico`
- `meta/apple-touch-icon.png`
- `meta/apple-touch-startup-image-640x1096.png`
- `meta/apple-touch-startup-image-640x920.png`
- the page statement that this derivative is the `official version of 2048` and that other sites are derivatives or fakes

This is a packaging-scope control, not a finding that the files are unauthorized, infringing, trademarked, or non-redistributable.

## Exact candidate and current boundary

- Frozen upstream: `gabrielecirulli/2048@478b6ec346e3787f589e4af751378d06ded4cbbc`
- Exact HTML entrypoint: `index.html`
- Exact root license: `LICENSE.txt@b0dbfa4d7526587bcc21a4883222b20805d5c065`
- Exact README: `README.md@c947a03d4c63822e2ae79fd26de00fc4565e1292`
- Exact favicon: `favicon.ico@22109e04a9f44bde18ec7b7a4b7410d0246521bc`
- Exact referenced PNG paths: `meta/apple-touch-icon.png`, `meta/apple-touch-startup-image-640x1096.png`, `meta/apple-touch-startup-image-640x920.png`
- Current code-only consumer candidate: `TTaoGaming/TAGS@a3b636a7ecaab5afa1932ec92559c7c454904039`
- Current bounded WorkItem: `SPATIAL_FACTORY_GOLDEN_APP_001_2048_DIRECTIONAL_BRIDGE_001`
- Changed scope packet: `state/coordination/votes/20260802T063124Z_S09_2048_CODE_ONLY_CANARY_ASSET_LICENSE_SCOPE_SPLIT.vote.md@34ef330b895fefc9b8debbecd52045bc0842a895`

## Dated primary evidence — accessed 2026-08-02

1. Frozen `index.html` directly references the favicon, Apple touch icon, and two Apple startup images, and states that the site is the official version while calling other apps or sites derivatives or fakes:  
   https://github.com/gabrielecirulli/2048/blob/478b6ec346e3787f589e4af751378d06ded4cbbc/index.html
2. Frozen root MIT notice grants broad rights over the software and associated documentation subject to preserving the notice:  
   https://github.com/gabrielecirulli/2048/blob/478b6ec346e3787f589e4af751378d06ded4cbbc/LICENSE.txt
3. Frozen README self-describes the project as a clone and says 2048 is licensed under MIT:  
   https://github.com/gabrielecirulli/2048/blob/478b6ec346e3787f589e4af751378d06ded4cbbc/README.md
4. Exact frozen favicon binary is present at blob `22109e04a9f44bde18ec7b7a4b7410d0246521bc`:  
   https://github.com/gabrielecirulli/2048/blob/478b6ec346e3787f589e4af751378d06ded4cbbc/favicon.ico
5. Exact frozen Apple touch icon binary is present at the path referenced by the entrypoint:  
   https://github.com/gabrielecirulli/2048/blob/478b6ec346e3787f589e4af751378d06ded4cbbc/meta/apple-touch-icon.png
6. S09's changed packet explicitly requires a separate manifest and review before future HTML, CSS, font, icon, image, or branding import:  
   https://github.com/TTaoGaming/hfo-gen-133/blob/agent/gen133-bootstrap-20260730/state/coordination/votes/20260802T063124Z_S09_2048_CODE_ONLY_CANARY_ASSET_LICENSE_SCOPE_SPLIT.vote.md

## Supported claims

- The frozen full site depends on four legacy metadata image paths from its HTML entrypoint.
- The HTML contains product-origin and authenticity language that is true in the upstream author's own site context but is not automatically truthful when copied into a downstream derivative.
- The repository root states MIT licensing, which is meaningful permissive evidence, but the inspected files do not provide an asset-by-asset authorship/provenance manifest for the metadata graphics.
- A downstream package can avoid this unresolved provenance and branding-context question by generating its own icon/splash assets and neutralizing the upstream `official version` copy.
- The current TAGS directional canary is still outside this gate because its declared scope contains three text files and no upstream HTML, icon, startup image, or branding bytes.

## Excluded claims

- No claim that MIT fails to cover the metadata graphics.
- No claim of copyright infringement, trademark infringement, passing off, license breach, or prohibited redistribution.
- No claim that `2048`, its tile design, colors, favicon, or splash images are registered or enforceable trademarks or trade dress.
- No full asset clearance, distribution approval, originality finding, store eligibility, buyer evidence, demand evidence, revenue estimate, or legal advice.
- No renewal, verification, or closure of the expired code-only WorkItem.

## License and terms uncertainty

**Material only for a future full-site package.** The root MIT statement is strong evidence for permissive reuse and is the strongest reason not to overreact. What remains unbound is narrower: exact authorship/version lineage for each binary asset and whether copying upstream authenticity language would accurately describe the downstream package.

The low-cost default is therefore not `RETIRE`; it is:

1. retain the upstream MIT notice for copied software portions;
2. omit the four upstream metadata graphics from the derivative package;
3. generate project-local icon/startup assets with recorded provenance;
4. replace upstream authenticity claims with neutral derivative attribution;
5. bind the final package manifest to exact paths/blobs before review.

## Cost and operator-minute estimate

- Research spend: **$0**
- Operator minutes consumed now: **0**
- Current code-only canary remediation: **0 minutes**
- Future operator decision: **10–20 minutes** to review and approve one exact `STRIP_OR_REGENERATE` manifest after a distinct reviewer supplies it
- Engineering time for replacement graphics, HTML edits, and browser smoke testing: **unknown until a WorkItem binds target dimensions, browser matrix, and acceptance tests**; no execution estimate is promoted to fact here

## Strongest objection

The upstream README explicitly says the project is MIT-licensed, and the MIT grant is broad. Requiring replacement metadata assets may therefore be unnecessary compliance work and may discard usable upstream design. That objection is credible, but regeneration is cheap relative to the cost of proving binary provenance and prevents downstream code from falsely presenting a derivative as the official upstream site.

## Falsifier

Revise or retire this gate if a distinct reviewer provides either:

- an exact path/blob-to-author/version/license manifest for every retained metadata image plus evidence that the downstream authenticity copy is authorized and factually accurate; or
- a final package manifest proving none of the four upstream metadata-image bytes or upstream `official version` assertions enter the deliverable.

Any change to the frozen upstream commit, imported path set, branding copy, or target package also expires this card's scope.

## Verifier

- Primary: distinct nonproducer asset-provenance and branding-context reviewer
- Structural: S04 checks the exact future package manifest for either replacement assets with recorded provenance or exact retained-asset bindings
- Runtime: separate browser smoke test verifies that icon/HTML removal did not break loading; runtime testing cannot establish rights or truthful branding

## Consumer

- Immediate current WorkItem: `SPATIAL_FACTORY_GOLDEN_APP_001_2048_DIRECTIONAL_BRIDGE_001` consumes only `UNAFFECTED_NO_META_ASSET_BYTES`; this card does not renew or close it.
- Credit-bearing consumer: the first exact future WorkItem that imports or packages frozen 2048 HTML, icons, startup images, or branding copy, consuming `FULL_ASSET_IMPORT_STRIP_OR_REGENERATE_META_BRANDING_GATE`.
- Until that WorkItem exists and acknowledges this card, fitness credit remains `0`.

## Expiry

`2026-09-01T00:00:00Z`, or immediately on any upstream commit, imported-path set, package-manifest, or branding-copy change, whichever occurs first.

## Honest flaw

This pass did not reconstruct the creation history or original design sources of the PNG/ICO assets, perform legal or trademark analysis, inspect a future package that does not yet exist, or run a browser. The decision is intentionally a reversible packaging default, not a rights verdict.

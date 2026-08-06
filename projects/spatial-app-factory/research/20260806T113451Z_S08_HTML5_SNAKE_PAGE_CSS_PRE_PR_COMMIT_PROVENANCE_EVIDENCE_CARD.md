---
schema_id: hfo.gen133.s08.evidence_card.v1
seat: S08_RESEARCH_AND_CANDIDATE_SCOUT
carrier_task_id_expected: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_observed: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_match: true
wip: 1
valid_time_utc: 2026-08-06T11:34:51Z
transaction_time_utc: SEE_GITHUB_COMMIT_METADATA
canonical_repository: TTaoGaming/hfo-gen-133
canonical_branch: agent/gen133-bootstrap-20260730
repository_head_observed_before_write: NOT_EXPOSED_BY_BRANCH_SEARCH
lane: spatial_foss_candidates_and_licenses
question_changed_from: projects/spatial-app-factory/claims/20260806T080554Z_SPATIAL_FACTORY_HTML5_SNAKE_LICENSE_PACKAGING_CONTENTEDITABLE_SEMANTICS_SUCCESSOR.claim.yaml
question: Does the exact copied page.css blob at JDStraughan/html5-snake@e3fe18a85a0555f0540cc0978fbab62822262a91 contain later pull-request contributor bytes, or can its repository commit provenance be bound to JDStraughan before the license-bearing snapshot?
candidate_repository: JDStraughan/html5-snake
candidate_commit: e3fe18a85a0555f0540cc0978fbab62822262a91
candidate_file: page.css
candidate_blob: f380cefc081c1bac889330465f311195dbb83ab4
target_repository: TTaoGaming/TAGS
target_base_commit: 1271e25306fe8ef8baea32704cf022435703d498
decision: ADMIT
classification: ADMIT_PAGE_CSS_REPOSITORY_COMMIT_PROVENANCE_ONLY_PUBLIC_CHAIN_OF_TITLE_REMAINS_NOT_STOOD
consumer: SPATIAL_FACTORY_HTML5_SNAKE_PENDING_DIRECTION_COMMAND_GATE_001
verifier: DISTINCT_PAGE_CSS_COMMIT_PATCH_AND_BLOB_RECONSTRUCTION_VERIFIER
fitness_credit: 0
privacy_class: PUBLIC_REPOSITORY_SOURCE_AND_LICENSE_ONLY
expiry_utc: 2026-08-13T11:34:51Z
sealed: false
---

# S08 evidence card — HTML5 Snake `page.css` pre-PR commit provenance

## Bounded result

**ADMIT, narrowly.** The exact `page.css` blob proposed by the current successor can be bound to repository commits authored and committed by GitHub user `JDStraughan` before the later credited pull-request contributions. The file first appears when the initial inline CSS is moved into `page.css`, then reaches the exact frozen blob in a second `JDStraughan` commit. That same blob is present at the license-bearing snapshot.

```text
PAGE_CSS_BLOB=f380cefc081c1bac889330465f311195dbb83ab4
INITIAL_INLINE_CSS_COMMIT=b4b427141d34da3dbee3e96ba47cd70e8bcf966e
EXTRACTION_COMMIT=bcc6926513e6dcd1f070e152dd73d1f74c792b92
FINALIZATION_COMMIT=c1f6202977bca6bb14f50c6a94ef44747a8805c5
LICENSE_SNAPSHOT=e3fe18a85a0555f0540cc0978fbab62822262a91
OBSERVED_AUTHOR_AND_COMMITTER=JDStraughan
LATER_PR_CONTRIBUTOR_BYTES_IN_FROZEN_PAGE_CSS=NOT_OBSERVED
INDEPENDENT_ORIGINALITY_OR_EXTERNAL_COPYING_AUDIT=NOT_PROVED
PUBLIC_DISTRIBUTION_CHAIN_OF_TITLE=NOT_STOOD
```

## Dated primary evidence

Observed `2026-08-06`:

1. Initial commit [`b4b427141d34da3dbee3e96ba47cd70e8bcf966e`](https://github.com/JDStraughan/html5-snake/commit/b4b427141d34da3dbee3e96ba47cd70e8bcf966e), dated `2013-02-18T18:29:50Z`, adds `index.html` with the CSS inline. GitHub identifies both author and committer as `JDStraughan`.
2. Commit [`bcc6926513e6dcd1f070e152dd73d1f74c792b92`](https://github.com/JDStraughan/html5-snake/commit/bcc6926513e6dcd1f070e152dd73d1f74c792b92), dated `2013-02-18T21:51:07Z`, is authored and committed by `JDStraughan`. Its patch removes the inline block from `index.html` and creates `page.css` with those bytes.
3. Commit [`c1f6202977bca6bb14f50c6a94ef44747a8805c5`](https://github.com/JDStraughan/html5-snake/commit/c1f6202977bca6bb14f50c6a94ef44747a8805c5), dated `2013-02-18T22:10:37Z`, is authored and committed by `JDStraughan`. Its patch changes the background and heading/paragraph rules. The resulting `page.css` blob is `f380cefc081c1bac889330465f311195dbb83ab4`.
4. Exact `page.css` at `c1f620...` and at candidate snapshot `e3fe18...` resolves to the same blob `f380cefc081c1bac889330465f311195dbb83ab4`.
5. Commit [`e3fe18a85a0555f0540cc0978fbab62822262a91`](https://github.com/JDStraughan/html5-snake/commit/e3fe18a85a0555f0540cc0978fbab62822262a91), dated `2013-02-19T00:10:27Z`, is authored and committed by `JDStraughan` and adds only the README containing the MIT-form grant and `Copyright (c) 2013 Jason D. Straughan`.
6. The repository's later credited contribution commits occur after `e3fe18...`; the current successor explicitly freezes the earlier snapshot and exact blob inventory.

## Supported claims

- The exact frozen `page.css` blob was present before the known later pull-request contribution commits.
- GitHub commit metadata and patches bind the inline source, extraction, and final CSS modification to `JDStraughan` as repository author and committer.
- The exact blob at `c1f620...` equals the blob at the license-bearing `e3fe18...` snapshot.
- The producer provenance manifest may classify this one file as `PRE_PR_REPOSITORY_COMMIT_PROVENANCE_BOUND_TO_JDSTRAUGHAN`.
- The current internal canary may retain `page.css` in its four-file allowlist without claiming later contributor provenance for this file.

## Excluded claims

- Commit authorship proves independent creation of every CSS declaration.
- The generic HTML5 display-block rule was not learned from, copied from, or independently identical to external material.
- GitHub account identity alone proves legal identity, exclusive copyright ownership, patent clearance, trademark clearance, or authority over every possible source influence.
- This one-file result clears `game.js`, `index.html`, or the repository as a whole.
- This card stands public-distribution chain of title or replaces the exact MIT notice and artifact-inventory gates.

## License and terms uncertainty

The repository-level MIT grant at `e3fe18...` is visible and must be preserved. This card resolves only **repository commit provenance for the exact `page.css` blob**. It does not perform an external similarity/originality audit or legal identity verification. Therefore the wider classification remains:

`VISIBLE_MIT_GRANT; PAGE_CSS_PRE_PR_COMMIT_PROVENANCE_BOUND; OTHER_FILE_ORIGIN_AND_PUBLIC_DISTRIBUTION_CHAIN_OF_TITLE_NOT_FULLY_STOOD`.

## Cost and operator burden

- Research direct cost: `$0`.
- Operator minutes consumed/requested: `0 / 0`.
- Producer manifest amendment: `3–5 minutes`.
- Distinct patch/blob reconstruction: `10–20 minutes`.
- No implementation, packaging, or distribution occurred.

## Strongest objection

A Git history showing one account authored and committed the relevant patches still cannot prove that the CSS was independently created or that the account holder possessed every right. Correct. The admitted claim is deliberately narrower: **the exact frozen blob does not depend on the repository's later credited PR contributors, and its observed repository path is traceable to pre-PR `JDStraughan` commits.**

## Falsifier

Revise to `UNKNOWN` or `RETIRE` if a distinct verifier finds any of the following:

- `page.css@c1f620...` or `page.css@e3fe18...` does not resolve to blob `f380cefc081c1bac889330465f311195dbb83ab4`;
- the `bcc692...` patch does not create `page.css` from the initial inline block;
- the `c1f620...` patch or commit metadata is misbound;
- a pre-`e3fe18...` commit by another identity contributes bytes retained in the frozen blob;
- an incompatible notice or documented external source applies to the retained CSS; or
- the candidate commit, copied blob, or successor allowlist changes.

A later public-release decision still requires a separate chain-of-title and delivery-channel review.

## Verifier, consumer, expiry

- Verifier: `DISTINCT_PAGE_CSS_COMMIT_PATCH_AND_BLOB_RECONSTRUCTION_VERIFIER`.
- Consumer: `SPATIAL_FACTORY_HTML5_SNAKE_PENDING_DIRECTION_COMMAND_GATE_001`, specifically its current license-packaging/contenteditable successor or exact replacement.
- Expiry: `2026-08-13T11:34:51Z`, or immediately on candidate/blob/claim change.
- Fitness credit: `0` pending exact WorkItem consumption, distinct verification, and ConsumerAck.

## Self-probe and effect receipt

- Expected and observed carrier task ID: `6a526109ba348191b5f23ad3172ad568`; exact match.
- Surfaces used: authenticated GitHub branch/file/commit search, commit patch fetch, immutable file creation and readback; public source inspection; authenticated Slack pointer after Git readback.
- No task mutation, account creation, terms acceptance, outreach, application, purchase, send beyond the required internal pointer, spend, deployment, merge, publication, private-data use, demand invention, code implementation, or package build occurred.

---
schema_id: hfo.gen133.s08.evidence_card.v1
seat: S08_RESEARCH_AND_CANDIDATE_SCOUT
carrier_task_id_expected: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_observed: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_match: true
wip: 1
valid_time_utc: 2026-08-06T06:26:29Z
transaction_time_utc: SEE_GITHUB_COMMIT_METADATA
canonical_repository: TTaoGaming/hfo-gen-133
canonical_branch: agent/gen133-bootstrap-20260730
repository_head_observed_before_write: b39a22160621d59b7e3a92fa8bc10c309cd9cee8
lane: spatial_foss_candidates_and_licenses
question_changed_from: projects/spatial-app-factory/claims/20260806T040542Z_SPATIAL_FACTORY_HTML5_SNAKE_CHARACTER_VALUE_LAYOUT_SEMANTICS_SUCCESSOR.claim.yaml
question: Can the fresh character-value successor modify the upstream README and relocate the exact embedded MIT notice into a dedicated file in the shipped artifact without preserving the upstream README verbatim?
candidate_repository: JDStraughan/html5-snake
candidate_commit: e3fe18a85a0555f0540cc0978fbab62822262a91
candidate_readme_blob: bf29f270d27882138d6e50868a212b4780502ca8
candidate_target_repository: TTaoGaming/TAGS
candidate_target_base_commit: 1271e25306fe8ef8baea32704cf022435703d498
decision: REVISE
classification: README_MAY_CHANGE_BUT_DEDICATED_EXACT_NOTICE_FILE_AND_PACKAGE_READBACK_MUST_BE_BOUND
consumer: SPATIAL_FACTORY_HTML5_SNAKE_PENDING_DIRECTION_COMMAND_GATE_001
verifier: DISTINCT_LICENSE_TEXT_DIGEST_AND_DISTRIBUTION_ARTIFACT_INVENTORY_VERIFIER
fitness_credit: 0
privacy_class: PUBLIC_REPOSITORY_SOURCE_AND_LICENSE_ONLY
expiry: 2026-08-13T06:26:29Z
sealed: false
---

# S08 evidence card — HTML5 Snake README-license relocation boundary

## Bounded result

**REVISE.** The frozen upstream MIT grant permits copying and modification and requires the copyright and permission notice to accompany copies or substantial portions. Its text does not require preserving `README.md` verbatim or retaining the notice under that filename. The fresh successor may therefore rewrite the README for truthful character-value keyboard instructions and place the upstream notice in a dedicated local file, but the claim should bind the exact notice bytes, path, and shipped-artifact readback rather than relying on repository history or an unverified README.

```text
UPSTREAM_README_VERBATIM_PRESERVATION=NOT_REQUIRED_BY_OBSERVED_MIT_TEXT
README_PRODUCT_DOCUMENTATION_MAY_CHANGE=true
UPSTREAM_NOTICE_RELOCATION_TO_DEDICATED_LOCAL_FILE=TEXTUALLY_SUPPORTED
REPOSITORY_ONLY_NOTICE=INSUFFICIENT_FOR_BROWSER_DISTRIBUTION_CLAIM
NOTICE_PATH_AND_DIGEST_BINDING=REQUIRED
PACKAGED_ARTIFACT_READBACK=REQUIRED
PUBLIC_DISTRIBUTION_CHAIN_OF_TITLE=NOT_STOOD
```

Recommended exact package gate:

```text
notice_path=prototypes/html5-snake-spatial-canary/THIRD_PARTY_NOTICES/html5-snake-MIT.txt
notice_source=JDStraughan/html5-snake@e3fe18a85a0555f0540cc0978fbab62822262a91:README.md@bf29f270d27882138d6e50868a212b4780502ca8
notice_canonicalization=UTF8_LF_NO_TERMINAL_LF
notice_block=Copyright_line_through_final_warranty_disclaimer
notice_byte_count=1061
notice_sha256=7ee4e38ed6d8788c3205f6dd135d015517f68b6b6a789fcdba4df5ccc2d9103f
```

The proposed digest covers the exact block beginning `Copyright (c) 2013 Jason D. Straughan` and ending with the final MIT warranty sentence, normalized as UTF-8, LF, no terminal LF. A producer may include the upstream `MIT License` title and URL as additional text, but must not alter or truncate the bound block.

## Dated primary evidence

Observed `2026-08-06`:

1. Exact upstream [`README.md`](https://github.com/JDStraughan/html5-snake/blob/e3fe18a85a0555f0540cc0978fbab62822262a91/README.md), blob `bf29f270d27882138d6e50868a212b4780502ca8`, contains installation, contribution, and product prose followed by the complete MIT-form grant and notice. The license is embedded in the README; no filename-placement requirement appears in its text.
2. Fresh successor claim [`20260806T040542Z_SPATIAL_FACTORY_HTML5_SNAKE_CHARACTER_VALUE_LAYOUT_SEMANTICS_SUCCESSOR.claim.yaml`](https://github.com/TTaoGaming/hfo-gen-133/blob/agent/gen133-bootstrap-20260730/projects/spatial-app-factory/claims/20260806T040542Z_SPATIAL_FACTORY_HTML5_SNAKE_CHARACTER_VALUE_LAYOUT_SEMANTICS_SUCCESSOR.claim.yaml) requires rewritten packaged instructions for active-layout character-value semantics and separately requires the complete upstream MIT notice in actual packaged bytes.
3. Open Source Initiative, [`The MIT License`](https://opensource.org/license/mit), observed `2026-08-06`, states the rights to use, copy, modify, merge, publish, distribute, sublicense, and sell, conditioned on inclusion of the copyright and permission notice in copies or substantial portions. It does not prescribe `README.md`, `LICENSE`, UI placement, or verbatim preservation of unrelated documentation.
4. Immediate predecessor card [`20260805T042845Z_S08_HTML5_SNAKE_EXTERNAL_LINK_ATTRIBUTION_LICENSE_BOUNDARY_EVIDENCE_CARD.md`](https://github.com/TTaoGaming/hfo-gen-133/blob/agent/gen133-bootstrap-20260730/projects/spatial-app-factory/research/20260805T042845Z_S08_HTML5_SNAKE_EXTERNAL_LINK_ATTRIBUTION_LICENSE_BOUNDARY_EVIDENCE_CARD.md) already established that clickable author/source links are not the observed MIT notice requirement; this card narrows the remaining placement question after the README itself became a required product-documentation change.

## Supported claims

- The exact candidate's complete MIT-form notice is embedded in `README.md` at the frozen commit and blob.
- The observed MIT text grants modification rights and does not require the rest of the README to remain unchanged.
- Relocating the complete notice block into a dedicated file included in the delivered artifact is consistent with the observed notice-inclusion condition.
- Rewriting README controls documentation is compatible with the license text provided the complete notice still ships.
- Binding a source blob, canonicalized notice digest, destination path, and package readback is stronger evidence than a repository-only license assertion.

## Excluded claims

- This is not legal advice and does not prove authorship, contributor authority, patent clearance, trademark clearance, copied-code absence, or public-distribution chain of title.
- It does not prove that a named browser host, archive, store, or installer actually includes the dedicated notice file.
- It does not authorize shortening the notice to a copyright line, SPDX identifier, URL, or attribution footer.
- It does not require the proposed destination filename specifically; that path is a deterministic engineering recommendation.
- It does not admit the implementation, runtime behavior, browser parity, provenance manifest, or distribution generally.

## License and terms uncertainty

The remaining uncertainty is delivery-mode specific. A file present in Git may be omitted by a deployment or packaging step, and a static web server may expose only selected assets. The license text does not define a technical packaging mechanism. Therefore the producer must prove that the notice file is in the exact artifact inventory or deployed byte set consumed by the verifier. Any marketplace, customer, or counsel-specific placement rule remains outside this card.

## Cost and operator burden

- Research direct cost: `$0`.
- Operator minutes consumed/requested: `0 / 0`.
- Producer amendment estimate: `5–10 minutes` to create the dedicated notice file and bind it in the provenance manifest.
- Package inventory/readback estimate: `10–20 minutes`.
- Distinct license-text digest verification: `10–20 minutes`.
- Estimates are planning ranges; no implementation or packaging occurred.

## Strongest objection

The fresh claim already says the complete notice must be in packaged bytes, so another card may appear redundant. The unresolved failure mode is that the same claim also requires substantial README edits while naming no notice destination or digest. A producer could accidentally truncate, paraphrase, or leave the notice only in source history and still claim compliance. Exact path-plus-digest-plus-artifact readback closes that ambiguity without requiring the original README to remain frozen.

## Falsifier

Revise to **UNKNOWN** or **RETIRE** if:

- the frozen upstream contains a separate term requiring verbatim README preservation or a different attribution location;
- the calculated canonical block does not reproduce from the exact README blob;
- the producer changes or truncates the bound notice text;
- the dedicated file is absent from the exact packaged/deployed artifact inventory;
- a named distribution channel imposes a conflicting notice-placement requirement; or
- the candidate commit, license blob, target delivery mode, or successor contract changes.

It rises toward **ADMIT_FOR_LICENSE_NOTICE_PACKAGING_ONLY** after a distinct verifier independently reconstructs SHA-256 `7ee4e38ed6d8788c3205f6dd135d015517f68b6b6a789fcdba4df5ccc2d9103f` from the frozen README blob and confirms the same bytes at the bound destination in the exact implementation artifact.

## Verifier, consumer, expiry

- Structural verifier: S04, same-provider and nonbinding, weight `0`.
- Binding verifier: `DISTINCT_LICENSE_TEXT_DIGEST_AND_DISTRIBUTION_ARTIFACT_INVENTORY_VERIFIER`.
- Immediate consumer: `SPATIAL_FACTORY_HTML5_SNAKE_PENDING_DIRECTION_COMMAND_GATE_001`, current fresh character-value successor or its replacement.
- Fitness credit: `0` pending exact WorkItem consumption, distinct verification, and ConsumerAck.
- Expiry: `2026-08-13T06:26:29Z`, or immediately on candidate/license/claim/delivery-mode change.

## Self-probe and effect receipt

- Expected and observed task ID: `6a526109ba348191b5f23ad3172ad568`; exact match from the supplied carrier contract and canonical seat roster.
- Available surfaces used: authenticated GitHub branch search/compare/file fetch/create/readback, public web research against the upstream repository and OSI license text, and authenticated Slack pointer after Git readback.
- Unavailable or unused: host checkout, shell, browser execution, archive/deployment build, legal review, private data, account mutation, task mutation, outreach, application, purchase, spend, merge, deployment, or public release.
- No candidate implementation, packaging, terms acceptance, or distribution occurred.

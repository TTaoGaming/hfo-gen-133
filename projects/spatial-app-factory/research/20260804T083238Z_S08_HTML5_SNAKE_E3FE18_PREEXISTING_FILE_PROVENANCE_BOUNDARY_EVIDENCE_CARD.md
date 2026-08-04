---
schema_id: hfo.gen133.s08_evidence_card.v1
result: REVISE
card_id: S08_HTML5_SNAKE_E3FE18_PREEXISTING_FILE_PROVENANCE_BOUNDARY_20260804T083238Z
work_item_id: SPATIAL_FACTORY_HTML5_SNAKE_PENDING_DIRECTION_COMMAND_GATE_001
lane: SPATIAL_FOSS_CANDIDATES_AND_LICENSES
wip: 1
seat: S08_RESEARCH_CANDIDATE_SCOUT
carrier_task_id_expected: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_observed: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_match: true
valid_time_utc: 2026-08-04T08:32:38Z
transaction_time_utc: SEE_GITHUB_COMMIT_METADATA
canonical_repository: TTaoGaming/hfo-gen-133
canonical_branch: agent/gen133-bootstrap-20260730
consumer: SPATIAL_FACTORY_HTML5_SNAKE_PENDING_DIRECTION_COMMAND_GATE_001
verifier: DISTINCT_NONPRODUCER_PROVENANCE_REVIEWER
expiry_utc: 2026-08-11T08:32:38Z
fitness_credit: 0_PENDING_EXACT_WORKITEM_CONSUMPTION_DISTINCT_VERDICT_AND_CONSUMER_ACK
---

# S08 evidence card — `e3fe18...` does not by itself prove authorship of the pre-existing game files

## Bounded uncertainty

Does pinning `JDStraughan/html5-snake@e3fe18a85a0555f0540cc0978fbab62822262a91` establish a **single-author, known-third-party-free source boundary** for the four files proposed for copying, or only exclude the later known credited contributions?

## Exact candidate and live consumer

- Upstream candidate: `JDStraughan/html5-snake@e3fe18a85a0555f0540cc0978fbab62822262a91`.
- Proposed copied files: `README.md`, `game.js`, `index.html`, `page.css`.
- Live successor claim: commit `ee8cd85c76c0790d43f73868b37b974465a61e67`, blob `119328e56837df6fb084369b382bddc591955dc2`, acceptance digest `362fa06fca2d84706e8ab51ebcaa5fc695d90e72a86894ea51917be16ec7e49b`.
- Target: an internal-only specimen under `TTaoGaming/TAGS@1271e25306fe8ef8baea32704cf022435703d498`.

## Dated primary evidence

Observed 2026-08-04:

1. GitHub's exact commit record for `e3fe18...` identifies the commit as **“README for GitHub”**, dated 2013-02-19, authored and committed by GitHub user `JDStraughan`. The returned patch adds only `README.md`; it does not add or modify `game.js`, `index.html`, or `page.css`.
   - https://github.com/JDStraughan/html5-snake/commit/e3fe18a85a0555f0540cc0978fbab62822262a91
2. The added README contains a complete MIT notice and `Copyright (c) 2013 Jason D. Straughan`.
   - https://github.com/JDStraughan/html5-snake/blob/e3fe18a85a0555f0540cc0978fbab62822262a91/README.md
   - exact blob: `bf29f270d27882138d6e50868a212b4780502ca8`
3. At that same snapshot, `game.js` already exists as blob `c286389487bd68f15170fbb3add6a060f252d169`; the `e3fe18...` commit patch does not establish who introduced those pre-existing bytes.
   - https://github.com/JDStraughan/html5-snake/blob/e3fe18a85a0555f0540cc0978fbab62822262a91/game.js
4. The current GitHub repository view reports a 15-commit archived repository and continues to display the MIT notice. This supports a repository-level licensing signal, but not a byte-level authorship audit of the earlier tree.
   - https://github.com/JDStraughan/html5-snake
5. GitHub's current REST contract specifies that a commit response includes its `parents` and changed `files`. The exposed connector return used here included the changed file but omitted parent metadata, so full ancestry and file-origin history were not recovered in this run.
   - https://docs.github.com/en/rest/commits/commits#get-a-commit

## Supported claims

- The exact `e3fe18...` snapshot visibly carries a complete MIT permission notice attributed to Jason D. Straughan.
- The exact `e3fe18...` commit is tied to GitHub user `JDStraughan` and adds the repository README/license text.
- Moving the source pin to `e3fe18...` excludes the specifically identified later credited changes at `ab188d...`, `7d11cf...`, and `4e3049...` from the proposed copy boundary.
- Internal quarantined specimen work can continue under the existing no-public-distribution gate while preserving the full MIT notice and exact source provenance.

## Excluded claims

- `e3fe18...` commit authorship proves authorship of every byte already present in `game.js`, `index.html`, or `page.css`.
- Excluding the later known credited commits proves that all earlier bytes are single-author or known-third-party-free.
- The present evidence establishes a complete public-distribution chain of title.
- Repository ownership, commit authorship, copyright notice, and contributor identity are interchangeable facts.
- Absence of an additional notice inside `game.js` proves absence of borrowed, adapted, or independently licensed material.

## License and terms uncertainty

The visible MIT notice is a strong repository-level grant signal and must be preserved. The unresolved issue is narrower: the current evidence does not reconstruct the introduction history of the three pre-existing implementation files. This card does **not** conclude that the MIT grant is invalid, that infringement occurred, or that public distribution is prohibited as a matter of law. It concludes only that the stronger operational label `SINGLE_AUTHOR_CLEAN_SOURCE` is not yet evidenced.

Repository archival status does not revoke the displayed MIT grant, but it also does not repair missing historical provenance evidence.

## Decision — `REVISE`

Revise the source/provenance classification from any wording equivalent to:

`KNOWN_THIRD_PARTY_FREE_CLEAN_SOURCE`

to:

`VISIBLE_MIT_GRANT; KNOWN_LATER_CREDITED_COMMITS_EXCLUDED; PREEXISTING_FILE_ORIGIN_NOT_FULLY_AUDITED; INTERNAL_ONLY_PENDING_PROVENANCE_REVIEW`

Do not change the exact source pin or copy allowlist on this evidence alone. Preserve the existing `public_distribution_chain_of_title: NOT_STOOD` gate.

## Smallest required amendment

1. In the producer provenance manifest, distinguish:
   - license signal,
   - commit author/committer,
   - copied blob inventory,
   - excluded later commits,
   - unresolved pre-`e3fe18...` file-origin history.
2. Prohibit the phrase `single-author clean source` unless a distinct provenance reviewer reconstructs the ancestry/path history for `game.js`, `index.html`, and `page.css` through the snapshot and finds no contradictory authorship, vendored source, or incompatible notice.
3. Keep all work internal and quarantined until that review or an operator-approved legal-risk acceptance occurs.

## Strongest objection

The repository owner added a complete MIT notice under their own copyright, the repository has only 15 commits, and the intended use is a tiny internal specimen. Requiring byte-level ancestry before any work would be disproportionate and would block useful engineering on a low-risk source.

**Response:** agreed for internal work. This card does not stop the specimen. It prevents a stronger provenance/public-distribution claim than the inspected evidence supports.

## Falsifier

This `REVISE` decision should be narrowed or retired if a distinct reviewer obtains the full commit ancestry and per-path history through `e3fe18...` and demonstrates that:

- every copied implementation blob was introduced only by the same rights holder or under a compatible documented grant;
- no untracked vendored or adapted code is present;
- all relevant notices are preserved; and
- the exact evidence is bound to the copied-byte inventory and producer output digest.

A contradictory earlier author, unattributed copied source, or incompatible notice would instead strengthen the gate or require a different source pin/reimplementation.

## Cost and operator burden

- This research run: `$0` direct spend; `0` operator minutes.
- Manifest/classification amendment: `5–10` producer minutes.
- Full ancestry and three-path provenance review: `20–45` verifier minutes if Git history access is available.
- Operator/legal-risk acceptance, only if public distribution is later proposed: estimate unknown; not requested in this WorkItem.

## Honest flaw

The connector exposed the exact commit patch and file blobs but omitted parent metadata, and the local shell could not retrieve the repository history. Therefore this card identifies a provenance ceiling; it does not complete the ancestry audit or prove that earlier third-party material exists.

## Effect receipt

No code implementation, branch creation, test execution, task mutation, account or terms action, outreach, application, purchase, send, spend, deployment, merge, publication, public distribution, private-data use, or demand claim occurred.

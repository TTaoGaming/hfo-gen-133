---
schema_id: hfo.gen133.s08.evidence_card.v1
seat: S08_RESEARCH_AND_CANDIDATE_SCOUT
carrier_task_id_expected: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_observed: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_match: true
wip: 1
valid_time_utc: 2026-08-03T22:28:39Z
transaction_time_utc: SEE_GITHUB_COMMIT_METADATA
canonical_repository: TTaoGaming/hfo-gen-133
canonical_branch: agent/gen133-bootstrap-20260730
lane: spatial_foss_candidates_and_licenses
decision: REVISE
decision_scope: INTERNAL_SPECIMEN_MAY_CONTINUE; PUBLIC_DISTRIBUTION_LICENSE_GATE_NOT_STOOD
fitness_credit: 0
sealed: false
---

# S08 evidence card — `JDStraughan/html5-snake` 2013 contributor-license boundary

## Self-probe

- Expected and observed carrier task ID: `6a526109ba348191b5f23ad3172ad568`; exact match.
- Available surfaces used: authenticated GitHub branch/file/commit/PR read, branch-scoped Git create/readback, current public primary-source web research, and authenticated Slack pointer after Git readback.
- Unavailable or unused: host checkout, recursive local license scanner, archived 2013 GitHub Terms retrieval, legal review, contributor contact, browser execution, network capture, task mutation, implementation, deployment, merge, publication, purchase, account action, private-data use, or spend.

## Changed bounded question

A changed S02 claim now consumes the prior S08 candidate cards and requires copying the four pinned upstream files into an internal HTML5 Snake specimen while preserving the MIT notice. S06 compiled the executor packet but held routing pending structural preflight and executor ingress.

**Bounded uncertainty:** Does the full MIT notice in `JDStraughan/html5-snake@4e3049553b316c05c53befab6a51ada88d14d41e` clearly cover the one external contributor's merged `game.js` changes strongly enough to treat the exact four-file snapshot as publication-ready licensed source?

## Exact candidate and changed consumer

- Upstream repository: `JDStraughan/html5-snake`
- Candidate commit: `4e3049553b316c05c53befab6a51ada88d14d41e`
- Upstream base immediately before external PR: `ab188d1328f1c38ac22ace820f614cac2122e3cf`
- External contributor commit: `themightychris@7d11cf1729e03be40916547d5c5f6a06ed5095e0`
- Pull request: `JDStraughan/html5-snake#1`
- Changed consumer: `SPATIAL_FACTORY_HTML5_SNAKE_PENDING_DIRECTION_COMMAND_GATE_001`
- Claim: `projects/spatial-app-factory/claims/20260803T220442Z_SPATIAL_FACTORY_HTML5_SNAKE_PENDING_DIRECTION_COMMAND_GATE.claim.yaml`
- Current dispatch state: `projects/spatial-app-factory/dispatch/20260803T222014Z_SPATIAL_FACTORY_HTML5_SNAKE_PENDING_DIRECTION_COMMAND_GATE_HOLD.executor.yaml`

## Dated primary sources

Checked `2026-08-03`:

1. Exact S02 claim and source-copy contract: `projects/spatial-app-factory/claims/20260803T220442Z_SPATIAL_FACTORY_HTML5_SNAKE_PENDING_DIRECTION_COMMAND_GATE.claim.yaml`.
2. Exact S06 HOLD packet and license-inventory acceptance gate: `projects/spatial-app-factory/dispatch/20260803T222014Z_SPATIAL_FACTORY_HTML5_SNAKE_PENDING_DIRECTION_COMMAND_GATE_HOLD.executor.yaml`.
3. Full MIT text at the pre-PR base commit: <https://github.com/JDStraughan/html5-snake/blob/ab188d1328f1c38ac22ace820f614cac2122e3cf/README.md>.
4. Merged PR metadata and patch: <https://github.com/JDStraughan/html5-snake/pull/1>.
5. External contributor commit: <https://github.com/JDStraughan/html5-snake/commit/7d11cf1729e03be40916547d5c5f6a06ed5095e0>.
6. Candidate merge commit: <https://github.com/JDStraughan/html5-snake/commit/4e3049553b316c05c53befab6a51ada88d14d41e>.
7. Current GitHub Terms of Service, effective `2026-04-27`, Section D.6 Contributions Under Repository License: <https://docs.github.com/en/site-policy/github-terms/github-terms-of-service>.
8. GitHub announcement that the explicit default contributor license was newly added and became effective `2017-02-28`: <https://github.blog/news-insights/new-github-terms-of-service/> and <https://github.blog/news-insights/new-github-terms-of-service-are-in-effect/>.

## Supported claims

- The repository already contained the full MIT permission grant and Jason D. Straughan copyright notice at base commit `ab188d1328f1c38ac22ace820f614cac2122e3cf`, before PR #1 was opened and merged.
- PR #1 was authored by GitHub user `themightychris`, contained one commit, changed only `game.js`, and was merged on `2013-03-07T02:25:46Z`.
- The PR body describes variable declarations, spacing/style corrections, and replacing an `Object.prototype` extension with a normal function. The patch reports `28` additions and `27` deletions; most changes are formatting, but some are functional source edits.
- No separate CLA, DCO, explicit MIT declaration, copyright assignment, or license statement appears in the fetched PR body or its empty comment set.
- Current GitHub Terms explicitly apply repository-license terms to contributions, but GitHub's own 2017 announcement says this explicit default contributor license was newly added and became effective on `2017-02-28`, nearly four years after this PR.
- Therefore current Section D.6 is evidence of today's platform rule and open-source norm, not sufficient evidence that the exact 2013 contribution was contractually licensed under that later clause.
- The existing internal, unmerged specimen effect ceiling remains materially lower risk than publication. The exact candidate may continue through internal technical verification while the license verdict stays qualified.

## Excluded claims

- This is not a legal opinion and does not conclude that the 2013 contribution is unlicensed, infringing, or unusable.
- No archived GitHub Terms effective on `2013-03-07` were recovered in this bounded pass.
- No contributor identity, employer agreement, contributor-side license record, email, or off-platform agreement was investigated.
- No claim is made that formatting changes or every individual patch hunk is copyrightable.
- Preserving attribution alone does not cure a missing license grant if one were actually required.
- No browser/runtime, zero-network, dependency, trademark, originality, buyer, revenue, or app-store claim is made.

## License and terms uncertainty

- Strong signal: full MIT text existed before the contribution and remained in the candidate snapshot; the maintainer deliberately merged a PR submitted to that licensed repository.
- Residual uncertainty: the only explicit platform-wide inbound-equals-outbound clause found is documented as a 2017 addition, after the 2013 contribution. The PR itself contains no express license statement.
- Low-cost internal rule: preserve the complete README MIT text verbatim and record PR #1 plus contributor commit in the specimen's provenance inventory.
- Public-distribution rule: do not label the chain of title fully cleared solely from current GitHub Terms. Before publication, either obtain a stronger historical or contributor-bound license record, receive legal acceptance, or rebind the distributable source to pre-PR base `ab188d1328f1c38ac22ace820f614cac2122e3cf` and independently implement the needed command seam and fixes without copying the PR patch.

## Strongest objection

The strongest objection is that contribution to a repository already displaying a full MIT license, followed by deliberate maintainer merge, is ordinarily understood as inbound under the same license; GitHub's current Terms call this a widely accepted open-source norm. For a tiny internal specimen, treating the residual risk as a blocker would be disproportionate.

That objection is accepted for internal execution but not for a zero-trust claim of publication-ready chain of title. The explicit GitHub default contributor clause was introduced in 2017, so applying it retroactively to a 2013 PR would overclaim.

## Cost and operator-minute estimate

- This research pass: `$0` external spend; `0` operator minutes.
- Internal provenance revision: `10–20 producer minutes` to add exact upstream/base/PR/commit bindings and preserve the MIT text; `10–15 verifier minutes` to confirm the inventory.
- Lower-risk distributable rebind: `20–40 producer minutes` to start from `ab188d1328f1c38ac22ace820f614cac2122e3cf` and independently implement the already-required guarded direction seam; `15–30 verifier minutes` to diff against the external PR and confirm no copied patch dependency.
- Legal review or contributor outreach is outside this WorkItem and is not authorized by this card.

## Falsifier

This `REVISE` upgrades to `ADMIT_PUBLICATION_LICENSE_GATE` if a verifier binds any one of the following to the exact contributor and contribution:

1. GitHub Terms effective on `2013-03-07` containing an applicable same-license contribution grant;
2. an explicit MIT/compatible license statement from `themightychris` for commit `7d11cf1729e03be40916547d5c5f6a06ed5095e0`;
3. a CLA/DCO or other agreement covering PR #1; or
4. a legal review accepting the repository-license and merge facts as sufficient for the intended distribution.

It falls to `RETIRE_EXACT_MERGED_SNAPSHOT_FOR_DISTRIBUTION` if a credible conflicting ownership or license claim appears. It becomes operationally moot if the consumer rebinds the distributable specimen to the pre-PR base and a verifier confirms independent implementation.

## Verifier

- Structural verifier: S04 may confirm task binding, exact source pointers, scope, expiry, and internal consistency; same-provider weight remains zero.
- License/provenance verifier: a distinct nonproducer should retrieve the exact PR/commit history, attempt to recover the GitHub Terms effective on `2013-03-07`, and produce a digest-bound provenance manifest.
- Technical verifier remains the distinct browser-capable nonproducer named by the current WorkItem; technical `STOOD` does not imply license-chain `STOOD`.

## Consumer

- Immediate: `SPATIAL_FACTORY_HTML5_SNAKE_PENDING_DIRECTION_COMMAND_GATE_001`, S02/S06/S07 routing chain, and S09 decision seat.
- Consumption rule: internal unmerged specimen work may proceed after its existing structural and executor gates. ConsumerAck for any public distribution claim must remain withheld until the provenance gate above is resolved or the source is rebound to the pre-PR base.
- This card does not mutate, pause, route, merge, publish, or retire the current WorkItem.

## Expiry

- Evidence expiry: `2026-08-10T22:28:39Z`.
- Immediate invalidation on change to the exact upstream/base/contributor commits, PR record, GitHub historical-terms evidence, intended effect ceiling, or named consumer.

## Disposition

**REVISE — INTERNAL SPECIMEN MAY CONTINUE; PUBLIC-DISTRIBUTION LICENSE GATE NOT STOOD.**

The pre-existing MIT notice and deliberate merge are strong enough for the current quarantined internal experiment, but the exact 2013 external contribution cannot be declared fully covered by GitHub's explicit inbound-equals-outbound clause because that clause was introduced in 2017. Preserve exact provenance now; before publication, bind historical/contributor license evidence or rebase the distributable specimen to the pre-PR MIT source and independently implement the required fixes.

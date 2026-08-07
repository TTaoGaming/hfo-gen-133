---
schema_id: hfo.gen133.s08.research_evidence_card.v1
seat: S08_RESEARCH_AND_CANDIDATE_SCOUT
result: RETIRE
result_scope: RETIRE_FROM_PERMISSIVE_LICENSE_SHORTLIST_ONLY
wip: 1
carrier_task_id_expected: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_observed: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_match: true
canonical_repository: TTaoGaming/hfo-gen-133
canonical_branch: agent/gen133-bootstrap-20260730
valid_time_utc: 2026-08-07T05:29:10Z
expiry_utc: 2026-09-06T05:29:10Z
lane: SPATIAL_FOSS_CANDIDATES_AND_LICENSES
bounded_uncertainty: WHETHER_ELLISONLEAO_CLUMSY_BIRD_IS_A_PERMISSIVELY_LICENSED_FOSS_CANDIDATE_OR_IS_GPL3_COPYLEFT_DESPITE_STALE_MIT_CATALOG_LABELS
candidate_repository: ellisonleao/clumsy-bird
candidate_default_branch: master
candidate_license_anchor_commit: fae3d487d5102af29fb3f78431cbd45e9b83aed3
candidate_license_anchor_commit_date_utc: 2017-06-16T16:16:38Z
candidate_license_anchor_commit_message: Change LICENSE to GPLv3
candidate_current_master_license_blob_sha1: 9cecc1d4669ee8af2ca727a5d8cde10cd8b2d7cc
candidate_archive_date: 2019-08-07
candidate_archive_status_observed_utc: 2026-08-07T05:29:10Z
operational_consumer: NOT_ASSIGNED
intended_consumer_surface: NEXT_SPATIAL_FOSS_CANDIDATE_SELECTION_WORKITEM
consumer_ack: NOT_OBSERVED
fitness_credit: 0
paid_cost_usd_observed: 0
operator_minutes_removed_measured: 0
research_effort_estimate_minutes: 8_to_15
independent_license_and_asset_provenance_verification_estimate_minutes: 30_to_60
verifier: S04_STRUCTURAL_PREFLIGHT_PLUS_DISTINCT_LICENSE_AND_ASSET_PROVENANCE_REVIEW_OF_EXACT_PINNED_CANDIDATE_IF_A_WORKITEM_LATER_CONSUMES_IT
---

# S08 evidence card — Clumsy Bird license catalog contradiction

## Decision

**RETIRE from a permissive-license / closed-distribution candidate shortlist.** Do **not** retire it from every possible use: GPLv3 permits commercial distribution when its conditions are met. The bounded failure is the permissive-license assumption, not commercial usability in general.

## Changed research question

X13 CURRENT v152 closes the Gmail campaign and directs the next wake to select a new candidate. S08 rotation returns to the spatial FOSS/license lane. A Gen-133 repository search found no prior `Clumsy-Bird` / `clumsy-bird` S08 evidence card, so this is not a duplicate candidate question.

## Primary evidence

1. **Authoritative repository:** `https://github.com/ellisonleao/clumsy-bird`, observed 2026-08-07. GitHub marks the repository **archived since 2019-08-07**, read-only, and renders its license as **GPL-3.0**.
2. **Exact current license object:** `LICENSE.md` on `master` has Git blob SHA-1 `9cecc1d4669ee8af2ca727a5d8cde10cd8b2d7cc` and begins `GNU GENERAL PUBLIC LICENSE / Version 3, 29 June 2007`.
3. **Exact license anchor commit:** `fae3d487d5102af29fb3f78431cbd45e9b83aed3`, dated 2017-06-16, commit message `Change LICENSE to GPLv3`. Fetching `LICENSE.md` at that commit yields the same blob SHA-1 as current `master`, so later repository state observed here has not changed that license file.
4. **GPLv3 consequence relevant to this shortlist:** the license explicitly allows charging for conveyed copies, but modified source versions conveyed to recipients must satisfy GPLv3 conditions, including licensing the covered work as a whole under GPLv3 and providing corresponding source for non-source conveyance as required.

## Contradictory secondary evidence

Historical/stale `awesome-selfhosted` catalog entries label Clumsy Bird as `MIT`, including an entry visible in a 2018-era mirror. A current ecosystem catalog that aggregates those lists still exposes the stale MIT label while separately identifying the GitHub repository itself as GPL-3.0. This is evidence of **catalog metadata drift**, not evidence that current authoritative repository rights are MIT.

## Supported claims

- The authoritative current repository license file is GPLv3, not MIT.
- The exact current `master` license blob is `9cecc1d4669ee8af2ca727a5d8cde10cd8b2d7cc`.
- Commit `fae3d487d5102af29fb3f78431cbd45e9b83aed3` introduced/changed the repository license to GPLv3 and is an exact license provenance anchor.
- GPLv3 does not prohibit charging money; commercial distribution is possible subject to GPL obligations.
- Clumsy Bird should not be admitted as a **permissively licensed** base merely because a third-party catalog says MIT.
- The repository is archived/read-only, which raises maintenance risk but does not revoke the license.

## Excluded claims

- No claim that GPLv3 forbids commercial use or paid distribution.
- No claim that every historical revision of Clumsy Bird was always GPLv3.
- No trademark, trade-dress, game-clone, character/art/audio, or other non-code IP clearance for `Flappy Bird`-related branding or assets.
- No exhaustive dependency-license or asset-provenance audit.
- No security, browser-compatibility, performance, accessibility, input-adapter, build reproducibility, or code-quality verdict.
- No buyer-demand inference from stars, forks, demos, or catalog inclusion.
- No claim that the exact repository HEAD commit equals the license-anchor commit; this card pins the license object and license-anchor commit, not an unverified code HEAD.

## License / terms uncertainty

The repository-level GPLv3 file is authoritative evidence for the repository's declared software license, but this pass did not prove that every bundled asset or dependency is owned by the same licensors or cleanly covered by GPLv3. Because the project is explicitly a Flappy Bird clone/port, non-code IP and branding clearance is a separate unresolved gate. If a future WorkItem consumes this candidate, it should pin an exact code commit and independently audit copied assets/dependencies before distribution.

## Strongest objection

**Objection:** GPLv3 is commercially usable, so retiring the project is overbroad.

**Answer:** Correct. The retirement is deliberately narrow: **from the permissive-license / proprietary-or-closed-distribution shortlist only**. An open-source commercial lane willing to satisfy GPLv3 obligations could still evaluate the project, subject to the unresolved asset/IP and maintenance risks above.

## Falsifier

Revise this decision if an authoritative upstream relicensing event or an exact historical code+asset commit selected by a real WorkItem is proven to carry a permissive license over all copied material relevant to that intended distribution. A stale catalog label, fork metadata, or README claim alone is insufficient.

## Verifier / consumer / expiry

- **Verifier:** `S04_STRUCTURAL_PREFLIGHT_PLUS_DISTINCT_LICENSE_AND_ASSET_PROVENANCE_REVIEW_OF_EXACT_PINNED_CANDIDATE_IF_A_WORKITEM_LATER_CONSUMES_IT`
- **Operational consumer:** `NOT_ASSIGNED`
- **Intended consumer surface:** next spatial FOSS candidate-selection WorkItem; no WorkItem consumption or ConsumerAck is claimed by this card.
- **Fitness:** `0` until a named WorkItem actually consumes the result.
- **Expiry:** `2026-09-06T05:29:10Z` because the repo is archived/static, while external catalog metadata and downstream selection context can still change.

## Honest flaw

This pass resolves only the **license-label contradiction**. It does not prove a distributable product package is legally clean, and it does not establish that Clumsy Bird is economically useful. The most consequential unknown is asset/non-code IP provenance around a Flappy Bird clone, which is intentionally outside this one bounded uncertainty.

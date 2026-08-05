---
schema_id: hfo.gen133.s08_evidence_card.v1
seat: S08_RESEARCH_AND_CANDIDATE_SCOUT
carrier_task_id_expected: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_observed: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_match: true
wip: 1
valid_time_utc: 2026-08-05T09:27:14Z
canonical_repository: TTaoGaming/hfo-gen-133
canonical_branch: agent/gen133-bootstrap-20260730
lane: spatial_foss_candidates_and_licenses
decision: ADMIT
expiry_utc: 2026-08-12T09:27:14Z
consumer: SPATIAL_FACTORY_HTML5_SNAKE_PENDING_DIRECTION_COMMAND_GATE_001_OR_FRESH_SUCCESSOR
verifier: DISTINCT_EXACT_SHA_ARCHIVE_AND_PACKAGED_NOTICE_INVENTORY_VERIFIER
---

# S08 evidence card — archived upstream is a maintenance boundary, not an automatic license retirement

## Bounded uncertainty

Does the current GitHub **archived** status of `JDStraughan/html5-snake` require retiring the exact pinned candidate from the internal HTML5 Snake canary on license grounds?

## Exact candidate

- Upstream repository: `JDStraughan/html5-snake`
- Exact source SHA: `e3fe18a85a0555f0540cc0978fbab62822262a91`
- Allowlisted files: `README.md`, `game.js`, `index.html`, `page.css`
- Current repository state observed 2026-08-05: public archive; GitHub displays that the owner archived it on 2024-10-22.

## Evidence

1. The current upstream repository page identifies the repository as archived and read-only, while still exposing the four candidate files and history. Source: https://github.com/JDStraughan/html5-snake (observed 2026-08-05; archive date displayed as 2024-10-22).
2. GitHub documents repository archival as making repository content and collaboration surfaces read-only and signaling that the project is no longer actively maintained. The archival documentation does not describe archival as changing file contents or license terms. Source: https://docs.github.com/en/repositories/archiving-a-github-repository/archiving-repositories (accessed 2026-08-05).
3. At exact SHA `e3fe18a85a0555f0540cc0978fbab62822262a91`, `README.md` contains the complete MIT permission, notice-retention condition, and warranty disclaimer with `Copyright (c) 2013 Jason D. Straughan`. Source: https://github.com/JDStraughan/html5-snake/blob/e3fe18a85a0555f0540cc0978fbab62822262a91/README.md (commit date 2013-02-19T00:10:27Z).
4. The exact pin is the commit titled `README for GitHub`, authored and committed through the `JDStraughan` GitHub identity, and adds the README containing that notice. Source: https://github.com/JDStraughan/html5-snake/commit/e3fe18a85a0555f0540cc0978fbab62822262a91 (2013-02-19T00:10:27Z).
5. GitHub's licensing guidance explicitly recognizes that a project may state its license in a README, while recommending a dedicated license file as a best practice. Source: https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository (accessed 2026-08-05).
6. The OSI-published MIT text grants broad copy, modification, publication, distribution, sublicensing, and sale permissions subject to retention of the copyright and permission notice. Source: https://opensource.org/license/mit (accessed 2026-08-05).

## Supported claims

- `UPSTREAM_ARCHIVED_READ_ONLY=true`
- `UPSTREAM_ACTIVE_MAINTENANCE=false_OR_NOT_EVIDENCED`
- `EXACT_PIN_CONTAINS_COMPLETE_MIT_NOTICE=true`
- `ARCHIVE_FLAG_ALONE_IS_NOT_A_LICENSE_RETIREMENT_SIGNAL=true`
- The exact pinned bytes remain admissible for the bounded internal canary when the complete MIT copyright, permission, and warranty text is retained in packaged derivative bytes.
- Archive status must be represented as a maintenance and supply-chain risk: no expectation of upstream fixes, review, releases, or security response.

## Excluded claims

- No claim that the MIT grant is judicially proven irrevocable in every jurisdiction.
- No claim that GitHub's archive flag proves copyright ownership, contributor authority, provenance completeness, noninfringement, or freedom from later rights disputes.
- No claim that the archived repository is secure, maintained, production-ready, or fit for public release.
- No claim that a README-only notice is better packaging than a local dedicated `LICENSE` or provenance surface.
- No public-distribution chain of title is stood by this card.

## License and terms uncertainty

- Exact pin license evidence: `MIT_NOTICE_PRESENT_IN_README`.
- Packaged derivative obligation: retain the full copyright and permission notice in all copies or substantial portions; retain the warranty disclaimer as part of the complete notice.
- Dedicated upstream `LICENSE` file: not evidenced at the exact pin.
- Contributor and third-party chain of title: `UNKNOWN` beyond the repository history and named copyright notice.
- GitHub Terms, DMCA history, trademark rights, and jurisdiction-specific enforceability: not evaluated.
- Public distribution remains `NOT_AUTHORIZED_BY_THIS_CARD` and `CHAIN_OF_TITLE_NOT_STOOD`.

## Strongest objection

An archived repository can be stale, abandoned, vulnerable, or later affected by a rights complaint. Correct: archive status increases maintenance and supply-chain risk. It does not, by itself, show that the exact historical MIT notice disappeared or that the archive operation changed the pinned files' stated license. The correct response is a maintenance/provenance gate, not automatic license retirement.

## Falsifier

Retire or revise this decision if any of the following is independently verified against the exact SHA or distributed bytes:

- the full MIT notice is absent, altered, or not shipped with substantial copied portions;
- the four allowlisted files differ from the exact pin without typed provenance;
- a verified upstream notice, takedown, court order, or rights-holder claim specifically disputes authority to license the pinned material;
- third-party code or assets inside the allowlist are identified with incompatible or missing terms;
- the consumer promotes this internal-canary admission into public distribution without a separate chain-of-title and packaging review.

## Verification contract

A distinct verifier should:

1. fetch the four files by exact SHA;
2. hash and inventory the fetched bytes;
3. confirm the repository archive flag separately from file/license content;
4. confirm the derivative package contains the complete local MIT notice without requiring external navigation;
5. confirm provenance records `upstream_archived=true`, `maintenance_status=UNMAINTAINED_OR_UNKNOWN`, and `public_distribution_chain_of_title=NOT_STOOD`;
6. fail closed on any mismatch, unavailable exact pin, missing notice, or discovered third-party term.

## Cost and operator-minute estimate

- This research pass: `$0`; `0 operator minutes`.
- Producer metadata and local notice amendment: `5–15 minutes`.
- Exact-SHA byte inventory and packaging check: `15–30 minutes`.
- Separate public-distribution provenance review, if ever authorized: `60–180+ minutes`; legal review cost excluded and unknown.

## Decision

`ADMIT`

Admit the exact pinned candidate only for the bounded internal canary with full MIT notice packaging and explicit archived/unmaintained provenance. Do not treat the archive flag as license revocation; do not treat this admission as public-distribution clearance.

## Fitness

`0` until an exact WorkItem consumes this card and a distinct verifier returns a bound verdict plus ConsumerAck.

## Effect boundary

No implementation, browser execution, dependency download, task mutation, account action, terms acceptance, outreach, application, purchase, send, spend, deployment, merge, release, public publication, or private-data use occurred. The only authorized effects are this internal Git evidence write, exact readback, and one material Slack pointer after readback.

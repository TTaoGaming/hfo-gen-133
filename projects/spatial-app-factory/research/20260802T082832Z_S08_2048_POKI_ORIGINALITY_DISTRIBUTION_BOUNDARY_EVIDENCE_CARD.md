---
schema_id: hfo.gen133.s08.evidence_card.v1
seat: S08_RESEARCH_AND_CANDIDATE_SCOUT
carrier_task_id_expected: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_observed: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_match: true
wip: 1
valid_time_utc: 2026-08-02T08:28:32Z
transaction_time_utc: SEE_GITHUB_COMMIT_METADATA
lane: distribution_and_buyer_evidence
question: Is the exact input-only 2048 spatial canary a credible Poki submission or revenue candidate under current Poki originality, access, technical, and deal requirements?
decision: RETIRE
fitness_credit: 0
fitness_condition: exact WorkItem ConsumerAck only
canonical_repository: TTaoGaming/hfo-gen-133
canonical_branch: agent/gen133-bootstrap-20260730
repository_head_observed_before_write: 0b8076060d9cc0acfb6dbee1804681db06244198
privacy_class: PUBLIC_PRIMARY_SOURCES_AND_SANITIZED_GIT_POINTERS_ONLY
verifier: distinct_nonproducer_distribution_reviewer_or_operator_authorized_platform_readback
consumers:
  - S09_STRATEGIC_REASONING_AND_VOTING
  - Olrun_or_current_spatial_factory_distribution_owner
  - any_future_distribution_WorkItem_for_the_2048_canary
expiry_utc: 2026-08-09T08:28:32Z
sealed: false
---

# S08 evidence card — retire the exact 2048 canary from Poki distribution

## Decision

**RETIRE the exact canary as a Poki submission, launch, or revenue candidate.**

Keep Poki only as a future candidate for a **materially original, rights-cleared, cross-device web game**. The current artifact is an internal adapter specimen layered onto an upstream project that describes itself as a clone. Poki's current quality guidance says it does not work with direct copies/clones or games that reuse templates or assets with little modification. The current canary changes an input seam and tests; it does not establish materially original gameplay, visual identity, game modes, content, or buyer fit.

This result does not retire the canary from internal conformance learning. It retires only the distribution/revenue interpretation.

## Self-probe and changed queue edge

```yaml
expected_task_id: 6a526109ba348191b5f23ad3172ad568
observed_task_id: 6a526109ba348191b5f23ad3172ad568
task_id_match: true
tools_observed:
  github: authenticated_search_fetch_write_exact_readback
  slack: authenticated_public_channel_write
  web: current_primary_documentation_read
  shell_or_browser_runtime: unavailable
  poki_account_or_submission_surface: not_accessed
  task_mutation: not_called
```

Changed queue edge:

- The prior S08 card at commit `5cf31404669117aceae24454ee8502140f321680` resolved one interaction uncertainty and narrowed the exact bridge to call-level behavior.
- S09 then issued `HOLD_FOR_BOUND_PRODUCER_CONTRACT_AND_REACHABLE_DISTINCT_VERIFIER` at commit `cd25b38b0bb4df08673fc4e7d640f3439c5a7680`.
- Explicit lane rotation therefore advances from interaction/input adapters to one bounded distribution uncertainty.
- Repository search found no prior Gen-133 Poki evidence card for this exact canary.

## Exact candidate scope

```yaml
integration_repository: TTaoGaming/TAGS
integration_commit: a3b636a7ecaab5afa1932ec92559c7c454904039
producer_branch: agent/spatial-2048-directional-bridge-repair-20260802T0424Z
bridge_path: prototypes/2048-spatial-canary/directional-bridge.js
bridge_blob: 1cedd74ea11a0199a3d7537b5b4136261307f309
test_path: prototypes/2048-spatial-canary/directional-bridge.test.js
test_blob: 92eaed8f2680f332e7bd62ca59724bb89b291bf0
upstream_repository: gabrielecirulli/2048
upstream_commit: 478b6ec346e3787f589e4af751378d06ded4cbbc
upstream_readme_blob: c947a03d4c63822e2ae79fd26de00fc4565e1292
platform_candidate: Poki_for_Developers
platform_docs_observed_utc: 2026-08-02
current_effect_ceiling: no_account_no_terms_no_submission_no_upload_no_publication_no_deal
```

The exact upstream README states that the project is a small clone of 1024, based on another 2048 clone, and indirectly inspired by Threes. The TAGS canary adds an app-local directional bridge and unit tests; it does not establish a materially original game.

## Dated primary/current sources — accessed 2026-08-02

1. Poki Quality Guidelines — Poki seeks original, high-quality games and states that it does not work with direct copies/clones or template/asset reuse with little modification:  
   https://sdk.poki.com/poki-quality-guidelines
2. Poki Working With Poki — access is limited/closed beta, submissions are hand-curated, and Poki evaluates quality, player fit, and web technical quality:  
   https://sdk.poki.com/
3. Poki Requirements — released games must support desktop, mobile, and tablet; satisfy aspect-ratio, SDK, privacy, and technical requirements:  
   https://sdk.poki.com/new-requirements
4. Poki External Resources — external requests are blocked by default and exceptions require approval and privacy documentation:  
   https://sdk.poki.com/external-resources
5. Poki Deal Types — current docs describe web-exclusive and non-exclusive structures, SDK obligations, performance duties, and a default five-year web-exclusivity term:  
   https://sdk.poki.com/deals
6. Poki Bonus Level — a separate current Poki docs page describes a seven-year default web-exclusivity term, conflicting with the Deal Types page:  
   https://sdk.poki.com/bonus
7. Poki Player Fit Test — the platform's own staged testing measures player behavior after access and prerequisites; it is not pre-submission demand proof:  
   https://sdk.poki.com/player-fit
8. Exact upstream README at the frozen commit:  
   https://github.com/gabrielecirulli/2048/blob/478b6ec346e3787f589e4af751378d06ded4cbbc/README.md
9. Exact current S08 repeat-suppression card:  
   https://github.com/TTaoGaming/hfo-gen-133/blob/5cf31404669117aceae24454ee8502140f321680/projects/spatial-app-factory/research/20260802T072820Z_S08_2048_DIRECTIONAL_BRIDGE_REPEAT_SUPPRESSION_BOUNDARY_EVIDENCE_CARD.md
10. Exact S09 successor-admission HOLD:  
    https://github.com/TTaoGaming/hfo-gen-133/blob/cd25b38b0bb4df08673fc4e7d640f3439c5a7680/state/coordination/votes/20260802T073224Z_S09_2048_REPEAT_SUPPRESSION_SUCCESSOR_ADMISSION_HOLD.vote.md

## Supported claims

- Poki is a curated distribution/publisher surface, not an open self-serve host with guaranteed acceptance.
- Current Poki guidance materially disfavors direct clones, heavily inspired games, and template/asset reuse with little modification.
- The exact upstream candidate self-identifies as a clone.
- The exact TAGS canary currently proves only a narrow app-local directional bridge and unit-test behavior. No evidence shows materially original gameplay, art direction, content, progression, game modes, or platform fit.
- A new input method alone is not documented by Poki as sufficient originality, and no Poki reviewer has evaluated this artifact.
- Poki requires cross-device web quality and additional platform integration. The current canary has no independent browser verdict, no mobile/tablet result, no 16:9 conformance result, no SDK integration, no performance evidence, and no platform review.
- Poki blocks external requests by default. This exact canary's future camera/hand-tracking path, permissions behavior, CSP treatment, and privacy acceptability are not documented or verified for Poki.
- Poki documents staged player testing and revenue/deal structures, but the current artifact has no access, test result, offer, accepted deal, payout, player metric, or buyer evidence.
- Current Poki documentation is internally inconsistent about default web-exclusivity duration: the Deal Types page says five years while the Bonus Level page says seven years. No exact term should be relied on without an actual current agreement readback.

## Excluded claims

- No claim that Poki would definitely reject every spatially controlled puzzle game.
- No claim that a materially redesigned game using a 2048-like mechanic can never qualify.
- No claim that MIT code licensing satisfies Poki originality, asset provenance, trademark, design-right, or contractual requirements.
- No claim that the camera API itself is prohibited. Its platform permission, privacy, iframe/CSP, mobile, and review status are `UNKNOWN`.
- No claim that Poki's advertised audience, testing pool, curation, or revenue split creates likely revenue for this developer or artifact.
- No claim about a specific revenue amount, acceptance probability, payout timing, flat-fee amount, effective exclusivity period, or retained margin.
- No account creation, submission, upload, SDK integration, reviewer contact, deal negotiation, terms acceptance, publication, or payment action occurred.
- No buyer demand, playtime, retention, conversion, ad yield, or product-market fit was invented.

## License and terms uncertainty

The exact upstream code is MIT-licensed, but code permission does not resolve originality or all non-code rights. Prior S08 evidence already separated bundled font/asset provenance from the root code license. Any future distribution candidate must bind exact code, fonts, images, audio, branding, screenshots, generated content, and trademark/title decisions to the final build.

Poki's public documentation is not a signed agreement and currently contains a material five-year-versus-seven-year exclusivity conflict. Revenue share descriptions, non-exclusive flat-license availability, performance duties, update obligations, content restrictions, and external-service approvals must be read from the actual agreement offered for the exact game. No agreement exists or was accepted in this run.

## Cost and operator-minute estimate

```yaml
direct_research_cost_usd: 0
operator_minutes_consumed_now: 0
account_or_terms_actions_now: 0
estimated_avoidable_submission_prep_minutes_for_this_exact_canary: 60_to_180
estimated_avoidable_terms_and_rights_review_minutes: 20_to_60
estimated_original_game_rework_minutes: UNKNOWN_and_out_of_scope
estimated_operator_minutes_saved_by_retirement_boundary: 20_to_60
estimate_status: unmeasured_planning_estimate_not_realized_relief
```

The useful saving is avoidance, not earned revenue: do not spend operator or engineering time preparing this exact clone-derived canary for Poki.

## Strongest objection

A camera/gesture control layer could create a novel player experience and may be a meaningful creative twist on a familiar mechanic. That is plausible. It does not overcome the current evidence boundary: the exact artifact has no integrated, independently verified camera experience, no original content package, and no Poki review. Calling the input seam alone sufficient differentiation would be demand and acceptance invention.

## Falsifier

This card is falsified only by one of the following exact changes:

1. Poki directly reviews and accepts the exact bound build despite its clone provenance; or
2. a materially original successor replaces the clone-derived product identity with source-bound original gameplay/content/art, clears all rights, passes cross-device and browser verification, integrates the required Poki contract, and receives a platform acceptance or signed offer.

A generic statement that Poki accepts puzzle games, an account invitation, a successful upload, a playtest request, page traffic, or SDK integration does not falsify this card.

Immediate expiry occurs on a material product-identity change, upstream replacement, new platform agreement, or changed Poki originality/deal terms.

## Verifier

- Primary verifier: a distinct nonproducer distribution reviewer comparing the exact build to current Poki requirements and originality rules.
- Strong verifier: operator-authorized direct Poki reviewer response or actual offered agreement bound to the exact game.
- S08, the bridge producer, and same-provider S09 do not self-grade acceptance.

## Consumer

- S09 should consume this as `NO_POKI_ROUTE_FOR_EXACT_2048_CANARY`.
- The spatial-factory distribution owner should keep Poki in a separate candidate pool only for materially original games.
- Any WorkItem proposing Poki submission for this exact canary must cite and explicitly overturn this card with falsifying evidence.
- Fitness remains `0` until a named WorkItem records `CONSUMED` or `REJECTED_WITH_EVIDENCE` against this exact Git blob.

## Expiry

`2026-08-09T08:28:32Z`, or immediately upon a material build/product-identity change, direct Poki acceptance, offered agreement, or changed Poki originality/deal documentation.

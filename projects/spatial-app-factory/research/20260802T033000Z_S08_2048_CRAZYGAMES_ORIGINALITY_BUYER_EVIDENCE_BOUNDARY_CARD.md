---
schema_id: hfo.gen133.s08.research_evidence_card.v1
card_id: S08_2048_CRAZYGAMES_ORIGINALITY_BUYER_EVIDENCE_BOUNDARY_20260802T033000Z
result: RETIRE
callsign_or_seat: S08_RESEARCH_CANDIDATE_SCOUT
carrier_task_id_expected: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_observed: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_match: true
carrier_identity_claim: DISPOSABLE_SCHEDULED_CARRIER_NOT_LINEAGE
controller: operator_direct
wip: 1
valid_time_utc: 2026-08-02T03:30:00Z
transaction_time_utc: SEE_GITHUB_COMMIT_METADATA
canonical_repository: TTaoGaming/hfo-gen-133
canonical_branch: agent/gen133-bootstrap-20260730
repository_head_observed_before_write: b9ee3ae65a257e5e096bc376fb33ecba87c92850
research_lane: distribution_and_buyer_evidence
bounded_uncertainty: WHETHER_EXACT_2048_SPATIAL_CANARY_IS_AN_ADMISSIBLE_CRAZYGAMES_BUYER_EVIDENCE_SUBMISSION
candidate_platform: CrazyGames
candidate_platform_contract: official_developer_docs_and_portal_observed_2026-08-02; HTML5_SDK_V3
candidate_repository: gabrielecirulli/2048
candidate_commit: 478b6ec346e3787f589e4af751378d06ded4cbbc
candidate_readme_blob: c947a03d4c63822e2ae79fd26de00fc4565e1292
current_work_item: SPATIAL_FACTORY_GOLDEN_APP_001_2048_DIRECTIONAL_BRIDGE_001
current_work_item_status: HOLD_CLAIM_NOT_STRUCTURALLY_ROUTABLE
current_hold_commit: b9ee3ae65a257e5e096bc376fb33ecba87c92850
current_hold_blob: 75f47b3faf64c9415814f850814b0328bdd363aa
privacy_class: PUBLIC_PRIMARY_SOURCES_AND_SANITIZED_REPOSITORY_POINTERS_ONLY
effect_ceiling: RESEARCH_CARD_AND_SANITIZED_SLACK_POINTER_ONLY
verifier: S04_STRUCTURAL_PREFLIGHT_THEN_SIGRUN_P4_OR_OTHER_DISTINCT_NONPRODUCER_PLATFORM_REVIEW
consumer:
  - S02_ADMISSION_PULL
  - S09_PRODUCT_DECISION_QUEUE
  - SPATIAL_APP_FACTORY_BACKLOG_OWNER
fitness_credit: 0_PENDING_EXACT_WORKITEM_CONSUMPTION
expiry_utc: 2026-08-09T03:30:00Z
sealed: false
---

# S08 evidence card — retire the exact 2048 canary from CrazyGames submission

## Changed queue evidence

The prior S08 result resolved the interaction/input-adapter lane by requiring an app-local semantic direction bridge. S02 then admitted an exact branch/file/test claim, but S04 and S06 found incomplete immutable task/WIP bindings and S07 returned `HOLD` without creating a branch or running code. The explicit lane rotation therefore advances to one distribution-and-buyer-evidence uncertainty while preserving global WIP=1.

This card does not reopen publication. It asks whether the exact internal 2048 canary is worth carrying forward as a CrazyGames submission candidate after the internal bridge closes.

## Bounded question

Can `gabrielecirulli/2048@478b6ec346e3787f589e4af751378d06ded4cbbc`, changed only by a spatial-input direction bridge and rebranding necessary to remove upstream “official” language, be admitted as a CrazyGames Basic Launch candidate for real buyer/player evidence without a materially new product design?

## Decision

`RETIRE` the **exact 2048 spatial canary** from the CrazyGames distribution lane.

CrazyGames states that initial QA may reject unoriginal content such as clones or asset flips, requires names/assets/overall content to exhibit originality, and says revenue-share eligibility requires a game to be original and clearly distinguishable from existing games. The exact upstream README describes this repository as a clone of 1024, based on another 2048 clone, indirectly inspired by Threes. The current WorkItem adds only an input bridge and explicitly avoids changing the game core. That is useful for internal adapter verification but is the wrong artifact to spend submission, SDK, metadata, QA, payment-onboarding, or operator time on.

CrazyGames remains a plausible later evidence surface for a materially original web game. That would be a new product WorkItem, not a distribution step for this canary.

## Self-probe

```yaml
expected_task_id: 6a526109ba348191b5f23ad3172ad568
observed_task_id: 6a526109ba348191b5f23ad3172ad568
task_id_match: true
tools_observed:
  github: authenticated_repository_read_and_branch_scoped_create_with_exact_readback
  slack: authenticated_channel_read_write
  web_primary_sources: available_and_used
  native_task_inventory: not_mutated
  shell_or_browser_runtime: unavailable
  crazygames_account_or_portal: not_accessed
```

## Exact candidate and current WorkItem state

```yaml
upstream_repository: gabrielecirulli/2048
upstream_commit: 478b6ec346e3787f589e4af751378d06ded4cbbc
upstream_license_family: MIT_CODE_LICENSE_WITH_NOTICE_PRESERVATION
upstream_self_description: CLONE_OF_1024_BASED_ON_ANOTHER_2048_CLONE_INDIRECTLY_INSPIRED_BY_THREES
bridge_target_repository: TTaoGaming/TAGS
bridge_frozen_base: e0e3125e1ef6bb33e189c91b485ec341f2d3cd52
bridge_allowed_scope: CREATE_ONLY_UNDER_prototypes/2048-spatial-canary/**
bridge_product_change: INPUT_DIRECTION_ADAPTER_ONLY
current_execution_status: HOLD_BEFORE_BRANCH_OR_TEST
publication_authority: NONE
```

## Dated primary/current sources inspected

Observed `2026-08-02`:

1. CrazyGames developer documentation, “Introduction”: Basic Launch is a temporary limited-audience two-week test with monetization disabled; Full Launch requires full implementation and is selected using average playtime, gameplay conversion, and retention. https://docs.crazygames.com/
2. CrazyGames FAQ: initial QA can reject unoriginal content including clones or asset flips; monetization eligibility requires original content clearly distinguishable from existing games; submissions require a web build, SDK integration, metadata, and cover assets. https://docs.crazygames.com/faq/
3. CrazyGames gameplay requirements: game names, assets, and overall content should exhibit originality; submitted games must satisfy responsive readability, smooth performance, and platform content rules. https://docs.crazygames.com/requirements/gameplay/
4. CrazyGames technical requirements: Basic Implementation limits total size/files and initial download; Full Implementation requires SDK gameplay start/stop events and other applicable modules. https://docs.crazygames.com/requirements/technical/
5. CrazyGames SDK introduction: HTML5 SDK v3 is loaded from CrazyGames, initialized asynchronously, exposes platform-specific environments, and the Developer Portal preview is the realistic QA surface. https://docs.crazygames.com/sdk/intro/
6. CrazyGames payouts documentation: payment onboarding uses Tipalti; payout requires account/billing information and a minimum €100 accrued balance; methods and fees vary by country. https://docs.crazygames.com/payouts/
7. CrazyGames Developer Portal marketing page: the platform advertises a large audience, analytics, ads, and support, but ties success to engagement, reviews, and retention. https://developer.crazygames.com/
8. Exact upstream README at `gabrielecirulli/2048@478b6ec346e3787f589e4af751378d06ded4cbbc`, blob `c947a03d4c63822e2ae79fd26de00fc4565e1292`: explicitly describes the game as a clone and uses “official app” branding. https://github.com/gabrielecirulli/2048/blob/478b6ec346e3787f589e4af751378d06ded4cbbc/README.md
9. Current S07 hold receipt, commit `b9ee3ae65a257e5e096bc376fb33ecba87c92850`, blob `75f47b3faf64c9415814f850814b0328bdd363aa`: the bridge remains branch/file/test-only and no branch, command, test, deployment, or publication occurred.

## Supported claims

- CrazyGames can provide a bounded limited-audience Basic Launch and source-system engagement metrics for an accepted game.
- Basic Launch does not itself monetize; progression to Full Launch depends on platform-observed engagement metrics.
- Originality is an explicit submission and monetization gate, not an optional optimization.
- The exact upstream candidate self-identifies as a clone; the current bridge contract adds spatial input without materially changing name, art, progression, content, or core mechanics.
- A spatial input bridge may be technically interesting while still failing the platform’s originality/product-differentiation gate.
- SDK integration, metadata, QA, portal setup, and payout onboarding are avoidable work for this exact canary because the candidate fails the earlier product-fit gate.
- CrazyGames telemetry could become buyer/player evidence only after an accepted, independently verified, rights-cleared, materially original game exists.

## Excluded claims

- No claim that CrazyGames would certainly reject the exact build; no submission or platform review occurred.
- No legal conclusion is made about game mechanics, copyright, trademark, trade dress, clone lineage, or whether any renamed derivative is lawful.
- No claim that adding spatial input can never create differentiation; only that the current input-only WorkItem does not establish enough originality for platform admission.
- No acceptance probability, player count, conversion rate, retention, RPM, revenue, payout date, or user-acquisition value is estimated.
- The platform’s audience and zero-UA claims are treated as vendor statements, not independent proof of traffic or revenue for this candidate.
- No account was created, terms accepted, build uploaded, SDK integrated, metadata submitted, payment profile completed, or publication attempted.
- No claim that CrazyGames is unsuitable for future original spatial games.

## License, terms, and provenance uncertainty

The MIT code license supports code reuse subject to notice preservation, but it does not satisfy CrazyGames originality review, clear “official” branding, prove rights in every asset/contribution, or resolve clone/provenance concerns. Platform submission would also require then-current developer terms, privacy/data handling review, account/billing information, and distribution-right warranties that were not accessed or accepted in this wake.

A future original game must bind its final build SHA to exact code and asset licenses, contributor provenance, marks/branding, SDK version, platform requirements, and payout terms. Do not infer those rights from this upstream repository’s MIT notice alone.

## Cost and operator-minute estimate

```yaml
direct_research_cost_usd: 0
operator_minutes_required_now: 0
cost_avoided_by_retiring_exact_canary: SDK_METADATA_PORTAL_QA_AND_PAYOUT_ONBOARDING_WORK_NOT_STARTED
estimated_sdk_and_platform_integration_minutes_if_wrongly_pursued: 90_to_240
estimated_metadata_cover_qa_packaging_minutes_if_wrongly_pursued: 60_to_180
estimated_operator_terms_billing_review_minutes_if_wrongly_pursued: 20_to_45
estimated_material_original_product_redesign_hours: 8_to_40_PLUS; NOT_CURRENT_WORKITEM_SCOPE
measured_buyer_evidence: NONE
measured_operator_minutes_removed: 0
```

## Strongest objection

Spatial hand/gesture control could be a meaningful differentiator, and CrazyGames already hosts many 2048-like games. Therefore the platform might accept a polished spatial version.

The objection is not enough to admit this artifact. The official gate concerns the game’s name, assets, and overall content, while the current WorkItem intentionally changes only input and preserves the upstream core. Existing similar listings are not a current submission promise, and no direct platform source says an input modality alone makes a clone clearly distinguishable.

## Falsifier

Revise this `RETIRE` result only if one of the following becomes exact, current, and source-bound:

1. CrazyGames provides written pre-submission guidance for this exact build/SHA that the spatial interaction and rebranding satisfy its originality gate; or
2. a new WorkItem materially changes product identity—original name, art, content/progression, UX, and rights-cleared assets—while preserving only the tested adapter pattern, and S09 plus the backlog owner explicitly admit it as a separate original-game candidate; or
3. current official requirements remove or materially narrow the originality/clone gate.

Even then, admission requires a local/browser PASS, exact build manifest, current SDK integration plan, rights review, measurable Basic Launch success criteria, stop condition, cost ceiling, and separate authority for account/terms/upload/publication effects.

Immediate reinforcement of `RETIRE` occurs if the candidate remains a renamed 2048 clone with only input changes, relies on upstream “official” branding/assets, or proposes success from submission, page views, or vendor audience claims rather than accepted platform telemetry.

## Verifier, consumer, expiry

- **Structural verifier:** S04 may verify exact candidate, source, hold, authority, and expiry bindings; same-provider weight remains zero.
- **Distinct verifier:** Sigrun/P4 or another authorized nonproducer may challenge the interpretation against current CrazyGames requirements and the exact candidate bytes.
- **Consumer:** S02 and S09 should consume this card to prevent CrazyGames packaging/submission scope from entering the current internal bridge WorkItem. The backlog owner may preserve CrazyGames only as a future channel for a separate materially original app.
- **Expiry:** `2026-08-09T03:30:00Z`; recheck current platform requirements before any future admission.

## Credit rule and honest flaw

This card earns zero fitness until an exact WorkItem or decision receipt records `CONSUMED` or `REJECTED_WITH_EVIDENCE` against its Git commit/blob. It produced no buyer, player, account, submission, SDK integration, browser run, revenue, or independent verdict.

The conclusion is a pre-submission product-fit gate, not a platform decision. CrazyGames may apply judgment differently, its documentation can change, and current listings were not treated as normative evidence. The narrow result is only that the exact input-only 2048 canary should stop at internal adapter verification rather than becoming the next CrazyGames submission candidate.

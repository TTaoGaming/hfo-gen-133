---
schema_id: hfo.gen133.s08.research_evidence_card.v1
card_id: S08_ITCHIO_RESTRICTED_HTML5_DEMO_20260801T073245Z
result: REVISE
callsign_or_seat: S08_RESEARCH_CANDIDATE_SCOUT
carrier_task_id_expected: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_observed: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_match: true
carrier_identity_claim: DISPOSABLE_SCHEDULED_CARRIER_NOT_LINEAGE
controller: operator_direct
wip: 1
valid_time_utc: 2026-08-01T07:32:45Z
transaction_time_utc: SEE_GITHUB_COMMIT_METADATA
canonical_repository: TTaoGaming/hfo-gen-133
canonical_branch: agent/gen133-bootstrap-20260730
repository_head_observed_before_write: aace7cd805c4ddfecf97fd6ec22982ec6e7a949e
work_item_id: SPATIAL_FACTORY_GOLDEN_APP_001
research_lane: distribution_and_buyer_evidence
candidate: itch.io_restricted_or_unlisted_HTML5_project_page
candidate_contract_version: official_docs_observed_2026-08-01_terms_updated_2023-04-15
privacy_class: PUBLIC_PRIMARY_SOURCES_AND_SANITIZED_REPOSITORY_POINTERS_ONLY
expiry_utc: 2026-08-08T07:32:45Z
verifier: Sigrun/P4_APEX_FALSIFICATION_or_other_distinct_provider_nonproducer
consumers:
  - Olrun/Claude-Dispatch_as_spatial_factory_coordinator
  - S09_task_6a539fb148bc8191a30b6009dbf22438
sealed: false
---

# S08 evidence card — itch.io is a plausible later restricted HTML5 demo surface, not a current deployment or buyer proof

## Changed queue evidence

The interaction/input uncertainty changed materially: S07 returned an adapter-level patch for `SPATIAL_FACTORY_GOLDEN_APP_001` at Gen-133 commit `aace7cd805c4ddfecf97fd6ec22982ec6e7a949e`, bound to claim `4ecc5350fe918b1ff466708a148dc0012f810ab8`. The target branch is now `TTaoGaming/TAGS@1f0c0a7831db6f4476a703856855ff7ccc4f454b`, with deterministic adapter tests reported green but browser wiring, the FAB smoke test, independent verdict, and ConsumerAck still absent. This consumes the prior S08 interaction question only at producer-return level and rotates the explicit lane to distribution/buyer evidence.

Repository search found no prior Gen-133 itch.io evidence card. The earlier distribution card evaluated GitHub Pages, a materially different host and terms surface.

## Bounded question

After the exact golden-app artifact is independently verified and accepted, can itch.io provide one restricted or unlisted HTML5 demo surface for a measured buyer experiment without treating hosting, views, downloads, donations, or marketplace exposure as proof of demand—and without assuming camera access, license clearance, or current publication authority?

## Decision

`REVISE` the future distribution plan.

itch.io can host HTML/JavaScript/CSS projects and supports Draft, Restricted, Public, and public-unlisted access modes. That makes it a credible candidate for a later bounded demo or packaging experiment. It is not admissible for the current WorkItem because the current effect ceiling forbids publication, an itch.io account and terms acceptance are consequential actions, exact repository license/provenance remains unresolved, and the current producer return explicitly leaves browser integration and FAB smoke behavior unproven.

Even later, use itch.io only as a distribution and measurement surface. A page view is exposure, a download is acquisition, and a donation or purchase is payment evidence; none alone proves repeatable buyer demand, product fit, retained margin, accessibility, or camera-capable spatial input.

## Self-probe

```yaml
expected_task_id: 6a526109ba348191b5f23ad3172ad568
observed_task_id: 6a526109ba348191b5f23ad3172ad568
task_id_match: true
tools_observed:
  native_tasks_inventory: authenticated_read
  github_connector: authenticated_read_write_and_exact_file_readback
  slack_public_channel: authenticated_write
  web_primary_docs: read
  shell_or_browser_runtime: unavailable
  itch_account_or_settings: not_accessed
  native_task_mutation: not_called
```

## Exact candidate and artifact state

```yaml
platform_candidate: itch.io HTML5 project hosting
platform_mode_candidate: Restricted_or_Public_Unlisted_after_separate_authority
artifact_repository: TTaoGaming/TAGS
artifact_branch: agent/spatial-golden-app-001-20260731
artifact_head_observed: 1f0c0a7831db6f4476a703856855ff7ccc4f454b
artifact_entry_candidate: prototypes/fab-prototype.html
adapter_path: prototypes/spatial-input-adapter.js
adapter_blob_at_head: ca327ea46049f499d0afe1be4f9632ee086f2637
test_path: tests/spatial-input-adapter.test.mjs
test_blob_at_head: 2e523f5c373203ae4f5e0f1a48a52d1570f0682a
producer_return: aace7cd805c4ddfecf97fd6ec22982ec6e7a949e
current_status: PATCH_RETURNED_NOT_INDEPENDENTLY_VERIFIED_NOT_CONSUMER_ACKED
```

The current HTML was unchanged by the patch and exact producer evidence says it does not reference `spatial-input-adapter.js`; therefore it is not yet an upload-ready integrated golden app.

## Primary/current sources observed 2026-08-01

1. itch.io, “Uploading HTML5 games”: supports any HTML/JavaScript/CSS project; multi-file projects require a ZIP containing `index.html`; assets use relative, case-sensitive paths; projects execute inside an iframe; HTML5 payments are donations unless access is sold as a downloadable project. https://itch.io/docs/creators/html5
2. itch.io, “Controlling who can access your project”: Draft is owner/secret-link access, Restricted supports approved users or a password and is excluded from browse/search/external indexing, Public can be unlisted from search and browse. https://itch.io/docs/creators/access-control
3. itch.io, “Your first itch.io page”: a free account is required, and the dashboard exposes views, downloads, purchases, and payment administration. https://itch.io/docs/creators/getting-started
4. itch.io, “Content creator quality guidelines”: discovery eligibility is conditional; public pages should be ready before first publication; Draft and Restricted pages are not browse/search releases. https://itch.io/docs/creators/quality-guidelines
5. itch.io Terms of Service, page updated 2023-04-15 and observed 2026-08-01: registration/use binds the terms; publishers warrant distribution rights; uploading grants service and user licenses described by the terms. https://itch.io/docs/legal/terms
6. itch.io, “Accepting Payments and Getting Paid”: payment routes use PayPal or Stripe; documented typical processor fees are `$0.30 + 2.9%`; selling and payouts introduce provider, tax, seller-term, fee, and account obligations. https://itch.io/docs/creators/payments
7. MDN, `MediaDevices.getUserMedia()`: camera/microphone require a secure context, explicit user permission, and iframe delegation through Permissions Policy when not in the top-level document. https://developer.mozilla.org/en-US/docs/Web/API/MediaDevices/getUserMedia

## Supported claims

- A future static multi-file build can fit itch.io's HTML5 upload contract if it is packaged as a ZIP with `index.html`, all required files, relative paths, and correct case.
- Restricted mode can support a bounded named-reviewer demo without browse/search indexing; public-unlisted can reduce discovery exposure but remains a publication effect.
- The platform dashboard can provide direct source-system counts for views, downloads, and purchases after an authorized experiment.
- itch.io is potentially a stronger buyer-experiment surface than GitHub Pages when the intended experiment needs project-page metadata, restricted access, download keys, or payment telemetry.
- Incremental hosting cost may be `$0` for a basic page, but account creation, terms acceptance, seller configuration, payment providers, tax handling, processor fees, and operator review are separate costs and effects.
- The current TAGS branch is not ready for this platform: the adapter-level return has no integrated HTML script reference, browser run, smoke-test result, independent verdict, or ConsumerAck.
- itch.io documentation confirms iframe hosting, but it does not establish that the exact embed delegates camera access. Camera-capable spatial behavior remains `UNKNOWN` until direct browser and Permissions-Policy evidence exists.

## Excluded claims

- No account was created, terms accepted, page configured, ZIP uploaded, access key generated, payment route connected, or project published.
- No claim that Restricted or unlisted access is confidential, NDA-grade, immune to link/password sharing, or appropriate for private data.
- No claim that itch.io permits or successfully runs camera input for the exact artifact.
- No claim that views, downloads, followers, ratings, donations, or purchases prove product-market fit, repeat demand, buyer identity, retained margin, or customer success.
- No claim that marketplace audience statistics guarantee discovery or fit for a non-game spatial tool.
- No claim that the current TAGS repository has complete distribution rights. `package.json` declares MIT at the pinned base, but the root `LICENSE` file was absent when directly queried and third-party asset/provenance review is not closed.
- No browser, accessibility, mobile, cross-browser, privacy, payment, deployment, publication, independent-verification, or ConsumerAck PASS is established.

## License and terms uncertainty

The exact platform terms require the publisher to hold the necessary rights and grant licenses upon submission. The repository's package metadata alone is insufficient publication clearance. Before any upload, bind the final producer SHA to an exact license text, copyright ownership, third-party assets, fonts/images/audio, and any model or generated-content disclosures required by current platform rules.

The terms page states that users retain a license to submitted content even after removal within the service's described functionality. A restricted experiment therefore remains a distribution decision, not an equivalent of a reversible local preview.

## Cost and operator burden

```yaml
direct_research_cost_usd: 0
operator_minutes_required_now: 0
new_credentials_or_terms_required_now: 0
estimated_future_packaging_specimen_minutes: 10_to_20
estimated_future_account_terms_rights_review_minutes: 20_to_45
estimated_future_restricted_page_setup_and_browser_probe_minutes: 15_to_30
estimated_operator_minutes_avoided_by_prebinding_gates: 10_to_20
payment_cost_if_enabled: processor_and_platform_share_apply; no_payment_route_authorized
cost_uncertainty: account_state_tax_region_payment_mode_and_current_terms_not_read_back
```

## Strongest objection

itch.io is a game-centric iframe marketplace. Selecting it can optimize for a convenient public artifact rather than the actual buyer. The current page is not wired to the adapter, the spatial product's camera path is absent/unproven, and iframe camera permission may fail. A restricted itch.io page could therefore consume operator time while producing only vanity telemetry and no qualified buyer action.

## Falsifier

Revise toward `ADMIT` only after one separate authorized WorkItem proves all of the following against an independently accepted producer SHA:

1. exact license and asset provenance permit distribution under the then-current itch.io terms;
2. a local no-upload package specimen has `index.html`, relative paths, case-correct assets, and no missing network dependencies;
3. the complete FAB smoke test and a real browser run pass;
4. if camera input is included, direct response-header/iframe inspection and at least two browser families prove the required permission flow;
5. Restricted or unlisted visibility is read back from the actual project settings;
6. the experiment names one buyer class and one action stronger than a page view, such as a qualified tester completing a defined task, requesting follow-up, downloading an evaluation build, or producing source-system payment evidence;
7. exact operator minutes, direct cost, and stop condition are recorded.

Immediate `RETIRE` conditions for itch.io in this lane:

- the intended buyer is materially mismatched with a game-marketplace page;
- the embed cannot support required camera permissions or native fallback;
- distribution rights remain ambiguous;
- private or sensitive data would enter the artifact or telemetry;
- success is declared from publication, page views, or platform audience claims;
- account, terms, upload, publication, or payment is attempted without separate operator authority.

## Reversible next experiment

Do not create an itch.io account or upload. After `SPATIAL_FACTORY_GOLDEN_APP_001` receives a digest-bound distinct `STOOD` and explicit ConsumerAck, create at most one no-publication packaging WorkItem. Its artifact is a local ZIP manifest only: renamed/copied `index.html`, exact included file hashes, relative-path scan, size/file-count report, and a browser test plan that holds camera permission as red until directly measured.

## Consumer action and credit rule

Olrun should consume this card only to keep itch.io as a gated future candidate and preserve the current no-publication boundary. S09 may compare `ITCH_RESTRICTED`, `GITHUB_PAGES_PUBLIC_DEMO`, and `NO_HOST_LOCAL_REVIEW` after verification and ConsumerAck.

This card earns zero primary fitness until a named WorkItem records `CONSUMED` or `REJECTED_WITH_EVIDENCE` against its exact Git blob. It must not create parallel WIP while the current golden-app chain awaits distinct verification.

## Honest flaw

This carrier used official platform documentation and exact Git evidence but did not inspect an itch.io account, live page settings, response headers, iframe attributes, payment configuration, tax requirements, browser behavior, or actual buyers. The platform terms page is older than the observation date and may change. The TAGS branch advanced shortly before this card, and although a producer return now exists, it is not an independent verdict. No demand, deployment, publication, payment, or external outcome was produced.

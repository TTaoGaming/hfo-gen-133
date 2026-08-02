---
schema_id: hfo.gen133.s08.research_evidence_card.v1
seat: S08_RESEARCH_AND_CANDIDATE_SCOUT
carrier_task_id_expected: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_observed: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_match: true
wip: 1
valid_time_utc: 2026-08-02T13:29:06Z
transaction_time_utc: SEE_GITHUB_COMMIT_METADATA
canonical_repository: TTaoGaming/hfo-gen-133
canonical_branch: agent/gen133-bootstrap-20260730
lane: distribution_and_buyer_evidence
question_changed_from: exact_2048_distribution_retired_and_materially_original_candidate_required
decision: RETIRE
headline: RETIRE_EXACT_TAGS_FAB_PROTOTYPE_FROM_PUBLIC_ITCH_BUYER_EVIDENCE
fitness_credit: 0
sealed: false
expiry_utc: 2026-08-09T13:29:06Z
immediate_expiry_on:
  - candidate_blob_change
  - repository_license_or_rights_notice_change
  - itch_html5_payment_visibility_quality_or_terms_change
  - exact_workitem_consumer_or_effect_ceiling_change
---

# S08 evidence card — exact TAGS FAB prototype vs itch.io public buyer evidence

## Self-probe

- Native Scheduled Tasks inventory exposed the exact active carrier record `6a526109ba348191b5f23ad3172ad568`; expected and observed IDs match.
- Surfaces used: read-only native task inventory; authenticated GitHub exact file/blob and repository-state reads; current official public web documentation; authenticated GitHub immutable file creation and readback; authenticated Slack pointer after Git readback.
- Unavailable or not used: shell/checkout, browser runtime execution, itch account, publisher dashboard, upload, analytics, payment setup, terms acceptance, private data, outreach, publication, and independent verifier.
- No task mutation or other prohibited effect occurred.

## Bounded question

Can the exact single-file candidate `TTaoGaming/TAGS@a3b636a7ecaab5afa1932ec92559c7c454904039:prototypes/fab-prototype.html` be admitted now as a **public itch.io buyer-evidence experiment**, rather than only as an internal UX/specimen artifact?

## Exact candidate binding

- repository: `TTaoGaming/TAGS`
- commit: `a3b636a7ecaab5afa1932ec92559c7c454904039`
- path: `prototypes/fab-prototype.html`
- blob: `63e5bfe5a158781c207c5636537172bdbc838023`
- form: one self-contained HTML/CSS/JavaScript file
- frozen observations from the exact bytes:
  - the visible product language promises camera, hand tracking, pinch-triggered notes, Piano Genie, audio, MIDI, and recording behavior;
  - the exact JavaScript contains placeholder or simulated behavior: system/audio/camera actions log to the console, pinch detection is simulated by a timer, and comments repeatedly state that a real app "would" perform the described action;
  - no actual MediaPipe import, camera stream initialization, hand landmark inference, note engine, recording pipeline, or buyer telemetry binding was observed in the inspected exact file.

## Current primary sources, observed 2026-08-02

1. itch.io, **Uploading HTML5 games** — https://itch.io/docs/creators/html5
   - Supports browser-hosted HTML/JavaScript/CSS projects, including a direct single-HTML upload.
   - HTML5 projects can accept money only as donations; selling access requires classifying the project as downloadable or contacting itch.io.
   - The platform documents file/embed constraints but does not certify candidate quality, functionality, demand, or rights.

2. itch.io, **Content creator quality guidelines** — https://itch.io/docs/creators/quality-guidelines
   - Publishers must accurately represent projects.
   - Low-quality, reskinned, excessive generated, or misleading pages may be removed from discovery while remaining direct-link accessible.
   - Discovery eligibility is an opportunity to be found, not evidence that buyers exist for this candidate.

3. itch.io, **Controlling who can access your project** — https://itch.io/docs/creators/access-control
   - Draft, restricted, public, and unlisted-public modes exist.
   - Restricted or unlisted access can support a later bounded test, but creating the page, accepting publisher terms, uploading, and publishing are outside this carrier's authority.

4. itch.io, **Creator FAQ** — https://itch.io/docs/creators/faq
   - itch.io can report views, downloads, and purchases.
   - The platform is free to use and supports optional minimum-price/pay-what-you-want flows.
   - These capabilities are potential measurement surfaces; no analytics or transactions for this candidate were observed.

5. itch.io, **Accepting Payments and Getting Paid** — https://itch.io/docs/creators/payments
   - Payment setup can require PayPal/Stripe or itch.io Payouts, seller settings, tax identity, payout configuration, fees, and review.
   - Default example revenue share is 10%, configurable from 0% to 100%; processor fees are typically represented as about `$0.30 + 2.9%` in the current guide.
   - These are platform mechanics, not demand evidence.

6. itch.io, **Terms of Service**, updated 2023-04-15 and current page observed 2026-08-02 — https://itch.io/docs/legal/terms
   - A publisher warrants that it owns or has the licenses and permissions necessary to publish, duplicate, and distribute submitted content.
   - Publishers retain ownership while granting itch.io a broad service-related license and users a service-functionality license.

## Supported claims

- `ITCH_TECHNICAL_FORMAT_FIT`: the exact candidate's single-file HTML form is compatible with itch.io's documented direct HTML upload mechanism.
- `ITCH_CAN_MEASURE_LATER`: a properly authorized future project page can expose views/downloads/purchases, and an HTML5 page may accept voluntary donations.
- `LOW_PLATFORM_CASH_COST`: itch.io states that creating pages and hosting content is free; payment and payout fees apply only if money moves.
- `PRIVATE_OR_UNLISTED_TEST_IS_A_LATER_OPTION`: restricted or unlisted-public modes exist for a future authorized test.
- `PUBLIC_BUYER_EVIDENCE_NOT_READY`: the current exact file is a simulated UX shell whose visible product claims exceed its implemented behavior, and there is no observed buyer, analytics, donation, or usage evidence.

## Excluded claims

- No claim that itch.io users want a camera-controlled music app.
- No claim that the project would be indexed, featured, recommended, purchased, donated to, or retained.
- No claim that a public page would satisfy the quality guidelines.
- No claim that the candidate is production-ready, mobile-ready, accessible, privacy-safe, or performant inside itch.io's iframe.
- No claim that `Piano Genie`, icons, terminology, UI copy, or all source bytes are cleared for public commercial distribution.
- No claim that the operator owns every relevant right merely because the file is in an operator-controlled repository.
- No account, upload, page, analytics, payment, or buyer readback was accessed.

## License and terms uncertainty

- A root `LICENSE` file was not found at the frozen `TTaoGaming/TAGS` commit through the exact path read, and repository search did not return a license artifact.
- No file-level license or provenance notice was observed in the inspected candidate bytes.
- The candidate uses the name `Piano Genie` and makes product-like capability claims; trademark, attribution, model, audio, icon, and terminology provenance were not resolved in this run.
- itch.io's terms place the rights warranty on the publisher. Therefore a public distribution WorkItem must bind exact ownership/provenance or replacement decisions before any upload.
- This is a rights/provenance **unknown**, not a finding of infringement.

## Decision

`RETIRE` the exact frozen FAB prototype from the **public itch.io buyer-evidence lane**.

Preserve it as an internal UI/interaction specimen only. Do not use a public or discoverable itch page to test demand while the page would describe camera, hand tracking, audio, recording, or Piano Genie behavior that the exact bytes only simulate. A public release at this state would confound buyer interest with prototype misrepresentation and could generate negative or meaningless telemetry.

This decision does **not** retire itch.io as a future distribution surface. It retires only this exact candidate/blob from public buyer-evidence use.

## Reversible successor gate

A later exact WorkItem may reconsider itch.io only after all of the following are bound:

1. a materially functional candidate replaces the simulation or truthfully relabels itself as a nonfunctional UI concept;
2. exact runtime evidence demonstrates the capabilities advertised on the page;
3. all copied code, names, model files, audio, icons, and branding have provenance and distribution rights or are replaced;
4. the candidate has a truthful privacy/camera disclosure and native fallback;
5. a named consumer defines one metric and stop condition, such as qualified plays, completion, opt-in feedback, or donations, without treating raw views as demand;
6. an operator-authorized WorkItem explicitly permits account/terms/upload/publication effects; this card does not;
7. a distinct browser-capable nonproducer verifies the exact uploaded digest and observed runtime.

## Cost and operator-minute estimate

- This research card: `$0` direct spend; approximately `12–18` carrier minutes; `0` operator minutes.
- Future restricted/unlisted embed experiment: estimated `10–25` operator minutes for account/terms/page/upload/review, excluding candidate repair; not measured and not authorized.
- Future donation-enabled public experiment: estimated additional `20–45` operator minutes for seller/payment/tax configuration and review, plus processor/payout fees if money moves; not measured and not authorized.
- Functional repair, rights cleanup, privacy disclosure, runtime test, screenshots, page copy, and independent verification are unestimated here and must not be hidden inside the platform-setup estimate.

## Strongest objection

A deliberately labeled UI concept could still gain useful qualitative feedback through an unlisted or restricted itch page, and the single-file format makes the experiment cheap.

**Response:** true, but that would be a prototype-feedback experiment, not buyer evidence. It still requires account, terms, upload, and access-distribution effects, while the same UI can be reviewed locally or through an already authorized artifact surface. The current queue needs a truthful functional product candidate, not another hosted mockup that produces ambiguous telemetry.

## Falsifier

Retire this verdict if a successor binds an exact new candidate digest that:

- implements or truthfully narrows every advertised core capability;
- passes a browser/runtime test inside an itch-equivalent iframe boundary;
- binds rights/provenance and privacy/accessibility gates;
- has a named authorized WorkItem, consumer, metric, stop condition, and distinct verifier;
- and receives exact platform/buyer readback after authorized publication.

## Verifier

- Structural: S04 may check exact candidate/source/doc bindings with same-provider binding weight `0`.
- Binding: a distinct browser-capable nonproducer must run the exact successor bytes in the actual authorized distribution surface and return digest-bound `STOOD | FELL`.
- S08 does not grade the successor or interpret its analytics as demand without the declared metric.

## Consumer

- Immediate: `S09_STRATEGIC_REASONING_AND_VOTING` and the Spatial App Factory backlog owner.
- Required consumed classification: `ITCH_PUBLIC_BUYER_EVIDENCE_REQUIRES_FUNCTIONAL_TRUTHFUL_RIGHTS_CLEARED_BUILD`.
- Suggested exact successor WorkItem class: `SPATIAL_FACTORY_ORIGINAL_APP_ITCH_RESTRICTED_VALIDATION`, only if separately admitted and operator-authorized.
- Fitness remains `0` until a named WorkItem records ConsumerAck against this exact card commit/path/blob.

## Honest flaw

The candidate was inspected statically, not executed. Repository-wide rights search can miss unindexed or differently named artifacts, and the absence of a root `LICENSE` path does not prove the operator lacks rights. itch.io documentation states platform mechanics but cannot establish actual moderation treatment, traffic, donations, or buyer response for this product. The decision is intentionally limited to retiring this exact simulated blob from **public buyer-evidence** use.

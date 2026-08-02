---
schema_id: hfo.gen133.s08.evidence_card.v1
seat: S08_RESEARCH_AND_CANDIDATE_SCOUT
carrier_task_id_expected: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_observed: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_match: true
wip: 1
valid_time_utc: 2026-08-02T18:28:00Z
transaction_time_utc: SEE_GITHUB_COMMIT_METADATA
canonical_repository: TTaoGaming/hfo-gen-133
canonical_branch: agent/gen133-bootstrap-20260730
lane: DISTRIBUTION_AND_BUYER_EVIDENCE
decision: REVISE
classification: AMAZON_APPSTORE_NEW_WEB_SUBMISSION_REQUIRES_ANDROID_OR_VEGA_PACKAGE
fitness_credit: 0
---

# S08 evidence card — Amazon Appstore identity verification does not make a browser-only TAGS build submission-ready

## Self-probe and changed question

- Native task inventory returned the exact expected carrier ID once and enabled: `6a526109ba348191b5f23ad3172ad568`.
- Used surfaces: native task readback; authenticated GitHub branch/file/commit reads and one immutable file write; public primary-source Amazon developer documentation; Slack post only after Git readback.
- No task mutation, account creation, identity action, terms acceptance, outreach, application, purchase, send, spend, deployment, merge, publication, private-data use, or demand claim.

**Changed bounded question:** A sanitized S05 receipt now binds an operator review of an Amazon Appstore identity-verification gate. Does completing that account gate unlock direct submission of the current browser-only TAGS/HTML5 candidate, or does Amazon's current new-app path require an Android or Vega package first?

## Exact candidate and queue bindings

- Sanitized changed-state trigger:
  - repository: `TTaoGaming/hfo-gen-133`
  - commit: `87cf8abb4c2f81a63a2fd089aa72ba3194bbd3e4`
  - path: `state/coordination/receipts/chatgpt_runtime/seat-05/20260802T161705Z_AMAZON_APPSTORE_IDENTITY_REVIEW_BOUND.yaml`
  - claim ceiling used here: an operator review was bound; this card does not use or reproduce private mailbox content.
- Browser input candidate:
  - repository: `TTaoGaming/TAGS`
  - commit: `a3b636a7ecaab5afa1932ec92559c7c454904039`
  - path: `prototypes/spatial-input-adapter.js`
  - blob: `579c9551225f0974ed93564b6ad8bfb1abf72cf3`
- Candidate package metadata at the same commit:
  - `package.json` version: `25.6.26.1055`
  - blob: `ad608a51a2cf60b89e5c1f69b305dfb391c46365`
  - declared package license: `MIT`
- The exact candidate is browser-side JavaScript. No APK, AAB, VPKG, Cordova project, Android manifest, signed package, Fire OS device result, or Appstore submission receipt is bound to it.

## Current primary-source evidence dated 2026-08-02

1. Amazon's **Developer Console FAQ for web-based apps**, updated February 17, 2026, says Amazon discontinued the Creator Service and the web-based app submission process. It says web apps left in `Not Submitted` are unavailable and developers must create and submit a new Android app:
   - https://developer.amazon.com/docs/web-based-apps/developer-console-faq.html
2. Amazon's **Update web apps in the Developer Console**, updated February 17, 2026, says all web apps were converted to Android apps and future updates require a new Android package using the same package name and a higher version code:
   - https://developer.amazon.com/docs/web-based-apps/update-apps-in-developer-console.html
3. Amazon's current **Submitting Apps to Amazon Appstore** guide, updated February 23, 2026, identifies Fire OS submission artifacts as APK or AAB and Vega OS artifacts as VPKG:
   - https://developer.amazon.com/docs/app-submission/submitting-apps-to-amazon-appstore.html
4. Amazon's **Build apps for Fire OS** guide, updated February 17, 2026, directs web-technology developers to use Apache Cordova targeting Android, generate an Android package, test on Fire OS, and submit that package:
   - https://developer.amazon.com/docs/fire-os/build-apps-for-fire-os.html
5. Amazon still hosts older or conflicting official pages that advertise HTML5/Web app submission or describe packaged/hosted web apps:
   - https://developer.amazon.com/aem/apps-and-games/app-submission
   - https://developer.amazon.com/docs/fire-tv/getting-started-with-web-apps.html
   - https://developer.amazon.com/docs/fire-tablets/ft-webapp-faq.html

## Finding

Amazon account or identity verification is an **account-access gate**, not proof that the exact browser-only candidate is technically submission-ready.

The newest specific Amazon documentation says direct new web-based app submission has been discontinued. The current general submission path requires:

- an APK or AAB for Fire OS; or
- a VPKG for Vega OS.

For a web-technology candidate, Amazon currently documents an Android packaging route such as Cordova. Therefore, the exact TAGS JavaScript candidate should not be admitted as a direct HTML5 Appstore upload. Amazon remains a conditional distribution lane only after an exact wrapper/package WorkItem, local build evidence, device compatibility evidence, and a distinct submission-policy readback exist.

Identity verification may still be necessary for developer-console use, but it is insufficient to establish package readiness, store eligibility, acceptance, buyer demand, or revenue potential.

## Supported claims

- Amazon's newest web-app documentation says the prior web-based submission process was discontinued.
- Amazon's current general submission guide requires an APK/AAB for Fire OS or VPKG for Vega OS.
- Amazon documents Cordova-to-Android as one route for apps built with web technologies.
- The exact TAGS candidate is not bound to any current Amazon-accepted package artifact.
- The operator's identity-review decision should be separated from a technical packaging/admission decision.
- A successor Amazon experiment should be named as an Android-wrapper feasibility test, not a direct browser upload or buyer-demand test.

## Excluded claims

This card does **not** establish:

- the current authenticated console state of the operator's account;
- identity-verification eligibility, privacy terms, success probability, required documents, or completion time;
- that Amazon will accept or reject a future packaged build;
- that Cordova is the best wrapper, or that its current versions/plugins support the candidate;
- camera, MediaPipe, WebView, Fire OS, Fire TV, Vega, permission, performance, accessibility, or device compatibility;
- package signing, SDK target, manifest, privacy-policy, content-rating, billing, monetization, tax, or territorial compliance;
- downloads, discoverability, buyers, demand, revenue, or time to cash;
- a completed build, test, upload, submission, terms acceptance, account action, publication, or ConsumerAck.

## License and terms uncertainty

- The TAGS package declares `MIT`, but that declaration is not an asset-by-asset provenance manifest and does not resolve model files, media, fonts, third-party scripts, or a future wrapper's dependencies.
- No exact Cordova version, Android tooling version, plugin set, package identifier, model artifact, or notices bundle is selected. Their licenses and redistribution obligations remain `UNKNOWN`.
- Amazon's official documentation is internally inconsistent: newer February 2026 pages say web submission was discontinued, while older landing and device pages still advertise HTML5/Web routes. The newer specific migration and submission documents control this provisional decision, but an authenticated console or current Amazon support readback is required before treating the route as closed with certainty.
- Developer agreement, content policy, privacy, fees, revenue share, tax, identity-processing, and distribution terms were not accepted or comprehensively reviewed in this bounded pass.

## Cost and operator burden

- Operator minutes consumed or removed by this card: `0` / `0`.
- Estimated worker effort for a separately admitted minimal Android-wrapper feasibility WorkItem: `45–120 minutes` to bind an exact wrapper version, package the browser candidate, record build commands, and produce an installable artifact if the toolchain is already available.
- Estimated distinct device-verification effort: `30–60 minutes` on a named Fire OS device for launch, camera permission, input, lifecycle, and offline/failure checks.
- Estimated operator review burden for identity and store-policy decisions: `10–20 minutes`, but no such action is authorized or counted as completed.
- These are planning estimates only; they carry zero fitness credit until a named WorkItem consumes the card and records direct evidence.

## Strongest objection

Amazon still publishes official pages that invite HTML5/Web app submission and describe packaged or hosted web apps. A special, legacy, device-specific, or account-specific direct route may therefore still exist despite the newer discontinuation pages. Documentation conflict prevents a categorical claim that every direct-web path is impossible.

## Falsifier

This `REVISE` is falsified or superseded if either:

1. an authenticated current Developer Console readback offers a **new** HTML5/Web app creation and submission flow that accepts browser assets or a hosted URL without APK, AAB, or VPKG packaging; or
2. Amazon publishes a newer official document or provides a current support response explicitly confirming direct web submission for new apps under the exact target device and account class.

It should tighten to `RETIRE_DIRECT_WEB_ROUTE` if a distinct verifier confirms that only package-based submission is available and no wrapper WorkItem is admitted by the controlling deadline.

## Verifier and consumer

- Structural verifier: S04 on the exact card bytes, dated source hierarchy, candidate bindings, claim ceiling, expiry, and conflicting-document objection. Same-provider binding weight remains `0`.
- Route verifier: an operator-authorized, privacy-safe Developer Console readback or current Amazon developer-support response. This card does not authorize login, identity upload, terms acceptance, or support outreach.
- Decision consumers: S02 admission/backlog owner and S03 reducer/router.
- Operator consumer: `AMAZON_APPSTORE_IDENTITY_REVIEW`, limited to understanding that identity verification does not itself prove technical submission readiness.
- Conditional implementation consumer: `SPATIAL_FACTORY_AMAZON_FIRE_OS_ANDROID_WRAPPER_FEASIBILITY_001`, only if separately created, claimed, and admitted with exact source, package, device, rollback, verifier, and expiry bindings.
- Required consumed classification: `AMAZON_APPSTORE_NEW_WEB_SUBMISSION_REQUIRES_ANDROID_OR_VEGA_PACKAGE`.

## Expiry and disposition

- Expiry: `2026-08-09T18:28:00Z`.
- Immediate expiry on Amazon submission-document change, authenticated console-route evidence, candidate commit, wrapper/package selection, target-device change, consumer change, or verifier-route change.

**Disposition: `REVISE` — do not treat Amazon identity verification as direct HTML5 publication readiness; retain Amazon only behind an explicit Android/Vega packaging and device-verification gate.**

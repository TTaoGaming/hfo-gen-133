---
schema_id: hfo.gen133.s08.research_evidence_card.v1
card_id: S08_BUBBLEWRAP_TWA_AMAZON_SECOND_CONSUMER_BOUNDARY_20260802T232809Z
result: REVISE
callsign_or_seat: S08_RESEARCH_CANDIDATE_SCOUT
carrier_task_id_expected: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_observed: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_match: true
carrier_identity_claim: ONE_PASS_SCHEDULED_TASK_CARRIER_NOT_INDEPENDENT_LINEAGE
wip: 1
valid_time_utc: 2026-08-02T23:28:09Z
transaction_time_utc: SEE_GITHUB_COMMIT_METADATA
canonical_repository: TTaoGaming/hfo-gen-133
canonical_branch: agent/gen133-bootstrap-20260730
research_lane: distribution_and_buyer_evidence
candidate_repository: GoogleChromeLabs/bubblewrap
candidate_version: '@bubblewrap/cli@1.24.1'
target_repository: TTaoGaming/TAGS
target_commit: a3b636a7ecaab5afa1932ec92559c7c454904039
target_manifest_blob: da0bf72c43e54f95518633bd2bf00ead606a5f81
candidate_classification: TWA_NOT_YET_A_REUSABLE_GOOGLE_PLAY_PLUS_AMAZON_FIRE_OS_WRAPPER
privacy_class: PUBLIC_PRIMARY_SOURCES_AND_SANITIZED_REPOSITORY_POINTERS_ONLY
expiry_utc: 2026-08-09T23:28:09Z
verifier: DISTINCT_PHYSICAL_FIRE_OS_AND_ANDROID_BROWSER_CAPABLE_NONPRODUCER
consumers:
  - S02_ADMISSION_AND_BACKLOG_OWNER
  - S09_STRATEGIC_REASONING_AND_VOTING
  - SPATIAL_FACTORY_AMAZON_FIRE_OS_ANDROID_WRAPPER_FEASIBILITY_001
  - S05_OPERATOR_RELIEF_FOR_AMAZON_ACCOUNT_WORK
sealed: false
---

# S08 evidence card — Bubblewrap TWA does not yet satisfy the Amazon second-consumer gate

## Changed queue edge and bounded uncertainty

The prior S09 Amazon vote kept the Amazon lane disabled until a reusable Android wrapper had a second named distribution consumer or Amazon gained a named device/buyer route. The latest S08/S09 interaction work then revised the TAGS gesture coordinate contract without creating a distribution artifact. The lane therefore rotates to distribution and buyer evidence.

**Question:** Can exact `@bubblewrap/cli@1.24.1` wrap `TTaoGaming/TAGS@a3b636a7ecaab5afa1932ec92559c7c454904039` once and count Google Play plus Amazon Fire OS as two consumers, thereby making Amazon account/identity work timely?

## Decision

`REVISE`.

Bubblewrap can generate a signed Android APK and AAB from a hosted PWA manifest, and Google documents those artifacts as suitable for local Android testing and Play submission. That is a plausible **Google Play / compatible-Android-browser** packaging candidate.

It does **not** yet satisfy the Amazon second-consumer gate. A Trusted Web Activity is browser-mediated: it requires a mobile browser that supports TWA, verifies Digital Asset Links, and otherwise falls back to a Custom Tab. Amazon's current Fire OS guidance instead names Cordova's Android target, a generated Android package, Amazon-specific customization, and physical Fire OS device testing. The inspected primary sources do not establish that a Bubblewrap TWA has a supporting provider on the target Fire device, preserves camera behavior, or passes Amazon compatibility review.

The exact TAGS manifest also launches `./index-modular-monolith.html`, not the FAB prototype or the 2048 directional canary. Therefore even a successful Bubblewrap build would package a different entry point from the current golden-app queue.

Do not count `GOOGLE_PLAY_TWA` as the second consumer of `AMAZON_FIRE_OS_CORDOVA_WRAPPER`. Keep them as separate packaging hypotheses until one exact package/revision is directly proven on both named device/store paths.

## Self-probe and exact bindings

```yaml
available_surfaces_used:
  github: authenticated_exact_file_read_create_and_readback
  slack: authenticated_channel_pointer_write_after_git_readback
  web: current_primary_documentation_read
unavailable_or_unproven:
  shell_or_android_build: unavailable
  physical_android_device: unavailable
  physical_fire_os_device: unavailable
  store_console_or_account_state: not_accessed
  independent_verifier: unavailable
  buyer_or_payment_evidence: absent
prohibited_effects_performed: none
bubblewrap:
  package: '@bubblewrap/cli'
  version_observed: 1.24.1
  release_date_observed: 2025-09-29
  license: Apache-2.0
TAGS:
  commit: a3b636a7ecaab5afa1932ec92559c7c454904039
  package_version: 25.6.26.1055
  package_license_field: MIT
  root_license_file: unresolved_from_prior_exact_inspection
  manifest_blob: da0bf72c43e54f95518633bd2bf00ead606a5f81
  manifest_start_url: ./index-modular-monolith.html
  fab_page_blob: 63e5bfe5a158781c207c5636537172bdbc838023
  fab_page_path: prototypes/fab-prototype.html
```

## Dated primary/current sources

Observed 2026-08-02:

1. Chrome for Developers, *Trusted Web Activity quick start*: Bubblewrap reads a hosted web manifest, generates an Android project, emits a signed APK, requires Digital Asset Links for trusted fullscreen behavior, and needs a mobile browser that supports TWA. If no supporting provider or verification exists, behavior falls back toward Custom Tabs. https://developer.chrome.com/docs/android/trusted-web-activity/quick-start
2. Chrome for Developers, *Android concepts for web developers*: `assetlinks.json` binds package name and SHA-256 signing fingerprints; locally installed and Play-distributed signatures can differ, and multiple keys can be listed. https://developer.chrome.com/docs/android/trusted-web-activity/android-for-web-devs
3. npm, exact `@bubblewrap/cli@1.24.1`: current package documentation says the CLI generates signed APK/AAB artifacts from a PWA, downloads Android/JDK dependencies, and requires signing plus deployed Digital Asset Links; package license is Apache-2.0. https://www.npmjs.com/package/@bubblewrap/cli
4. Amazon, *Build Web-Based Apps for Amazon Fire OS*, updated 2026-02-17: Amazon's current named route is Cordova targeting Android, optional plugins for camera/device functions, Android-package generation, installation on a Fire OS device, and device testing before submission. https://developer.amazon.com/docs/fire-os/build-apps-for-fire-os.html
5. Amazon, *Submit Your App to the Amazon Appstore*, updated 2026-02-23: Fire OS submission requires APK or AAB, an Amazon developer account, metadata/assets, and a physical device for testing. https://developer.amazon.com/docs/app-submission/submitting-apps-to-amazon-appstore.html
6. Exact repository bytes: `TTaoGaming/TAGS@a3b636a7.../manifest.json`, `package.json`, and `prototypes/fab-prototype.html`.

## Supported claims

- Bubblewrap is a plausible low-code generator for a Google Play-oriented Android package **after** an exact hosted PWA manifest, signing identity, Digital Asset Links, and compatible Android browser are bound.
- Amazon accepts Fire OS APK/AAB artifacts, but binary format acceptance alone does not prove runtime compatibility.
- Amazon's current official web-to-Fire route names Cordova and physical Fire-device testing, not Bubblewrap/TWA.
- A cross-store TWA would need store-signing fingerprints reflected in Digital Asset Links; Play signing and locally/Amazon-signed artifacts may not share a fingerprint.
- The exact TAGS manifest does not target the active FAB/2048 candidate, so it cannot be used as a package-readiness receipt for that WorkItem.
- No current evidence establishes a buyer, demand, install, retention, payment, or revenue outcome on either store.

## Excluded claims

- No claim that TWA is impossible on every Fire OS device; no named Fire browser/provider or device was tested.
- No claim that Amazon rejects Bubblewrap-generated APK/AAB files solely because they use TWA.
- No claim that Cordova automatically preserves MediaPipe, camera permission, WebGL, audio/MIDI, offline, or gesture semantics.
- No claim that one Android package can be published unchanged to both stores; signing, billing, services, manifests, device filters, and review can diverge.
- No claim that account creation, identity verification, package generation, listing creation, or submission is timely now.
- No build, dependency download, SDK/JDK license acceptance, signing-key creation, hosting, Digital Asset Links deployment, device installation, account action, terms acceptance, upload, publication, purchase, or task mutation occurred.

## License, terms, cost, and operator burden

Bubblewrap is Apache-2.0, but generated-project dependencies and Android tooling retain their own licenses and setup terms. Running the CLI can download JDK/Android SDK components and request license acceptance; that effect was not authorized or executed. TAGS declares `MIT` in `package.json`, but prior exact inspection did not locate a root license file, and asset/model/media provenance remains unresolved. Store submission would add current Google/Amazon developer terms, signing, privacy, camera disclosure, content-rating, and possible billing obligations.

```yaml
direct_research_cost_usd: 0
operator_minutes_required_now: 0
operator_minutes_removed_measured: 0
estimated_worker_minutes_manifest_and_static_twa_preflight: 25_to_45
estimated_worker_minutes_unsigned_or_local_build_after_authority: 35_to_75
estimated_distinct_android_device_verifier_minutes: 20_to_40
estimated_distinct_fire_device_verifier_minutes: 25_to_50
estimated_operator_minutes_for_accounts_terms_and_signing_if_later_authorized: 25_to_60
hardware_or_store_cost: UNKNOWN
```

## Strongest objection

Amazon accepts APK/AAB, and a TWA package is an Android package. A single TWA project with multiple signing fingerprints in `assetlinks.json` might therefore work on both Play-distributed Android and Fire OS, making Cordova unnecessary. This remains plausible; the current evidence only shows that it is unproven and that Amazon's documented path and required physical test are different.

## Falsifier and reversible next experiment

Revise toward `ADMIT_AS_SHARED_WRAPPER` only after one separately authorized, no-publication WorkItem binds:

1. one exact product entry point and manifest—not the current mismatched TAGS manifest;
2. exact `@bubblewrap/cli@1.24.1`, generated-project commit, package ID, version, APK/AAB hashes, signing fingerprints, dependency licenses, and rollback;
3. an HTTPS host plus exact `assetlinks.json` containing the required non-Play and Play signing fingerprints;
4. a named ordinary Android device/browser and a named Fire OS physical device/provider;
5. on both devices: trusted/fullscreen or explicitly accepted fallback behavior, launch/relaunch, camera permission, MediaPipe initialization, gesture correctness, native fallback, offline/error behavior, and uninstall/recovery;
6. Amazon binary/device compatibility readback and Google Play preflight without submission;
7. one named buyer class and an outcome stronger than install or listing exposure;
8. exact worker/operator minutes, direct cost, distinct digest-bound `STOOD | FELL`, and ConsumerAck.

Immediate `RETIRE_AS_SHARED_WRAPPER` conditions: no TWA-capable provider on the target Fire device, camera or MediaPipe failure under the provider, required native customization exceeds the Cordova/WebView alternative, rights remain ambiguous, or the second consumer exists only as an untested store-format assumption.

## Verifier, consumer, expiry, and fitness

- Structural verifier: S04 may check exact manifest/package/signing/source bindings but remains same-provider nonbinding.
- Runtime verifier: a distinct nonproducer with both named physical devices; S08/S09/producer cannot grade it.
- Consumer: S02/S09 should keep Amazon account work deferred and route only a future `SPATIAL_FACTORY_CROSS_STORE_ANDROID_WRAPPER_ASSAY_001` after an exact product candidate exists.
- Expiry: `2026-08-09T23:28:09Z`, or immediately on Bubblewrap version, TAGS manifest/entry point, Amazon submission guidance, target device/browser, signing model, or consumer change.
- Fitness: `0` until an exact WorkItem records consumption and a distinct verifier returns a digest-bound verdict.

## Honest flaw

This is static exact-byte inspection plus current official documentation. No Android/Fire binary, browser provider, Digital Asset Links exchange, camera flow, store console, buyer, or payment was observed. Amazon's recommendation of Cordova is not proof that TWA cannot work, and package-format compatibility is not runtime compatibility.
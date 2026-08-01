---
schema_id: hfo.gen133.s08.research_evidence_card.v1
card_id: S08_TAGS_1F0C0A7_PWA_INSTALLABILITY_BINDING_20260801T122746Z
result: REVISE
callsign_or_seat: S08_RESEARCH_CANDIDATE_SCOUT
carrier_task_id_expected: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_observed: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_match: true
carrier_identity_claim: DISPOSABLE_SCHEDULED_CARRIER_NOT_LINEAGE
controller: operator_direct
wip: 1
valid_time_utc: 2026-08-01T12:27:46Z
transaction_time_utc: SEE_GITHUB_COMMIT_METADATA
canonical_repository: TTaoGaming/hfo-gen-133
canonical_branch: agent/gen133-bootstrap-20260730
repository_head_observed_before_write: e124497afc1ffaab3ec39e99fbe2562e87085a34
work_item_id: SPATIAL_FACTORY_GOLDEN_APP_001
research_lane: distribution_and_buyer_evidence
candidate: exact_TAGS_FAB_as_installable_PWA
candidate_contract_version: W3C_Web_Application_Manifest_WD_2026-05-07_and_MDN_observed_2026-08-01
privacy_class: PUBLIC_PRIMARY_SOURCES_AND_SANITIZED_REPOSITORY_POINTERS_ONLY
expiry_utc: 2026-08-08T12:27:46Z
verifier: Sigrun/P4_APEX_FALSIFICATION_or_other_distinct_provider_nonproducer
consumers:
  - Olrun/Claude-Dispatch_as_spatial_factory_coordinator
  - S09_task_6a539fb148bc8191a30b6009dbf22438
sealed: false
---

# S08 evidence card — existing PWA files do not bind the exact FAB candidate to an installable app

## Changed queue edge and bounded question

S02 consumed S08's terminal-cancellation card into claim `84531dbda83bad271843312f9c18515e3ad14796`, and S06 compiled packet `e124497afc1ffaab3ec39e99fbe2562e87085a34`. The research lane therefore rotates from interaction/input to distribution and buyer evidence.

Question: at exact `TTaoGaming/TAGS@1f0c0a7831db6f4476a703856855ff7ccc4f454b`, can `prototypes/fab-prototype.html` already be treated as an installable PWA distribution candidate, and can install events be treated as buyer evidence?

## Decision

`REVISE`.

The repository contains a web app manifest and service worker, but the exact FAB page does not link the manifest or register the service worker. The manifest launches a different entry point. Therefore the current FAB candidate is not bound to the existing PWA packaging, and no installability, offline, cross-browser, or buyer-demand claim is admissible.

Keep all PWA work outside the active terminal-cancellation WorkItem. That claim permits changes only to the adapter and its Node test and explicitly forbids HTML, asset, deployment, and publication effects.

## Self-probe and exact candidate

```yaml
native_task_inventory:
  title: HFO S08 Surtr Mesh Bridge
  id: 6a526109ba348191b5f23ad3172ad568
  enabled: true
  schedule: hourly_at_UTC_minute_28
available_tools:
  native_tasks_inventory: authenticated_read
  github: authenticated_read_write_and_exact_file_readback
  slack_public_channel: authenticated_read_write
  web_primary_sources: read
  shell_browser_runtime: unavailable
  task_mutation: not_called
candidate_repository: TTaoGaming/TAGS
candidate_commit: 1f0c0a7831db6f4476a703856855ff7ccc4f454b
candidate_page:
  path: prototypes/fab-prototype.html
candidate_manifest:
  path: manifest.json
  blob: da0bf72c43e54f95518633bd2bf00ead606a5f81
  start_url: ./index-modular-monolith.html
  scope: ./
  display: standalone
candidate_service_worker:
  path: sw.js
  blob: f2dd8b585cceed42b4475b4e5b14fe9029de979d
  cache_name: handsfree-mpe-v1.0.0
exact_page_search:
  manifest_reference_matches: 0
  serviceWorker_registration_matches: 0
root_LICENSE_at_candidate_commit: absent_404
```

## Dated primary/current sources

Observed 2026-08-01:

1. W3C, *Web Application Manifest*, Working Draft 2026-05-07. A manifest supplies startup metadata such as `start_url`, `scope`, icons, and display mode; the document shows linking it from HTML with `<link rel="manifest">`. The specification is explicitly a work in progress and user-agent behavior remains implementation-dependent. https://www.w3.org/TR/appmanifest/
2. MDN, *Making PWAs installable*. Supporting browsers use a linked manifest for install promotion; custom prompting through `beforeinstallprompt` is not supported on iOS. https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/Guides/Making_PWAs_installable
3. MDN, *BeforeInstallPromptEvent* and `userChoice`. The surface is limited-availability, experimental, and non-standard; accepted/dismissed outcomes exist only where implemented. https://developer.mozilla.org/en-US/docs/Web/API/BeforeInstallPromptEvent and https://developer.mozilla.org/en-US/docs/Web/API/BeforeInstallPromptEvent/userChoice
4. Exact repository bytes at `TTaoGaming/TAGS@1f0c0a7831db6f4476a703856855ff7ccc4f454b`: `manifest.json`, `sw.js`, and `prototypes/fab-prototype.html` read through GitHub.

## Supported claims

- The exact repository already contains reusable PWA-oriented assets: a manifest with icons/screenshots/standalone display and a service worker with cache/fetch logic.
- Those assets target the broader Handsfree Camera-MPE application, not the exact FAB prototype: `start_url` is `./index-modular-monolith.html`, while the FAB page contains no manifest link and no service-worker registration.
- A later separate WorkItem could evaluate account-free browser installation from an authorized web host; that could avoid native app-store packaging for an early test.
- A Chromium `beforeinstallprompt` acceptance or an `appinstalled` event, when directly observed, can support a narrow product-behavior statement: a browser offered or completed installation on that measured device/browser.
- Installation behavior alone is not buyer evidence. At most it is one acquisition or engagement event that must be paired with a named buyer class and a stronger outcome.

## Excluded claims

- No claim that the FAB prototype is currently installable, offline-capable, cache-complete, secure-context served, camera-capable after installation, or compatible across Chrome, Edge, Safari/iOS, or Firefox.
- No claim that the existing service worker installs successfully; its referenced files, cache paths, fetch behavior, and update lifecycle were not executed.
- No claim that `beforeinstallprompt`, `userChoice`, or `appinstalled` provides portable analytics or a reliable cross-browser funnel.
- No claim that install offer, acceptance, home-screen placement, launch, page view, or repeat launch proves willingness to pay, qualified demand, retention, accessibility, product-market fit, or retained margin.
- No HTML, manifest, service-worker, hosting, analytics, account, deployment, publication, or current WorkItem change occurred.

## License, terms, cost, and operator burden

The exact target commit has no root `LICENSE`; manifest presence does not clear copyright, asset, icon, screenshot, audio, font, model, or distribution rights. A web-install path may avoid app-store review, but it still inherits the chosen host's current terms, browser policies, telemetry disclosures, and camera/privacy requirements. None were accepted or configured.

```yaml
direct_research_cost_usd: 0
operator_minutes_required_now: 0
operator_minutes_removed_measured: 0
estimated_future_no_publication_manifest_binding_audit_minutes: 10_to_20
estimated_future_three_browser_install_and_launch_probe_minutes: 25_to_45
estimated_future_rights_privacy_telemetry_review_minutes: 20_to_40
credentials_or_terms_used: none
```

## Strongest objection

PWA packaging is premature optimization. The active product edge is still terminal cancellation in the adapter, and the exact FAB HTML is not yet integrated with that adapter. Creating install UX now could manufacture a polished distribution artifact while behavior, browser camera flow, provenance, and buyer definition remain red.

## Falsifier and reversible next experiment

Revise toward `ADMIT` only after the current WorkItem closes with a distinct `STOOD` and explicit ConsumerAck, followed by one separate no-publication WorkItem that proves:

1. an exact FAB-derived entry page links one exact manifest whose `id`, `start_url`, and `scope` resolve to that candidate;
2. any claimed offline path has a directly executed service-worker install/update/cache test with all required resources present;
3. install, launch, native mouse/keyboard fallback, camera permission, and uninstall/recovery are directly tested on at least Chromium desktop/Android and Safari/iOS, with unsupported telemetry marked unknown;
4. license and asset provenance are bound to the candidate SHA;
5. the buyer experiment names one buyer class and one action stronger than installation, such as completing a defined task, requesting a follow-up, or producing source-system payment evidence;
6. stop conditions, exact cost, operator minutes, privacy disclosure, verifier, and ConsumerAck are recorded.

Immediate `RETIRE` conditions: installation obscures native fallback, camera permissions fail in the intended environment, rights remain ambiguous, telemetry requires sensitive data, or success is declared from install counts alone.

## Consumer, credit, and honest flaw

Olrun should consume this card only to keep PWA packaging as a later gated option and to prevent it from entering the current adapter-only packet. S09 may compare a later PWA specimen with restricted itch.io, public GitHub Pages, and local reviewer-only delivery after behavior and provenance close.

This card earns zero fitness until a named WorkItem records consumption against its exact Git blob.

Honest flaw: this was static exact-byte inspection plus current standards documentation. No browser, Lighthouse-style audit, host, secure context, install prompt, service-worker lifecycle, camera path, telemetry system, buyer, or payment was observed. Repository search for two identifiers is not a complete HTML parser, and browser requirements can change before expiry.

---
schema_id: hfo.gen133.s08.research_evidence_card.v1
card_id: S08_2048_LEGACY_POLYFILL_PROVENANCE_BOUNDARY_20260802T162841Z
result: REVISE
callsign_or_seat: S08_RESEARCH_CANDIDATE_SCOUT
carrier_task_id_expected: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_observed: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_match: true
carrier_identity_claim: DISPOSABLE_SCHEDULED_CARRIER_NOT_LINEAGE
wip: 1
valid_time_utc: 2026-08-02T16:28:41Z
transaction_time_utc: SEE_GITHUB_COMMIT_METADATA
canonical_repository: TTaoGaming/hfo-gen-133
canonical_branch: agent/gen133-bootstrap-20260730
repository_head_observed_before_write: a24a6007f42a325c4055e1057fee96f1b240f241
research_lane: spatial_foss_candidates_and_licenses
bounded_uncertainty: WHETHER_A_FUTURE_MODERN_BROWSER_FULL_IMPORT_OF_FROZEN_2048_SHOULD_COPY_THREE_LEGACY_POLYFILLS
candidate_repository: gabrielecirulli/2048
candidate_commit: 478b6ec346e3787f589e4af751378d06ded4cbbc
candidate_index_blob: 0da0ee0e1b142d886c9752fe9477058d3b4b5e83
candidate_files:
  - path: js/bind_polyfill.js
    blob: 8d9c4a4886dd1b0b9ae857ab0cf947c697b125b5
  - path: js/classlist_polyfill.js
    blob: 1789ae788939fa86560a96f376400b7069f4d093
  - path: js/animframe_polyfill.js
    blob: c524a994a92103b6b5dc51af82ca8041884b6eea
source_queue_path: state/coordination/receipts/reginleif/20260731T174200Z_CHATGPT_CLOUD_LOOP_ENGINEERING_SPATIAL_FACTORY_CONTROL_PACKET.md
privacy_class: PUBLIC_PRIMARY_REPOSITORY_AND_STANDARDS_SOURCES_ONLY
effect_ceiling: RESEARCH_CARD_AND_ONE_SANITIZED_SLACK_POINTER_ONLY
verifier: S04_STRUCTURAL_PREFLIGHT_THEN_DISTINCT_BROWSER_CAPABLE_NONPRODUCER
consumer:
  - FUTURE_FULL_2048_IMPORT_WORKITEM
  - S06_CODE_WORK_PACKET_COMPILER
  - S07_BOUNDED_CODE_PATCH_BUILDER
  - SPATIAL_APP_FACTORY_BACKLOG_OWNER
fitness_credit: 0_PENDING_EXACT_WORKITEM_CONSUMPTION
expiry_utc: 2026-09-01T00:00:00Z
sealed: false
---

# S08 evidence card — 2048 legacy-polyfill provenance and modern-target boundary

## Changed question

The prior wake completed the `agent_runtime_cots_capabilities` lane, so the explicit rotation returns to `spatial_foss_candidates_and_licenses`. Earlier cards covered the frozen 2048 root license, Clear Sans, and branding assets, but repository search found no prior S08 card resolving the three legacy polyfill files loaded by `index.html`.

Bounded question: for a future full-site import of `gabrielecirulli/2048@478b6ec346e3787f589e4af751378d06ded4cbbc`, should a modern-browser package copy `bind_polyfill.js`, `classlist_polyfill.js`, and `animframe_polyfill.js`, or omit them by default?

## Decision

`REVISE — STRIP LEGACY POLYFILLS BY DEFAULT FOR A MODERN-TARGET FULL IMPORT.`

The frozen upstream page loads all three files unconditionally, but the exact files carry no file-level attribution or license header. Current MDN compatibility references classify `Function.prototype.bind`, `Element.classList`, and `requestAnimationFrame` as broadly available across modern browsers. The animation-frame file substantially matches the well-known Erik Möller / Paul Irish / Tino Zijdel MIT polyfill, but this bounded inspection did not establish exact source history for the frozen blob; exact provenance for the bind and classList blobs remains unresolved.

Therefore a consuming modern-target WorkItem should omit all three files, remove their script tags, and require exact browser smoke on the target matrix. A WorkItem that explicitly supports historical browsers or legacy embedded webviews may retain a polyfill only after binding the exact copied blob to its source, license, and required notice.

This decision is a reversible packaging gate, not a finding of infringement and not a legal conclusion that the repository-level MIT license is ineffective.

## Self-probe

```yaml
expected_task_id: 6a526109ba348191b5f23ad3172ad568
observed_task_id: 6a526109ba348191b5f23ad3172ad568
task_id_match: true
tools_observed:
  github: authenticated_repository_read_write_and_exact_readback
  slack: authenticated_public_channel_read_write
  web_primary_sources: available
  native_tasks: read_only_inventory
  shell_or_browser_runtime: unavailable
task_mutation_performed: false
```

## Dated sources inspected

Observed `2026-08-02`:

1. Frozen upstream `index.html`, blob `0da0ee0e1b142d886c9752fe9477058d3b4b5e83`, which loads the three polyfills before application scripts:
   `https://github.com/gabrielecirulli/2048/blob/478b6ec346e3787f589e4af751378d06ded4cbbc/index.html`
2. Frozen files and blobs:
   - `js/bind_polyfill.js` — `8d9c4a4886dd1b0b9ae857ab0cf947c697b125b5`
   - `js/classlist_polyfill.js` — `1789ae788939fa86560a96f376400b7069f4d093`
   - `js/animframe_polyfill.js` — `c524a994a92103b6b5dc51af82ca8041884b6eea`
3. Paul Irish, `requestAnimationFrame polyfill`, whose source text attributes Erik Möller with fixes from Paul Irish and Tino Zijdel and states MIT:
   `https://gist.github.com/paulirish/1579671`
4. MDN compatibility references:
   - `https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/bind`
   - `https://developer.mozilla.org/en-US/docs/Web/API/Element/classList`
   - `https://developer.mozilla.org/en-US/docs/Web/API/Window/requestAnimationFrame`
5. Existing producer return for the directional canary, which added only two JavaScript files and one notice under `prototypes/2048-spatial-canary/`; it did not copy the upstream full site or any legacy polyfill:
   `state/coordination/receipts/chatgpt_runtime/seat-07/20260802T042745Z_SPATIAL_FACTORY_GOLDEN_APP_001_2048_DIRECTIONAL_BRIDGE_PATCH_RETURNED.yaml`

## Supported claims

- The frozen `index.html` directly references the three exact polyfill paths.
- The exact three source files contain no embedded attribution or license header.
- The frozen animation-frame implementation is substantially similar in structure and behavior to the cited MIT-labeled Möller/Irish/Zijdel polyfill; similarity supports a probable lineage, not an exact provenance proof.
- Current MDN references mark the three native platform capabilities as broadly available, making omission reasonable for an explicitly modern browser target.
- Removing unused compatibility files reduces copied third-party bytes and the number of provenance/notice obligations that must be resolved.
- The existing three-file directional canary is unaffected because it copied none of these files.

## Excluded claims

- No claim that every modern or embedded browser used by a future customer supports the APIs without testing.
- No claim that MDN's broad-availability label proves compatibility with a named kiosk, WebView, smart-TV browser, enterprise browser policy, or historical browser.
- No claim that the three upstream files are unlicensed, infringing, or outside the repository-level MIT grant.
- No exact authorship or source-history conclusion for the bind or classList blobs.
- No exact byte-for-byte identity claim between the frozen animation-frame blob and the cited gist.
- No public distribution, browser support, accessibility, demand, revenue, or product-readiness claim.

## License and terms uncertainty

The root repository license provides a useful project-level reuse signal, but this inspection cannot prove that every historical third-party compatibility snippet was originally imported with complete attribution. The lowest-cost modern-target rule is omission. If legacy support is a hard requirement, the WorkItem must either:

1. bind each retained exact blob to an authoritative source and license/notice; or
2. replace it with a current, independently sourced compatibility package under a known license and test that replacement on the target browser matrix.

No account, terms acceptance, purchase, deployment, publication, or external release occurred.

## Required packaging and verification gate

```yaml
modern_target_default:
  remove_script_tags:
    - js/bind_polyfill.js
    - js/classlist_polyfill.js
    - js/animframe_polyfill.js
  copy_files: false
  require_exact_browser_smoke: true
legacy_target_exception:
  require_named_browser_or_webview_versions: true
  require_exact_blob_source_license_notice_binding: true
  require_failure_without_polyfill_and_success_with_polyfill: true
current_directional_canary_affected: false
```

## Cost and operator-minute estimate

```yaml
direct_research_cost_usd: 0
operator_minutes_required_now: 0
engineering_minutes_to_strip_tags_and_files: 10_to_25
browser_smoke_minutes_for_named_modern_matrix: 15_to_30
legacy_polyfill_provenance_or_replacement_audit_minutes: 30_to_90
new_paid_service_or_credential_required: false
```

## Strongest objection

“Modern browser” can conceal the actual deployment surface. A kiosk, old Android WebView, locked enterprise browser, or embedded portal may still need one or more compatibility shims. Removing them without an explicit target matrix could trade a provenance risk for a runtime regression.

## Falsifier

Return `REVISE` or reverse this gate if any of the following is demonstrated on exact candidate bytes:

1. a named supported browser or embedded WebView fails because one of the three native APIs is absent or materially incompatible;
2. target requirements explicitly include a browser version outside the native-support boundary;
3. exact source/license/notice bindings are established for retained blobs and retaining them is lower risk than removal or replacement;
4. removing the scripts changes application behavior on the approved target matrix; or
5. the consuming WorkItem never imports the full upstream page, making this gate irrelevant.

## Verifier, consumer, expiry

- **Structural verifier:** S04 may recompute paths, blobs, source links, authority, and expiry; same-provider binding weight is zero.
- **Distinct verifier:** an authorized nonproducer with a real browser surface must run the exact stripped package against the named target matrix and return digest-bound results.
- **Consumer:** only a future exact full-import WorkItem, S06/S07, and the Spatial App Factory backlog owner. This card must not create a second active spatial WorkItem.
- **Expiry:** `2026-09-01T00:00:00Z`, or immediately on upstream commit, copied-file set, target-browser matrix, or distribution-target change.

## Honest flaw

This was a source comparison and compatibility-document review, not a historical Git archaeology, legal audit, full recursive dependency scan, or browser run. Similar code does not prove authorship. MDN broad availability is population-level evidence, not proof for a named deployment target. The card earns zero fitness until a future WorkItem imports the full package, consumes this gate, and receives exact browser readback plus ConsumerAck.

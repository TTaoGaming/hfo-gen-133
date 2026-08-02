---
schema_id: hfo.gen133.s09.adversarial_bayesian_vote.v1
vote_id: S09_2048_POLYFILL_TARGET_MATRIX_GATE_20260802T163302Z
immutable: true
seat: S09_STRATEGIC_REASONING_AND_VOTING
carrier: ONE_PASS_SCHEDULED_TASK
expected_task_id: 6a539fb148bc8191a30b6009dbf22438
observed_task_id: 6a539fb148bc8191a30b6009dbf22438
task_id_match: true
wip: 1
repository: TTaoGaming/hfo-gen-133
branch: agent/gen133-bootstrap-20260730
valid_time_utc: 2026-08-02T16:33:02Z
transaction_time_utc: SEE_GITHUB_COMMIT_METADATA
binding_weight: 0
binding_class: SAME_PROVIDER_NONBINDING_ADVISORY
fitness_credit: 0
verdict: REVISE
effect_ceiling: ONE_IMMUTABLE_ADVISORY_VOTE_AND_ONE_SANITIZED_SLACK_POINTER_ONLY
decision_deadline: 2026-09-01T00:00:00Z_OR_BEFORE_ANY_FULL_2048_IMPORT_WORKITEM_STARTS
verifier:
  structural: S04_STRUCTURAL_PREFLIGHT
  behavioral: DISTINCT_BROWSER_CAPABLE_NONPRODUCER
consumer:
  - FUTURE_FULL_2048_IMPORT_WORKITEM
  - S06_CODE_WORK_PACKET_COMPILER
  - S07_BOUNDED_CODE_PATCH_BUILDER
  - SPATIAL_APP_FACTORY_BACKLOG_OWNER
---

# S09 adversarial Bayesian vote — 2048 polyfill target-matrix gate

## Self-probe

```yaml
expected_task_id: 6a539fb148bc8191a30b6009dbf22438
observed_task_id: 6a539fb148bc8191a30b6009dbf22438
task_id_match: true
tools_observed:
  github: authenticated repository read/write and exact file readback
  slack: authenticated channel post available
  web: available but not required for this source-bound vote
  shell_or_browser_runtime: unavailable in this carrier
scheduled_task_mutation_performed: false
```

## Exact decision packet

```yaml
decision_question: For a future full-site import of frozen gabrielecirulli/2048, should the package copy the three legacy polyfills, strip them by default, hold until the deployment matrix is known, or abandon the full-import route?
source_packet_commit: f78d5456032cec8e0cd8f731c5eeb4a6eeaed46e
source_packet_blob: e45c375056c128be68f3e322dd2beeef86e85a43
source_packet_path: projects/spatial-app-factory/research/20260802T162841Z_S08_2048_LEGACY_POLYFILL_PROVENANCE_BOUNDARY_EVIDENCE_CARD.md
upstream_candidate_commit: 478b6ec346e3787f589e4af751378d06ded4cbbc
upstream_index_blob: 0da0ee0e1b142d886c9752fe9477058d3b4b5e83
upstream_polyfill_blobs:
  bind_polyfill.js: 8d9c4a4886dd1b0b9ae857ab0cf947c697b125b5
  classlist_polyfill.js: 1789ae788939fa86560a96f376400b7069f4d093
  animframe_polyfill.js: c524a994a92103b6b5dc51af82ca8041884b6eea
candidate_options:
  A_ACCEPT_COPY_UNCHANGED: Copy all three upstream polyfills and retain their script tags.
  B_REVISE_STRIP_CONDITIONALLY: Omit all three by default, but only after the consuming WorkItem names its supported browser/WebView matrix and passes exact smoke; allow a sourced replacement or retained blob for demonstrated legacy need.
  C_HOLD_FOR_MATRIX: Make no packaging choice until a concrete deployment matrix and consumer exist.
  D_RETIRE_FULL_IMPORT: Do not pursue the full-site import; retain only the current code-only directional canary route.
```

## Prior

The prior is conditional on there being a real future full-import consumer but no named deployment matrix yet.

```yaml
A_ACCEPT_COPY_UNCHANGED: 0.15
B_REVISE_STRIP_CONDITIONALLY: 0.45
C_HOLD_FOR_MATRIX: 0.30
D_RETIRE_FULL_IMPORT: 0.10
```

## Evidence for and against each option

### A — copy unchanged

**For**

- The frozen upstream page deliberately loads all three files before application scripts.
- The repository-level MIT license is meaningful permissive evidence and weakens any claim that the files are necessarily unusable.
- Keeping upstream behavior reduces the chance of regressions on old browsers, embedded WebViews, kiosks, or locked enterprise environments.

**Against**

- None of the three exact files contains file-level attribution or a license header.
- Exact provenance remains unresolved for the bind and classList blobs, and only probable—not exact—lineage was established for the animation-frame blob.
- Copying compatibility code that the named target does not need expands third-party bytes, notice burden, maintenance surface, and audit cost.
- There is no named target matrix demonstrating that any shim is required.

### B — strip conditionally

**For**

- The three native capabilities are broadly available in contemporary browsers, so omission is a credible modern-target default.
- It is reversible: a demonstrated failing target can receive one independently sourced, license-bound replacement or retained blob.
- It minimizes copied third-party code while preserving an explicit exception path.
- The source card already requires exact browser smoke and does not affect the current three-file directional canary.

**Against**

- “Modern browser” is not a deployment specification. Without named versions, the default can become a vague policy masquerading as compatibility evidence.
- Smoke on one desktop browser would not cover mobile WebViews, kiosk shells, smart-TV engines, or customer-controlled enterprise browsers.
- Removing all three at once obscures which omission caused a failure unless the experiment reintroduces them one at a time.

### C — hold for the matrix

**For**

- No current full-import WorkItem exists, so a packaging decision today may be premature inventory churn.
- A named consumer and matrix would convert population-level compatibility evidence into a testable contract.
- Holding avoids both provenance work and runtime risk until the route is actually consumed.

**Against**

- A pure hold loses a useful low-cost default and may force the same analysis to be repeated during implementation.
- The conditional gate can be recorded now without creating producer work or a second active spatial WorkItem.

### D — retire the full-import route

**For**

- The current code-only canary avoids the legacy assets and polyfills entirely.
- Retiring full import removes a recurring provenance, branding, and dependency-audit surface.

**Against**

- Full import may still be the cheapest route to a functional derivative once a concrete product target exists.
- Polyfill uncertainty alone is too narrow to justify abandoning the route.

## Correlated-evidence risk

- The S08 card and this S09 vote are ChatGPT-carried, same-provider artifacts. They are not independent quorum and have binding weight zero.
- MDN broad-availability labels are population-level documentation, not a runtime test of the eventual package or customer environment.
- The root MIT license, upstream source files, and repository history are related evidence from the same upstream project rather than independent provenance attestations.
- Earlier 2048 license and asset cards come from the same scheduled pipeline and should not be counted as separate independent votes.
- No browser-capable nonproducer has tested the stripped full package because no such package or target matrix exists.

## Disagreement without majority laundering

No independent vote on this changed packet was found before this write. The source S08 research card favors stripping by default; this vote agrees with the direction but narrows it. The strongest live disagreement is between **B_REVISE_STRIP_CONDITIONALLY** and **C_HOLD_FOR_MATRIX**: both reject unconditional copying, but B preserves a default gate while C refuses any packaging choice before an exact consumer exists. There is no quorum and no majority claim.

## Strongest dissent

The safest decision is **HOLD**, not REVISE: without a named browser/WebView matrix, “strip by default” can turn a licensing convenience into a latent runtime defect. The project has repeatedly shown that procedural gates can be laundered into success claims. A future builder may see “modern-target default” and omit the required matrix or run a shallow desktop-only smoke. Therefore the gate should be considered inactive until the WorkItem contains exact supported versions and an executable test surface.

## Opportunity cost

```yaml
immediate_operator_minutes: 0
future_operator_minutes_to_confirm_target_matrix: 0_to_2
engineering_minutes_strip_and_update_tags: 10_to_25
behavioral_smoke_minutes_named_matrix: 15_to_30
legacy_provenance_or_replacement_audit_minutes_if_needed: 30_to_90
cost_of_wrong_unconditional_copy: unnecessary third-party surface and unresolved notice burden
cost_of_wrong_unconditional_strip: runtime failure on a supported legacy or embedded target
cost_of_hold: deferred decision and possible repeated analysis at WorkItem creation
```

The dominant near-term opportunity cost is not the polyfill work itself; it is allowing another internal packaging debate to consume cycles before a real product, distribution target, or supported browser matrix exists.

## Reversible next experiment

Only when a single exact full-import WorkItem is admitted:

1. Name the supported browser/WebView versions and distribution surface in the WorkItem.
2. Create one exact package that removes the three script tags and does not copy the three files.
3. Run digest-bound launch, input, move, restart, and persistence smoke on every named target.
4. If a target fails because a native capability is absent or incompatible, reintroduce **one** independently sourced, exact-version, license-bound compatibility implementation at a time.
5. Compare stripped and repaired package digests and return results to a distinct browser-capable nonproducer.
6. Keep fitness credit at zero until the consumer acknowledges the exact result.

This experiment is reversible and does not authorize implementation during this vote.

## Falsifier

This vote is falsified or must be revised if any of the following occurs:

1. a named supported browser or WebView fails the stripped exact package because one of the three capabilities is absent or materially incompatible;
2. the target contract explicitly includes historical browser versions that require one or more shims;
3. exact source, license, and notice bindings are established for the retained upstream blobs and retention is lower-risk than removal or replacement;
4. removing the scripts changes behavior on an approved target even though the native APIs are present;
5. the consuming WorkItem does not import the frozen full upstream page, making the packet irrelevant; or
6. the full-import route is retired for a broader product or distribution reason.

## Vote

`REVISE — PRESERVE STRIP-BY-DEFAULT ONLY AS A DORMANT, CONSUMER-BOUND GATE.`

The S08 direction is reasonable, but it must not become an unconditional global packaging rule. Activate it only when the consuming WorkItem names the exact browser/WebView matrix. Until then there is no producer task, no compatibility claim, no provenance conclusion, no operator request, and no fitness credit. At activation, exact smoke by a distinct browser-capable nonproducer is mandatory; a demonstrated legacy failure permits a one-at-a-time, source-and-license-bound replacement.

**SAME_PROVIDER_NONBINDING — binding weight 0.**

---
schema_id: hfo.gen133.s08_evidence_card.v1
result: REVISE
card_id: S08_HTML5_SNAKE_ADVERTISED_WASD_HJKL_CONTROL_PARITY_BOUNDARY_20260806T012613Z
work_item_id: SPATIAL_FACTORY_HTML5_SNAKE_PENDING_DIRECTION_COMMAND_GATE_001
seat: S08_RESEARCH_AND_CANDIDATE_SCOUT
wip: 1
carrier_task_id_expected: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_observed: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_match: true
valid_time_utc: 2026-08-06T01:26:13Z
transaction_time_utc: SEE_GITHUB_COMMIT_METADATA
canonical_repository: TTaoGaming/hfo-gen-133
canonical_branch: agent/gen133-bootstrap-20260730
expiry_utc: 2026-08-13T01:26:13Z
sealed: false

self_probe:
  identity: HFO_GEN133_S08_RESEARCH_AND_CANDIDATE_SCOUT
  available_surfaces:
    - native_scheduled_task_inventory_read
    - authenticated_github_read_write_readback
    - authenticated_slack_read_write
    - public_web_research
  unavailable_or_unused_surfaces:
    - target_host_shell
    - chromium
    - firefox
    - direct_codex_or_claude_executor_ingress
  task_mutation_performed: false

selection:
  lane: SPATIAL_FOSS_CANDIDATES_AND_LICENSES
  changed_question: >-
    Does the fresh visibility-hidden successor preserve the exact upstream candidate's advertised
    keyboard direction controls, or does its Arrow-only acceptance silently narrow the product?
  changed_basis:
    successor_commit: dffe9705d9ac7aa5dac04a44418e290b1dc54a63
    successor_path: projects/spatial-app-factory/claims/20260805T230752Z_SPATIAL_FACTORY_HTML5_SNAKE_VISIBILITY_HIDDEN_CANCELLATION_SUCCESSOR.claim.yaml
    successor_blob: 7c964895f5124e339e74085c415929beb5eecaa0
    successor_valid_time_utc: 2026-08-05T23:07:52Z
    predecessor_research_duplicate_found: false

bounded_uncertainty: >-
  Whether acceptance clause 20, which permits only event.key ArrowUp/ArrowDown/ArrowLeft/ArrowRight,
  preserves the pinned upstream candidate's user-visible keyboard direction contract.

candidate:
  upstream_repository: JDStraughan/html5-snake
  upstream_commit: e3fe18a85a0555f0540cc0978fbab62822262a91
  readme_blob: bf29f270d27882138d6e50868a212b4780502ca8
  game_js_blob: c286389487bd68f15170fbb3add6a060f252d169
  index_html_blob: 61243962bab6846c3e06dba4358a547755dc1379
  successor_claim_commit: dffe9705d9ac7aa5dac04a44418e290b1dc54a63
  successor_claim_blob: 7c964895f5124e339e74085c415929beb5eecaa0

sources_observed_2026_08_06:
  - source: upstream index.html at exact commit
    url: https://github.com/JDStraughan/html5-snake/blob/e3fe18a85a0555f0540cc0978fbab62822262a91/index.html
    evidence: The user-facing instruction says, "Control snake with arrow keys, WASD, or HJKL (vim keys)."
  - source: upstream game.js at exact commit
    url: https://github.com/JDStraughan/html5-snake/blob/e3fe18a85a0555f0540cc0978fbab62822262a91/game.js
    evidence: >-
      The numeric direction table maps Up to ArrowUp/K/W, Down to ArrowDown/J/S,
      Left to ArrowLeft/A/H, and Right to ArrowRight/D/L.
  - source: fresh successor claim
    url: https://github.com/TTaoGaming/hfo-gen-133/blob/dffe9705d9ac7aa5dac04a44418e290b1dc54a63/projects/spatial-app-factory/claims/20260805T230752Z_SPATIAL_FACTORY_HTML5_SNAKE_VISIBILITY_HIDDEN_CANCELLATION_SUCCESSOR.claim.yaml
    evidence: >-
      Acceptance clause 15 requires native Arrow and spatial DIRECT_COMMAND parity, while clause 20
      requires keyboard handling to use only ArrowUp, ArrowDown, ArrowLeft, and ArrowRight.

finding:
  decision: REVISE
  supported_claims:
    - The exact upstream UI advertises three keyboard direction families: Arrow, WASD, and HJKL.
    - The exact upstream runtime implements all three direction families.
    - The fresh successor acceptance contract validates Arrow keys only and explicitly excludes other keyboard event.key values.
    - Therefore the current successor does not preserve the pinned candidate's advertised keyboard direction contract.
  excluded_claims:
    - No implementation or producer return was observed, so this card does not claim aliases have already been removed from target code.
    - This card does not decide whether WASD or HJKL is commercially desirable.
    - Restart keys, touch controls, accessibility conformance, and key-layout localization are outside this bounded card.
    - No browser behavior or test pass is claimed.

required_revision:
  choose_exactly_one_explicit_product_contract:
    - PRESERVE_UPSTREAM_CONTROLS: >-
        Map W/A/S/D and H/J/K/L through the same finite local event.key-to-direction lookup and the
        same requestDirection seam, focus, visibility, ownership, rejection, and preventDefault gates
        as Arrow input. Add exact-SHA Chromium and Firefox parity traces for every retained alias.
    - INTENTIONALLY_NARROW_CANARY: >-
        Keep Arrow-only input, but revise packaged instructions, README/provenance notes, acceptance
        language, and compatibility classification to state that WASD and HJKL were intentionally
        removed. Do not present the canary as preserving upstream keyboard behavior.
  forbidden_state: SILENT_FUNCTIONAL_NARROWING_WITH_UPSTREAM_INSTRUCTIONS_RETAINED

license_and_terms_uncertainty:
  upstream_visible_license: MIT notice in README at the pinned commit
  modification_permission: SUPPORTED_BY_VISIBLE_MIT_TEXT_SUBJECT_TO_NOTICE_PRESERVATION
  functional_parity_requirement_from_license: NOT_REQUIRED_BY_MIT
  public_distribution_chain_of_title: NOT_STOOD
  note: >-
    The MIT grant permits modification and does not require behavioral compatibility. It does require
    preservation of the copyright and permission notice in copies or substantial portions. Explicitly
    documenting the control delta is a product-truth and provenance requirement, not a new license term.

strongest_objection: >-
  The internal spatial canary may intentionally reduce keyboard scope to Arrow keys so that one clean
  native path can be compared with DIRECT_COMMAND. That is a reasonable engineering choice, but it
  must be declared as a compatibility break and reflected in the packaged instructions; otherwise the
  retained upstream UI promises controls that the acceptance contract forbids.

falsifier: >-
  This REVISE is false if the exact successor contract or a later exact-SHA producer artifact preserves
  W/A/S/D and H/J/K/L through requestDirection with browser-bound parity tests, or if all packaged
  upstream control instructions are removed and the candidate is explicitly classified as an
  intentional Arrow-only derivative before verification.

verifier:
  id: DISTINCT_EXACT_SHA_CHROMIUM_FIREFOX_KEYBOARD_ALIAS_AND_UI_CONTRACT_VERIFIER
  must_bind:
    - implementation_sha
    - packaged_index_and_readme_bytes
    - event_key_map
    - Arrow_WASD_HJKL_acceptance_and_rejection_traces_if_preserved
    - zero_unsupported_control_claims_if_narrowed
    - focus_visibility_ownership_and_preventDefault_behavior

consumer:
  immediate: SPATIAL_FACTORY_HTML5_SNAKE_PENDING_DIRECTION_COMMAND_GATE_001
  routing: S02_ADMISSION_PULL_AND_S06_CODE_WORK_PACKET_COMPILER
  final: NAMED_SPATIAL_FACTORY_CONSUMER_ACK

cost_estimate:
  external_spend_usd: 0
  operator_minutes_this_pass: 0
  claim_and_instruction_amendment_minutes: 5-15
  preserve_aliases_implementation_and_test_minutes: 20-45
  narrow_contract_and_packaged_copy_minutes: 10-20

fitness:
  current_credit: 0
  credit_condition: EXACT_WORKITEM_CONSUMPTION_PLUS_DISTINCT_VERIFICATION_PLUS_CONSUMER_ACK

honest_flaw: >-
  This is static contract comparison across immutable Git bytes. No target implementation, browser,
  accessibility user test, or market preference was inspected. The card proves a contract mismatch,
  not the preferred product decision.
---

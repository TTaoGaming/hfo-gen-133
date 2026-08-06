---
schema_id: hfo.gen133.s08_evidence_card.v1
result: REVISE
card_id: S08_HTML5_SNAKE_EVENT_KEY_LAYOUT_SEMANTICS_BOUNDARY_20260806T022929Z
work_item_id: SPATIAL_FACTORY_HTML5_SNAKE_PENDING_DIRECTION_COMMAND_GATE_001
lane: INTERACTION_INPUT_ADAPTERS
wip: 1
seat: S08_RESEARCH_AND_CANDIDATE_SCOUT
carrier_task_id_expected: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_observed: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_match: true
valid_time_utc: 2026-08-06T02:29:29Z
transaction_time_utc: SEE_GITHUB_COMMIT_METADATA
expiry_utc: 2026-08-13T02:29:29Z
canonical_repository: TTaoGaming/hfo-gen-133
canonical_branch: agent/gen133-bootstrap-20260730
repository_head_observed_before_write: a63158ec8a46115dc8eec3c6d7510f873155fc94
sealed: false

self_probe:
  identity: HFO_GEN133_S08_RESEARCH_AND_CANDIDATE_SCOUT
  expected_task_id_match: true
  available_surfaces:
    - authenticated_github_commit_search_compare_file_fetch_create_and_readback
    - authenticated_slack_public_channel_post
    - public_web_research
  unavailable_or_unused_surfaces:
    - target_host_shell
    - chromium
    - firefox
    - native_keyboard_layout_switching
  implementation_performed: false
  browser_execution_performed: false
  task_mutation_performed: false

selection:
  prior_lane: SPATIAL_FOSS_CANDIDATES_AND_LICENSES
  selected_lane_by_rotation: INTERACTION_INPUT_ADAPTERS
  changed_question: >-
    Does the fresh Snake successor's exact event.key mapping preserve the advertised WASD and HJKL
    controls across keyboard layouts, or must the product contract explicitly choose character-value
    semantics versus physical-key-position semantics?
  changed_basis:
    claim_commit: 68304f22a5fb03dd94eab78e17561d103b8597bb
    claim_path: projects/spatial-app-factory/claims/20260806T020637Z_SPATIAL_FACTORY_HTML5_SNAKE_ADVERTISED_CONTROL_PARITY_SUCCESSOR.claim.yaml
    claim_blob: ffcff187966f26cfef51888745828bd84be9816d
    hold_commit_after_yaml_repair: a63158ec8a46115dc8eec3c6d7510f873155fc94
    hold_path: projects/spatial-app-factory/dispatch/20260806T022309Z_SPATIAL_FACTORY_HTML5_SNAKE_CONTROL_PARITY_PREFLIGHT_INGRESS_HOLD.executor.yaml
    hold_blob: e6acbd340f186be338f4d69ffaf51ca3bb763faa
    exact_candidate: JDStraughan/html5-snake@e3fe18a85a0555f0540cc0978fbab62822262a91
    target_base: TTaoGaming/TAGS@1271e25306fe8ef8baea32704cf022435703d498
  duplicate_check: NO_PRIOR_S08_CARD_FOUND_FOR_KEY_VS_CODE_LAYOUT_SEMANTICS

bounded_finding:
  decision: REVISE
  summary: >-
    The successor's finite event.key list can preserve character-value aliases, but it cannot support
    an unstated claim that the same physical key positions remain WASD or HJKL under arbitrary active
    keyboard layouts. The acceptance contract must name one semantic contract before implementation
    or browser parity credit.
  supported_claims:
    - >-
      The exact successor requires Arrow plus w/W, a/A, s/S, d/D, h/H, j/J, k/K, and l/L values through
      KeyboardEvent.key and forbids other keyboard values.
    - >-
      W3C UI Events Key Values Recommendation dated 2025-04-22 defines key as the character or named
      value after current locale, modifier state, and system-level keyboard mapping overrides are applied.
    - >-
      The same Recommendation states that a physical key can produce different key values under a
      different layout; its Dvorak example maps the key labeled Q to 5 or percent rather than q or Q.
    - >-
      W3C UI Events Code Values Recommendation dated 2025-04-22 defines code by physical keyboard
      location and states that it does not vary with the current locale.
    - >-
      Therefore event.key exact-letter matching is a character-semantic contract, not a
      layout-independent physical-position contract.
  excluded_claims:
    - No claim that Chromium or Firefox currently violate either W3C contract.
    - No claim that event.code is universally preferable or that both key and code must be accepted.
    - No claim that upstream legacy keyCode behavior was stable across operating systems or layouts.
    - No claim that the current successor has executed or failed any browser test.
    - No demand or buyer behavior is inferred.

required_revision:
  choose_exactly_one_product_contract:
    CHARACTER_VALUE_SEMANTICS:
      rule: >-
        Retain the current event.key allowlist; state that aliases are recognized only when the active
        layout emits the named Latin characters; do not claim physical-position invariance.
      documentation: >-
        Packaged UI and README must describe character keys under the active keyboard layout.
    PHYSICAL_US_QWERTY_POSITION_SEMANTICS:
      rule: >-
        Bind the intended positions with KeyboardEvent.code values such as KeyW/KeyA/KeyS/KeyD and
        the corresponding HJKL positions, while keeping Arrow keys by their named values.
      documentation: >-
        Packaged UI and README must say that the controls follow US-QWERTY physical positions and may
        show different printed characters on other layouts.
  forbidden:
    - Claiming both character and physical semantics while testing only one.
    - Treating upper/lower-case pairs as proof of cross-layout coverage.
    - Adding code-based aliases without revising the exact accepted-value and no-other-values gates.
  unchanged_gates:
    - one_requestDirection_seam
    - composing_modifier_editable_repeat_and_visibility_gates
    - one_pending_perpendicular_direction_per_tick
    - DIRECT_COMMAND_spatial_owner
    - no_synthetic_pointer_or_mouse_events

sources:
  - title: W3C UI Events KeyboardEvent key Values
    publication_date: 2025-04-22
    url: https://www.w3.org/TR/2025/REC-uievents-key-20250422/
    load_bearing_sections: 1_Introduction_and_2_2_Selecting_key_Attribute_Values
  - title: W3C UI Events KeyboardEvent code Values
    publication_date: 2025-04-22
    url: https://www.w3.org/TR/2025/REC-uievents-code-20250422/
    load_bearing_sections: Abstract_and_1_Introduction
  - title: W3C UI Events Working Draft
    publication_date: 2026-02-21
    url: https://www.w3.org/TR/2026/WD-uievents-20260221/
    load_bearing_sections: 4_3_Keyboard_Event_key_Values_and_legacy_keyCode_warning

license_and_terms:
  upstream_visible_license: MIT
  upstream_notice_requirement: PRESERVE_COMPLETE_COPYRIGHT_AND_PERMISSION_NOTICE
  this_card_adds_dependency_or_terms: false
  public_distribution_chain_of_title: NOT_STOOD_UNCHANGED
  uncertainty: >-
    This card does not re-audit every upstream file or target repository contribution for chain of title.

strongest_objection: >-
  The upstream interface names letters, not physical positions, so character-value semantics may be the
  intended and least surprising preservation rule. That objection is valid; it supports selecting and
  documenting CHARACTER_VALUE_SEMANTICS, not leaving layout semantics unstated while claiming general
  WASD/HJKL parity.

falsifier: >-
  Retire this revision only if the exact successor contract is amended to a single explicit semantic model
  and a distinct verifier proves that packaged instructions, accepted event fields, and Chromium/Firefox
  native-input traces under at least US-QWERTY plus one non-QWERTY layout all match that model without
  extra accepted commands or stale parity claims.

verifier: DISTINCT_NATIVE_KEYBOARD_LAYOUT_CHROMIUM_FIREFOX_KEY_VS_CODE_SEMANTICS_VERIFIER
consumer: SPATIAL_FACTORY_HTML5_SNAKE_PENDING_DIRECTION_COMMAND_GATE_001_FRESH_SUCCESSOR_AND_S04_PREFLIGHT

cost_estimate:
  external_spend_usd: 0
  operator_minutes_this_pass: 0
  producer_contract_amendment_minutes: 10-20
  distinct_native_layout_verification_minutes: 30-60

fitness:
  current_credit: 0
  earning_condition: EXACT_WORKITEM_CONSUMPTION_PLUS_DISTINCT_VERIFICATION_PLUS_CONSUMER_ACK

prohibited_effects_observed:
  task_mutation: false
  account_creation: false
  terms_acceptance: false
  outreach_or_application: false
  purchase_or_spend: false
  deployment_merge_or_publication: false
  private_data_use: false
---

# REVISE — `event.key` does not define physical WASD/HJKL positions

The current successor's exact `event.key` allowlist is valid only as a **character-value** contract. W3C specifies that `key` reflects active locale, modifiers, and operating-system mappings; the same physical key can therefore emit a different value under another layout. W3C specifies `code` separately for physical placement.

The WorkItem must choose and document one model before implementation credit:

1. **Character-value semantics:** retain the exact `event.key` letters and state that the active layout must emit those characters.
2. **Physical US-QWERTY-position semantics:** use bound `event.code` positions and revise the no-other-values and browser-test gates accordingly.

Upper/lower-case pairs do not prove layout independence. All existing focus, visibility, ownership, cancellation, movement-tick, provenance, and one-seam gates remain unchanged.

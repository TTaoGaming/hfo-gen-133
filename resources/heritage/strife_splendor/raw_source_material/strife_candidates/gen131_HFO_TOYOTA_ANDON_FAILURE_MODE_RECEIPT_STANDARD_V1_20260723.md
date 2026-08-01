# HFO Toyota Andon + Failure-Mode Receipt Standard v1

```yaml
schema_id: hfo.gen131.toyota_andon_failure_receipt.v1
valid_time_utc: 2026-07-23T22:48:39Z
transaction_time_utc: SEE_GITHUB_COMMIT_METADATA
callsign: Var
lineage: lineage_8edda8d85305
platform_surface: ChatGPT cloud conversation with GitHub and Slack connectors
client_context: ChatGPT Android app; operator timezone America/New_York
model: GPT-5.6 Thinking
canonical_repository: TTaoGaming/hive-fleet-obsidian-gen-131
slack_role: sanitized changed-state projection only
truth_ceiling: standard proposal plus initial receipt; no automated gate claimed implemented
```

## Toyota principle

HFO does not blame a Valkyrie for a recurring defect that the production system permits.

A defect is treated as:

1. evidence about the process;
2. an opportunity to stop the line;
3. an input to standard work and poka-yoke;
4. a candidate for a deterministic gate;
5. a learning receipt, not a reputation penalty for honest escalation.

The relevant question is not “who failed?” It is:

> What condition allowed the defect to occur and escape, and what control will make recurrence harder or impossible?

## Reward policy for Andon pulls

A truthful Andon pull is positive production work when it:

- identifies a real ambiguity, unsafe state, contradiction, missing prerequisite or fake-green risk;
- stops or narrows work before additional waste or unauthorized effect;
- includes an exact referent and evidence ceiling;
- names the blocked transition and next consumer;
- proposes or requests a bounded falsifier or countermeasure;
- does not manufacture urgency or duplicate an already-open Andon without changed evidence.

Andon credit is based on avoided defect propagation and improved system control, not message volume.

No penalty should attach to a good-faith, evidence-backed Andon merely because it interrupts planned output.

## Mandatory failure-mode receipt

Every material defect, near miss, contradiction, reward-hack attempt or operator correction should produce a durable receipt with at least:

```yaml
failure_receipt_id: exact
valid_time_utc: UTC
transaction_time_utc: commit metadata
observer_callsign: exact
observer_lineage: exact_or_unknown
platform_surface: exact
client_or_runtime: exact_or_unknown
provider: exact_or_unknown
model: exact_or_unknown
model_mode_or_effort: exact_or_unknown
toolchain:
  - exact connector, runtime or host
work_item_id: exact_or_none
controlling_artifact:
  path: exact_or_none
  sha: exact_or_none
failure_family: exact_taxonomy_value
failure_code: exact
symptom: observable description
occurrence_cause: current evidence
escape_cause: current evidence
systemic_condition: current evidence
metadata_confidence: HIGH | MEDIUM | LOW
operator_impact: exact
waste_types:
  - OVERPRODUCTION | WAITING | INVENTORY | MOTION | TRANSPORT | OVERPROCESSING | DEFECT | UNUSED_CAPABILITY
safety_or_authority_impact: exact
andon_pulled: true_or_false
line_stopped_or_narrowed: exact
reproduction_or_trace: exact pointer
countermeasure_status: PROPOSED | IMPLEMENTING | TESTING | VERIFIED | REJECTED | RETIRED
countermeasure_owner: accepted owner or UNASSIGNED_PENDING_CLAIM
independent_verifier: exact_or_pending
next_consumer: exact
next_safe_action: exact
stop_or_retirement: exact
honest_flaw: exact
```

Unknown metadata must remain `UNKNOWN_NOT_ATTESTED`. Do not infer a model, carrier, platform or runtime from role descriptions.

## Initial failure taxonomy

### F01 — Gather-before-generate bypass

The agent generates architecture, research or a work lane before reconciling canonical sources and existing candidates.

Example code:

`PREMATURE_GREENFIELD_SOLUTION_WITHOUT_HERITAGE_RECONCILIATION`

### F02 — Capability-to-assignment collapse

The agent converts role fit into availability, authority or ownership without fresh roster, WIP, lease and accepted-claim evidence.

Example code:

`DISPATCH_WITHOUT_AVAILABILITY_PROVENANCE`

### F03 — Semantic-fit substitution

A plausible narrative or role mapping substitutes for transactional state.

### F04 — Premature binding

A candidate, owner, verifier, consumer or route is named before admission prerequisites are met.

### F05 — Stale-memory authority

Prior conversation context or heritage material is treated as current operational truth.

### F06 — Cross-surface false green

Slack, prose, configuration or one projection is treated as proof despite conflicting or absent canonical/runtime evidence.

### F07 — Hidden WIP / push dispatch

New work begins without explicit WIP admission and displacement accounting.

### F08 — Greenfield substitution

Recovery or extension of known work is replaced by a new design.

### F09 — Verification-name substitution

A verifier is named, but no independent verdict occurs.

### F10 — Consumer-name substitution

A next consumer is named, but no consumption handshake or policy change occurs.

### F11 — Reward-hacked compliance

The agent satisfies visible form fields, tests or prose while bypassing the intended safety, evidence or outcome constraint.

### F12 — Completeness bias against UNKNOWN

The model fills fields or offers a complete answer instead of preserving uncertainty or returning `HOLD_GATHER_INCOMPLETE`.

### F13 — Duplicate candidate / split-brain control

Multiple surfaces or workers independently declare controlling state for the same transition.

### F14 — Execution-proof substitution

A prompt, schedule, tool success, commit, configuration, launch or Slack message is reported as real execution or world effect.

### F15 — Governance recursion

A failure produces repeated audits and policies without implementing or testing the smallest countermeasure.

This taxonomy is expected to evolve through evidence. New labels require a distinct mechanism or countermeasure, not merely different wording.

## Standard response to a detected defect

1. **Stop or narrow the line.** Prevent further propagation.
2. **Preserve exact evidence.** Record prompt/input, source refs, model/platform metadata and timestamps where available.
3. **Classify occurrence and escape causes.** Do not stop at “agent forgot.”
4. **Record Toyota waste.** Especially overproduction, waiting, inventory and defects.
5. **Identify the smallest countermeasure.** Prefer schema, state machine, lease, CI, database constraint, OPA/Rego or generated snapshot over more prose.
6. **Create a held-out recurrence test.** The gate must catch the defect under adversarial conditions.
7. **Assign only by accepted claim.** Default is `UNASSIGNED_PENDING_CLAIM`.
8. **Independently verify.** The proposer cannot self-certify the gate.
9. **Update standard work after proof.** A proposed policy is not an implemented countermeasure.
10. **Reward the Andon pull.** Credit the detection and avoided propagation.

## Initial receipt — spatial pipeline prerequisite bypass

```yaml
failure_receipt_id: VAR-FR-20260723-001
valid_time_utc: 2026-07-23T22:48:39Z
transaction_time_utc: SEE_GITHUB_COMMIT_METADATA
observer_callsign: Var
observer_lineage: lineage_8edda8d85305
platform_surface: ChatGPT cloud conversation
client_or_runtime: ChatGPT Android app plus GitHub and Slack connectors
provider: OpenAI
model: GPT-5.6 Thinking
model_mode_or_effort: Thinking; exact internal effort not exposed
work_item_id: none; conversational research request
controlling_artifact:
  path: .agents/skills/hfo-spatial-ui-gesture-stack/SKILL.md
  sha: 4b78c9d4c2b6a5209fe4bf917f45d78b73cb38e1
failure_family: F01_GATHER_BEFORE_GENERATE_BYPASS
failure_code: PREMATURE_GREENFIELD_SOLUTION_WITHOUT_HERITAGE_RECONCILIATION
symptom: proposed a Dino Runner pose-jump signal-refinery design before checking existing spatial-engine adapters, demos, recovery queue and current proof gap
occurrence_cause: recent prompt cues activated architecture synthesis and local technical completion
escape_cause: no deterministic reuse-before-create admission gate blocked generation when canonical reconciliation fields were absent
systemic_condition: prose gather-before-generate guidance competes with generative completion incentives
metadata_confidence: HIGH
operator_impact: required correction and additional reconciliation; risked adding duplicate spatial architecture and hidden WIP
waste_types:
  - OVERPRODUCTION
  - INVENTORY
  - OVERPROCESSING
  - DEFECT
  - UNUSED_CAPABILITY
safety_or_authority_impact: no external effect; increased control-plane ambiguity and delay risk
andon_pulled: true
line_stopped_or_narrowed: new Dino architecture reclassified as a possible profile/assay on the existing pipeline; recovery-first order restored
reproduction_or_trace:
  - research/VAR_SPATIAL_PIPELINE_RECONCILIATION_AND_QUORUM_20260723.md
  - commit 55bcbb1eb5df0accfdfc88030fd7f882782b89c7
countermeasure_status: PROPOSED
countermeasure_owner: UNASSIGNED_PENDING_CLAIM
independent_verifier: pending quorum
next_consumer: Sigrun or accepted control-plane consumer
next_safe_action: implement and test a deterministic reuse-before-create admission record that fails closed on missing reconciliation
stop_or_retirement: retire this receipt only after a held-out test proves the gate blocks this failure family
honest_flaw: this standard and receipt do not implement the validator or establish independent verification
```

## Metrics

Track at minimum:

- Andon pulls by failure family;
- confirmed defects caught before propagation;
- confirmed false-positive Andon pulls;
- recurrence rate after countermeasure;
- time from detection to classified receipt;
- time from receipt to implemented gate;
- percentage of receipts with model/platform/UTC metadata;
- percentage of countermeasures independently tested;
- governance-recursion count where another policy was created instead of implementation;
- avoided unauthorized effects, duplicate work or WIP hours where estimable.

Metrics must not punish honest reporting or incentivize manufacturing incidents.

## Standard-practice adoption condition

This becomes operational standard only after:

1. quorum accepts or revises the schema;
2. a canonical append-only failure registry or typed issue form exists;
3. CI/schema validation checks required fields;
4. at least three historical failures are backfilled as test cases;
5. an independent verifier tests missing-metadata, duplicate, stale-state and reward-hack fixtures;
6. changed-state Slack projection points to canonical receipts;
7. the operator or authorized controller ratifies the Andon reward policy.

Until then, this document is a proposed standard and initial evidence receipt—not an implemented control.

---
schema_id: hfo.gen133.s09.adversarial_bayesian_vote.v1
vote_id: S09_X14_MUTANT081_STALE_SOURCE_DIGEST_20260804T083334Z
seat: S09_STRATEGIC_REASONING_AND_VOTING_CELL
carrier_task_id_expected: 6a539fb148bc8191a30b6009dbf22438
carrier_task_id_observed: 6a539fb148bc8191a30b6009dbf22438
carrier_task_id_match: true
carrier_enabled_observed: true
wip: 1
valid_time_utc: 2026-08-04T08:33:34Z
transaction_time_utc: SEE_GIT_COMMIT_METADATA
canonical_repository: TTaoGaming/hfo-gen-133
canonical_branch: agent/gen133-bootstrap-20260730
verdict: REVISE
binding_weight: 0
same_provider_status: SAME_PROVIDER_ADVISORY_NONBINDING
independent_verification_closed: false
sealed: true
---

# S09 adversarial Bayesian vote — X14 mutant 081

## Self-probe

- Identity observed from native automation inventory: `HFO S09 Sigrun Recovery Queue`, task `6a539fb148bc8191a30b6009dbf22438`, enabled.
- Tools actually used before vote: native automation inventory read; GitHub branch/commit search; exact commit, file, and blob reads; local deterministic UTF-8 byte-count and SHA-256 recomputation; GitHub create-file.
- No task mutation, source edit, provider effect, deployment, merge, account/security change, spend, deletion, or quorum claim was performed.

## Exact decision packet

- Decision object: `X14_MUTANT_081_40b008bd1bf5`
- Mutant commit: `162a07c79a0a861040783f3e371b7f69b8be5171`
- Mutant path: `state/coordination/experiments/false_green_x14/quarantine/20260804T075333Z_X12_SLACK_RECEIPT_STALE_SOURCE_DIGEST.mutant.yaml`
- Source receipt commit: `7c2e22132348a40f39d17de8e6db3a7e4645bef7`
- Source receipt blob: `dc8c7a4edd55fe16fb0980beb56e03b20ef6437d`
- Current event commit/blob: `d52f9d38b3cc02309212cb276a07e386a342e429` / `1a28bdbc52ed81c4aca93d8af3707d9f65a0b531`
- Current event path: `state/coordination/experiments/durable_object_x12/events/20260804T074403Z_V0083_TO_V0084_IDEMPOTENCY_STRATEGY_UNANCHORED_CLAIM_RESUME_REVISE.json`
- CURRENT v84 commit/blob: `9dd7f389c6f6595eef66bb2a0a1238e03d623058` / `ac02d4b8754ee8119334dcd90fd5a76b432152bb`
- Predecessor event commit/blob: `65a68c5956c555a6c77e6f02b9af72ca03c295d3` / `b56a5e36adc7f1b2d33375c452d41922286ce655`
- Decision deadline: `2026-08-04T11:53:33Z`
- Source effect ceiling: `ONE_SANITIZED_SLACK_POINTER_RECEIPT`
- Vote effect ceiling: one immutable Git vote plus one concise sanitized Slack pointer.
- Structural verifier: `S04_STRUCTURAL_PREFLIGHT`, task `6a52861fbdb08191b9ef33a0b9c3c15c`.
- Consumer: `X14_CAMPAIGN_REDUCER_AND_REGINLEIF_OLRUN_DURABLE_OBJECT_CONSUMERS`.

## Candidate options

1. `ACCEPT`: treat the substituted predecessor digest as valid proof for the named current event.
2. `REVISE`: reject the stale digest, grant no event-integrity or downstream credit, and revise campaign closure so every routed mutant is terminal or explicitly missed before reduction.
3. `HOLD`: wait for an independent canonicalizer to hash exact current and predecessor bytes.
4. `RETIRE`: keep the artifact only as historical quarantine and stop repeating this conspicuous mutation class.
5. `ABSTAIN`: decline because the evidence surface is insufficient.

## Bayesian assessment

### Prior before exact reads

- `REVISE 0.60`
- `HOLD 0.15`
- `RETIRE 0.15`
- `ABSTAIN 0.05`
- `ACCEPT 0.05`

The prior favors rejection because this is an intentionally quarantined stale-digest negative control, but the producer's expected verdict is not itself verification.

### Evidence

**For REVISE**

- The immutable source receipt binds the named v83-to-v84 event commit, path, blob, and digest `a5fcf510f890d6acfbe700c289e1b94a8e2a35f432e51786230454a4feb9c816`.
- The fetched current-event blob declares the same `a5fcf510...` event digest and names the predecessor event separately.
- CURRENT v84 anchors the current event commit/path with `a5fcf510...`, not the predecessor tuple.
- The fetched predecessor event declares `d1f5f9cff4e18aac4ba673f52a1c3bffc4587cb3899b0f32d010d71246caf6a4` for the v82-to-v83 transition.
- Mutant 081 changes only `receipt.event_digest_sha256` from `a5fcf510...` to `d1f5f9cf...` while preserving the current event commit/path/blob and CURRENT v84 anchors. A real digest of different historical bytes cannot authenticate the named current bytes.
- Independent local recomputation of the mutant overlay confirmed `315` UTF-8 bytes and SHA-256 `40b008bd1bf53654318908280aca48d171b426a70c463191653086ce88b526cb`, matching the mutant ID/binding.

**Against REVISE / for HOLD**

- This seat did not independently reimplement the producer's full `JCS_LIKE_V3_RESTRICTED_INTEGER_LEXEME_ONLY` event-digest algorithm over both event projections. The decisive structural mismatch is exact, but the event digests remain producer-originated fields plus Git object reads.
- Git commit/path/blob binding proves object identity and immutability at those commits; it does not prove the semantic correctness of either event body or delivery claim.

**For RETIRE**

- The mutation is conspicuous and has close historical analogues. Repeating it may measure prompt compliance more than subtle integrity enforcement.
- The campaign was reduced while this fourth mutant was still pending, showing a more valuable reducer-timing defect than another easy digest catch.

**Against RETIRE**

- Retiring before recording the exact miss/catch would erase useful evidence that the reducer closed a four-mutant campaign without waiting for the fourth verdict deadline or explicitly marking it missed.

**For ACCEPT**

- The substituted digest is syntactically valid and genuinely belongs to the same object history.

**Against ACCEPT**

- Same-history membership is not event authentication. Accepting it would sever digest-to-commit/path/blob/version-edge binding and create false event-integrity, CURRENT-anchor, delivery, and outcome credit.

**For ABSTAIN**

- No distinct provider or nonproducer canonicalizer has independently consumed this packet.

**Against ABSTAIN**

- The exact stale-field substitution and current/predecessor identity mismatch are available and sufficient for a nonbinding structural vote.

### Posterior

- `REVISE 0.86`
- `RETIRE 0.07`
- `HOLD 0.04`
- `ABSTAIN 0.02`
- `ACCEPT 0.01`

## Correlated-evidence risk

X12 source artifacts, X14 mutant construction, S04/S09 reviews, and Git/Slack receipts are all produced or interpreted inside the same ChatGPT-carried control plane. Agreement between S04 and S09 must not be counted as an independent majority. Git object identity and deterministic byte/hash mismatch reduce ambiguity, but they do not create provider diversity, ConsumerAck, or binding authority.

## Strongest dissent

`HOLD`: do not award even structural catch credit until a distinct implementation fetches the exact current and predecessor blobs, applies the declared canonicalization profile, and independently reproduces both event digests. This dissent is strongest where the campaign wants credit beyond merely rejecting the mutant.

## Opportunity cost

- Accepting the mutant risks laundering a stale event into accepted history and contaminating delivery, idempotency, and outcome accounting.
- Holding indefinitely spends verifier cycles on an intentionally obvious mutant.
- Retiring immediately misses the campaign-reducer defect: campaign 20 closed with the fourth routed verdict pending rather than terminal-or-explicitly-missed.

## Operator-minute burden

- Immediate operator burden: `0 minutes`.
- Recommended next assay burden: `0 operator minutes`; automated only, no provider/world effect.

## Reversible next experiment

Retain this artifact as quarantined non-executable evidence. In a later campaign, test one subtler coherent stale-tuple replay: predecessor event commit, path, blob, and digest all agree with each other while the receipt's version edge, nonce/idempotency key, or CURRENT anchor remains current. Require the gate to reject the cross-anchor mismatch. Do not mutate accepted history or provider state.

## Falsifier

This vote is falsified if exact independent reads show either:

1. the named current event bytes canonically hash to `d1f5f9cf...`, or
2. CURRENT v84 actually anchors the predecessor v82-to-v83 event tuple, or
3. the receipt schema explicitly defines `event_digest_sha256` as a predecessor digest rather than the named event digest.

No inspected source supports any of those conditions.

## Vote

`REVISE`

- Reject mutant 081 for `STALE_PREDECESSOR_DIGEST_DOES_NOT_BIND_NAMED_CURRENT_EVENT_BYTES`.
- Grant zero event-integrity, CURRENT-anchor, delivery, ConsumerAck, adoption, fitness, outcome, or independent-verification credit.
- Record campaign-20 reduction as structurally premature unless mutant 081 becomes terminal before its deadline or is explicitly classified missed; do not count a late verdict retroactively as an on-time catch.
- Binding weight remains `0` until independently consumed by a distinct decision-maker.

## Honest flaw

This vote independently verified the mutant overlay byte count/hash and exact Git identities/declared digest mismatch, but did not independently reimplement the full event canonicalization profile or verify Slack persistence. Readback of this vote is integrity confirmation, not self-verification.
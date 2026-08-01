---
schema_id: hfo.gen133.x13.cots_connector_probe_manifest.v1
experiment_id: X13_SLACK_PUBLIC_CHANNEL_CONNECTOR_001
seat: X13_COTS_CONNECTOR_PDCA
carrier_task_id_expected: 6a55c1733708819185088bf334e33ea5
carrier_task_id_observed: 6a55c1733708819185088bf334e33ea5
carrier_task_id_match: true
carrier_task_id_observation_source: AUTOMATION_RUNTIME_PROMPT
native_task_inventory_read_this_wake: false
phase: 2
campaign_wake: 2_of_4
prior_current_version: 9
expected_next_current_version: 10
prior_current_blob_sha: 21dc856e119d9359df98db435629a9f165f3c1c0
candidate: Slack_public_channel_connector
canonical_repository: TTaoGaming/hfo-gen-133
canonical_branch: agent/gen133-bootstrap-20260730
valid_time_utc: 2026-08-01T06:48:30Z
transaction_time_utc: SEE_GIT_COMMIT_METADATA
wip: 1
target_channel_id: C0BGNGPJFHU
effect_ceiling: EXACTLY_ONE_CONCISE_PUBLIC_CHANNEL_POINTER_POST_AND_BOUNDED_DIRECT_HISTORY_READBACK
operator_relay_minutes_budget: 0
paid_cost_usd_budget: 0
verifier: S04_STRUCTURAL_PREFLIGHT_THEN_DISTINCT_NONPRODUCER_BEFORE_HIGHER_EFFECT_USE
consumer: Ratatoskr_and_Olrun
expiry_utc: 2026-08-08T06:48:30Z
same_provider_binding_weight: 0
sealed: true
---

# X13 phase 2 Git-first Slack pointer manifest

This immutable manifest authorizes one bounded public-channel micro-use after exact Git
readback. The posted message must contain only this experiment identifier, the manifest
commit and blob identifiers, the expected `CURRENT` transition `v9 -> v10`, a no-action
notice, and the same-provider/nonbinding marker.

Deterministic message form:

`X13 PHASE2 MICRO-USE | Slack public-channel connector | Git-first manifest commit=<MANIFEST_COMMIT> blob=<MANIFEST_BLOB> | expected CURRENT v9->v10 | no action requested | SAME_PROVIDER_NONBINDING`

Acceptance requires:

1. exactly one post to `C0BGNGPJFHU`;
2. a returned Slack message timestamp or permalink;
3. direct bounded channel-history readback containing the exact submitted message;
4. no private data, mention, attachment, thread broadcast, edit, deletion, or second post;
5. an immutable measured-result event followed by exact-SHA `CURRENT` update from v9 to v10.

Failure classes to record include permission denial, channel-not-found, ambiguous send,
missing direct readback, content transformation, duplicate post, rate limit, transport
failure, and connector-return/readback disagreement.

Rollback is containment rather than deletion: do not edit or delete the harmless pointer;
stop further writes and emit an Andon only if the post or readback violates this manifest.
The strongest falsifier is a send reported as successful that cannot be found by direct
channel history with the exact body and timestamp, or a post that reaches another channel.

Honest flaw: a Slack message is a durable provider-side write and is not reversible under
the no-deletion ceiling. This probe tests bounded exact-post/readback behavior, not message
immutability, retention, least privilege, quota predictability, independent verification,
or ConsumerAck.

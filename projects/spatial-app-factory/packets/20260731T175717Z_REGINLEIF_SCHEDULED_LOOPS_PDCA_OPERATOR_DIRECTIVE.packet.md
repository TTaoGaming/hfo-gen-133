---
schema_id: hfo.gen133.reginleif_scheduled_loops_pdca_operator_directive.v1
packet_id: REGINLEIF_SCHEDULED_LOOPS_PDCA_20260731T175717Z
callsign: Ratatoskr
lineage_id: lineage_61cd69f1c256
coordinate: [4, 7]
port: P7_NAVIGATE
generation: 133
valid_time_utc: 2026-07-31T17:57:17Z
transaction_time_utc: SEE_GIT_COMMIT_METADATA
canonical_repo: TTaoGaming/hfo-gen-133
canonical_branch: agent/gen133-bootstrap-20260730
activation: ONLY_WHEN_OPERATOR_PASTES_THE_DIRECTIVE_VERBATIM_INTO_REGINLEIF_CHATGPT_CLOUD_THREAD
status: PASTE_READY_NOT_YET_CONSUMED
claim_status: proposed
wip: 1
effect_ceiling: FILE_AND_MESSAGE_COORDINATION_ONLY_THIS_PACKET_PERFORMS_NO_SCHEDULED_TASK_MUTATION
privacy_class: SANITIZED_PUBLIC_NO_CREDENTIAL_ACCOUNT_POLICY_MEDICAL_OR_FAMILY_DETAILS
references:
  ratatoskr_loop_design_commit: 85e706e2152a7c7cdc751148c35abd6cbf2b99de
  reginleif_loop_design_commit: 721504d17d1c82d32195627a889c3a8d29198eda
verifier: Sigrun/P4_APEX_FALSIFICATION
consumer: Reginleif/lineage_0dc1db03347f
expiry: 2026-08-03T17:57:17Z
sealed: false
---

# Paste-ready operator directive for Reginleif

This file carries the exact bounded instruction the operator can paste into the
manual Reginleif ChatGPT Cloud control thread. The authority below is **not
active merely because it exists in Git**. It activates only when the operator
pastes it verbatim into Reginleif's current thread.

The packet is intentionally narrower than “repair all fifteen.” It authorizes a
measured S02 admission canary, then an S03 reduction canary only after S02 passes.
It does not authorize mass restoration or another architecture cycle.

## Copy from here

```text
Use the current best non-Pro ChatGPT model available to this Reginleif manual thread.

Wake as REGINLEIF:

callsign: Reginleif
lineage_id: lineage_0dc1db03347f
mode: GEN133_SCHEDULED_LOOPS_PDCA_STEWARD
controller: operator_direct
canonical_repository: TTaoGaming/hfo-gen-133
canonical_branch: agent/gen133-bootstrap-20260730
wip_limit: 1

This pasted message is fresh, exact operator authority for one bounded Scheduled Tasks PDCA experiment. It supersedes stale transition-era text requiring a Ratatoskr mutation packet. Reginleif owns ChatGPT Scheduled Tasks inventory and mutation. Ratatoskr does not mutate tasks from its Pro thread.

Read first, in order:

1. `projects/spatial-app-factory/packets/20260731T175717Z_REGINLEIF_SCHEDULED_LOOPS_PDCA_OPERATOR_DIRECTIVE.packet.md`
2. `state/coordination/receipts/reginleif/20260731T174200Z_CHATGPT_CLOUD_LOOP_ENGINEERING_SPATIAL_FACTORY_CONTROL_PACKET.md`
3. `projects/spatial-app-factory/packets/20260731T174610Z_CHATGPT_CLOUD_LOOP_ENGINEERING_AND_GOLDEN_PATH.packet.md`
4. the newest Gen-133 Git head and only changed Slack state in `C0BGNGPJFHU` and `C0BGC646A1H`
5. the native Scheduled Tasks inventory once

GOAL

Prove or falsify one useful ChatGPT-cloud scheduled loop for the spatial app factory while lowering operator cognitive load. Success is not 15/15 enabled. Success is:

`READY WorkItem -> exact claim -> real producer return -> tested/source readback -> distinct-provider STOOD|FELL -> named ConsumerAck -> terminal Gen-133 receipt`

Zero primary fitness: wake, heartbeat, queue-empty, task enabled, commit count, Slack post, draft, schema-valid artifact, repeated unchanged Andon, or same-provider PASS.

AUTHORITY CEILING

You may inspect all fifteen exact HFO tasks. You may mutate only these exact task IDs, sequentially and under the gates below:

- S02 admission/pull: `6a55088a3d308191ac1cda97221f0957`
- S03 reducer/ConsumerAck: `6a539fc5130c81918c13624739fb2a60`

For S02 and S03 only, you may:

- snapshot the complete current task record;
- replace the instructions with the bounded contracts below;
- enable or resume the task;
- later pause it as rollback;
- read the exact provider record back after every mutation.

Preserve each existing task ID, name/title, hourly-indefinite schedule, timezone, staggering, notification settings, and associated chat. Do not create, delete, clone, rename, retime, bulk-enable, or change any other task or account setting. Do not mutate S03 until S02 passes its canary. Do not restore S06-S10 or X11-X14 under this authority.

BASELINE / PLAN

1. Read the full native inventory once and bind each of the fifteen stable IDs to enabled state, schedule, last run, updated time, and a SHA-256 digest of its current instructions.
2. Verify that all fifteen exact records still exist, all remain hourly and indefinite, and no unexpected identity or cadence drift exists.
3. Record the baseline Git-first, read it back, and post one concise Slack pointer.
4. If the provider state differs materially from the expected four enabled seats `[S01,S04,S05,S15]`, do not blindly apply this plan. Re-plan from the fresh inventory and remain within the same two-task ceiling.
5. Preserve rollback data for S02 and S03 before changing either one. Do not publish private task content; store sanitized exact text only when safe, otherwise store the provider record digest plus sufficient local rollback state.

PDCA CYCLE A — S02 ADMISSION/PULL CANARY

Update only S02 instructions to this operating contract, preserving its existing schedule and identity:

--- S02 CONTRACT START ---
You are HFO Gen-133 S02 Admission/Pull, a one-pass Scheduled Task carrier. You are a job, not a daemon. WIP=1.

Every wake:

0. Self-probe the native task ID. It must equal `6a55088a3d308191ac1cda97221f0957`. Record actual available tools and permissions. Mismatch or missing required Git read/write means HOLD once, then stop.
1. Read the newest head of `TTaoGaming/hfo-gen-133` on `agent/gen133-bootstrap-20260730`.
2. Read the exact operator packet at `projects/spatial-app-factory/packets/20260731T175717Z_REGINLEIF_SCHEDULED_LOOPS_PDCA_OPERATOR_DIRECTIVE.packet.md` and its referenced spatial golden-path packet.
3. Treat `SPATIAL_FACTORY_GOLDEN_APP_001` as the sole READY WorkItem for this canary. Compute an idempotency key from `work_item_id + source_commit + source_path + acceptance_contract_digest`.
4. Search Gen-133 for an existing claim with that idempotency key. If one exists, do not claim again. If no eligible unclaimed WorkItem exists or all relevant input digests are unchanged, `YIELD_SILENT`: no Git receipt and no Slack post.
5. If eligible and unclaimed, create exactly one immutable Gen-133 claim receipt. Bind the exact source commit, path, blob, idempotency key, lease expiry, effect ceiling, named next consumer `Olrun/Claude-Dispatch`, acceptance test, verifier, and honest flaw.
6. Read the created Git bytes back. Only after exact readback, post one concise material Slack pointer to `C0BGNGPJFHU`.
7. Do not implement the app, invent another queue, create another architecture root, perform a send/deploy/merge/publication, or grade your own claim. Yield.

Required result vocabulary: `CLAIMED | YIELD_SILENT | HOLD | FELL`.
--- S02 CONTRACT END ---

After mutation:

1. Read S02 back and verify exact ID, instructions digest, enabled state, and unchanged schedule.
2. Read the complete fifteen-task inventory back. Any unexpected change outside S02 is an immediate circuit-breaker.
3. Observe at most two closed S02 hourly wakes.

S02 PASS requires all of:

- exactly one claim for `SPATIAL_FACTORY_GOLDEN_APP_001`;
- no duplicate claim or second queue;
- exact Git commit/path/blob readback;
- one named Olrun consumer and expiry;
- no world effect beyond the file/message ceiling;
- unchanged input on the second wake produces silence, not another receipt.

S02 FAIL/HOLD triggers:

- no claim after two eligible wakes;
- wrong task ID or missing required tool;
- duplicate claim;
- another task is unexpectedly modified, disabled, or rate-restricted;
- schedule/title/timezone drift;
- it invents work or a new queue;
- it posts queue-empty or repeated unchanged messages;
- it exceeds its effect ceiling.

On FAIL/HOLD, pause S02, restore its prior instructions if safe and exact, write one Git-first Andon with the failed edge, and stop. Do not proceed to S03.

PDCA CYCLE B — S03 REDUCER / CONSUMERACK CANARY

Proceed only after S02 PASS and only when a real producer return for the exact S02 claim exists in Git. Do not synthesize a producer return.

Update only S03 instructions to this operating contract, preserving its existing schedule and identity:

--- S03 CONTRACT START ---
You are HFO Gen-133 S03 Reducer/ConsumerAck, a one-pass Scheduled Task carrier. You are a job, not a daemon. WIP=1.

Every wake:

0. Self-probe the native task ID. It must equal `6a539fc5130c81918c13624739fb2a60`. Record actual tools and permissions. Mismatch or missing required Git access means HOLD once, then stop.
1. Read the newest Gen-133 head and the exact S02 claim for `SPATIAL_FACTORY_GOLDEN_APP_001`.
2. Find a real producer return that binds the S02 claim commit, exact changed bytes or build/test/source-system readback, real exit codes where applicable, effect ceiling, and rollback. No return means `YIELD_SILENT`.
3. If the return lacks required evidence, write one `REVISE` request to the named producer and yield. Do not repair the producer's work yourself.
4. Route one exact verification packet to a distinct provider/nonproducer. S04 same-provider structural preflight may be read but has binding weight zero and cannot close the loop.
5. Consume only an exact `STOOD | FELL` verdict that binds the producer return digest and held-out acceptance test.
6. After `STOOD`, obtain explicit ConsumerAck from `Olrun/Claude-Dispatch` as spatial-factory coordinator. A Slack post, heartbeat, or implicit read is not ConsumerAck.
7. Write one terminal Gen-133 receipt only when producer return, distinct verdict, and ConsumerAck all bind to the same WorkItem and digests. Read it back, post one material Slack pointer, then yield.
8. If inputs are unchanged or the loop is waiting on producer/verifier/consumer before expiry, `YIELD_SILENT`.

Required result vocabulary: `REVISE | STOOD_AND_ACKED | FELL | YIELD_SILENT | HOLD`.
--- S03 CONTRACT END ---

After mutation:

1. Read S03 and the complete task inventory back.
2. Observe at most two closed S03 hourly wakes after all required inputs exist.

S03 PASS requires one terminal Gen-133 receipt binding:

- S02 claim;
- real producer return and readback;
- distinct-provider/nonproducer `STOOD`;
- named Olrun ConsumerAck;
- one exact terminal outcome;
- zero operator state-ferry events after this directive.

S03 FAIL/HOLD triggers:

- same-provider PASS is treated as terminal;
- no ConsumerAck after one reducer epoch once a distinct verdict exists;
- output is only a draft, architecture document, queue report, or Slack message;
- producer/verifier/consumer digests do not bind;
- duplicate terminal receipts;
- any unauthorized task or world effect;
- more than one Olrun browser recovery nudge is needed for the same transition.

On FAIL/HOLD, pause S03, preserve S02 evidence, write one Andon naming the exact failed edge, and stop. Do not restore additional seats.

OLRUN DEADMAN RULE

Olrun browser control is an external deadman, not the routine scheduler. It may nudge the existing Reginleif or Ratatoskr thread once when:

- a required receipt is missing by scheduled epoch + 15 minutes;
- a claim lease expires;
- a required canary is paused or disabled;
- a producer return, distinct verdict, or ConsumerAck waits beyond its stated expiry.

One packet version gets one browser nudge. A second failure becomes one Andon and stop. Do not click repeatedly, invent work, rewrite prompts outside this authority, or ask the operator to ferry Git/Slack state.

CHECK / SCORECARD

Measure:

- closed useful loops;
- READY-to-ConsumerAck latency;
- operator minutes and state-ferry events per closed loop;
- producer returns consumed / producer returns written;
- duplicate receipts and unchanged notifications;
- browser deadman interventions;
- exact build/test/source readbacks.

Wake count, enabled count, commit count, prose volume, and same-provider agreement have zero primary fitness.

ACT

- If Cycle A and B pass: keep S02/S03 enabled, mark `SPATIAL_FACTORY_GOLDEN_APP_001` closed, log exact receipts, and propose—but do not execute—the next wave for S06-S10.
- If either fails: roll back/pause only the failed canary, preserve evidence, identify the exact broken edge, and yield.
- Do not mass-restore the portfolio under this directive.

REPORTING

Git first, exact readback, one material Slack pheromone per state transition. No hourly queue-empty or unchanged-drift messages. Return to the operator only:

1. PASS with exact claim/terminal receipts;
2. HOLD/FELL with the exact broken edge and rollback receipt;
3. APPROVAL_REQUIRED for a genuinely private or irreversible effect.

Verifier: Sigrun/P4 apex falsification.
Consumers: Olrun for host execution and ConsumerAck; Ratatoskr for technical fan-in.
Authority expires at `2026-08-03T17:57:17Z` or immediately after one terminal PASS/FELL, whichever comes first.

No send, spend, payment, deployment, merge, publication, permanent deletion, account/security mutation, seal, IMMUNIZE, or permaweb upload is authorized.
```

## Copy ends here

## Why this is the correct forcing-function shape

The native platform supplies a clock, task inventory, edit/pause/resume controls,
monitoring memory, notifications, and connected-app access when enabled. It does
not supply a webhook, transactionally shared queue, cross-provider quorum,
ConsumerAck, or a guarantee that an unattended task remains active. Those missing
properties are supplied through exact Git packets, idempotency, leases, held-out
acceptance, provider separation, readback, silence-on-unchanged, rollback, and an
external deadman.

Official product facts were checked against OpenAI's “Scheduled Tasks in ChatGPT”
help article on 2026-07-31:

- Pro supports up to fifteen active tasks;
- no task may run more than once per hour;
- monitoring tasks remember prior runs and can notify only on meaningful change;
- unattended tasks may pause;
- tasks can use connected apps subject to permissions;
- tasks do not support webhooks;
- tasks do not support Pro models, voice chats, file uploads, or GPTs;
- a task created in a Project cannot access that Project's files.

Source: https://help.openai.com/en/articles/10291617-scheduled-tasks-in-chatgpt

## Honest flaw

This packet does not prove that Scheduled Tasks expose the same GitHub/Slack write
surface on every unattended wake, that provider timing will meet the requested
15-minute deadman tolerance, that Olrun browser control is reliable, or that the
spatial producer will return within the canary window. It deliberately uses
self-probe and HOLD rather than assuming those capabilities. No task mutation was
performed by creating this file.

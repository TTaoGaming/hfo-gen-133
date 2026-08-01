# Herfjotur Noria Failure Diagnostics Yield

callsign: herfjotur
lane: local diagnostics / free-mesh p0-p6 readiness
status: PARTIAL_LOCAL_GREEN
utc: 2026-06-14T01:56Z
claim_ceiling: local_no_egress_diagnostics_only

## Intake

Read first:

- `inbox/gunnr/20260614T0138Z_reginleif_free_mesh_readiness_diagnosis.md`
- `inbox/gunnr/20260614T0137Z_olrun_hrist_guard_green_operator_board.md`
- `work/moba_q_shared_blackboard/state/latest.md`

Current truth consumed:

- Blackboard guard is `GREEN_BOUNDED`.
- Routine p0/p6 free mesh is ANDON/unavailable because quorum fails closed.
- Family A is valid in current quarantine samples.
- Family B is absent from current quarantine samples.
- Family C is malformed or schema-contract-invalid.
- The routine wrapper still has a capture gap: stdout/stderr/exit/final-json status are not separated well enough when the child exits before final JSON.

## Files Changed

- `scripts/sigrun_noria_failure_diagnostics.py`
- `scripts/test_sigrun_noria_failure_diagnostics.py`

## What Changed

Added a local/no-egress companion verifier that replays existing quarantine samples under:

- `state/sigrun/wake_runner_free_mesh_runs/noria-p0-20260614T012618Z/quarantine_in/`
- `state/sigrun/wake_runner_free_mesh_runs/noria-p6-20260614T013002Z/quarantine_in/`

It does not call providers, read secrets, start scheduler, deploy, push, or merge. It reads quarantined local wrapper files and classifies failure modes by family.

Classifier coverage:

- `family_b_absent`
- `family_c_schema_id_mismatch`
- `family_c_missing_question_id`
- `family_c_json_parse_failed`
- additional type mismatches: confidence and boolean fields as strings

## Verification

```text
python -m unittest scripts.test_sigrun_noria_failure_diagnostics
...
Ran 3 tests in 0.017s
OK
```

```text
python scripts\sigrun_noria_failure_diagnostics.py --json
status=LOCAL_REPLAY_COMPLETE
aggregate_failure_classes=[
  family_b_absent,
  family_c_confidence_type_mismatch,
  family_c_external_action_authorized_type_mismatch,
  family_c_json_parse_failed,
  family_c_missing_question_id,
  family_c_native_quorum_effect_type_mismatch
]
can_classify family_b_absent=true
can_classify family_c_schema_id_mismatch=true
can_classify family_c_missing_question_id=true
can_classify family_c_json_parse_failed=true
```

```text
python -m py_compile scripts\sigrun_noria_failure_diagnostics.py scripts\test_sigrun_noria_failure_diagnostics.py
# exit 0, no output
```

```text
git diff --check -- scripts\sigrun_noria_failure_diagnostics.py scripts\test_sigrun_noria_failure_diagnostics.py
# exit 0, no output
```

## Answer To Live-Retry Diagnostic Question

With this companion verifier, the next live retry would have enough local replay logic to classify:

- `family_b_absent`: yes, if no family B sample is present for the run.
- `family_c_schema_id_mismatch`: yes, classifier and unit test cover it.
- `family_c_missing_question_id`: yes, present in current p0 quarantine replay.
- `family_c_json_parse_failed`: yes, present in current p6 quarantine replay.

It still would not persist separated stdout/stderr/exit/final-JSON status from the PowerShell runner. The next smallest wrapper patch should add those capture fields to `scripts/sigrun_noria_runner.ps1`; I did not patch it in this pass because the companion verifier was the smaller local/no-egress step.

## Top Blocker

Diagnostics are better, but the routine wrapper still loses stderr/traceback and may persist zero-byte raw logs. Until that is patched, failures can still collapse to `UNAVAILABLE` in the blackboard sidechain row even when quarantine samples are classifiable.

## Next Pull

Patch `scripts/sigrun_noria_runner.ps1` to persist separate:

- stdout path + byte count
- stderr path + byte count
- process exit code
- raw log byte count
- final JSON parse status/error

Then run the companion verifier against the next p0/p6 failed run before any live retry decision.

## Walls

No live vendor call, no network, no scheduler start, no deploy/push/merge, no secrets/.env/HMAC read, no private data, no external action.

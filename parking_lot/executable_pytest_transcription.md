# PARKED — transcribe held-out tests to executable pytest

```yaml
feature: executable_pytest_transcription
status: PARKED — BLOCKED on code-authoring lease
spec: tests/held_out/RED_FIRST.md §2
parked_by: SIGRÚN P4 · 2026-07-30
```

## Purpose

Turn the 13 `red_first.md` specifications into runnable `pytest` files, so that
`python -m pytest tests/held_out -q` produces **13 genuine reds** rather than a
collection error.

## Why parked

I attempted it. The enforcing gate denied all three files:

```
[hfo-gate enforcing] code_authoring: no valid lease for code_authoring
  (required verb=EMERGENCY_FORGE) | OPA: material action requires
  reputation_spend descriptor
```

That is the Claude compose-lane code-touch policy firing **correctly**. I hold no
`EMERGENCY_FORGE` lease. Routing around a safety gate to make a deliverable look
more complete is exactly the failure this generation exists to prevent, so I took
the directive's stated fallback — `red_first.md` per test dir with the exact
failing invocation — instead.

## Environment (confirmed, for whoever holds the lease)

```
forge root: C:\Dev\hfo_gen_133_forge
python:     3.12.10   (on PATH)
pytest:     9.0.2     (installed)
deps:       NONE needed — every assertion is stdlib-only
```

## Dependencies

| # | dependency |
|---|---|
| 1 | operator types `verb=EMERGENCY_FORGE`, **or** the work routes to a code lane (Codex / free-mesh) which is the better answer |
| 2 | the shared helpers in `RED_FIRST.md` §4 (`canon`, `canon_sha256`, `read_jsonl`, `REPO`) become `tests/held_out/conftest.py` |
| 3 | each dir gets `test_<subsystem>.py` transcribed from its `red_first.md` |

## What to watch for during transcription

- Several assertions reference helpers that do **not exist yet**
  (`recompute_rollup`, `substrate_removed`, `audit_effects`, `slack_unreachable`,
  `kill_carrier`). Those are harness, not tests. Stub them to `pytest.fail("RED:
  harness absent")` rather than deleting the assertion.
- `rehydration_abi::test_integrity_failure_exits_2` is **known-wrong as written**
  — it rehydrates an untampered capsule and asserts exit 2. Corrupt a byte first.
  Flagged in its own file.
- `neurosymbolic_gates::test_G4_still_denies_a_genuine_destructive_command`
  **must not be run against a live tree.** It needs a sandbox.
- `gleipnir_grimoire::test_no_agent_can_satisfy_publish_preconditions` is
  **red-by-design** and must never go green through agent action.

## When to revisit

This is the **first verification step** of the whole specification. Until these
run, the assertions are specified rather than exercised — and a specified
assertion can be subtly unsatisfiable or trivially satisfiable without anyone
finding out.

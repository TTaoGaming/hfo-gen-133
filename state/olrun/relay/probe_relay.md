# Olrun relay synthesis

- generated_utc: 2026-08-02T18:21:34Z (clock_source: host_read)
- sources_read: 1 | unreadable: 1

## Headline

1 of 1 sources carry a nonzero exit or an adverse claim_status (failed, partial, proposed). Read those first.

## Per-source receipts

- `chains/OLRUN_FACADE.jsonl` -- claim_status failed x45/partial x7/proposed x161/wired_with_receipts; counts 486

## Honest flaws carried forward

- no capsule has been harvested yet at definition time
- cross-family strength is aspirational until non-Ollama lanes auth
- 0 artifacts staged at definition time; STAGE boundary untested end-to-end
- reduces operator load only modestly: doing-clicks becomes approving-clicks
- cannot detect a problem no source named
- prose value judgment still requires quorum vote
- gate refusal is advisory-in-process; a caller invoking the runner directly bypasses this dispatcher entirely
- a source that lies in its own exit_code/claim_status field is relayed faithfully; the relay does not re-verify upstream claims
- plumbing proven, retrieval QUALITY unproven; bm25 surfaces mentions not merit
- gate tested via CLI only; no test proves a MALFORMED envelope value fails closed rather than open
- a 100% pass rate on a gate is evidence the gate did not bind, not evidence of quality
- I did not read the tool's --out contract before driving it at scale; the tool also fails late instead of failing fast
- approval rubric was authored by opus-5 and is meant to be ratified by opus-5 Sigrun - same-family, the exact drift the quorum exists to catch
- exit_code 0 proves the process ran, not that the skill's claim is true
- exit 0 from a dispatched runner proves the process ran, not that the skill did what it claims; the dispatcher never re-verifies downstream output
- the invariant was pre-registered in the SKILL.md and the tool built to honor it violated it anyway - specs do not constrain code, tests do
- under load the slow careful models time out first, so this bug manufactured agreement precisely when the host was least healthy
- I built the quorum, ran it on 100 capsules, and the honest result is that its output cannot be used - the measurement invalidated the pipeline it was measuring

## Unreadable sources

- `state/ssot/NO_SUCH_FILE.json` -- not found

## Next safe action

Open only the sources flagged above. Everything else is accounted for.


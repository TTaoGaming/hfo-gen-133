```yaml
schema_id: hfo.gen133.forge_post_mortem.v0_1
forge_id: F8
pattern_class: internal-instrument
name: EMERGENCY_FORGE pattern formalization v1
model: claude-opus-5
now_utc: 2026-08-02T04:38:55Z
clock_source: host_read
timebox_min: 90
claim_status: wired_with_receipts   # probe only
blameless: true
```

# Post-mortem — F8

## Prior post-mortems in this class that I read, by filename

**None. This directory did not exist before this forge.** That is the honest and
damning answer, and it is exactly the field §6 exists to force. The next
`internal-instrument` forge reads this file.

## What was built

- `state/patterns/EMERGENCY_FORGE_PATTERN_v1.md` — 2,181 words.
- `tools/verify_forge_dispatch.py` — stdlib, ~140 lines, the activation probe.
- `state/ssot/forge_dispatches.jsonl` — 12 retro rows, the historical scan as data.
- `cap-emergency-forge-pattern-compliance` in `state/ssot/capability_registry.json`.

## What external signal was pre-registered

None — correctly. This is `internal_fitness_only: true` with a retirement
condition: **the next 3 EMERGENCY_FORGE dispatches must each cite the pattern doc
and append a compliant ledger row, by 2026-09-02.** Fewer than 3 of 3 → the
pattern is retired and the next attempt is a hook, not a document.

## What arrived

`python tools/verify_forge_dispatch.py` → exit 0, 12 rows, **base rate 0%**, and
it independently fired the §4 rule: `internal-mechanism-build` DEAD (5 forges,
0 signal). Negative test on a doctored row → exit 1 with 5 named violations.
Census: `cap-emergency-forge-pattern-compliance ALIVE exit=0`, `ALIVE=7 DEAD=8 LEAKED=0`.

## What the next forge in this class must not repeat

1. **Do not let the probe test file existence.** My first instinct for the
   compliance probe was `glob_min state/forge_post_mortems/*.md`. That is the
   exact defect F7's author was caught committing four minutes after diagnosing
   it. The probe must run a checker over data.
2. **Registration is not enforced.** A dispatch that skips the ledger is
   invisible to the census. Do not read `exit=0` as "every forge complied" — read
   it as "every forge that registered, complied." Close this with a PreToolUse
   hook before adding any further instrument.
3. **Two sonnet lanes wrote the same disclaimer 24h apart (E1).** The cure is
   step 1 of §6 — read the class's post-mortems by glob before dispatching. If a
   future forge writes "None" in the first section of its post-mortem while files
   exist in this directory, the mechanism has failed and should be reported as
   such rather than quietly tolerated.

## Honest flaw of this post-mortem

It was written by the same session that did the work, in the same pass — the
propose/dispose split named in `C:\Dev\CLAUDE.md` RBR #3 and still unimplemented.
A generator grading its own output grades generously. Treat the §7 kill list as
`proposed`, not adjudicated.

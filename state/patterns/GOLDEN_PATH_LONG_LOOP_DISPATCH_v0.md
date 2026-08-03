---
schema_id: hfo.pattern.golden_path_long_loop_dispatch.v0_1
codified_utc: ~2026-08-03T~morning
codified_by: olrun_operator_authorized
purpose: formalize how to dispatch 4hr+ autonomous loops to Codex (or any external agent) so operator stops being event-bus
external_fitness_test: within 3 subsequent long-loop dispatches, does the operator paste-and-forget (yes) or need to micromanage (no) — if micromanage in 2/3, this pattern is DEAD
---

# GOLDEN PATH — LONG LOOP DISPATCH v0

**When to use:** operator has a bounded goal that can run 4-12hr autonomously on an external substrate (Codex GPT, Claude Code, ChatGPT Agent, external MCP-connected agent). Operator wants stop-being-event-bus discipline.

**When NOT to use:** work that requires per-decision operator judgment mid-flight (e.g. picking niches, approving external sends). Those stay in HFO dispatch with class-preauth envelope.

## The 7-part loop-prompt template

Every long-loop dispatch to an external substrate MUST have these 7 parts. Missing any = high probability of drift / reward-hack / silent-fail.

### 1. GOAL (one sentence, bounded, verifiable)
Not "improve X." Instead: "ship N artifacts of type T with property P by deadline D."

### 2. STARTING INVENTORY (what to read first, with paths)
- Prior work already done (avoid duplication)
- Reference documents (canon, capsules)
- API keys available (which tools work without operator sign)
- Explicit exclusions (what NOT to touch)

### 3. WORK QUEUE (source of next items)
- RSS feeds, public URLs, cached lists
- Skip criteria (dedupe rules)
- Rotation (per-category balance)

### 4. LOOP (numbered steps, each with success/fail branch)
```
LOOP (repeat until <stop conditions>):
1. Pick next item from queue
2. Do action
3. TEST BEHAVIORALLY (invoke + assert, not doc-exists)
4. If test fails, retry differently (max 3 attempts per item)
5. Register receipt (chain row + capability + file)
6. Increment counters
```

### 5. STOP CONDITIONS (multiple, whichever hits first)
- Target reached: N artifacts of type T
- Wall clock: X hours
- Consecutive fails: M in a row
- External signal: any of {operator ping, external human interaction with output}

### 6. DELIVERABLE (specific paths, verifiable receipts)
- File path or URL pattern per artifact
- Chain-row schema per artifact
- Progress command operator can run one-liner

### 7. NEVER LIST (explicit prohibitions)
- SEND / PUBLISH / SPEND without operator sign
- Modify original heritage files (COPY-WITH-RECEIPT discipline)
- OAuth new platforms mid-loop
- Fabricate receipts (silent-drift = REWARD_HACK, must halt + andon-pull)

## Companion pattern: SCHEDULED CHECKIN

Every long-loop dispatch is paired with a `mcp__scheduled-tasks__create_scheduled_task` scheduled ~1hr before expected wall-clock deadline:
- Probes filesystem for per-loop progress
- Writes report to `state/olrun/CODEX_LOOP_CHECKIN_<utc>.md`
- Andon-pulls if any loop is RED (< 20% of target)
- Sends operator relay via SendUserMessage or `inbox/operator/`

## Companion pattern: OPERATOR ANDON ONE-LINER

Every long-loop dispatch produces a shell one-liner operator can paste to any terminal for instant mid-flight status. Format:
```bash
cd <forge> && \
  echo "L1 <metric>: $(<probe_command>)" && \
  echo "L2 <metric>: $(<probe_command>)" && \
  ...
```

## Companion pattern: TRACKER FILE

Every long-loop batch gets a tracker file at `state/olrun/CODEX_GOAL_LOOP_TRACKER_<utc>.md` with:
- Per-loop: substrate, launched_utc, target, deliverable_path, stop_conditions, envelope, progress_command, health
- Scheduled checkin ref
- Operator andon one-liner

## Class-preauth envelope (default)

- **BUILD / TEST / DEPLOY-TO-CLOUDFLARE-PAGES / STAGE = pre-authorized**
- **SEND / PUBLISH / POST / SPEND / OAUTH-NEW-PLATFORM = STOP + andon-pull**

## Anti-patterns to avoid

- **Vague goals** ("improve X") — drift guaranteed
- **No behavioral test** ("assert file exists") — reward-hack guaranteed
- **No dedupe rule** — repeats guaranteed
- **No inventory** — silent duplication with prior work
- **No scheduled checkin** — silent-drift undetected
- **No never-list** — external send at 3am

## First 3 dispatches this pattern was used for (base rate for external-fitness test)

1. 2026-08-03T~morning: LOOP 1 SUIKA-VARIANT-EXPANDER
2. 2026-08-03T~morning: LOOP 2 DISTRIBUTION-DRAFT-EXPANDER
3. 2026-08-03T~morning: LOOP 3 HERITAGE-MINER-CURATOR

**External-fitness verdict pending:** if 2/3 hit target without operator micromanagement mid-flight, pattern is VALID. If 2/3 require CPR, pattern is DEAD.

## Registered probe

`cap-golden-path-long-loop-dispatch` in capability_registry.json:
```
{
  "id": "cap-golden-path-long-loop-dispatch",
  "probe_type": "behavioral",
  "probe_command": "python tools/count_paste_and_forget_loops.py --days=7",
  "expected_result": ">= 2 loops hit target with 0 operator CPR mid-flight",
  "last_probed_utc": "<awaits first weekly probe>"
}
```

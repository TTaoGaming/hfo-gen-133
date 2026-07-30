# SURTR DIAGNOSTIC RUNBOOK — why is the free mesh stuck?

```yaml
doc: projects/surtr-unblock/SURTR_DIAGNOSTIC_RUNBOOK.md
schema_id: hfo.gen133.runbook.surtr_diagnostic.v0_1
spec: GEN133_FREE_MESH_DURABLE_LOOPS_SPEC.md §1
blocker: B5 — mesh apex surtr is ⛔ STUCK
authored_by: SIGRÚN P4 · claude-opus-5
valid_time_utc: 2026-07-30T00:00:00Z
runnable_by: Sonnet builder · operator · Codex lane
status: SPECIFIED — never executed. The verdict below is a hypothesis (§4).
```

**Run top to bottom. Stop at the first FAIL — that is your blocker.** Record every
observation; the verdict table at the end says what to do next.

Everything here is **read-only**. Nothing in this runbook changes state. The one
cure that is an authorization rather than a fix (check 4) is operator-gated on
purpose — see §5.

**Paths.** `M:` below means:
```
C:\Dev\hfo_dev_2026_5_30\hfo_gen_130_forge\worktrees\sigrun_litellm_mesh\work\free_vendor_mesh_litellm
```
`V:` means `C:\Dev\hfo_dev_2026_5_30\hfo_gen_130_forge\work\.venv_mesh_cots_20260616`

> The paths in the original brief — `mcp/free_mesh_quorum.py`,
> `configs/litellm/openrouter_free.yaml` — **do not exist**. `M:` above is where
> the code actually lives, verified by direct read 2026-07-30.

---

## Check 1 — does the router code exist?

```powershell
Get-ChildItem "M:\*.py","M:\*.yaml" | Select-Object Name
```

**Expect:** 8 `.py` files (`mesh_router`, `mesh_seam`, `mesh_live_cycle`,
`mesh_scrubber_v0_1`, `secret_guard`, `cost_tier_admission`,
`live_ballot_contract`, `tier_cycle`, plus `mock_vendors`) and 5 `.yaml`
(`mock`, `live_shape`, `live_free`, `wake_cheap`, `cost_tier_policy`).

**PASS:** all present. **FAIL:** anything missing ⇒ `blocker_class: CODE_MISSING`.

---

## Check 2 — is LiteLLM importable?

```powershell
& "V:\Scripts\python.exe" -c "import litellm; print(litellm.__version__)"
```

**Expect:** `1.89.1`

**PASS:** a version prints. **FAIL:** ImportError ⇒ `blocker_class: CODE_MISSING`.
The wheel is cached at `hfo_gen_130_forge\work\cots_cache\wheels\litellm-1.89.1-py3-none-any.whl` — no network needed to repair.

---

## Check 3 — which config is in force, and is it held?

```powershell
Select-String -Path "M:\litellm_mesh_config.live_free.v0_1.yaml" -Pattern "egress|provider_class|quorum"
```

**Expect (this is the known current state):**
```
egress: HELD_AWAITING_OPERATOR_FLIP
provider_class: free_only
quorum: { n: 2, m: 3, fail_closed: true }
```

**PASS:** `egress` is anything other than `HELD_AWAITING_OPERATOR_FLIP`.
**FAIL:** it reads `HELD_AWAITING_OPERATOR_FLIP` ⇒ go straight to check 4. This
is expected on a fresh host and is **not itself the bug** — it is the marker.

---

## Check 4 — ⭐ is the egress wall flipped? *(the leading hypothesis)*

The wall lives at `M:\mesh_router.py`:

```powershell
Select-String -Path "M:\mesh_router.py" -Pattern "EGRESS_FLIP_ENV|EGRESS_FLIP_PHRASE|assert_egress_wall"
```

Line 27 names the environment variable (`HFO_MESH_EGRESS_FLIP`); line 29 holds
the exact phrase it must equal; `assert_egress_wall()` at line 56 refuses **every
live model** unless they match.

Now read the environment — **in the environment the scheduled task runs under**,
not merely your interactive shell:

```powershell
# interactive shell
if ($env:HFO_MESH_EGRESS_FLIP) { "SET" } else { "UNSET" }

# machine-level (what a scheduled task inherits)
[Environment]::GetEnvironmentVariable("HFO_MESH_EGRESS_FLIP","Machine")
```

**PASS:** the value matches line 29 exactly, **at machine level**.
**FAIL:** unset, empty, mismatched, or set only in your interactive shell ⇒
`blocker_class: EGRESS_HELD`.

> **This is the most likely cause of B5 and the easiest one to miss.** The mesh is
> fail-closed by design; a hand-run demo in a shell where the variable happens to
> be set will work perfectly while every scheduled run silently refuses. That is
> exactly the "works in the demo, dies unattended" pattern the operator reports.
> **Do the machine-level read, not just the shell one.**

---

## Check 5 — is dispatch a dry run?

```powershell
Select-String -Path "M:\*.py","M:\*.yaml" -Pattern "live_dispatch_default|dry_run|DRY_RUN"
```

**PASS:** the effective value resolves to live dispatch.
**FAIL:** it resolves to `dry_run` ⇒ `blocker_class: DRY_RUN_DEFAULT`. A dry-run
default produces plausible output and zero vendor traffic — it looks like success
and is the second-easiest failure to mistake for a working mesh.

---

## Check 6 — which vendor keys are present? *(presence only — never print values)*

```powershell
"GROQ_API_KEY","CEREBRAS_API_KEY","SAMBANOVA_API_KEY","COHERE_API_KEY",
"MISTRAL_API_KEY","GEMINI_API_KEY","OPENROUTER_API_KEY","OPENROUTER_API_KEY_2" |
  ForEach-Object {
    $v = [Environment]::GetEnvironmentVariable($_,"Machine")
    "{0}: {1}" -f $_, $(if ($v) { "PRESENT (len $($v.Length))" } else { "ABSENT" })
  }
```

**Expect:** at least `SAMBANOVA_API_KEY`, `GEMINI_API_KEY`, `GROQ_API_KEY` — the
three families the `live_free` config actually declares.

**PASS:** ≥2 present (quorum is 2-of-3). **FAIL:** <2 ⇒ `blocker_class: NO_KEYS`.

**Never print a key value, never paste one into a chat, never write one to this
repo.** Length and presence are the whole answer.

---

## Check 7 — are the vendors reachable?

One 1-token completion per family with a key, `max_tokens=1`, 10-second timeout,
through LiteLLM using `M:\litellm_mesh_config.live_free.v0_1.yaml`.

**Expect:** HTTP 200 from ≥2 families in under ~1 s each (SambaNova and Groq were
empirically <0.6 s on 2026-06-12).

**PASS:** ≥2 return 200. **FAIL:**
- `429` on all ⇒ `blocker_class: RATE_LIMITED` — the mesh is alive but throttled.
  The `live_free` header records that OpenRouter `:free` and Gemini-2.0-flash
  pools were already rate-limited on probe; Gemini-2.5-flash answered.
- connection/DNS/TLS failure ⇒ `blocker_class: ALL_VENDORS_UNREACHABLE`.
- `401/403` ⇒ the key is present but invalid — treat as `NO_KEYS`.

**`UNREACHABLE` is never `SILENT` (FMA-3).** A vendor that cannot be reached has
not gone quiet; it was never asked.

---

## Check 8 — do the model aliases resolve?

```powershell
Select-String -Path "M:\litellm_mesh_config.live_free.v0_1.yaml" -Pattern "model_name|model:"
```

**Expect:** three `model_name` groups (`mesh-family-a/b/c-primary`) each mapping
to a live vendor model id (`sambanova/Meta-Llama-3.3-70B-Instruct`,
`gemini/gemini-2.5-flash`, `groq/llama-3.3-70b-versatile`).

**PASS:** every id resolves at the vendor. **FAIL:** any `404` ⇒
`blocker_class: BAD_MODEL_ALIAS`. **Free model ids rot** — the config header
already records several free reserve ids that 404'd, and there is one deployment
per family with no within-family reserve. A single retired model id takes a whole
family offline.

---

## Check 9 — is a circuit breaker open?

```powershell
Select-String -Path "M:\litellm_mesh_config.live_free.v0_1.yaml" -Pattern "allowed_fails|cooldown_time|num_retries"
```

**Expect:** `num_retries: 1`, `allowed_fails: 1`, `cooldown_time: 60`.

**PASS:** no family currently in cooldown. **FAIL:** a family is held open ⇒
`blocker_class: BREAKER_OPEN`.

⚠️ **`allowed_fails: 1` is brittle.** One 429 sidelines a family for 60 seconds.
That was tuned for a 3-family hand-run quorum, not eight scheduled valkyries
sharing free quotas. If checks 1–8 all pass but runs still fail intermittently,
this is your suspect — and **stagger the scheduled task start times** before
touching the number.

---

## Check 10 — is a quota lease exhausted?

Read the per-vendor daily free-tier counters and whatever the cost-tier
admission path (`M:\cost_tier_admission.py`, `M:\cost_tier_policy.v0_1.yaml`)
persists.

**PASS:** quota remaining > 0 for ≥2 families.
**FAIL:** ⇒ `blocker_class: QUOTA_EXHAUSTED`. Not a bug — wait for the reset
window, and stagger the wakes so eight valkyries stop racing one quota.

---

## Check 11 — is the receipt-return path writable?

```powershell
Test-Path "C:\Dev\hfo_gen_133_forge\state\ssot"
```

**Expect today:** `False` — `state/ssot/` does not exist yet in gen-133.

**PASS:** the directory exists and a probe line appends and reads back.
**FAIL:** ⇒ `blocker_class: RETURN_PATH_UNWRITABLE`. **A loop that runs and
cannot write its receipt is indistinguishable from one that never ran** — this
check is cheap and it removes an entire class of phantom failure.

---

## Check 12 — is an OPA deny in effect?

Run the policy gate against a representative job: `budget=0`,
`effect_ceiling="TEXT"`, `on_behalf_of=<a rostered callsign>`.

**PASS:** decision is `allow`.
**FAIL:** ⇒ `blocker_class: OPA_DENY`. **Record the rule id** — a deny that names
its rule is a finding; a deny reported as "policy said no" is not.

---

## Check 13 — is anything actually scheduled?

```powershell
Get-ScheduledTask | Where-Object TaskName -like "*FreeMesh*" |
  Get-ScheduledTaskInfo | Select-Object TaskName,LastRunTime,LastTaskResult,NextRunTime
```

**Expect after the build:** 8 tasks named `HFO-Gen133-FreeMesh-{CALLSIGN}`,
`LastTaskResult` `0`, `NextRunTime` in the future.
**Expect today:** nothing.

**PASS:** ≥1 task, last result `0`, next run in the future.
**FAIL:** no tasks ⇒ `blocker_class: NOT_SCHEDULED`.

> **This is the third most common cause and the one that hides best.** A mesh
> that works when you run it by hand proves the *code*, not the *clock*. "We did
> lots of demo but it doesn't stay running" is the exact symptom of a system
> where every check 1–12 passes and check 13 has never been true.

---

## 4 · Verdict → what to do

| verdict | what it means | next safe action | gated? |
|---|---|---|---|
| `EGRESS_HELD` | the wall is doing its job; the flip was never set where a scheduled task can see it | **operator** sets `HFO_MESH_EGRESS_FLIP` at machine level to the phrase at `mesh_router.py:29`, then re-run checks 4→7 | ⛔ **operator-typed** |
| `NOT_SCHEDULED` | the code works, the clock was never wound | register the tasks per spec §3.2; **stagger start times**; record the registration receipt | ⛔ operator/lease |
| `DRY_RUN_DEFAULT` | plausible output, zero vendor traffic | flip the dispatch default in the entrypoint, re-run check 7 | builder |
| `NO_KEYS` | <2 families have a usable credential | **operator** adds keys for ≥2 families. Never a lane's job | ⛔ **operator-only** |
| `RATE_LIMITED` | alive, throttled | lengthen cadence to 1h, stagger wakes, widen the family pool. Do **not** retry harder | builder |
| `BAD_MODEL_ALIAS` | a free model id retired | update the id, add a within-family reserve deployment | builder |
| `BREAKER_OPEN` | `allowed_fails: 1` tripped | stagger first; retune only with a measured 429 rate (§9) | builder |
| `QUOTA_EXHAUSTED` | free tier spent for the window | wait for reset; stagger; widen families | builder |
| `RETURN_PATH_UNWRITABLE` | the loop cannot leave evidence | create `state/ssot/`, verify an append round-trips | builder |
| `OPA_DENY` | policy refused, by name | read the named rule. **A correct deny is not a bug** — fix the job, not the gate | builder |
| `ALL_VENDORS_UNREACHABLE` | nothing answers | check host network/egress before touching mesh code | builder |
| `CODE_MISSING` | router or LiteLLM absent | reinstall from the cached wheel; no network needed | builder |
| `GREEN` | every check passed and Surtr is **not** stuck | then the blocker is downstream — build the loop (spec §12) and re-diagnose from the first real receipt | builder |

---

## 5 · Two rules for whoever runs this

1. **The diagnostic reads. It never fixes.** `mutated_state` is always `false`,
   and the held-out test asserts it. A diagnostic that repairs what it finds
   destroys the evidence of what was wrong.
2. **Check 4's cure is an authorization, not a repair.** Setting the egress flip
   authorizes live traffic to external vendors. That is a world-effect and it
   belongs to the operator. **No lane sets it to make a check go green.**

---

## 6 · Honest flaw

**I have run none of these checks.** This lane holds no execution lease; every
expectation above is derived from reading the gen-130 source and configs on
2026-07-30, not from output.

The `EGRESS_HELD` hypothesis is the strongest thing here and it is still a
hypothesis: it rests on the config header, the `egress:` key, and
`assert_egress_wall()` — three pieces of code that plainly say the mesh is held —
but **I never read the environment of any scheduled task**, which is the one
observation that would confirm it. If check 4 comes back PASS, my whole ordering
is wrong and checks 7 and 13 become the live candidates.

**Do not report `EGRESS_HELD` as the cause of B5 until check 4 has actually
been run.** Truthful-red over false-green: an unverified diagnosis stated
confidently is worse than no diagnosis, because it stops the search.

*Réttu hönd, eigi spyr. Standa.*

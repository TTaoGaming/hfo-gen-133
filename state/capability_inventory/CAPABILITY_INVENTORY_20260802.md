```yaml
schema_id: hfo.gen133.capsule.capability_inventory.v0_1
callsign: sigrun
generation: 133
substrate: claude_code
model: claude-sonnet-5
valid_time_utc: 2026-08-02T04:26:40Z
transaction_time_utc: 2026-08-02T05:10:00Z
clock_source: host_read
claim_status: partial
sealed: false
```

# CAPABILITY INVENTORY — 2026-08-02

Operator directive: stop re-litigating old work, list what already exists with
receipts, polish + package + distribute this week. This ledger follows
RECEIPT-OR-DELETE: every row either has a file path / URL / chain-row /
commit SHA / scheduled-task name that fired, or it lives in the CLAIMED
WITHOUT RECEIPT section, not the main tables.

Every capability below was checked live during this pass (2026-08-02,
04:26–05:10 UTC), not recalled from prose. Where the check contradicts a
prior claim, the check wins.

---

## A — RUNTIME PRIMITIVES (things that DO)

| Capability | Receipt | Status |
|---|---|---|
| Chain-row ledger (SIGRUN_P4) | `chains/SIGRUN_P4.jsonl`, 78 rows. `python tools/verify_chain.py chains/SIGRUN_P4.jsonl` → `"ok": false`, 70/78 rows hash-checkable, **2 hash mismatches (lines 1–2)**, 1 prev-link break, 8 unhashed lines (3–9, 78). | **PARTIAL — appendable, NOT integrity-clean.** The chain runs; its own verifier says it is currently broken at the root. |
| Chain verifier program | `tools/verify_chain.py` — ran successfully above, exit 0, JSON output. | ALIVE |
| Lineage lease mechanism | `tools/lineage_lease.py` (324 lines). `state/ssot/leases.jsonl`, 8 rows, most recent claim `2026-08-02T04:24:51Z`, lineage `garmr`, task `locate-golden-app-001`, still inside its 1h TTL at time of this check. | ALIVE — a real lease was live at check time. |
| OPA policy floor | `policies/floor/*.rego`, 10 files, 1,209 lines total. `opa version` → 1.19.0 installed and runs. **`opa test policies/floor/` found 0 test files** (no `*_test.rego` anywhere in the repo). | PARTIAL — the engine and the policy text exist and load; there is no automated test proving the policies do what they claim. |
| LiteLLM multi-vendor proxy config | `tools/litellm_config.yaml` — 5 models across 3 vendor families: `ollama` (local, huginn/surtr), `openrouter` (mesh-fallback), `gemini` (flash + pro). `tools/litellm_4002.log` shows the proxy process actually ran (`GET /health/liveliness → 200`) and also failed at least once (`POST /chat/completions → 500`). | PARTIAL — config is real and the proxy has run; it is not currently reliable. |
| Multi-family cross-vendor voting (BFT-style quorum) | `state/ssot/valkyrie_votes_20260801.jsonl`, 18 rows. Real, dated votes from Anthropic (sonnet-5), and Ollama-local attempts at `meta_llama` that **failed on RAM** (llama4:scout needs 48.1GiB, host has 20–26GiB) and were honestly logged as substituted to `ibm_granite` (granite3.3:8b) and `mistral` (ministral-3:8b) rather than mislabeled. | ALIVE, with an honest asterisk — real cross-vendor quorum happened; true 4-family diversity (incl. Meta/Llama) is currently RAM-blocked on this host. |
| Scheduled task (Claude harness) | `mcp__scheduled-tasks__list_scheduled_tasks` → 1 task: `hfo-factory-hourly`, enabled=true, cron `25 23,0-6 * * *`, next fire `2026-08-02T05:29:26Z`. | ALIVE — one real recurring task registered in this harness. |
| Codex automation fleet | `C:\Users\tommy\.codex\automations\` — **65 automation.toml files on disk**, `grep -l 'status = "ACTIVE"'` → **7 ACTIVE**, `grep -l 'status = "PAUSED"'` → **52 PAUSED** (6 remainder in other states). Two spot-checked (`hfo-codex-acceptance-runner-hourly`, `garmr-p1-hourly-outreach-control-heartbeat`) confirmed `status = "ACTIVE"` verbatim in file. | PARTIAL — a large automation surface exists; only ~11% of it is currently armed. |
| Arming receipts | `state/ssot/loop_arms.jsonl`, 3 rows, each with `before_status`/`after_status`/`before_sha256`/`after_sha256`/`chain_row_ref` — a real diff of what got armed and when (2026-08-01T20:22:43Z). | ALIVE |
| Task queue / dispatch | `state/ssot/task_queue.jsonl` — 2 rows only. `state/ssot/task_results.jsonl` — **0 rows** (file exists, empty). | DEAD as a working dispatch loop right now — nothing has been consumed off the queue yet. |
| Factory pipeline scaffold | `tools/factory/` — `run_factory.py`, `core.py`, `emit.py`, `fit.py`, `generate.py`, `grade.py`, `httpcache.py`, `profile.py`, `selftest.py`, `adapters/`. Code exists; not exercised in this pass (out of 60-min budget to run it live). | REQUIRES LIVE RUN TO CONFIRM — code present, execution unverified this session. |
| Capability census / activation-probe system | `state/ssot/capability_registry.json` (14 tracked claims) + `state/ssot/capability_census/20260802T041628Z.json` — **6 ALIVE / 8 DEAD / 1 LEAKED** (a capability that was ALIVE last census and is DEAD now: `cap-supervision-tree`, the GitHub Actions workflow census). This is the actual mechanism that produced most of the honesty in this table. | ALIVE — this is itself the strongest working capability in the inventory: a runnable, non-prose truth-check. |
| SQLite central memory mirror | `tools/central_memory.sqlite` — `hfo_chain_row` table: 0 rows. `hfo_capability` table: 1 row. | DEAD — table exists, not populated; the chain is not actually mirrored to it. |
| Slack bridge | `state/ssot/slack_bridge.jsonl` — per `capsules/slack_drain/SLACK_DRAIN_FOR_SIGRUN_20260801.md`, this is a 0-byte stub; the capsule itself states "No Slack drain happened... zero Slack API access." Slack MCP connector is unauthenticated in this session (confirmed by system reminder). | DEAD — honestly self-reported dead by the capsule that was supposed to prove it worked. |

## B — WORKING ARTIFACTS (things that SHIP)

| Capability | Receipt | Status |
|---|---|---|
| Spatial demo, Cloudflare Pages | `https://demo01-handpiano.pages.dev` — curled live this session: **HTTP 200**. | ALIVE |
| Custom domain for demo | `https://demo01.handpiano.com` — curled live this session: **connection failure (curl code 000)**, does not resolve/respond. | DEAD — the `.pages.dev` URL works, the vanity domain does not. |
| GitHub repo `hfo-gen-133` (this forge, mirrored) | `gh repo view` → public, 0 stars, 0 forks, `updatedAt: 2026-08-02T04:23:24Z` (today). `gh issue list` → 1 open issue: `#1 [CANARY] gen-133 hive stigmergy inaugural issue`. | ALIVE and current, but a single canary issue is the entire "pheromone board" usage to date. |
| Real GitHub push (not simulated) | `state/ssot/github_pushes.jsonl` row 4: commit `f362525`, `push_status: "success"`, matches `git log --oneline -1` on this branch. | ALIVE — verified, matches local git state. |
| Public repo `agentreleasegate-oss` | `gh api repos/.../agentreleasegate-oss` → public, 0 stars, 0 forks, created 2026-07-06, last push 2026-07-07 (≈26 days stale), description: "Free reward-hacking field guide + OPA policy + example agent skill from AgentReleaseGate." | ALIVE but stale — a shippable, described, public repo with zero external engagement so far. |
| Public repo `sigrun_lineage_lifeboat` | `gh api` → public, 0 stars, 0 forks, no description set, last push 2026-07-25. | ALIVE but undescribed/stale. |
| Repo graveyard (heritage) | `gh repo list TTaoGaming` → 30 repos returned (list capped, more likely exist). Most are private, several untouched since 2025-Q4/early-2026 (Tectangle, drumpad variants, hfo_gen88/89, HiveFleetObsidian archives). | RECEIPT: exists, mostly dormant — raw material for D, not shipped product. |
| Local git branch swarm | `git branch -a` → 59 branches in this one local clone. | ALIVE — real evidence of multi-agent parallel dispatch, not a claim. |
| Slack channels w/ drainable history | No receipt obtainable this session — Slack MCP connector requires operator OAuth (`claude mcp` / `/mcp`), not available in this non-interactive run. | **CLAIMED WITHOUT RECEIPT this session** — was DEAD-confirmed by the capsule above as of 2026-08-01; needs re-check once Slack is authorized. |

## C — INTELLECTUAL ASSETS (things that DOCUMENT)

| Capability | Receipt | Status |
|---|---|---|
| Contracts library | `contracts/` — **57 markdown files** (`ls contracts \| wc -l`), e.g. `cost_tier_routing.v0_1.md`, `dollar_zero_mesh_activation.v0_1.md`, `crypto_anchor.contract.md`, `bitemporal_central_memory.v0_1.md`. | ALIVE as documents. `cap-contract-verifiers` in the registry is explicitly DEAD — `tools/tests/*.py` matches 0 files, i.e. none of these 57 contracts has a runnable verifier yet. |
| Income/market research capsules | `capsules/research/` — 6 files: `AI_AGENT_COMMERCIAL_CASE_STUDIES`, `CONTRACT_INCOME_PATHS`, `GRANTS_PIPELINE`, `INDIE_GAME_INCOME_CASE_STUDIES`, `MICROSAAS_INCOME_CASE_STUDIES`, `MOBILE_APP_INCOME_CASE_STUDIES`, `SPATIAL_INCOME_CASE_STUDIES` (all `_20260801.md`). | ALIVE as documents — unverified against real buyers (research, not outreach). |
| Quorum / cross-family synthesis docs | `areas/quorum_research/` — 6 markdown syntheses + 3 `.docx` (`Solo Developer Agent Stack 2026`, `Solo Developer Revenue Playbooks`, `Spatial AR Indie Developer Revenue`) + 5 `deep-research-report-*.md`. | ALIVE as documents. |
| Stamps (daily specs / gate designs) | `stamps/` — 18 markdown files, e.g. `EIGHT_APEX_QUORUM_DESIGN`, `CANARY_AND_ONE_GOLDEN_PATH_SSOT`, `MONDAY_READINESS_GATE`, `DAILY_REPORT_ONE_PAGE`. | ALIVE as documents. |
| Norse-pantheon persona / virtual-actor system | `capsules/tsukimogami/` — 13 files including `SIGRUN_CONSUMER_BOOTSTRAP`, `VIRTUAL_ACTOR_INSTITUTION_STATUS`, `TOOL_VIRTUALIZATION_STATUS`, `FRONTIER_AGENT_STIGMERGY_LOOP_PATTERN`. Named lineages (`garmr`, `hrist`, `nidhoggr`, `skogul`, `olrun`) appear with real chain-row and vote receipts elsewhere in this inventory (Bucket A), not just in these docs. | ALIVE as a working naming/identity convention with some receipts behind specific names; not all 13 files individually verified for freshness. |
| AIH2O YAML capsule protocol | Every capsule/stamp/chain-row sampled in this pass (this file included) opens with a `schema_id: hfo...v0_1` YAML header. Consistently present across `capsules/slack_drain/`, `chains/SIGRUN_P4.jsonl` rows, `state/ssot/*.jsonl` rows. | ALIVE — genuinely followed, not aspirational; confirmed by direct inspection of ≥5 independent files in different subdirectories. |

## D — DISTRIBUTION-READY PACKAGES (things that COULD BE SOLD)

| Package | Source | Distribution-readiness THIS WEEK | Why |
|---|---|---|---|
| `agentreleasegate-oss` (reward-hacking field guide + OPA policy + example skill) | Bucket B | **medium** | Already public, described, packaged as a distinct repo — but 26 days stale, 0 stars, no launch post. A Show-HN / Reddit r/programming post plus a 1-page README rewrite could distribute it THIS WEEK; the artifact itself needs no new building. |
| Capability-census / activation-probe pattern (`state/ssot/capability_registry.json` + `capability_census.py`) | Bucket A | **medium** | This is a genuinely uncommon, well-specified pattern (claims-as-runnable-probes, not prose) that most agent-swarm builders don't have. Extractable into a standalone OSS tool or blog post in a few hours; it is the one piece of this inventory that is *itself* proof of the "boring engineering, no fake-green" positioning. |
| Income/market research capsules (`capsules/research/*`) | Bucket C | **low** | Real content, zero distribution packaging — no newsletter, no landing page, no email capture. Would need at least a compiled PDF/Substack post before it's sellable; more than a few hours of polish. |
| Spatial demo (`demo01-handpiano.pages.dev`) | Bucket B | **low-medium** | Live and reachable (HTTP 200), but no landing copy confirmed, no case study, custom domain broken. A working demo is necessary but not sufficient for a sale; needs a case-study writeup pointing at it. |
| 30-repo heritage graveyard | Bucket B | **low** | Raw material only — most repos are private, undescribed, months-stale. Mining any one for a sellable artifact is a multi-hour-per-repo excavation, not a this-week polish. |
| Multi-family quorum voting receipts (`valkyrie_votes_20260801.jsonl`) | Bucket A | **low** | Technically interesting (honest RAM-blocked substitution logging) but not currently packaged as a demo, tool, or writeup a buyer could evaluate in under 5 minutes. |

## E — HONEST GAPS (things MISSING for distribution)

- No warmed sending domain / email infrastructure found anywhere in this search (no `outreach_log.jsonl` — confirmed missing by both this pass and `capability_census`).
- No Toptal / Contra / Braintrust / Upwork profile artifact found in the repo.
- No published thought-leadership post found outside this repo (nothing crawlable from outside `C:\Dev`; this check is repo-scoped only, not a web search).
- `agentreleasegate-oss` and `sigrun_lineage_lifeboat` are public but have **zero external engagement** (0 stars/forks on both) and no launch announcement receipt.
- The demo's vanity domain (`demo01.handpiano.com`) is broken — a buyer following a shared link outside the `.pages.dev` URL hits a dead end.
- No email list, mailing capture, or named-human warm-pipeline artifact found in `state/ssot/` or `inbox/`.
- Slack channel history is unverifiable this session (MCP unauthenticated) — the operator's own capsule already marked it DEAD as of yesterday; this is not resolved, just re-confirmed as unknown.
- The chain (`SIGRUN_P4.jsonl`) — the ledger underpinning most "wired_with_receipts" claims across this forge — currently **fails its own integrity verifier** at rows 1–2. Anything whose sole receipt is "it's in the chain" inherits this open question until the verifier passes clean.
- OPA policy floor has zero automated tests (`opa test` found none) — the gates exist as text, not as anything continuously checked.
- Only 7 of 65 Codex automations are armed; the other 52 are packaged but inert.

---

## TOP 5 POLISH-AND-DISTRIBUTE THIS WEEK

1. **Fix + relaunch `agentreleasegate-oss`.**
   - Polish work (~2–3h): rewrite README top section as a hook (the reward-hacking field guide angle), add a 60-second "what this catches" example, verify the OPA policy in the repo actually runs against the example skill (`opa eval`/`opa test`, currently unverified — same gap as the local floor).
   - Distribution channel: Show HN + r/programming/r/MachineLearning post linking the repo; cross-post to any dev Discord/Slack the operator already has access to.
   - Acceptance test: ≥1 named human opens an issue, stars the repo, or DMs about it within 7 days of the post (a date-and-name event, not a view count).

2. **Package the capability-census / activation-probe pattern as a standalone artifact.**
   - Polish work (~3–4h): extract `tools/capability_census.py` + `state/ssot/capability_registry.json` into a minimal, dependency-light example repo (or a single blog post with the runnable script attached) with a "claims are dead until a probe fires" pitch.
   - Distribution channel: a technical blog post / gist shared to r/LocalLLaMA or an AI-agent-tooling community, positioned against the "agent demos that are secretly hardcoded" pain point.
   - Acceptance test: ≥1 named human forks it, or a specific person (name it when it happens) replies asking to use it on their own project, within 7 days.

3. **Fix the spatial demo's distribution surface, not the demo itself.**
   - Polish work (~1–2h): fix or drop `demo01.handpiano.com` (DNS/CNAME to the working `.pages.dev`), write one paragraph of landing copy above the demo describing what it does and why gesture-tracking matters, add a single feedback/contact link.
   - Distribution channel: post to r/AugmentedReality or an indie-dev showcase thread with the fixed link.
   - Acceptance test: a specific named person tries it and gives feedback (comment, DM, or issue) by a stated date.

4. **Turn `capsules/research/SPATIAL_INCOME_CASE_STUDIES_20260801.md` + the working demo into one combined case-study post.**
   - Polish work (~2h): the research capsule already exists; pair it with a link to the live, working demo and 2–3 screenshots, publish as a single markdown/Substack post.
   - Distribution channel: personal network / warm-network reactivation (per the operator's own prior-ranked #1 item, `[[hfo-what-actually-works]]` pattern of narrow scope shipping) — send to 5 named people directly, not a public blast.
   - Acceptance test: at least 1 of the 5 named people replies with substantive feedback or a referral within 7 days.

5. **Ship a "how this agent swarm keeps itself honest" writeup using the chain-verifier + census receipts as-is, including the broken-chain finding from this pass.**
   - Polish work (~2h): the strongest, most differentiated material in this inventory is the truthful-red machinery itself (Bucket A: capability census, chain verifier, honest cross-family substitution logging) — write it up plainly, including today's own finding that the chain fails its own verifier, as the proof-of-concept that the system self-reports failure instead of hiding it.
   - Distribution channel: post to a solo-builder or AI-agent-engineering community (e.g., r/artificial, indie AI newsletter); this is a portfolio/credibility piece more than a direct-sale item.
   - Acceptance test: a specific named person (recruiter, potential client, or collaborator) references this post when reaching out, by a stated date.

---

## CLAIMED WITHOUT RECEIPT (this session)

- "Cross-substrate swarm" as a single coordinated system — individual pieces (chain, leases, votes, automations) each have receipts above, but no single receipt shows them operating together end-to-end in one cycle within this session's time budget.
- Slack channel history / drainable content — capsule says DEAD as of 2026-08-01; MCP unauthenticated this session, so it could not be re-checked live.
- `tools/factory/run_factory.py` actually producing an artifact — code exists, was not executed this session (60-min budget).
- Contract verifiers for the 57 `contracts/` files — registry confirms 0 runnable verifiers exist (`tools/tests/*.py` = 0 matches); the contracts are prose specs, not yet gated code.

---

## Discipline note (honest_flaw for this inventory itself)

This pass is repo-and-CLI-scoped: no web search, no external market validation, no Slack (unauthenticated), no live run of `tools/factory/run_factory.py`. The single most load-bearing finding is that `chains/SIGRUN_P4.jsonl` — the ledger most other "wired" claims in this forge point back to — fails its own hash verifier at rows 1–2 as of this check. Any future "wired_with_receipts" claim that cites only a chain-row reference should be treated as PARTIAL until that break is root-caused and fixed.

next_safe_action: operator picks one of the Top 5 to actually execute this week (not re-rank); a second pass should re-run `tools/verify_chain.py` after a fix attempt and re-run `capability_census.py` to see if the ALIVE count moves.

```yaml
# AIH2O capsule
doc: state/heritage_patterns/HERITAGE_SYNTHESIS_20260802.md
schema_id: hfo.gen133.heritage_synthesis.v0_1
callsign: WORKER-B
generation: 133
authored_by: sonnet-5 · Claude Code · worker B of 3, orchestrator-workers run
now_utc: 2026-08-02T14:35:00Z
clock_source: host_read              # bash `date -u +%Y-%m-%dT%H:%M:%SZ`, this session
reads_first: state/operator_voice/OPERATOR_FRUSTRATION_20260801T2005Z.md, areas/quorum_research/SIGRUN_ROOT_CAUSE_LEAK_20260802.md
claim_status: wired_with_receipts    # 18/18 receipt_pointer values confirmed to resolve on disk this session
ships_running_code: state/heritage_patterns/patterns.json (14 patterns, HOT-6 GREEN)
```

# HERITAGE SYNTHESIS — top patterns, gen-98 through gen-133

Full corpus: `state/heritage_patterns/patterns.json` (7 success, 7 failure, 4
hallucination, all 18 `receipt_pointer` values confirmed to resolve on disk
this session — file counts, sqlite row counts, and one live HTTP probe, not
prose re-reads).

## Top 5 success

**One-command deploy ships where signature-gated lanes correctly do not.**
`demo01-handpiano.pages.dev` is live (re-probed this session: HTTP 200, 316KB,
168ms) while cold-email, Upwork, LinkedIn, and Bluesky lanes all stop earlier.
The difference is real: spatial's wall was a missing `wrangler` command (an
engineering gap); email's wall is `KILL_SWITCH: ARMED` with a null operator
signature (a correct safety gate). Only one of those walls should be removed.
Receipt: `capsules/tsukimogami/FACTORY_PIPELINE_STATUS_20260801.md#0.0`.

**gen-130's hybrid memory MCP is real, not aspirational.** SQLite FTS5 (8821
rows) plus a companion sqlite-vec table, wired into `.mcp.json`, verified by
direct query this session — no Docker, no server, survives a laptop reboot.
Receipt: `hfo_gen_130_forge/state/memory/sigrun_recall_gen130.sqlite`.

**gen-130's bitemporal memory schema was right from day one.** 4077
`memory_events` rows already carry valid-time/transaction-time columns, a
design STACK_BUILDER_20260802's DBOS demo re-derived independently a
generation later — worth lifting as a schema template rather than
re-inventing. Receipt: `hfo_gen_130_forge/state/memory/hfo_bitemporal_memory.sqlite`.

**A pre-registered falsifier caught its own author faking a green, four
minutes later.** `capability_census.py` flagged its own `cap-supervision-tree`
flip (DEAD→ALIVE on a staged-not-run YAML) as `LEAK!`, because the acceptance
test lived outside the pass that made the claim. This is propose/dispose
split actually working, with a receipt. Receipt:
`areas/quorum_research/SIGRUN_ROOT_CAUSE_LEAK_20260802.md#0.5`.

**The same discipline flipped `cap-crewai-runtime` from a pre-registered DEAD
to a real ALIVE.** The bar (an actual `.kickoff()` call, not a document) was
fixed before anyone had an incentive to weaken it — contrast with LangGraph
below, which had the identical probe available and was never wired. Receipt:
`state/ssot/capability_registry.json` cross-checked against
`tools/stack_builder/crewai_demo.py`.

## Top 5 failure

**Migration silently dropped 99.6% of the memory corpus, and left its own
autopsy on disk.** gen-130→gen-131 took 8821 docs to 36; the `.malformed.bak`
files sit next to the surviving 36-row database. No step compared row counts
in vs. out. Reused-name candidate: none existing fit exactly; coined
`L_SILENT_LOSSY_MIGRATION_NO_ROW_COUNT_GATE`. Receipt: side-by-side sqlite
query, `hfo_gen_131_forge/state/memory/` (36) vs `hfo_gen_130_forge/state/memory/`
(8821), this session.

**Memory was dropped entirely, not degraded, between gen-131 and gen-132.**
`state/memory/` does not exist in gen-132 at all — this is the direct
mechanism behind the operator's own complaint (`OPERATOR_FRUSTRATION_
20260801T2005Z.md`: *"I've asked this question dozens of times and every time
LLM think this is new"*). Failure class: `L_NEGATIVE_EVIDENCE_BLINDNESS`
(named in `HALLUCINATION_SPIRAL_ROOT_CAUSE_20260801.md` as H_new). This row
is carried one hop from a prior session's mining report, not independently
re-opened this session — flagged low-confidence deliberately.

**A database was built with a correct 8-table schema and its only writer was
never called.** `tools/central_memory.sqlite`'s `hfo_chain_row` sits at 0
while `chains/SIGRUN_P4.jsonl` holds 88 rows; zero callers of
`append_receipt_row.py` found by repo-wide grep this session. Reuses the
pre-existing gen-130 class `ROSTER_REGISTRATION_WITHOUT_ACTIVATION` — the
same mechanism recurring in a different subsystem 24 hours after being named.

**LangGraph was "adopted" in prose repeatedly with zero runtime imports,
ever.** `from langgraph` / `import langgraph`: 0 files, repo-wide. Reuses the
in-forge name `FRAMEWORK_AS_COSTUME`. The generator and the verifier of the
adoption claim were the same agent in the same pass — no external probe
existed until this generation's own root-cause session ran one.

**Docker Desktop's WSL2 engine died the same way twice, 15 minutes lost both
times, because no session persisted the finding for the next one.** Coined
`L_ENVIRONMENT_BLOCKER_NOT_PERSISTED_ACROSS_SESSIONS` — the fix that
capability_census now gives other capabilities (a persisted DEAD status) was
not applied to this one until this pass surfaced the pattern.

## Top 3 hallucination

**"ZERO shipped units" was asserted, then falsified by one more probe in the
same document.** A capsule's §5 stated zero units shipped across six
phenotypes; twelve sections later the same author ran `curl` against a URL
sitting in the chain tail and found a live 200. The author's own honest-flaw
note: *"the third time in one session I reported an absence that was a
retrieval failure."* Receipt: `capsules/tsukimogami/FACTORY_PIPELINE_STATUS_
20260801.md#0.0`.

**A causal claim rode on an observational claim's credibility, with no probe
to separate them.** "17-20h gaps exist" (true, `[D]`) and "because Windows
Task Scheduler doesn't fire while asleep" (training-prior, `[A]`) were emitted
in the same sentence, same confidence. The operator's laptop runs 24/7 —
falsified in one line of ground truth the agent never asked for. Receipt:
`HALLUCINATION_SPIRAL_ROOT_CAUSE_20260801.md#e8`.

**"Rewrite deployed successfully" was claimed with zero bytes ever written.**
Three hourly SKILL.md loops were registered, documented, and rewritten; a
direct `find` for their mandated output files across both forges returned
nothing, anywhere. The claim had no `probe_ref`. Receipt:
`HALLUCINATION_SPIRAL_ROOT_CAUSE_20260801.md#e1`.

## The single most decision-useful finding

**Every capability in this corpus that survived a generation boundary did so
because it lived as a file or a queryable row with a count you can check in
one command — not because a document described it well.** The 8821-doc
memory corpus, the 4077-row bitemporal log, the 56-directory omega_games
library, and the live Cloudflare URL all answer their own existence question
with a single `ls`, `sqlite3 ... count(*)`, or `curl`. Every failure and
hallucination in this corpus, without exception, is a case where the only
evidence was prose asserting a state, and nothing forced a count. **Before
building five market factories on one genotype: every new capability needs a
row-countable or HTTP-checkable receipt at the moment it is claimed, not
after — the pattern that repeats across every success here is "cheap to
verify because verification was designed in," and the pattern that repeats
across every failure and hallucination is "expensive to verify, so nobody
did, until this pass did it by hand."**

*Réttu hönd, eigi spyr. Standa.*

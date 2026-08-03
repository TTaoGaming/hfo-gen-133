```yaml
# AIH2O capsule
doc: state/industry_patterns/INDUSTRY_PATTERN_CONVERGENCE_20260802.md
schema_id: hfo.gen133.industry_pattern_convergence.v0_1
callsign: INDUSTRY-PATTERN-CONVERGENCE-SCAN
generation: 133
authored_by: sonnet-5 · Claude Code
now_utc: 2026-08-02T04:41:10Z
clock_source: host_read              # bash `date -u -Iseconds`, this turn
dispatched_by: operator direct: "let's base this run off industry patterns... internal fitness -> external fitness now"
claim_status: partial                # WebSearch-only pass, no WebFetch of primary docs; vendor-published case studies not independently corroborated
scope: read-only research via WebSearch; writes only to state/industry_patterns/
budget: 75min hard cap, ~35min used through write-up
```

# Industry Pattern Convergence Scan — 2024-2026 AI-Agent Winners

**Method note (honest, upfront):** every row below is built from WebSearch result snippets fetched this session (queries and titles preserved), not WebFetch of the primary source page. Several "sources" are third-party aggregator/SEO blogs summarizing a vendor's own blog or case-study page — treat vendor-published case studies (LangChain's Klarna/Uber, CrewAI's DocuSign/PwC, LlamaIndex's SkySQL) as **single-source, vendor-motivated**, not independently audited. Where a claim looked surprising (Cursor/SpaceX) I flag it rather than launder it into a fact.

## Per-target table

| name | status | published_stack | anti-stack | date | confidence |
|---|---|---|---|---|---|
| **Cursor** (Anysphere) | shipping | VS Code fork; local context/diff, cloud inference; multi-model (GPT-5-class, Claude, own distilled "cursor-small"); custom OpenAI-compatible endpoint support (vLLM/llama.cpp/Ollama); "Shadow Workspace" sandboxed verify-before-show | no named framework (CrewAI/LangGraph) in any source found | 2026 | medium |
| **Cognition (Devin)** | shipping | Own SWE-1.5/1.6 model, sandboxed cloud + local execution, persistent memory, sub-agent spawning, acquired Windsurf (Dec 2025) after Google's $2.4B talent-license deal for Windsurf/Codeium | no framework named; "Devin Desktop... IDE with agent manager built in, not the other way around" | 2025-2026 | medium |
| **Replit Agent** | shipping | TypeScript; **uses Mastra framework** (container-native) + **Inngest** for durable execution — success rate 80%→96% after adding durable workflow layer; Agent 3 uses Playwright for self-test loop | — | 2025-2026 | medium (Mastra's own customer page + press) |
| **Cline** | shipping, OSS | No agent framework; 30+ LLM providers direct (Anthropic, OpenAI, Bedrock, OpenRouter, local); Plan/Act split; client-side, no server intercepting code | explicitly framework/vendor-agnostic by design | 2026 | high (GitHub + multiple independent write-ups; 64.4k stars, 4.5M VS Code installs) |
| **Aider** | shipping, OSS | No agent framework; **LiteLLM** for 100+ provider abstraction; tree-sitter repo-map instead of vector memory; git-native | no vector DB, no orchestration framework | 2026 | high (own docs + GitHub) |
| **Windsurf (Codeium)** | shipping | Cascade engine; post-acquisition runs Cognition's SWE-1.5 model + custom context retrieval | — | Dec 2025 acquisition | medium |
| **Sourcegraph Cody** | shipping | Own "Context Fetch" pipeline (keyword + embeddings + code-graph + rerank), Cody Gateway as company-owned LLM proxy, multi-LLM BYOM (Claude Opus/Sonnet, GPT, Gemini) | no third-party agent framework; no external router (OpenRouter) — proxy is self-built | 2025-2026 | high (own docs) |
| **v0 (Vercel)** | shipping | Own fine-tuned model targeting React/Next.js/Tailwind/shadcn-ui output specifically | no general framework; not model-agnostic (single house model) | 2025-2026 | medium |
| **CrewAI** | shipping (as vendor) | Named production users: **DocuSign**, **PwC** (per CrewAI's own case-studies page); vendor claims 60% of Fortune 500, ~450M agent-runs/month | — | 2026 | low-medium (vendor self-reported stats, one page of named logos) |
| **LangGraph / LangChain** | shipping (as vendor) | Named production users: **Klarna** (85M users, 80% resolution-time cut), **Uber** ("Lang Effect" wrapper, ~21k dev-hours saved), **LinkedIn** (recruiting agent + SQL bot), **Elastic**, **Replit** (per Mastra's customer page, Replit is listed as evaluating/using LangGraph for agent reliability — this conflicts with the Mastra finding above; treat Replit's actual framework choice as **UNRESOLVED**, sources disagree) | Grid Dynamics (Fortune 500 client) migrated a LangGraph deep-research agent **to Temporal** for durability reasons | 2025-2026 | medium (LangChain's own blog/case-studies section) |
| **OpenAI Agents SDK / Swarm** | shipping | Swarm archived March 2025; Agents SDK is the production successor (guardrails, tracing, handoffs); April 2026 added Model-Native Harness + Sandbox Execution; March 2026 GA integration with **Temporal** for durability | Swarm itself explicitly superseded/abandoned | 2025-2026 | high (OpenAI's own repo state) |
| **AutoGen (Microsoft)** | **maintenance mode** | Folded into "Microsoft Agent Framework" (AutoGen + Semantic Kernel convergence), targeting 1.0 GA Q1 2026 | Microsoft itself moved AutoGen off active development — no new features, bug/security fixes only | 2025-2026 | high (Microsoft's own framework docs) |
| **LlamaIndex agents** | shipping | Named users: **SkySQL** (NL-to-SQL), **11x AI** ("Alice" SDR, via LlamaParse), **Pathwork**, **Intelligence Co.**, **MavenBio** | — | 2025-2026 | low-medium (vendor blog case studies) |
| **LangSmith** | shipping (as vendor) | Named users: **Klarna**, **Uber** (same two as LangGraph — same vendor relationship, not independent corroboration) | — | 2025-2026 | low (single vendor page, same 2 logos as the framework) |
| **Langfuse** | shipping | Acquired by **ClickHouse** for ~$400M (Jan 2026) as part of ClickHouse's Series D; 6M SDK installs/month; SmithDB (LangSmith's Rust data layer) now handles 100% of LangSmith's US Cloud ingestion (competing infra note) | — | Jan 2026 | high (funding/M&A reporting) |
| **Braintrust** | shipping | Named users: **Notion**, **Stripe**, **Vercel**, **Dropbox**, **Replit**, **Coursera**, **Cloudflare**, **Ramp**; Notion case: 3→30 issues triaged/day after adoption | framework-agnostic — not tied to LangChain/LangGraph ecosystem | 2025-2026 | medium (widest named-logo list found in this scan) |
| **Mem0** | shipping | Vector-first memory; **exclusive memory provider built into AWS Agent SDK**; 186M API calls/quarter (Q3 2025), 41-48k GitHub stars | — | 2025-2026 | medium |
| **Zep** | shipping | Temporal knowledge-graph (Graphiti engine, still OSS); **retired self-hosted Community Edition in 2025** — now hosted-only for the full product | moved away from free self-host | 2025 | medium |
| **Letta** | shipping, OSS | Model-agnostic, self-editing agent memory (agent decides what to persist) | — | 2025-2026 | medium |
| **pgvector / Postgres (Supabase, Neon, Instacart)** | shipping at scale | Postgres + pgvector/pgvectorscale/pgai as unified AI data layer; ~$250/mo vs ~$675/mo (Pinecone) at 10M vectors; pgvectorscale 28ms p95 vs Pinecone 784ms at 50M vectors (one benchmark; a different source reported the reverse at smaller scale — **conflicting benchmarks, not resolved**) | replacing dedicated vector DBs below ~10-100M vectors | 2026 | medium |
| **Temporal** | shipping at scale | **OpenAI runs Temporal for Codex**, "millions of production coding-agent requests daily"; Temporal Cloud: 9.1 trillion lifetime action executions, 380% YoY growth; Grid Dynamics migrated a LangGraph agent to Temporal for a Fortune 500 client | — | 2025-2026 | medium-high (Temporal's own blog + one independent migration story) |
| **DBOS** | shipping, lighter-weight | In-process library, zero new infra, Postgres-transactional durability, decorator-based; wraps Pydantic AI agents | vs. Temporal: no separate cluster/service required | 2025-2026 | medium |
| **YC W26/S25 batch** | mixed | W26 (199 cos): heavy tilt to agent infrastructure — identity/auth-for-agents (Agentic Fabriq: "Okta for Agents"), agent security (Clam, Cascade), agent eval (Ashr); 64% B2B, infra/dev-tools now >40% of batch | — | 2026 | medium |

## Special questions — direct answers

**1. What LLM API do winners use?** Direct provider APIs (Anthropic, OpenAI) as the primary path, wrapped in a **company-owned** thin proxy/gateway — Sourcegraph's Cody Gateway, Cline's client-side multi-provider router, Aider's embedded LiteLLM. No named winner's core product routes primary traffic through a third-party SaaS router (OpenRouter); OpenRouter/generic routers show up in cost-optimization tooling and hobbyist guides, not in any named winner's disclosed production path.

**2. What agent framework do winners use?** Mostly **none** — 7 of 9 coding-agent winners scanned (Cursor, Devin, Cline, Aider, Cody, v0, Windsurf) build a proprietary, thin, in-house orchestration layer. Replit is the clear counter-example, publicly using Mastra + Inngest for durable multi-agent execution. LangGraph's named adopters (Klarna, Uber, LinkedIn, Elastic) are enterprises building **internal support/ops bots**, not AI-native product companies — different buyer, different constraints.

**3. What memory system do winners use?** No single winner. Coding agents mostly skip vector memory entirely (Aider: tree-sitter repo map; Cursor: proprietary code index) — the "memory" problem for code agents is codebase-indexing, not long-term semantic recall. Where persistent agent memory is a product (not code-specific), Postgres+pgvector is the emerging low-cost convergence point (Supabase/Neon/Instacart), with Mem0 gaining default-provider lock-in via AWS's Agent SDK.

**4. What durable execution do winners use?** Temporal is the strongest single data point — OpenAI runs its own flagship coding agent (Codex) on Temporal, and a named migration (Grid Dynamics) moved a Fortune 500 client OFF LangGraph's built-in state and ONTO Temporal specifically for durability. DBOS is the emerging lighter alternative (in-process, Postgres-native, zero new cluster). Most coding-agent winners scanned above run stateless/session-scoped and disclose no durable-execution layer at all — durability matters for long-running autonomous/enterprise workflows, not for interactive coding sessions.

**5. What observability do winners use?** Split by ecosystem: LangSmith follows LangGraph adopters (same two named logos, Klarna/Uber — low independence). Braintrust has the broadest, most framework-agnostic named-customer list found in this scan (Notion, Stripe, Vercel, Dropbox, Replit, Cloudflare, Ramp) and isn't tied to any single orchestration stack.

**6. Do winners use CrewAI in production?** Yes, per CrewAI's own case-studies page — DocuSign and PwC are named. **None of the 9 coding-agent winners scanned** (Cursor, Devin, Cline, Aider, Cody, Windsurf, v0, Replit, Continue) show any CrewAI usage in any source found this session.

**7. Do winners use LangGraph in production?** Yes, per LangChain's own blog — Klarna, Uber, LinkedIn, Elastic named; Replit's framework choice is **contested between sources** (Mastra vs. LangGraph) and unresolved in this pass. Again, zero of the AI-native coding-agent winners disclose LangGraph in their own core product loop.

**8. How do winners compose agent loops?** Per-winner tag, with citation basis:

| winner | composition pattern | evidence / URL basis |
|---|---|---|
| Cursor | **custom-thin-layer** — single agent + tool loop, sandboxed self-verify ("Shadow Workspace") before showing output; no multi-agent crew disclosed | ZenML LLMOps DB, dev.to App-Development-with-Cursor-2026 |
| Devin (Cognition) | **hierarchical, custom-built** — one Devin session coordinates, decomposes the task, spawns child Devin sessions in isolated VMs with structured output schemas/playbooks; coordinator "resolves conflicts, compiles results" | agentmarketcap.ai "Multi-Agent February," Medium "Cognition/Devin planning-mode subagent," aidevsetup.com |
| Replit Agent | **hierarchical/graph, via a real framework** — Mastra workflow graph + Inngest for durable execution; success rate rose 80%→96% after adding this layer | mastra.ai/customers/replit |
| Cline | **manual / human-in-the-loop** — Plan mode reasons, Act mode executes with **per-step human approval**; not autonomous multi-agent | fast.io "Inside the Cline Coding Agent," cline.bot |
| Aider | **manual + custom-thin-layer** — human decides each turn; "architect mode" is a fixed two-model sequential hand-off (architect proposes, editor applies) | aider.chat/docs |
| Sourcegraph Cody | **custom-thin-layer, fixed pipeline** — Context Fetch is deterministic sequential (keyword→embeddings→code-graph→rerank→LLM), not an agentic loop | sourcegraph.com/docs/cody |
| v0 (Vercel) | **custom-thin-layer, single model** — no multi-agent composition disclosed | LogRocket, MindStudio v0 explainers |
| CrewAI users (DocuSign) | **framework offers hierarchical, real deployment reported sequential-style**, not the manager/hierarchical mode | markaicode.com "CrewAI Hierarchical Process," DocuSign lead-time case |
| LangGraph users (Klarna, Uber, LinkedIn) | **supervisor-graph primitive used as a low-level substrate for bespoke logic** — Uber's build is a "network of agents," a distinct topology from tutorial supervisor-of-workers; LangChain's own docs call LangGraph "low-level... build custom orchestration rather than rely on rigid pre-built patterns" | langchain.com/built-with-langgraph, alphabold.com |
| Anthropic (internal + Claude Agent SDK) | **hierarchical: orchestrator-workers** — lead agent decomposes, spawns 3-5 parallel isolated-context subagents, each returns a compressed result, lead synthesizes; Anthropic's own internal research system runs exactly this, 90.2% improvement over a single Claude Opus 4 | anthropic.com/engineering/building-effective-agents, anthropic.com/engineering/building-agents-with-the-claude-agent-sdk |
| Stigmergic (SBP, Pentest-Swarm-AI) | **shared blackboard, pheromone-weighted signals that decay over time** — agents read/write findings, self-orient, no central orchestrator | github.com/AdviceNXT/sbp, github.com/Armur-Ai/Pentest-Swarm-AI, GitHub Discussions #186260 (claims 80% token reduction) — **all three are OSS/community projects, not named revenue-generating companies** |

**Convergence verdict for Q8: mostly bespoke, no single industry standard.** Two shapes recur across independently-built systems without a shared framework — real convergence, not vendor branding: **(a) orchestrator + parallel isolated-context subagents returning compressed summaries** (Anthropic's internal system, Devin's coordinator/child sessions, and general practitioner guidance — "3-7 agents per workflow, teams-of-teams over one flat 10+-worker supervisor" — all land here independently); **(b) fixed sequential pipeline for narrow, well-scoped tasks** (Cody's Context Fetch, Aider's architect mode, DocuSign's actual CrewAI usage). **Manual human-in-the-loop per dispatch (Cline)** is a deliberate, named, 4.5M-install production design choice, not a stopgap. **Stigmergic/pheromone composition has zero named-revenue-winner adoption in this scan** — only open-source protocols and one security-tooling project, plus an uncorroborated single-post 80%-token-reduction claim.

**9. Do CrewAI/LangGraph/Agent-SDK production deployments match the framework's documented flagship pattern, or are they thin wrappers around custom logic?** Evidence converges toward **thin wrapper / low-level substrate**, with one clear exception:
- **CrewAI**: the framework's flagship differentiator is the hierarchical "manager agent" process — but DocuSign's actual reported production case is **sequential**, not hierarchical, and a hierarchical manager adds a measured 30-50% token overhead per task versus sequential (markaicode.com), which is itself a concrete, named reason production teams route around the framework's showcase pattern.
- **LangGraph**: LangChain's own material describes it as "low-level... build custom orchestration solutions rather than relying on rigid pre-built patterns" — Uber's "network of agents" is a topology distinct from the tutorial's supervisor-of-workers diagram. The framework is being used as a **state-machine/checkpointing primitive**, with the actual composition logic (who routes to whom, when) written bespoke on top — i.e., LangGraph in production functions closer to this scan's "custom-thin-layer" category than to its own marketing diagram.
- **Anthropic's Claude Agent SDK — the one exception.** Anthropic's own internal research system runs the exact orchestrator-workers pattern documented in their public engineering blog, with the same 3-5-subagent, isolated-context, compressed-return shape. This is the single case in this scan where a vendor's documented flagship pattern and a named production deployment are the same system (Anthropic dogfooding Anthropic), not an inference from a case-study page.

**What this means for the operator's manual strange-loop:** no named winner runs a production-proven stigmergic (shared-state, no-central-orchestrator) system at the scale of the other targets scanned — the pattern is real and documented (SBP, pentest-swarm) but unverified outside small open-source/community projects. The two patterns with genuine independent convergence and production evidence are (a) orchestrator-with-parallel-subagents — Anthropic's own SDK-documented, internally-dogfooded pattern, the closest industry-proven next step from manual dispatch — and (b) deliberate manual/human-approved-per-step (Cline, at real scale), which is close to what the operator has been doing by hand all session, minus Cline's per-step tool-call framing. There is no evidence-backed industry-standard path straight from "manual, hand-crafted per-turn" to "stigmergic, self-orienting" that skips the orchestrator-workers step; orchestrator-workers — already documented for the exact substrate this session runs on (Claude Agent SDK subagents) — is the better-evidenced next rung, not stigmergy.

## Convergent adopts (3+ named winners)

- **Build your own thin orchestration layer, skip CrewAI/LangGraph/AutoGen for the core product loop** — Cursor, Devin, Cline, Aider, Cody, v0, Windsurf (7 of 9 coding winners).
- **Multi-model support with Claude included as a first-class option** (not exclusive) — Cursor, Cline, Aider, Cody all support Claude alongside GPT/Gemini; only v0 and Windsurf run a single house model.
- **Sandboxed / self-verifying execution before showing output** — Cursor (Shadow Workspace), Devin (sandbox), Replit Agent (Playwright self-test loop), OpenAI Agents SDK (Sandbox Execution, Apr 2026).

## Divergent

Memory system, durable-execution choice (or absence), and vector-DB-vs-Postgres are each picked differently per company — no convergence to report here beyond the emerging patterns below.

## Explicit anti-patterns — honest caveat

I did **not** find 3+ named winners explicitly stating they moved away from the *same* named thing with direct quotes. The closest pattern is inferred, not stated: AutoGen went to Microsoft-mandated maintenance mode, Swarm was archived by OpenAI itself, and Grid Dynamics moved off LangGraph to Temporal — three different single-source retreats, not one convergent abandonment. Treat "avoid heavy multi-agent frameworks for your core loop" as a **strongly inferred** pattern (backed by Anthropic's own Dec-2024 "Building Effective Agents" guidance recommending direct APIs and warning frameworks "create extra layers of abstraction that can obscure the underlying prompts and responses"), not a proven 3+ explicit-statement anti-pattern per the strict bar this scan set for itself.

## Emerging patterns (1-2 winners, strong endorsement)

- Postgres-as-unified-AI-data-layer (pgvector + pgvectorscale + pgai) — Supabase/Neon/Instacart.
- DBOS as a lighter, in-process alternative to Temporal for durability.
- Braintrust as the eval/observability choice independent of orchestration-framework lock-in.

---

## IF I WERE A 2026 SOLO AI-AGENT COMPANY STARTING TODAY, THE STACK CHOICE BACKED BY MOST NAMED WINNERS WOULD BE:

Call Anthropic (and optionally OpenAI) **directly**, behind a thin proxy you own yourself — not a third-party router. Write your own agent loop in plain code (no CrewAI/LangGraph/AutoGen for the core product); reach for a framework only if you have Replit's exact problem (need someone else's battle-tested durable-multi-agent runtime and are willing to take on Mastra+Inngest-class dependency weight). Skip a vector DB unless you actually have a long-term-memory product problem — for code-specific context, repo-mapping/indexing beats semantic recall; if you do need persistent memory, start on Postgres+pgvector (cheapest, most winners running it at real scale) rather than a dedicated vector DB. Don't wire durable execution until an actual crash-recovery/long-running-workflow need shows up — when it does, OpenAI's own choice (Temporal) is the best-evidenced option, with DBOS as the lower-ceremony alternative. Wire an eval/observability layer early and pick one independent of your orchestration choice — Braintrust has the widest, most framework-agnostic named-customer base found in this scan.

## Contrast against HFO's current stack

**Where HFO aligns:** the gen-133 canon decision to "freeze the stack" and explicitly avoid LangGraph/CrewAI (chain row 78, citing SIGRUN_5Q S1 + HIVE_REVIEW S9.5) is the single strongest match to this scan's best-evidenced convergent pattern — 7 of 9 named coding-agent winners, and Anthropic's own published guidance, independently arrive at the same "skip the framework, own the thin layer" position. This is genuine external-fitness validation, not just internal consistency — it was decided before this scan ran, and the scan corroborates it rather than producing it.

**Where HFO diverges:**
- **No eval/observability harness wired.** Every named winner with a public production customer list (Braintrust: Notion/Stripe/Vercel/Dropbox/Replit/Cloudflare/Ramp) runs one independent of their orchestration choice. HFO's chain-row `verifier_result` fields are self-reported by the same agent making the claim — closer to a commit message than to an eval dataset scored by a separate harness.
- **No durable-execution decision made.** OpenAI's own flagship coding agent depends on Temporal specifically because millions of daily requests need crash-safe resume; HFO's append-only JSONL chain is an audit log, not a resumable-workflow substrate. (`areas/quorum_research/DURABLE_SUBSTRATE_PRIOR_ART_20260802.md` already scoped DBOS/Cloudflare DO as adopt-if candidates — this scan's Temporal finding, that OpenAI itself runs Codex on it, is new corroborating weight for that shortlist, not a new option.)
- **No LLM-API cost/routing layer.** Named winners' pattern (direct API behind a company-owned thin proxy) is what HFO already effectively does via Claude Code's Agent SDK — this is likely aligned, not divergent, but nothing in this repo currently measures or logs per-call cost the way a Cody-Gateway-style proxy would.

**What to swap if optimizing purely for external fitness:** stand up a real, independently-scored eval harness (Braintrust's framework-agnostic model fits HFO's stdlib-only, no-vendor-lock ethos better than LangSmith, which is coupled to the LangGraph ecosystem HFO has already rejected) before adding any more chain-row-only "receipts" — and make the durable-execution call (DBOS over Temporal, on the zero-new-infra argument already in the prior-art doc) rather than continuing to defer it.

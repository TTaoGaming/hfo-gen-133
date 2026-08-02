# The Recommended Off-the-Shelf Autonomous-Agent Stack for a Solo Developer in 2026

## Executive verdict

**As of August 2, 2026, the best budget-constrained standard harness is:**

| Piece | Recommendation | Role |
|---|---|---|
| Coding agent | [Aider](https://aider.chat/) | Local, Git-native implementation and refactoring |
| Agent orchestration | [LangGraph](https://www.langchain.com/langgraph) | Explicit multi-agent state machine, loops, retries, and gates |
| LLM routing | [LiteLLM](https://docs.litellm.ai/docs/) in **embedded SDK mode** | One API for Anthropic, OpenAI, Google, OpenRouter, and Ollama |
| Observability and evaluations | [Langfuse Cloud](https://langfuse.com/) free tier | Traces, costs, scores, datasets, and CI evaluations |
| Control plane | [GitHub Actions](https://github.com/features/actions) plus [GitHub Issues](https://docs.github.com/en/rest/issues) | Scheduling, shared state, policy gates, pull requests, and deployment |

The fifth piece deliberately treats GitHub as one control plane rather than pretending that the scheduler, issue tracker, policy script, and deployment workflow are separate infrastructure products. Slack Incoming Webhooks should be a **notification adapter**, not the state store. Vercel or Cloudflare can be the deployment target while GitHub remains the CI/CD authority.

This is the strongest fit because its fixed platform cost can remain at **$0 per month**, leaving most of the approximately $100 monthly ceiling for model inference. Aider, LangGraph, and LiteLLM are open-source; LangGraph is MIT-licensed; LiteLLM exposes one `completion()` interface across more than 100 models/providers, including Ollama; and GitHub Free includes 2,000 Actions minutes per month for private repositories while standard runners are free for public repositories. citeturn12view0turn12view5turn12view6turn13view4turn13view5

The recommendation has three important boundaries:

1. **Do not deploy a generic autonomous “swarm.”** Model the workflow as a small graph with named responsibilities, typed state, bounded retries, and explicit acceptance gates.
2. **Do not operate LiteLLM Proxy or self-host Langfuse initially.** Both are valid later, but they add services, persistence, upgrades, secrets, and failure modes that a solo developer does not need.
3. **Do not expect a GitHub-hosted runner to call Ollama on a laptop.** `localhost` on the runner is not your Windows or Mac machine. Local Ollama should be used during development; scheduled cloud loops should use hosted providers unless you accept a self-hosted runner or machine-local scheduler.

A practical monthly envelope is:

| Expense | Expected monthly range |
|---|---:|
| Aider, LangGraph, LiteLLM SDK | $0 |
| Langfuse Cloud within free allowance | $0 |
| GitHub Actions and Issues within quota | $0 |
| Vercel or Cloudflare free tier | $0 |
| Anthropic, OpenAI, and Google inference | $35–$70 |
| OpenRouter emergency/fallback credit | $0–$15 |
| Contingency | $10–$20 |
| **Expected total** | **$45–$95** |

That estimate assumes short, bounded scheduled jobs, aggressive use of small models, local Ollama for development, and no unattended recursive coding loops.

## Tool comparison

The effort ratings below are implementation judgments for one experienced developer:

- **Low:** usable in under an hour.
- **Medium:** half a day to establish a reliable path.
- **High:** at least a day, a container/runtime service, or substantial workflow design.
- **Integration friction** measures fit with the recommended GitHub/LangGraph/Python architecture, not general product quality.

The “2026 exemplar evidence” column is intentionally strict. I looked for public evidence that established both **solo-developer status** and **actual 2026 use**, rather than treating a vendor tutorial, repository star count, or company testimonial as a case study. Where that evidence was not found, the table says so.

**Coding agents**

| Tool and current URL | Cost, effort, and friction | 2026 solo-dev exemplar evidence | Honest failure mode and disposition |
|---|---|---|---|
| [Aider](https://aider.chat/) | OSS; model usage is BYOK. **Low setup, low friction.** Terminal- and Git-oriented, supports existing codebases and multiple model providers. citeturn12view0turn9search15 | The project publicly dogfoods Aider and publishes usage demonstrations, but I did not find a third-party 2026 production case proving a solo developer’s whole stack. | Context selection still requires judgment; large refactors can produce plausible but incoherent cross-file edits. It can also become expensive when repeatedly sending large repository maps. **Recommended.** |
| [OpenHands](https://www.openhands.dev/) | Local open-source edition is free; individual SaaS is free with BYOK or provider inference at cost. It includes web, terminal and CLI interfaces, Git integration, API automation, and Slack/Jira integration. **Medium-to-high setup locally; medium friction.** citeturn12view1 | Public demos and users exist, but no independently verifiable exact 2026 solo-production case was found. | Its sandbox/container/runtime model is substantially heavier than Aider. The extra autonomy increases blast radius, debugging complexity, and token consumption. Good when you specifically need remote asynchronous coding, but excessive as the default local editor. |
| [SWE-agent](https://swe-agent.com/latest/) | OSS. **Medium setup, high friction for daily development.** It is optimized around taking a repository issue, operating in a controlled environment, and attempting a patch. citeturn0search6turn0search10 | Benchmark runs and public repositories are inspectable; no clear 2026 solo-operated production service was found. | Benchmark-oriented abstractions do not automatically translate into a pleasant interactive coding workflow. Environment construction and dependency reproduction often dominate the actual fix. Better as an evaluation harness than the primary pair programmer. |
| [Cursor](https://cursor.com/) | Hobby is free with limited agent requests; individual Pro is currently $20 per month and supports frontier models, cloud agents, MCPs, skills, and hooks. **Low setup, low integration friction, but closed-source and budget-consuming.** citeturn12view2 | There are abundant personal endorsements, but few audit-ready public cases connecting a solo operator, a specific production system, and 2026 usage. | Cost and usage allowances can be harder to reason about than direct API spend. It also places important development workflow behavior behind a proprietary client. **Best paid UX alternative**, but not the best under a hard $100 total budget. |
| [Cline](https://cline.bot/) | OSS extension and CLI; model spend is generally BYOK. **Low setup, medium friction.** Its Plan/Act workflow and visible tool approvals are useful for controlled editing. citeturn1search0turn1search4 | Personal side-project reports exist, including developers pairing Cline with inexpensive model subscriptions, but these are anecdotes rather than audited production cases. citeturn1search19 | On February 17, 2026, an unauthorized `cline@2.3.0` npm release was published in a supply-chain incident; affected users were instructed to upgrade and rotate exposed credentials. This does not make Cline unusable, but it reinforces the need for extension/package provenance and secrets isolation. citeturn1search6 |
| [Continue.dev](https://continue.dev/) | Historically OSS and easy to install in VS Code/JetBrains. **Low setup, now high lifecycle risk.** | No current independent case is decisive because the product’s status has changed. | Continue was acquired by Cursor; its site says the open-source code remains available, but active users should not choose an acquired, sunset-transition product as the foundation of a new 2026 harness. citeturn12view3turn1search3 |

**Multi-agent frameworks, routing, and observability**

| Tool and current URL | Cost, effort, and friction | 2026 solo-dev exemplar evidence | Honest failure mode and disposition |
|---|---|---|---|
| [CrewAI](https://www.crewai.com/) | OSS core is free. Its hosted Basic plan advertises a free visual editor, GitHub integration, and a limited number of monthly workflow executions. **Low-to-medium setup, medium friction.** citeturn10view0turn2search8 | Numerous tutorials exist, but I did not find a publicly auditable solo-production case proving sustained 2026 operation. | “Crew,” “role,” and conversational delegation abstractions can encourage token-heavy agents discussing work rather than executing a concise state transition. Debugging implicit memory and delegation becomes difficult. Good for rapid demos; weaker for deterministic operations. |
| [AutoGen](https://github.com/microsoft/autogen) | OSS. **Medium setup, high adoption risk for a new project.** | Historical examples are plentiful, but they are no longer persuasive for a greenfield choice. | Microsoft now labels AutoGen **maintenance mode**, says it will not receive new features or enhancements, and directs new users to Microsoft Agent Framework. **Do not start a new system on it.** citeturn12view4 |
| [LangGraph](https://www.langchain.com/langgraph) | MIT-licensed and free. **Medium setup, low-to-medium integration friction.** Strong fit for explicit nodes, conditional edges, durable execution, streaming, interrupts, and human approval. citeturn12view5turn2search6 | Official and community 2026 examples demonstrate real graphs and evaluation paths, though no exact five-piece solo case was found. | It is deliberately low-level. You must design state schemas, termination conditions, retries, checkpoints, idempotency, and side-effect boundaries. That work is a feature for production reliability, but it is more code than CrewAI. **Recommended.** |
| [DSPy](https://dspy.ai/) | MIT Python framework; free aside from model and evaluation calls. **Medium setup, medium-to-high conceptual friction.** citeturn2search3turn2search11 | Public 2026 guides and repositories exist, but not an exact solo production exemplar for this use case. | DSPy is primarily a way to program and optimize language-model pipelines. It does not replace a scheduler, durable orchestration graph, shared issue state, or operational policy layer. Optimizers also require representative datasets and can generate substantial evaluation spend. Use it later for prompt/program optimization, not as the control plane. |
| [LiteLLM](https://docs.litellm.ai/docs/) | OSS SDK and self-hostable proxy. **Low setup in SDK mode; high if operating the proxy.** It provides a consistent OpenAI-shaped interface, retries/fallbacks, and support for OpenAI, Anthropic, Vertex/Google, Ollama, and many others. citeturn12view6 | Personal 2026 self-hosting writeups exist, but public proof of the exact recommended five-piece stack was not found. | Provider features never normalize perfectly. Tool calls, reasoning fields, caching, safety settings, structured output, token accounting, and streaming behavior can diverge. The proxy also needs persistent storage for serious budget/key management. **Recommended as an embedded SDK first.** |
| [Portkey](https://portkey.ai/pricing) | Developer plan is free with 10,000 recorded logs per month and three-day log retention; Production is $49 per month with 100,000 recorded logs and longer retention. **Low setup, low friction, but overlaps both routing and observability.** citeturn13view1 | Vendor customer stories are mostly teams, not verifiable solo cases. | On the free tier, requests continue after the log limit but excess logs are not recorded. That is precisely when a small operator may falsely assume everything is observable. The $49 production plan consumes roughly half the total monthly budget. |
| [OpenRouter](https://openrouter.ai/) | Free tier includes free-model access with limited requests; pay-as-you-go currently adds a 5.5% platform fee and exposes hundreds of models/providers. **Very low setup, low friction.** citeturn12view8 | Widespread indie use is visible, but I did not find an audit-ready exact-stack case. | It is an external aggregation service, not a route to local Ollama. Provider-specific features and data-routing policies can vary, and all hosted calls gain another commercial dependency. **Useful optional fallback or single-billing adapter, not the core abstraction.** |
| [Langfuse](https://langfuse.com/) | OSS and self-hostable; Cloud has a free allowance. It provides traces, sessions, scores, evaluations, prompt management, datasets, and OpenTelemetry-based SDKs. **Low setup in Cloud; high self-hosted.** citeturn4search0turn4search4turn15search1turn15search11 | Personal self-hosting writeups and official LangGraph/LiteLLM integrations exist. No independent exact-five-piece solo case was found. citeturn6search2turn15search5turn15search12 | Self-hosting the current platform is not a tiny single-process deployment; operational requirements undermine the “no custom infrastructure” constraint. In short-lived CI jobs, buffered spans can disappear unless the client is explicitly flushed. **Recommended as managed Cloud first.** citeturn15search7 |
| [LangSmith](https://www.langchain.com/langsmith) | Developer plan provides one free seat and 5,000 base traces per month; paid usage applies beyond the allocation. **Very low friction with LangGraph, low setup.** citeturn12view9 | Strong official LangGraph examples exist; independently verified solo-production cases remain sparse. | It is the smoothest vertically integrated choice but produces greater framework/vendor coupling and has a smaller quoted free trace allowance than the broad free allowances advertised by some alternatives. Choose it when convenience matters more than OSS portability. |
| [Weave by Weights & Biases](https://wandb.ai/site/weave/) | Tracing and evaluation product with a free entry path through W&B. **Low-to-medium setup, medium friction.** citeturn4search2turn4search18 | Public examples largely come from the broader machine-learning community rather than clearly identified 2026 solo agent deployments. | It carries W&B’s broader ML-platform surface area, which can be more product than a solo agent project requires. Current documentation also notes gaps such as TypeScript cost-tracking limitations. citeturn4search30 |
| [Braintrust](https://www.braintrust.dev/) | Starter is $0 with 1 GB processed data, 10,000 scores, 14-day retention, and unlimited projects/users; Pro is $249 per month. **Low setup, medium friction.** citeturn13view3 | Public examples are credible but generally team/company-oriented. | The free tier is attractive for evaluation-heavy prototypes, but the next platform tier is far outside this project’s budget. A successful project can therefore hit an abrupt economic cliff. |

**Scheduling, policy, coordination, and deployment**

| Tool and current URL | Cost, effort, and friction | 2026 solo-dev exemplar evidence | Honest failure mode and disposition |
|---|---|---|---|
| [GitHub Actions](https://github.com/features/actions) | GitHub Free currently includes 2,000 private-repository minutes per month; standard hosted runners are free for public repositories. **Low setup, very low friction.** Scheduled workflows gained IANA timezone support in March 2026. citeturn13view4turn13view5turn13view6 | Millions of public workflows are inspectable, but authorship alone does not prove solo-production status. | Cron execution is best effort: jobs can be delayed or even dropped during high load, especially around the start of an hour. It is not an exact-time workflow engine. Use off-minute schedules, idempotency, and catch-up checks. **Recommended.** citeturn14search1turn14search2 |
| [Windows Task Scheduler](https://learn.microsoft.com/en-us/windows/win32/taskschd/about-the-task-scheduler) | Built into supported Windows versions; no cloud cost. **Low setup, high cross-platform friction.** It can run programs on time- or event-based triggers. citeturn11search0turn11search1 | Personal automation is ubiquitous but normally not published as a traceable case study. | Jobs depend on one physical machine, its power state, network, user permissions, environment variables, and credential storage. It also creates a separate operational path from Mac and CI. Use only for local Ollama jobs that genuinely must stay local. |
| `cron` / macOS scheduling | Built into Unix-like environments, with no cloud fee. **Low setup, high cross-device operational friction.** | A 2026 solo-built multi-agent project, Constellagent, publicly describes cron-based automation, but it is not the exact recommended stack. citeturn8search0 | The machine must be awake and correctly configured; secrets and Python environments drift; macOS sleep behavior can make scheduled execution unreliable. It also lacks hosted logs, issue permissions, and deployment environments by default. |
| [Temporal Cloud](https://temporal.io/pricing) | Current Essentials pricing starts at **$100 per month**; higher plans start at $500. A startup credit program exists, but that is not a permanent general free tier. **High setup and economically disqualifying here.** citeturn12view12 | Strong production company cases exist, not a compelling under-$100 solo case. | Temporal is excellent for durable, long-running, high-value business workflows. For this project, its minimum price alone exhausts the cloud budget before model inference. **Reject for now.** |
| [Open Policy Agent](https://www.openpolicyagent.org/) | Apache-licensed CNCF project; standalone binary and container options. **Medium setup, medium-to-high friction for a solo application.** citeturn5search6turn5search10turn10view5 | No convincing 2026 solo agent-system case was found. | Rego, bundles, input schemas, test infrastructure, and policy distribution add a second programming system. OPA becomes valuable once multiple services or teams must enforce the same policy; it is premature for one repository and one operator. |
| Custom policy gate | No platform fee. A small version-controlled Python module can check test results, evaluation scores, cost limits, file paths, and requested side effects. **Low setup, low friction.** | The recommended reference implementation below is reproducible, but not presented as an external case study. | Ad hoc checks become inconsistent when scattered through prompts and workflow YAML. Keep one typed policy result, unit-test it, and log every decision. **Recommended initially.** |
| [GitHub Issues](https://docs.github.com/en/rest/issues) | Included with GitHub. **Low setup, very low friction.** Issues provide labels, comments, assignees, references, searchable history, and API access. citeturn7search0turn14search2 | Public solo projects routinely use Issues, although proving that an issue was agent-controlled rather than manually controlled is difficult. | Issues are not a transactional database. Concurrent updates, duplicate runs, stale labels, API limits, and prompt injection through issue text must be handled. Despite that, they are an excellent low-volume canonical work ledger. **Recommended.** |
| [Slack Incoming Webhooks](https://api.slack.com/messaging/webhooks) | Webhook posting is available without a custom message server; Slack Free has product limits including finite searchable history and application limits. **Low setup, low friction as an output only.** citeturn5search3turn5search25 | Personal automation examples are common but rarely production-auditable. | Incoming webhooks are effectively write-only notification channels. A leaked webhook URL is a secret leak, and Slack messages make poor canonical state because they can be buried, deleted, or aged out. Use for alerts, never as the source of truth. |
| [Vercel GitHub deployment](https://vercel.com/docs/deployments/git) | Free entry tier with Git-based previews and production deployments. GitHub Actions can invoke Vercel CLI for explicit builds and deployment. **Low setup, low friction.** citeturn7search2turn7search6turn7search10 | Numerous indie applications use it, but exact stack provenance is generally private. | Usage ceilings and platform-specific conventions can create lock-in. Never let an agent deploy directly from an unreviewed issue; deploy a tested commit or protected branch. |
| [Cloudflare Pages Git integration](https://developers.cloudflare.com/pages/configuration/git-integration/) | Free entry tier and automatic branch previews. **Low setup, low friction for static/edge applications.** citeturn7search1turn7search3 | Similar evidence limitations to Vercel. | It is strongest for static and edge-oriented applications. Traditional long-running server workloads may need architectural changes for Workers or an external backend. |

The most consequential eliminations are therefore:

- **Continue.dev:** acquired and no longer a safe greenfield foundation.
- **AutoGen:** maintenance mode.
- **Temporal Cloud:** minimum price consumes the entire budget.
- **OPA:** sound technology at the wrong operational scale.
- **Self-hosted Langfuse and LiteLLM Proxy:** avoidable infrastructure for the initial system.
- **CrewAI:** faster demo, weaker operational explicitness.
- **OpenHands:** capable but too heavy as the default coding interface.
- **Cursor:** excellent UX, but the $20 subscription competes directly with inference budget.
- **Slack as state:** wrong data model.

## Recommended architecture

The system should be a **bounded issue-processing machine**, not an open-ended society of agents.

```text
Developer
   |
   | Aider edits, tests, commits, opens PRs
   v
GitHub repository
   |
   +---- GitHub Issue: canonical task/state ledger
   |
   +---- GitHub Action: schedule / manual dispatch / issue trigger
              |
              v
         LangGraph workflow
         ┌───────────────────────────────┐
         │ intake -> plan -> execute     │
         │       -> review -> gate       │
         │          ^          |         │
         │          └-- retry --┘         │
         └───────────────────────────────┘
              |
              +---- LiteLLM SDK
              |       +-- Anthropic primary
              |       +-- OpenAI reviewer
              |       +-- Google long-context/fallback
              |       +-- Ollama during local runs only
              |
              +---- Langfuse traces, costs, scores
              |
              +---- GitHub Issue comments and labels
              |
              +---- PR, tests, evaluation gate
                        |
                        v
                 Vercel / Cloudflare
```

The architectural rules matter more than the tool names.

**GitHub Issues is the durable shared surface.** Each work item receives an issue with machine-readable labels such as:

```text
agent:queued
agent:running
agent:blocked
agent:review
agent:approved
agent:failed
agent:done
risk:low
risk:high
```

The issue body contains the requested outcome, acceptance criteria, repository scope, and an immutable task identifier. Agent outputs appear as comments, while labels represent the coarse state. This keeps the operator-visible ledger outside LangGraph’s internal memory.

**LangGraph owns only execution state.** A graph run can hold plans, candidate results, review findings, attempt counts, and score summaries. It should not become the only record of what happened.

**LiteLLM owns provider normalization, not business routing.** The graph decides that a task needs “primary,” “reviewer,” “cheap,” or “long-context” capability. Environment variables map those roles to concrete provider model IDs. That avoids spreading model names across node code.

**Langfuse owns telemetry and evaluation evidence.** It should capture graph-run IDs, issue numbers, model aliases, actual provider model IDs, token use, latency, retry count, estimated cost, test outcome, and evaluation scores. Langfuse’s current Python SDK is OpenTelemetry-based, and its LiteLLM integration can capture provider calls through either SDK or proxy modes. citeturn15search1turn15search5turn15search12

**The custom policy gate owns authority.** LLM output does not grant permission. A deterministic function decides whether a run can open a pull request, request human review, or deploy.

A minimal release policy should require all of the following:

```text
tests_passed == true
static_checks_passed == true
evaluation_score >= configured threshold
estimated_run_cost <= configured ceiling
attempt_count <= configured ceiling
changed_paths are within allowlist
no secret-like strings in generated diff
no dependency or workflow changes unless explicitly permitted
no database migration without human approval
no direct push to the protected production branch
```

**Aider stays out of production.** It is the operator’s implementation tool. Scheduled runtime code should not launch an unrestricted coding agent against the repository. A scheduled job may generate a proposed patch in a branch, but production deployment must remain downstream of deterministic tests and branch protection.

**Slack receives alerts only.** Send concise messages for blocked, failed, unexpectedly expensive, or deploy-ready tasks. The message should link back to the Issue and Langfuse trace instead of duplicating state.

### The Ollama boundary

Local Ollama and infrastructure-free hosted scheduling are not simultaneously available from a standard GitHub runner.

A hosted Action can use:

```text
Anthropic API
OpenAI API
Google API
OpenRouter API
another internet-reachable endpoint
```

It cannot use:

```text
http://localhost:11434 on your laptop
```

There are only three technically honest choices:

| Requirement | Execution choice |
|---|---|
| No persistent personal infrastructure | Use hosted models in scheduled Actions |
| Scheduled jobs must use local Ollama | Use Windows Task Scheduler, cron/launchd, or a self-hosted GitHub runner |
| Hosted scheduler must reach privately hosted Ollama | Expose a secured network endpoint, which is custom infrastructure and not recommended here |

The recommended split is **Ollama for local development and cheap manual dry runs; hosted models for unattended GitHub Actions**.

## Installation

All of the following approaches install into the user profile or project virtual environment and do not require system-wide administrator access.

**Aider on macOS**

```bash
curl -LsSf https://aider.chat/install.sh | sh
aider --version
```

**Aider on Windows PowerShell**

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://aider.chat/install.ps1 | iex"
aider --version
```

Aider’s documentation also provides `uv`-based installation paths and provider-specific configuration, including Ollama and OpenRouter. citeturn0search12turn9search1turn9search3

For a local Ollama model:

```bash
# Ollama must already be running locally.
export OLLAMA_API_BASE=http://127.0.0.1:11434
aider --model ollama_chat/qwen3:8b
```

PowerShell equivalent:

```powershell
$env:OLLAMA_API_BASE = "http://127.0.0.1:11434"
aider --model "ollama_chat/qwen3:8b"
```

Do not hard-code a hosted provider key into `.aider.conf.yml`. Put keys in environment variables or a secrets manager.

**Python project on macOS**

```bash
python3 -m venv .venv
. .venv/bin/activate

python -m pip install --upgrade pip
python -m pip install \
  langgraph \
  litellm \
  langfuse \
  pydantic \
  httpx \
  pytest

python -m pip freeze > requirements.lock.txt
```

**Python project on Windows PowerShell**

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1

python -m pip install --upgrade pip
python -m pip install `
  langgraph `
  litellm `
  langfuse `
  pydantic `
  httpx `
  pytest

python -m pip freeze > requirements.lock.txt
```

For reproducibility, commit the lock file and periodically update dependencies on a dedicated branch. Do not use unbounded automatic dependency upgrades inside the agent loop.

A reasonable repository layout is:

```text
.
├── .github/
│   └── workflows/
│       ├── agent-loop.yml
│       └── deploy.yml
├── agent/
│   ├── graph.py
│   ├── models.py
│   ├── github_state.py
│   ├── policy.py
│   └── evals.py
├── tests/
│   ├── test_graph.py
│   ├── test_policy.py
│   └── test_evals.py
├── prompts/
│   ├── planner.md
│   ├── worker.md
│   └── reviewer.md
├── requirements.lock.txt
├── .env.example
└── pyproject.toml
```

## Reference configuration

### Provider aliases

Use capability aliases instead of embedding changing model names in source code.

```dotenv
# .env.example — never commit real values

ANTHROPIC_API_KEY=
OPENAI_API_KEY=
GEMINI_API_KEY=

# Local development only
OLLAMA_API_BASE=http://127.0.0.1:11434

# Concrete provider model identifiers are configuration.
MODEL_CHEAP=ollama_chat/qwen3:8b
MODEL_PRIMARY=anthropic/REPLACE_WITH_CURRENT_MODEL_ID
MODEL_REVIEW=openai/REPLACE_WITH_CURRENT_MODEL_ID
MODEL_LONG=gemini/REPLACE_WITH_CURRENT_MODEL_ID

LANGFUSE_PUBLIC_KEY=
LANGFUSE_SECRET_KEY=
LANGFUSE_BASE_URL=https://us.cloud.langfuse.com
LANGFUSE_OTEL_HOST=https://us.cloud.langfuse.com

MAX_AGENT_ATTEMPTS=2
MAX_RUN_COST_USD=2.00
MIN_EVAL_SCORE=0.85
```

Keeping concrete hosted model IDs outside the codebase is important because providers rename, retire, or repoint model identifiers. LiteLLM’s stable value is the provider-normalized call surface, not a guarantee that every model’s semantics remain identical. LiteLLM documents the provider-prefixed model convention and one `completion()` API across providers. citeturn12view6

### LiteLLM and Langfuse

Langfuse’s current LiteLLM SDK integration uses its OpenTelemetry callback:

```python
# agent/models.py
from __future__ import annotations

import os
from typing import Any

import litellm
from litellm import completion


litellm.callbacks = ["langfuse_otel"]

MODEL_BY_ROLE = {
    "cheap": os.environ["MODEL_CHEAP"],
    "primary": os.environ["MODEL_PRIMARY"],
    "review": os.environ["MODEL_REVIEW"],
    "long": os.environ["MODEL_LONG"],
}


def call_model(
    *,
    role: str,
    system: str,
    user: str,
    temperature: float = 0.0,
) -> str:
    if role not in MODEL_BY_ROLE:
        raise ValueError(f"Unknown model role: {role}")

    response: Any = completion(
        model=MODEL_BY_ROLE[role],
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": user},
        ],
        temperature=temperature,
        timeout=90,
        num_retries=1,
        metadata={
            "model_role": role,
            "runtime": os.getenv("AGENT_RUNTIME", "local"),
            "github_issue": os.getenv("AGENT_ISSUE_NUMBER", ""),
        },
    )

    content = response.choices[0].message.content
    if not content:
        raise RuntimeError(f"Model role {role!r} returned empty content")

    return str(content)
```

The exact `langfuse_otel` callback is documented by Langfuse for LiteLLM SDK calls. citeturn15search12

### Bounded LangGraph workflow

The graph should be small enough to understand from one screen.

```python
# agent/graph.py
from __future__ import annotations

import os
from typing import Literal, TypedDict

from langgraph.graph import END, START, StateGraph
from langfuse import get_client, observe

from agent.models import call_model


class AgentState(TypedDict):
    issue_number: int
    task: str
    acceptance_criteria: str
    plan: str
    result: str
    review: str
    attempts: int
    approved: bool
    failure_reason: str


MAX_ATTEMPTS = int(os.getenv("MAX_AGENT_ATTEMPTS", "2"))


@observe(name="planner")
def plan_node(state: AgentState) -> dict:
    plan = call_model(
        role="primary",
        system=(
            "Create a concise execution plan. Do not claim that work has "
            "been completed. Identify tests and risky side effects."
        ),
        user=(
            f"Task:\n{state['task']}\n\n"
            f"Acceptance criteria:\n{state['acceptance_criteria']}"
        ),
    )
    return {"plan": plan}


@observe(name="worker")
def work_node(state: AgentState) -> dict:
    result = call_model(
        role="primary",
        system=(
            "Produce the requested artifact or proposed change. "
            "Stay within the supplied task and acceptance criteria."
        ),
        user=(
            f"Plan:\n{state['plan']}\n\n"
            f"Previous review:\n{state.get('review', '')}"
        ),
    )
    return {
        "result": result,
        "attempts": state["attempts"] + 1,
    }


@observe(name="reviewer")
def review_node(state: AgentState) -> dict:
    review = call_model(
        role="review",
        system=(
            "Act as an adversarial reviewer. Return the first line as "
            "'APPROVE' or 'REJECT', then explain concrete defects."
        ),
        user=(
            f"Task:\n{state['task']}\n\n"
            f"Acceptance criteria:\n{state['acceptance_criteria']}\n\n"
            f"Candidate result:\n{state['result']}"
        ),
    )

    return {
        "review": review,
        "approved": review.lstrip().startswith("APPROVE"),
    }


def route_after_review(
    state: AgentState,
) -> Literal["retry", "finish", "fail"]:
    if state["approved"]:
        return "finish"
    if state["attempts"] >= MAX_ATTEMPTS:
        return "fail"
    return "retry"


def failure_node(state: AgentState) -> dict:
    return {
        "failure_reason": (
            f"Reviewer rejected output after {state['attempts']} attempts"
        )
    }


builder = StateGraph(AgentState)
builder.add_node("plan", plan_node)
builder.add_node("work", work_node)
builder.add_node("review", review_node)
builder.add_node("failure", failure_node)

builder.add_edge(START, "plan")
builder.add_edge("plan", "work")
builder.add_edge("work", "review")
builder.add_conditional_edges(
    "review",
    route_after_review,
    {
        "retry": "work",
        "finish": END,
        "fail": "failure",
    },
)
builder.add_edge("failure", END)

graph = builder.compile()


def run_agent(initial_state: AgentState) -> AgentState:
    try:
        return graph.invoke(initial_state)
    finally:
        # GitHub Actions and CLI commands are short-lived.
        # Export buffered telemetry before the process exits.
        get_client().flush()
```

Langfuse explicitly recommends `flush()` or shutdown handling for short-lived jobs so queued telemetry is exported before process termination. citeturn15search7

This graph intentionally does not allow agents to invent additional agents, recursively rewrite their own workflow, or run indefinitely. Adding agents should mean adding a visible node with a testable contract.

### Deterministic policy gate

```python
# agent/policy.py
from __future__ import annotations

from dataclasses import dataclass
from pathlib import PurePosixPath


ALLOWED_ROOTS = {
    "app",
    "src",
    "tests",
    "docs",
    "prompts",
}

SENSITIVE_PATHS = {
    ".github/workflows",
    "infra",
    "migrations",
    "terraform",
}


@dataclass(frozen=True)
class GateInput:
    tests_passed: bool
    static_checks_passed: bool
    eval_score: float
    estimated_cost_usd: float
    max_cost_usd: float
    changed_files: tuple[str, ...]
    attempts: int
    max_attempts: int
    human_approved_sensitive_change: bool = False


@dataclass(frozen=True)
class GateResult:
    allowed: bool
    reasons: tuple[str, ...]


def evaluate_gate(value: GateInput) -> GateResult:
    reasons: list[str] = []

    if not value.tests_passed:
        reasons.append("Tests failed")

    if not value.static_checks_passed:
        reasons.append("Static checks failed")

    if value.eval_score < 0.85:
        reasons.append(f"Evaluation score too low: {value.eval_score:.3f}")

    if value.estimated_cost_usd > value.max_cost_usd:
        reasons.append(
            f"Run cost ${value.estimated_cost_usd:.2f} exceeds "
            f"${value.max_cost_usd:.2f}"
        )

    if value.attempts > value.max_attempts:
        reasons.append("Attempt limit exceeded")

    for raw_path in value.changed_files:
        path = PurePosixPath(raw_path)
        root = path.parts[0] if path.parts else ""

        if root not in ALLOWED_ROOTS and not raw_path.startswith(".github/"):
            reasons.append(f"Path outside allowlist: {raw_path}")

        if any(
            raw_path == sensitive
            or raw_path.startswith(f"{sensitive}/")
            for sensitive in SENSITIVE_PATHS
        ) and not value.human_approved_sensitive_change:
            reasons.append(f"Sensitive path requires human approval: {raw_path}")

    return GateResult(
        allowed=not reasons,
        reasons=tuple(reasons),
    )
```

OPA should replace this only when policies must be shared across several repositories, languages, services, or enforcement points. Until then, Python offers fewer moving parts and easier unit testing.

### GitHub Actions loop

```yaml
# .github/workflows/agent-loop.yml
name: Agent loop

on:
  workflow_dispatch:
    inputs:
      issue_number:
        description: "Issue number to process; empty selects queued issue"
        required: false
        type: string

  schedule:
    - cron: "17 */6 * * *"
      timezone: "America/Denver"

permissions:
  contents: read
  issues: write
  pull-requests: write

concurrency:
  group: autonomous-agent-loop
  cancel-in-progress: false

jobs:
  agent:
    runs-on: ubuntu-latest
    timeout-minutes: 20

    env:
      AGENT_RUNTIME: github-actions
      ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
      OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
      GEMINI_API_KEY: ${{ secrets.GEMINI_API_KEY }}

      MODEL_PRIMARY: ${{ vars.MODEL_PRIMARY }}
      MODEL_REVIEW: ${{ vars.MODEL_REVIEW }}
      MODEL_LONG: ${{ vars.MODEL_LONG }}
      # Do not set MODEL_CHEAP to Ollama in a hosted runner.
      MODEL_CHEAP: ${{ vars.MODEL_CHEAP_CLOUD }}

      LANGFUSE_PUBLIC_KEY: ${{ secrets.LANGFUSE_PUBLIC_KEY }}
      LANGFUSE_SECRET_KEY: ${{ secrets.LANGFUSE_SECRET_KEY }}
      LANGFUSE_BASE_URL: ${{ vars.LANGFUSE_BASE_URL }}
      LANGFUSE_OTEL_HOST: ${{ vars.LANGFUSE_BASE_URL }}

      MAX_AGENT_ATTEMPTS: "2"
      MAX_RUN_COST_USD: "2.00"
      MIN_EVAL_SCORE: "0.85"

    steps:
      - name: Check out repository
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.12"
          cache: pip

      - name: Install locked dependencies
        run: python -m pip install -r requirements.lock.txt

      - name: Select issue
        id: issue
        shell: bash
        env:
          REQUESTED_ISSUE: ${{ inputs.issue_number }}
          GH_TOKEN: ${{ github.token }}
        run: |
          set -euo pipefail

          if [[ -n "${REQUESTED_ISSUE}" ]]; then
            ISSUE="${REQUESTED_ISSUE}"
          else
            ISSUE="$(
              gh issue list \
                --state open \
                --label "agent:queued" \
                --limit 1 \
                --json number \
                --jq '.[0].number // empty'
            )"
          fi

          if [[ -z "${ISSUE}" ]]; then
            echo "No queued issue"
            echo "found=false" >> "$GITHUB_OUTPUT"
            exit 0
          fi

          echo "found=true" >> "$GITHUB_OUTPUT"
          echo "number=${ISSUE}" >> "$GITHUB_OUTPUT"

      - name: Mark issue running
        if: steps.issue.outputs.found == 'true'
        env:
          GH_TOKEN: ${{ github.token }}
          ISSUE: ${{ steps.issue.outputs.number }}
        run: |
          gh issue edit "$ISSUE" \
            --remove-label "agent:queued" \
            --add-label "agent:running"

      - name: Execute bounded graph
        if: steps.issue.outputs.found == 'true'
        env:
          GH_TOKEN: ${{ github.token }}
          AGENT_ISSUE_NUMBER: ${{ steps.issue.outputs.number }}
        run: |
          python -m agent.run_issue "$AGENT_ISSUE_NUMBER"

      - name: Publish failure state
        if: failure() && steps.issue.outputs.found == 'true'
        env:
          GH_TOKEN: ${{ github.token }}
          ISSUE: ${{ steps.issue.outputs.number }}
        run: |
          gh issue edit "$ISSUE" \
            --remove-label "agent:running" \
            --add-label "agent:failed"

          gh issue comment "$ISSUE" \
            --body "Agent run failed. See workflow run: $GITHUB_SERVER_URL/$GITHUB_REPOSITORY/actions/runs/$GITHUB_RUN_ID"
```

GitHub’s 2026 timezone support allows the `timezone` sibling next to the cron expression. Scheduling at minute 17 rather than minute 0 reduces exposure to the documented top-of-hour queue spike, although it does not create a timing SLA. citeturn13view6turn14search1

For a production repository, pin third-party Actions to reviewed commit SHAs rather than floating tags. Tags are shown above for readability.

### GitHub Issue output

The runtime should write one structured summary rather than dumping entire model transcripts:

```markdown
## Agent run summary

**Run:** `2026-08-02T18:17:03Z-issue-142`
**Status:** Awaiting human review
**Attempts:** 2
**Models:** primary=`…`, review=`…`
**Estimated provider cost:** `$0.84`
**Evaluation score:** `0.91`
**Tests:** Passed
**Policy:** Passed

### Proposed result

Concise description of the generated change.

### Review findings

Concise adversarial review.

### Evidence

- Pull request: #147
- Workflow run: …
- Langfuse trace: …
```

Do not place complete prompts, provider keys, user data, or large generated artifacts in an Issue comment.

### Slack notification

```python
# agent/notify.py
from __future__ import annotations

import os

import httpx


def notify_slack(*, text: str) -> None:
    webhook = os.getenv("SLACK_WEBHOOK_URL")
    if not webhook:
        return

    response = httpx.post(
        webhook,
        json={"text": text},
        timeout=10,
    )
    response.raise_for_status()
```

Only notify on transitions requiring attention:

```text
agent:blocked
agent:failed
agent:approved
cost threshold exceeded
deployment failed
```

### GitHub-native Vercel deployment

Keep deployment in a separate workflow triggered by a protected branch, not directly by the model run.

```yaml
# .github/workflows/deploy.yml
name: Production deploy

on:
  push:
    branches: [main]

permissions:
  contents: read
  deployments: write

jobs:
  deploy:
    runs-on: ubuntu-latest
    environment: production
    timeout-minutes: 15

    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-node@v4
        with:
          node-version: "22"
          cache: npm

      - run: npm ci
      - run: npm test
      - run: npm run build

      - run: npm install --global vercel@latest

      - name: Pull Vercel environment
        run: vercel pull --yes --environment=production --token="$VERCEL_TOKEN"
        env:
          VERCEL_TOKEN: ${{ secrets.VERCEL_TOKEN }}
          VERCEL_ORG_ID: ${{ secrets.VERCEL_ORG_ID }}
          VERCEL_PROJECT_ID: ${{ secrets.VERCEL_PROJECT_ID }}

      - name: Build deployable output
        run: vercel build --prod --token="$VERCEL_TOKEN"
        env:
          VERCEL_TOKEN: ${{ secrets.VERCEL_TOKEN }}
          VERCEL_ORG_ID: ${{ secrets.VERCEL_ORG_ID }}
          VERCEL_PROJECT_ID: ${{ secrets.VERCEL_PROJECT_ID }}

      - name: Deploy production
        run: vercel deploy --prebuilt --prod --token="$VERCEL_TOKEN"
        env:
          VERCEL_TOKEN: ${{ secrets.VERCEL_TOKEN }}
          VERCEL_ORG_ID: ${{ secrets.VERCEL_ORG_ID }}
          VERCEL_PROJECT_ID: ${{ secrets.VERCEL_PROJECT_ID }}
```

Vercel documents both automatic Git deployments and the `pull` → `build` → `deploy --prebuilt` GitHub Actions pattern. citeturn7search2turn7search6turn7search10

## Budget and operational limits

### Cost containment

Set limits at three layers.

**Provider account limits**

Configure hard or alerting budgets at Anthropic, OpenAI, Google, and OpenRouter where available. Do not rely solely on application-side token estimates.

**Per-run limits**

Every graph invocation should have:

```text
maximum wall time
maximum graph transitions
maximum attempts per node
maximum model calls
maximum estimated cost
maximum output tokens
maximum changed files
maximum diff size
```

A sensible starting profile is:

```yaml
limits:
  workflow_timeout_minutes: 20
  graph_transitions: 12
  attempts_per_task: 2
  model_calls: 8
  run_cost_usd: 2.00
  changed_files: 12
  diff_lines: 800
```

**Monthly limits**

At $2 maximum per run, a six-hour schedule could theoretically spend approximately $240 in a 30-day month if every run reached the ceiling. Therefore, the per-run ceiling alone is insufficient. Add a monthly ledger or query Langfuse/provider usage before beginning a run.

A more realistic schedule is:

```text
Four scheduled scans per day
Zero model calls when no issue is queued
One active issue per run
Typical successful run under $0.50
Hard stop at $2
Monthly model budget stop at $70–$80
```

### Security model

Treat issue text, pull-request comments, repository content, retrieved web pages, and model output as **untrusted input**.

The scheduled identity should not possess:

```text
production database credentials
cloud account administrator tokens
package registry publishing credentials
unrestricted shell access to personal machines
permissions to change branch-protection rules
permissions to alter repository secrets
```

Prefer narrowly scoped GitHub permissions:

```yaml
permissions:
  contents: read
  issues: write
  pull-requests: write
```

Only a separate deployment workflow on a protected branch should receive deployment credentials.

Other non-negotiable controls are:

- Never run secret-bearing workflows on untrusted fork pull requests.
- Never interpolate raw Issue text directly into shell commands.
- Validate issue numbers and file paths.
- Block modifications to `.github/workflows`, infrastructure, migrations, and secret-related files without human approval.
- Pin third-party Actions and review dependency updates.
- Require a human review for destructive tools or data changes.
- Make every external side effect idempotent.
- Use a unique run ID in Issue comments and trace metadata.
- Record which concrete model produced each output.
- Keep generated patches on a branch; do not let the agent push directly to `main`.

The 2026 Cline package incident is a practical reminder that coding-agent and extension supply chains have direct access to valuable credentials and source code. citeturn1search6

### Failure containment

| Failure | Expected response |
|---|---|
| Provider unavailable | LiteLLM retries once, then moves to an explicitly configured fallback |
| Reviewer disagrees | One bounded revision; then mark Issue blocked |
| GitHub schedule delayed | Next run scans for stale `agent:queued` and `agent:running` labels |
| Duplicate workflow | Concurrency group plus issue-level run identifier prevents duplicate side effects |
| Langfuse unavailable | Application continues, but run is marked telemetry-degraded; never silently treat it as fully observed |
| Cost estimate exceeds ceiling | Stop before the next model call and mark blocked |
| Tests fail | No PR approval and no deployment |
| Issue contains prompt injection | Treat it as task data; system instructions and tool policy remain fixed in code |
| Hosted runner cannot reach Ollama | Use a hosted model or run the graph locally; do not expose the laptop ad hoc |
| Slack fails | Preserve state in the Issue and continue; Slack is non-authoritative |
| GitHub API update conflicts | Re-fetch issue state, verify run ID, and retry only an idempotent update |

GitHub itself warns that scheduled events may be delayed or dropped under load. Consequently, stale-state reconciliation is mandatory: each run should detect an `agent:running` issue whose heartbeat is older than the workflow timeout and move it to `agent:failed` or safely resume it. citeturn14search0turn14search1

### Migration from a custom swarm

The pivot should remove abstractions rather than wrap them.

| Custom-swarm concept | Standard-harness replacement |
|---|---|
| Agent registry | LangGraph node functions |
| Message bus | Typed graph state |
| Shared agent memory | GitHub Issue plus explicit persisted artifacts |
| Custom provider clients | LiteLLM |
| Custom trace database | Langfuse |
| Homegrown scheduler | GitHub Actions |
| Agent status dashboard | Issue labels, Actions runs, Langfuse dashboards |
| Informal approval prompt | Deterministic policy gate |
| Autonomous production write | Protected PR and deployment workflow |
| Agent-to-agent chat transcript | Structured node input/output and review result |

Do not migrate all agents one-for-one. Collapse them into the smallest operational graph:

```text
planner
worker
reviewer
deterministic gate
```

Add a separate specialist only when measurements show a specific node cannot reliably perform the task.

## Case-study evidence and final recommendation

### The requested exact-stack case study is not publicly verifiable

I did **not** find a credible public 2026 case that proves all of the following simultaneously:

- one identifiable solo developer;
- Aider as the coding interface;
- LangGraph as the production orchestrator;
- LiteLLM as the live multi-provider router;
- Langfuse as the trace/evaluation system;
- GitHub Actions and Issues as scheduler and shared state;
- a successfully deployed production web application;
- enough public artifacts to independently verify those claims.

Claiming such a case would require inventing evidence.

The absence is understandable. Aider is normally a private local development tool and does not leave a required runtime fingerprint. API keys, Langfuse projects, GitHub Actions secrets, and production deployment histories are commonly private. A public repository may prove LangGraph imports, LiteLLM calls, and workflow YAML but still cannot prove that Aider was used or that the system operated successfully in production.

The strongest available component-level evidence is:

- Aider is an active Git-native coding tool with substantial published usage and provider support. citeturn12view0
- LangGraph is an active MIT-licensed orchestration framework designed for explicit agent workflows. citeturn12view5
- LiteLLM officially supports one interface across Anthropic, OpenAI, Google/Vertex, Ollama, and other providers. citeturn12view6
- Langfuse officially documents both LangGraph evaluations and LiteLLM SDK/proxy telemetry. citeturn6search2turn15search5turn15search12
- GitHub officially supports scheduled Issues workflows, timezone-aware cron schedules, repository-scoped permissions, and sufficient free Actions capacity for a small agent loop. citeturn14search2turn13view4turn13view6
- Vercel and Cloudflare officially support GitHub-driven preview and production deployments. citeturn7search2turn7search1

The closest real solo-developer evidence found was **Constellagent**, a publicly described solo-built multi-agent orchestration project using cron-style automation. It supports the feasibility of one operator maintaining scheduled multi-agent behavior, but it does **not** use or validate the exact recommended stack and should not be represented as doing so. citeturn8search0

### Verification-grade pilot

Before replacing the custom swarm, the exact stack should pass this small production pilot:

1. A GitHub Issue labeled `agent:queued` requests a bounded documentation or low-risk code change.
2. A timezone-aware GitHub Action picks it up at minute 17 of a scheduled interval.
3. LangGraph runs one planner, one worker, and one reviewer, with no more than two attempts.
4. LiteLLM sends the primary call to Anthropic and the review call to OpenAI or Google.
5. Langfuse records one coherent trace containing both provider calls, graph-node spans, issue number, token use, latency, and evaluation score.
6. The policy gate rejects an intentionally failing test and accepts a passing fixture.
7. The run creates a branch and pull request, not a direct production commit.
8. GitHub branch protection requires tests and evaluation status.
9. Merging the pull request triggers a GitHub-native Vercel or Cloudflare deployment.
10. The Issue receives a concise result comment and transitions to `agent:done`.
11. A Slack webhook emits only the completion or failure notification.
12. Re-running the same workflow does not create duplicate comments, pull requests, or deployments.

That pilot is the evidence threshold the existing custom swarm should have to beat.

### Final choice

**Adopt:**

- **Aider** for local coding.
- **LangGraph** for the runtime graph.
- **LiteLLM SDK** for provider abstraction.
- **Langfuse Cloud** for traces and evaluations.
- **GitHub Actions plus Issues** for scheduling, shared state, policy execution, pull requests, and deployment control.

**Keep optional:**

- **OpenRouter** as an emergency provider aggregator or access path to models for which direct accounts are inconvenient.
- **Slack Incoming Webhooks** for alerts.
- **Vercel** for Next.js/full-stack web applications.
- **Cloudflare Pages/Workers** for static or edge-oriented applications.
- **Ollama** for local development and manual low-cost runs.
- **DSPy** later, once a real evaluation dataset exists and prompt optimization becomes a measured bottleneck.

**Do not adopt now:**

- AutoGen, because it is in maintenance mode.
- Continue.dev, because it has joined Cursor and is not a stable greenfield foundation.
- Temporal Cloud, because its current minimum price consumes the entire monthly cloud budget.
- OPA, until policy must be reused across several independently deployed systems.
- Self-hosted Langfuse or LiteLLM Proxy, until traffic, multiple users, or centralized API-key management justify persistent infrastructure.
- A free-form swarm that can recursively delegate, rewrite its control logic, or deploy without deterministic gates.

The core design principle is not “multiple agents.” It is **one inspectable workflow, several replaceable model roles, one canonical task ledger, and one deterministic authority boundary**.
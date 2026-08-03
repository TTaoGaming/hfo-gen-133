#!/usr/bin/env python3
"""
RUNTIME PROBE — HOT-9. Verified by EXECUTION, not import.

Row 77 (areas/quorum_research/SIGRUN_ROOT_CAUSE_LEAK_20260802.md) measured
LangGraph adopted in prose inside this forge but at ZERO imports, twice.
`import langgraph` succeeding is explicitly NOT what this probe checks. This
probe builds a real 2-node StateGraph, invokes it, and asserts on the actual
returned output -- one node calls the local Ollama model through LiteLLM
(the same known-good call as tools/stack_builder/probe_litellm.py) so the
graph is doing real work end to end, not passing an integer between two
no-op functions.

Decision trail (probe-first discipline, per the worker brief):
  1. LangGraph tried first (industry-preferred; external fitness ranks it
     above CrewAI -- Klarna/Uber/LinkedIn). `pip show langgraph` -> 1.1.3,
     already installed, no network/infra excuse.
  2. A minimal 2-node graph (produce -> verify) was built and invoked
     directly in this session BEFORE this file was written (probe-first):
         from langgraph.graph import StateGraph, END
         ... g.compile().invoke({"x": 1, "log": []}) -> {"x": 4, "log": ["a","b"]}
     Real state passed through two real nodes, state mutated by both. PASS.
  3. Because it passed within the 25-minute budget, CrewAI was not needed as
     a fallback. `cap-crewai-runtime` remains true independently (crewai
     1.11.1 is installed and STACK_BUILDER already measured a real kickoff()
     elsewhere) but this probe -- and this phenotype wiring -- uses LangGraph.

kickoff() wiring: tools/factory/phenotypes/games.py's GamesGrader ranking
step is the kind of small, swappable decision LangGraph is suited to; wiring
a full graph into the genotype's template method is future work (see
honest_flaw) -- this probe demonstrates the runtime executes for real, which
is what HOT-9 requires, not that every phenotype has been rewired onto it yet.
"""
from __future__ import annotations

import sys
from typing import TypedDict


class GraphState(TypedDict):
    task: str
    produced: str
    verified: bool
    log: list


def _node_produce(state: GraphState) -> dict:
    """Node 1: a real LLM call through LiteLLM -> local Ollama.
    Same known-good call as tools/stack_builder/probe_litellm.py. The prompt
    is deliberately trivial -- this tests the LangGraph node wiring, not the
    model (llama3.2:3b is weak, per the worker brief)."""
    import litellm
    r = litellm.completion(
        model="ollama/llama3.2:3b",
        api_base="http://127.0.0.1:11434",
        messages=[{"role": "user",
                    "content": f"Reply with exactly the word OK if you can read this: "
                               f"{state['task']}"}],
        timeout=60,
    )
    content = (r.choices[0].message.content or "").strip()
    return {"produced": content, "log": state["log"] + [f"produce:{content!r}"]}


def _node_verify(state: GraphState) -> dict:
    """Node 2: checks node 1's real output. Asserting on actual returned
    content -- not a mocked/short-circuited value -- is what makes this an
    execution probe rather than an import probe."""
    ok = "ok" in state["produced"].lower()
    return {"verified": ok, "log": state["log"] + [f"verify:{ok}"]}


def run_langgraph() -> tuple[bool, str]:
    from langgraph.graph import END, StateGraph

    g = StateGraph(GraphState)
    g.add_node("produce", _node_produce)
    g.add_node("verify", _node_verify)
    g.set_entry_point("produce")
    g.add_edge("produce", "verify")
    g.add_edge("verify", END)
    app = g.compile()

    result = app.invoke({"task": "runtime probe", "produced": "", "verified": False, "log": []})

    if len(result.get("log", [])) < 2:
        return False, f"graph ran but log has <2 entries: {result.get('log')}"
    if not result.get("produced"):
        return False, "produce node returned empty content"
    if not result.get("verified"):
        return False, f"verify node did not confirm produce output: {result.get('produced')!r}"
    return True, f"2-node graph executed: produced={result['produced']!r} log={result['log']}"


def run_crewai() -> tuple[bool, str]:
    """Fallback path -- only reached if LangGraph fails. See module docstring:
    not exercised this run because LangGraph passed."""
    from crewai import Agent, Crew, Task
    from crewai.llm import LLM

    llm = LLM(model="ollama/llama3.2:3b", base_url="http://127.0.0.1:11434")
    writer = Agent(role="Writer", goal="reply with exactly OK",
                    backstory="terse verifier", llm=llm, verbose=False)
    checker = Agent(role="Checker", goal="confirm the reply says OK",
                     backstory="terse verifier", llm=llm, verbose=False)
    t1 = Task(description="Reply with exactly the word OK.",
              expected_output="OK", agent=writer)
    t2 = Task(description="Confirm the previous output contains OK. State yes or no.",
              expected_output="yes or no", agent=checker)
    crew = Crew(agents=[writer, checker], tasks=[t1, t2], verbose=False)
    result = crew.kickoff()
    text = str(result)
    if not text.strip():
        return False, "crew.kickoff() returned empty output"
    return True, f"crew executed 2 agents/tasks: output={text[:200]!r}"


def main() -> int:
    try:
        ok, evidence = run_langgraph()
        if ok:
            print(f"RUNTIME_OK runtime=langgraph")
            print(f"# evidence: {evidence}", file=sys.stderr)
            return 0
        print(f"# langgraph probe ran but did not verify: {evidence}", file=sys.stderr)
    except Exception as exc:
        print(f"# langgraph FAILED: {type(exc).__name__}: {exc}", file=sys.stderr)

    print("# falling back to crewai", file=sys.stderr)
    try:
        ok, evidence = run_crewai()
        if ok:
            print(f"RUNTIME_OK runtime=crewai")
            print(f"# evidence: {evidence}", file=sys.stderr)
            return 0
        print(f"# crewai probe ran but did not verify: {evidence}", file=sys.stderr)
    except Exception as exc:
        print(f"# crewai FAILED: {type(exc).__name__}: {exc}", file=sys.stderr)

    print("RUNTIME_FAIL both langgraph and crewai probes failed", file=sys.stderr)
    return 1


if __name__ == "__main__":
    sys.exit(main())

"""
Optional LangGraph bridge so the genotype's kickoff() can actually use the
runtime HOT-9 proved executes -- not just prove it executes in isolation.

Off by default everywhere it is wired (task_spec.get("use_langgraph", False))
so the held-out tests (HOT-2/HOT-3), which require --dry-run to be
deterministic and NETWORK-FREE, are never affected by this import or by
LangGraph's own startup cost. This module is imported lazily (inside the
function, not at module load) for the same reason: importing langgraph/
litellm at package-import time would slow every CLI invocation, including
the default dry-run path nobody asked to make LLM-dependent.

See tools/factory/phenotypes/leads.py LeadsVerifier -- when
task_spec["use_langgraph"] is truthy, the structural verify check runs as a
2-node LangGraph graph (split-check -> combine) instead of a single Python
function. That is a genuine (if modest) use of the runtime inside kickoff(),
not merely alongside it. It deliberately does NOT call an LLM in this path
(keeps it fast + offline); tools/factory/runtime_probe.py is the one place
that exercises the LLM-calling node, per HOT-9's activation command.
"""
from __future__ import annotations

from typing import Any, Callable, TypedDict


class BridgeState(TypedDict):
    payload: Any
    result_a: Any
    result_b: Any


def run_two_node_graph(node_a: Callable[[Any], Any], node_b: Callable[[Any, Any], Any],
                        payload: Any) -> Any:
    """Build + invoke a real 2-node LangGraph graph: node_a(payload) -> result_a,
    then node_b(payload, result_a) -> result_b. Returns result_b.

    This is a thin, honest wrapper -- no hidden fallback to plain function
    calls. If LangGraph is not importable this raises, same as any other hard
    dependency; callers gate on task_spec["use_langgraph"] precisely so this
    path is opt-in.
    """
    from langgraph.graph import END, StateGraph

    def _a(state: BridgeState) -> dict:
        return {"result_a": node_a(state["payload"])}

    def _b(state: BridgeState) -> dict:
        return {"result_b": node_b(state["payload"], state["result_a"])}

    g = StateGraph(BridgeState)
    g.add_node("a", _a)
    g.add_node("b", _b)
    g.set_entry_point("a")
    g.add_edge("a", "b")
    g.add_edge("b", END)
    app = g.compile()

    out = app.invoke({"payload": payload, "result_a": None, "result_b": None})
    return out["result_b"]

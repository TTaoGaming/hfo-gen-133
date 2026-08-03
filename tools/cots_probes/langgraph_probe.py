#!/usr/bin/env python3
"""Behavioral probe: real langgraph StateGraph, compiled and invoked.

Builds a genuine two-node StateGraph, compiles it, and invokes it with a
real input. Asserts on the OUTPUT STATE content -- both nodes must have
appended their marker to the shared state, proving the graph actually
executed both nodes in order, not merely that `from langgraph.graph import
StateGraph` parsed.

If langgraph is not importable, this probe attempts
`python -m pip install --user langgraph` once, then re-checks. If it still
cannot be made to work, it exits non-zero with the real error -- no faking.
"""
import subprocess
import sys


def _ensure_langgraph():
    try:
        import langgraph  # noqa: F401
        return True
    except ImportError:
        print("langgraph not importable -- attempting pip install --user langgraph")
        r = subprocess.run(
            [sys.executable, "-m", "pip", "install", "--user", "langgraph"],
            capture_output=True, text=True, timeout=300,
        )
        print(f"INSTALL_EXIT={r.returncode}")
        if r.returncode != 0:
            print(r.stdout[-2000:])
            print(r.stderr[-2000:])
            return False
        try:
            import langgraph  # noqa: F401
            return True
        except ImportError as e:
            print(f"still not importable after install: {e}")
            return False


def main() -> int:
    if not _ensure_langgraph():
        print("PROBE_PASS=False")
        print("REASON=langgraph could not be installed/imported")
        return 1

    try:
        from typing import TypedDict
        from langgraph.graph import StateGraph, END
    except Exception as e:
        print(f"IMPORT_ERROR: {type(e).__name__}: {e}")
        print("PROBE_PASS=False")
        return 1

    class GraphState(TypedDict):
        trail: str

    def node_a(state: GraphState) -> GraphState:
        return {"trail": state["trail"] + "|A_VISITED"}

    def node_b(state: GraphState) -> GraphState:
        return {"trail": state["trail"] + "|B_VISITED"}

    try:
        builder = StateGraph(GraphState)
        builder.add_node("node_a", node_a)
        builder.add_node("node_b", node_b)
        builder.set_entry_point("node_a")
        builder.add_edge("node_a", "node_b")
        builder.add_edge("node_b", END)
        graph = builder.compile()

        result = graph.invoke({"trail": "START"})
    except Exception as e:
        print(f"RUNTIME_ERROR: {type(e).__name__}: {e}")
        print("PROBE_PASS=False")
        return 1

    trail = result.get("trail", "")
    print(f"OUTPUT_STATE: {result!r}")

    ok = "A_VISITED" in trail and "B_VISITED" in trail and trail.index("A_VISITED") < trail.index("B_VISITED")
    print(f"PROBE_PASS={ok}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())

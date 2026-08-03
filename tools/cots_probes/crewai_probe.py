#!/usr/bin/env python3
"""Behavioral probe: real 2-agent CrewAI crew, kickoff(), non-empty output.

Uses the local Ollama model via litellm's `ollama/` provider so it needs no
API key and costs $0. Kept deliberately tiny (short task descriptions, low
max_iter) because CrewAI + a small local model can be slow. If this exceeds
its own internal timeout budget, it exits non-zero with a TIMEOUT reason
rather than hanging past the held-out suite's 420s-per-probe ceiling.
"""
import sys
import threading

TIMEOUT_S = 300  # leave headroom under the holdout's 420s ceiling


def _run_crew(result_box: dict) -> None:
    try:
        from crewai import Agent, Crew, Task, LLM

        llm = LLM(model="ollama/llama3.2:3b", base_url="http://127.0.0.1:11434")

        researcher = Agent(
            role="Researcher",
            goal="State one concrete fact about durable execution engines",
            backstory="A terse infrastructure researcher who never pads answers.",
            llm=llm,
            verbose=False,
            max_iter=2,
        )
        writer = Agent(
            role="Writer",
            goal="Compress the researcher's fact into one plain sentence",
            backstory="A blunt technical writer, no marketing language.",
            llm=llm,
            verbose=False,
            max_iter=2,
        )

        research_task = Task(
            description="Name one durable execution engine and one fact about it, in under 20 words.",
            expected_output="One short sentence naming an engine and a fact.",
            agent=researcher,
        )
        write_task = Task(
            description="Rewrite the researcher's sentence to be under 12 words, plain English.",
            expected_output="One short sentence, under 12 words.",
            agent=writer,
            context=[research_task],
        )

        crew = Crew(agents=[researcher, writer], tasks=[research_task, write_task], verbose=False)
        result = crew.kickoff()
        result_box["output"] = str(result)
    except Exception as e:
        result_box["error"] = f"{type(e).__name__}: {e}"


def main() -> int:
    result_box: dict = {}
    t = threading.Thread(target=_run_crew, args=(result_box,), daemon=True)
    t.start()
    t.join(timeout=TIMEOUT_S)

    if t.is_alive():
        print(f"REASON=TIMEOUT after {TIMEOUT_S}s -- crew did not finish kickoff()")
        print("PROBE_PASS=False")
        return 1

    if "error" in result_box:
        print(f"RUNTIME_ERROR: {result_box['error']}")
        print("PROBE_PASS=False")
        return 1

    output = result_box.get("output", "")
    print(f"CREW_OUTPUT={output!r}")
    ok = len(output.strip()) > 0
    print(f"PROBE_PASS={ok}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())

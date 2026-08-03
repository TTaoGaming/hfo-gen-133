#!/usr/bin/env python3
"""Runtime probe: 2-agent CrewAI crew, kickoff(), real non-empty output.

Backed by local Ollama via litellm so it costs $0 and needs no API key.
This is the falsifier for cap-crewai-runtime: Sigrun pre-registered this DEAD
and said it only flips ALIVE if `from crewai import` appears AND a real
kickoff() produces output -- not merely that the import succeeds.
"""
import sys

from crewai import Agent, Crew, Task, LLM


def main() -> int:
    llm = LLM(model="ollama/llama3.2:3b", base_url="http://127.0.0.1:11434")

    researcher = Agent(
        role="Researcher",
        goal="State one concrete fact about durable execution engines",
        backstory="A terse infrastructure researcher who never pads answers.",
        llm=llm,
        verbose=False,
    )
    writer = Agent(
        role="Writer",
        goal="Compress the researcher's fact into one plain sentence",
        backstory="A blunt technical writer, no marketing language.",
        llm=llm,
        verbose=False,
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

    output = str(result)
    print(f"CREW_OUTPUT={output!r}")
    ok = len(output.strip()) > 0
    print(f"PROBE_PASS={ok}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())

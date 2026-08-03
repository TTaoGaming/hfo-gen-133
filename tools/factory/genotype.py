"""
GENOTYPE — textbook GoF Abstract Factory (gen-133, EMERGENCY_FORGE 2026-08-02).

Operator's vision, verbatim: "1 genotype with many phenotypes creating many
different effects." This module IS the genotype. Everything phenotype-specific
(leads, games, and whatever comes next -- email, grant, indie-SaaS) lives one
level down in tools/factory/phenotypes/ and customizes ONLY the four products
below. It must never override kickoff().

    AbstractFactory              the genotype
      create_producer()  -> Producer          generates variants
      create_grader()    -> Grader            ranks them
      create_verifier()  -> Verifier          runs an EXTERNAL-fitness probe
      create_memory_writer() -> MemoryWriter  persists
      kickoff(task_spec) -> Result            TEMPLATE METHOD: the only place
                                               the pipeline order lives

Why this shape and not a new one: the existing tools/factory/{core,fit,grade,
generate,emit}.py pipeline is a proven set of pure functions (see core.py's own
docstring: "stdlib only, no LangGraph/CrewAI, the pipeline is five pure
functions over dataclasses"). This module does not replace that pipeline; it
gives it a GoF Abstract Factory *shape* so a new phenotype (email, grant,
indie-SaaS) is cheap to add -- subclass AbstractFactory, write four small
adapter classes that wrap existing pure functions, done. If a phenotype ever
needs to override kickoff(), that is a signal the genotype is wrong here, not
that the phenotype has a special case.
"""
from __future__ import annotations

import abc
import dataclasses
from typing import Any


# ---------------------------------------------------------------------------
# ABSTRACT PRODUCTS
# ---------------------------------------------------------------------------
class Producer(abc.ABC):
    """Generates candidate variants for a task_spec. The market-specific part."""

    @abc.abstractmethod
    def produce(self, task_spec: dict) -> list[Any]:
        """-> list of phenotype-specific items (e.g. LeadRecord, GamePlan)."""
        raise NotImplementedError


class Grader(abc.ABC):
    """Ranks the variants a Producer made. Market-specific rubric."""

    @abc.abstractmethod
    def grade(self, task_spec: dict, variants: list[Any]) -> list["GradedItem"]:
        raise NotImplementedError


class Verifier(abc.ABC):
    """Runs an EXTERNAL-fitness probe against the graded variants.

    "External" means: does the world (not this process) corroborate the
    claim? A verifier that only re-checks the producer's own output is not a
    verifier, it is the producer grading its own homework -- the exact defect
    row 77 (areas/quorum_research/SIGRUN_ROOT_CAUSE_LEAK_20260802.md) names.
    """

    @abc.abstractmethod
    def verify(self, task_spec: dict, graded: list["GradedItem"]) -> "VerifyResult":
        raise NotImplementedError


class MemoryWriter(abc.ABC):
    """Persists the kickoff() result to durable storage under a namespace."""

    @abc.abstractmethod
    def write(self, task_spec: dict, result: "Result") -> str:
        """-> path or id of what was written."""
        raise NotImplementedError


# ---------------------------------------------------------------------------
# SHARED VALUE OBJECTS
# ---------------------------------------------------------------------------
@dataclasses.dataclass
class GradedItem:
    item: Any
    score: float
    rank: int = 0
    reason: str = ""


@dataclasses.dataclass
class VerifyResult:
    ok: bool
    evidence: str
    checked: int = 0
    details: dict = dataclasses.field(default_factory=dict)


@dataclasses.dataclass
class Result:
    task_spec: dict
    variants: list[Any]
    graded: list[GradedItem]
    verify: VerifyResult
    persisted_path: str = ""
    factory: str = ""


# ---------------------------------------------------------------------------
# THE GENOTYPE
# ---------------------------------------------------------------------------
class AbstractFactory(abc.ABC):
    """One genotype: produce -> grade -> verify -> persist.

    kickoff() is a TEMPLATE METHOD (GoF): it is the ONLY place the pipeline
    order lives. A phenotype subclass customizes what create_producer() /
    create_grader() / create_verifier() / create_memory_writer() RETURN --
    never the order kickoff() calls them in. That is the "one genotype, many
    phenotypes, many effects" claim: the next market lane (email, grant,
    indie-SaaS) gets the whole pipeline for free by implementing four small
    classes, not by re-deriving the orchestration.
    """

    #: Overridable by a phenotype constructor; used by kickoff()'s log line and
    #: by memory writers as a default namespace. Not a pipeline step.
    name: str = "abstract"

    @abc.abstractmethod
    def create_producer(self) -> Producer:
        raise NotImplementedError

    @abc.abstractmethod
    def create_grader(self) -> Grader:
        raise NotImplementedError

    @abc.abstractmethod
    def create_verifier(self) -> Verifier:
        raise NotImplementedError

    @abc.abstractmethod
    def create_memory_writer(self) -> MemoryWriter:
        raise NotImplementedError

    def kickoff(self, task_spec: dict) -> Result:
        """produce -> grade -> verify -> persist. DO NOT OVERRIDE in a phenotype."""
        producer = self.create_producer()
        grader = self.create_grader()
        verifier = self.create_verifier()
        writer = self.create_memory_writer()

        variants = producer.produce(task_spec)
        graded = grader.grade(task_spec, variants)
        verify_result = verifier.verify(task_spec, graded)

        result = Result(
            task_spec=task_spec,
            variants=variants,
            graded=graded,
            verify=verify_result,
            factory=type(self).__name__,
        )
        result.persisted_path = writer.write(task_spec, result)
        return result

"""HFO gen-133 distribution-artifact factory.

One genotype (tools.factory.genotype.AbstractFactory), many phenotypes.
Importing this package registers every phenotype on
AbstractFactory.__subclasses__() -- HOT-1 relies on that.
"""
__version__ = "0.1.0"

from .phenotypes.leads import LeadsFactory
from .phenotypes.games import GamesFactory

__all__ = ["LeadsFactory", "GamesFactory"]

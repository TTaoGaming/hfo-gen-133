"""Adapter registry. Add a platform by adding one class and one line here."""
from __future__ import annotations

from .base import OpportunityAdapter
from .boards import (ArbeitnowAdapter, HimalayasAdapter, JobicyAdapter,
                     RemoteOKAdapter, WeWorkRemotelyAdapter)
from .games import GamePortalsAdapter, ItchJamsAdapter
from .grants import GrantsGovAdapter
from .hn_contracts import HNContractsAdapter
from .operator_cached import OperatorCachedAdapter, write_seed

REGISTRY: dict[str, type[OpportunityAdapter]] = {
    "hn_contracts": HNContractsAdapter,        # M1 contracts  (canon rank 1)
    "linkedin_cached": OperatorCachedAdapter,  # M1 warm       (needs operator input)
    "remoteok": RemoteOKAdapter,               # M2 employment (canon counterweight, P=0.60)
    "arbeitnow": ArbeitnowAdapter,             # M2
    "himalayas": HimalayasAdapter,             # M2
    "jobicy": JobicyAdapter,                   # M2
    "weworkremotely": WeWorkRemotelyAdapter,   # M2
    "grants_gov": GrantsGovAdapter,            # M6 grants (SBIR is down)
    "game_portals": GamePortalsAdapter,        # M5 portals (canon rank 2)
    "itch_jams": ItchJamsAdapter,              # M5 jams -- audience, not income
}

DEFAULT_ADAPTERS = list(REGISTRY)

__all__ = ["REGISTRY", "DEFAULT_ADAPTERS", "OpportunityAdapter", "write_seed"]

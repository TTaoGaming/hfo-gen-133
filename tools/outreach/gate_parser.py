"""Superseded by tools/olrun/approvals_parser.py.

An earlier revision of this file (written 2026-08-02 before the executor spotted
the parallel work) reimplemented gate parsing. The canonical implementation is
tools/olrun/approvals_parser.py — see its docstring for the full CLASS/INSTANCE/REJECT
line grammar. This shim re-exports the public symbols so existing imports don't
break.
"""

from tools.olrun.approvals_parser import (  # noqa: F401
    CLASS_TO_MARKET,
    GateLine,
    load_index,
    parse_gate_file,
    resolve,
)

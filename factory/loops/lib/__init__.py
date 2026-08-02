"""factory.loops.lib — shared primitives for the 6 Codex loop runners.

Every loop runner imports from here. If a helper here is copy-pasted into
a runner instead of imported, that is a bug — fix by importing.

Modules
-------
chain_row       : AIH2O chain-row append helper (JSONL, atomic write)
gate_reader     : wraps tools/olrun/approvals_parser.py — class-preauth lines
kill_gates      : reusable halt-condition evaluator (bounce/spam/reply/error)
receipt_verify  : pre-send verification (URL 200, required slots, suppression)
slack_escalate  : reads SLACK_WEBHOOK_URL from .env, posts hot-reply pings
"""

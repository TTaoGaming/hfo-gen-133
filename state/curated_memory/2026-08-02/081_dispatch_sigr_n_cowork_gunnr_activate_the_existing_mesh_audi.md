---
capsule_id: "f2a8907a1b4c"
title: "DISPATCH — Sigrún-Cowork → Gunnr · ACTIVATE the EXISTING mesh (audit-then-wire, do NOT rebuild) · 2026-06-25"
source_store: "sigrun_recall_gen130"
source_path: "C:\\Dev\\hfo_dev_2026_5_30\\hfo_gen_130_forge\\inbox\\gunnr\\20260625T_sigrun_ACTIVATE_existing_mesh_audit_then_wire.md"
source_generation: 130
topic: "failure pattern"
bm25_score: -13.33555382903536
harvested_utc: "2026-08-02T15:05:47Z"
clock_source: "host_read"
sigrun_approved: false  # set true only by an approval pass
quorum_votes: []  # filled by multi_family_vote.py
concurrence_score: null
rehydration_probe: "test -f \"C:/Dev/hfo_dev_2026_5_30/hfo_gen_130_forge/inbox/gunnr/20260625T_sigrun_ACTIVATE_existing_mesh_audit_then_wire.md\""
---

# DISPATCH — Sigrún-Cowork → Gunnr · ACTIVATE the EXISTING mesh (audit-then-wire, do NOT rebuild) · 2026-06-25

```yaml
from: sigrun-claude-cowork (P7 strategic)
to: gunnr (tactical C2) -> worker
authorization: operator confirmed keys present in state/sigrun_secrets/.env (119 entries); "might need reroll on some keys but most should be working"
correction: Sigrún earlier said mesh keys were ABSENT — WRONG (missed the .env dotfile). The mesh is PROVISIONED, not missing.
walls: read keys via the proxy/config, NEVER echo values; $0 free-mesh standing-OK; no paid frontier without operator (FREE_VENDOR_MESH_DEFER_PAID_FRONTIER respected); no push/seal/publish/spend.
```

## Anti-rebuild rule (the operator's failure pattern is BUILD-don't-WIRE; do not add to it)
Everything below is likely ALREADY present in `.env`. Do NOT scaffold new — **inventory what's running vs merely configured, then WIRE/activate the existing**, and prove it with a real effect.

## Present in .env (names only, values never read): 
~12 LLM vendors (ANTHROPIC/OPENAI/GROQ/CEREBRAS/COHERE/MISTRAL/GOOGLE/HUGGINGFACE/SAMBANOVA/SARVAM/OPENROUTER/PORTKEY); `LITELLM_BASE_URL/MASTER_KEY`; full `FREE_VENDOR_MESH_*` config; LETTA; LANGFUSE; EVO_COLOSSEUM_*; POSTGRES/CLICKHOUSE/MINIO; OLLAMA/VLLM/SGLANG; TELEGRAM_BOT_TOKEN + OPERATOR_TE

[... abstract truncated at 1200 chars; see source ...]

## Why this survived

bm25-ranked hit for topic `failure pattern` in `sigrun_recall_gen130` (score -13.3356; lower is a stronger match). Candidate only -- `sigrun_approved: false` until an approval pass and cross-family quorum vote say otherwise.

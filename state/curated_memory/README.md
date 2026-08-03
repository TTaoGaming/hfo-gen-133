# state/curated_memory/

Sigrún-approved memory capsules brought forward from heritage mining or other sources.

## How this directory populates

1. Codex LOOP 3 (heritage miner) stages capsules to `state/heritage_mining/` with `sigrun_approved: false`
2. Sigrún runs a curation pass (via canon session send_message)
3. Approved capsules get COPIED (not moved) here with `sigrun_approved: true` in metadata
4. Codex LOOP D3 (daily audience drafter) reads from THIS directory for talking points

## Current status

- Heritage staging batch: `state/heritage_mining/STAGING_MANIFEST_20260802.md` (40 capsules awaiting Sigrún approval)
- Approved-in-this-directory: 0 (Sigrún approval pass pending)
- Curated capsule files: (none yet)

## Bootstrap for D3 gracefully-degrade mode

If D3 fires and this directory is empty, D3 should use ONE of:
- `state/heritage_mining/` content directly (with `sigrun_approved: false` disclaimer in the draft)
- Chain rows from `chains/SIGRUN_P4.jsonl` tail as talking points
- Live HFO factory receipts (12 Suika DLCs deployed, 150 drafts staged, etc)

D3 must NOT halt just because this dir is empty — degrade gracefully using available signals.

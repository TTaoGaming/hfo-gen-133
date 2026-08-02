# notes — games batch, 2026-08-02

All 21 `portal_candidates` titles from `state/factory_input/omega_games_portal_shortlist.json`
got a manifest. None were skipped for unclear mechanics — the source
`omega_games/game_registry.json` has a factual one-line description and an
explicit `input` array for every title in the shortlist, so every
`long_description` is built from that registry text plus the file's own
control scheme, not invented.

## Missing thumbnails (all 21)

No cover images or screenshots exist for any of the 21 titles. Every
manifest has `cover_image_path: "MISSING_NEEDS_SCREENSHOT"` and an empty
`screenshots` array. Two ways to close this, operator's call:

1. Open each `index.html` locally (`file://` is fine, they're self-contained,
   zero network calls) and take a manual screenshot per title — 21 screenshots,
   itch.io wants at least a cover image (630x500 recommended) plus 1+
   in-game screenshot.
2. Use a plain placeholder cover (e.g. title text on a flat color card) for
   the first draft pass, swap in real screenshots after the first upload —
   itch.io lets you edit a draft's images without republishing.

## Genre calls (not in source data, judgment calls)

The registry doesn't carry a `genre` field, so genre in each manifest was
assigned from the `desc`/`tags` fields already in the registry:
puzzle-logic games (hex_flip, ice_slide, magnetic_orbs, match3, maze_runner,
memory_match, number_crush, pipe_puzzle, slide_puzzle, tic_tac_toe) →
`puzzle`; reflex/movement games (infinite_runner, light_trail,
platformer_hop, snake, snake_neon, tower_drop) → `action`; aim-based games
(slingshot, target_aim) → `shooter`; the rest (paint_blast, reaction_test,
rhythm_tap) → `other`. These are reasonable but not registry-sourced —
worth a five-minute operator sanity check before bulk-submitting.

## Tags — no gesture/webcam claims

The Task 2 spec example listed tags like `webcam`, `gesture`,
`hand-tracking`. Checked: none of these 21 `index.html` files reference
`getUserMedia`, MediaPipe, or any camera/gesture code (the one grep hit,
`platformer_hop`, was a `// scroll camera` code comment, not a webcam
feature). Those tags were left off every manifest — adding them would have
been a fabricated feature claim per the brief's own instruction not to
invent mechanics. If a future build wires in the `spatial_input_bridge.js`
gesture layer referenced elsewhere in the omega_games repo, tags can be
added then.

## html_file paths point outside this repo

The actual game source lives at
`C:\Dev\hfo_dev_2026_3\omega_games\{slug}\index.html` — a different git repo
(`hfo_dev_2026_3`, branch `gen100_migration`), not under
`C:\Dev\hfo_gen_133_forge`. `html_file` in each manifest is an absolute path
into that repo. Before uploading, either zip that single `index.html` per
title as-is, or copy it into this repo first if you want the upload source
tracked alongside the manifest.

## Patch commit did not land (receipt gap)

Task 1's fix (strip `X-Frame-Options`) is applied and `git add`-staged in
the `omega_games` repo, but `git commit` failed there — a pre-commit hook
(`nidhogg_pre_commit.py`) references a path that doesn't exist in that repo
checkout (`hfo_gen_100_forge/1_alpha/hfo_core/nidhogg_pre_commit.py`), so
the commit is blocked fail-closed. Did not use `--no-verify` (per standing
instruction: never skip hooks without explicit operator ask). The file
edits are real and on disk — `grep -L X-Frame-Options` confirms all 21
files are clean — but there is no commit, so no receipt in that repo's log.
Operator: either fix/bypass that hook yourself, or say the word and I'll
retry with `--no-verify` next session.

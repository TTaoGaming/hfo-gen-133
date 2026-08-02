# CrazyGames manual submission -- Light Trail

**Generated 2026-08-02T16:50:23Z by crazygames_submit.py (STAGE only, no network call made).**

## What this tool did
- Zipped `outputs/pages/games/games/004_light_trail` -> `outputs/staged_sends/crazygames/004_light_trail/game.zip` (1 files)
- Wrote a placeholder thumbnail at `outputs/staged_sends/crazygames/004_light_trail/thumbnail_placeholder.png` -- **REPLACE with a real
  1280x720+ screenshot before submitting.** The placeholder is a 1x1 pixel and
  will fail CrazyGames' asset review as-is.
- Wrote the multipart form-data field plan to `outputs/staged_sends/crazygames/004_light_trail/submission_plan.json`

## What the operator must do by hand
1. Go to https://developer.crazygames.com/games/new (log in with the
   operator's own CrazyGames developer account -- this tool has no
   credentials and makes no request to this URL).
2. Upload `outputs/staged_sends/crazygames/004_light_trail/game.zip` as the game build.
3. Replace `outputs/staged_sends/crazygames/004_light_trail/thumbnail_placeholder.png` with a real screenshot/promo image before
   uploading the thumbnail field.
4. Fill in: title="Light Trail", genre="action", tags=['action', 'browser-game', 'html5', 'keyboard', 'single-page', 'swipe'].
5. Paste description from `outputs/staged_sends/crazygames/004_light_trail/submission_plan.json` (`multipart_form_fields.description`).
6. CrazyGames' review queue historically approves roughly 1 in 8 unknown
   solo submissions within 1-3 weeks (source: areas/quorum_research
   DEEP_RESEARCH_INDEX_20260802T1545Z.md). Expect asset/SDK review comments
   on the first pass.

## What CrazyGames reviews (per public developer docs + this repo's research)
- SDK integration presence (ads + leaderboard hooks) -- currently missing,
  flagged above.
- No iframe-blocking headers (this build is confirmed clean -- static HTML,
  no CSP/X-Frame-Options set).
- Asset quality: real thumbnail/screenshots, not placeholders.
- Revenue terms if accepted: ~60% ad rev-share / ~70% net IAP share, NET-60
  payout (docs.crazygames.com/payouts, cited in
  areas/quorum_research/FOSS_GAME_EXEMPLAR_RESEARCH_20260802.md).

This file and the JSON plan are the entire submission artifact. Nothing here
was POSTed to crazygames.com.

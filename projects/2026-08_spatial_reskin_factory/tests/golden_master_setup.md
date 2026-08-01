# Signal Refinery demo — golden-master injection test

Drives the deployed `demo01-handpiano` Cloudflare Pages build through
`window.HandPiano.injectRawLandmarks` (one of the 4 documented `hfopiano_v512`
injection seams) with a fixed synthetic hand trace — no camera, no human — and
records a video of the run via Playwright's `recordVideo`.

## What's here

- `scripts/record_gesture_run.mjs` — launches Chromium, opens `<baseUrl>/index.html`,
  waits for `window.HandPiano.injectRawLandmarks` to exist, then feeds it a
  deterministic two-hand synthetic landmark stream (~30Hz, 12s) via
  `page.evaluate`. `seed` selects the trace shape (`seed=0` is the golden trace).
- `scripts/verify_golden_master.mjs` — records a fresh run and compares it
  against the sealed golden master with ffmpeg SSIM, cropped to the hand-cursor
  overlay region.
- `golden_master/demo01_20260801.mp4` — the sealed golden-master recording.
  sha256: `b1c8305b0fa28ce6a0ff4493c36548cc164f7bb4cc64ba1ff806796a2e375cdc`

## Reproduction

Requires the Playwright 1.61.1 + Chromium install already present at
`C:\Dev\hfo_dev_2026_5_30\hfo_gen_130_forge\work\tooling\playwright\node_modules`
(Node 24 resolves it via an absolute `file://` import in the script, not
`node_modules` lookup — no install/network step needed) and ffmpeg from the
WinGet `Gyan.FFmpeg` package already on this machine.

Record a fresh run against the live demo and diff it against the golden master:

```bash
cd C:/Dev/hfo_gen_133_forge/projects/2026-08_spatial_reskin_factory/tests/scripts
node verify_golden_master.mjs https://demo01-handpiano.pages.dev 0   # reproduction (seed 0)
node verify_golden_master.mjs https://demo01-handpiano.pages.dev 1   # held-out variant
node verify_golden_master.mjs https://demo01-handpiano.pages.dev 3   # held-out variant
```

Re-record the golden master itself (only if the demo is intentionally changed):

```bash
node record_gesture_run.mjs https://demo01-handpiano.pages.dev ../golden_master/demo01_20260801.webm 0
"C:/Users/tommy/AppData/Local/Microsoft/WinGet/Packages/Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe/ffmpeg-8.1.1-full_build/bin/ffmpeg.exe" \
  -y -i ../golden_master/demo01_20260801.webm -c:v libx264 -pix_fmt yuv420p -movflags +faststart ../golden_master/demo01_20260801.mp4
sha256sum ../golden_master/demo01_20260801.mp4
```

## What this test actually proves, and what it doesn't (honest limitation)

**Proves:** the deployed page loads, exposes all 4 injection seams as live
functions, accepts a synthetic landmark stream with zero console errors, and
visibly renders hand-cursor overlays + piano key response driven purely by
injected data — verified by eye against a captured frame during this build
(see `SIGRUN_PLAIN_LANGUAGE_SYSTEM_OVERVIEW_20260801.md` seam claim). Golden
master vs. itself (byte-identical file) scores an exact SSIM `1.0` on the
cropped cursor ROI, confirming the comparison isn't a no-op.

**Does not yet prove:** clean separation between "same seed, independent
re-recording" and "different seed" runs. Measured on live re-recordings:
seed 0 (reproduction) vs. golden = SSIM 0.884; seed 1 vs. golden = 0.877;
seed 3 vs. golden = 0.889 — all in the same band. Root cause: frame injection
is paced by wall-clock `Date.now()` + `page.waitForTimeout`, so two
independent recordings of even the *same* seed land their landmark updates at
slightly different frame offsets; that inter-run timing jitter is currently
the same order of magnitude as the actual cursor-position difference between
seeds. The `pass` gate in `verify_golden_master.mjs` is therefore set well
below the observed live band (`threshold=0.55`) — it functions today as a
**"did the page not blank-screen/crash" regression gate**, not yet as a
**frame-accurate reproduction gate**.

**FALSIFIER for this test, checked in this session:**
`node record_gesture_run.mjs https://example.com /tmp/falsifier_check.webm 0`
— a real page with no `window.HandPiano` at all — exits with code `1`
(`page.waitForFunction: Timeout 30000ms exceeded`) instead of silently
producing an empty/blank recording. The harness fails loudly on a page
lacking the injection seam rather than fake-passing, which is the minimum bar
for this being a real gate and not a no-op.

**Next safe action to close the gap:** drive the injected timestamp from a
frame counter or Chrome DevTools Protocol virtual time budget instead of
`Date.now()`, so two recordings of the same seed are frame-identical and the
SSIM gate can be tightened to actually distinguish seeds.

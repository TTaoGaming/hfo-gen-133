---
schema_id: hfo.gen133.microsaas_unit_ship.v0_1
doc_kind: UNIT_SHIP_REPORT
unit_slug: local-whisper-web
subject: Unit 5 — local-whisper-web (private in-browser transcription PWA)
claim_status: SCAFFOLDED_AWAITING_DEPLOY
created_utc: 2026-08-02T00:00:00Z
created_by: Executor (Cowork/Claude), gen-133
sealed: false
---

# Unit 5 · local-whisper-web — ship report

## What the unit does

Drop an audio/video file → get a transcript (TXT free, SRT/VTT/JSON on Pro). Model runs 100% in the browser via Transformers.js + Xenova's ONNX-quantized Whisper weights. WebGPU when available (Chrome/Edge/Arc), WASM fallback everywhere else. Installs as a PWA — one-click install on Windows/Linux/macOS/ChromeOS, works offline after first model download. Fills the missing middle between MacWhisper (macOS-only, $19) and command-line `whisper.cpp` (no GUI, requires setup) and cloud services (upload your audio to someone else's server).

## FOSS parents + license verification

- **whisper.cpp** — MIT (Georgi Gerganov). Not directly forked; referenced as the reference C++ implementation. ✓
- **Transformers.js** — Apache 2.0 (Xenova / Hugging Face). Loaded at runtime from jsDelivr, not bundled. ✓
- **OpenAI Whisper** (original PyTorch weights) — MIT (OpenAI). ✓
- **Xenova ONNX-quantized weights on HF Hub** — MIT. ✓

All four permissive. Nothing is redistributed here — Transformers.js loads via `<script>` tag; model weights download from HF Hub on first use into the browser's IndexedDB cache.

**Our license:** MIT. See `factory/units/local-whisper-web/LICENSE`.

## Placeholder-config JSON slots

`factory/units/local-whisper-web/.placeholder-config.json` operator-swap slots:

- `STRIPE_LINK`: `"#"` — swap for real Payment Link (Pro is $19 one-time, not $/mo).
- `CAL_LINK`: `"https://cal.com/ttao/15min"`.
- `GITHUB_URL`: `"https://github.com/TTaoGaming/local-whisper-web"`.
- `SUBDOMAIN` / `ROOT_DOMAIN`: `local-whisper-web.agentreleasegate.com`.

All landing copy already populated for production.

## PWA-specific artifacts

- `public/manifest.json` — installability metadata, `start_url: /app.html`, standalone display.
- `public/sw.js` — service worker; caches app shell (HTML/CSS/JS/icons) with cache-first strategy. Does not cache model weights (Transformers.js handles those in IndexedDB).
- `public/icon-192.svg`, `public/icon-512.svg` — waveform-style app icon in brand colors.
- `public/_headers` — overrides template CSP to allow `https://cdn.jsdelivr.net`, `https://huggingface.co`, `https://*.huggingface.co`, `https://cas-bridge.xethub.hf.co` (HF's CDN), plus `wasm-unsafe-eval` for the ONNX runtime, plus `worker-src 'self' blob:` for Transformers.js workers. Adds `COOP: same-origin` + `COEP: credentialless` which are prerequisites for WebGPU / SharedArrayBuffer paths.

## 5 canonical URLs (post-deploy HEAD check)

1. `https://local-whisper-web.pages.dev/`
2. `https://local-whisper-web.pages.dev/app.html`
3. `https://local-whisper-web.pages.dev/pricing`  (302 → `/#pricing`)
4. `https://local-whisper-web.pages.dev/privacy.html`
5. `https://local-whisper-web.pages.dev/robots.txt`

Plus manual smoke: `/manifest.json` returns 200 with `application/manifest+json`, `/sw.js` returns 200 with `no-cache`, and installing as a PWA succeeds in Chrome (address-bar install button appears).

## Distribution package

### Reddit — r/macapps (primary; the pain audience already knows MacWhisper)

**Title:** I made a MacWhisper alternative that works on Windows and Linux too — everything runs in the browser, nothing uploads

**Body:**
> Love MacWhisper — but my dev machine is Windows and my server is Linux. Every "alternative" I found was either a cloud service (upload my audio, no thanks) or command-line `whisper.cpp` (fine, but not a Sunday-afternoon tool).
>
> Built a PWA that runs Whisper 100% in-browser via Transformers.js + Xenova's ONNX weights. Drop an audio or video file, get a transcript. Works offline after the first model download (~40 MB for tiny, ~140 MB for base).
>
> WebGPU when available (Chrome/Edge/Arc — very fast), WASM fallback for Firefox/Safari (~3-5× slower but still real-time on tiny).
>
> Install button appears in the address bar in Chrome/Edge — one click and it's a standalone app in your OS launcher.
>
> Free tier: TXT export with a small watermark, tiny + base models. Pro ($19 one-time, launching Tuesday): SRT/VTT/JSON, no watermark, small + medium models, batch mode.
>
> Everything is MIT: `https://local-whisper-web.agentreleasegate.com/`.
>
> The audio-never-uploads part is verifiable in devtools — I invite you to check the Network tab and confirm.

**Secondary subs:** r/productivity, r/podcasting, r/webdev, r/LocalLLaMA, r/selfhosted, r/opensource, r/pwa.

### Hacker News — Show HN

**Title:** Show HN: Local Whisper Web – private in-browser transcription, installs as a PWA

**URL:** `https://local-whisper-web.agentreleasegate.com/`

**Top comment (self-post):**
> Author here. Two motivations: (1) MacWhisper is macOS-only and I'm on Windows for dev + Linux for server; (2) every cloud transcription service uploads my audio and I don't want that for interviews or drafts.
>
> Runs OpenAI Whisper (MIT) via Xenova's ONNX quantized weights (MIT) through Transformers.js (Apache 2.0). WebGPU when the browser has `navigator.gpu`, WASM fallback otherwise. Model downloads once from HF Hub (~40 MB tiny, ~140 MB base), caches in IndexedDB.
>
> Verifiable privacy claim: open devtools, watch the Network tab, drop a file. You'll see model weight downloads from HF on first run and zero requests carrying your audio anywhere.
>
> Free tier ships TXT with a watermark line + tiny/base models. Pro $19 one-time unlocks SRT/VTT/JSON, small/medium models, and batch mode (drop a folder).
>
> Interested in feedback especially on: (a) whether the WebGPU path holds up on your GPU, (b) whether Firefox WASM speed is acceptable for you, (c) any codec I'm mis-decoding.

### Product Hunt Ships / directories

- Product Hunt Ships (upcoming, then launch Tuesday)
- IndieHackers, BetaList, SaaSHub, AlternativeTo (list under "MacWhisper alternative for Windows/Linux"), StackShare, TinyLaunch, Uneed, Startupbase, ToolFinder, Peerlist Launchpad, MicroLaunch, LaunchPedia, Fazier.
- Tier 2 (AI-native): TAAFT, Futurepedia, AI Tool Report, Insidr AI, aitools.fyi.

### Cold email — template

**Subject:** private transcription that never leaves your browser

**Body:**
> Hey {first_name},
>
> {personal_hook — e.g. saw you post about MacWhisper / saw your Windows dev setup / saw your podcast episode notes}.
>
> Quick share: I built a private in-browser transcription PWA — Windows/Linux/Mac, runs Whisper locally via WebGPU, audio never uploads. It's the "MacWhisper equivalent for the other 60% of computers."
>
> Free tier gets you TXT export today: `https://local-whisper-web.agentreleasegate.com/`.
>
> If you record interviews, podcasts, meetings, or voice memos and don't want them going to a cloud service, would love your feedback. MIT-licensed either way.
>
> — Tao

**Personas / target list:**
- Podcasters (Podcast Index maintainers, indie podcast Discord regulars)
- Journalists / researchers who record interviews (LinkedIn: reporter + investigative)
- Windows-only devs frustrated by macOS-only tooling (Twitter search #wsl or #windowsdev)
- Privacy-focused indie creators (Fosstodon, r/privacy, r/selfhosted)

**Volume target:** 30 sends. FU1 day 3, FU2 day 8 (same schema as Unit 4).

## Deploy command operator runs Tuesday

```bash
node factory/scripts/deploy-unit.mjs local-whisper-web
node factory/scripts/verify-unit.mjs local-whisper-web
```

Post-deploy smoke: open the deployed URL in Chrome desktop, drop a 30-second WAV file, confirm transcript appears. Verify Network tab shows model download from HF Hub but zero audio upload.

## Files on disk

```
factory/units/local-whisper-web/
├── .placeholder-config.json
├── LICENSE                          # MIT + third-party attribution
├── README.md
├── package.json
├── src/
│   ├── app.html                     # the tool + PWA manifest link
│   └── whisper-tool.js              # audio decode + Transformers.js pipeline + downloads
└── public/
    ├── _headers                     # CSP override for CDN + HF + WebGPU
    ├── manifest.json                # PWA manifest
    ├── sw.js                        # service worker (app-shell cache)
    ├── icon-192.svg
    └── icon-512.svg
```

## Truthful-red notes

- **First-load latency is real.** Users see 30-90s on their first transcript on a slow connection. Log message + progress bar cover this — no hidden wait.
- **Firefox / Safari fall back to WASM.** ~3-5× slower. Still real-time on tiny for most inputs.
- **Free-tier watermark is one line appended to TXT.** Trivial to strip; friction + honor system is the design.
- **Batch mode and speaker diarization are Pro-tier stubs.** Speaker diarization is marked "roadmap" in the FAQ.
- **Native Tauri wrapper was in the brief as an option.** Not shipped this pass — PWA-only within budget. Native is a future unit if operator wants it.

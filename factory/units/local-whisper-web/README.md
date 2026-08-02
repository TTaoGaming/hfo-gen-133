# Local Whisper Web

**One-liner:** Private in-browser Whisper transcription. Drop audio, get SRT/VTT/TXT. Windows + Linux + Mac. Install as a PWA.

## Why this exists

MacWhisper ($19, macOS-only, native) is beautiful. Windows and Linux users don't have an equivalent — they get pushed to cloud services (upload your audio to someone else's server) or to `whisper.cpp` on the command line (Python setup, no GUI). This is the missing middle: same private, offline transcription, in a web app you install like an app.

## Wedge

- **100% local.** Model + inference run in the browser. Audio never uploads.
- **Cross-platform.** Chrome/Edge/Arc/Firefox on Windows, Linux, macOS, ChromeOS.
- **PWA-installable.** One-click install, service-worker cached, works offline after first model download.
- **WebGPU when available, WASM fallback.** Fast on modern hardware, works on everything.

## Pricing

- **Free** — tiny + base models, TXT export (small watermark line), single-file.
- **Pro $19 one-time** — small + medium models, SRT/VTT/JSON export (no watermark), batch mode (drop a folder), speaker diarization roadmap.

## FOSS parents + licenses

- [`whisper.cpp`](https://github.com/ggerganov/whisper.cpp) — MIT (Georgi Gerganov). Reference C++ implementation.
- [`Transformers.js`](https://github.com/xenova/transformers.js) — Apache 2.0 (Xenova / Hugging Face). Runtime we load at CDN import.
- [OpenAI Whisper](https://github.com/openai/whisper) — MIT (OpenAI). Model weights.
- Xenova's ONNX-quantized weights on HF Hub — MIT.

**This project:** MIT. Not a fork — we import Transformers.js from jsDelivr and load the model from HF Hub at runtime. Zero third-party code is bundled. See `LICENSE`.

## Architecture (v0 MVP)

1. User drops an audio/video file.
2. Browser decodes via `AudioContext.decodeAudioData` to Float32 PCM at 16 kHz mono.
3. Transformers.js loads `Xenova/whisper-tiny.en` (or `whisper-base`) from HF Hub. First load ≈ 40-140 MB, cached in IndexedDB via HF cache manager.
4. Model runs in-browser (WebGPU if `navigator.gpu` is present; else WASM).
5. Output: array of `{start, end, text}` chunks.
6. Renderer formats to TXT (free), or SRT/VTT/JSON (Pro gate — pop upgrade modal).

Service worker caches app shell + Transformers.js so second load is offline.

## Deploy

```bash
node ../../scripts/deploy-unit.mjs local-whisper-web
node ../../scripts/verify-unit.mjs local-whisper-web
```

Because we override `public/_headers`, the CSP allows loading Transformers.js from jsDelivr and model weights from Hugging Face CDN. Verify with browser devtools.

## Distribution

See `state/factory_ships/UNIT_local-whisper-web_20260803.md` — Reddit, HN Show, Product Hunt Ships, r/macapps, r/productivity, r/podcasting.

## Truthful-red notes

- **First-load latency.** Model download is ~40 MB (tiny) or ~140 MB (base). Slow connections wait 30-90s on first run. Cached after that.
- **Browser support caveat.** WebGPU is Chrome/Edge/Arc first-class; Firefox flagged; Safari partial. WASM fallback works everywhere but is ~3-5× slower.
- **Watermark.** Free-tier TXT gets a single line appended: `— transcribed by local-whisper-web (agentreleasegate.com)`. Trivial to strip; the honor system + friction is the point.
- **Speaker diarization** is roadmap, not shipped in v0. Stated as roadmap in FAQ + Pro bullet.
- **No native compilation this pass.** The brief allowed Tauri as native fallback; we shipped PWA-only to hit budget. Native wrapper is a future ship.

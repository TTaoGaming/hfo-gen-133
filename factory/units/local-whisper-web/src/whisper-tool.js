// whisper-tool.js — Local Whisper Web v0.
// Loads Transformers.js from jsDelivr (Apache 2.0), pulls whisper ONNX
// weights from Hugging Face on first use, caches in IndexedDB via HF cache.
// All inference runs in-browser (WebGPU when available, WASM fallback).
//
// Truthful-red notes:
//   - First model download is ~40 MB (tiny) or ~140 MB (base). Not instant.
//   - Chrome/Edge/Arc get WebGPU (fastest). Firefox/Safari get WASM fallback.
//   - Free tier is TXT only + watermark. Pro-tier SRT/VTT/JSON export logic
//     is stubbed to a modal until Stripe wires Tuesday.

const TRANSFORMERS_URL = 'https://cdn.jsdelivr.net/npm/@xenova/transformers@2.17.2';

const $ = id => document.getElementById(id);
const log = msg => { $('log').textContent = msg; console.log('[whisper]', msg); };
const setProg = pct => { $('prog').style.width = Math.max(0, Math.min(100, pct)) + '%'; };

let transcriber = null;   // cached pipeline
let currentModel = null;
let lastChunks = null;    // array of {text, timestamp:[start,end]}

// -------- engine detection --------
(async function detectEngine() {
  const hasGPU = !!navigator.gpu;
  $('engine-badge').textContent = hasGPU ? 'WebGPU' : 'WASM';
})();

// -------- drag+drop wiring --------
const drop = $('drop');
['dragover', 'dragenter'].forEach(e => drop.addEventListener(e, ev => {
  ev.preventDefault(); drop.classList.add('hot');
}));
['dragleave', 'drop'].forEach(e => drop.addEventListener(e, ev => {
  ev.preventDefault(); drop.classList.remove('hot');
}));
drop.addEventListener('drop', ev => {
  ev.preventDefault();
  const f = ev.dataTransfer && ev.dataTransfer.files && ev.dataTransfer.files[0];
  if (f) handleFile(f);
});
$('file').addEventListener('change', ev => {
  const f = ev.target.files && ev.target.files[0];
  if (f) handleFile(f);
});

// -------- audio decode → 16 kHz Float32 mono --------
async function decodeToMono16k(file) {
  log(`decoding ${file.name} (${(file.size / 1024 / 1024).toFixed(1)} MB)…`);
  const buf = await file.arrayBuffer();
  const AC = window.OfflineAudioContext || window.webkitOfflineAudioContext;
  // First: general-purpose decode
  const tmpCtx = new (window.AudioContext || window.webkitAudioContext)({ sampleRate: 16000 });
  let decoded;
  try {
    decoded = await tmpCtx.decodeAudioData(buf.slice(0));
  } catch (e) {
    tmpCtx.close && tmpCtx.close();
    throw new Error('Could not decode audio (unsupported codec): ' + e.message);
  }
  tmpCtx.close && tmpCtx.close();

  // If already 16 kHz mono, done.
  if (decoded.sampleRate === 16000 && decoded.numberOfChannels === 1) {
    return decoded.getChannelData(0);
  }
  // Otherwise resample via OfflineAudioContext at 16 kHz mono.
  const offline = new AC(1, Math.ceil(decoded.duration * 16000), 16000);
  const src = offline.createBufferSource();
  src.buffer = decoded; src.connect(offline.destination); src.start(0);
  const rendered = await offline.startRendering();
  return rendered.getChannelData(0);
}

// -------- pipeline loader --------
async function ensurePipeline(modelId) {
  if (transcriber && currentModel === modelId) return transcriber;
  log(`loading ${modelId} (first time may take 30-90s)…`);
  setProg(2);
  const mod = await import(/* @vite-ignore */ TRANSFORMERS_URL);
  const { pipeline, env } = mod;
  // Point HF cache to browser (default). Don't try to fetch local model bin.
  env.allowLocalModels = false;
  env.useBrowserCache = true;
  transcriber = await pipeline('automatic-speech-recognition', modelId, {
    progress_callback: (info) => {
      if (info.status === 'progress' && typeof info.progress === 'number') {
        setProg(2 + info.progress * 0.5);   // model load is 0-50% of overall bar
        log(`downloading ${info.file || modelId}: ${info.progress.toFixed(0)}%`);
      } else if (info.status === 'ready' || info.status === 'done') {
        setProg(52);
        log(`${modelId} ready.`);
      }
    }
  });
  currentModel = modelId;
  return transcriber;
}

// -------- main handler --------
async function handleFile(file) {
  try {
    $('actions').hidden = true;
    $('out').hidden = true;
    setProg(0);
    const audio = await decodeToMono16k(file);
    setProg(2);

    const modelId = $('model').value;
    const lang = $('lang').value;
    const task = $('task').value;

    const asr = await ensurePipeline(modelId);
    log(`transcribing (${(audio.length / 16000).toFixed(1)}s of audio)…`);

    const opts = { chunk_length_s: 30, stride_length_s: 5, return_timestamps: true };
    if (lang !== 'auto') opts.language = lang;
    if (task) opts.task = task;

    // Fake a moving bar during inference since we don't get token-level events.
    let bar = 52; const timer = setInterval(() => { bar = Math.min(bar + 1.5, 95); setProg(bar); }, 400);
    let result;
    try {
      result = await asr(audio, opts);
    } finally { clearInterval(timer); }
    setProg(100);

    lastChunks = result.chunks || [{ text: result.text, timestamp: [0, audio.length / 16000] }];
    const text = result.text || lastChunks.map(c => c.text).join('');
    const watermarked = text + '\n\n— transcribed by local-whisper-web (agentreleasegate.com)';
    $('out').hidden = false;
    $('out').textContent = watermarked;
    $('actions').hidden = false;
    log(`done — ${lastChunks.length} segments, ${text.length} chars.`);
    // Stash for downloads.
    window._lwwText = watermarked;
    window._lwwChunks = lastChunks;
  } catch (e) {
    console.error(e);
    log('error: ' + e.message);
    setProg(0);
  }
}

// -------- exports --------
function download(name, mime, body) {
  const blob = new Blob([body], { type: mime });
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url; a.download = name; a.click(); URL.revokeObjectURL(url);
}

function tsSrt(sec) {
  const h = Math.floor(sec / 3600), m = Math.floor((sec % 3600) / 60), s = Math.floor(sec % 60), ms = Math.round((sec - Math.floor(sec)) * 1000);
  return `${String(h).padStart(2, '0')}:${String(m).padStart(2, '0')}:${String(s).padStart(2, '0')},${String(ms).padStart(3, '0')}`;
}
function tsVtt(sec) { return tsSrt(sec).replace(',', '.'); }

function toSRT(chunks) {
  return chunks.map((c, i) =>
    `${i + 1}\n${tsSrt(c.timestamp[0])} --> ${tsSrt(c.timestamp[1] || c.timestamp[0] + 1)}\n${c.text.trim()}\n`
  ).join('\n');
}
function toVTT(chunks) {
  return 'WEBVTT\n\n' + chunks.map((c, i) =>
    `${tsVtt(c.timestamp[0])} --> ${tsVtt(c.timestamp[1] || c.timestamp[0] + 1)}\n${c.text.trim()}\n`
  ).join('\n');
}

$('dl-txt').onclick = () => {
  if (!window._lwwText) return;
  download('transcript.txt', 'text/plain', window._lwwText);
};

document.querySelectorAll('[data-pro]').forEach(btn => btn.onclick = () => {
  const kind = btn.dataset.pro;
  // Soft-gate: show a modal-ish prompt, but still allow local generation
  // if the operator flipped `localStorage.setItem('lww.pro', '1')` (for
  // testing). Real gate lands when Stripe wires Tuesday.
  const proUnlocked = localStorage.getItem('lww.pro') === '1';
  if (!proUnlocked) {
    const go = confirm(`SRT / VTT / JSON export is a Pro feature ($19 one-time).\n\nBuy Pro on the pricing page?`);
    if (go) location.href = '/#pricing';
    return;
  }
  if (!window._lwwChunks) return;
  if (kind === 'srt')  download('transcript.srt', 'application/x-subrip', toSRT(window._lwwChunks));
  if (kind === 'vtt')  download('transcript.vtt', 'text/vtt', toVTT(window._lwwChunks));
  if (kind === 'json') download('transcript.json', 'application/json', JSON.stringify({ chunks: window._lwwChunks }, null, 2));
});

// -------- PWA service worker --------
if ('serviceWorker' in navigator) {
  navigator.serviceWorker.register('/sw.js').catch(err => console.warn('[sw] register failed', err));
}

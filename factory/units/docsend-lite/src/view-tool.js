// view-tool.js — viewer side.
// Loads params from URL, gates on password digest (SHA-256 of salt+password),
// checks expiry, then renders PDF via pdfjs-dist (loaded from CDN in view.html).
// Beacons one POST /api/v1/view per page as viewer scrolls (Free returns 202;
// Pro writes to KV).

const $ = id => document.getElementById(id);

// pdf.js is loaded as an ES module from CDN in view.html. Wait for it.
async function waitForPdfjs() {
  // The mjs build exposes on window.pdfjsLib after import completes.
  for (let i = 0; i < 40; i++) {
    if (window.pdfjsLib) return window.pdfjsLib;
    await new Promise(r => setTimeout(r, 100));
  }
  // Fallback: dynamic import.
  const mod = await import('https://cdn.jsdelivr.net/npm/pdfjs-dist@4.7.76/legacy/build/pdf.min.mjs');
  window.pdfjsLib = mod;
  return mod;
}

async function sha256Hex(str) {
  const buf = new TextEncoder().encode(str);
  const h = await crypto.subtle.digest('SHA-256', buf);
  return [...new Uint8Array(h)].map(b => b.toString(16).padStart(2, '0')).join('');
}

const p = new URLSearchParams(location.search);
const src = p.get('src');
const id = p.get('id') || 'unknown';
const salt = p.get('s') || '';
const digest = p.get('d') || '';
const expiryTs = +p.get('e') || 0;
const title = p.get('t') || '';

if (!src || !expiryTs) {
  document.body.innerHTML = '<div class="gate"><h2>Missing link parameters</h2><p class="micro">This link is malformed. Ask the sender to regenerate it.</p></div>';
  throw new Error('missing params');
}

if (title) document.title = `${title} · shared`;

if (Date.now() > expiryTs) {
  $('expired').hidden = false;
} else if (digest) {
  $('gate').hidden = false;
  $('unlock').onclick = attemptUnlock;
  $('pw').addEventListener('keydown', e => { if (e.key === 'Enter') attemptUnlock(); });
} else {
  loadAndRender();
}

async function attemptUnlock() {
  const pw = $('pw').value;
  const msg = $('gate-msg');
  msg.className = 'msg';
  if (!pw) { msg.textContent = 'Enter the password.'; msg.classList.add('err'); return; }
  const attempt = await sha256Hex(salt + pw);
  if (attempt !== digest) {
    msg.textContent = 'Wrong password.'; msg.classList.add('err');
    $('pw').value = '';
    return;
  }
  $('gate').hidden = true;
  loadAndRender();
}

async function loadAndRender() {
  $('viewer').hidden = false;
  try {
    const pdfjs = await waitForPdfjs();
    pdfjs.GlobalWorkerOptions.workerSrc = 'https://cdn.jsdelivr.net/npm/pdfjs-dist@4.7.76/legacy/build/pdf.worker.min.mjs';
    $('load-status').textContent = 'Fetching PDF…';
    const doc = await pdfjs.getDocument({ url: src, disableRange: false, disableStream: false }).promise;
    $('load-status').textContent = '';
    $('page-status').textContent = `1 / ${doc.numPages}`;
    beacon({ event: 'open', pages_total: doc.numPages });

    const pagesEl = $('pages');
    const observers = [];
    for (let i = 1; i <= doc.numPages; i++) {
      const page = await doc.getPage(i);
      const scale = Math.min(1.4, (pagesEl.clientWidth || 800) / page.getViewport({ scale: 1 }).width);
      const viewport = page.getViewport({ scale });
      const canvas = document.createElement('canvas');
      canvas.className = 'page';
      canvas.width = viewport.width;
      canvas.height = viewport.height;
      canvas.dataset.page = String(i);
      pagesEl.appendChild(canvas);
      await page.render({ canvasContext: canvas.getContext('2d'), viewport }).promise;
      observers.push(canvas);
    }

    // page-in-view tracking
    const seen = new Set();
    const pageStart = performance.now();
    const io = new IntersectionObserver(entries => {
      for (const e of entries) {
        if (!e.isIntersecting) continue;
        const n = +e.target.dataset.page;
        $('page-status').textContent = `${n} / ${doc.numPages}`;
        if (!seen.has(n)) {
          seen.add(n);
          beacon({ event: 'page_view', page: n, elapsed_ms: Math.round(performance.now() - pageStart) });
        }
      }
    }, { threshold: 0.5 });
    for (const c of observers) io.observe(c);
  } catch (e) {
    console.error(e);
    $('load-status').textContent = 'Failed to load PDF: ' + e.message +
      '. The source URL may not allow cross-origin fetches — the sender needs to host on R2 (Pro) or use a CORS-friendly URL.';
    $('load-status').classList.add('err');
  }
}

function beacon(payload) {
  try {
    const body = JSON.stringify({ docId: id, ts: Date.now(), ...payload });
    if (navigator.sendBeacon) {
      navigator.sendBeacon('/api/v1/view', new Blob([body], { type: 'application/json' }));
    } else {
      fetch('/api/v1/view', { method: 'POST', body, headers: { 'content-type': 'application/json' }, keepalive: true }).catch(() => {});
    }
  } catch (_) { /* fine */ }
}

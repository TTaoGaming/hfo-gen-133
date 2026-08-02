// prompt-tool.js — the actual tool.
// Storage is localStorage (v0 MVP). Content-addressed by SHA-256 of prompt
// body. Share URL is #<first-8-of-hash>. Model rerun proxies through
// /api/run if configured; otherwise it stubs a demo response.
//
// Freemium counting: > 10 saved prompts triggers the upgrade nudge. That's
// enforced client-side for MVP — server-side enforcement lands when Stripe
// is wired.
//
// Truthful-red note: this is v0. The persistence layer is local. Multi-device
// sync and true immutability arrive when we add a Cloudflare D1 backend.

const LS_KEY = 'pvl.revisions.v1';

const $ = id => document.getElementById(id);

async function sha256Hex(str) {
  const buf = new TextEncoder().encode(str);
  const h = await crypto.subtle.digest('SHA-256', buf);
  return Array.from(new Uint8Array(h)).map(b => b.toString(16).padStart(2, '0')).join('');
}

function loadAll() {
  try { return JSON.parse(localStorage.getItem(LS_KEY) || '[]'); }
  catch { return []; }
}
function saveAll(list) { localStorage.setItem(LS_KEY, JSON.stringify(list)); }

function fmtTs(ts) { return new Date(ts).toISOString().replace('T', ' ').slice(0, 16) + 'Z'; }

function renderRevs() {
  const list = loadAll();
  $('stats').textContent =
    `${list.length} / 10 prompts on the free tier · localStorage-backed for now`;
  const el = $('revs');
  el.innerHTML = '';
  list.slice().reverse().forEach((r, i) => {
    const div = document.createElement('div');
    div.className = 'rev';
    div.innerHTML = `
      <div>
        <code>${r.hash.slice(0, 12)}</code>
        <span class="micro"> · ${fmtTs(r.ts)} · ${r.body.length} chars</span>
      </div>
      <div class="actions">
        <button data-load="${r.hash}">Load</button>
        <button data-diff="${r.hash}">Diff vs current</button>
        <button data-copy="${r.hash}">Copy URL</button>
      </div>`;
    el.appendChild(div);
  });
  el.querySelectorAll('[data-load]').forEach(b => b.onclick = () => {
    const rev = list.find(x => x.hash === b.dataset.load);
    if (rev) { $('prompt').value = rev.body; setActiveHash(rev.hash); }
  });
  el.querySelectorAll('[data-diff]').forEach(b => b.onclick = () => {
    const rev = list.find(x => x.hash === b.dataset.diff);
    if (rev) showDiff(rev.body, $('prompt').value);
  });
  el.querySelectorAll('[data-copy]').forEach(b => b.onclick = () => {
    const url = `${location.origin}/app.html#${b.dataset.copy.slice(0, 12)}`;
    navigator.clipboard.writeText(url);
    b.textContent = 'copied';
    setTimeout(() => b.textContent = 'Copy URL', 900);
  });
}

// naive word-level diff
function diffWords(a, b) {
  const aw = a.split(/(\s+)/), bw = b.split(/(\s+)/);
  const n = aw.length, m = bw.length;
  const dp = Array.from({ length: n + 1 }, () => new Uint32Array(m + 1));
  for (let i = 1; i <= n; i++)
    for (let j = 1; j <= m; j++)
      dp[i][j] = aw[i - 1] === bw[j - 1] ? dp[i - 1][j - 1] + 1 : Math.max(dp[i - 1][j], dp[i][j - 1]);
  const out = [];
  let i = n, j = m;
  while (i > 0 && j > 0) {
    if (aw[i - 1] === bw[j - 1]) { out.unshift(['eq', aw[i - 1]]); i--; j--; }
    else if (dp[i - 1][j] >= dp[i][j - 1]) { out.unshift(['del', aw[i - 1]]); i--; }
    else { out.unshift(['add', bw[j - 1]]); j--; }
  }
  while (i > 0) { out.unshift(['del', aw[--i]]); }
  while (j > 0) { out.unshift(['add', bw[--j]]); }
  return out;
}

function showDiff(oldStr, newStr) {
  const parts = diffWords(oldStr, newStr);
  const html = parts.map(([k, w]) =>
    k === 'eq' ? escapeHtml(w)
    : `<span class="${k}">${escapeHtml(w)}</span>`).join('');
  const el = $('diff'); el.hidden = false; el.innerHTML = html;
}

function escapeHtml(s) {
  return s.replace(/[&<>"']/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
}

function setActiveHash(hash) {
  $('rev-badge').textContent = 'rev ' + hash.slice(0, 12);
  const short = hash.slice(0, 12);
  $('permalink').textContent = 'Permalink: ' + location.origin + '/app.html#' + short;
  history.replaceState(null, '', '#' + short);
}

$('save').onclick = async () => {
  const body = $('prompt').value.trim();
  if (!body) return;
  const list = loadAll();
  if (list.length >= 10) {
    if (!confirm('Free tier caps at 10 prompts. Overwrite the oldest?')) return;
    list.shift();
  }
  const hash = await sha256Hex(body);
  if (list.some(r => r.hash === hash)) {
    alert('No changes since last save.');
    return;
  }
  list.push({ hash, body, ts: Date.now() });
  saveAll(list);
  setActiveHash(hash);
  renderRevs();
};

$('copy').onclick = () => {
  const hash = ($('rev-badge').textContent.match(/rev ([a-f0-9]+)/) || [])[1];
  if (!hash) return alert('Save a revision first.');
  navigator.clipboard.writeText(`${location.origin}/app.html#${hash}`);
  $('copy').textContent = 'copied';
  setTimeout(() => $('copy').textContent = 'Copy share URL', 900);
};

$('run').onclick = async () => {
  const body = $('prompt').value.trim();
  const model = $('model').value;
  const key = $('api-key').value.trim();
  if (!body) return;
  $('output').textContent = 'Running ' + model + '…';
  try {
    const r = await fetch('/api/run', {
      method: 'POST',
      headers: { 'content-type': 'application/json' },
      body: JSON.stringify({ model, prompt: body, apiKey: key })
    });
    if (!r.ok) throw new Error('API returned ' + r.status);
    const j = await r.json();
    $('output').textContent = j.output;
  } catch (e) {
    // Fallback demo response until /api/run is wired (Cloudflare Worker).
    $('output').textContent =
      '[demo — /api/run not yet deployed] ' + model +
      ' would answer here.\n\nPrompt received (' + body.length + ' chars): ' +
      body.slice(0, 120) + (body.length > 120 ? '…' : '');
  }
};

// hydrate from #hash
(function hydrate() {
  renderRevs();
  const h = location.hash.replace('#', '');
  if (h) {
    const rev = loadAll().find(r => r.hash.startsWith(h));
    if (rev) { $('prompt').value = rev.body; setActiveHash(rev.hash); }
  }
})();

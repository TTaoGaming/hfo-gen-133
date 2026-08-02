// docsend-tool.js — creator side.
// Persists doc metadata (title, salt, digest, expiry, src URL, view rollup)
// in localStorage. Share link is /view.html?src=…&s=<salt>&d=<digest>&e=<expiry>&id=<docId>&t=<title>
//
// Free tier caps at 3 docs. Pro tier moves storage to Cloudflare KV / R2 via
// functions/api/create.js (currently stub).

const LS_DOCS = 'dsl.docs.v1';
const FREE_CAP = 3;

const $ = id => document.getElementById(id);

async function sha256Hex(str) {
  const buf = new TextEncoder().encode(str);
  const h = await crypto.subtle.digest('SHA-256', buf);
  return [...new Uint8Array(h)].map(b => b.toString(16).padStart(2, '0')).join('');
}

function loadDocs() {
  try { return JSON.parse(localStorage.getItem(LS_DOCS) || '[]'); } catch { return []; }
}
function saveDocs(list) { localStorage.setItem(LS_DOCS, JSON.stringify(list)); }

function randHex(bytes = 16) {
  const a = new Uint8Array(bytes);
  crypto.getRandomValues(a);
  return [...a].map(b => b.toString(16).padStart(2, '0')).join('');
}

function fmtTs(ts) {
  const d = new Date(ts);
  if (Number.isNaN(d.getTime())) return '';
  return d.toISOString().slice(0, 16).replace('T', ' ');
}

function render() {
  const list = loadDocs();
  $('stats').textContent =
    `${list.length} / ${FREE_CAP} docs on the free tier · localStorage-backed. Pro tier syncs across devices via Cloudflare KV.`;
  $('link-count').textContent = ` (${list.length})`;
  const tb = document.querySelector('#tbl tbody');
  tb.innerHTML = '';
  if (!list.length) {
    tb.innerHTML = '<tr><td colspan="4" class="micro">No links yet.</td></tr>';
    return;
  }
  list.slice().reverse().forEach((d, i) => {
    const tr = document.createElement('tr');
    const expired = d.expiryTs < Date.now();
    tr.innerHTML = `
      <td>${escapeHtml(d.title || d.id)}</td>
      <td>${fmtTs(d.expiryTs)}${expired ? ' <span style="color:#f87171">expired</span>' : ''}</td>
      <td>${d.views || 0}</td>
      <td>
        <button data-copy="${d.id}" style="padding:2px 8px;font-size:11px;background:transparent;border:1px solid var(--border);color:var(--muted);border-radius:4px;cursor:pointer">copy</button>
        <button data-del="${d.id}" style="padding:2px 8px;font-size:11px;background:transparent;border:1px solid var(--border);color:var(--muted);border-radius:4px;cursor:pointer">del</button>
      </td>`;
    tb.appendChild(tr);
  });
  tb.querySelectorAll('[data-copy]').forEach(b => b.onclick = () => {
    const d = loadDocs().find(x => x.id === b.dataset.copy);
    if (d) { navigator.clipboard.writeText(d.link); b.textContent = 'copied'; setTimeout(() => b.textContent = 'copy', 900); }
  });
  tb.querySelectorAll('[data-del]').forEach(b => b.onclick = () => {
    if (!confirm('Delete this link?')) return;
    saveDocs(loadDocs().filter(x => x.id !== b.dataset.del));
    render();
  });
}

function escapeHtml(s) {
  return String(s).replace(/[&<>"']/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
}

$('gen').onclick = async () => {
  const src = $('src').value.trim();
  const title = $('title').value.trim() || 'Untitled';
  const pw = $('pw').value;                            // do not trim — spaces allowed
  const days = Math.min(+$('exp').value || 7, 7);      // free tier cap
  const msg = $('msg');
  msg.className = 'msg';
  if (!src) { msg.textContent = 'PDF URL required.'; msg.classList.add('err'); return; }
  try { new URL(src); } catch { msg.textContent = 'That is not a valid URL.'; msg.classList.add('err'); return; }

  const list = loadDocs();
  if (list.length >= FREE_CAP) {
    if (!confirm(`Free tier caps at ${FREE_CAP} docs. Drop the oldest to make room?`)) return;
    list.shift();
  }

  const id = randHex(8);
  const salt = randHex(16);
  const digest = pw ? await sha256Hex(salt + pw) : '';
  const expiryTs = Date.now() + days * 86400 * 1000;

  const params = new URLSearchParams({
    src, id, s: salt, e: String(expiryTs), t: title
  });
  if (digest) params.set('d', digest);
  const link = `${location.origin}/view.html?${params.toString()}`;

  list.push({ id, title, src, salt, digest, expiryTs, link, views: 0, createdTs: Date.now() });
  saveDocs(list);

  $('link-out').hidden = false;
  $('link-out').textContent = link;
  $('copy').hidden = false;
  $('preview').hidden = false;
  msg.classList.add('ok');
  msg.textContent = pw
    ? `Link created. Password-gated, expires ${fmtTs(expiryTs)}.`
    : `Link created (no password). Expires ${fmtTs(expiryTs)}.`;

  $('copy').onclick = () => { navigator.clipboard.writeText(link); $('copy').textContent = 'copied'; setTimeout(() => $('copy').textContent = 'Copy link', 900); };
  $('preview').onclick = () => window.open(link, '_blank', 'noopener');
  render();
};

render();

// changelog-tool.js — renders a demo changelog. When /api/changelog/<slug>
// is deployed (Cloudflare Worker + KV), the client fetches real data instead.

const DEMO = [
  { version: '2.0.0', date: '2026-07-30', breaking: true, sections: {
    Added: ['New "browse-shop" tool with 4-arg schema (query, category, min_price, max_price).',
            'Structured citations in every response — clickable back to the source doc.'],
    Changed: ['System prompt rewritten for terser answers (avg -40% tokens).',
              'Default model bumped from claude-haiku-4 → claude-sonnet-5.'],
    Removed: ['Legacy "search-catalog" tool (replaced by "browse-shop").'],
    Fixed: ['Retrieval no longer echoes back the user\'s question verbatim.'] } },
  { version: '1.4.2', date: '2026-07-22', breaking: false, sections: {
    Fixed: ['Time-zone handling for order-status queries (was returning UTC, now respects user locale).',
            'Rare 500 when the retriever returned 0 chunks.'] } },
  { version: '1.4.0', date: '2026-07-15', breaking: false, sections: {
    Added: ['"track-order" tool now supports partial order IDs.'],
    Changed: ['Rate limit raised from 10 → 30 req/min per user.'] } },
  { version: '1.3.0', date: '2026-07-01', breaking: false, sections: {
    Deprecated: ['"search-catalog" tool — will be removed in 2.0.0 (see 2026-07-30 release).'] } }
];

function render(list) {
  const root = document.getElementById('releases');
  root.innerHTML = list.map(r => `
    <div class="release">
      <div class="release-head">
        <span class="ver">v${r.version}</span>
        <span class="date">${r.date}</span>
        ${r.breaking ? '<span class="badge breaking">BREAKING</span>' : ''}
      </div>
      ${Object.entries(r.sections).map(([k, items]) => `
        <div class="section">
          <h4>${k}</h4>
          <ul>${items.map(i => `<li>${escapeHtml(i)}</li>`).join('')}</ul>
        </div>`).join('')}
    </div>`).join('');
}

function escapeHtml(s) {
  return s.replace(/[&<>"']/g, c => ({ '&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;' }[c]));
}

(async function hydrate() {
  try {
    const r = await fetch('/api/changelog/demo-agent');
    if (!r.ok) throw 0;
    render(await r.json());
  } catch {
    render(DEMO);
  }
})();

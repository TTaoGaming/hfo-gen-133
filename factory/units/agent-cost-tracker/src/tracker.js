// tracker.js — Agent Cost Tracker v0 MVP.
// Local-first: prompts/keys never sent anywhere on the free tier.
// Pricing sourced from tokencost (MIT, AgentOps-AI) + provider public pages.
// Updated 2026-08. Prices in USD per 1K tokens (input / output).
//
// Truthful-red: this is a static table — the app doesn't fetch live prices.
// Ship a monthly release to refresh.

const LS_EVENTS = 'act.events.v1';
const LS_OVERRIDE = 'act.prices.override';
const FREE_CAP = 100;

// USD per 1K tokens: { in: <price>, out: <price> }
const PRICES = {
  // OpenAI
  'gpt-4o':                { in: 2.50,  out: 10.00, provider: 'openai' },
  'gpt-4o-mini':           { in: 0.15,  out: 0.60,  provider: 'openai' },
  'gpt-4-turbo':           { in: 10.00, out: 30.00, provider: 'openai' },
  'gpt-4':                 { in: 30.00, out: 60.00, provider: 'openai' },
  'gpt-3.5-turbo':         { in: 0.50,  out: 1.50,  provider: 'openai' },
  'o1':                    { in: 15.00, out: 60.00, provider: 'openai' },
  'o1-mini':               { in: 3.00,  out: 12.00, provider: 'openai' },
  'o3-mini':               { in: 1.10,  out: 4.40,  provider: 'openai' },
  // Anthropic
  'claude-opus-4':           { in: 15.00, out: 75.00, provider: 'anthropic' },
  'claude-sonnet-4-5':       { in: 3.00,  out: 15.00, provider: 'anthropic' },
  'claude-sonnet-4':         { in: 3.00,  out: 15.00, provider: 'anthropic' },
  'claude-haiku-4-5':        { in: 0.80,  out: 4.00,  provider: 'anthropic' },
  'claude-3-5-sonnet-latest':{ in: 3.00,  out: 15.00, provider: 'anthropic' },
  'claude-3-5-haiku-latest': { in: 0.80,  out: 4.00,  provider: 'anthropic' },
  'claude-3-opus':           { in: 15.00, out: 75.00, provider: 'anthropic' },
  // Google
  'gemini-2.5-pro':        { in: 1.25,  out: 5.00,  provider: 'google' },
  'gemini-2.5-flash':      { in: 0.15,  out: 0.60,  provider: 'google' },
  'gemini-2.0-flash':      { in: 0.10,  out: 0.40,  provider: 'google' },
  'gemini-1.5-pro':        { in: 1.25,  out: 5.00,  provider: 'google' },
  'gemini-1.5-flash':      { in: 0.075, out: 0.30,  provider: 'google' },
  // Groq (approximate — Groq re-hosts open-weight models at low cost)
  'llama-3.3-70b-versatile':{ in: 0.59,  out: 0.79,  provider: 'groq' },
  'llama-3.1-70b':         { in: 0.59,  out: 0.79,  provider: 'groq' },
  'llama-3.1-8b-instant':  { in: 0.05,  out: 0.08,  provider: 'groq' },
  'mixtral-8x7b':          { in: 0.24,  out: 0.24,  provider: 'groq' },
  // Mistral
  'mistral-large-latest':  { in: 2.00,  out: 6.00,  provider: 'mistral' },
  'mistral-small-latest':  { in: 0.20,  out: 0.60,  provider: 'mistral' },
  'codestral-latest':      { in: 0.30,  out: 0.90,  provider: 'mistral' },
  // Cohere
  'command-r-plus':        { in: 2.50,  out: 10.00, provider: 'cohere' },
  'command-r':             { in: 0.15,  out: 0.60,  provider: 'cohere' },
};
window.ACT_PRICES = PRICES;

function loadOverrides() {
  try { return JSON.parse(localStorage.getItem(LS_OVERRIDE) || '{}'); }
  catch { return {}; }
}

function priceOf(model) {
  const overrides = loadOverrides();
  return overrides[model] || PRICES[model] || null;
}

// Fuzzy model resolver — providers append version dates ("claude-sonnet-4-5-20260901").
function resolveModel(name) {
  if (!name) return null;
  const n = String(name).toLowerCase();
  if (priceOf(n)) return n;
  // Try prefix match
  const keys = Object.keys(loadOverrides()).concat(Object.keys(PRICES));
  const hit = keys.find(k => n.startsWith(k.toLowerCase())) ||
              keys.find(k => n.includes(k.toLowerCase()));
  return hit || null;
}

// Multi-provider usage extraction.
function extractUsage(obj) {
  if (!obj || typeof obj !== 'object') return null;
  const u = obj.usage || obj.usageMetadata || obj;
  // OpenAI, Groq, Mistral, Cohere v2: prompt_tokens / completion_tokens
  if ('prompt_tokens' in u || 'completion_tokens' in u) {
    return { input: +u.prompt_tokens || 0, output: +u.completion_tokens || 0 };
  }
  // Anthropic: input_tokens / output_tokens
  if ('input_tokens' in u || 'output_tokens' in u) {
    return { input: +u.input_tokens || 0, output: +u.output_tokens || 0 };
  }
  // Google Gemini: promptTokenCount / candidatesTokenCount
  if ('promptTokenCount' in u || 'candidatesTokenCount' in u) {
    return { input: +u.promptTokenCount || 0, output: +u.candidatesTokenCount || 0 };
  }
  // Cohere v1: meta.tokens.input_tokens / output_tokens
  if (obj.meta && obj.meta.tokens) {
    const t = obj.meta.tokens;
    return { input: +t.input_tokens || 0, output: +t.output_tokens || 0 };
  }
  return null;
}

function extractModel(obj) {
  if (!obj) return null;
  return obj.model || obj.model_id || (obj.metadata && obj.metadata.model) || null;
}

function computeCost(model, input, output) {
  const p = priceOf(resolveModel(model));
  if (!p) return { cost: 0, unknown: true };
  return { cost: (input / 1000) * p.in + (output / 1000) * p.out, unknown: false };
}

// -------- storage --------
function loadEvents() {
  try { return JSON.parse(localStorage.getItem(LS_EVENTS) || '[]'); }
  catch { return []; }
}
function saveEvents(list) { localStorage.setItem(LS_EVENTS, JSON.stringify(list)); }
function addEvent(ev) {
  const list = loadEvents();
  if (list.length >= FREE_CAP) {
    if (!confirm(`Free tier caps at ${FREE_CAP} events. Drop the oldest to add this one?`)) return false;
    list.shift();
  }
  list.push(ev);
  saveEvents(list);
  return true;
}

function fmtUSD(n) {
  if (n === 0) return '$0.0000';
  if (n < 0.01) return '$' + n.toFixed(6);
  if (n < 1)    return '$' + n.toFixed(4);
  return '$' + n.toFixed(2);
}

function fmtInt(n) { return n.toLocaleString('en-US'); }
function fmtTs(iso) { return iso.replace('T', ' ').replace(/:\d\d\.\d+Z$/, 'Z'); }

// -------- render --------
const $ = id => document.getElementById(id);

function render() {
  const list = loadEvents();
  $('stats').textContent =
    `${list.length} / ${FREE_CAP} events on the free tier · localStorage-backed · pricing table baked ${new Date().getFullYear()}-08`;
  $('log-count').textContent = ` (${list.length})`;

  let totCost = 0, totTok = 0;
  const byAgent = new Map(), byModel = new Map();
  for (const e of list) {
    totCost += e.cost_usd;
    totTok += e.input + e.output;
    const a = byAgent.get(e.agent) || { n: 0, tokens: 0, cost: 0 };
    a.n++; a.tokens += e.input + e.output; a.cost += e.cost_usd;
    byAgent.set(e.agent, a);
    const m = byModel.get(e.model) || { n: 0, tokens: 0, cost: 0 };
    m.n++; m.tokens += e.input + e.output; m.cost += e.cost_usd;
    byModel.set(e.model, m);
  }

  $('tot-events').textContent = fmtInt(list.length);
  $('tot-cost').textContent = fmtUSD(totCost);
  $('tot-tokens').textContent = fmtInt(totTok);

  function renderAgg(tbodySel, map) {
    const tb = document.querySelector(tbodySel + ' tbody');
    tb.innerHTML = '';
    [...map.entries()].sort((a, b) => b[1].cost - a[1].cost).forEach(([k, v]) => {
      const tr = document.createElement('tr');
      tr.innerHTML = `<td>${escapeHtml(k)}</td><td>${v.n}</td>
        <td class="num">${fmtInt(v.tokens)}</td><td class="num">${fmtUSD(v.cost)}</td>`;
      tb.appendChild(tr);
    });
    if (!map.size) tb.innerHTML = '<tr><td colspan="4" class="micro">No events yet.</td></tr>';
  }
  renderAgg('#by-agent', byAgent);
  renderAgg('#by-model', byModel);

  const lb = document.querySelector('#log tbody');
  lb.innerHTML = '';
  list.slice().reverse().forEach((e, i) => {
    const tr = document.createElement('tr');
    tr.innerHTML = `<td class="micro">${fmtTs(e.ts)}</td>
      <td>${escapeHtml(e.agent)}</td>
      <td>${escapeHtml(e.model)}</td>
      <td class="num">${fmtInt(e.input)}</td>
      <td class="num">${fmtInt(e.output)}</td>
      <td class="num">${fmtUSD(e.cost_usd)}</td>
      <td><button data-drop="${list.length - 1 - i}" style="padding:2px 8px;font-size:11px;background:transparent;border:1px solid var(--border);color:var(--muted);border-radius:4px;cursor:pointer">del</button></td>`;
    lb.appendChild(tr);
  });
  if (!list.length) lb.innerHTML = '<tr><td colspan="7" class="micro">No events yet — paste one on the left.</td></tr>';
  lb.querySelectorAll('[data-drop]').forEach(b => b.onclick = () => {
    const list = loadEvents();
    list.splice(+b.dataset.drop, 1);
    saveEvents(list); render();
  });
}

function escapeHtml(s) {
  return String(s).replace(/[&<>"']/g, c =>
    ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
}

function toCSV(list) {
  const cols = ['ts', 'agent', 'model', 'input', 'output', 'cost_usd', 'source'];
  const lines = [cols.join(',')];
  for (const e of list) {
    lines.push(cols.map(c => {
      const v = e[c] == null ? '' : String(e[c]);
      return /[",\n]/.test(v) ? `"${v.replace(/"/g, '""')}"` : v;
    }).join(','));
  }
  return lines.join('\n');
}

// -------- handlers --------
$('parse-add').onclick = () => {
  const raw = $('paste').value.trim();
  const agent = $('agent').value.trim();
  const modelOverride = $('model-override').value.trim();
  const msg = $('parse-msg');
  msg.className = 'msg';
  if (!raw) { msg.textContent = 'Paste an API response above.'; msg.classList.add('err'); return; }
  if (!agent) { msg.textContent = 'Agent label is required.'; msg.classList.add('err'); return; }
  let obj;
  try { obj = JSON.parse(raw); } catch (e) {
    msg.textContent = 'That is not valid JSON: ' + e.message; msg.classList.add('err'); return;
  }
  const usage = extractUsage(obj);
  if (!usage) {
    msg.textContent = 'No usage block found. Expected keys like `usage.prompt_tokens`, `usage.input_tokens`, or `usageMetadata`.';
    msg.classList.add('err'); return;
  }
  const model = modelOverride || extractModel(obj) || 'unknown';
  const resolved = resolveModel(model) || model;
  const { cost, unknown } = computeCost(resolved, usage.input, usage.output);
  const ev = {
    ts: new Date().toISOString(),
    agent, model: resolved,
    input: usage.input, output: usage.output,
    cost_usd: cost, source: 'paste'
  };
  if (!addEvent(ev)) return;
  msg.classList.add('ok');
  msg.textContent = unknown
    ? `Added — ${fmtInt(usage.input + usage.output)} tokens, cost $0 (model "${model}" not in pricing table — add it via localStorage override).`
    : `Added — ${fmtInt(usage.input + usage.output)} tokens, ${fmtUSD(cost)}.`;
  $('paste').value = '';
  render();
};

$('manual-open').onclick = () => { $('manual').hidden = !$('manual').hidden; };

$('manual-add').onclick = () => {
  const provider = $('m-provider').value;
  const model = $('m-model').value.trim();
  const agent = $('m-agent').value.trim();
  const input = +$('m-in').value || 0;
  const output = +$('m-out').value || 0;
  const msg = $('parse-msg');
  msg.className = 'msg';
  if (!model || !agent) { msg.textContent = 'Model + agent required.'; msg.classList.add('err'); return; }
  if (!input && !output) { msg.textContent = 'At least one token count required.'; msg.classList.add('err'); return; }
  const resolved = resolveModel(model) || model;
  const { cost, unknown } = computeCost(resolved, input, output);
  const ev = { ts: new Date().toISOString(), agent, model: resolved, input, output, cost_usd: cost, source: `manual-${provider}` };
  if (!addEvent(ev)) return;
  msg.classList.add('ok');
  msg.textContent = unknown ? `Added — model "${model}" not in table, cost $0.` : `Added — ${fmtUSD(cost)}.`;
  $('m-model').value = ''; $('m-in').value = ''; $('m-out').value = '';
  render();
};

$('export-csv').onclick = () => {
  const list = loadEvents();
  if (!list.length) return alert('No events yet.');
  const blob = new Blob([toCSV(list)], { type: 'text/csv' });
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url; a.download = `agent-cost-tracker-${new Date().toISOString().slice(0, 10)}.csv`;
  a.click(); URL.revokeObjectURL(url);
};

$('clear-all').onclick = () => {
  if (!confirm('Delete all local events? This cannot be undone.')) return;
  saveEvents([]); render();
};

render();

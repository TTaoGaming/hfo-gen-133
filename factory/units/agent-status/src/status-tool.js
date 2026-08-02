// status-tool.js — client for a single status page.
// v0 renders a synthetic demo agent so the landing page has something live
// to show on first paint. When /api/status/<slug> exists (Cloudflare Worker
// + KV), the client swaps to fetching real data.
//
// Storage: none client-side (unlike prompt-versioning-lite). Status data
// is server-authoritative — anything else invites forged uptime badges.

const $ = id => document.getElementById(id);

function synthDemo() {
  // Generate 60 heartbeats over the last hour with a plausible pattern:
  // mostly green, one yellow cluster, one red spike.
  const now = Date.now();
  const beats = [];
  for (let i = 59; i >= 0; i--) {
    const t = now - i * 60_000;
    let kind = 'ok', latency = 90 + Math.random() * 40;
    if (i >= 20 && i <= 23) kind = 'slow', latency = 700 + Math.random() * 300;
    if (i === 12 || i === 11) kind = 'miss', latency = 0;
    beats.push({ t, kind, latency });
  }
  const runs = beats.filter(b => b.kind !== 'miss').length;
  const errRate = ((60 - runs) / 60 * 100).toFixed(1) + '%';
  const uptime = ((runs / 60) * 100).toFixed(2) + '%';
  const latencies = beats.filter(b => b.latency > 0).map(b => b.latency).sort((a, b) => a - b);
  const p95 = Math.round(latencies[Math.floor(latencies.length * 0.95)] || 0) + 'ms';
  const lastRun = new Date(beats[beats.length - 1].t).toISOString().replace('T', ' ').slice(0, 16) + 'Z';
  return { beats, runs, errRate, uptime, p95, lastRun,
    incidents: [
      { start: new Date(now - 12 * 60_000).toISOString(),
        end: new Date(now - 10 * 60_000).toISOString(),
        title: 'Missed 2 consecutive heartbeats',
        resolved: true },
      { start: new Date(now - 24 * 60_000).toISOString(),
        end: new Date(now - 20 * 60_000).toISOString(),
        title: 'Elevated latency (p95 > 700ms)',
        resolved: true } ] };
}

function render(data) {
  const anyMiss = data.beats.some(b => b.kind === 'miss');
  const anySlow = data.beats.some(b => b.kind === 'slow');
  $('dot').className = 'status-dot' + (anyMiss ? ' red' : anySlow ? ' yellow' : '');
  $('headline').textContent = anyMiss
    ? 'Demo Agent has an active incident'
    : anySlow ? 'Demo Agent is degraded' : 'Demo Agent is operational';
  $('last-run').textContent = 'Last run: ' + data.lastRun;
  $('m-uptime').textContent = data.uptime;
  $('m-runs').textContent = data.runs + '/60';
  $('m-err').textContent = data.errRate;
  $('m-p95').textContent = data.p95;

  const hb = $('hb'); hb.innerHTML = '';
  data.beats.forEach(b => {
    const s = document.createElement('span');
    s.className = b.kind === 'ok' ? '' : b.kind;
    s.title = new Date(b.t).toISOString() + ' · ' +
      (b.kind === 'miss' ? 'missed' : Math.round(b.latency) + 'ms');
    hb.appendChild(s);
  });

  const inc = $('incidents');
  if (!data.incidents.length) {
    inc.innerHTML = '<p class="micro">No incidents in the last 7 days.</p>';
  } else {
    inc.innerHTML = data.incidents.map(i => `
      <div class="incident ${i.resolved ? 'resolved' : ''}">
        <p style="margin:0;font-weight:600">${i.title}</p>
        <p class="when">${i.start.slice(0, 16).replace('T', ' ')}Z
          → ${(i.end || 'ongoing').slice(0, 16).replace('T', ' ')}Z
          · ${i.resolved ? 'resolved' : 'ONGOING'}</p>
      </div>`).join('');
  }
}

async function hydrate() {
  try {
    const r = await fetch('/api/status/demo-agent');
    if (!r.ok) throw new Error('no api yet');
    render(await r.json());
  } catch {
    render(synthDemo());
  }
}
hydrate();

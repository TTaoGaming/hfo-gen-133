#!/usr/bin/env node
// verify-unit.mjs — HEAD-check the 5 canonical URLs for a unit and
// upgrade the ship's claim_status to VERIFIED (or FAILED) accordingly.
//
// Usage (from repo root):
//   node factory/scripts/verify-unit.mjs <slug>
//   node factory/scripts/verify-unit.mjs <slug> --base https://<slug>.pages.dev
//
// Emits a chain-row per verification pass.

import { readFile, writeFile, mkdir } from 'node:fs/promises';
import { existsSync } from 'node:fs';
import { join, dirname, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

const [, , slug, ...rest] = process.argv;
if (!slug) { console.error('usage: verify-unit <slug> [--base URL]'); process.exit(1); }
const baseFlag = rest.indexOf('--base');
const HERE = dirname(fileURLToPath(import.meta.url));
const REPO = resolve(HERE, '..', '..');
const UNIT = join(REPO, 'factory', 'units', slug);
const cfg = existsSync(join(UNIT, '.placeholder-config.json'))
  ? JSON.parse(await readFile(join(UNIT, '.placeholder-config.json'), 'utf8')) : {};
const base = baseFlag >= 0 ? rest[baseFlag + 1] : `https://${slug}.pages.dev`;

const CANONICAL = ['/', '/app.html', '/pricing', '/privacy.html', '/robots.txt'];
const results = [];
for (const path of CANONICAL) {
  const url = base.replace(/\/$/, '') + path;
  try {
    const r = await fetch(url, { method: 'HEAD', redirect: 'manual' });
    const ok = r.status === 200 || r.status === 301 || r.status === 302;
    results.push({ url, status: r.status, ok });
    console.log(`  ${ok ? '✔' : '✗'} ${r.status} ${url}`);
  } catch (e) {
    results.push({ url, status: 0, ok: false, error: e.message });
    console.log(`  ✗ ERR ${url} — ${e.message}`);
  }
}

const allOk = results.every(r => r.ok);
const SHIPS_DIR = join(REPO, 'state', 'factory_ships');
await mkdir(SHIPS_DIR, { recursive: true });
const now = new Date().toISOString();
const row = {
  schema_id: 'hfo.gen133.microsaas_ship.v0_1',
  event_type: 'MICROSAAS_UNIT_VERIFICATION',
  ts_utc: now,
  tool_slug: slug,
  base_url: base,
  claim_status: allOk ? 'VERIFIED' : 'FAILED',
  results
};
await writeFile(join(SHIPS_DIR, 'MICROSAAS_SHIPS.jsonl'),
  JSON.stringify(row) + '\n', { flag: 'a' });
console.log(`[verify-unit] ${allOk ? 'VERIFIED' : 'FAILED'} ${slug}`);
process.exit(allOk ? 0 : 3);

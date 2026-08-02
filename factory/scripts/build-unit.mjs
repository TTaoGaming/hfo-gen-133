#!/usr/bin/env node
// build-unit.mjs — layered builder.
//
// Reads the shared template at factory/microsaas_template/{src,public}, then
// overlays factory/units/<slug>/{src,public} on top (unit files win on
// collision), then substitutes {{TOKEN}} placeholders from the unit's
// .placeholder-config.json (falling back to the template's config for any
// key the unit doesn't override).
//
// Output goes to factory/units/<slug>/dist/, ready for
// `wrangler pages deploy dist --project-name <slug>`.
//
// Usage (from repo root):
//   node factory/scripts/build-unit.mjs <slug>
//   node factory/scripts/build-unit.mjs prompt-versioning-lite

import { readFile, writeFile, mkdir, readdir, stat, copyFile } from 'node:fs/promises';
import { existsSync } from 'node:fs';
import { join, dirname, relative, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

const SLUG = process.argv[2];
if (!SLUG) { console.error('usage: build-unit <slug>'); process.exit(1); }

const HERE = dirname(fileURLToPath(import.meta.url));
const FACTORY = resolve(HERE, '..');
const TEMPLATE = join(FACTORY, 'microsaas_template');
const UNIT = join(FACTORY, 'units', SLUG);
const OUT = join(UNIT, 'dist');

const TEXT_EXT = new Set(['.html', '.css', '.js', '.txt', '.xml', '.json', '.svg', '.md']);

async function loadCfg(dir) {
  const p = join(dir, '.placeholder-config.json');
  if (!existsSync(p)) return {};
  return JSON.parse(await readFile(p, 'utf8'));
}
const cfg = { ...(await loadCfg(TEMPLATE)), ...(await loadCfg(UNIT)) };
for (const [k, v] of Object.entries(process.env))
  if (k === k.toUpperCase() && typeof v === 'string') cfg[k] = v;

function sub(str) {
  return str.replace(/\{\{([A-Z0-9_]+)\}\}/g, (_, k) =>
    (k in cfg && cfg[k] != null) ? String(cfg[k]) : `[[MISSING:${k}]]`);
}

async function walk(dir, base = dir) {
  const out = [];
  if (!existsSync(dir)) return out;
  for (const entry of await readdir(dir)) {
    const p = join(dir, entry);
    const st = await stat(p);
    if (st.isDirectory()) out.push(...await walk(p, base));
    else out.push({ abs: p, rel: relative(base, p) });
  }
  return out;
}

// Build in layers: template first, then unit overrides.
async function overlay(srcRoot) {
  for (const [subdir] of [['src'], ['public']]) {
    const layer = join(srcRoot, subdir);
    for (const { abs, rel } of await walk(layer)) {
      const dest = join(OUT, rel);
      await mkdir(dirname(dest), { recursive: true });
      const dot = rel.lastIndexOf('.');
      const ext = dot === -1 ? '' : rel.slice(dot).toLowerCase();
      if (TEXT_EXT.has(ext)) {
        await writeFile(dest, sub(await readFile(abs, 'utf8')), 'utf8');
      } else {
        await copyFile(abs, dest);
      }
    }
  }
}

await mkdir(OUT, { recursive: true });
await overlay(TEMPLATE);
await overlay(UNIT);

// Missing-placeholder audit.
const missing = new Set();
for (const { abs, rel } of await walk(OUT)) {
  const dot = rel.lastIndexOf('.');
  const ext = dot === -1 ? '' : rel.slice(dot).toLowerCase();
  if (!TEXT_EXT.has(ext)) continue;
  const txt = await readFile(abs, 'utf8');
  for (const m of txt.matchAll(/\[\[MISSING:([A-Z0-9_]+)\]\]/g)) missing.add(m[1]);
}
if (missing.size) {
  console.error(`[build-unit ${SLUG}] MISSING placeholders:`);
  for (const k of missing) console.error('  -', k);
  process.exit(2);
}
console.log(`[build-unit] ✔ ${SLUG} → ${relative(process.cwd(), OUT)}`);

// Drives the Signal Refinery demo (hfopiano_v512 core) through window.HandPiano.injectRawLandmarks
// with a fixed, deterministic synthetic hand trace, and records a video of the run.
//
// Usage:
//   node record_gesture_run.mjs <baseUrl> <outFile.webm> <seed>
//
// seed selects the trace shape so a held-out variant can be produced deterministically
// without touching this script (seed=0 is the golden-master trace).

import { mkdirSync } from 'node:fs';
import { dirname } from 'node:path';
import { pathToFileURL } from 'node:url';

const PLAYWRIGHT_ENTRY = process.env.PLAYWRIGHT_ENTRY
  || 'C:/Dev/hfo_dev_2026_5_30/hfo_gen_130_forge/work/tooling/playwright/node_modules/playwright/index.mjs';
const { chromium } = await import(pathToFileURL(PLAYWRIGHT_ENTRY).href);

const [, , baseUrlArg, outFileArg, seedArg] = process.argv;
if (!baseUrlArg || !outFileArg) {
  console.error('usage: node record_gesture_run.mjs <baseUrl> <outFile.webm> [seed=0]');
  process.exit(2);
}
const baseUrl = baseUrlArg.replace(/\/$/, '');
const outFile = outFileArg;
const seed = Number(seedArg ?? 0);
mkdirSync(dirname(outFile), { recursive: true });

const DURATION_MS = 12000;
const FRAME_INTERVAL_MS = 33; // ~30Hz synthetic landmark stream

function buildHandFrame(tMs, seed, which) {
  // which: 0 = left hand, 1 = right hand. Deterministic sinusoidal path in normalized [0,1] space,
  // seed perturbs frequency/phase so held-out variants are reproducibly different from the golden trace.
  const t = tMs / 1000;
  const freq = 0.35 + seed * 0.12;
  const phase = which === 0 ? 0 : Math.PI * (0.6 + seed * 0.2);
  const cx = 0.5 + 0.28 * Math.sin(2 * Math.PI * freq * t + phase);
  const cy = 0.55 + 0.18 * Math.cos(2 * Math.PI * (freq * 0.7) * t + phase);
  // 21-point MediaPipe-style landmark set, all points offset from a moving centroid so the
  // hand silhouette stays coherent while it travels.
  const base = [
    [0, 0], [-0.03, -0.02], [-0.05, -0.05], [-0.06, -0.08], [-0.07, -0.10],
    [-0.02, -0.06], [-0.02, -0.11], [-0.02, -0.15], [-0.02, -0.18],
    [0.00, -0.06], [0.00, -0.12], [0.00, -0.16], [0.00, -0.19],
    [0.02, -0.06], [0.02, -0.11], [0.02, -0.15], [0.02, -0.18],
    [0.04, -0.05], [0.05, -0.09], [0.05, -0.12], [0.05, -0.15],
  ];
  const landmarks = base.map(([dx, dy], i) => ({
    x: cx + dx + 0.01 * Math.sin(2 * Math.PI * freq * t + i),
    y: cy + dy,
    z: 0,
  }));
  return { landmarks, handedness: which === 0 ? 'Left' : 'Right', confidence: 0.96 };
}

const run = async () => {
  const browser = await chromium.launch();
  const context = await browser.newContext({
    viewport: { width: 1280, height: 720 },
    recordVideo: { dir: dirname(outFile), size: { width: 1280, height: 720 } },
  });
  const page = await context.newPage();
  const consoleErrors = [];
  page.on('pageerror', (e) => consoleErrors.push(String(e)));
  page.on('console', (msg) => { if (msg.type() === 'error') consoleErrors.push(msg.text()); });

  await page.goto(`${baseUrl}/index.html`, { waitUntil: 'load' });
  await page.waitForFunction(() => typeof window.HandPiano?.injectRawLandmarks === 'function', { timeout: 15000 });

  // Dismiss the start gate if present so the piano/cursor UI is actually visible on camera.
  const startBtn = page.locator('.startGate wa-button, .startGate button').first();
  if (await startBtn.count().catch(() => 0)) {
    await startBtn.click({ timeout: 3000 }).catch(() => {});
  }

  const startedAt = Date.now();
  while (Date.now() - startedAt < DURATION_MS) {
    const tMs = Date.now() - startedAt;
    const left = buildHandFrame(tMs, seed, 0);
    const right = buildHandFrame(tMs, seed, 1);
    await page.evaluate(({ left, right, ts }) => {
      window.HandPiano.injectRawLandmarks([left, right], ts);
    }, { left, right, ts: tMs }).catch(() => {});
    await page.waitForTimeout(FRAME_INTERVAL_MS);
  }

  await context.close();
  await browser.close();

  // Playwright names the video file itself; find it and move/report the path.
  const { readdirSync, renameSync } = await import('node:fs');
  const dir = dirname(outFile);
  const produced = readdirSync(dir).filter((f) => f.endsWith('.webm') && f !== require_basename(outFile));
  function require_basename(p) { return p.split(/[\\/]/).pop(); }
  if (produced.length) {
    renameSync(`${dir}/${produced[produced.length - 1]}`, outFile);
  }

  console.log(JSON.stringify({ outFile, seed, durationMs: DURATION_MS, consoleErrors }, null, 2));
  if (consoleErrors.length) process.exitCode = 1;
};

run().catch((err) => { console.error(err); process.exit(1); });

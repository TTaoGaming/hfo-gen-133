#!/usr/bin/env node
/**
 * Deterministic builder for the operator-authorized Suika DLC 5-16 staging set.
 *
 * Each target is an independent moonfloof/suika-game clone. This builder only
 * adds the selected mechanic, its visible runtime HUD, and a focused Node test.
 * It never deploys, submits, posts, emails, or reads credentials.
 */
import { mkdirSync, readFileSync, writeFileSync } from 'node:fs';
import path from 'node:path';

const FORGE = 'C:/Dev/hfo_gen_133_forge';
const GAMES = path.join(FORGE, 'outputs', 'staged_sends', 'games');

const SPECS = [
  { n: 5, slug: 'timer_mode', mechanic: 'timer_mode', title: 'Blitz Clock', lineage: 'arcade score attack', accent: '#ffb703', instructions: 'Score as high as possible before the 3-minute clock expires.' },
  { n: 6, slug: 'gravity_flip', mechanic: 'gravity_flip', title: 'Gravity Sigil', lineage: 'action roguelite active skill', accent: '#8ecae6', instructions: 'Press SPACE to invert gravity for 5 seconds. Cooldown: 30 seconds.' },
  { n: 7, slug: 'boss_fruits', mechanic: 'boss_fruits', title: 'Boss Orchard', lineage: 'Vampire Survivors elite waves', accent: '#fb5607', instructions: 'Every 30 merges summons a boss. Make three tier-5 merges to banish it.' },
  { n: 8, slug: 'character_select', mechanic: 'character_select', title: 'Valkyrie Select', lineage: 'character-passive roguelite', accent: '#ff70a6', instructions: 'Keys 1/2/3 select Freya auto-merge, Raven delete, or Loki wildcard.' },
  { n: 9, slug: 'daily_seed', mechanic: 'daily_seed', title: 'Daily Seed', lineage: 'daily deterministic challenge', accent: '#90be6d', instructions: 'Everyone gets the same fruit sequence for today. Copy the seed URL to compare.' },
  { n: 10, slug: 'combo_burst', mechanic: 'combo_burst', title: 'Combo Burst', lineage: 'Vampire Survivors screen-clear proc', accent: '#f72585', instructions: 'Land 5 merges within 3 seconds to clear every bottom-tier fruit.' },
  { n: 11, slug: 'reverse_suika', mechanic: 'reverse_suika', title: 'Reverse Suika', lineage: 'rules inversion mutator', accent: '#c77dff', instructions: 'Start large. Matching fruits split downward into smaller, faster pieces.' },
  { n: 12, slug: 'gauntlet_mode', mechanic: 'gauntlet_mode', title: 'Falling Gauntlet', lineage: 'Vampire Survivors escalation curve', accent: '#ef476f', instructions: 'Automatic drops accelerate from 4.5 seconds toward a 0.65-second floor.' },
  { n: 13, slug: 'relic_draft', mechanic: 'relic_draft', title: 'Relic Draft', lineage: 'Slay the Spire relic cadence', accent: '#ffd166', instructions: 'Every 15 merges drafts Anchor, Crown, or Magnet and changes the run.' },
  { n: 14, slug: 'joker_hands', mechanic: 'joker_hands', title: 'Joker Hands', lineage: 'Balatro hand scoring', accent: '#06d6a0', instructions: 'Each five-drop hand scores Pair, Two Pair, Trips, Full House, or Quads bonuses.' },
  { n: 15, slug: 'evolution_frenzy', mechanic: 'evolution_frenzy', title: 'Evolution Frenzy', lineage: 'Vampire Survivors weapon evolution', accent: '#4cc9f0', instructions: 'Merges grant XP. Evolve at 5/10/15 merges for stronger starting drops.' },
  { n: 16, slug: 'curse_pacts', mechanic: 'curse_pacts', title: 'Curse Pacts', lineage: 'Slay the Spire risk-reward cards', accent: '#e63946', instructions: 'Every 12 merges invokes a rotating pact: power rises with a gravity curse.' },
];

function mechanicsSource(spec) {
  const config = JSON.stringify(spec);
  return `// HFO_MECHANIC_HOOK: ${spec.mechanic}\n` + String.raw`(function (root) {
  'use strict';
  const CONFIG = __CONFIG__;
  const CHARACTERS = ['FREYA', 'RAVEN', 'LOKI'];
  const RELICS = ['ANCHOR', 'CROWN', 'MAGNET'];
  const PACTS = [
    { name: 'BLOOD_PRICE', multiplier: 2, gravity: 1.25 },
    { name: 'GLASS_CANNON', multiplier: 3, gravity: 1.55 },
    { name: 'HEAVY_CROWN', multiplier: 4, gravity: 1.9 },
  ];

  function clone(value) { return JSON.parse(JSON.stringify(value)); }
  function mergeCount(fruitsMerged) { return (fruitsMerged || []).reduce((a, b) => a + Number(b || 0), 0); }
  function tickTimer(seconds, elapsedSeconds = 1) {
    const remaining = Math.max(0, Number(seconds) - Math.max(0, Number(elapsedSeconds)));
    return { remaining, ended: remaining === 0 };
  }
  function requestGravityFlip(state, nowMs) {
    const next = { ...state };
    if (Number(nowMs) < Number(state.cooldownUntil || 0)) return { ...next, accepted: false };
    next.accepted = true;
    next.flips = Number(state.flips || 0) + 1;
    next.activeUntil = Number(nowMs) + 5000;
    next.cooldownUntil = Number(nowMs) + 30000;
    return next;
  }
  function bossProgress(state, event, threshold = 30, chainNeed = 3) {
    const next = { ...state };
    if (event.type !== 'merge') return next;
    next.merges = Number(state.merges || 0) + 1;
    if (!state.activeBoss && next.merges % threshold === 0) {
      next.activeBoss = true;
      next.bossProgress = 0;
      next.bossSpawns = Number(state.bossSpawns || 0) + 1;
    } else if (state.activeBoss && event.tier === 5) {
      next.bossProgress = Number(state.bossProgress || 0) + 1;
      if (next.bossProgress >= chainNeed) {
        next.activeBoss = false;
        next.bossClears = Number(state.bossClears || 0) + 1;
      }
    }
    return next;
  }
  function selectCharacter(state, character) {
    if (!CHARACTERS.includes(character)) return { ...state };
    return { ...state, character };
  }
  function characterTransition(state, event) {
    let next = { ...state };
    if (event.type === 'select') return selectCharacter(next, event.character);
    if (event.type === 'drop') {
      next.drops = Number(state.drops || 0) + 1;
      if (state.character === 'RAVEN' && next.drops % 8 === 0) next.deleteReady = Number(state.deleteReady || 0) + 1;
      if (state.character === 'LOKI' && next.drops % 5 === 0) next.wildcardReady = Number(state.wildcardReady || 0) + 1;
    }
    if (event.type === 'merge') {
      next.merges = Number(state.merges || 0) + 1;
      if (state.character === 'FREYA' && next.merges % 8 === 0) next.autoMergeReady = Number(state.autoMergeReady || 0) + 1;
    }
    return next;
  }
  function seedFromText(text) {
    let h = 2166136261 >>> 0;
    for (const ch of String(text)) { h ^= ch.charCodeAt(0); h = Math.imul(h, 16777619); }
    return h >>> 0;
  }
  function dailySequence(seedText, count) {
    let a = seedFromText(seedText);
    const out = [];
    for (let i = 0; i < count; i++) {
      a |= 0; a = (a + 0x6D2B79F5) | 0;
      let t = Math.imul(a ^ (a >>> 15), 1 | a);
      t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
      out.push(Math.floor((((t ^ (t >>> 14)) >>> 0) / 4294967296) * 5));
    }
    return out;
  }
  function comboTransition(state, nowMs) {
    const timestamps = [...(state.timestamps || []), Number(nowMs)].filter(t => Number(nowMs) - t <= 3000);
    const burst = timestamps.length >= 5;
    return { ...state, timestamps: burst ? [] : timestamps, burstCount: Number(state.burstCount || 0) + (burst ? 1 : 0) };
  }
  function reverseOrder(values) { return [...values].reverse(); }
  function nextGauntletDelay(drops, start = 4500, step = 120, floor = 650) {
    return Math.max(floor, start - Number(drops) * step);
  }
  function draftRelic(mergeTotal) {
    if (mergeTotal <= 0 || mergeTotal % 15 !== 0) return null;
    return RELICS[(mergeTotal / 15 - 1) % RELICS.length];
  }
  function scorePokerHand(values) {
    if (!Array.isArray(values) || values.length !== 5) return { name: 'NO_HAND', bonus: 0 };
    const counts = Object.values(values.reduce((m, v) => (m[v] = (m[v] || 0) + 1, m), {})).sort((a, b) => b - a);
    if (counts[0] === 5) return { name: 'FIVE_KIND', bonus: 100 };
    if (counts[0] === 4) return { name: 'QUADS', bonus: 60 };
    if (counts[0] === 3 && counts[1] === 2) return { name: 'FULL_HOUSE', bonus: 45 };
    if (counts[0] === 3) return { name: 'TRIPS', bonus: 30 };
    if (counts[0] === 2 && counts[1] === 2) return { name: 'TWO_PAIR', bonus: 20 };
    if (counts[0] === 2) return { name: 'PAIR', bonus: 10 };
    return { name: 'HIGH_FRUIT', bonus: 3 };
  }
  function evolutionLevel(merges) { return Math.min(3, Math.floor(Number(merges) / 5)); }
  function pactForMerges(merges) {
    if (merges <= 0 || merges % 12 !== 0) return null;
    return clone(PACTS[(merges / 12 - 1) % PACTS.length]);
  }
  function createState() {
    return {
      variant: CONFIG.n, theme: CONFIG.slug, mechanic: CONFIG.mechanic,
      title: CONFIG.title, lineage: CONFIG.lineage, hook: 'HFO_MECHANIC_HOOK:' + CONFIG.mechanic,
      remaining: 180, ended: false, flips: 0, cooldownUntil: 0, activeUntil: 0,
      merges: 0, drops: 0, activeBoss: false, bossProgress: 0, bossSpawns: 0, bossClears: 0,
      character: 'FREYA', deleteReady: 0, wildcardReady: 0, autoMergeReady: 0,
      timestamps: [], burstCount: 0, delayMs: 4500, activeRelic: null,
      hand: [], lastHand: { name: 'NO_HAND', bonus: 0 }, bonusScore: 0,
      level: 0, activePact: null,
    };
  }
  function transition(state, event) {
    const s = state || createState();
    switch (CONFIG.mechanic) {
      case 'timer_mode':
        if (event.type === 'tick') return { ...s, ...tickTimer(s.remaining, event.seconds) };
        return { ...s };
      case 'gravity_flip':
        return event.type === 'flip' ? requestGravityFlip(s, event.nowMs) : { ...s };
      case 'boss_fruits':
        return bossProgress(s, event);
      case 'character_select':
        return characterTransition(s, event);
      case 'daily_seed':
        return { ...s };
      case 'combo_burst':
        return event.type === 'merge' ? comboTransition({ ...s, merges: s.merges + 1 }, event.nowMs) : { ...s };
      case 'reverse_suika':
        return { ...s };
      case 'gauntlet_mode': {
        if (event.type !== 'drop') return { ...s };
        const drops = s.drops + 1;
        return { ...s, drops, delayMs: nextGauntletDelay(drops) };
      }
      case 'relic_draft': {
        if (event.type !== 'merge') return { ...s };
        const merges = s.merges + 1;
        const relic = draftRelic(merges);
        return { ...s, merges, activeRelic: relic || s.activeRelic, bonusScore: s.bonusScore + (s.activeRelic === 'CROWN' ? 5 : 0) };
      }
      case 'joker_hands': {
        if (event.type !== 'drop') return { ...s };
        const hand = [...s.hand, event.tier].slice(-5);
        const scored = hand.length === 5 ? scorePokerHand(hand) : { name: 'BUILDING', bonus: 0 };
        return { ...s, drops: s.drops + 1, hand, lastHand: scored, bonusScore: s.bonusScore + scored.bonus };
      }
      case 'evolution_frenzy': {
        if (event.type !== 'merge') return { ...s };
        const merges = s.merges + 1;
        const level = evolutionLevel(merges);
        return { ...s, merges, level, bonusScore: s.bonusScore + level };
      }
      case 'curse_pacts': {
        if (event.type !== 'merge') return { ...s };
        const merges = s.merges + 1;
        return { ...s, merges, activePact: pactForMerges(merges) || s.activePact };
      }
      default: return { ...s };
    }
  }

  const API = { CONFIG, CHARACTERS, RELICS, PACTS, mergeCount, tickTimer, requestGravityFlip, bossProgress, selectCharacter, characterTransition, seedFromText, dailySequence, comboTransition, reverseOrder, nextGauntletDelay, draftRelic, scorePokerHand, evolutionLevel, pactForMerges, createState, transition };
  if (typeof module !== 'undefined' && module.exports) module.exports = API;
  else { root.DLCMechanics = API; installBrowserRuntime(API); }

  function installBrowserRuntime(M) {
    if (typeof Game === 'undefined' || typeof engine === 'undefined') return;
    let state = M.createState();
    let seenMerges = (Game.fruitsMerged || []).slice();
    let bossBody = null;
    let dailyIndex = 0;
    const originalCalculateScore = Game.calculateScore.bind(Game);
    const originalAddFruit = Game.addFruit.bind(Game);
    const originalFruitSizes = Game.fruitSizes.slice();

    Game.dlc = state;
    Game.fruitSizes.forEach((fruit, i) => { fruit.name = 'Rune Fruit ' + (i + 1); });

    const hud = document.getElementById('hfo-mechanic-state');
    const dynamicBodies = () => Composite.allBodies(engine.world).filter(b => !b.isStatic && Number.isInteger(b.sizeIndex));
    const removeBody = body => { if (body) Composite.remove(engine.world, body); };
    const removeTier = tier => dynamicBodies().filter(b => b.sizeIndex === tier).forEach(removeBody);
    const removeLargest = () => removeBody(dynamicBodies().sort((a, b) => b.circleRadius - a.circleRadius)[0]);
    const spawn = (tier, x = Game.width / 2, y = 120) => {
      const body = Game.generateFruitBody(x, y, Math.max(0, Math.min(Game.fruitSizes.length - 1, tier)));
      Composite.add(engine.world, body);
      return body;
    };
    const mostCommonTier = () => {
      const counts = dynamicBodies().reduce((m, b) => (m[b.sizeIndex] = (m[b.sizeIndex] || 0) + 1, m), {});
      return Number(Object.entries(counts).sort((a, b) => b[1] - a[1])[0]?.[0] || 0);
    };
    const publishState = () => { Game.dlc = state; updateHud(); };
    const applyScore = () => {
      const base = Game.score;
      let score = base + Number(state.bonusScore || 0);
      if (state.activePact) score = Math.floor(score * state.activePact.multiplier);
      Game.score = score;
      Game.elements.score.innerText = String(score);
    };
    const updateHud = () => {
      if (!hud) return;
      let detail = 'ready';
      if (M.CONFIG.mechanic === 'timer_mode') detail = state.remaining + 's remaining';
      if (M.CONFIG.mechanic === 'gravity_flip') detail = state.flips + ' flips used';
      if (M.CONFIG.mechanic === 'boss_fruits') detail = state.activeBoss ? 'BOSS ' + state.bossProgress + '/3' : state.merges + '/30 merges';
      if (M.CONFIG.mechanic === 'character_select') detail = state.character + ' · 1/2/3 to switch';
      if (M.CONFIG.mechanic === 'daily_seed') detail = 'seed ' + dailySeed;
      if (M.CONFIG.mechanic === 'combo_burst') detail = state.timestamps.length + '/5 combo · bursts ' + state.burstCount;
      if (M.CONFIG.mechanic === 'reverse_suika') detail = 'large → small';
      if (M.CONFIG.mechanic === 'gauntlet_mode') detail = 'next auto-drop ' + (state.delayMs / 1000).toFixed(2) + 's';
      if (M.CONFIG.mechanic === 'relic_draft') detail = state.activeRelic || (state.merges + '/15 to relic');
      if (M.CONFIG.mechanic === 'joker_hands') detail = state.lastHand.name + ' +' + state.lastHand.bonus;
      if (M.CONFIG.mechanic === 'evolution_frenzy') detail = 'evolution ' + state.level + '/3';
      if (M.CONFIG.mechanic === 'curse_pacts') detail = state.activePact?.name || (state.merges + '/12 to pact');
      hud.textContent = detail;
    };

    const dailySeed = new URLSearchParams(location.search).get('seed') || new Date().toISOString().slice(0, 10);
    if (M.CONFIG.mechanic === 'daily_seed') {
      Game.setNextFruitSize = function () {
        Game.nextFruitSize = M.dailySequence(dailySeed, ++dailyIndex).at(-1);
        Game.elements.nextFruitImg.src = './assets/img/circle' + Game.nextFruitSize + '.png';
      };
      Game.nextFruitSize = M.dailySequence(dailySeed, ++dailyIndex).at(-1);
      const share = document.getElementById('hfo-share-seed');
      if (share) share.href = location.origin + location.pathname + '?seed=' + encodeURIComponent(dailySeed);
    }
    if (M.CONFIG.mechanic === 'reverse_suika') {
      Game.fruitSizes = M.reverseOrder(originalFruitSizes);
      Game.currentFruitSize = 2;
      Game.nextFruitSize = 3;
      Game.setNextFruitSize = function () {
        Game.nextFruitSize = 2 + Math.floor(Math.random() * 4);
        Game.elements.nextFruitImg.src = Game.fruitSizes[Game.nextFruitSize].img;
      };
    }

    function handleActions(before, event) {
      if (M.CONFIG.mechanic === 'boss_fruits') {
        if (state.bossSpawns > before.bossSpawns) {
          bossBody = spawn(5);
          bossBody.isBoss = true;
          bossBody.sizeIndex = 99;
          bossBody.render.strokeStyle = '#ff4d00'; bossBody.render.lineWidth = 12;
        }
        if (before.activeBoss && !state.activeBoss) { removeBody(bossBody); bossBody = null; state.bonusScore += 250; }
      }
      if (M.CONFIG.mechanic === 'combo_burst' && state.burstCount > before.burstCount) { removeTier(0); state.bonusScore += 50; }
      if (M.CONFIG.mechanic === 'character_select') {
        if (state.deleteReady > before.deleteReady) removeLargest();
        if (state.wildcardReady > before.wildcardReady) Game.currentFruitSize = mostCommonTier();
        if (state.autoMergeReady > before.autoMergeReady) { spawn(0, Game.width / 2 - 12, 160); spawn(0, Game.width / 2 + 12, 160); }
      }
      if (M.CONFIG.mechanic === 'relic_draft' && state.activeRelic !== before.activeRelic) {
        if (state.activeRelic === 'ANCHOR') engine.gravity.y = 0.72;
        if (state.activeRelic === 'MAGNET') engine.gravity.x = 0.18;
      }
      if (M.CONFIG.mechanic === 'evolution_frenzy' && state.level > before.level) Game.currentFruitSize = Math.min(4, state.level);
      if (M.CONFIG.mechanic === 'curse_pacts' && state.activePact !== before.activePact && state.activePact) engine.gravity.y = state.activePact.gravity;
      applyScore();
      publishState();
    }

    Game.calculateScore = function () {
      originalCalculateScore();
      const counts = Game.fruitsMerged || [];
      for (let tier = 0; tier < counts.length; tier++) {
        const delta = Number(counts[tier] || 0) - Number(seenMerges[tier] || 0);
        for (let i = 0; i < delta; i++) {
          const before = clone(state);
          state = M.transition(state, { type: 'merge', tier, nowMs: Date.now() });
          handleActions(before, { type: 'merge', tier });
        }
      }
      seenMerges = counts.slice();
      applyScore();
    };
    Game.addFruit = function (x) {
      const ready = Game.stateIndex === 1;
      const tier = Game.currentFruitSize;
      originalAddFruit(x);
      if (!ready) return;
      const before = clone(state);
      state = M.transition(state, { type: 'drop', tier, nowMs: Date.now() });
      handleActions(before, { type: 'drop', tier });
    };

    if (M.CONFIG.mechanic === 'timer_mode') {
      setInterval(() => {
        if (Game.stateIndex === 0 || Game.stateIndex === 3) return;
        state = M.transition(state, { type: 'tick', seconds: 1 }); publishState();
        if (state.ended && Game.stateIndex !== 3) Game.loseGame();
      }, 1000);
    }
    if (M.CONFIG.mechanic === 'gravity_flip') {
      addEventListener('keydown', event => {
        if (event.code !== 'Space') return;
        event.preventDefault();
        const before = state; state = M.transition(state, { type: 'flip', nowMs: Date.now() });
        if (state.flips > before.flips) {
          engine.gravity.y = -Math.abs(engine.gravity.y || 1);
          setTimeout(() => { engine.gravity.y = Math.abs(engine.gravity.y || 1); }, 5000);
        }
        publishState();
      });
    }
    if (M.CONFIG.mechanic === 'character_select') {
      addEventListener('keydown', event => {
        const pick = { Digit1: 'FREYA', Digit2: 'RAVEN', Digit3: 'LOKI' }[event.code];
        if (!pick) return;
        state = M.transition(state, { type: 'select', character: pick }); publishState();
      });
    }
    if (M.CONFIG.mechanic === 'gauntlet_mode') {
      const autoDrop = () => {
        if (Game.stateIndex === 1) Game.addFruit(70 + Math.random() * (Game.width - 140));
        setTimeout(autoDrop, state.delayMs);
      };
      setTimeout(autoDrop, state.delayMs);
    }
    publishState();
  }
})(typeof self !== 'undefined' ? self : globalThis);
`.replace('__CONFIG__', config);
}

function testSource(spec) {
  const common = `import { test } from 'node:test';\nimport assert from 'node:assert/strict';\nimport { createRequire } from 'node:module';\nconst require = createRequire(import.meta.url);\nconst M = require('../mechanics.js');\n\ntest('variant metadata binds the mechanic hook', () => {\n  assert.equal(M.CONFIG.n, ${spec.n});\n  assert.equal(M.CONFIG.mechanic, '${spec.mechanic}');\n  assert.equal(M.createState().hook, 'HFO_MECHANIC_HOOK:${spec.mechanic}');\n});\n\n`;
  const cases = {
    timer_mode: `test('timer decrements and ends at zero', () => {\n  assert.deepEqual(M.tickTimer(180, 1), { remaining: 179, ended: false });\n  assert.deepEqual(M.tickTimer(1, 2), { remaining: 0, ended: true });\n});`,
    gravity_flip: `test('SPACE transition flips once and enforces 30s cooldown', () => {\n  const first = M.requestGravityFlip({ flips: 0, cooldownUntil: 0 }, 1000);\n  assert.equal(first.accepted, true); assert.equal(first.activeUntil, 6000); assert.equal(first.cooldownUntil, 31000);\n  const blocked = M.requestGravityFlip(first, 5000); assert.equal(blocked.accepted, false); assert.equal(blocked.flips, 1);\n});`,
    boss_fruits: `test('30 merges spawn a boss and three tier-5 chain links clear it', () => {\n  let s = M.createState();\n  for (let i = 0; i < 30; i++) s = M.bossProgress(s, { type: 'merge', tier: 0 });\n  assert.equal(s.activeBoss, true); assert.equal(s.bossSpawns, 1);\n  for (let i = 0; i < 3; i++) s = M.bossProgress(s, { type: 'merge', tier: 5 });\n  assert.equal(s.activeBoss, false); assert.equal(s.bossClears, 1);\n});`,
    character_select: `test('three characters expose distinct state-changing passives', () => {\n  let freya = M.selectCharacter(M.createState(), 'FREYA'); for (let i=0;i<8;i++) freya=M.characterTransition(freya,{type:'merge'}); assert.equal(freya.autoMergeReady,1);\n  let raven = M.selectCharacter(M.createState(), 'RAVEN'); for (let i=0;i<8;i++) raven=M.characterTransition(raven,{type:'drop'}); assert.equal(raven.deleteReady,1);\n  let loki = M.selectCharacter(M.createState(), 'LOKI'); for (let i=0;i<5;i++) loki=M.characterTransition(loki,{type:'drop'}); assert.equal(loki.wildcardReady,1);\n});`,
    daily_seed: `test('date seed is deterministic, changes across dates, and stays in drop range', () => {\n  const a=M.dailySequence('2026-08-02',12), b=M.dailySequence('2026-08-02',12), c=M.dailySequence('2026-08-03',12);\n  assert.deepEqual(a,b); assert.notDeepEqual(a,c); assert.ok(a.every(v=>v>=0&&v<5));\n});`,
    combo_burst: `test('five merges inside three seconds fire one burst and reset the window', () => {\n  let s=M.createState(); [0,500,1000,1500,2500].forEach(nowMs=>{s=M.comboTransition(s,nowMs)});\n  assert.equal(s.burstCount,1); assert.deepEqual(s.timestamps,[]);\n});`,
    reverse_suika: `test('tier table is reversed so a normal +1 merge shrinks fruit', () => {\n  const radii=[24,32,40,56,64,72,84,96,128,160,192]; const reversed=M.reverseOrder(radii);\n  assert.deepEqual(reversed,[192,160,128,96,84,72,64,56,40,32,24]); assert.ok(reversed[3]>reversed[4]);\n});`,
    gauntlet_mode: `test('automatic drop delay accelerates toward but never below floor', () => {\n  assert.equal(M.nextGauntletDelay(0),4500); assert.equal(M.nextGauntletDelay(10),3300); assert.equal(M.nextGauntletDelay(100),650);\n});`,
    relic_draft: `test('relic draft fires every 15 merges and cycles three relics', () => {\n  assert.equal(M.draftRelic(14),null); assert.equal(M.draftRelic(15),'ANCHOR'); assert.equal(M.draftRelic(30),'CROWN'); assert.equal(M.draftRelic(45),'MAGNET');\n});`,
    joker_hands: `test('Balatro-style hand classifier awards distinct bonuses', () => {\n  assert.deepEqual(M.scorePokerHand([1,1,2,2,2]),{name:'FULL_HOUSE',bonus:45});\n  assert.deepEqual(M.scorePokerHand([1,1,2,3,4]),{name:'PAIR',bonus:10});\n  assert.ok(M.scorePokerHand([7,7,7,7,2]).bonus>M.scorePokerHand([1,1,2,3,4]).bonus);\n});`,
    evolution_frenzy: `test('merge XP evolves at 5, 10, and 15 without exceeding level 3', () => {\n  assert.equal(M.evolutionLevel(4),0); assert.equal(M.evolutionLevel(5),1); assert.equal(M.evolutionLevel(10),2); assert.equal(M.evolutionLevel(15),3); assert.equal(M.evolutionLevel(99),3);\n});`,
    curse_pacts: `test('pacts trigger each 12 merges and rotate rising risk/reward', () => {\n  assert.equal(M.pactForMerges(11),null); assert.deepEqual(M.pactForMerges(12),M.PACTS[0]); assert.deepEqual(M.pactForMerges(24),M.PACTS[1]); assert.deepEqual(M.pactForMerges(36),M.PACTS[2]);\n});`,
  };
  return common + cases[spec.mechanic] + '\n';
}

function packageSource(spec) {
  return JSON.stringify({
    name: `hfo-suika-dlc-${spec.n}-${spec.slug}`,
    version: '1.0.0', private: true, license: 'Unlicense',
    description: `${spec.title}: ${spec.instructions}`,
    scripts: { test: 'node --test test/mechanic.test.mjs', serve: `python -m http.server ${8100 + spec.n} --bind 127.0.0.1` },
  }, null, 2) + '\n';
}

function htmlFor(original, spec) {
  const title = `HFO Suika DLC ${spec.n} — ${spec.title}`;
  const style = `<style id="hfo-dlc-style">\n#hfo-dlc-banner{max-width:640px;margin:0 auto;background:#15151f;color:#fff;border-bottom:4px solid ${spec.accent};padding:12px 16px;font-family:system-ui,sans-serif;line-height:1.35}#hfo-dlc-banner strong{color:${spec.accent};font-size:20px}#hfo-dlc-banner small{display:block;color:#ddd;margin-top:4px}#hfo-share-seed{color:${spec.accent}}\n</style>`;
  const share = spec.mechanic === 'daily_seed' ? ` <a id="hfo-share-seed" href="">share seed</a>` : '';
  const banner = `<section id="hfo-dlc-banner" data-mechanic-hook="${spec.mechanic}"><strong>SUIKA DLC ${spec.n}: ${spec.title}</strong><small>${spec.instructions} · ${spec.lineage}${share}</small><small id="hfo-mechanic-state">loading mechanic…</small></section>`;
  return original
    .replace(/<title>[^<]*<\/title>/, `<title>${title}</title>`)
    .replace('</head>', `${style}\n</head>`)
    .replace('<body>', `<body>\n  ${banner}`)
    .replace('<script type="text/javascript" src="./index.js?v=4"></script>', `<script type="text/javascript" src="./index.js?v=4"></script>\n  <script type="text/javascript" src="./mechanics.js?v=${spec.n}"></script>`);
}

for (const spec of SPECS) {
  const dir = path.join(GAMES, `suika_dlc_${spec.n}_${spec.slug}`);
  const indexJsPath = path.join(dir, 'index.js');
  const indexHtmlPath = path.join(dir, 'index.html');
  const originalJs = readFileSync(indexJsPath, 'utf8');
  const originalHtml = readFileSync(indexHtmlPath, 'utf8');
  if (!originalJs.includes("const Game =")) throw new Error(`upstream Game entrypoint missing: ${dir}`);
  if (!originalHtml.includes('./index.js?v=4')) throw new Error(`upstream script marker missing: ${dir}`);

  writeFileSync(indexJsPath, `// HFO_MECHANIC_HOOK: ${spec.mechanic}\n${originalJs}`, 'utf8');
  writeFileSync(indexHtmlPath, htmlFor(originalHtml, spec), 'utf8');
  writeFileSync(path.join(dir, 'mechanics.js'), mechanicsSource(spec), 'utf8');
  writeFileSync(path.join(dir, 'package.json'), packageSource(spec), 'utf8');
  mkdirSync(path.join(dir, 'test'), { recursive: true });
  writeFileSync(path.join(dir, 'test', 'mechanic.test.mjs'), testSource(spec), 'utf8');
  writeFileSync(path.join(dir, 'VARIANT.md'), `# Suika DLC ${spec.n}: ${spec.title}\n\n- Mechanic: \`${spec.mechanic}\`\n- Hook: \`HFO_MECHANIC_HOOK:${spec.mechanic}\`\n- Lineage: ${spec.lineage}\n- Play: ${spec.instructions}\n- Upstream: moonfloof/suika-game at c30848ed79f7c23e54a89e3e58a993b4fd991d14\n- License: Unlicense (public domain); Matter.js remains MIT.\n- Distribution state: Cloudflare Pages staging only. No marketplace submission.\n`, 'utf8');
  console.log(`built ${spec.n}\t${spec.mechanic}\t${dir}`);
}

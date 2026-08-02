# itch.io publish runbook — all staged titles

generated_utc: 2026-08-02T18:22:35Z  (clock_source=host_read)

## 0. One-time setup

```
1. Download the itch.io butler CLI for this OS from https://itchio.itch.io/butler
2. Unzip and put the `butler` binary on PATH (or reference it by full path below).
3. Run: butler login   (opens a browser, stores an API key in the butler config dir)
4. Verify: butler version
5. Then the butler_command in this plan can be run as-is from the repo root.
NOTE: this host does NOT have butler installed (verified `command not found`, 16:10Z 2026-08-03) — this skill does not download or install it (unapproved external fetch); the operator installs it by hand using the steps above.
```

## 1. Known blocker

itch.io project pages require at least one screenshot before they can go public (`visibility: draft` in every `itch_manifest.json` here is a symptom of this — `cover_image_path` is `MISSING_NEEDS_SCREENSHOT` for every title). Screenshots must be captured per title before `butler push` output can be flipped from draft to public on itch.io's side; butler itself will happily push the build either way.

## 2. Per-title push commands

### Hex Flip  (`001_hex_flip`)

```
butler push --if-changed C:/Dev/hfo_gen_133_forge/outputs/pages/games/games/001_hex_flip ttaogaming/hex-flip:html5
```

### Ice Slide  (`002_ice_slide`)

```
butler push --if-changed C:/Dev/hfo_gen_133_forge/outputs/pages/games/games/002_ice_slide ttaogaming/ice-slide:html5
```

### Infinite Runner  (`003_infinite_runner`)

```
butler push --if-changed C:/Dev/hfo_gen_133_forge/outputs/pages/games/games/003_infinite_runner ttaogaming/infinite-runner:html5
```

### Light Trail  (`004_light_trail`)

```
butler push --if-changed C:/Dev/hfo_gen_133_forge/outputs/pages/games/games/004_light_trail ttaogaming/light-trail:html5
```

### Magnetic Orbs  (`005_magnetic_orbs`)

```
butler push --if-changed C:/Dev/hfo_gen_133_forge/outputs/pages/games/games/005_magnetic_orbs ttaogaming/magnetic-orbs:html5
```

### Match 3  (`006_match3`)

```
butler push --if-changed C:/Dev/hfo_gen_133_forge/outputs/pages/games/games/006_match3 ttaogaming/match3:html5
```

### Maze Runner  (`007_maze_runner`)

```
butler push --if-changed C:/Dev/hfo_gen_133_forge/outputs/pages/games/games/007_maze_runner ttaogaming/maze-runner:html5
```

### Memory Match  (`008_memory_match`)

```
butler push --if-changed C:/Dev/hfo_gen_133_forge/outputs/pages/games/games/008_memory_match ttaogaming/memory-match:html5
```

### Number Crush  (`009_number_crush`)

```
butler push --if-changed C:/Dev/hfo_gen_133_forge/outputs/pages/games/games/009_number_crush ttaogaming/number-crush:html5
```

### Paint Blast  (`010_paint_blast`)

```
butler push --if-changed C:/Dev/hfo_gen_133_forge/outputs/pages/games/games/010_paint_blast ttaogaming/paint-blast:html5
```

### Pipe Puzzle  (`011_pipe_puzzle`)

```
butler push --if-changed C:/Dev/hfo_gen_133_forge/outputs/pages/games/games/011_pipe_puzzle ttaogaming/pipe-puzzle:html5
```

### Platformer Hop  (`012_platformer_hop`)

```
butler push --if-changed C:/Dev/hfo_gen_133_forge/outputs/pages/games/games/012_platformer_hop ttaogaming/platformer-hop:html5
```

### Reaction Test  (`013_reaction_test`)

```
butler push --if-changed C:/Dev/hfo_gen_133_forge/outputs/pages/games/games/013_reaction_test ttaogaming/reaction-test:html5
```

### Rhythm Tap  (`014_rhythm_tap`)

```
butler push --if-changed C:/Dev/hfo_gen_133_forge/outputs/pages/games/games/014_rhythm_tap ttaogaming/rhythm-tap:html5
```

### Slide Puzzle  (`015_slide_puzzle`)

```
butler push --if-changed C:/Dev/hfo_gen_133_forge/outputs/pages/games/games/015_slide_puzzle ttaogaming/slide-puzzle:html5
```

### Slingshot  (`016_slingshot`)

```
butler push --if-changed C:/Dev/hfo_gen_133_forge/outputs/pages/games/games/016_slingshot ttaogaming/slingshot:html5
```

### Snake  (`017_snake`)

```
butler push --if-changed C:/Dev/hfo_gen_133_forge/outputs/pages/games/games/017_snake ttaogaming/snake:html5
```

### Snake Neon  (`018_snake_neon`)

```
butler push --if-changed C:/Dev/hfo_gen_133_forge/outputs/pages/games/games/018_snake_neon ttaogaming/snake-neon:html5
```

### Target Aim  (`019_target_aim`)

```
butler push --if-changed C:/Dev/hfo_gen_133_forge/outputs/pages/games/games/019_target_aim ttaogaming/target-aim:html5
```

### Tic-Tac-Toe  (`020_tic_tac_toe`)

```
butler push --if-changed C:/Dev/hfo_gen_133_forge/outputs/pages/games/games/020_tic_tac_toe ttaogaming/tic-tac-toe:html5
```

### Tower Drop  (`021_tower_drop`)

```
butler push --if-changed C:/Dev/hfo_gen_133_forge/outputs/pages/games/games/021_tower_drop ttaogaming/tower-drop:html5
```

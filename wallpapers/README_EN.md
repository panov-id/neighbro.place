# NEIGHBRO — wallpaper & banner generator

Builds on-brand NEIGHBRO wallpapers and banners from a matrix of
**themes × modes × languages × background styles × content × formats**. Everything
is code-drawn (SVG/CSS) on the landing's own fonts and colors; AI art backgrounds
are an optional layer.

## Contents
- `catalog.mjs` — single source of truth: themes, palettes, copy (6 langs), formats, styles.
- `template.html` — render page: draws one layout, fonts loaded from `../landing/fonts/`.
- `render.mjs` — Puppeteer: walks the matrix, writes PNGs + `output/index.html` gallery.
- `ai-prompts/PROMPTS_EN.md` / `PROMPTS_RU.md` — Lexica / Midjourney background prompts.
- `docker/` — Chromium image + run script (nothing is installed on the host).

## Matrix axes
- **Themes:** gold (default), crimson, teal, azure, violet
- **Modes:** dark, light
- **Languages:** en, ru, fr, de, es, el
- **Background styles:** plain, glow, mesh, grid, rings, contour, houses, steps, art (AI)
- **Content:** `mark` (logo only), `brand` (logo + eyebrow), `full` (+ headline)
- **Formats:** ultrawide 3440×1440, desktop 1080p/1440p/4K, iPhone 1179×2556,
  Android 1080×2340, stories 1080×1920, post 1080×1080, OG 1200×630, hero 1920×1080

## Run
```bash
# Full default set (5 themes × 2 modes × 8 styles × all formats, en)
./docker/run.sh

# Targeted
./docker/run.sh --formats ultrawide,mobileIPhone --themes gold,teal \
  --modes dark --styles glow,mesh,rings --content full --langs en,ru

# With AI background art
./docker/run.sh --formats ultrawide --styles art --art art/twilight.jpg
```
Output lands in `output/<category>/...png`; browse via `output/index.html`.

Flags: `--formats --themes --modes --langs --styles --content --art --out --limit`
(comma-separated, `all` = everything). No flags = curated default.

## Quick preview without Docker
Open `template.html?spec=<base64 JSON>` in a browser, JSON e.g.
`{"format":"ultrawide","theme":"gold","mode":"dark","lang":"en","style":"glow","content":"full"}`.

## AI backgrounds (hybrid)
1. Run the prompts from `ai-prompts/PROMPTS_EN.md` in Lexica at the right aspect ratio.
2. Save the picks into `art/…jpg`.
3. Render with `--styles art --art art/your.jpg` — logo/text/scrim composite on top.

## Future iterations
Add a language/theme/format/style to `catalog.mjs` and rerun `run.sh`. The script is
idempotent and redraws everything.

# NEIGHBRO — AI background prompts (Lexica Art / Midjourney / SDXL)

These generate the **background art** only. Text, logo and headline are composited
on top by the code generator (`template.html` → `render.mjs`), so keep the center /
upper area calm and leave negative space. Do **not** ask the model to render text.

## Brand direction (paste as a preamble if the tool allows a style block)
Warm dark minimalism, "cozy speakeasy" mood, quiet and premium, editorial, calm.
Near-black warm-brown ground (#0c0b09), warm cream light, a single muted-gold accent
(#c6a24e). Anti-social-media: no crowds, no logos, no UI. Soft, intimate,
architectural. Grain and depth over saturation.

## Aspect ratios per target
- Ultrawide 34": `--ar 21:9`
- Desktop: `--ar 16:9`
- Mobile / Stories: `--ar 9:16` (Midjourney) — Lexica: pick the tallest portrait
- Square post: `--ar 1:1`
- OG / hero banner: `--ar 16:9` or `1.91:1`

Append quality tags for Midjourney: `--style raw --v 6 --q 2`. For Lexica, add
`highly detailed, cinematic lighting, 8k` and pick the SDXL/Flux model.

---

## Palette variants
Swap the accent word to match the landing themes:
gold `muted gold #c6a24e` · crimson `deep crimson red #e0342b` ·
teal `deep teal green #1fb39a` · azure `soft azure blue #3d84d6` ·
violet `muted violet #9b5de5`. Keep the ground near-black warm for dark, warm
cream/#e9e6dd for light versions.

---

## 1 — Twilight courtyard (flagship, dark)
> A quiet residential courtyard at blue hour, warm glowing windows scattered across
> dark building facades, seen from a distance, cinematic depth of field, soft bokeh
> of golden window light, near-black warm-brown atmosphere, muted gold highlights,
> minimal, moody, intimate, film grain, negative space in the sky, no people, no
> text, editorial photography --ar 21:9 --style raw

## 2 — Aerial neighborhood at night
> Abstract aerial view of a small neighborhood at night, softly glowing golden
> streetlights forming a gentle constellation, dark warm ground, out-of-focus,
> minimal, calm, lots of negative space, muted gold on near-black, cinematic,
> subtle grain, no text --ar 16:9

## 3 — Two windows, one street (intimacy)
> Two warmly lit apartment windows facing each other across a narrow dark street at
> dusk, cozy golden interior light, minimal, tender, cinematic, shallow focus,
> near-black warm palette, muted gold glow, film grain, no people visible, no text
> --ar 9:16

## 4 — Abstract gold light field
> Minimal abstract background, soft flowing bands of muted gold light dissolving into
> near-black warm-brown darkness, gentle gradient, faint grain, calm, premium,
> spacious, cinematic, no objects, no text --ar 21:9

## 5 — Contour map of a district
> Elegant topographic contour lines of a city district, thin muted-gold lines on a
> near-black warm ground, minimal cartographic art, precise, quiet, spacious, a
> single soft glow, no labels, no text --ar 16:9

## 6 — Doorway with warm light
> A single dark doorway spilling a warm golden light onto a quiet cobblestone
> street at night, minimal, cinematic, intimate, deep shadows, muted gold accent,
> near-black warm atmosphere, film grain, no people, no text --ar 9:16

## 7 — Rooftop terrace, wine hour (moments)
> A softly lit rooftop terrace at dusk, two empty chairs and a small table, warm
> golden string lights bokeh, city silhouette far below, calm and intimate,
> cinematic, near-black warm palette, muted gold, shallow depth, film grain, no
> people, no text --ar 21:9

## 8 — Fading paper / ephemeral (Fade concept)
> Abstract minimal composition of soft dissolving particles of warm golden light
> drifting and fading into dark warm-brown void, sense of impermanence, calm,
> premium, cinematic, fine grain, lots of negative space, no text --ar 16:9

## 9 — Light-mode / concrete
> Minimal warm off-white concrete texture (#e9e6dd), soft daylight, a single muted
> gold geometric arc, calm, editorial, spacious, subtle grain, architectural, no
> text --ar 21:9

## 10 — Window grid, morning (light)
> Facade of warm cream apartment building in soft morning light, orderly grid of
> windows, minimal, calm, editorial architectural photography, muted gold reflection
> in one window, warm off-white palette, spacious, no people, no text --ar 16:9

---

## Tips
- Prefer **portrait crops** for mobile — generate at 9:16, the overlay upper-third
  will sit above the subject.
- If Lexica adds accidental text, add negatives: `no text, no watermark, no letters,
  no signage, no UI`.
- Save picks into `wallpapers/art/<style-or-theme>/<name>.jpg`; the generator reads
  them when `style=art` and `--art <path>` is passed.

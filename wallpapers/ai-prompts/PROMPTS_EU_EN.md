# NEIGHBRO — landing background prompts, European slant (Midjourney)

Backgrounds only. **No people, no text, no logos, no UI.** Keep the center/upper
area calm with negative space — headline and logo are composited on top by the
landing. Same brand as the main prompts, but the settings lean **European**:
Haussmann Paris, Amsterdam canal houses, Lisbon azulejo facades, Italian piazzas,
old-town cobblestone, terracotta rooftops, wrought-iron balconies.

## Brand style block (paste as preamble)
Warm dark minimalism, cozy speakeasy mood, quiet and premium, editorial, calm.
Near-black warm-brown ground (#0c0b09), warm cream light, a single muted-gold accent
(#c6a24e). Soft, intimate, architectural. Film grain and depth over saturation.
European city, old town, no crowds, no signage, no text.

Append for Midjourney: `--style raw --v 6 --q 2`

---

## Landing image slots (generate one pick per slot)

### splash — European twilight courtyard  ·  `--ar 21:9`
> A quiet European inner courtyard at blue hour, old-town Parisian / Viennese
> apartment block, warm glowing windows scattered across dark stone facades with
> wrought-iron balconies, seen from a distance, cinematic depth of field, soft golden
> window bokeh, near-black warm-brown atmosphere, muted gold highlights, minimal,
> moody, intimate, film grain, negative space in the sky, no people, no text,
> editorial photography --ar 21:9 --style raw --v 6 --q 2

### hero — European street facade  ·  `--ar 16:9`
> A Haussmann-style Parisian apartment facade at dusk, elegant rows of tall windows,
> a few warmly lit, zinc rooftops, wrought-iron balconies, near-black warm-brown
> palette, muted gold interior glow, cinematic, shallow depth, film grain, calm,
> spacious, negative space, no people, no text, editorial architectural photography
> --ar 16:9 --style raw --v 6 --q 2

### card_say — two windows across a narrow lane  ·  `--ar 16:11`
> Two warmly lit apartment windows facing each other across a narrow European old-town
> cobblestone lane at dusk, Lisbon / Bologna alley, cozy golden interior light,
> minimal, tender, cinematic, shallow focus, near-black warm palette, muted gold glow,
> film grain, no people, no text --ar 16:11 --style raw --v 6 --q 2

### card_match — rooftop terrace over the old town  ·  `--ar 16:11`
> A small rooftop terrace at dusk overlooking a European old town of terracotta
> rooftops, two empty chairs and a low table, string of warm golden lights, distant
> church spire, near-black warm-brown twilight, muted gold accents, intimate,
> cinematic, film grain, negative space, no people, no text --ar 16:11 --style raw --v 6 --q 2

### card_fade — aerial European neighborhood at night  ·  `--ar 16:11`
> Abstract aerial view of a small European old-town neighborhood at night, winding
> cobblestone streets and squares, softly glowing golden streetlights forming a gentle
> constellation, dark warm ground, out-of-focus, minimal, calm, muted gold on
> near-black, cinematic, subtle grain, no text --ar 16:11 --style raw --v 6 --q 2

### texture — cobblestone / contour  ·  `--ar 16:9`
> Elegant abstract texture of European old-town cobblestone under warm low light,
> thin muted-gold highlights on a near-black warm-brown ground, minimal, quiet,
> spacious, faint film grain, no objects, no text --ar 16:9 --style raw --v 6 --q 2

---

## When your picks are ready
Drop the chosen images into **`neighbro.place/landing/img-src/`** named exactly:
`splash · hero · card_say · card_match · card_fade · texture` (any of .png/.jpg).
I compress them to web files (`landing/img/*.jpg`) and wire them into the landing.

// Single source of truth for the wallpaper/banner generator.
// Imported by both the browser template (template.html) and the Node renderer
// (render.mjs). Keep it framework-free and side-effect-free.

// Accent themes mirror landing/index.html. "" is the signature gold default.
export const THEMES = {
  gold:    { accent: "#c6a24e", accentInk: "#1a1509" },
  crimson: { accent: "#e0342b", accentInk: "#fdeceb" },
  teal:    { accent: "#1fb39a", accentInk: "#04201c" },
  azure:   { accent: "#3d84d6", accentInk: "#eaf2ff" },
  violet:  { accent: "#9b5de5", accentInk: "#f3ecfd" },
};

// Ground palettes per mode (accent stays constant, injected from THEMES).
export const MODES = {
  dark: {
    bg: "#0c0b09", panel: "#14120e", panel2: "#26221a",
    border: "#3a331f", fg: "#ede8dd", muted: "#8a8172", muted2: "#928979",
  },
  light: {
    bg: "#e9e6dd", panel: "#f4f1e8", panel2: "#ded9cc",
    border: "#1e1b14", fg: "#181510", muted: "#5f5a4e", muted2: "#5c5749",
  },
};

// Localized copy pulled from landing/index.html i18n table.
// `loop` is the present-tense product loop (Say·Match·Fade) — it reads as a live,
// shipped product, unlike the old coming-soon status. `tags` feed the moment chips.
export const COPY = {
  en: { eyebrow: "The art of being nearby", h1a: "Good neighbors.", h1b: "Real moments.",
    loop: "Say · Match · Fade", tags: ["morning espresso company", "a partner for tennis", "wine on the terrace", "new in the city"] },
  ru: { eyebrow: "Искусство быть рядом", h1a: "Хорошие соседи.", h1b: "Живые моменты.",
    loop: "Скажи · Совпало · Исчезло", tags: ["компания за утренним эспрессо", "партнёр по теннису", "вино на террасе", "новичок в городе"] },
  fr: { eyebrow: "L'art d'être tout près", h1a: "Bons voisins.", h1b: "De vrais moments.",
    loop: "Dis · Match · Efface", tags: ["compagnie pour l'espresso du matin", "un partenaire de tennis", "un verre sur la terrasse", "nouveau en ville"] },
  de: { eyebrow: "Die Kunst, nah zu sein", h1a: "Gute Nachbarn.", h1b: "Echte Momente.",
    loop: "Sag · Match · Verblasse", tags: ["Gesellschaft für den Morgen-Espresso", "ein Tennispartner", "Wein auf der Terrasse", "neu in der Stadt"] },
  es: { eyebrow: "El arte de estar cerca", h1a: "Buenos vecinos.", h1b: "Momentos reales.",
    loop: "Di · Match · Desvanece", tags: ["compañía para el espresso de la mañana", "una pareja de tenis", "vino en la terraza", "nuevo en la ciudad"] },
  el: { eyebrow: "Η τέχνη του να είσαι κοντά", h1a: "Καλοί γείτονες.", h1b: "Αληθινές στιγμές.",
    loop: "Πες · Ταίριαξε · Σβήσε", tags: ["παρέα για πρωινό espresso", "παρτενέρ για τένις", "κρασί στη βεράντα", "νέος στην πόλη"] },
};

// Output formats grouped by category. size in physical pixels (scale 1).
export const FORMATS = {
  ultrawide:  { w: 3440, h: 1440, category: "ultrawide", label: "Ultrawide 34\" 21:9" },
  desktopFHD: { w: 1920, h: 1080, category: "desktop",   label: "Desktop 1080p" },
  desktopQHD: { w: 2560, h: 1440, category: "desktop",   label: "Desktop 1440p" },
  desktopUHD: { w: 3840, h: 2160, category: "desktop",   label: "Desktop 4K" },
  mobileIPhone: { w: 1179, h: 2556, category: "mobile",  label: "iPhone 15/16" },
  mobileAndroid:{ w: 1080, h: 2340, category: "mobile",  label: "Android FHD+" },
  storiesVertical: { w: 1080, h: 1920, category: "social", label: "Stories 9:16" },
  postSquare:  { w: 1080, h: 1080, category: "social",   label: "Post 1:1" },
  ogBanner:    { w: 1200, h: 630,  category: "banner",   label: "OG / social banner" },
  heroBanner:  { w: 1920, h: 1080, category: "banner",   label: "Hero banner" },
};

// Background styles. `art` styles expect an AI-generated image behind the
// overlay (see ai-prompts/); the rest are fully code-drawn and need no assets.
export const STYLES = {
  plain:    { label: "Flat + vignette", needsArt: false },
  glow:     { label: "Accent glow", needsArt: false },
  mesh:     { label: "Soft mesh blobs", needsArt: false },
  grid:     { label: "Mono dot grid", needsArt: false },
  rings:    { label: "Concentric rings", needsArt: false },
  contour:  { label: "Topographic contours", needsArt: false },
  houses:   { label: "House-icon pattern", needsArt: false },
  steps:    { label: "Say·Match·Fade infographic", needsArt: false },
  splash:   { label: "Splash — brand + neighbor feed", needsArt: false },
  art:      { label: "AI art background", needsArt: true },
};

// Content presets: how much branding sits on the wallpaper.
export const CONTENT = {
  mark:  "logo only",       // symbol + wordmark, minimal
  brand: "logo + eyebrow",  // symbol + wordmark + eyebrow line
  full:  "logo + headline", // symbol + wordmark + eyebrow + headline
};

export const THEME_KEYS = Object.keys(THEMES);
export const MODE_KEYS = Object.keys(MODES);
export const LANG_KEYS = Object.keys(COPY);
export const FORMAT_KEYS = Object.keys(FORMATS);
export const STYLE_KEYS = Object.keys(STYLES);

// Build a resolved palette for one (theme, mode) pair.
export function palette(themeKey, modeKey) {
  return { ...MODES[modeKey], ...THEMES[themeKey], mode: modeKey, theme: themeKey };
}
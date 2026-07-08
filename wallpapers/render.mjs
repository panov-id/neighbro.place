// Headless renderer: walks the (theme × mode × lang × style × content × format)
// matrix from catalog.mjs and writes a PNG per combination via Puppeteer.
//
// Runs inside Docker (see docker/). Never install Chromium on the host.
//
// Usage (all flags optional, comma-separated multi-values, "all" = everything):
//   node render.mjs \
//     --formats ultrawide,mobileIPhone --themes gold,teal --modes dark,light \
//     --langs en,ru --styles glow,mesh,rings --content brand \
//     --art art/twilight.jpg --out output --limit 0
//
// With no flags it renders a sensible curated default set (see DEFAULTS).

import { fileURLToPath } from "node:url";
import { dirname, resolve, join } from "node:path";
import { mkdir, writeFile } from "node:fs/promises";
import puppeteer from "puppeteer";
import {
  FORMATS, THEME_KEYS, MODE_KEYS, LANG_KEYS, FORMAT_KEYS, STYLE_KEYS,
} from "./catalog.mjs";

const HERE = dirname(fileURLToPath(import.meta.url));

function parseArgs(argv) {
  const a = {};
  for (let i = 0; i < argv.length; i++) {
    if (argv[i].startsWith("--")) { a[argv[i].slice(2)] = argv[i + 1]; i++; }
  }
  return a;
}
function list(val, all) {
  if (val === undefined) return null;
  if (val === "all") return all;
  return val.split(",").map((s) => s.trim()).filter(Boolean);
}

const args = parseArgs(process.argv.slice(2));

// Curated default matrix — broad enough to give 20+ per category to choose from,
// small enough to render quickly. Override any axis with a flag.
const DEFAULTS = {
  formats: FORMAT_KEYS,
  themes: THEME_KEYS,                       // 5 accents
  modes: MODE_KEYS,                         // dark + light
  langs: ["en"],                            // one language by default
  styles: ["glow", "mesh", "rings", "contour", "grid", "houses", "steps", "plain"],
  content: ["brand"],
};

const sel = {
  formats: list(args.formats, FORMAT_KEYS) || DEFAULTS.formats,
  themes: list(args.themes, THEME_KEYS) || DEFAULTS.themes,
  modes: list(args.modes, MODE_KEYS) || DEFAULTS.modes,
  langs: list(args.langs, LANG_KEYS) || DEFAULTS.langs,
  styles: list(args.styles, STYLE_KEYS) || DEFAULTS.styles,
  content: list(args.content, ["mark", "brand", "full"]) || DEFAULTS.content,
};
const jpeg = args.jpeg !== undefined;
const jpegQuality = args.quality ? parseInt(args.quality, 10) : 88;
const artUrl = args.art ? "file://" + resolve(process.cwd(), args.art) : null;
const outDir = resolve(HERE, args.out || "output");
const limit = args.limit ? parseInt(args.limit, 10) : 0;

function specs() {
  const out = [];
  for (const format of sel.formats)
    for (const theme of sel.themes)
      for (const mode of sel.modes)
        for (const style of sel.styles)
          for (const content of sel.content)
            for (const lang of sel.langs)
              out.push({ format, theme, mode, style, content, lang, artUrl });
  return out;
}

function fileName(s) {
  const cat = FORMATS[s.format].category;
  const ext = jpeg ? "jpg" : "png";
  return join(cat, `${s.format}_${s.style}_${s.theme}_${s.mode}_${s.content}_${s.lang}.${ext}`);
}

async function main() {
  const all = specs();
  const jobs = limit > 0 ? all.slice(0, limit) : all;
  console.log(`Rendering ${jobs.length} wallpapers → ${outDir}`);

  const browser = await puppeteer.launch({
    headless: "new",
    // file:// ES-module imports are CORS-blocked without this flag.
    args: ["--no-sandbox", "--disable-setuid-sandbox", "--force-color-profile=srgb",
      "--allow-file-access-from-files"],
  });
  const page = await browser.newPage();
  const templateUrl = "file://" + join(HERE, "template.html");

  let done = 0;
  const catsSeen = new Set();
  for (const spec of jobs) {
    const fmt = FORMATS[spec.format];
    await page.setViewport({ width: fmt.w, height: fmt.h, deviceScaleFactor: 1 });
    await page.goto(templateUrl, { waitUntil: "networkidle0" });
    await page.waitForFunction(() => typeof window.__render === "function", { timeout: 10000 });
    await page.evaluate((s) => window.__render(s), spec);
    await page.evaluate(() => document.fonts.ready);
    // Small settle for font paint.
    await new Promise((r) => setTimeout(r, 60));

    const rel = fileName(spec);
    const dest = join(outDir, rel);
    await mkdir(dirname(dest), { recursive: true });
    await page.screenshot(jpeg
      ? { path: dest, type: "jpeg", quality: jpegQuality }
      : { path: dest, type: "png" });
    catsSeen.add(fmt.category);
    done++;
    if (done % 10 === 0 || done === jobs.length) console.log(`  ${done}/${jobs.length}`);
  }
  await browser.close();

  await writeGallery(jobs);
  console.log(`Done. ${done} files. Categories: ${[...catsSeen].join(", ")}`);
  console.log(`Open output/styles.html (code/splash) or output/index.html (hub).`);
}

// A lightweight gallery so the whole set can be eyeballed and picked from.
async function writeGallery(jobs) {
  const byCat = {};
  for (const s of jobs) {
    const cat = FORMATS[s.format].category;
    (byCat[cat] ||= []).push(fileName(s).split("/").join("/"));
  }
  const sections = Object.entries(byCat).map(([cat, files]) => `
    <h2>${cat} <small>(${files.length})</small></h2>
    <div class="grid">${files.map((f) => `
      <figure><img loading="lazy" src="${f}"><figcaption>${f.split("/").pop()}</figcaption></figure>`).join("")}</div>`).join("");
  const html = `<!doctype html><meta charset="utf-8"><title>NEIGHBRO wallpapers</title>
  <style>
    body{background:#0c0b09;color:#ede8dd;font-family:system-ui,sans-serif;margin:0;padding:24px}
    h1{font-weight:800;letter-spacing:.04em}h2{margin-top:40px;text-transform:capitalize;color:#c6a24e}
    small{color:#8a8172}
    .grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:16px}
    figure{margin:0;background:#14120e;border:1px solid #3a331f;border-radius:10px;overflow:hidden}
    img{width:100%;display:block;background:#000}
    figcaption{font-size:11px;color:#8a8172;padding:8px;word-break:break-all}
  </style>
  <h1>NEIGHBRO — wallpapers &amp; banners</h1><p style="color:#8a8172">${jobs.length} renders</p>${sections}`;
  await writeFile(join(outDir, "styles.html"), html);
}

main().catch((e) => { console.error(e); process.exit(1); });

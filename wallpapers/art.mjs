// Composites the curated AI backgrounds (art/manifest.mjs) into their target
// formats with the NEIGHBRO logo/headline overlaid, cover-cropped to each exact
// size. Runs inside Docker (see docker/run-art.sh).
//
// Usage:
//   node art.mjs [--langs en,ru] [--only courtyard,windows] [--out output]

import { fileURLToPath } from "node:url";
import { dirname, resolve, join } from "node:path";
import { mkdir, writeFile, access } from "node:fs/promises";
import puppeteer from "puppeteer";
import { FORMATS } from "./catalog.mjs";
import { ART } from "./art/manifest.mjs";

const HERE = dirname(fileURLToPath(import.meta.url));

function parseArgs(argv) {
  const a = {};
  for (let i = 0; i < argv.length; i++) if (argv[i].startsWith("--")) { a[argv[i].slice(2)] = argv[i + 1]; i++; }
  return a;
}
const args = parseArgs(process.argv.slice(2));
const langs = (args.langs || "en").split(",").map((s) => s.trim()).filter(Boolean);
const only = args.only ? args.only.split(",").map((s) => s.trim()) : null;
const outDir = resolve(HERE, args.out || "output");
const theme = args.theme || "gold";

async function exists(p) { try { await access(p); return true; } catch { return false; } }

async function main() {
  const items = ART.filter((a) => !only || only.includes(a.file.replace(/\.png$/, "")));
  const jobs = [];
  for (const a of items) {
    const artPath = join(HERE, "art", a.file);
    if (!(await exists(artPath))) { console.warn(`skip ${a.file} (missing — run art/prepare.sh)`); continue; }
    for (const format of a.formats)
      for (const lang of langs)
        jobs.push({
          style: "art", artUrl: "file://" + artPath, format, theme, mode: "dark",
          lang, content: a.content, placement: a.placement, scrim: a.scrim, tone: a.tone, chip: a.chip,
          _name: a.file.replace(/\.png$/, ""), _title: a.name,
        });
  }
  console.log(`Compositing ${jobs.length} art wallpapers → ${outDir}/art`);

  const browser = await puppeteer.launch({
    headless: "new",
    // file:// ES-module imports are CORS-blocked without this flag.
    args: ["--no-sandbox", "--disable-setuid-sandbox", "--force-color-profile=srgb",
      "--allow-file-access-from-files"],
  });
  const page = await browser.newPage();
  const templateUrl = "file://" + join(HERE, "template.html");

  let done = 0;
  for (const spec of jobs) {
    const fmt = FORMATS[spec.format];
    await page.setViewport({ width: fmt.w, height: fmt.h, deviceScaleFactor: 1 });
    await page.goto(templateUrl, { waitUntil: "networkidle0" });
    await page.waitForFunction(() => typeof window.__render === "function", { timeout: 10000 });
    await page.evaluate((s) => window.__render(s), spec);
    await page.evaluate(() => document.fonts.ready);
    await new Promise((r) => setTimeout(r, 80));
    const dest = join(outDir, "art", spec._name, `${spec.format}_${spec.lang}.png`);
    await mkdir(dirname(dest), { recursive: true });
    await page.screenshot({ path: dest, type: "png" });
    done++;
    if (done % 5 === 0 || done === jobs.length) console.log(`  ${done}/${jobs.length}`);
  }
  await browser.close();
  await writeGallery(jobs);
  console.log(`Done. Open output/art/index.html`);
}

async function writeGallery(jobs) {
  const byArt = {};
  for (const s of jobs) (byArt[s._name] ||= { title: s._title, files: [] }).files.push(`${s._name}/${s.format}_${s.lang}.png`);
  const sections = Object.entries(byArt).map(([, v]) => `
    <h2>${v.title} <small>(${v.files.length})</small></h2>
    <div class="grid">${v.files.map((f) => `<figure><img loading="lazy" src="${f}"><figcaption>${f.split("/").pop()}</figcaption></figure>`).join("")}</div>`).join("");
  const html = `<!doctype html><meta charset="utf-8"><title>NEIGHBRO art wallpapers</title>
  <style>body{background:#0c0b09;color:#ede8dd;font-family:system-ui,sans-serif;margin:0;padding:24px}
  h1{font-weight:800}h2{margin-top:40px;color:#c6a24e}small{color:#8a8172}
  .grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(320px,1fr));gap:16px}
  figure{margin:0;background:#14120e;border:1px solid #3a331f;border-radius:10px;overflow:hidden}
  img{width:100%;display:block;background:#000}figcaption{font-size:11px;color:#8a8172;padding:8px}</style>
  <h1>NEIGHBRO — AI art wallpapers</h1><p style="color:#8a8172">${jobs.length} renders</p>${sections}`;
  await writeFile(join(outDir, "art", "index.html"), html);
}

main().catch((e) => { console.error(e); process.exit(1); });

// One social preview per language, drawn from the landing's own dictionary.
//
//   og/docker/run-all.sh                 # every language → landing/og-image[-<lang>].jpg
//   og/docker/run-all.sh --only ka       # just one, for a look
//
// Why per language: the sheet carries the tagline, and an English tagline under a
// Georgian headline is exactly the seam a social preview shows off. The taglines
// are not repeated here — they are read out of index.html, the same dictionary
// the pages are built from, so a translation edited in one place cannot leave a
// stale image behind.
//
// Playwright rather than the puppeteer image render.mjs uses: that image is not
// pullable from here, and this repo already keeps a browser for its checks. The
// output is the same 1200×630 JPEG at quality 90.
import { chromium } from "playwright";
import { createServer } from "node:http";
import { readFile } from "node:fs/promises";
import { dirname, extname, join, normalize, resolve } from "node:path";
import { fileURLToPath } from "node:url";

const HERE = dirname(fileURLToPath(import.meta.url));
const REPO = process.env.OG_REPO || resolve(HERE, "..");
const LANDING = join(REPO, "landing");
const DEFAULT_LANGUAGE = "en";
const PORT = 8331;

const only = process.argv.includes("--only")
  ? process.argv[process.argv.indexOf("--only") + 1]
  : null;

const site = process.env.OG_SITE || "NEIGHBRO.PLACE";

// The dictionary lives inside index.html; landing/i18n-dictionary.mjs is the one
// place that knows how to get it out, and both the page generator and the
// completeness check already use it.
const { readDictionary } = await import(join(LANDING, "i18n-dictionary.mjs"));
const dictionary = readDictionary(await readFile(join(LANDING, "index.html"), "utf-8"));

const TYPES = {
  ".html": "text/html; charset=utf-8",
  ".css": "text/css; charset=utf-8",
  ".woff2": "font/woff2",
  ".jpg": "image/jpeg",
  ".png": "image/png",
  ".svg": "image/svg+xml",
};

const server = createServer(async (request, response) => {
  const path = normalize(decodeURIComponent(new URL(request.url, "http://x").pathname));
  try {
    const body = await readFile(join(REPO, path));
    response.writeHead(200, { "content-type": TYPES[extname(path)] ?? "application/octet-stream" });
    response.end(body);
  } catch {
    response.writeHead(404).end("not found");
  }
});
await new Promise((done) => server.listen(PORT, "127.0.0.1", done));

const languages = Object.keys(dictionary).filter((language) => !only || language === only);
if (languages.length === 0) {
  console.error(only ? `нет такого языка: ${only}` : "в словаре нет языков");
  process.exit(2);
}

const browser = await chromium.launch();
let failures = 0;

for (const language of languages) {
  const tagline = dictionary[language].eyebrow;
  if (!tagline) {
    console.log(`  ✗ ${language} — в словаре нет ключа eyebrow`);
    failures++;
    continue;
  }

  const page = await browser.newPage({ viewport: { width: 1200, height: 630 }, deviceScaleFactor: 1 });
  await page.goto(`http://127.0.0.1:${PORT}/og/template.html`, { waitUntil: "load" });
  await page.waitForFunction(() => typeof window.__render === "function", { timeout: 10000 });
  await page.evaluate((spec) => window.__render(spec), { caption: [tagline, site] });
  await page.evaluate(() => document.fonts.ready);
  await page.waitForTimeout(300);

  // Which font actually drew the caption, asked rather than assumed. A script we
  // have no face for falls back to whatever the container happens to carry, and
  // that gets baked into a JPEG nobody will re-examine.
  const client = await page.context().newCDPSession(page);
  await client.send("DOM.enable");
  await client.send("CSS.enable");
  const { root } = await client.send("DOM.getDocument");
  const { nodeId } = await client.send("DOM.querySelector", { nodeId: root.nodeId, selector: "#caption div:first-child" });
  const used = nodeId
    ? (await client.send("CSS.getPlatformFontsForNode", { nodeId })).fonts
    : [];
  const strangers = used.filter((font) =>
    font.glyphCount > 2 && !/JetBrains Mono|Noto Sans Georgian|Noto Sans Armenian|Golos Text|Unbounded/i.test(font.familyName));

  const suffix = language === DEFAULT_LANGUAGE ? "" : `-${language}`;
  const destination = join(LANDING, `og-image${suffix}.jpg`);
  await page.screenshot({ path: destination, type: "jpeg", quality: 90 });
  await page.close();

  if (strangers.length) failures++;
  console.log(
    `  ${strangers.length ? "✗" : "✓"} ${language.padEnd(3)} ${JSON.stringify(tagline).padEnd(34)}` +
      ` → og-image${suffix}.jpg   ${used.map((f) => `${f.familyName} (${f.glyphCount})`).join(", ")}`,
  );
}

await browser.close();
server.close();

if (failures) {
  console.error(`\nне своим шрифтом: ${failures} — картинка невоспроизводима, чинить шрифты, а не рендер`);
  process.exit(1);
}
console.log(`\nнарисовано: ${languages.length}`);

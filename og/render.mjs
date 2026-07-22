// Renders the OG image (1200×630) from template.html via Puppeteer.
// Runs inside Docker (see docker/run.sh). Never installs Chromium on the host.
//
// Usage:
//   node render.mjs [--caption "TAGLINE|SITE"] [--out output]   # candidate PNG
//   node render.mjs --pick final                                # writes ../landing/og-image.jpg

import { fileURLToPath } from "node:url";
import { dirname, resolve, join } from "node:path";
import { mkdir } from "node:fs/promises";
import puppeteer from "puppeteer";

const HERE = dirname(fileURLToPath(import.meta.url));

function parseArgs(argv) {
  const a = {};
  for (let i = 0; i < argv.length; i++) if (argv[i].startsWith("--")) { a[argv[i].slice(2)] = argv[i + 1]; i++; }
  return a;
}
const args = parseArgs(process.argv.slice(2));
const outDir = resolve(HERE, args.out || "output");
const caption = args.caption
  ? args.caption.split("|").map((s) => s.trim())
  : ["THE ART OF BEING NEARBY", "NEIGHBRO.PLACE"];

async function main() {
  const browser = await puppeteer.launch({
    headless: "new",
    args: ["--no-sandbox", "--disable-setuid-sandbox", "--force-color-profile=srgb",
      "--allow-file-access-from-files"],
  });
  const page = await browser.newPage();
  await page.setViewport({ width: 1200, height: 630, deviceScaleFactor: 1 });
  await page.goto("file://" + join(HERE, "template.html"), { waitUntil: "networkidle0" });
  await page.waitForFunction(() => typeof window.__render === "function", { timeout: 10000 });
  await page.evaluate((s) => window.__render(s), { caption });
  await page.evaluate(() => document.fonts.ready);
  await new Promise((r) => setTimeout(r, 60));

  if (args.pick) {
    const dest = resolve(HERE, "..", "landing", "og-image.jpg");
    await page.screenshot({ path: dest, type: "jpeg", quality: 90 });
    console.log(`Wrote ${dest}`);
  } else {
    await mkdir(outDir, { recursive: true });
    const dest = join(outDir, "og_photo.png");
    await page.screenshot({ path: dest, type: "png" });
    console.log(`Wrote ${dest}`);
  }
  await browser.close();
}

main().catch((e) => { console.error(e); process.exit(1); });

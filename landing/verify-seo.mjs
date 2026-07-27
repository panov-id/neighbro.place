#!/usr/bin/env node
// Check a generated site the way a crawler meets it — checklist items F1–F3 of
// docs/SEO_AND_ANALYTICS_*.md. Run against a directory build-pages.mjs has
// already written to, so it inspects files rather than a running site: none of
// these three questions needs a deployment to answer.
//
//   node landing/verify-seo.mjs <builtDirectory>
//
//   F1  a language page carries translated HTML without executing JavaScript
//   F2  hreflang is reciprocal and every alternate exists as a file
//   F3  every sitemap URL exists as a file, and the XML is well formed
//
// Exits non-zero on the first failing check, so it can gate a deploy later.

import { readFileSync, existsSync } from "node:fs";
import { join } from "node:path";
import { readDictionary } from "./i18n-dictionary.mjs";

const builtDirectory = process.argv[2];
if (!builtDirectory) {
  console.error("usage: verify-seo.mjs <builtDirectory>");
  process.exit(1);
}

const failures = [];
const note = (ok, message) => {
  console.log(`   ${ok ? "ok  " : "FAIL"} ${message}`);
  if (!ok) failures.push(message);
};

// A page's own file: the root is the default language, the rest live in folders.
const pagePath = (language, defaultLanguage) =>
  language === defaultLanguage
    ? join(builtDirectory, "index.html")
    : join(builtDirectory, language, "index.html");

const dictionary = readDictionary(readFileSync(join(builtDirectory, "index.html"), "utf8"));
const languages = Object.keys(dictionary);
// The root page states its own language, which is what the generator decided.
const rootHtml = readFileSync(join(builtDirectory, "index.html"), "utf8");
const defaultLanguage = rootHtml.match(/<html[^>]*\blang="([^"]+)"/)?.[1] ?? "en";

console.log(`site: ${builtDirectory}`);
console.log(`languages: ${languages.length} (root = ${defaultLanguage})\n`);

// --- F1: translated HTML in the response, no JavaScript involved --------------
console.log("F1 — translated HTML without JS");
for (const language of languages) {
  const path = pagePath(language, defaultLanguage);
  if (!existsSync(path)) {
    note(false, `${language}: no page at ${path}`);
    continue;
  }
  const html = readFileSync(path, "utf8");
  const declared = html.match(/<html[^>]*\blang="([^"]+)"/)?.[1];
  // A heading string this language actually uses, taken from the dictionary
  // rather than hardcoded — the check must not know the copy.
  const heading = dictionary[language]?.h1a;
  const strings = [heading].filter((value) => typeof value === "string" && value.length > 2);
  const present = strings.every((value) => html.includes(value));
  note(
    declared === language && present,
    `${language}: lang="${declared}"${present ? "" : ", translated copy missing from the HTML"}`,
  );
}

// --- F2: reciprocal hreflang, every alternate a real file ---------------------
console.log("\nF2 — reciprocal hreflang");
const alternatesOf = (html) =>
  [...html.matchAll(/<link[^>]+rel="alternate"[^>]*>/g)]
    .map((match) => ({
      lang: match[0].match(/hreflang="([^"]+)"/)?.[1],
      href: match[0].match(/href="([^"]+)"/)?.[1],
    }))
    .filter((entry) => entry.lang && entry.href);

// href -> the file it should resolve to, relative to the built directory.
const fileForHref = (href) => {
  const path = new URL(href).pathname.replace(/^\/+/, "");
  return join(builtDirectory, path === "" ? "index.html" : join(path, "index.html"));
};

for (const language of languages) {
  const path = pagePath(language, defaultLanguage);
  if (!existsSync(path)) continue;
  const alternates = alternatesOf(readFileSync(path, "utf8"));
  const listed = alternates.map((entry) => entry.lang);
  const missingLanguages = languages.filter((candidate) => !listed.includes(candidate));
  const hasDefault = listed.includes("x-default");
  const brokenTargets = alternates
    .filter((entry) => !existsSync(fileForHref(entry.href)))
    .map((entry) => entry.href);
  note(
    missingLanguages.length === 0 && hasDefault && brokenTargets.length === 0,
    `${language}: ${alternates.length} alternates` +
      (missingLanguages.length ? `, missing ${missingLanguages.join(",")}` : "") +
      (hasDefault ? "" : ", no x-default") +
      (brokenTargets.length ? `, dead: ${brokenTargets.join(" ")}` : ""),
  );
}

// --- F3: the sitemap lists only URLs that exist ------------------------------
console.log("\nF3 — sitemap");
const sitemapPath = join(builtDirectory, "sitemap.xml");
if (!existsSync(sitemapPath)) {
  note(false, "no sitemap.xml (expected for a production build)");
} else {
  const sitemap = readFileSync(sitemapPath, "utf8");
  const urls = [...sitemap.matchAll(/<loc>([^<]+)<\/loc>/g)].map((match) => match[1]);
  // Well-formed enough to be parsed by a crawler: one urlset, balanced <url>.
  const opening = (sitemap.match(/<url>/g) ?? []).length;
  const closing = (sitemap.match(/<\/url>/g) ?? []).length;
  note(sitemap.includes("<urlset"), "has a urlset root");
  note(opening === closing && opening === urls.length, `${urls.length} <url> entries, balanced`);

  const missing = urls.filter((url) => {
    const path = new URL(url).pathname.replace(/^\/+/, "");
    const candidate = path === ""
      ? join(builtDirectory, "index.html")
      : path.endsWith(".html")
      ? join(builtDirectory, path)
      : join(builtDirectory, path, "index.html");
    return !existsSync(candidate);
  });
  note(missing.length === 0, missing.length ? `dead URLs: ${missing.join(" ")}` : "every URL exists");
}

console.log("");
if (failures.length) {
  console.error(`FAILED — ${failures.length} check(s)`);
  process.exit(1);
}
console.log("F1–F3 OK");

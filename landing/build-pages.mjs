#!/usr/bin/env node
// Generate one static page per language, plus the sitemap.
//
// The landing translates itself in the browser, which means a crawler only ever sees one
// language. This turns the single page into a folder per language — /de/, /fr/, … — where
// the translated text is already in the HTML response, with reciprocal hreflang between
// them. English lives at the root; every other language gets a folder.
//
// Usage:  node landing/build-pages.mjs <targetDirectory>
//
// The target directory is modified in place: its index.html is read, rewritten in the
// default language, and the other languages are written into subfolders. Deploy runs this
// against its staging copy, so the repository itself keeps a single source page.
//
// Environment:
//   SITE_ORIGIN   absolute origin used in canonical, hreflang and sitemap URLs
//                 (default: https://sosed.place)

import { readFileSync, writeFileSync, mkdirSync } from "node:fs";
import { join } from "node:path";
import { readDictionary } from "./i18n-dictionary.mjs";

const targetDirectory = process.argv[2];
if (!targetDirectory) {
  console.error("usage: build-pages.mjs <targetDirectory>");
  process.exit(2);
}

const origin = (process.env.SITE_ORIGIN || "https://neighbro.place").replace(/\/+$/, "");
const DEFAULT_LANGUAGE = "en";

// The brand is written the same way everywhere, so search results always show one name.
// The dictionary's `brand` key stays translated for the page body, but the title, where
// the brand competes for recognition, is always this.
const BRAND = "neighbro";

const sourceFile = join(targetDirectory, "index.html");
const sourceHtml = readFileSync(sourceFile, "utf8");
const dictionary = readDictionary(sourceHtml);

const languages = Object.keys(dictionary);
if (!languages.includes(DEFAULT_LANGUAGE)) {
  throw new Error(`the default language ${DEFAULT_LANGUAGE} is missing from the dictionary`);
}

// A language page is served from /<language>/, so every relative reference in it would
// resolve inside that folder. A single <base href="/"> fixes all of them at once —
// including url() inside the inline stylesheet, which rewriting attributes would miss.
// That only holds while the page has no in-page anchors: with a base, href="#section"
// would jump to the root document instead of staying put. Fail loudly if one appears.
// Matched on the anchor element itself, not on the bare attribute: the same text appears
// in comments explaining this very rule, and a comment must not fail the build.
const anchors = sourceHtml.match(/<a\b[^>]*\bhref="#[^"]*"/g);
if (anchors) {
  throw new Error(
    `in-page anchors are incompatible with <base href="/">: ${[...new Set(anchors)].join(", ")}\n` +
    `either drop the anchors or switch this generator to rewriting relative URLs instead.`
  );
}

const pageUrl = (language) =>
  language === DEFAULT_LANGUAGE ? `${origin}/` : `${origin}/${language}/`;

const escapeText = (value) =>
  String(value).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");

const escapeAttribute = (value) => escapeText(value).replace(/"/g, "&quot;");

// og:locale expects language_TERRITORY. Only the territories the landing actually ships
// are listed; anything unknown falls back to the bare language code instead of a guess.
const LOCALES = {
  en: "en_US", ru: "ru_RU", uk: "uk_UA", be: "be_BY", kk: "kk_KZ", ka: "ka_GE",
  hy: "hy_AM", az: "az_AZ", uz: "uz_UZ", ky: "ky_KG", tg: "tg_TJ", pl: "pl_PL",
  ro: "ro_RO", fr: "fr_FR", de: "de_DE", es: "es_ES", el: "el_GR",
};
const localeOf = (language) => LOCALES[language] || language;

// Rewrite a meta tag in place when the source document has one; never invent tags the
// page did not already declare.
const replaceMeta = (page, attribute, name, value) => {
  const pattern = new RegExp(`<meta ${attribute}="${name}" content="[^"]*">`);
  return pattern.test(page)
    ? page.replace(pattern, `<meta ${attribute}="${name}" content="${escapeAttribute(value)}">`)
    : page;
};

// hreflang has to be reciprocal — every page lists every language, itself included, plus
// x-default for readers whose language we do not publish. Google drops the whole
// annotation when the links do not point back at each other.
const alternateLinks = [
  ...languages.map(
    (language) => `<link rel="alternate" hreflang="${language}" href="${pageUrl(language)}">`
  ),
  `<link rel="alternate" hreflang="x-default" href="${pageUrl(DEFAULT_LANGUAGE)}">`,
].join("\n");

// The page declares its own locale and lists every other language as an alternate. Entries
// from the source document are dropped first, so the list always matches the dictionary.
function setLocales(page, language) {
  page = page.replace(/\s*<meta property="og:locale:alternate" content="[^"]*">/g, "");
  const alternates = languages
    .filter((other) => other !== language)
    .map((other) => `\n<meta property="og:locale:alternate" content="${localeOf(other)}">`)
    .join("");
  const block = `<meta property="og:locale" content="${localeOf(language)}">${alternates}`;
  const existing = /<meta property="og:locale" content="[^"]*">/;
  return existing.test(page)
    ? page.replace(existing, block)
    : page.replace(/<link rel="canonical" href="[^"]*">/, (match) => `${match}\n${block}`);
}

function translate(html, translations) {
  // Text nodes: <tag … data-i18n="key">text</tag>. Every such element holds plain text,
  // which the generator verifies below, so matching up to the closing tag is safe.
  let page = html.replace(
    /(<([a-zA-Z0-9]+)[^>]*\bdata-i18n="([^"]+)"[^>]*>)([^<]*)(<\/\2>)/g,
    (match, opening, _tag, key, _text, closing) => {
      const value = translations[key];
      return value == null ? match : opening + escapeText(value) + closing;
    }
  );

  // Placeholders: the input carries both placeholder and aria-label, and the runtime
  // script keeps them in sync, so the generated markup must do the same.
  page = page.replace(/<input\b([^>]*\bdata-i18n-ph="([^"]+)"[^>]*)>/g, (match, attributes, key) => {
    const value = translations[key];
    if (value == null) return match;
    const translated = attributes
      .replace(/\splaceholder="[^"]*"/, ` placeholder="${escapeAttribute(value)}"`)
      .replace(/\saria-label="[^"]*"/, ` aria-label="${escapeAttribute(value)}"`);
    return `<input${translated}>`;
  });

  return page;
}

function buildPage(language) {
  const translations = dictionary[language];
  const url = pageUrl(language);
  const title = `${BRAND} — ${translations.h1a} ${translations.h1b}`;
  const description = translations.sub;

  let page = translate(sourceHtml, translations);

  // <base> must precede the first relative URL in the document, and the language marker
  // must be set before the page script reads it.
  page = page.replace(
    '<meta charset="utf-8">',
    '<meta charset="utf-8">\n' +
      '<base href="/">\n' +
      `<script>window.__PAGE_LANG__=${JSON.stringify(language)};</script>`
  );

  page = page.replace(/<title>[\s\S]*?<\/title>/, `<title>${escapeText(title)}</title>`);
  page = page.replace(
    /<meta name="description" content="[^"]*">/,
    `<meta name="description" content="${escapeAttribute(description)}">`
  );
  page = page.replace(
    /<link rel="canonical" href="[^"]*">/,
    `<link rel="canonical" href="${url}">\n${alternateLinks}`
  );
  page = replaceMeta(page, "property", "og:url", url);
  page = replaceMeta(page, "property", "og:title", title);
  page = replaceMeta(page, "property", "og:description", description);
  page = replaceMeta(page, "name", "twitter:title", title);
  page = replaceMeta(page, "name", "twitter:description", description);
  page = setLocales(page, language);

  // FAQ structured data, built from the same keys as the visible block above it — the
  // markup and the text can never disagree, and every language ships its own.
  const questions = [1, 2, 3, 4, 5, 6]
    .map((number) => [translations[`faqQ${number}`], translations[`faqA${number}`]])
    .filter(([question, answer]) => question && answer)
    .map(([question, answer]) => ({
      "@type": "Question",
      name: question,
      acceptedAnswer: { "@type": "Answer", text: answer },
    }));

  if (questions.length) {
    const faq = JSON.stringify({
      "@context": "https://schema.org",
      "@type": "FAQPage",
      inLanguage: language,
      mainEntity: questions,
    });
    // The source document has no explicit </head> to append to — head and body are left
    // implicit — so the block goes in next to the other head metadata.
    page = page.replace(
      '<link rel="icon"',
      `<script type="application/ld+json">${faq}</script>\n<link rel="icon"`
    );
  }

  // The source document leaves <html> implicit. Stating it explicitly gives crawlers the
  // language of the page without waiting for the script to set it.
  return `<!doctype html>\n<html lang="${language}">\n${page}\n</html>\n`;
}

function buildSitemap() {
  const entries = languages
    .map((language) => {
      const alternates = [
        ...languages.map(
          (other) =>
            `    <xhtml:link rel="alternate" hreflang="${other}" href="${pageUrl(other)}"/>`
        ),
        `    <xhtml:link rel="alternate" hreflang="x-default" href="${pageUrl(DEFAULT_LANGUAGE)}"/>`,
      ].join("\n");
      return `  <url>\n    <loc>${pageUrl(language)}</loc>\n${alternates}\n    <changefreq>weekly</changefreq>\n    <priority>${
        language === DEFAULT_LANGUAGE ? "1.0" : "0.8"
      }</priority>\n  </url>`;
    })
    .join("\n");

  // Listed without the ?doc= parameter: both documents live on one page, whose canonical
  // points at the bare address, and a sitemap should only ever offer canonical URLs.
  const legalPages = [
    [`${origin}/rules.html`, "monthly", "0.4"],
    [`${origin}/legal.html`, "yearly", "0.3"],
  ]
    .map(
      ([location, frequency, priority]) =>
        `  <url>\n    <loc>${location.replace(/&/g, "&amp;")}</loc>\n    <changefreq>${frequency}</changefreq>\n    <priority>${priority}</priority>\n  </url>`
    )
    .join("\n");

  return (
    '<?xml version="1.0" encoding="UTF-8"?>\n' +
    '<!-- Generated by landing/build-pages.mjs — do not edit by hand. -->\n' +
    '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"\n' +
    '        xmlns:xhtml="http://www.w3.org/1999/xhtml">\n' +
    `${entries}\n${legalPages}\n</urlset>\n`
  );
}

// --- guard: the text substitution assumes plain-text content in every marked element ---
const nested = sourceHtml.match(/<[a-zA-Z0-9]+[^>]*\bdata-i18n="[^"]+"[^>]*>[^<]*<[^/]/g);
if (nested) {
  throw new Error(
    `data-i18n elements must hold plain text, found nested markup in: ${nested.slice(0, 3).join(" | ")}`
  );
}

let written = 0;
for (const language of languages) {
  const page = buildPage(language);
  if (language === DEFAULT_LANGUAGE) {
    writeFileSync(sourceFile, page);
  } else {
    const directory = join(targetDirectory, language);
    mkdirSync(directory, { recursive: true });
    writeFileSync(join(directory, "index.html"), page);
  }
  written++;
}

writeFileSync(join(targetDirectory, "sitemap.xml"), buildSitemap());

console.log(
  `build-pages · ${written} pages (${DEFAULT_LANGUAGE} at the root, ${written - 1} folders) · sitemap with ${
    languages.length + 2
  } urls · origin ${origin}`
);

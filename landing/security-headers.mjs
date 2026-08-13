// Build the security headers for a staged landing, from the bytes that are about
// to be uploaded.
//
//   node landing/security-headers.mjs <staged-dir>
//
// Prints one JSON object: { headers: [{name, value}], counted: {...} }.
//
// Why it runs here and not from a hand-kept list: the policy names sha256 hashes
// of every inline script, every inline style block and every style attribute on
// the pages. A hash kept by hand goes stale on the first markup edit, and a stale
// hash is a blank page in production and nowhere else — the header lives at the
// CDN edge, so a local server never sends it and never catches the mistake.
// Computed from the staging directory, it cannot go stale: the bytes hashed are
// the bytes served.
//
// The pages are counted after the per-language pre-render, so every generated
// copy is included rather than only the four sources.

import { createHash } from "node:crypto";
import { readdirSync, readFileSync, statSync } from "node:fs";
import { join } from "node:path";

const stage = process.argv[2];
if (!stage) {
  console.error("usage: security-headers.mjs <staged-dir>");
  process.exit(2);
}

const sha256 = (value) => `'sha256-${createHash("sha256").update(value, "utf8").digest("base64")}'`;

function htmlFiles(dir) {
  const found = [];
  for (const entry of readdirSync(dir)) {
    const path = join(dir, entry);
    if (statSync(path).isDirectory()) found.push(...htmlFiles(path));
    else if (entry.endsWith(".html")) found.push(path);
  }
  return found;
}

const scripts = new Set();
const styles = new Set();
const styleAttributes = new Set();

// Deliberately narrow patterns rather than a parser: a dependency for four tags
// is a dependency to keep, and anything these miss shows up as a console
// violation on the very first check after a deploy.
// `type="application/ld+json"` is data, not code: browsers never execute it and
// CSP never blocks it, so hashing it would add noise that can never match.
const INLINE_SCRIPT = /<script(?![^>]*\bsrc=)([^>]*)>([\s\S]*?)<\/script>/g;
const EXECUTABLE = (attributes) => {
  const type = /\btype\s*=\s*"([^"]*)"/.exec(attributes)?.[1]?.toLowerCase();
  return !type || type === "text/javascript" || type === "module";
};
const INLINE_STYLE = /<style[^>]*>([\s\S]*?)<\/style>/g;
const STYLE_ATTRIBUTE = /\sstyle="([^"]*)"/g;

const pages = htmlFiles(stage);
for (const page of pages) {
  const html = readFileSync(page, "utf8");
  for (const [, attributes, body] of html.matchAll(INLINE_SCRIPT)) {
    if (EXECUTABLE(attributes)) scripts.add(sha256(body));
  }
  for (const [, body] of html.matchAll(INLINE_STYLE)) styles.add(sha256(body));
  for (const [, value] of html.matchAll(STYLE_ATTRIBUTE)) styleAttributes.add(sha256(value));
}

// The relay this landing talks to differs per environment, so it comes from the
// deploy rather than from a list here that would be wrong for two of the three.
//
// A CSP source carrying a path matches that exact path, so `https://relay/v1`
// would permit one request and block every other — while the page, which
// concatenates onto the same string, works fine. The two disagree silently and
// only in production, so a malformed value stops the deploy instead of shipping
// a policy nobody will read. An empty value stays legal: a stand without a
// relay is a stand, not a mistake.
const configured = process.env.RELAY_API_URL || "";
let relay = "";
if (configured) {
  try {
    const parsed = new URL(configured);
    if (parsed.origin !== configured.replace(/\/$/, "")) {
      throw new Error(`expected a bare origin, got ${configured}`);
    }
    relay = parsed.origin;
  } catch (error) {
    console.error(`RELAY_API_URL is not a usable CSP source: ${error.message}`);
    process.exit(1);
  }
}

// Where the browser says the policy blocked something. The hashes are computed
// from the markup at deploy time, so the policy drifts by construction, and the
// only thing that stood between a drifted policy and a dead page was somebody
// remembering to open the console. Both spellings: report-to is the current one
// and the only one Chrome honours, report-uri is deprecated and the only one
// Firefox and Safari honour. No relay means no endpoint, and the directives are
// left out rather than pointed at nothing.
const reportTo = relay ? `${relay}/csp-report` : "";
// Analytics is production-only and consented; without an id, nothing of Google's
// is allowed at all rather than allowed and unused.
const analytics = process.env.ANALYTICS_ID
  ? {
    script: ["https://www.googletagmanager.com"],
    connect: [
      "https://www.google-analytics.com",
      "https://region1.google-analytics.com",
      "https://analytics.google.com",
    ],
    img: ["https://www.google-analytics.com"],
  }
  : { script: [], connect: [], img: [] };

const csp = [
  "default-src 'self'",
  // 'self' rather than 'none': the per-language pages are served from /ru/, /de/
  // and so on, and a single <base href="/"> is what makes their relative links —
  // and the url() inside the inline stylesheet — resolve from the root. 'none'
  // blocked our own tag while an injected <base href="https://elsewhere/"> is
  // what the directive is actually for, and 'self' still refuses that.
  "base-uri 'self'",
  "object-src 'none'",
  // The landing is never framed by anyone, and saying so twice — here and in
  // X-Frame-Options — costs nothing and covers older browsers.
  "frame-ancestors 'none'",
  "form-action 'self'",
  `img-src 'self' data: ${analytics.img.join(" ")}`.trim(),
  "font-src 'self'",
  // 'unsafe-hashes' is what lets a hash apply to a style attribute rather than
  // only to a <style> block. It does not loosen script-src, and the hashes are
  // recomputed here on every deploy, so markup can be edited freely.
  `style-src 'self' 'unsafe-hashes' ${[...styles, ...styleAttributes].join(" ")}`,
  `script-src 'self' ${[...scripts, ...analytics.script].join(" ")}`.replace(/\s+/g, " "),
  `connect-src 'self' ${[relay, ...analytics.connect].filter(Boolean).join(" ")}`.trim(),
  ...(reportTo ? [`report-uri ${reportTo}`, "report-to csp"] : []),
  "upgrade-insecure-requests",
].join("; ");

const headers = [
  { name: "Content-Security-Policy", value: csp },
  // `report-to csp` above names a group; this header is what defines it.
  ...(reportTo ? [{ name: "Reporting-Endpoints", value: `csp="${reportTo}"` }] : []),
  // A year, no preload: preload is a list somebody else keeps and leaving it
  // takes months, which is the wrong shape for a service still finding its feet.
  { name: "Strict-Transport-Security", value: "max-age=31536000; includeSubDomains" },
  { name: "X-Content-Type-Options", value: "nosniff" },
  { name: "Referrer-Policy", value: "strict-origin-when-cross-origin" },
  { name: "X-Frame-Options", value: "DENY" },
  // The application will ask for geolocation one day; the landing never does,
  // and the two are different documents on different hosts.
  { name: "Permissions-Policy", value: "camera=(), microphone=(), geolocation=(), payment=()" },
];

console.log(JSON.stringify({
  headers,
  counted: {
    pages: pages.length,
    inline_scripts: scripts.size,
    inline_styles: styles.size,
    style_attributes: styleAttributes.size,
    relay: relay || "(not set)",
    analytics: Boolean(process.env.ANALYTICS_ID),
  },
}, null, 2));

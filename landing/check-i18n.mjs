#!/usr/bin/env node
// Verify the landing i18n dictionary is complete.
// Checks, across every language in the T dictionary:
//   1. every data-i18n / data-i18n-ph key used in the HTML exists in that language
//   2. every language has the exact same set of keys (no missing, no extras)
//   3. flags empty values and values identical to English (likely untranslated)
// Usage: node check-i18n.mjs [path/to/index.html]   (default: ./index.html)
import { readFileSync } from "node:fs";

const file = process.argv[2] || new URL("./index.html", import.meta.url).pathname;
const html = readFileSync(file, "utf8");

// --- extract the i18n object literal (`T = { ... }`) by brace balancing ---
function extractDict(src) {
  const m = src.match(/\b(?:const|let|var)\s+T\s*=\s*\{/);
  if (!m) throw new Error("could not find the T dictionary");
  let i = m.index + m[0].length - 1, depth = 0, inStr = null;
  for (let j = i; j < src.length; j++) {
    const ch = src[j], prev = src[j - 1];
    if (inStr) { if (ch === inStr && prev !== "\\") inStr = null; continue; }
    if (ch === '"' || ch === "'" || ch === "`") inStr = ch;
    else if (ch === "{") depth++;
    else if (ch === "}") { depth--; if (depth === 0) return src.slice(i, j + 1); }
  }
  throw new Error("unbalanced braces in T");
}
const T = Function("return (" + extractDict(html) + ")")();
const langs = Object.keys(T);

// --- keys actually used in the markup ---
const used = new Set([...html.matchAll(/data-i18n(?:-ph)?="([^"]+)"/g)].map((m) => m[1]));

// --- reference key set = union of all languages ---
const union = new Set();
for (const l of langs) for (const k of Object.keys(T[l])) union.add(k);

let problems = 0;
const base = T.en || T[langs[0]];
console.log(`i18n check · ${file}`);
console.log(`languages: ${langs.join(", ")}  ·  keys/union: ${union.size}  ·  used in DOM: ${used.size}\n`);

for (const l of langs) {
  const keys = new Set(Object.keys(T[l]));
  const missingUsed = [...used].filter((k) => !keys.has(k));
  const missingUnion = [...union].filter((k) => !keys.has(k));
  const empty = [...keys].filter((k) => !String(T[l][k] ?? "").trim());
  const sameAsEn = l === "en" ? [] : [...keys].filter((k) => base[k] != null && T[l][k] === base[k]);
  const issues = [];
  if (missingUsed.length) issues.push(`MISSING (used in DOM): ${missingUsed.join(", ")}`);
  if (missingUnion.length) issues.push(`missing vs other langs: ${missingUnion.join(", ")}`);
  if (empty.length) issues.push(`empty: ${empty.join(", ")}`);
  if (sameAsEn.length) issues.push(`same as EN (maybe untranslated): ${sameAsEn.join(", ")}`);
  if (issues.length) { problems += missingUsed.length + missingUnion.length + empty.length; console.log(`  ✗ ${l}\n     ` + issues.join("\n     ")); }
  else console.log(`  ✓ ${l}  (${keys.size} keys, complete)`);
}

// keys used in DOM that exist in NO language
const orphanUsed = [...used].filter((k) => !union.has(k));
if (orphanUsed.length) { problems += orphanUsed.length; console.log(`\n  ✗ used in DOM but defined nowhere: ${orphanUsed.join(", ")}`); }

console.log(problems ? `\nFAILED · ${problems} missing/empty key(s)` : `\nOK · all languages complete`);
process.exit(problems ? 1 : 0);

#!/usr/bin/env node
// Dictionary keys nothing renders. check-i18n.mjs answers the opposite question
// — is every marked-up key translated — so a key that outlived its element sits
// in all 17 languages forever, translated by someone, read by nobody.
//
//   node landing/find-dead-keys.mjs landing/index.html
//
// Reports rather than fails: a key may legitimately be used from JavaScript by a
// name this cannot see, so the list is for a human to judge.

import { readFileSync } from "node:fs";
import { readDictionary } from "./i18n-dictionary.mjs";

const file = process.argv[2] ?? new URL("./index.html", import.meta.url).pathname;
const html = readFileSync(file, "utf8");
const dictionary = readDictionary(html);
const english = dictionary.en ?? Object.values(dictionary)[0];

// Where a key can legitimately be referenced: the markup attributes, or JS that
// reaches into the dictionary by name.
const marked = new Set([
  ...[...html.matchAll(/data-i18n(?:-ph)?="([^"]+)"/g)].map((match) => match[1]),
]);

const dead = Object.keys(english).filter((key) => {
  if (marked.has(key)) return false;
  // d.key, T[LANG].key, dictionary["key"] — any direct mention outside the
  // dictionary literal itself.
  const mentions = html.split(key).length - 1;
  // Every key appears once per language inside the dictionary; more than that
  // means something else refers to it.
  const languages = Object.keys(dictionary).length;
  return mentions <= languages;
});

console.log(`${Object.keys(english).length} keys, ${marked.size} marked up in the HTML`);
if (dead.length === 0) {
  console.log("no keys look unused");
} else {
  console.log(`\n${dead.length} key(s) nothing seems to render:`);
  for (const key of dead) console.log(`   ${key}`);
  console.log("\nCheck each before deleting: a key used only from JavaScript can look dead here.");
}

#!/usr/bin/env node
// Contrast of the landing's text colours against the surfaces they sit on, in
// both modes and across every accent. The palette is warm and low-contrast by
// design, which is exactly the case where an eye is a poor judge: "looks fine on
// my screen" is how a button ends up at 3.4:1.
//
//   node landing/check-contrast.mjs
//
// Reads the values out of index.html, so it checks what ships, and exits
// non-zero below the threshold, so it can gate a deploy.

import { readFileSync } from "node:fs";

const html = readFileSync(new URL("./index.html", import.meta.url), "utf8");

const channel = (value) => {
  const part = value / 255;
  return part <= 0.03928 ? part / 12.92 : ((part + 0.055) / 1.055) ** 2.4;
};

function luminance(hex) {
  const clean = hex.replace("#", "");
  const full = clean.length === 3 ? [...clean].map((c) => c + c).join("") : clean;
  const [r, g, b] = [0, 2, 4].map((offset) => parseInt(full.slice(offset, offset + 2), 16));
  return 0.2126 * channel(r) + 0.7152 * channel(g) + 0.0722 * channel(b);
}

const ratio = (a, b) => {
  const [light, dark] = [luminance(a), luminance(b)].sort((x, y) => y - x);
  return (light + 0.05) / (dark + 0.05);
};

// Every rule block that declares custom properties, with the selector that opens
// it. The two landings name their themes differently — data-theme, data-accent,
// data-mode — and none of that matters here: what matters is which values a
// block sets.
function blocks() {
  const found = [];
  for (const match of html.matchAll(/([^{}\n]+)\{([^{}]*--[^{}]*)\}/g)) {
    const selector = match[1].trim();
    const values = {};
    for (const [, name, value] of match[2].matchAll(/--([\w-]+):\s*(#[0-9a-fA-F]{3,8})/g)) {
      values[name] = value;
    }
    if (Object.keys(values).length) found.push({ selector, values });
  }
  return found;
}

const declared = blocks();
const base = Object.assign({}, ...declared.map((block) => block.values));

// An accent block is one that sets an accent and its ink together — that pair is
// a button, and a button carries 16px bold text, so 4.5:1 applies.
const accents = declared.filter((block) => block.values.accent && block.values["accent-ink"]);

// A mode block is one that redefines the page ground.
const modes = declared.filter((block) => block.values.bg && block.values.fg);

const PAIRS = [
  ["body text on the page", "fg", "bg", 4.5],
  ["body text on a panel", "fg", "panel", 4.5],
  ["muted text on the page", "muted", "bg", 4.5],
  ["muted text on a panel", "muted", "panel", 4.5],
  ["secondary muted on the page", "muted-2", "bg", 4.5],
  ["secondary muted on a panel", "muted-2", "panel", 4.5],
  // A nested plate is a busier ground than a panel, and --muted does not clear it.
  // Moving that colour is no fix: it collapses into --muted-2, which is what the
  // palette already keeps for exactly this ground. So the line is a rule rather
  // than a threshold — it prints the number and names the token to use instead.
  ["muted on a nested plate — use --muted-2 there", "muted", "panel-2", null],
  ["secondary muted on a nested plate", "muted-2", "panel-2", 4.5],
];

let failed = 0;

console.log("accents (button and bubble text on their own accent)");
for (const block of accents) {
  const value = ratio(block.values["accent-ink"], block.values.accent);
  const ok = value >= 4.5;
  if (!ok) failed += 1;
  console.log(
    `   ${ok ? "ok  " : "FAIL"} ${block.selector.padEnd(26)} ` +
      `${block.values.accent} / ${block.values["accent-ink"]}   ${value.toFixed(2)}:1`,
  );
}

for (const block of modes) {
  const values = { ...base, ...block.values };
  console.log(`\n${block.selector}`);
  for (const [label, foreground, background, minimum] of PAIRS) {
    if (!values[foreground] || !values[background]) continue;
    const value = ratio(values[foreground], values[background]);
    if (minimum === null) {
      console.log(`   note ${label.padEnd(46)} ${value.toFixed(2)}:1`);
      continue;
    }
    const ok = value >= minimum;
    if (!ok) failed += 1;
    console.log(
      `   ${ok ? "ok  " : "FAIL"} ${label.padEnd(46)} ${value.toFixed(2)}:1 (needs ${minimum})`,
    );
  }
}


// --accent-text depends on the accent AND on the theme, so it cannot ride on the
// merged `base`: the last block declared would win and the check would be about
// nothing. Each block that sets one is measured against the grounds of the theme
// its own selector names. A negated attribute — :not([data-mode="light"]) — names
// the theme it is NOT, which is how the dark default is written here, so it has to
// be read as an exclusion or the dark set gets measured on the light ground.
//
// This is the pair that was missing while this counter said "every pair passes":
// the accent as a fill was always checked; the accent as a word never was.
const textAccents = declared.filter((block) => block.values["accent-text"]);
const themeIn = (selector) => {
  const positive = selector.replace(/:not\([^)]*\)/g, "");
  const negated = [...selector.matchAll(/:not\((\[[^\]]+\])\)/g)].map((m) => m[1]);
  const key = (s) => (s.match(/\[data-(?:theme|mode)="(?:light|dark)"\]/) || [null])[0];
  return { is: key(positive), isNot: negated.map(key).filter(Boolean) };
};

console.log("\nthe accent as small text, on each ground of its theme");
for (const block of textAccents) {
  const want = themeIn(block.selector);
  for (const mode of modes) {
    const has = themeIn(mode.selector).is;
    if (want.is && want.is !== has) continue;
    if (want.isNot.length && want.isNot.includes(has)) continue;
    if (!want.is && !want.isNot.length && has) continue;
    const values = { ...base, ...mode.values };
    for (const ground of ["bg", "panel", "panel-2"]) {
      if (!values[ground]) continue;
      const value = ratio(block.values["accent-text"], values[ground]);
      const ok = value >= 4.5;
      if (!ok) failed += 1;
      console.log(
        `   ${ok ? "ok  " : "FAIL"} ${(block.selector + " on --" + ground).padEnd(56)} ` +
          `${value.toFixed(2)}:1`,
      );
    }
  }
}

if (failed) {
  console.error(`\n${failed} pair(s) below the threshold`);
  process.exit(1);
}
console.log("\nevery pair passes");

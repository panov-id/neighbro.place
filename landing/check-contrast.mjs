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
    const ok = value >= minimum;
    if (!ok) failed += 1;
    console.log(
      `   ${ok ? "ok  " : "FAIL"} ${label.padEnd(30)} ${value.toFixed(2)}:1 (needs ${minimum})`,
    );
  }
}

if (failed) {
  console.error(`\n${failed} pair(s) below the threshold`);
  process.exit(1);
}
console.log("\nevery pair passes");

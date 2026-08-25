#!/usr/bin/env node
// The published documents must not contradict each other.
//
// They did. The community guidelines said a prohibited message "is never
// published or sent, in the feed or in chat" and that every message is
// pre-screened; the privacy policy, served from the same page and the same
// directory, said chats are not checked at all — encrypted end to end, and we
// cannot open them. A reader could hold both pages open at once. Only one of
// them matched the product.
//
// That is not a typo class of mistake: two documents drifted apart because
// nothing ever read them together. This does.
//
// What it cannot do is check a translation's meaning. So it checks the English —
// the version the files themselves declare authoritative — for what is said, and
// every translation for the shape that carries it, which is what a translator
// dropping a paragraph would break.

import { readFileSync, readdirSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const LEGAL = join(dirname(fileURLToPath(import.meta.url)), "legal");
const problems = [];

const read = (name) => readFileSync(join(LEGAL, name), "utf8");
const guidelines = readdirSync(LEGAL).filter((name) => name.startsWith("community-guidelines_"));

// --- what the English says ---------------------------------------------------

const english = read("community-guidelines_EN.md");
const privacy = read("privacy_EN.md");

if (!/Chats are not checked/i.test(privacy)) {
  problems.push(
    "the privacy policy no longer states that chats are not checked — if that changed, " +
      "the guidelines and the product have to change with it",
  );
}
if (!/chat is not screened/i.test(english)) {
  problems.push(
    "the guidelines no longer say a chat is not screened, while the privacy policy still " +
      "says chats are not checked — the two pages disagree again",
  );
}

// The exact promise that was wrong, in the words it was written in. Kept as a
// literal so that reintroducing it fails here rather than in front of a reader.
for (const phrase of ["in the feed or in chat", "pre-screen every message"]) {
  if (english.includes(phrase)) {
    problems.push(`the guidelines promise "${phrase}" again — the chat gets no such check`);
  }
}

// --- the shape every translation has to carry --------------------------------

for (const name of guidelines) {
  const lines = read(name).split("\n");
  const headings = lines.reduce((found, line, index) => {
    if (line.startsWith("## ")) found.push(index);
    return found;
  }, []);
  if (headings.length < 2) {
    problems.push(`${name}: no sections — the file is not the document it should be`);
    continue;
  }
  const principle = lines
    .slice(headings[0] + 1, headings[1])
    .filter((line) => line.trim());
  // Two paragraphs: what is screened, and that a chat is not. One means the
  // second was lost — in a translation, that is the contradiction returning in
  // whichever language it was lost in.
  if (principle.length < 2) {
    problems.push(
      `${name}: the general principle has ${principle.length} paragraph(s), expected 2 — ` +
        "the one saying a chat is not screened is missing",
    );
  }
}

// --- a translation that says it twice ----------------------------------------
//
// The Armenian file carried both editions at once: the retired promise that a
// chat is screened, and the sentence that replaced it. Structure passed — two
// paragraphs were there — and the literal ban above only reads English, so CI
// was green while a published page contradicted itself in front of an Armenian
// reader (found 2026-08-23).
//
// Sentences are the cheapest cross-language shape there is: a leftover edition
// shows up as extra terminators against the English original, and this needs no
// knowledge of the language it fires on.
const terminators = (text) => (text.match(/[.!?։。][\s]|[.!?։。]$/gu) || []).length;

for (const name of guidelines) {
  if (name.endsWith("_EN.md")) continue;
  const other = read(name);
  const englishSentences = terminators(english);
  const otherSentences = terminators(other);
  const drift = Math.abs(otherSentences - englishSentences) / englishSentences;
  if (drift > 0.25) {
    problems.push(
      `${name}: ${otherSentences} sentences against ${englishSentences} in English — ` +
        "a translation that drifted this far is usually one that kept a retired edition " +
        "alongside its replacement",
    );
  }
}

// --- and the bar has to know these changed ------------------------------------

const deploy = readFileSync(join(LEGAL, "../../deploy/deploy-landing.sh"), "utf8");
if (!deploy.includes("community-guidelines_EN.md")) {
  problems.push(
    "the legal revision is computed without the guidelines, so editing them changes the " +
      "documents while the \"documents changed\" bar stays silent",
  );
}
if (!/Last updated:/.test(english.split("## ")[0])) {
  problems.push("the guidelines carry no date, so they cannot move the revision either");
}

if (problems.length) {
  console.error("legal documents disagree:");
  for (const problem of problems) console.error(`  - ${problem}`);
  process.exit(1);
}
console.log(`legal documents agree (${guidelines.length} languages checked for shape)`);

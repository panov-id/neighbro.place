# Screen 15 — Legal Documents

## Purpose

Access to the Terms of Service, Privacy Policy, and Community Guidelines.

## Screen elements

- Links to three documents: Terms of Service, Privacy Policy, Community Guidelines.
- **A revision date under each link** (added 2026-08-29), and, if the text changed after the person accepted it, a note beside it: "changed since you accepted".
- **A "contest a moderator's decision" link** (added 2026-08-29).
- **Who the operator is and where to write** (added 2026-08-29): Evgenii Panov, brands PSYTICAN & PEJEDED, Limassol, Cyprus; support@neighbro.place.

## Logic

- The documents are short and simple, not exhaustive legal boilerplate.
- Content mirrors the rules already described in the README (Moderation, Privacy sections), rather than introducing new ones.
- The texts live in `landing/legal/`, where the documents page serves them from: `terms_EN.md`, `privacy_EN.md`, `community-guidelines_*.md`. The root `legal/` holds pointers only.
- **The documents come in different numbers of languages, and that is not an oversight (verified 2026-08-27).** Terms and privacy are English only, in a single version. The community rules are translated: **17 languages** for sosed, **10** for neighbro. The reason is who reads them: the rules are read before anybody writes anything, and in their own language; terms and privacy are read rarely and on purpose.
- **Every translation of the rules carries the governing-version clause** — in the document's language with the English line beside it: "The English version of these rules is the one that applies; translations are provided for convenience." Verified across all 27 files.
- **A document a person has accepted must match what the product does.** On 2026-08-27 the opposite turned up: the rules stated "reports and blocks reduce the author's posting quota" — the decision of 2026-08-26 had reversed that in the mechanics and on screen 5, while the published text stayed as it was. A divergence here costs more than one in the spec: the spec is read by us, the rules are accepted by a person with a checkbox.
- **The 2026-08-27 fix covered half of it, which surfaced on 2026-08-28.** It searched for the retired sentence by a dictionary of translations, while German says "Veröffentlichungskontingent", Georgian writes quota in its own script, and Belarusian and Ukrainian use a different verb. **Seven languages out of seventeen** kept the claim — eleven places in two documents went on lying for two more days. The sentences are now extracted by parsing the files rather than guessed: removed everywhere, and the correct one stands in **23 places** across 27 documents (all but Russian and English, where it already was).
- **The correct sentence was machine-translated — decided 2026-08-27, done 2026-08-28.** A deliberate departure from "do not translate legal text into languages you do not know": nine languages had no such paragraph at all, and the document is accepted with a checkbox. A poor wording under the clause about the English version governing is worse than a good one and better than a hole; a native speaker will replace it when one appears.
- **A check watches this rather than attention** (`xor.ad/scripts/check-rules-quota-sentence.sh`, created 2026-08-28). It is two-sided: the retired sentence must be in **no** file and the correct one in **every** file — the wording registry can only do the first. Verified by injection in both directions.

- **A revision is signed by a date and a hash of the text — decided 2026-08-29.** Each document carries a date in its header, and the storefront build computes the file's `sha256` and writes a manifest beside the texts. The identity records the pair (date, hash) for each of the three documents; the person is shown the **date**, while the hash is evidence rather than decoration.
  **Why not a version number kept by hand.** A number is raised by a person. Forget to raise it and the consent signed a different text, with no way to tell: two different documents with the same header line are indistinguishable. A hash cannot be forgotten — it is computed from the very file the person read.
  **The price is named:** the build needs a step that computes the manifest, and it is not written yet; without it the date under the link exists but there is nothing to compare the accepted one against.
- **The terms and the privacy policy stay in one language, but stop being silent about it — decided 2026-08-29.** A line in the person's own language stands above the English text: "this document exists in English only". Once screen 2 gained a language switcher, the silence became visible: the interface switched, the document did not, and a person learned of it only after opening the text.
  **Why not translate those too.** The terms and the policy are three times the size of the guidelines, and every edit to the terms means 10 files again plus a wider check. The clause about the English version governing already makes any translation advisory, so we pay for translation where the text is read before acting, not where people arrive on business.
- **The screen now offers a way to contest a decision — added 2026-08-29.** The right is written into the terms (the reporting section) and into the Article 17 statement of reasons, but there was no route from this screen: a person learned of the right from a document and could not use it. The link goes where the text says — to a human at support@neighbro.place and onward to the Digital Services Coordinator. **We run no formal internal appeals body under Article 20, and the screen does not pretend otherwise** (`xor.ad/docs/dsa/SPEC_EN.md`).

## Open questions

- ~~Where this screen is opened from~~ — **from settings** (screen 10) and **as a checkbox at registration** (screen 2), settled 2026-08-27.
- ~~How a document's edition is shown~~ — **a date plus a hash of the text, decided 2026-08-29** (above).
- **The build step that computes the hash manifest does not exist yet** (opened 2026-08-29). Until it does, there is nothing to draw "changed since you accepted" from.
- ~~The corrected description of reporting exists in two languages only~~ — **written in all of them on 2026-08-28** by machine translation under the clause (above). A native speaker is still wanted, but now to **improve** the text rather than to fill a hole.
- ~~Whether explicit agreement is required at registration~~ — **yes, a separate checkbox** on screen 2 (settled 2026-08-26). It is a contract, and the accepted revision is recorded with the identity; a line saying "by pressing, you accept" is weaker as evidence.

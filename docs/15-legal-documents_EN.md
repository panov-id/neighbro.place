# Screen 15 — Legal Documents

## Purpose

Access to the Terms of Service, Privacy Policy, and Community Guidelines.

## Screen elements

- Links to three documents: Terms of Service, Privacy Policy, Community Guidelines.

## Logic

- The documents are short and simple, not exhaustive legal boilerplate.
- Content mirrors the rules already described in the README (Moderation, Privacy sections), rather than introducing new ones.
- The texts live in `landing/legal/`, where the documents page serves them from: `terms_EN.md`, `privacy_EN.md`, `community-guidelines_*.md`. The root `legal/` holds pointers only.
- **The documents come in different numbers of languages, and that is not an oversight (verified 2026-08-27).** Terms and privacy are English only, in a single version. The community rules are translated: **17 languages** for sosed, **10** for neighbro. The reason is who reads them: the rules are read before anybody writes anything, and in their own language; terms and privacy are read rarely and on purpose.
- **Every translation of the rules carries the governing-version clause** — in the document's language with the English line beside it: "The English version of these rules is the one that applies; translations are provided for convenience." Verified across all 27 files.
- **A document a person has accepted must match what the product does.** On 2026-08-27 the opposite turned up: the rules stated "reports and blocks reduce the author's posting quota" — the decision of 2026-08-26 had reversed that in the mechanics and on screen 5, while the published text stayed as it was. The claim was removed from **16 files** (10 for sosed, 6 for neighbro). A divergence here costs more than one in the spec: the spec is read by us, the rules are accepted by a person with a checkbox.

## Open questions

- ~~Where this screen is opened from~~ — **from settings** (screen 10) and **as a checkbox at registration** (screen 2), settled 2026-08-27.
- How a document's edition is shown: the texts carry only "last updated", while screen 2 records the accepted edition with the identity — there is no version number to refer to.
- The corrected description of reporting is written so far **in English and Russian only**. The other nine languages need a paragraph from a native speaker: a bad legal translation is worse than a missing sentence, so there the false claim was simply removed.
- ~~Whether explicit agreement is required at registration~~ — **yes, a separate checkbox** on screen 2 (settled 2026-08-26). It is a contract, and the accepted revision is recorded with the identity; a line saying "by pressing, you accept" is weaker as evidence.

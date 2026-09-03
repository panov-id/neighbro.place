// Environment config for the neighbro.place landing, loaded before the page
// script. Local dev keeps this committed version: an empty apiUrl means
// same-origin, so a local relay stand (xor.ad/relay/local) serves /waitlist.
// Production deploy overwrites this file (see deploy/deploy-landing.sh).
//
// Feature flags — "чик и полетело":
//   apiUrl          — relay backend base (waitlist + client-error); deploy injects per env
//   reportUrl       — where an Article 16 notice is sent. Separate from apiUrl
//                     because the api host sits behind a blocking WAF, and a
//                     notice that quotes what it complains about — a <script> tag,
//                     a ../ path — is refused there (measured 03.09.2026). Empty
//                     falls back to apiUrl, which is the old behaviour.
//   publishableKey  — relay API key naming this brand ("" = the relay falls back
//                     to resolving the brand from the request host)
//   alphaUrl        — where "enter the alpha" goes after signup ("" = hidden)
//   analyticsId     — GA4 measurement ID; "" = no analytics and no consent banner
//   legalRevision   — the date the Terms/Policy last changed, taken from the
//                     documents at deploy time; "" = the "documents changed"
//                     bar stays hidden, which is right for a local copy
window.__XOR_CONFIG__ = {
  apiUrl: "",
  reportUrl: "",
  publishableKey: "",
  alphaUrl: "",
  analyticsId: "",
  legalRevision: "",
};

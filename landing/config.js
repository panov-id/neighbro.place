// Environment config for the neighbro.place landing, loaded before the page
// script. Local dev keeps this committed version: an empty apiUrl means
// same-origin, so a local relay stand (xor.ad/relay/local) serves /waitlist.
// Production deploy overwrites this file (see deploy/deploy-landing.sh).
//
// Feature flags — "чик и полетело":
//   apiUrl          — relay backend base (waitlist + client-error); deploy injects per env
//   publishableKey  — relay API key naming this brand ("" = the relay falls back
//                     to resolving the brand from the request host)
//   alphaUrl        — where "enter the alpha" goes after signup ("" = hidden)
//   analyticsId     — GA4 measurement ID; "" = no analytics and no consent banner
window.__XOR_CONFIG__ = {
  apiUrl: "",
  publishableKey: "",
  alphaUrl: "",
  analyticsId: "",
};

// Environment config for the neighbro.place landing, loaded before the page
// script. Local dev keeps this committed version: an empty apiUrl means
// same-origin, so a local relay stand (xor.ad/relay/local) serves /waitlist.
// Production deploy overwrites this file (see deploy/deploy-landing.sh).
//
// Feature flags — "чик и полетело":
//   apiUrl          — relay backend base (waitlist + client-error); deploy injects per env
//   alphaUrl        — where "enter the alpha" goes after signup ("" = hidden)
//   vapidPublicKey  — enables the push-subscribe offer ("" = hidden)
//   supabaseUrl/Key — legacy, push-only (disabled unless vapidPublicKey is set)
window.__XOR_CONFIG__ = {
  apiUrl: "",
  alphaUrl: "",
  vapidPublicKey: "",
  supabaseUrl: "",
  supabaseAnonKey: "",
};

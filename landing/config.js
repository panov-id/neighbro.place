// Environment config for the neighbro.place landing, loaded before the page
// script. Local dev keeps this committed version: an empty supabaseUrl means
// same-origin, so the xor.ad gateway proxies /rest to the local Supabase.
// Production deploy overwrites this file (see deploy/deploy-landing.sh).
//
// Feature flags — "чик и полетело":
//   alphaUrl        — where "enter the alpha" goes after signup ("" = hidden)
//   vapidPublicKey  — enables the push-subscribe offer ("" = hidden)
window.__XOR_CONFIG__ = {
  supabaseUrl: "",
  supabaseAnonKey:
    "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyAgCiAgICAicm9sZSI6ICJhbm9uIiwKICAgICJpc3MiOiAic3VwYWJhc2UtZGVtbyIsCiAgICAiaWF0IjogMTY0MTc2OTIwMCwKICAgICJleHAiOiAxNzk5NTM1NjAwCn0.dc_X5iR_VP_qT0zsiyj_I_OZ2T9FtRU2BBNWN8Bu4GE",
  alphaUrl: "",
  vapidPublicKey: "",
};

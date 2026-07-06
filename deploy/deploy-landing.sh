#!/usr/bin/env bash
# Deploy this landing to a Bunny Storage Zone and purge its Pull Zone.
# Self-contained (no shared libs) so it runs standalone in CI.
#
# Required env:
#   BUNNY_STORAGE_ZONE       Storage Zone name
#   BUNNY_STORAGE_API_KEY    Storage Zone password
#   SUPABASE_URL             Supabase project URL for this environment
#   SUPABASE_ANON_KEY        Supabase anon key for this environment
# Optional env:
#   BUNNY_PULL_ZONE_ID       numeric Pull Zone ID (for cache purge)
#   BUNNY_API_KEY            account API key (purge; falls back to storage key)
#   SOURCE_TAG               waitlist source tag (default: neighbro.place-landing)
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
SRC="$ROOT_DIR/landing"

: "${BUNNY_STORAGE_ZONE:?}"
: "${BUNNY_STORAGE_API_KEY:?}"
: "${SUPABASE_URL:?}"
: "${SUPABASE_ANON_KEY:?}"
SOURCE_TAG="${SOURCE_TAG:-neighbro.place-landing}"

BASE_URL="https://storage.bunnycdn.com/${BUNNY_STORAGE_ZONE}"
PURGE_KEY="${BUNNY_API_KEY:-$BUNNY_STORAGE_API_KEY}"

mime_type() {
  case "$1" in
    *.html) echo "text/html; charset=utf-8" ;;
    *.js)   echo "application/javascript; charset=utf-8" ;;
    *.css)  echo "text/css; charset=utf-8" ;;
    *.json) echo "application/json; charset=utf-8" ;;
    *.svg)  echo "image/svg+xml" ;;
    *.png)  echo "image/png" ;;
    *.ico)  echo "image/x-icon" ;;
    *.woff2) echo "font/woff2" ;;
    *)      echo "application/octet-stream" ;;
  esac
}

# Stage a copy and inject the environment's config.js (the committed one is
# local same-origin; this points the form at the environment's Supabase).
STAGE="$(mktemp -d)"
trap 'rm -rf "$STAGE"' EXIT
cp -R "$SRC/." "$STAGE/"
cat > "$STAGE/config.js" <<EOF
// Generated at deploy time — ${SOURCE_TAG} → ${SUPABASE_URL}
window.__XOR_CONFIG__ = {
  supabaseUrl: "${SUPABASE_URL}",
  supabaseAnonKey: "${SUPABASE_ANON_KEY}",
};
EOF
rm -f "$STAGE"/SPEC_*.md

echo "Deploying landing → Bunny zone '${BUNNY_STORAGE_ZONE}'"
( cd "$STAGE" && find . -type f -print0 | while IFS= read -r -d '' f; do
    rel="${f#./}"
    echo "  → /${rel}"
    curl -sS -X PUT \
      -H "AccessKey: ${BUNNY_STORAGE_API_KEY}" \
      -H "Content-Type: $(mime_type "$f")" \
      --data-binary "@${f}" \
      "${BASE_URL}/${rel}" >/dev/null
  done )

if [ -n "${BUNNY_PULL_ZONE_ID:-}" ]; then
  echo "Purging pull zone ${BUNNY_PULL_ZONE_ID}…"
  curl -sS -X POST -H "AccessKey: ${PURGE_KEY}" \
    "https://api.bunny.net/pullzone/${BUNNY_PULL_ZONE_ID}/purgeCache" >/dev/null
  echo "  cache purged."
fi

echo "Landing deployed."

#!/usr/bin/env bash
# Deploy this landing to a Bunny Storage Zone and purge its Pull Zone.
# Self-contained (no shared libs) so it runs standalone in CI.
#
# Required env:
#   BUNNY_STORAGE_ZONE       Storage Zone name
#   BUNNY_STORAGE_API_KEY    Storage Zone password
#   RELAY_API_URL            relay backend base for this environment (waitlist + client-error)
# Optional env:
#   RELAY_PUBLISHABLE_KEY    the relay API key naming this brand to the backend.
#                            Publishable by design — it ships inside config.js.
#                            Empty leaves the relay resolving the brand from the
#                            request host, which stops working once the relay
#                            environment sets REQUIRE_API_KEY=true
#   BUNNY_PULL_ZONE_ID       numeric Pull Zone ID (for cache purge)
#   BUNNY_API_KEY            account API key (purge; falls back to storage key)
#   SOURCE_TAG               waitlist source tag (default: neighbro.place-landing)
#   ANALYTICS_ID             GA4 measurement ID; empty (dev, uat) disables analytics
#                            and the consent banner entirely
#   LANDING_ENV              dev | uat | prod (default: dev). Only prod is crawlable;
#                            anything else gets a Disallow-all robots.txt and noindex
#   SEARCH_CONSOLE_TOKEN     Google Search Console verification token (prod only)
#   SITE_ORIGIN              absolute origin for canonical/hreflang/sitemap URLs
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
SRC="$ROOT_DIR/landing"

: "${BUNNY_STORAGE_ZONE:?}"
: "${BUNNY_STORAGE_API_KEY:?}"
: "${RELAY_API_URL:?}"
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
# local same-origin; this points the form at the environment's relay backend).
# The revision the documents themselves declare. Both carry "**Last updated: N
# Month YYYY**" on their third line; the later of the two is what a visitor is
# told about, because either changing is a change to the agreement.
#
# Derived rather than kept by hand: a fourth place for a version number drifts
# from the documents on the first edit, and the drift is silent — the bar would
# announce a revision nobody made, or stay quiet about one somebody did.
legal_revision() {
  python3 - "$SRC/legal/terms_EN.md" "$SRC/legal/privacy_EN.md" <<'PYEOF'
import datetime, re, sys

MONTHS = {m: i for i, m in enumerate(
    ["january", "february", "march", "april", "may", "june", "july",
     "august", "september", "october", "november", "december"], start=1)}

latest = None
for path in sys.argv[1:]:
    with open(path, encoding="utf-8") as handle:
        head = handle.read(2000)
    found = re.search(r"Last updated:\s*(\d{1,2})\s+([A-Za-z]+)\s+(\d{4})", head)
    if not found:
        sys.exit(f"no 'Last updated' line in {path} — cannot derive the revision")
    day, month, year = found.groups()
    if month.lower() not in MONTHS:
        sys.exit(f"unknown month '{month}' in {path}")
    date = datetime.date(int(year), MONTHS[month.lower()], int(day))
    latest = date if latest is None or date > latest else latest

print(latest.isoformat())
PYEOF
}

LEGAL_REVISION="$(legal_revision)"
echo "== legal revision: ${LEGAL_REVISION}"

# The bar is the whole of Article 14(6) here — there is no account to mail — and
# both of its failure modes are invisible on the day they appear: markup nobody
# wires, or an edition somebody keeps by hand. Gate the deploy on it.
bash "$ROOT_DIR/deploy/run-node.sh" landing/check-legal-bar.mjs landing/index.html

STAGE="$(mktemp -d)"
trap 'rm -rf "$STAGE"' EXIT
cp -R "$SRC/." "$STAGE/"
cat > "$STAGE/config.js" <<EOF
// Generated at deploy time — ${SOURCE_TAG} → ${RELAY_API_URL}
window.__XOR_CONFIG__ = {
  apiUrl: "${RELAY_API_URL}",
  publishableKey: "${RELAY_PUBLISHABLE_KEY:-}",
  alphaUrl: "${ALPHA_URL:-}",
  analyticsId: "${ANALYTICS_ID:-}",
  legalRevision: "${LEGAL_REVISION}",
};
EOF
rm -f "$STAGE"/SPEC_*.md "$STAGE"/*standalone* "$STAGE"/*.zip; rm -rf "$STAGE"/img-src

# Pre-render one page per language into the staging copy: the root becomes English and
# every other language gets its own folder, each with translated text already in the HTML
# and reciprocal hreflang. The sitemap is generated here too, replacing the placeholder.
SITE_ORIGIN="${SITE_ORIGIN:-https://neighbro.place}" RUN_NODE_MOUNT="$STAGE" \
  bash "$ROOT_DIR/deploy/run-node.sh" landing/build-pages.mjs "$STAGE"
rm -f "$STAGE"/build-pages.mjs "$STAGE"/check-i18n.mjs "$STAGE"/check-legal-bar.mjs "$STAGE"/i18n-dictionary.mjs

# Indexing is a production-only privilege. dev and uat serve the same landing from their
# own zones, so a crawlable copy there competes with production as a duplicate. An unset
# LANDING_ENV is deliberately treated as non-production: the safe default is invisible.
LANDING_ENV="${LANDING_ENV:-dev}"
if [ "$LANDING_ENV" = "prod" ]; then
  if [ -n "${SEARCH_CONSOLE_TOKEN:-}" ]; then
    for page in "$STAGE"/*.html "$STAGE"/*/index.html; do
      [ -f "$page" ] || continue
      sed -i "s#<meta charset=\"utf-8\">#<meta charset=\"utf-8\">\n<meta name=\"google-site-verification\" content=\"${SEARCH_CONSOLE_TOKEN}\">#" "$page"
    done
    echo "  Search Console verification tag injected."
  fi
else
  printf 'User-agent: *\nDisallow: /\n' > "$STAGE/robots.txt"
  rm -f "$STAGE/sitemap.xml"
  for page in "$STAGE"/*.html "$STAGE"/*/index.html; do
    [ -f "$page" ] || continue
    sed -i 's#<meta charset="utf-8">#<meta charset="utf-8">\n<meta name="robots" content="noindex, nofollow">#' "$page"
  done
  echo "  Environment '${LANDING_ENV}': crawling disabled, sitemap removed."
fi

# Bust the caches that must not outlive a deploy: the service worker, and the
# config.js reference inside every generated page. config.js is served with a
# long max-age like any .js file, so without a versioned address a returning
# visitor keeps whichever copy they already have — including one from before the
# publishable key existed.
BUILD=$(git -C "$ROOT_DIR" rev-parse --short HEAD 2>/dev/null || date +%s)
if [ -f "$STAGE/sw.js" ]; then
  sed -i "s/__BUILD__/${BUILD}/g" "$STAGE/sw.js"
fi
# After the generator ran, so the language pages carry the same build id.
find "$STAGE" -name '*.html' -exec sed -i "s/__BUILD__/${BUILD}/g" {} +

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

# IndexNow: tell Bing and Yandex what changed instead of waiting to be crawled. The key is
# public by design — it is verified by fetching https://<host>/<key>.txt, which ships with
# the landing. Production only: the other environments are not indexable at all.
if [ "$LANDING_ENV" = "prod" ] && [ -f "$STAGE/sitemap.xml" ]; then
  INDEXNOW_KEY="3d9b6e2c47f84a15b8c0d7e39a52f16b"
  INDEXNOW_HOST="$(printf '%s' "${SITE_ORIGIN:-https://neighbro.place}" | sed 's#^https\?://##; s#/.*##')"
  URL_LIST="$(grep -o '<loc>[^<]*</loc>' "$STAGE/sitemap.xml" | sed 's#</\?loc>##g' \
    | python3 -c 'import json,sys; print(json.dumps([line.strip() for line in sys.stdin if line.strip()]))')"
  echo "Pinging IndexNow for ${INDEXNOW_HOST}…"
  curl -sS -m 20 -X POST -H "Content-Type: application/json" \
    --data "{\"host\":\"${INDEXNOW_HOST}\",\"key\":\"${INDEXNOW_KEY}\",\"keyLocation\":\"https://${INDEXNOW_HOST}/${INDEXNOW_KEY}.txt\",\"urlList\":${URL_LIST}}" \
    -o /dev/null -w '  IndexNow responded %{http_code}\n' \
    "https://api.indexnow.org/indexnow" || echo "  IndexNow ping failed (not fatal)"
fi

if [ -n "${BUNNY_PULL_ZONE_ID:-}" ]; then
  echo "Purging pull zone ${BUNNY_PULL_ZONE_ID}…"
  curl -sS -X POST -H "AccessKey: ${PURGE_KEY}" \
    "https://api.bunny.net/pullzone/${BUNNY_PULL_ZONE_ID}/purgeCache" >/dev/null
  echo "  cache purged."
fi

echo "Landing deployed."

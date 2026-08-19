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
  # The rules are one of the documents the bar is about: they say what a person
  # may post and what happens if they do not, and they changed on 13.08.2026 to
  # stop promising a check the chat does not get. Leaving them out meant the
  # documents could change while the bar said nothing.
  python3 - "$SRC/legal/terms_EN.md" "$SRC/legal/privacy_EN.md" \
           "$SRC/legal/community-guidelines_EN.md" <<'PYEOF'
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

# Pre-render one page per language into the staging copy: the root becomes English and
# every other language gets its own folder, each with translated text already in the HTML
# and reciprocal hreflang. The sitemap is generated here too, replacing the placeholder.
SITE_ORIGIN="${SITE_ORIGIN:-https://neighbro.place}" RUN_NODE_MOUNT="$STAGE" \
  bash "$ROOT_DIR/deploy/run-node.sh" landing/build-pages.mjs "$STAGE"
# What never ships, decided in one place. It used to be decided in two, and the
# half that was a hand-written list of five names drifted: by 2026-08-18 the
# directory held ten tools, and check-contrast.mjs, check-legal-consistency.mjs,
# find-dead-keys.mjs, verify-seo.mjs and test-security-headers.sh were being
# served from the production storefront, which nobody had decided to publish.
#
# A rule does not go stale when a file is added the way a list does. Nothing the
# markup loads is .mjs or .sh — the one mention of build-pages.mjs in index.html
# is a comment — and the service worker is sw.js, which this leaves alone. It
# runs after build-pages, which needs its own .mjs to still be here.
find "$STAGE" -maxdepth 1 -type f \( -name '*.mjs' -o -name '*.sh' \) -delete
rm -f "$STAGE"/SPEC_*.md "$STAGE"/*standalone* "$STAGE"/*.zip
rm -rf "$STAGE"/img-src

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
# curl without --fail exits 0 on 401, 403 and 507, so this loop used to report a
# finished deploy over a zone that had rejected every byte. The failures are
# counted and named at the end rather than at the first one, and the run stops:
# what follows deletes files, and deleting after a half-finished upload is how a
# site disappears. Process substitution rather than a pipe, or the counter would
# live in a subshell and come back zero.
( cd "$STAGE"
  failed=0
  while IFS= read -r -d '' f; do
    rel="${f#./}"
    code="$(curl -sS -o /dev/null -w '%{http_code}' -X PUT \
      -H "AccessKey: ${BUNNY_STORAGE_API_KEY}" \
      -H "Content-Type: $(mime_type "$f")" \
      --data-binary "@${f}" \
      "${BASE_URL}/${rel}" || true)"
    case "$code" in
      2*) echo "  → /${rel}" ;;
      *)  echo "  ✗ /${rel} — HTTP ${code:-no response}"; failed=$((failed + 1)) ;;
    esac
  done < <(find . -type f -print0)
  [ "$failed" -eq 0 ] || {
    echo "${failed} file(s) did not upload — the zone is now half-updated." >&2
    exit 1
  }
)

# Uploading is only half of a deploy: until 2026-08-18 nothing was ever deleted,
# so a file dropped from the landing kept being served. It runs here because this
# is the one place where the directory compared against the zone is the directory
# that was just uploaded into it.
if [ "${SKIP_PRUNE:-}" = "1" ]; then
  echo "SKIP_PRUNE=1 — лишние файлы в зоне остаются как есть." >&2
else
  echo "Убираю из зоны то, чего нет в этой выкладке…"
  # Not fatal, and deliberately so: the prune runs after the upload, so a refusal
  # that stopped the run would leave the zone uploaded but the security headers
  # uncomputed and the cache unpurged — which is worse than leaving a stale file
  # behind. Loud, and the deploy carries on.
  if ! BUNNY_STORAGE_API_KEY="$BUNNY_STORAGE_API_KEY" \
       python3 "$ROOT_DIR/deploy/prune-storage-zone.py" "$BUNNY_STORAGE_ZONE" "$STAGE" --apply; then
    echo "  ⚠ уборка не выполнена — в зоне остаётся лишнее. Выкат продолжается." >&2
  fi
fi

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

# --- security headers --------------------------------------------------------
#
# Computed from the staged copy — the bytes about to be uploaded — and applied to
# the pull zone as one edge rule carrying every header. The policy names a sha256
# for each inline script, style block and style attribute, so a hand-kept list
# would go stale on the first markup edit; computing it here it cannot.
#
# The failure mode this guards against is specific: the header lives at the edge,
# a local server never sends it, so a wrong hash is a blank page in production and
# nowhere else. That is why this runs inside the deploy and not beside it.
# A way out when the builder itself is wrong. Rolling back by code fixes a policy
# that is wrong for these bytes; it does nothing when every version computes the
# same broken policy, and the page is then blank in production and fine
# everywhere else. SKIP_SECURITY_HEADERS=1 ships the files and purges without
# touching the rule; deploy/apply-edge-headers.py --remove (in xor.ad) takes an
# already-applied rule off a zone.
if [ "${SKIP_SECURITY_HEADERS:-}" = "1" ]; then
  echo "SKIP_SECURITY_HEADERS=1 — the policy is left exactly as it is on the zone." >&2
elif [ -n "${BUNNY_PULL_ZONE_ID:-}" ] && [ -n "${BUNNY_API_KEY:-}" ]; then
  echo "Building the security headers from the staged copy…"
  HEADERS_JSON="$(RELAY_API_URL="$RELAY_API_URL" ANALYTICS_ID="${ANALYTICS_ID:-}" \
    RUN_NODE_MOUNT="$STAGE" bash "$ROOT_DIR/deploy/run-node.sh" \
    landing/security-headers.mjs "$STAGE")"

  export HEADERS_JSON
  # The key through the environment, not argv: an argument is visible in
  # ps to every local account for the life of the call. HEADERS_JSON
  # already travelled this way; the key beside it did not.
  BUNNY_API_KEY="$BUNNY_API_KEY" \
  python3 - "$BUNNY_PULL_ZONE_ID" <<'PYEOF'
import json, os, sys, urllib.error, urllib.request

zone = sys.argv[1]
key = os.environ["BUNNY_API_KEY"]
data = json.loads(os.environ["HEADERS_JSON"])
headers = data["headers"]
print("  " + json.dumps(data["counted"]))

def action(header):
    return {
        "ActionType": 5,  # set response header — verified against the API, not remembered
        "ActionParameter1": header["name"],
        "ActionParameter2": header["value"],
        "ActionParameter3": None,
    }

# One rule, every header: an edge rule carries extra actions, so six rules per
# zone would be five more things to forget.
rule = {
    "Guid": None,
    **action(headers[0]),
    "ExtraActions": [action(h) for h in headers[1:]],
    "Enabled": True,
    "Description": "security headers (managed by deploy-landing.sh)",
    "TriggerMatchingType": 0,
    "Triggers": [{"Type": 0, "PatternMatches": ["*"], "PatternMatchingType": 0, "Parameter1": ""}],
}

# Replace our own rule rather than adding another: without the Guid every deploy
# would leave one more copy behind, and the last one to load would win silently.
def call(method, path, body=None):
    request = urllib.request.Request(
        f"https://api.bunny.net{path}", method=method,
        headers={"AccessKey": key, "content-type": "application/json"},
        data=json.dumps(body).encode() if body is not None else None)
    with urllib.request.urlopen(request, timeout=30) as response:
        raw = response.read()
        return json.loads(raw) if raw else {}

existing = call("GET", f"/pullzone/{zone}")
for item in existing.get("EdgeRules", []):
    if (item.get("Description") or "").startswith("security headers"):
        rule["Guid"] = item["Guid"]
        break

try:
    call("POST", f"/pullzone/{zone}/edgerules/addOrUpdate", rule)
except urllib.error.HTTPError as error:
    sys.exit(f"  edge rule refused: {error.code} {error.read()[:300]!r}")
print(f"  security headers applied to zone {zone}"
      f" ({'updated' if rule['Guid'] else 'created'}).")
PYEOF
else
  echo "BUNNY_PULL_ZONE_ID or BUNNY_API_KEY unset — security headers not applied." >&2
fi

if [ -n "${BUNNY_PULL_ZONE_ID:-}" ]; then
  echo "Purging pull zone ${BUNNY_PULL_ZONE_ID}…"
  curl -sS -X POST -H "AccessKey: ${PURGE_KEY}" \
    "https://api.bunny.net/pullzone/${BUNNY_PULL_ZONE_ID}/purgeCache" >/dev/null
  echo "  cache purged."
fi

echo "Landing deployed."

#!/usr/bin/env bash
# Render one social preview per language.
#
#   og/docker/run-all.sh              # every language
#   og/docker/run-all.sh --only ka    # one, for a look
#
# Playwright rather than the puppeteer image render.mjs uses: that image is not
# pullable here, and the browser is the only reason this needs a container at
# all. Nothing is installed on the host.
set -euo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO="$(dirname "$(dirname "$HERE")")"

docker run --rm \
  --user "$(id -u):$(id -g)" -e HOME=/tmp \
  -e OG_SITE="${OG_SITE:-}" \
  -v "$REPO":/repo \
  -w /tmp \
  --entrypoint bash \
  mcr.microsoft.com/playwright:v1.49.0-noble \
  -c '
    # -w создаётся демоном от root, поэтому подкаталог заводим уже здесь: /tmp открыт всем.
    work=$(mktemp -d) && cd "$work"
    npm init -y >/dev/null 2>&1
    npm install --silent playwright@latest >/dev/null 2>&1
    npx playwright install chromium >/dev/null 2>&1
    cp /repo/og/render-all.mjs "$work/render-all.mjs"
    OG_REPO=/repo node "$work/render-all.mjs" '"$*"'
  '

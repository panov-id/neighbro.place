#!/usr/bin/env bash
# Prepare the art/ folder from the raw drops, then composite the AI backgrounds
# into their target formats with the NEIGHBRO overlay. Args forward to art.mjs, e.g.
#   ./docker/run-art.sh --langs en,ru --only courtyard,windows
set -euo pipefail
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
WALLPAPERS_DIR="$(dirname "$HERE")"
REPO_DIR="$(dirname "$WALLPAPERS_DIR")"
IMAGE="neighbro-wallpapers:latest"

bash "$WALLPAPERS_DIR/art/prepare.sh"

echo "==> Building image $IMAGE"
docker build -t "$IMAGE" -f "$HERE/Dockerfile" "$WALLPAPERS_DIR"

echo "==> Compositing art (args: $*)"
docker run --rm \
  --user "$(id -u):$(id -g)" -e HOME=/tmp -e PUPPETEER_CACHE_DIR=/home/pptruser/.cache/puppeteer \
  -v "$REPO_DIR:/work/repo" \
  -w /work/repo \
  "$IMAGE" \
  wallpapers/art.mjs "$@"

echo "==> Output: $WALLPAPERS_DIR/output/art/index.html"

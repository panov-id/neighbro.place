#!/usr/bin/env bash
# Build the renderer image (once) and generate wallpapers into wallpapers/output/.
# All arguments are forwarded to render.mjs, e.g.:
#   ./docker/run.sh --formats ultrawide --themes gold,teal --styles glow,mesh
# No flags = curated default matrix. Never installs anything on the host.
set -euo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
WALLPAPERS_DIR="$(dirname "$HERE")"
REPO_DIR="$(dirname "$WALLPAPERS_DIR")"
IMAGE="neighbro-wallpapers:latest"

echo "==> Building image $IMAGE"
docker build -t "$IMAGE" -f "$HERE/Dockerfile" "$WALLPAPERS_DIR"

echo "==> Rendering (args: $*)"
docker run --rm \
  --user "$(id -u):$(id -g)" -e HOME=/tmp -e PUPPETEER_CACHE_DIR=/home/pptruser/.cache/puppeteer \
  -v "$REPO_DIR:/work/repo" \
  -w /work/repo \
  "$IMAGE" \
  wallpapers/render.mjs "$@"

echo "==> Output: $WALLPAPERS_DIR/output/index.html"

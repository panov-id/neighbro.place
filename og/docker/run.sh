#!/usr/bin/env bash
# Build the renderer image (once) and render the OG image.
#   ./docker/run.sh                  # candidate → og/output/og_photo.png
#   ./docker/run.sh --pick final     # final → landing/og-image.jpg
# Never installs anything on the host.
set -euo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
OG_DIR="$(dirname "$HERE")"
REPO_DIR="$(dirname "$OG_DIR")"
IMAGE="neighbro-og:latest"

echo "==> Building image $IMAGE"
docker build -t "$IMAGE" -f "$HERE/Dockerfile" "$OG_DIR"

echo "==> Rendering (args: $*)"
docker run --rm \
  --user "$(id -u):$(id -g)" -e HOME=/tmp -e PUPPETEER_CACHE_DIR=/home/pptruser/.cache/puppeteer \
  -v "$REPO_DIR:/work/repo" \
  -w /work/repo \
  "$IMAGE" \
  og/render.mjs "$@"

echo "==> Done"

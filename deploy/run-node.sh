#!/usr/bin/env bash
# Single entry point for the landing's Node tooling (check-i18n, page generation).
# Nothing Node-related runs on the host: the repository is mounted into a pinned
# container and the script runs there.
#
#   deploy/run-node.sh landing/check-i18n.mjs landing/index.html
#
# Paths are relative to the repository root, which is the container working directory.
#
# Environment:
#   NODE_IMAGE        container image to use (default: node:22-alpine)
#   RUN_NODE_NATIVE   set to 1 to use the host Node instead of a container; meant for
#                     CI runners, which already ship a pinned Node and have no Docker
#                     daemon worth spinning a container up for.
#   RUN_NODE_MOUNT    extra directory to mount at the same path inside the container,
#                     for scripts that write outside the repository (the deploy staging
#                     directory lives in /tmp and would otherwise be invisible)
#   SITE_ORIGIN       passed through to the script when set
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
NODE_IMAGE="${NODE_IMAGE:-node:22-alpine}"

if [ "$#" -eq 0 ]; then
  echo "usage: $(basename "$0") <script.mjs> [args...]" >&2
  exit 2
fi

if [ "${RUN_NODE_NATIVE:-0}" = "1" ]; then
  cd "$ROOT_DIR"
  exec node "$@"
fi

EXTRA_MOUNT=()
if [ -n "${RUN_NODE_MOUNT:-}" ]; then
  EXTRA_MOUNT=(--volume "${RUN_NODE_MOUNT}:${RUN_NODE_MOUNT}")
fi

exec docker run --rm \
  --volume "$ROOT_DIR:/work" \
  "${EXTRA_MOUNT[@]}" \
  --workdir /work \
  --user "$(id -u):$(id -g)" \
  --env SITE_ORIGIN \
  "$NODE_IMAGE" node "$@"

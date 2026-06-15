#!/usr/bin/env bash
# Remove local build artifacts (never committed except dist/)
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
CHAOS="$ROOT/variants/ultimate-chaos-pack"

echo "Removing build outputs..."
rm -rf \
  "$ROOT/pack" \
  "$ROOT/behavior_pack" \
  "$ROOT/build" \
  "$CHAOS/pack" \
  "$CHAOS/behavior_pack" \
  "$CHAOS/vanilla_src" \
  "$CHAOS/venice_cache"

echo "Clean complete. Rebuild with: ./scripts/build-mcaddon.sh"

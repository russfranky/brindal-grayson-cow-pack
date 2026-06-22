#!/usr/bin/env bash
# Remove local build artifacts (dist/ is committed for release installs).
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
VARIANT="$ROOT/variants/cel-band"

echo "Removing build outputs..."
rm -rf \
  "$VARIANT/build" \
  "$VARIANT/Cel_Band_Pack.mcpack" \
  "$ROOT/download/diorama_mc_output"

echo "Clean complete. Rebuild with: ./scripts/build_pack.sh"

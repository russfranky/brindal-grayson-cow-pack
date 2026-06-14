#!/usr/bin/env bash
# Build both Brindal & Grayson add-on variants into dist/
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
DIST="$ROOT/dist"
CHAOS="$ROOT/variants/ultimate-chaos-pack"

CUSTOM_BP="$ROOT/behavior_packs/brindal_grayson_cow_bp"
CUSTOM_RP="$ROOT/resource_packs/brindal_grayson_cow_rp"

mkdir -p "$DIST"

echo "=============================================="
echo " Brindal & Grayson Cow Pack — dual build"
echo "=============================================="

# --- 1. Custom Cows (lightweight, kid-friendly) ---
echo ""
echo ">>> Building custom-cows.mcaddon ..."
if [[ ! -d "$CUSTOM_BP" || ! -d "$CUSTOM_RP" ]]; then
  echo "Error: Custom cow packs not found in resource_packs/ and behavior_packs/" >&2
  exit 1
fi

CUSTOM_OUT="$DIST/custom-cows.mcaddon"
TEMP_CUSTOM=$(mktemp -d)
trap 'rm -rf "$TEMP_CUSTOM"' EXIT

cp -r "$CUSTOM_BP" "$TEMP_CUSTOM/brindal_grayson_cow_bp"
cp -r "$CUSTOM_RP" "$TEMP_CUSTOM/brindal_grayson_cow_rp"
(
  cd "$TEMP_CUSTOM"
  zip -qr "$CUSTOM_OUT" brindal_grayson_cow_bp brindal_grayson_cow_rp -x "*.DS_Store" -x "__MACOSX/*"
)
echo "Built: $CUSTOM_OUT ($(du -h "$CUSTOM_OUT" | cut -f1))"

# --- 2. Ultimate Chaos (full cowification pipeline) ---
echo ""
echo ">>> Building ultimate-chaos.mcaddon ..."
if [[ -f "$ROOT/requirements.txt" ]]; then
  pip3 install -r "$ROOT/requirements.txt" -q 2>/dev/null || true
fi

python3 "$CHAOS/scripts/build_all.py" --rebuild-textures

echo ""
echo "=============================================="
echo " Build complete — dist/"
ls -lh "$DIST"/custom-cows.mcaddon "$DIST"/ultimate-chaos.mcaddon "$DIST"/ultimate-chaos.mcpack 2>/dev/null || ls -lh "$DIST"/
echo "=============================================="
echo ""
echo "  custom-cows.mcaddon   — Brindal & Grayson custom cows (recommended for kids)"
echo "  ultimate-chaos.mcaddon — EVERYTHING becomes cows (needs experiments)"
echo "  ultimate-chaos.mcpack  — Visual-only chaos (no behavior/scripts)"

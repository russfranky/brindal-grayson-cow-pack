#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
DIST="$ROOT/dist"
OUTPUT="$DIST/brindal-grayson-cow-pack.mcaddon"
BP="$ROOT/behavior_packs/brindal_grayson_cow_bp"
RP="$ROOT/resource_packs/brindal_grayson_cow_rp"

echo "Building Brindal & Grayson Cow Pack..."

if [[ ! -d "$BP" ]]; then
  echo "Error: Behavior pack not found at $BP" >&2
  exit 1
fi

if [[ ! -d "$RP" ]]; then
  echo "Error: Resource pack not found at $RP" >&2
  exit 1
fi

rm -rf "$DIST"
mkdir -p "$DIST"

TEMP=$(mktemp -d)
trap 'rm -rf "$TEMP"' EXIT

cp -r "$BP" "$TEMP/brindal_grayson_cow_bp"
cp -r "$RP" "$TEMP/brindal_grayson_cow_rp"

cd "$TEMP"
zip -r "$OUTPUT" brindal_grayson_cow_bp brindal_grayson_cow_rp -x "*.DS_Store" -x "__MACOSX/*"

echo "Built: $OUTPUT"
echo "Import this file into Minecraft Bedrock to install both packs."

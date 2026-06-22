#!/usr/bin/env bash
# Assemble committed converted textures into Cel_Band_Pack.mcpack.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
VARIANT="$ROOT/variants/cel-band"
DOWNLOAD="$ROOT/download"

echo "=============================================="
echo " Cel Band Pack — assemble"
echo "=============================================="

python3 "$VARIANT/scripts/assemble_pack.py"
python3 "$VARIANT/scripts/convert_level.py" \
  --level "$VARIANT/levels/sample_level.json" \
  --output "$DOWNLOAD"
cp "$VARIANT/scripts/convert_level.py" "$DOWNLOAD/convert_level.py"
rm -rf "$DOWNLOAD/pack"
cp -r "$VARIANT/pack" "$DOWNLOAD/pack"

echo ""
echo "=============================================="
echo " Build complete"
ls -lh "$ROOT/dist/Cel_Band_Pack.mcpack"
echo "=============================================="

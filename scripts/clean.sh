#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"

echo "Removing local build outputs..."
rm -rf "$ROOT/variants/cel-band/build"

echo "Clean complete. Rebuild with: ./scripts/build_pack.sh"

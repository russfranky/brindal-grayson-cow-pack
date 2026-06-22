#!/usr/bin/env python3
"""Validate Cel Band Pack build artifacts."""

from __future__ import annotations

import json
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACK = ROOT / "dist" / "Cel_Band_Pack.mcpack"
PACK_SRC = ROOT / "variants" / "cel-band" / "pack"
SAMPLE = ROOT / "download" / "sample_level.json"


def fail(message: str) -> None:
    print(f"validate_pack: {message}", file=sys.stderr)
    raise SystemExit(1)


def main() -> None:
    if not PACK_SRC.is_dir():
        fail(f"missing pack source: {PACK_SRC}")

    if not (PACK_SRC / "manifest.json").is_file():
        fail("pack source missing manifest.json")

    if not PACK.is_file():
        fail(f"missing distributable: {PACK}")

    if PACK.stat().st_size < 8_000:
        fail(f"pack too small: {PACK.stat().st_size} bytes")

    with zipfile.ZipFile(PACK) as archive:
        names = archive.namelist()
        if "manifest.json" not in names:
            fail("pack missing manifest.json")
        if "pack_icon.png" not in names:
            fail("pack missing pack_icon.png")
        manifest = json.loads(archive.read("manifest.json"))
        header = manifest.get("header", {})
        if header.get("min_engine_version", [0, 0, 0]) < [1, 21, 0]:
            fail("manifest min_engine_version must be >= 1.21.0")
        if "lara" in header.get("name", "").lower() or "croft" in header.get("name", "").lower():
            fail("pack name must not reference trademarked franchises")

    if not SAMPLE.is_file():
        fail(f"missing sample level: {SAMPLE}")

    level = json.loads(SAMPLE.read_text())
    tiles = level.get("tiles", [])
    if len(tiles) < 40:
        fail(f"sample level too small: {len(tiles)} tiles")

    print("validate_pack: OK")


if __name__ == "__main__":
    main()

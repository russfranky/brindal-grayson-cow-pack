#!/usr/bin/env python3
"""Zip committed pack assets into Cel_Band_Pack.mcpack."""

from __future__ import annotations

import json
import zipfile
from pathlib import Path

VARIANT_ROOT = Path(__file__).resolve().parent.parent
PACK_DIR = VARIANT_ROOT / "pack"
VERSION_FILE = VARIANT_ROOT / "VERSION"
DIST_PACK = VARIANT_ROOT.parents[1] / "dist" / "Cel_Band_Pack.mcpack"
DOWNLOAD_PACK = VARIANT_ROOT.parents[1] / "download" / "Cel_Band_Pack.mcpack"


PACK_NAME = "Cel Band Pack"
PACK_DESCRIPTION = (
    "Converted cel-band textures for Bedrock 1.21+: four-step bands, warm stone, ink outlines."
)


def read_version() -> list[int]:
    parts = VERSION_FILE.read_text().strip().split(".")
    return [int(parts[0]), int(parts[1]), int(parts[2])]


def sync_manifest_version() -> None:
    manifest_path = PACK_DIR / "manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    version = read_version()
    manifest["header"]["name"] = PACK_NAME
    manifest["header"]["description"] = PACK_DESCRIPTION
    manifest["header"]["version"] = version
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")


def assemble(target: Path) -> None:
    target.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(target, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
        for path in sorted(PACK_DIR.rglob("*")):
            if path.is_file():
                zf.write(path, path.relative_to(PACK_DIR).as_posix())


def main() -> None:
    if not PACK_DIR.is_dir():
        raise SystemExit(f"pack source missing: {PACK_DIR}")

    sync_manifest_version()
    assemble(DIST_PACK)
    assemble(DOWNLOAD_PACK)
    kb = DIST_PACK.stat().st_size / 1024
    print(f"Assembled {DIST_PACK} ({kb:.1f} KB)")


if __name__ == "__main__":
    main()

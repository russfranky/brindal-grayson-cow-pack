# Contributing

Thank you for improving the **Cel Band Toolkit** for Minecraft Bedrock.

## Repository layout

| Path | Role |
|------|------|
| `variants/cel-band/scripts/diorama_mc_tool.py` | Texture generator, pack assembler, voxel converter |
| `variants/cel-band/levels/` | Sample level JSON |
| `variants/cel-band/VERSION` | Pack semver (bumped on release) |
| `dist/` | Committed distributable `.mcpack` |
| `download/` | Release bundle mirrored from builds |

## Build and validate

```bash
pip3 install -r requirements.txt
./scripts/build_pack.sh
python3 scripts/validate_pack.py
./scripts/clean.sh   # remove local build dirs only
```

## Conventions

- **Palette changes** — edit `PALETTE` and tile mappings in `diorama_mc_tool.py`, then rebuild.
- **Pack UUID** — do not change manifest UUIDs after a public release.
- **Versioning** — `variants/cel-band/VERSION` follows semver; `publish.yml` bumps patch on merge to `main`.
- **Pre-commit** — `pip install -r requirements.txt && pre-commit install`

## Pull requests

1. Run `./scripts/build_pack.sh` and `python3 scripts/validate_pack.py`.
2. Describe palette, level, or tooling changes.
3. Attach in-game screenshots when texture output changes.

## Issues

Open a [GitHub Issue](https://github.com/russfranky/charles-world-of-chaos/issues) with Minecraft version, platform, and steps to reproduce.

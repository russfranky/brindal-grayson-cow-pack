# Installation

Install **Cel Band Pack** on Minecraft Bedrock 1.21 or newer.

## Download

**[Latest release — Cel_Band_Pack.mcpack](https://github.com/russfranky/charles-world-of-chaos/releases/latest/download/Cel_Band_Pack.mcpack)**

Or build locally: `./scripts/build_pack.sh` → open `dist/Cel_Band_Pack.mcpack`.

## Platform steps

### Windows / macOS

1. Double-click the `.mcpack` file.
2. **Settings → Global Resources** → activate **Cel Band Pack**.
3. Open any world.

### iOS / iPadOS

1. Download in Safari → **Open in Minecraft**.
2. **Settings → Global Resources** → activate the pack.

### Android

1. Download and open with Minecraft.
2. Activate under **Settings → Global Resources**.

## Per-world activation

Edit world → **Resource Packs** → add **Cel Band Pack**.

## Updating

Re-import the latest release `.mcpack`. Pack UUID is stable; newer semver replaces the previous install.

## Troubleshooting

| Problem | Fix |
|---------|-----|
| Import failed | Update Minecraft to 1.21.0+ |
| Textures unchanged | Confirm pack is in **Active** resources |
| Checkerboard blocks | Re-import and activate |
| Java Edition | Bedrock only |

## Sample build

```bash
python3 variants/cel-band/scripts/diorama_mc_tool.py --mode convert \
  --level variants/cel-band/levels/sample_level.json \
  --origin 100,64,200
```

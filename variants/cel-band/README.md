# Cel Band Toolkit — Bedrock 1.21+

Four-step cel bands, Holstein spots, ink outlines, and a voxel level converter for Minecraft Bedrock.

## Quick start

```bash
./scripts/build_pack.sh

python3 variants/cel-band/scripts/diorama_mc_tool.py --mode all \
  --output variants/cel-band/build
```

## Cel bands

| Band | Block | Use |
|------|-------|-----|
| Lit cream | `calcite` | Top faces |
| Warm sand | `stone` | Lit sides |
| Warm brown | `deepslate` | Shadow sides |
| Deep shadow | `bedrock` | Cave floors |

## Files

| Path | Role |
|------|------|
| `scripts/diorama_mc_tool.py` | Textures, pack assembly, voxel conversion |
| `levels/sample_level.json` | Cave of Snakes sample (12 tile types) |
| `VERSION` | Pack semver |

Install: `dist/Cel_Band_Pack.mcpack` → **Settings → Global Resources**.

# Cel Band Toolkit

A **Minecraft Bedrock 1.21+ cel-band system** for builders: procedural block textures, a voxel level converter, and a tile specification — not just a resource pack.

| Component | What it does |
|-----------|--------------|
| **Cel Band Pack** | Global resource pack — four-step cel bands, Holstein spots, ink outlines |
| **Voxel converter** | Level JSON → `/setblock` commands and `.mcfunction` files |
| **Voxel spec** | 12 tile types, palette rules, builder reference (PDF) |

---

## Install the pack

### Option A — Latest release

**[Cel_Band_Pack.mcpack](https://github.com/russfranky/charles-world-of-chaos/releases/latest/download/Cel_Band_Pack.mcpack)**

1. Open the file on your device (or import via Minecraft).
2. Go to **Settings → Global Resources** and activate **Cel Band Pack**.
3. Load any Bedrock world — block textures update immediately.

### Option B — Build from source

```bash
pip3 install -r requirements.txt
./scripts/build_pack.sh
```

Output: `dist/Cel_Band_Pack.mcpack`. See [docs/installation.md](docs/installation.md).

---

## Visual system

Four cel bands map to vanilla blocks for in-game placement:

| Band | Block | Use |
|------|-------|-----|
| Lit cream | `calcite` | Top faces, highlights |
| Warm sand | `stone` | Lit side faces |
| Warm brown | `deepslate` | Occluded sides |
| Deep shadow | `bedrock` | Cave floors, underhangs |

Holstein spot masks and ink outlines are baked into block textures. Relic blocks (gold, emerald, copper) use bronze and jade tones. Water, moss, bark, and dirt each have their own three-band variants.

---

## Voxel pipeline

Author levels as JSON, convert to Bedrock placements:

```bash
python3 variants/cel-band/scripts/diorama_mc_tool.py --mode convert \
  --level variants/cel-band/levels/sample_level.json \
  --origin 100,64,200
```

The included **Cave of Snakes** sample (`download/sample_level.json`) exercises all 12 tile types.

---

## Repository layout

| Path | Description |
|------|-------------|
| `dist/Cel_Band_Pack.mcpack` | Shipped resource pack |
| `variants/cel-band/` | Generator source, sample level, version |
| `variants/cel-band/scripts/diorama_mc_tool.py` | Textures + pack + voxel converter |
| `download/` | Release bundle (pack, tool, sample, voxel spec PDF) |

---

## Documentation

- [Installation guide](docs/installation.md)
- [Development guide](docs/development.md)
- [Voxel spec PDF](download/Voxel_Spec.pdf)

---

## Requirements

| Requirement | Notes |
|-------------|-------|
| Minecraft Bedrock 1.21.0+ | Not Java Edition |
| Python 3.11+ | For local builds (`Pillow`) |

---

## License

MIT — see [LICENSE](LICENSE).

This project is not affiliated with or endorsed by Mojang Studios.

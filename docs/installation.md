# Installation

Install **Cel Band Pack** on Minecraft Bedrock 1.21+.

**[Cel_Band_Pack.mcpack](https://github.com/russfranky/charles-world-of-chaos/releases/latest/download/Cel_Band_Pack.mcpack)**

Or: `./scripts/build_pack.sh` → `dist/Cel_Band_Pack.mcpack`.

1. Import the `.mcpack`.
2. **Settings → Global Resources** → activate **Cel Band Pack**.
3. Open any world.

Per-world: edit world → **Resource Packs** → add **Cel Band Pack**.

## Sample build

```bash
python3 variants/cel-band/scripts/convert_level.py \
  --level variants/cel-band/levels/sample_level.json \
  --origin 100,64,200
```

Use `download/sample_level.setblock` in-game at the chosen origin.

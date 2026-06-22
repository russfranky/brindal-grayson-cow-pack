# Development

## Build

```bash
./scripts/build_pack.sh
```

Steps:

1. `assemble_pack.py` reads `variants/cel-band/pack/`, syncs semver from `VERSION`, zips to `dist/` and `download/`.
2. `convert_level.py` writes `download/sample_level.setblock` from the sample level.

No Pillow or texture synthesis — only packaging and level conversion.

## Pack source

```
variants/cel-band/pack/
  manifest.json
  pack_icon.png
  textures/blocks/
  textures/items/
  textures/ui/
```

Edit PNGs directly or drop in newly converted textures, then rebuild.

## Level conversion

```bash
python3 variants/cel-band/scripts/convert_level.py \
  --level my_level.json \
  --origin 100,64,200 \
  --output download/
```

Tile types are defined in `download/Voxel_Spec.pdf`.

## Versioning

- `variants/cel-band/VERSION` — semver written into manifest on build
- `pack_version.py --bump-patch` — used by publish workflow

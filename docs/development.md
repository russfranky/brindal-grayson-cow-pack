# Development

## Prerequisites

- Python 3.11+
- `pip install -r requirements.txt` (Pillow)

## Build pipeline

```bash
./scripts/build_pack.sh
```

1. Runs `diorama_mc_tool.py --mode all` → `variants/cel-band/build/`
2. Copies `Cel_Band_Pack.mcpack` to `dist/` and `download/`
3. Syncs tool outputs to `download/`

```bash
python3 scripts/validate_pack.py
```

## Generator modes

```bash
TOOL=variants/cel-band/scripts/diorama_mc_tool.py

python3 $TOOL --mode all --output variants/cel-band/build
python3 $TOOL --mode textures --output variants/cel-band/build
python3 $TOOL --mode pack --output variants/cel-band/build
python3 $TOOL --mode convert --level my_level.json --origin 100,64,200 \
  --output variants/cel-band/build
```

## Level JSON format

Levels have a `tiles` array. Each tile: `x`, `z`, optional `y`, and `type` (one of 12 tile types in the voxel spec).

See `variants/cel-band/levels/sample_level.json` and `download/Voxel_Spec.pdf`.

## Versioning

- Semver: `variants/cel-band/VERSION`
- Bump: `python3 variants/cel-band/scripts/pack_version.py --bump-patch`
- Publish: merge to `main` → `publish.yml`

## Project structure

```
variants/cel-band/
  VERSION
  levels/sample_level.json
  scripts/diorama_mc_tool.py
  scripts/pack_version.py
dist/Cel_Band_Pack.mcpack
download/
scripts/build_pack.sh
scripts/validate_pack.py
```

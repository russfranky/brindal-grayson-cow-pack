# Testing Guide — Cel Band Toolkit

## Automated (Linux CI)

| Check | Command | Notes |
|-------|---------|-------|
| Build completes | `./scripts/build_pack.sh` | Pack + download bundle |
| Pack structure | `python3 scripts/validate_pack.py` | Manifest, icon, engine version |
| Sample level | `validate_pack.py` | ≥ 35 tiles |
| Pack size | `validate_pack.py` | `.mcpack` ≥ 5 KB |

CI uploads `dist/Cel_Band_Pack.mcpack` as an artifact on every PR to `main`.

## Manual (in-game)

1. Import `dist/Cel_Band_Pack.mcpack`.
2. Activate under **Settings → Global Resources**.
3. Open a creative world (Bedrock 1.21+).
4. Confirm cel bands on `calcite` / `stone` / `deepslate` / `bedrock`, relic palette on gold/emerald/copper, correct pack name and icon.
5. Optional: paste sample build via `sample_level.setblock` or `diorama_level.mcfunction`.

## Local commands

```bash
./scripts/build_pack.sh
python3 scripts/validate_pack.py
python3 variants/cel-band/scripts/diorama_mc_tool.py --mode textures \
  --output variants/cel-band/build
python3 variants/cel-band/scripts/diorama_mc_tool.py --mode convert \
  --level my_level.json --origin 0,100,0
./scripts/clean.sh
```

## Release path

Merges to `main` trigger `publish.yml`: patch bump → build → validate → commit `dist/` → GitHub Release.

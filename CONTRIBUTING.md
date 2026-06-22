# Contributing

## Layout

| Path | Role |
|------|------|
| `variants/cel-band/pack/` | Converted PNG textures and manifest |
| `variants/cel-band/scripts/assemble_pack.py` | Packages `pack/` into `.mcpack` |
| `variants/cel-band/scripts/convert_level.py` | Tile JSON → Bedrock placements |
| `variants/cel-band/levels/` | Sample level JSON |

## Workflow

```bash
./scripts/build_pack.sh
python3 scripts/validate_pack.py
```

To ship new art: add or replace PNGs in `variants/cel-band/pack/`, then rebuild. Do not regenerate textures in CI — commit the converted assets.

## Pull requests

- Run build + validate before opening.
- Include screenshots when texture files change.
- Note which source assets were converted when adding textures.

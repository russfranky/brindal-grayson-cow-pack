# Testing Guide

## What Linux CI Can Test

| Check | Automated | Notes |
|-------|-----------|-------|
| Build pipeline completes | Yes | `./scripts/build-mcaddon.sh` |
| Texture count (4000+) | Yes | `validate_pack.py` |
| Entity override count (100+) | Yes | Client entities use `geometry.cow.v2` |
| BP transform count (100+) | Yes | `bgcow:transform_to_cow` component group |
| Spawn rules zeroed (50+) | Yes | Non-cow weight = 0 |
| Custom Brindal/Grayson cows present | Yes | Textures + entity files after merge |
| Manifest UUID linkage | Yes | BP depends on RP UUID `d36a0504-...` |
| Script API file present | Yes | `behavior_pack/scripts/main.js` |
| Package artifacts exist | Yes | `.mcaddon` and `.mcpack` in `dist/` |
| Venice AI textures | Optional | Requires `VENICE_API_KEY` locally or in CI secret |
| Sounds play as cow moos | No | Requires in-game testing |
| Mobs visually render as cows | No | Requires Bedrock client |
| Transform-on-spawn works | No | Requires world with BP + experiments |
| Script API commands | No | Requires Beta APIs enabled |
| iPad import via Safari | No | Requires physical iPad |

## What Requires iPad / macOS Testing

### iPad (primary target)

1. Download `.mcaddon` from GitHub raw URL or AirDrop from Mac
2. Open in Minecraft → verify both packs import
3. Create new world:
   - Holiday Creator Features: **ON**
   - Beta APIs: **ON**
   - Both packs: **activated**
4. Verify:
   - [ ] Blocks/items have cow-hide textures
   - [ ] Diamond block shows "B", gold block shows "G"
   - [ ] Zombies, creepers, etc. appear as cows
   - [ ] Mobs make cow sounds
   - [ ] Button clicks moo (cow GUI sounds)
   - [ ] Inventory/chest backgrounds show cow spots
   - [ ] Non-cow mobs transform to cows on spawn
   - [ ] Brindal and Grayson cows spawn and are NOT transformed away
   - [ ] `!moo`, `!party`, `/bgcow:help` work

### macOS Minecraft Bedrock

Same as iPad. After building, copy packs from:

```
variants/ultimate-chaos-pack/pack/          → development_resource_packs/
variants/ultimate-chaos-pack/behavior_pack/ → development_behavior_packs/
```

## CI Artifacts

Every push to `main` uploads:
- `brindal-grayson-cow-pack.mcaddon`
- `brindal-grayson-cow-pack.mcpack`

Download from **Actions** → latest workflow run → **Artifacts**.

CI builds algorithmic textures + cow GUI. Venice AI art requires `VENICE_API_KEY` (maintainer rebuild).

## Manual Validation Commands

```bash
# Full rebuild
./scripts/build-mcaddon.sh

# Validate structure
python3 variants/ultimate-chaos-pack/scripts/validate_pack.py

# Count cowified textures
find variants/ultimate-chaos-pack/pack/textures -name '*.png' | wc -l

# Count entity overrides
grep -rl 'geometry.cow.v2' variants/ultimate-chaos-pack/pack/entity/ | wc -l

# Count BP transforms
grep -rl 'bgcow:transform_to_cow' variants/ultimate-chaos-pack/behavior_pack/entities/ | wc -l

# Check dist sizes
ls -lh dist/

# Clean build artifacts
./scripts/clean.sh
```

## Known Limitations

- Linux CI cannot run Minecraft Bedrock
- Default CI build uses algorithmic cow-hide + procedural GUI (not Venice AI)
- Some complex mobs may have visual glitches when forced to cow geometry
- Script API requires Beta APIs experimental toggle
- JSON UI modifications may need updates after major Bedrock releases

# Development Guide

This repo has two add-ons. See [installation.md](installation.md) for which to use.

## Custom Cows — layout

| Path | Purpose |
|------|---------|
| `manifest.json` | Pack metadata and resource pack dependency |
| `entities/` | Entity behavior definitions (AI, health, breeding) |
| `spawn_rules/` | Natural spawn conditions |
| `texts/` | Localization strings |

### Resource Pack (`resource_packs/brindal_grayson_cow_rp/`)

| Path | Purpose |
|------|---------|
| `manifest.json` | Pack metadata |
| `entity/` | Client-side entity definitions (textures, animations) |
| `textures/entity/` | Cow texture PNG files |
| `texts/` | Localization strings |

## Local Development Workflow

### Option A: Development Folders (Recommended)

1. Copy or symlink the pack folders into Minecraft's development directories:

   **Windows:**
   ```
   %localappdata%\Packages\Microsoft.MinecraftUWP_8wekyb3d8bbwe\LocalState\games\com.mojang\development_behavior_packs\brindal_grayson_cow_bp
   %localappdata%\Packages\Microsoft.MinecraftUWP_8wekyb3d8bbwe\LocalState\games\com.mojang\development_resource_packs\brindal_grayson_cow_rp
   ```

   **iPad (with file access):**
   ```
   games/com.mojang/development_behavior_packs/brindal_grayson_cow_bp
   games/com.mojang/development_resource_packs/brindal_grayson_cow_rp
   ```

2. Create a world with both packs activated
3. Edit JSON files in your editor
4. Reload the world (exit and re-enter) to pick up changes

### Option B: Build and Import

1. Edit files in the repository
2. Run `./scripts/build-mcaddon.sh`
3. Import the resulting `.mcaddon` into Minecraft
4. Test in a world with the packs enabled

## Adding a New Cow Variant

1. Create `behavior_packs/.../entities/new_cow.json` with identifier `bgcow:new_cow`
2. Create `resource_packs/.../entity/new_cow.entity.json`
3. Add a texture at `resource_packs/.../textures/entity/new_cow.png`
4. Add spawn rules in `behavior_packs/.../spawn_rules/new_cow.json`
5. Add localization strings to both `texts/en_US.lang` files
6. Test with `/summon bgcow:new_cow`

## Ultimate Chaos — layout

See [variants/ultimate-chaos-pack/README.md](../variants/ultimate-chaos-pack/README.md). Build scripts live in `variants/ultimate-chaos-pack/scripts/`. Vanilla assets are cloned to `variants/ultimate-chaos-pack/vanilla_src/` at build time.

```bash
python3 variants/ultimate-chaos-pack/scripts/build_all.py --rebuild-textures
python3 variants/ultimate-chaos-pack/scripts/validate_pack.py
```

## Manifest UUIDs

Each pack has unique UUIDs in its `manifest.json`. The behavior pack's `dependencies` section references the resource pack UUID. **Never change these UUIDs** after a public release — doing so will break existing worlds.

## Useful Commands

```
/summon bgcow:brindal_cow          # Spawn Brindal
/summon bgcow:grayson_cow          # Spawn Grayson
/kill @e[type=bgcow:brindal_cow]   # Remove all Brindal cows
/gamerule doMobSpawning true       # Ensure natural spawning is on
```

## References

- [Bedrock Wiki — Pack Structure](https://wiki.bedrock.dev/documentation/pack-structure)
- [Microsoft Learn — Behavior Packs](https://learn.microsoft.com/en-us/minecraft/creator/documents/behaviorpack)
- [Mojang Bedrock Samples](https://github.com/Mojang/bedrock-samples)

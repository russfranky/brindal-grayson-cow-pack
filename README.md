# Brindal & Grayson Cow Pack

A Minecraft Bedrock Edition add-on that introduces two custom cows — **Brindal** and **Grayson** — designed for iPad and other Bedrock platforms.

## Features

- Two custom cow entities with unique textures
- Natural spawning in animal biomes alongside vanilla cows
- Full cow behaviors: milking, breeding, aging, and herd spawning
- Cross-breeding between Brindal and Grayson cows

## Repository Structure

```
brindal-grayson-cow-pack/
├── behavior_packs/
│   └── brindal_grayson_cow_bp/     # Entity logic, spawn rules, loot
├── resource_packs/
│   └── brindal_grayson_cow_rp/     # Textures, models, client entities
├── docs/
│   ├── installation.md             # iPad and desktop install guide
│   └── development.md              # Local development workflow
├── scripts/
│   └── build-mcaddon.sh            # Package add-on for distribution
├── LICENSE
└── README.md
```

## Quick Start

### Install on iPad

1. Run `./scripts/build-mcaddon.sh` to create `dist/brindal-grayson-cow-pack.mcaddon`
2. Transfer the `.mcaddon` file to your iPad (AirDrop, email, or cloud storage)
3. Open the file in Minecraft — both packs import automatically
4. Create or edit a world, enable the behavior and resource packs, and turn on **Holiday Creator Features** or **Beta APIs** if prompted

See [docs/installation.md](docs/installation.md) for detailed platform-specific instructions.

### Local Development

Copy the pack folders into your Minecraft development directories:

| Platform | Behavior Pack Path | Resource Pack Path |
|----------|-------------------|-------------------|
| iPad | `games/com.mojang/development_behavior_packs/` | `games/com.mojang/development_resource_packs/` |
| Windows | `%localappdata%\Packages\...\development_behavior_packs\` | `%localappdata%\Packages\...\development_resource_packs\` |

See [docs/development.md](docs/development.md) for the full development workflow.

## Custom Entities

| Entity | Identifier | Description |
|--------|-----------|-------------|
| Brindal Cow | `bgcow:brindal_cow` | Brown cow with white spots |
| Grayson Cow | `bgcow:grayson_cow` | Gray cow with dark spots |

Summon in-game with:

```
/summon bgcow:brindal_cow
/summon bgcow:grayson_cow
```

## Requirements

- Minecraft Bedrock Edition 1.21.0 or later
- Experimental gameplay toggles may be required depending on your Minecraft version

## Contributing

Contributions are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## License

This project is licensed under the [MIT License](LICENSE).

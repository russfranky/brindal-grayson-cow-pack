# Contributing

Thank you for your interest in improving the Brindal & Grayson Cow Pack.

## Getting Started

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-change`
3. Make your changes in the appropriate pack folder
4. Test in Minecraft Bedrock before submitting
5. Open a pull request with a clear description of what changed and why

## Pack Conventions

- **Namespace**: Use the `bgcow:` prefix for all custom identifiers
- **Behavior pack**: JSON entity definitions go in `behavior_packs/brindal_grayson_cow_bp/`
- **Resource pack**: Textures and client entities go in `resource_packs/brindal_grayson_cow_rp/`
- **UUIDs**: Do not change existing UUIDs in `manifest.json` files — this breaks worlds that already use the pack
- **Versioning**: Bump the version in both manifest files when releasing

## Textures

Entity textures live in `resource_packs/brindal_grayson_cow_rp/textures/entity/`. Textures should be 64×64 PNG files that follow the vanilla cow UV layout.

## Testing Checklist

Before submitting a pull request, verify:

- [ ] Both cows spawn naturally in animal biomes
- [ ] Spawn eggs appear in the creative inventory
- [ ] Cows can be milked with a bucket
- [ ] Cows can be bred with wheat
- [ ] Baby cows grow into adults
- [ ] Textures render correctly (no missing texture checkerboard)

## Reporting Issues

Use the [GitHub issue tracker](https://github.com/russfranky/brindal-grayson-cow-pack/issues) and include:

- Minecraft version and platform (e.g., iPad, Windows, Android)
- Steps to reproduce
- Expected vs. actual behavior
- Screenshots if applicable

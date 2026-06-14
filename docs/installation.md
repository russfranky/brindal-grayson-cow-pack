# Installation Guide

## Building the Add-On

From the repository root:

```bash
./scripts/build-mcaddon.sh
```

This creates `dist/brindal-grayson-cow-pack.mcaddon`, a single file that contains both the behavior and resource packs.

## iPad (iOS)

1. Build or download the `.mcaddon` file
2. Transfer it to your iPad using one of:
   - **AirDrop** from a Mac
   - **Files app** via iCloud Drive, Dropbox, or Google Drive
   - **Email** the file as an attachment and open it on iPad
3. Tap the `.mcaddon` file — Minecraft opens and imports both packs
4. Create a new world (or edit an existing one):
   - Go to **Settings** → **Behavior Packs** → activate **Brindal & Grayson Cow BP**
   - Go to **Resource Packs** → activate **Brindal & Grayson Cow RP**
5. Enable experimental features if prompted
6. Create the world and explore

## Windows 10/11

1. Double-click the `.mcaddon` file, or place pack folders in:
   ```
   %localappdata%\Packages\Microsoft.MinecraftUWP_8wekyb3d8bbwe\LocalState\games\com.mojang\
   ```
2. Launch Minecraft → **Play** → **Create New** or edit a world
3. Activate both packs under Behavior Packs and Resource Packs

## Android

1. Transfer the `.mcaddon` file to your device
2. Open it with Minecraft (use a file manager app)
3. Activate both packs in world settings

## Verifying Installation

After loading a world with the packs enabled:

1. Open chat and run `/summon bgcow:brindal_cow`
2. Run `/summon bgcow:grayson_cow`
3. Both cows should appear with their custom textures

If cows appear as checkered black-and-purple blocks, the resource pack is not active. Re-check world settings.

## Troubleshooting

| Problem | Solution |
|---------|----------|
| Packs don't appear in world settings | Re-import the `.mcaddon` file; restart Minecraft |
| Cows have missing textures | Ensure the resource pack is activated, not just the behavior pack |
| Cows don't spawn naturally | Make sure you're in an animal biome (plains, forest) and wait for natural spawning |
| "Pack failed to import" | Verify you're on Minecraft Bedrock 1.21.0 or later |

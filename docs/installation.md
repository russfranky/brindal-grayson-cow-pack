# Installation Guide

This repo ships two add-ons. Pick the right one for your kids.

## Which add-on should I install?

| | Custom Cows | Ultimate Chaos |
|---|-------------|----------------|
| **File** | `custom-cows.mcaddon` | `ultimate-chaos.mcaddon` |
| **For** | Brindal & Grayson's everyday worlds | Silly "everything is cows" mode |
| **Experiments needed** | No | Yes (Holiday Creator + Beta APIs) |
| **Changes vanilla mobs** | No — adds 2 new cow types | Yes — all mobs become cows |
| **Changes textures** | Only the 2 custom cows | Everything (4600+ textures) |

**Start with Custom Cows.** Add Ultimate Chaos when you want chaos.

---

## Custom Cows — iPad

1. Download [custom-cows.mcaddon](https://github.com/russfranky/brindal-grayson-cow-pack/raw/main/dist/custom-cows.mcaddon)
2. Transfer via AirDrop, Files, or email
3. Tap the file → **Open in Minecraft**
4. Create or edit a world → activate **Brindal & Grayson Cow BP** and **Brindal & Grayson Cow RP**
5. Explore plains/forest biomes or run `/summon bgcow:brindal_cow`

## Ultimate Chaos — iPad

1. Download [ultimate-chaos.mcaddon](https://github.com/russfranky/brindal-grayson-cow-pack/raw/main/dist/ultimate-chaos.mcaddon)
2. Tap → **Open in Minecraft**
3. Create a **NEW** world:
   - Holiday Creator Features: **ON**
   - Beta APIs: **ON**
   - Activate both Ultimate Chaos packs
4. Everything should look and sound like cows

Visual-only (no experiments): [ultimate-chaos.mcpack](https://github.com/russfranky/brindal-grayson-cow-pack/raw/main/dist/ultimate-chaos.mcpack)

---

## Building locally

```bash
pip3 install -r requirements.txt
./scripts/build-mcaddon.sh
```

Output in `dist/`:
- `custom-cows.mcaddon`
- `ultimate-chaos.mcaddon`
- `ultimate-chaos.mcpack`

## Windows / Android

Same steps — download the `.mcaddon`, open with Minecraft, activate packs in world settings.

## Troubleshooting

| Problem | Solution |
|---------|----------|
| Packs don't appear | Re-import the `.mcaddon`; restart Minecraft |
| Missing textures (checkerboard) | Ensure **both** resource and behavior packs are active |
| Ultimate Chaos mobs aren't cows | Enable Holiday Creator Features + Beta APIs; create a **new** world |
| Custom cows don't spawn | Use animal biomes (plains, forest); or `/summon bgcow:brindal_cow` |
| Pack failed to import | Requires Minecraft Bedrock 1.21.0+ |

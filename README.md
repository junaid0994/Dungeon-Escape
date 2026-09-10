# Dungeon Explorer — Improved Edition

A text-based dungeon crawler with leveling, scaling difficulty, and a shop system. Explore rooms, fight enemies that get tougher as you grow, collect loot, and spend coins to power up.

## How to Play

```bash
python dungeon_game.py
```

Enter your name to begin. Each turn you choose from:

```
1. Explore Dungeon
2. Check Stats
3. Visit Shop
4. Quit Game
```

## Exploring

Each exploration triggers one random event, weighted so some are more common than others:

| Event | Chance | Effect |
|---|---|---|
| Enemy encounter | 35% | Turn-based combat — see below |
| Coin Chest | 15% | +30 coins |
| Trap | 15% | -20 health, attack -5 (min 5), coins -20 (min 0) |
| Nothing | 15% | No effect |
| Mysterious Box | 12% | +10 attack, +15 health |
| Healing Spring | 8% | +30 health (capped at max) |

## Combat

Enemies scale with your level — early on you'll only face Goblins, Wolves, and Bandits; as you level up, Orcs, Trolls, and eventually the Dark Knight enter the pool. Each enemy also has a randomized stat variance (±10-20%) so no two fights feel identical.

When an enemy appears:
- **Attack** — trade hits until one of you reaches 0 health. Winning grants coins and XP.
- **Run** — usually escapes safely, but there's a 40% chance of taking a parting hit (half the enemy's attack power) on the way out.

## Leveling Up

Defeating enemies grants XP. Once you cross the XP threshold, you level up:
- Max health +20 (and you're fully healed)
- Attack +5
- The XP needed for the next level increases (×1.4 each time)

## Shop

Spend coins between explorations:

| Item | Cost | Effect |
|---|---|---|
| Heal 30 HP | 20 coins | Restores health (capped at max) |
| +5 Attack | 30 coins | Permanent attack boost |

## Starting Stats

| Stat | Value |
|---|---|
| Health | 100 / 100 |
| Attack Power | 20 |
| Coins | 50 |
| Level | 1 |

## What Changed From the Original Version

- Health, attack, and coins are now capped — no more overflow above max health or dropping below 0.
- Trap damage is now checked for a player death (previously the game could continue after health hit 0).
- Mysterious Box gives a flat +10 attack instead of doubling it, so it can't be farmed into an exponential exploit.
- Running from a fight carries a small risk instead of being guaranteed-safe.
- Added leveling, XP, scaling enemy difficulty, and a shop — coins and progress now have an ongoing purpose.

## Requirements

- Python 3
- No external libraries — only the built-in `random` module

## Known Limitations

- No save/load — progress resets each run.
- No inventory system — items are instant-use rather than carried.
- Only one boss-tier enemy (Dark Knight); no dedicated boss fight at set milestones yet.

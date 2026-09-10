# Dungeon Explorer (Console Game)

A simple text-based dungeon crawler written in Python. Explore rooms, fight goblins, find loot, and avoid traps — all from the terminal.

## How to Play

Run the script and enter your name to begin:

```bash
python dungeon_game.py
```

You'll see your starting stats, then a menu each turn:

```
1. Explore Dungeon
2. Check Stats
3. Quit Game
```

### Exploring
Choosing **Explore Dungeon** puts you in a random room. One of five things can happen:

| Event | Effect |
|---|---|
| **Mysterious Box** | Find a Holy Sword — attack doubles, +15 health |
| **Coin Chest** | +30 coins |
| **Goblin** | Enter combat — see below |
| **Nothing** | No effect, just flavor text |
| **Trap** | -10 attack, -20 health, -20 coins |

### Goblin Combat
When a goblin appears, choose to **Attack** or **Run**.

- Running ends the encounter safely with no risk.
- Attacking starts a turn-based fight: you deal your attack power to the goblin, then it deals its attack power to you, repeating until one of you reaches 0 health. Defeating a goblin gives +20 coins. If your health hits 0, the game ends.

### Checking Stats
Shows your current health, attack power, and coin count at any time.

### Quitting
Exits the game loop immediately.

## Starting Stats

| Stat | Value |
|---|---|
| Health | 100 |
| Attack Power | 20 |
| Coins | 50 |

## Requirements

- Python 3
- No external libraries — only the built-in `random` module

## Known Limitations

- Health, attack, and coins have no upper/lower caps, so a lucky or unlucky run can push stats out of a reasonable range (e.g. a trap can take coins below the amount you actually have, or repeated Mysterious Box events can double attack power indefinitely).
- Difficulty doesn't scale — goblin stats are randomly picked from a fixed list regardless of how far you've progressed.
- No save/load — progress is lost when the game ends.

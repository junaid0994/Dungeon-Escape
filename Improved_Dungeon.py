import random

# ---------- Data ----------

ENEMY_TEMPLATES = [
    # name, base_health, base_attack, coin_reward, xp_reward
    ("Goblin", 40, 8, 15, 10),
    ("Wolf", 55, 12, 20, 15),
    ("Bandit", 70, 15, 30, 20),
    ("Orc", 90, 18, 40, 30),
    ("Troll", 130, 22, 60, 45),
    ("Dark Knight", 160, 28, 90, 65),
]

EVENTS = ["enemy", "mysterious_box", "coin_chest", "nothing", "trap", "healing_spring"]
EVENT_WEIGHTS = [35, 12, 15, 15, 15, 8]  # out of 100


class Player:
    def __init__(self, name):
        self.name = name
        self.max_health = 100
        self.health = 100
        self.attack = 20
        self.coins = 50
        self.level = 1
        self.xp = 0
        self.xp_to_next = 50

    def is_alive(self):
        return self.health > 0

    def heal(self, amount):
        self.health = min(self.max_health, self.health + amount)

    def take_damage(self, amount):
        self.health = max(0, self.health - amount)

    def gain_xp(self, amount):
        self.xp += amount
        print(f"You gained {amount} XP.")
        while self.xp >= self.xp_to_next:
            self.xp -= self.xp_to_next
            self.level_up()

    def level_up(self):
        self.level += 1
        self.max_health += 20
        self.health = self.max_health  # full heal on level up
        self.attack += 5
        self.xp_to_next = int(self.xp_to_next * 1.4)
        print(f"*** LEVEL UP! You are now level {self.level}. "
              f"Max Health: {self.max_health}, Attack: {self.attack} ***")

    def show_stats(self):
        print("-" * 30)
        print(f"Player: {self.name}   Level: {self.level}")
        print(f"Health: {self.health}/{self.max_health}")
        print(f"Attack Power: {self.attack}")
        print(f"Coins: {self.coins}")
        print(f"XP: {self.xp}/{self.xp_to_next}")
        print("-" * 30)


class Enemy:
    def __init__(self, name, health, attack, coin_reward, xp_reward):
        self.name = name
        self.health = health
        self.attack = attack
        self.coin_reward = coin_reward
        self.xp_reward = xp_reward

    def is_alive(self):
        return self.health > 0


# ---------- Helpers ----------

def get_choice(prompt, minimum, maximum):
    while True:
        try:
            value = int(input(prompt))
            if minimum <= value <= maximum:
                return value
            print(f"Enter a number from {minimum} to {maximum}.")
        except ValueError:
            print("Please enter a valid number.")


def pick_event():
    return random.choices(EVENTS, weights=EVENT_WEIGHTS, k=1)[0]


def spawn_enemy(player_level):
    # Enemy pool scales with player level so the game gets harder over time
    max_index = min(len(ENEMY_TEMPLATES), 2 + player_level)
    name, hp, atk, coins, xp = random.choice(ENEMY_TEMPLATES[:max_index])
    # slight random variance so the same enemy isn't identical every time
    hp = int(hp * random.uniform(0.9, 1.2))
    atk = int(atk * random.uniform(0.9, 1.15))
    return Enemy(name, hp, atk, coins, xp)


# ---------- Encounter handlers ----------

def handle_enemy(player):
    enemy = spawn_enemy(player.level)
    print(f"\n👹 A {enemy.name} appears! (HP: {enemy.health}, ATK: {enemy.attack})")
    print("1. Attack   2. Run")
    move = get_choice("Enter your move: ", 1, 2)

    if move == 2:
        # Running has a small risk of a free hit, so it's not a free escape
        if random.random() < 0.4:
            dmg = enemy.attack // 2
            print(f"You got hit while fleeing! -{dmg} HP")
            player.take_damage(dmg)
        else:
            print("You got away safely.")
        return

    while enemy.is_alive() and player.is_alive():
        enemy.health -= player.attack
        print(f"You hit the {enemy.name} for {player.attack}. ({max(enemy.health, 0)} HP left)")

        if not enemy.is_alive():
            print(f"You defeated the {enemy.name}!")
            player.coins += enemy.coin_reward
            print(f"You received {enemy.coin_reward} coins.")
            player.gain_xp(enemy.xp_reward)
            break

        player.take_damage(enemy.attack)
        print(f"The {enemy.name} hits you for {enemy.attack}. (Your HP: {player.health})")

        if not player.is_alive():
            print(f"\nYou were killed by the {enemy.name}. GAME OVER!")


def handle_mysterious_box(player):
    print("You found a mysterious chest! You found a Holy Sword!")
    player.attack += 10  # flat, permanent — not a doubling exploit
    player.heal(15)


def handle_coin_chest(player):
    print("You found a coin chest!")
    player.coins += 30


def handle_nothing(player):
    print("You explore the room... nothing here.")


def handle_trap(player):
    print("It's a trap! Spikes shoot from the walls!")
    player.attack = max(5, player.attack - 5)
    player.take_damage(20)
    player.coins = max(0, player.coins - 20)
    if not player.is_alive():
        print("\nThe trap finished you off. GAME OVER!")


def handle_healing_spring(player):
    print("You find a glowing spring. It restores your health.")
    player.heal(30)


EVENT_HANDLERS = {
    "enemy": handle_enemy,
    "mysterious_box": handle_mysterious_box,
    "coin_chest": handle_coin_chest,
    "nothing": handle_nothing,
    "trap": handle_trap,
    "healing_spring": handle_healing_spring,
}


def shop(player):
    print("\n--- Shop ---")
    print(f"Coins: {player.coins}")
    print("1. Heal 30 HP - 20 coins")
    print("2. +5 Attack - 30 coins")
    print("3. Leave shop")
    choice = get_choice("Choose: ", 1, 3)

    if choice == 1:
        if player.coins >= 20:
            player.coins -= 20
            player.heal(30)
            print("You feel refreshed.")
        else:
            print("Not enough coins.")
    elif choice == 2:
        if player.coins >= 30:
            player.coins -= 30
            player.attack += 5
            print("Your weapon feels sharper.")
        else:
            print("Not enough coins.")


# ---------- Main game ----------

def main():
    name = input("Enter your name: ")
    player = Player(name)

    print(f"\nWelcome, {player.name}!")
    player.show_stats()

    game_running = True
    while game_running and player.is_alive():
        print('''
What do you want to do?
    1. Explore Dungeon
    2. Check Stats
    3. Visit Shop
    4. Quit Game
        ''')
        choice = get_choice("Enter your choice: ", 1, 4)

        if choice == 1:
            print("Exploring Dungeon!.....")
            event = pick_event()
            EVENT_HANDLERS[event](player)

            if not player.is_alive():
                game_running = False

        elif choice == 2:
            player.show_stats()

        elif choice == 3:
            shop(player)

        elif choice == 4:
            print("Thanks for playing!")
            game_running = False

    if not player.is_alive():
        print(f"\nFinal stats — Level {player.level}, Coins: {player.coins}")


if __name__ == "__main__":
    main()
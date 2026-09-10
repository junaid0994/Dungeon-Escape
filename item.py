import random
health = 100
name = input ("Enter your name: ")
attack = 20
coins = 50
game_running = True

Goblin_health = [100,50,20,40,60,45,67,90,150]
Goblin_attack_power = [20,10,15,17,30]

G = random.choice(Goblin_health)

move = int(input ("enter your move: "))
while game_running:

        G_attack = random.choice(Goblin_attack_power)

        while G != 0:
                if move == 1 and health < G :
                        print("Goblin is too powerful and He Killed you....... GAME OVER!")
                        game_running = False
                if move == 1 and health > G:
                        print(f'''Goblin'S Health: {G}
                        Attacking Goblin.....''')
                        G -= attack
                        print(f"Goblin's Health: {G}")
                        if G <= 0:
                                print("YOu killed GOblin...")
                                G = 0
                                
                        elif G != 0:
                                print("Goblin IS Attacking.......")
                                health -= G_attack
                                print(f"YOur Health: {health}")
                                if health <= 0 :
                                        print("You Got Killed By Goblin....GAME OVER")
                                        game_running = False
                        
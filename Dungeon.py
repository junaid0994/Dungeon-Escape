import random
health = 100
name = input ("Enter your name: ")
attack = 20
coins = 50
game_running = True
item = ["Goblin","Mysterious Box","coin chest","Nothing","Trap"]
Goblin_health = [100,50,20,40,60,45,67,90,150]
Goblin_attack_power = [20,10,15,17,30]
def get_choice(prompt, minimum, maximum):
    while True:
        try:
            value = int(input(prompt))
            if minimum <= value <= maximum:
                return value
            print(f"Enter a number from {minimum} to {maximum}.")
        except ValueError:
            print("Please enter a valid number.")



print(f"Player: {name}")
print(f"Health: {health}")
print(f"Attack Power: {attack}")
print(f"Coins: {coins}")
while game_running:
    
    M = random.choice(item)
   
    goblin_health = random.choice(Goblin_health)
    goblin_attack_power = random.choice(Goblin_attack_power)
    
    
    
    print(''' What do you want to do?
                1. Explore Dungeon
                2. Check Stats
                3. Quit Game
        ''')
    choice = get_choice("Enter your choice: ", 1, 3)

    if (choice == 1):
        print(" Exploring Dungeon!..... ")
      
        if( M == "Mysterious Box"):
            print('''You enter a room...
                You found a mysterious chest! 🧰
                YOu Found a Holy Sword!.''')
            attack *= 2
            health += 15
            
        elif( M == "coin chest"):
            
            print('''You enter a room...
                    You Found a Coin chest''')
            coins += 30
            
        elif( M == "Goblin"):
            print(f'''You enter a room...
            👹 A Goblin appears!
            Current Health: {health}
            Goblin's Health: {goblin_health}
            What Do You Want to Do?
            1.Attack Goblin
            2.Run''')
            move = get_choice("Enter your move: ", 1, 2)

            if move == 2:
                print("You got away safely.")

            else:
                while goblin_health > 0 and health > 0:
                    print(f"Goblin's Health: {goblin_health}")
                    print("Attacking goblin...")

                    goblin_health -= attack

                    if goblin_health <= 0:
                        print("You killed the goblin!")
                        coins += 20
                        print("You received 20 coins.")
                        break

                    print("The goblin is attacking...")
                    health -= goblin_attack_power
                    print(f"Your Health: {health}")

                    if health <= 0:
                        print("You were killed by the goblin. GAME OVER!")
                        game_running = False
                
        elif(M == "Nothing"):
            print('''You enter a room...
                  Nothing seems to be here...''')
        elif M == "Trap":
            print('''You Entered A Room...
                     There Is a Trap''')
            attack -= 10
            health -= 20
            coins -= 20     
            
    elif(choice == 2):
        print(" checking stats!......... ")
                
        print(f"Player: {name}")
        print(f"Health: {health}")
        print(f"Attack Power: {attack}")
        print(f"Coins: {coins}")
                
            
    elif (choice == 3):
        print(" Quit Game! ")
        game_running = False
        
    else:
        print("Invalid Choice")
             

import random
health = 100
name = input ("Enter your name: ")
attack = 20
coins = 50
game_running = True
item = ["Goblin","Mysterious Box","coin chest","Nothing"]
Goblin_health = [100,50,20,40,60,45,67,90,150]
Goblin_attack_power = [20,10,15,17,30]



print(f"Player: {name}")
print(f"Health: {health}")
print(f"Attack Power: {attack}")
print(f"Coins: {coins}")
while game_running:
    
    M = random.choice(item)
    G = random.choice(Goblin_health)
    G_attack = random.choice(Goblin_attack_power)
    
    
    
    print(''' What do you want to do?
                1. Explore Dungeon
                2. Check Stats
                3. Quit Game
        ''')
    choice = int(input ("Enter your choice: "))

    if (choice == 1):
        print(" Exploring Dungeon!..... ")
      
        if( M == "Mysterious Box"):
            print('''You enter a room...
                You found a mysterious chest! 🧰''')
            attack += 5
            health += 15
            coins += 5
        elif( M == "coin chest"):
            
            print('''You enter a room...
                    You Found a Coin chest''')
            coins += 30
            
        elif( M == "Goblin"):
            print(f'''You enter a room...
            👹 A Goblin appears!
            Current Health: {health}
            What Do You Want to Do?
            1.Attack Goblin
            2.Run''')
            move = int(input("Enter your Move: "))
            print(move)
            
            
            if move == 2:
                print("You Got Away, You Are Safe Now")
            
            elif move == 1:
                    
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
                                   
            
        else:
            print('''You enter a room...
                  Nothing seems to be here...''')
            
            
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
             

import random #a module (file of prewritten code)


room = 1
#function definition
def monster(biome):
    num = random.randrange(0,100) # function call
    if biome == "Bedroom":
        if num < 20: # 20% percent chance 
            print("A zombie breaks out of the closet is running to attack you")
        elif num < 50: # 30% percent chance
            print("A skeleton crawls under the bed and tries to grab you")
        elif num < 90: # 40% percent chance
            print("An ogre is slamming on your window")
        else: #10 percent chance
            print("You see a giant spider outside your window")
    elif biome == "Hallway":
        if num < 20: # 20% percent chance 
            print("A zombie is breaking into your window on the left")
        elif num < 50: # 30% percent chance
            print("A skeleton is aiming an arrow at you from the attic")
        elif num < 90: # 40% percent chance
            print("A giant spider bites you on your way out!")
        else: #10 percent chance
            print("A witch throws a potion at you from across the hallway and disappears")
    elif biome == "TopStair":
        if num < 25: # 25% percent chance 
            print("A zombie comes up from the floorboard trying to grab at you")
        elif num < 75: # 50% percent chance
            print("A witch comes out the bathroom and is heading towards you direction")
        elif num < 90: # 15% percent chance
            print("Spiders start flooding the hallway!")
        else: #10 percent chance
            print("Acid slime creature is oozing from the walls behind you")
    
     
# Moving around (Map)
while True:
    if room == 1:
        print()
        monster("Bedroom") #function call
        print("Your only direction you can go is (e)ast ")
        choice = input()
        if choice == 'e' or choice == 'E' or choice == 'east':
            room = 2
        else:
            print("Sorry that isn't a direction you can go.")
    if room == 2:
        print()
        monster("Hallway") #function call
        print("You are in the hallway, you can go (w)est to go back to your room or (s)outh ")
        choice = input()
        if choice == 's' or choice == 'S' or choice == 'South':
            room = 3
        elif choice == 'w' or choice == 'W' or choice == 'West':
            room = 1
        else:
            print("Sorry that isn't a direction you can go.")
    
    if room == 3:
        print()
        print("You are in the middle of the hallway. You can go (n)orth or (s)outh ")
        choice = input()
        if choice == 's' or choice == 'S' or choice == 'South':
            room = 4
        elif choice == 'n' or choice == 'N' or choice == 'North':
            room = 2
        else:
            print("Sorry that isn't a direction you can go.")
            
    if room == 4:
        print()
        monster("TopStair") #function call
        print("You are at the end of the hallway at the top of the stairway.")
        choice = input()
        if choice == 'n' or choice == 'N' or choice == 'North':
            room = 3
        elif choice == 'placeholder':
            room = 10
        else:
            print("Sorry that isn't a direction you can go.")

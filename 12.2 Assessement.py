#Inventory
inventory = {
    'health potions': 0,
    'mana potions': 0,
    'fire arrows': 0,
    'silver dabloons': 2,
}
#Function for the shop 
def shop():
    gdab = 150 #Money
    shopstart = True 
    while shopstart == True: #While loop for the shop to keep printing
        print("------------------------------------------------------")
        print("Welcome to the shop, you have", gdab, "gold dabloons")
        print()
        print("Your inventory:", inventory)
        print()
        print("Shop Items: Health pot[$5],   Mana pot[$3],   Fire arrow[$4],   10 silver dabloons[$1]")
        print()
        #Userinput so the player can actually input letters to buy items
        userinput = input("Enter [P] for health pot\nEnter [M] for mana pot\nEnter [F] for fire arrow\nEnter [S] for 10 silver dabloons\n\nEnter [Q] to exit the shop\n")
        if userinput == "P" or userinput == "p":
            gdab = gdab - 5
            inventory["health potions"] += 1
            print("Now you have", inventory["health potions"], "health potions")
        elif userinput == "M" or userinput == "m":
            gdab = gdab - 3
            inventory["mana potions"] += 1
            print("Now you have", inventory["mana potions"], "mana potions")
        elif userinput == "F" or userinput == "f":
            gdab = gdab - 4
            inventory["fire arrows"] += 1
            print("Now you have", inventory["fire arrows"], "fire arrows")
        elif userinput == "S" or userinput == "s":
            gdab = gdab - 1
            inventory["silver dabloons"] += 1
            print("Now you have", inventory["silver dabloons"], "silver dabloons")
        elif userinput == "Q" or userinput == 'q':
            print("Goodbye, please visit Tam's best adventure shop again soon. We have a buy one, get one free deal in a couples. ")
            shopstart = False
            
shop() #call functions
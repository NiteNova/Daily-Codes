import random

inventory = ['empty', 'empty', 'empty', 'empty',]
print (inventory)


def ranslot():
    num = random.randrange(0, 100)
    if num < 25:
        inventory[random.randrange(0,4)] = "Book"
    elif num < 40:
        inventory[random.randrange(0,4)] = "Frog"
    elif num < 80:
        inventory[random.randrange(0,4)] = "Potion"
    else:
        inventory[random.randrange(0,4)] = "Cupcake"
    
i = 0
while i != 4:
    ranslot()
    print (inventory)
    i += 1
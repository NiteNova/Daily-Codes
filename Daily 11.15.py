import random

adj = ["Stinky", "lil", "cold", "witty", "silly", "clownish", "funny", "ridiculous", "ludicrous", "smart"]
noun = ["Cat", "Dog", "Bird", "Chicken", "Spider", "Sheep", "Shark", "Giraffe", "T-Rex", "Ladybug",]

print("Stage name Generator")

GenOff = False

while GenOff == False:
    user = input("Input any key to continue and q to quit:\n")
    if user == "q" or user == "Q":
        print("Goodbye")
        GenOff = True
    else:
        print(adj[random.randrange(0,10)], noun[random.randrange(0,10)])
        print()
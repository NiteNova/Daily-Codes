import random


#--------------------Start of Function---------------------
def NpcGen(dialogue):
    num = random.randrange(0,100) # function call
    if dialogue == "Npc":
        if num < 20: # 20% percent chance
            print("Hey I like shorts")
        elif num < 30: # 10% percent chance
            print("DO A BARREL ROLL!")
        elif num < 45: # 15% percent chance
            print("Science isn't about why, it's about why not!")
        elif num < 80: # 35% percent chance
            print("What is a man? A miserable little pile of secrets.")
        else: # 20% percent chance
            print("I used to be an adventurer like you. Then I took an arrow in the knee")
#--------------------End of Function-----------------------

#NpcGen("Npc")

#------------------For loop that runs 5 times--------------
for A in range (5):
    print(end = NpcGen("Npc"))
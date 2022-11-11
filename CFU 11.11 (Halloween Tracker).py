import random

#0=Butterfinger
#1=Hershey's
#2=Peanutbutter cups
#3=M&Ms
#4=Sour Patch Kids
#5=Rocks

Cand = [0, 0, 0, 0, 0, 0]


def ca_rand():
    chance = random.randrange(0,100)
    if chance < 15: # butterfingers
        Cand[0] += random.randrange(1, 4)
    if chance < 35: # hershey's
        Cand[1] += random.randrange(1, 4)
    if chance < 70: # peanutbutter cups
        Cand[2] += random.randrange(1, 4)
    if chance < 80: # M&Ms
        Cand[3] += random.randrange(1, 4)
    if chance < 98:#
        Cand[4] += random.randrange(1, 4)    
    else:
        Cand[5] = 1


i = 0
while i != 6:
    ca_rand()
    i += 1

print("You have", Cand[0],"Butterfingers")
print("You have", Cand[1],"Hershey's")
print("You have", Cand[2],"Peanutbutter Cups")
print("You have", Cand[3],"M&Ms")
print("You have", Cand[4],"Sour Patch Kids")
print("You have", Cand[5], "rock(s)")
print()
print("Final candy count for each kind:", Cand)

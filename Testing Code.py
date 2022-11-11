import random

list = []
loop = int(input("How much series of numbers do you want to add: "))
for h in range(loop):
    num = random.randrange(0, 100)
    list.append(num)
    print (list)
    
def bubble():
    for i in range(len(list)):
        for j in range(len(list)):
            if i < j
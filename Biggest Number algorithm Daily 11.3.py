bruh = []
loop = int(input("How much series of numbers do you want to add: "))
for k in range(loop):
    user = int(input("Enter your number: "))
    bruh.append(user)


def wah(bruh =[]):
    j = bruh[0]
    for i in range(len(bruh)):
        if j < bruh[i]:
            j = bruh[i]
    return j

print (wah(bruh))

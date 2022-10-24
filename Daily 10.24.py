friends = ('Alex', 'Lalo', 'Seth', 'Kevin', 'Jacob')
print("The friend names are", friends)

f1 = int(input("Age of friend 1: "))
f2 = int(input("Age of friend 2: "))
f3 = int(input("Age of friend 3: "))
f4 = int(input("Age of friend 4: "))
f5 = int(input("Age of friend 5: "))

ages = [f1, f2, f3, f4, f5]

print()
print("Friend ages: ")
print("Alex:", ages[0])
print("Lalo:", ages[1])
print("Seth:", ages[2])
print("Kevin:", ages[3])
print("Jacob:", ages[4])
print()

avg = sum(ages)/len(ages)
print("The average age is:", (avg))
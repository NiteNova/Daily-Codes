
print ("You hear a faint girl's voice calling to you saying, 'You need to wake up. The kingdom is under attack, please we need you!' Then suddenly you wake up in your bedroom and with sense of exhaustion and confusion as to what the dream meant. ")
print ()
user = input("(Type A to continue): ")
if user == 'A' or user == 'a':
    print("You are finally able to get up from your bed and look around your room to find yourself in the early dawn of the day. You're put back into realization of reality. You can smell the delicious smell of breakfast from the kitchen downstairs.")
    room = 1

while True:
    if room == 1:
        print()
        print("Your only direction you can go is (e)ast ")
        choice = input()
        if choice == 'e' or choice == 'E' or choice == 'east':
            room = 2
        else:
            print("Sorry that isn't a direction you can go.")
    if room == 2:
        print("You are in the hallway, you can go (w)est to go back to your room or (s)outh ")
        choice = input()
        if choice == 's' or choice == 'S' or choice == 'south':
            room = 3
        if choice == 'w' or choice == 'W' or choice == 'west':
            room = 1
        else:
            print("Sorry that isn't a direction you can go.")
    if room == 3:
        print("You are in the middle of the hallway. There you recognize old family photos and in a single flash you imagine a girl in one of the albums, but you double check it again but found nothing had changed. You can go (n)orth or (s)outh ")
        choice = input()
        if choice == 's' or choice == 'S' or choice == 'south':
            room = 4
        if choice == 'n' or choice == 'N' or choice == 'North':
            room = 2
        else:
            print("Sorry that isn't a direction you can go.")
    if room == 4:
        print("You are at the end of the hallway at the top of the stairway. The stairway gives an eerie feeling as you stare downwards. You can go (n)orth to go back to the middle of the hallway.")
        if choice == 'n' or choice == 'N' or choice == 'North':
            room = 3
        else:
            print("Sorry that isn't a direction you can go.")

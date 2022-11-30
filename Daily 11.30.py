#--------------Boss Battle system function#----------------
def boss_battle(health):
    bosshealth = 50
    while health >0 and bosshealth >0:
        #You attack the monster
        damage = random.randrange(10, 21)
        print("You hit the monster for", damage, "HP.")
        bosshealth -= damage
        print("The boss' health is now", bosshealth)
        #the monster attacks you
        damage = random.randrange(5, 16)
        print("The monster bites you for", damage, "HP.")
        health -= damage
        print("Your health is now", health)

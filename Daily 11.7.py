#Class Car
class plane:
    #constructor function
    def __init__(self, type):
        self.type = type
        self.speed = 0
        self.in_air = False
        self.fuel = 5000
        self.isWorking = True
    
    def printPlane(self):
        print("Hi I'm a", self.type, "and my speed is", self.speed, "In the air:", self.in_air)
        print()
    
    def fly(self, speedinc):
        print("Nroom! Nroom!")
        self.speed += speedinc
        self.in_air = True
        
    def land(self):
        print("Pshhh! Pshhh!")
        self.speed = 0
        self.in_air = False
        
    def fly_one_hour(self):
        self.fuel -= 1000
        print("Warning fuel decreased to", self.fuel)
#---------------------------------        
#create (instantiate) a car

Boeing = plane("Boeing 777")
Airbus = plane("Airbus")
Comac = plane("Comac C919")
Boeing.printPlane()
#Airbus.printPlane()
#Comac.printPlane()

Boeing.fly(400)
Boeing.printPlane()
Boeing.land()
Boeing.printPlane()
Boeing.fly_one_hour()



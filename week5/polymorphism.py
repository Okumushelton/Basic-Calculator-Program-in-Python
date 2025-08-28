class Car:
    def move(self):
        print(f"{self.__class__.__name__} - Driving.")

class Plane:
    def move(self):
        print(f"{self.__class__.__name__} - Flying.")

class Ship:
    def move(self):
        print(f"{self.__class__.__name__} - Sailing.")

vehicles = [Car(), Plane(), Ship()]

for v in vehicles:
    v.move() # Each class executes its own version of move()

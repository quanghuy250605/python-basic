print(len("Hello"))           
print(len((1, 2, 3)))   
print(len({"brand": "Ford"})) 


#Polymorphism
class Car:
    def move(self):
        print("motor")

class Boat:
    def move(self):
        print("ship")

class Plane:
    def move(self):
        print("fly")

vehicles = [Car(), Boat(), Plane()]

for vehicle in vehicles:
    vehicle.move()

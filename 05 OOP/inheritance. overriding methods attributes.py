

class Vehicle:
    def __init__(self, brand, name):
        self.brand = brand
        self.name = name
        self.topSpeed = 10
        self.numWheels = 4

    def printVehicleInfo(self):
        print("Vehicle info: ", self.brand, self.name, self.topSpeed, self.numWheels)

    def printNumWheels(self):
        print("VehicleNumWheels: ", self.numWheels)


vehicle1 = Vehicle("Vehicle", "Basic")
vehicle1.printVehicleInfo()

class Car(Vehicle):
    def printCarInfo(self):
        self.topSpeed = 230
        print("printCarInfo", self.brand, self.name, self.topSpeed, self.numWheels)

    def printVehicleInfo(self):
        print("Car.printVehicle info: ", self.brand, self.name, self.topSpeed, self.numWheels)    


car1 = Car("Ford", "Mustang")
car1.printCarInfo()
car1.printVehicleInfo()
car1.printNumWheels()

class SuperCar(Car):
    def reachSpeed300(self):
        self.topSpeed = 301
        print("Super car reach 300!")

superCar1 = SuperCar("Ford", "GT")
superCar1.reachSpeed300()
superCar1.printVehicleInfo()
superCar1.printNumWheels()

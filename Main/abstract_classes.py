from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass
    

class Car(Vehicle):

    def go(self):
        print("This car is riding")

    def stop(self):
        print("This car is stopped")


class Motorcycle(Vehicle):

    def go(self):
        print("This motorcycle is riding")

    def stop(self):
        print("This motorcycle is stopped")


# vehicle = Vehicle()

car = Car()
car.go()
car.stop()

cycle = Motorcycle()
cycle.go()
cycle.stop()

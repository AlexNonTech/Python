import time


class Bike:
    def __init__(self, meters):
        self.meters = meters
        self.distance = None

    def ride(self):
        print("Starting our trip...")
        time.sleep(1)
        self.distance = self.meters - self.meters
        for i in range(5):
            print(f"We ride about {self.distance} meters")
            self.distance += self.meters
            time.sleep(1)
        self.distance -= self.meters

    def display(self):
        print(f"Overall distance of our trip is {self.distance} meters")


# trip = Bike(100)
# trip.ride()
# trip.display()


class Math:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def sum(self):
        return self.a + self.b

    def divide(self):
        return self.a / self.b

    def multiply(self):
        return self.a * self.b

    def subtract(self):
        return self.a - self.b


example = Math(20, 2)
sum = example.sum()
sub = example.subtract()
div = example.divide()
multi = example.multiply()

print(sum, sub, div, multi)

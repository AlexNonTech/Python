class Animal:
    isAlive = True

    def eat(self):
        print("This animal is eating")

    def sleep(self):
        print("This animal is sleeping")


class Rabbit(Animal):

    def jumps(self):
        print("This rabbit is jumps")


class Bear(Animal):
    def roars(self):
        print("This bear is roars")


someAnimal = Animal()
print(someAnimal.isAlive)
someAnimal.eat()

rabbit = Rabbit()
print(rabbit.isAlive)
rabbit.jumps()

bear = Bear()
print(bear.isAlive)
bear.roars()

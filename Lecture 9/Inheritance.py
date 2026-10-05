# class Car:
#     ...

# class ToyotaCar(Car):
#     ...

#       #Single Inheitance -> When a class inherits from only one class, it is called single inheritance.

class Car:
    Color = "black"
    @staticmethod
    def start():
        print("car started..")

    @staticmethod
    def stop():
        print("car stopped..")

class ToyotaCar(Car):
    def __init__(self, name):
        self.name = name

car1 = ToyotaCar("fortuner")
car2 = ToyotaCar("prius")

print(car1.name)
print(car1.start())

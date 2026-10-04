#  Static methods dont use self parameter, they work at the class level

class Student:
    @staticmethod   # decorator
    def college():
        print("ABC College")



#   Notes

#  Abstraction  and  Encapsulation

#  Abstraction -> Hiding the implementation details of a class and only showing the essential features to the user.

class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clucth = False

    def start(self):
        self.clucth = True
        self.acc = True
        print("car started..")

car1 = Car()
car1.start()





#   Encapsulation -> Wrapping data and functions into a single unit(object).
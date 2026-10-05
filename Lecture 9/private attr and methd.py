#  This is a wrong thing this will become public and it is not private

# class Account:
#     def __init__(self, acc_no, acc_pass):
#         self.acc_no = acc_no
#         self.acc_pass = acc_pass


# acc1 = Account("12345", "abcde")

# print(acc1.acc_no)
# print(acc1.acc_pass)                     # This is wrong because this is a public method and it can be accessed outside the class. So, we have to make it private by using double underscore before the variable name.



class Account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass     # Private method

    def reset_pass(self):
        print(self.__acc_pass)       # This is inside the class so it is private method and it can be accessed here


acc1 = Account("12345", "abcde")

print(acc1.acc_no)
print(acc1.reset_pass())



#   02   Another class

class Person:
    __name = "anonymous"

    def __hello(self, name):
        print("hello person!")

    def welcome(self):
        self.__hello()


p1 = Person()

print(p1.__name)
print(p1.__hello())
print(p1.welcome())
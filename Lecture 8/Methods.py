# Creating class

class Student:
    def __init__(self, fullname):
        self.name = fullname

    def hello(self):
        print("hello", self.name)


#  creating object

s1 = Student("karan")
s1.hello()



#  For Example

 
class Student:                                   # create Class
    college_name ="ABC College"         # Class Attribute

    def __init__(self, name, marks):
        self.name = name               # Object Attribute
        self.marks = marks

    def welcome(self):
        print("welcome student,", self.name)

    def get_marks(self):
        return self.marks


s1 = Student("karan", 97)                         # create Objects
s1.welcome()
print(s1.get_marks())
#  Class and Instance Attributes
#   1. Class.attr
#   2. obj.attr



class Student:
    college_name ="ABC College"

    def __init__(self, name, marks):
        self.name = name         
        self.marks = marks
        print("adding new student in Database..")

s1 = Student("karan")
print(s1.name, s1.marks)

s2 = Student("arjun")
print(s2.name, s2.marks)

print(s2.college_name)      # OR
print(Student.college_name)





#  Another Example


class Student:
    college_name ="ABC College"
    name = "anonymous"            # class attr

    def __init__(self, name, marks):
        self.name = name            # obj  attr > class attr
        self.marks = marks
        print("adding new student in Database..")

s1 = Student("karan", 97)
print(s1.name)
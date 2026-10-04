#   __init__ function
# creating class

class Student:
    def __init__(self, fullname):
        self.name = fullname



# creating object

s1 = Student("Karan")
print(s1.name)




#  Another Example

class Student:
    name = "Karan"
    def __init__(self):
        print(self)
        print("adding new student in Database..")

s1 = Student()
print(s1)



#   Another with a fullname

class Student:

    def __init__(self, fullname):
        self.name = fullname
        print("adding new student in Database..")

s1 = Student("karan")
print(s1.name)   #Karan

s2 = Student("arjun")
print(s2.name)   #arjun




#  



class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        print("adding new student in Database..")


s1 = Student("karan", 97)
print(s1.name, s1.marks)   #Karan 97

s2 = Student("arjun", 88)
print(s2.name, s2.marks)   #arjun 88



# Another Version

class Student:

    # Default Constructors
    def __init__(self):
        pass

    # parameterized constructors
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        print("adding new student in Database..")



s1 = Student("karan", 97)
print(s1.name, s1.marks)   #Kara

s2 = Student("arjun", 88)
print(s2.name, s2.marks) 
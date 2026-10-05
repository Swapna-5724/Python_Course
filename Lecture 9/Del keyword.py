#  Del Keyword
    # del s1.name
    # del s1


class Student:
    def __init__(self, name):
        self.name = name

s1 = Student("shradha")
print(s1)
del s1
print(s1)

# 02

s1 = Student("shradha")
print(s1.name)
del s1.name
print(s1.name)
class Person:
    name = "anonymous"

    def changenName(self, name):
        self.name = name

p1 = Person()
p1.changeName("rahul kumar")
print(p1.name)
print(Person.name)


#   Change self to Person

class Person:
    name = "anonymous"

    def changenName(self, name):
        Person.name = name

p1 = Person()
p1.changeName("rahul kumar")
print(p1.name)
print(Person.name)


#   Another type

class Person:
    name = "anonymous"

    # def changenName(self, name):
    #     self.__class__.name = "Rahul"
    #    #self.__class__. Person.

    @classmethod
    def changeName(cls, name):
        cls.name = name


p1 = Person()
p1.changeName("rahul kumar")
print(p1.name)
print(Person.name)









#   Notes
#  Different Methods

#  1. static Method
#  2. Class Method
#  3. Instance Method
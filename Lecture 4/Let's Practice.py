#   Question = 01

#  Store following word meanings in a python dictionary: 
# table: "a piece of furniture", "list of facts and figures"
#  cat: "a small animal"

dictionary = {
    "cat" : "a small animal",
    "table" : ["a piece of furniture", "list of facts & figures"]
}

print(dictionary)




#    Question  =  02

#  You are given a list of subjects for students. Assume one classroom is required for 1 subject. How many classrooms are needed by all students.
#   "python", "java", "C++", "python", "javascript"
#    "java", "python", "java", "C++", "C"

subjects = {
    "python", "java", "c++", "python", "javascript", "java",
    "python", "java", "c++", "c"
}

print(subjects)
print(len(subjects))




#   Question  =  03

#   Write a Program to enter marks of 3 subjects from the user and store them in a dictionary. 
# Start with an empty dictionary and add one by one. Use Subject name as key and marks as value.

marks = {}

x = int(input("enter phy : "))
marks.update({"phy" : x})

x = int(input("enter math : "))
marks.update({"math" : x})

x = int(input("enter chem : "))
marks.update({"chem" : x})

print(marks)





#   Question  =  04

#  Figure out a way to store 9 & 9.0 as separate values in the set.
#  (You can take help of built-in data types)


# values = {9, 9.0}
# values = {9, 9.25}
# values = {9, 9.25, 8, 8.0}
# values = {9, "9.0"}
values = {"9", 9.0}
print(values)


#   2nd Possible solution

values = {
    ("float", 9.0),
    ("int", 9)
}
print(values)

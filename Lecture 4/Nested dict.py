student = {
    "name" : "rahul kumar",
    "subjects" : {
        "phy" : 97,
        "chem" : 98,
        "math" : 95
    }
}

# nested dictionary

# Dictionary Methods
#   01  ->  myDict.keys()  = Returns all keys

print(student["subjects"]["chem"])

print(student.keys())

# float(9)

print(list(student.keys()))

print(len(student))
print(list(student.keys()))

#   20 and 21st line in one line

print(len(list(student.keys())))



#    02  ->  myDict.values()   =>  returns all values


print(student.values())

print(list(student.values()))



#    03  ->   myDict.items    =>   returns all (key, val) pairs as tuples


print(student.items())

print(list(student.items()))


#  Individually access

pairs = list(student.items())
print(pairs[0])  # or
print(pairs[1])



#    04  ->  myDict.get("key")  =>   returns the key according to value


print(student["name2"])      #error
print(student.get("name2"))    # no error -> None


print("hi")
print("welcome to")
print("apnacollege")
print("we are learning")
print("coding")


print("BEFORE")
print(student["name2"])  #error
print("AFTER")


#    05   ->  myDict.update(newDict)    =>    inserts thespecified items to the dictionary

student.update({"city" : "delhi"})

print(student)

#   or

new_dict = {"city" : "delhi"}
student.update(new_dict)

print(student)
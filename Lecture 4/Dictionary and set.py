info = {
    "key" : "value",
    "name" : "apnacollege",
    "learning" : "coding"
}

print(info)


#  02

info = {
    "name" : "apnacollege",
    "subjects" : ["c", "python", "C", "Java"],
    "topics" : (),
    "age" : 35,
    "is_adult" : True,
    "marks" : 94.4
    # 12.99 : 94.4
    }

print(info)

print(type(info))

print(info["name"])
print(info["topics"])
print(info["subjects"])
print(info["age"])


print(info["surname"])   # It will come error
pass

#   To change 'name'

info["name"] = "shradha"  #Overwrite
info["surname"] = "khapra"
print(info)


#  Null Dictoionary

null_dict = {}
print(null_dict)


null_dict = {}
null_dict["name"] = "apnacollege"
print(null_dict)
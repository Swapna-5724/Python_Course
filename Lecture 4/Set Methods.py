# 1.  set.add(el) # 1. adds an element

collection = set()
collection.add(1)
collection.add(2)
collection.add(2)
collection.add("apnacollege")
collection.add((1,2,3))
collection.add([1,2,3])   # TypeError  -> Unhashable  [dict, lists, set]


# 2. set.remove(el) #removes the elem an

# collection.remove(7)   # error
collection.remove(1)
print(collection)

# 3. set.clear() #empires the set

collection = set()
collection.add(1)
collection.add(2)
collection.add(2)
collection.add("apnacollege")
collection.add((1,2,3))
collection.add([1,2,3]) 

collection.clear()

print(len(collection))

# 4. set.pop() #removes a random value


collection = {"hello", "apnacollege", "World", "coding", "python"}

print(collection.pop())
print(collection.pop())





#   Two other important Methods

# set.union(set 2)   #  combines both set values and returns new

set1= {1, 2, 3}
set2 = {2, 3, 4}

print(set1.union(set2))  #{1, 2, 3, 4}
print(set1)
print(set2)


# set.intersection(set 2)    # combines common values and returnns new

print(set.intersection(set2))  # {2, 3}
# open("demo.text")

f = open("demo.txt", "r")   #  rt, rb wb, ab
data = f.read()
print(data)
print(type(data))
f.close()



#   02

f = open("demo.txt", "r+")
f.write("abc")                      #  Overwrite
f.close()



#   03

f = open("demo.txt", "w+")
f.write("abc")
print(f.read())
f.close()


#  04


f = open("demo.txt", "a+")
# f.write("abc")
print(f.read())
f.write("abc")
f.close()
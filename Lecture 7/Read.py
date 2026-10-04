f = open("demo.txt", "r")

data = f.read(5)                 # pass the parameter
print(data)

f.close()


#   02

f = open("demo.txt", "r")

line1 = f.readline()
print(line1)

f.close()



#   03


f = open("demo.txt", "r")

data = f.read()
print(data)

line1 = f.readline()
print(line1)

line2 = f.readline()
print(line2)

f.close()












# Notes

# data = f.read()      #  reads entire file

#  data = f.readline()     #reads one line at a time



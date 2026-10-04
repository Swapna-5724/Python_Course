#   Question ->  01

# Create a new file "Practice.txt" using pyhton. Add the following data in it:

            # Hi everyone
            # we are learning File I/O
            # Using Java.
            # I like programming in Java.


with open("practice.txt", "w") as f:
    f.write("Hi everyone\nwe are learning File I/O\n")
    f.write("using Java.\nI like programming in java.")











#    Question ->  02
#   WAF that replace all occurences of "java" with "python" in above file.


with open("practice.txt", "r") as f:
    data = f.read()

# data.replace("Java", "Python")
# print(data)


new_data = data.replace("Java", "Python")
print(new_data)


with open("practice.txt", "w") as f:
    f.write(new_data)






#   Question ->  03
# Search is the word "learning" exists in the file or not.


# word = "xlearning"                      #  Error  ->  Not Found 
with open("practice.txt", "r") as f:
    data = f.read()
    # word = "learning"
    if(data.find(word) != -1):
        print("Found")
    else:
        print("not found")





#   02


def check_for_word():
    word = "xlearning"
    with open("practice.txt", "r") as f:
        data = f.read()
        # word = "learning"
        if(data.find(word) != -1):
            print("Found")
        else:
            print("not found")

check_for_word()





#  Question  ->  04

#  WAF to find in which line of the file does the word "learning" occur first.
#  Print -1 if word not found


def check_for_word():
    word = "xlearning"
    with open("practice.txt", "r") as f:
        data = f.read()
        # word = "learning"
        # if(data.find(word) != -1):
        if(word in data):
            print("Found")
        else:
            print("not found")

def check_for_line():
    # word = "learning"
    word = "programming"
    data = True
    line_no = 1
    with open("practice.txt", "r") as f:
        while data:
            data = f.readline()
            # if(data.find(word))
            if(word in data):
                print(line_no)
                return
            line_no += 1

    return -1

print(check_for_line())








#   Question  ->  05

# From a file containing numbers separated by comma, print the count of even numbers. 

            #  1, 2, 45, 55, 86, 76  -> Data separated by comma.
            #  1. Individual Number
            #  2. 


with open("practice.txt", "r") as f:
    data = f.read()
    print(data)

    num = ""
    for i in range(len(data)):
        if(data[i] == ","):
            # print(num)
            print(int(num))
            num = ""
        else:
            num += data[i]




#   02

count = 0
with open("practice.txt", "r") as f:
    data = f.read()
    print(data)

    nums = data.split(",")
    # print(nums)
    for val in nums:
        if(int(val) % 2 == 0):
            count += 1

print(count)

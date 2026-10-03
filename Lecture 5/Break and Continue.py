#   Break:

i = 1
while i <= 5:
    print(i)
    i += 1

print("end of loop")


#   02  -> checcking the break function

i = 1
while i <= 5:
    print(i)
    if(i== 3):
        break
    i += 1

print("end of loop")




#    02

nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 36)

x = 36

i = 0
while i < len(nums):
    if(nums[i] == x):
        print("FOUND at idx", i)
        break
    else:
        print("finding..")
        i += 1

print("end of loop")





#   Continue:


i = 0
while i <= 5:
    print(i)
    if(i == 3):
        i += 1
        continue      #skip
    print(i)
    i += 1


#   2nd


i = 1
while i <= 10:
    # if(i%2 == 0):      # Even Numbers
    if(i%2 != 0):        # Odd Numbers
        i += 1
        continue      #skip
    print(i)
    i += 1


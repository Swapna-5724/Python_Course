#   Question =   01
#   Print numbers fromt 1 to 100

i = 1
while i <= 100:
    print(i)
    i += 1




#   Question =   02
#   Print numbers from 100 to 1

i = 100
while i >= 1:   #stopping condition
    print(i)
    i -= 1




#   Question =   03
#   Print the multiplication table of a number n.

                    # i = 1
                    # while i <= 10:
                    #     print(3*i)
                    #     i += 1


n = int(input("enter number : "))
i = 1
while i <= 10:
    print(n*i)
    i += 1






#   Question =   04
#   Print the elements of the following list using a loop:
#      [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


                    # nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
                    # len(nums) -> 10, 9

                    # print(nums[0])
                    # print(nums[1])
                    # print(nums[2])
                    # print(nums[3])  #...  print(nums[len(nums)-1])


nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

idx = 0
while idx < len(nums):
    # print(idx)
    print(nums[idx])         #nums[0], nums[1], num[2]...
    idx += 1



#   02  -> another Example

heroes = ["ironman", "thor", "superman", "batman"]

# traverse   -> It Travel to the next index of every element
i = 0
while i < len(heroes):
    print(heroes[i])
    i += 1




#   Question =   05
#   Search for a number X in this tuple using loop
#       [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)


i = 0
while i < len(nums):
    print(nums[i])
    i += 1 


#   02   ->  using only if Condition

x = 36

i = 0
while i < len(nums):
    if(nums[i] == x):
        print("FOUND at idx", i)
    i += 1




#    03   ->   using if else Condition



x = 36

i = 0
while i < len(nums):
    if(nums[i] == x):
        print("FOUND at idx", i)
    else:
        print("finding....")
    i += 1









#   Question =   06
#   Question =   07
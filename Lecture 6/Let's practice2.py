# Question - 01
#  Write a recursive function to calculate the sum of first n natural numbers.

def calc_sum(n):
    print(n)
    calc_sum(n-1)

calc_sum(5)


#   02


def calc_sum(n):
    if(n == 0):
        return 0
    print(n)
    calc_sum(n-1)

calc_sum(5)


#   03


def calc_sum(n):
    if(n == 0):
        return 0
    return calc_sum(n-1) + n

sum = calc_sum(5)
print(sum)





#  Question - 02
#  Write a recursive function to print all elements in a list.
#  Hint : Use list and index as parameters.


def print_list(list, idx=0):
    if(idx == len(list)):
        return
    print(list[idx])
    print_list(list, idx+1)

fruits = ["mango", "litchi", "apple", "banana"]

print_list(fruits)


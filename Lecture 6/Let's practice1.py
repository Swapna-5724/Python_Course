# # Let's Practice

# #   01
# #   WAF to print the length of a list. (list is the parameter)

cities = ["delhi", "gurgaon", "noida", "pune", "mumbai", "chennai"]
heroes = ["thor", "ironman", "captain america", "shaktiman"]

def print_len(list):
    print(len(list))

print_len(cities)
print_len(heroes)








# #   02
# #   WAF to print the elements of a list in a single line. (list is the parameter)


cities = ["delhi", "gurgaon", "noida", "pune", "mumbai", "chennai"]
heroes = ["thor", "ironman", "captain america", "shaktiman"]

print(heroes[0])
print(heroes[1])



print(heroes[0], end=" ")
print(heroes[1], end=" ")


print(heroes[0], end="\n")
print(heroes[1], end="\n")


def print_len(list):
    print(len(list))

print_len(cities)
print_len(heroes)


# # 2nd function 

cities = ["delhi", "gurgaon", "noida", "pune", "mumbai", "chennai"]
heroes = ["thor", "ironman", "captain america", "shaktiman"]

def print_len(list):
    print(len(list))

def print_list(list):                   # 2nd function
    for item in list:
        print(item, end=" ")

# print_list(heroes)
print_list(cities)
print()


# #   03
# #   WAF to find the factorial of n. (n is the parameter)

n = 5
fact = 1
for i in range(1, n+1):
    fact *= i
print(fact)


# #  function

n = 5

def cal_fact(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    print(fact)

cal_fact(5)



# #   04
# #   WAF to convert USD to INR.


def converter(usd_val):
    inr_val = usd_val * 83
    print(usd_val, "USD =", inr_val, "INR")

converter(73)  # or 100


#  Let's Practice

#  01
#  WAP to find the sum of first n numbers. (using While)

# 001
n = 5

for i in range(n+1):
    print(i)

#  002

n = 5

sum = 0
for i in range(1, n+1):
    sum += i
    i += 1

print("total sum =", sum)


#   003


n = 7
sum = 0
i = 1
while i <= n:
    sum += i

print("total sum =", sum)


#  Factorial Using while Loop

n = 3
fact = 1
i = 1
while i <= n:
    fact *= i
    i += 1

print("factorial =", fact)



#   02
#   WAP to find the factorial of first n numbers. (using for)


n = 5
fact = 1

for i in range(1, n+1):
    fact *= i

print("factorial =", fact)

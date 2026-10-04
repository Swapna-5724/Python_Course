#  sample of Recursion

def show(n):
    if(n == 0):   # Base case
        return
    print(n)
    show(n-1)


#   02

def show(n):
    print(n)
    show(n-1)

show(5)    #5, 4, 3, 2, 1


#   03
#   Recursive function
def show(n):
    if(n == 0):  
        return
    print(n)
    show(n-1)
    print("END")

show(5)




#   Base case helps to decide the loop will stop or not






#   This is a sample
#   Using factorial
#   return n!

def fact(n):
    if(n == 0 or n == 1):
        return 1
    else:
        return n * fact(n-1)




def fact(n):
    if(n == 1 or n == 0):
        return 1
    return fact(n-1) * n


print(fact(2))











#   Notes
#  n! = (n-1)! * n







#  Question -> 01
#  WAP to ask the user to enter names of their 3 favorite movies and store them in a list


#  01

movies = []
mov1 = input("enter 1st movie: ")
mov2 = input("enter 2nd movie: ")
mov3 = input("enter 3rd movie: ")

movies.append(mov1)
movies.append(mov2)
movies.append(mov3)

print(movies)


#  02

movies = []
mov = input("enter 1st movie: ")
movies.append(mov)
mov = input("enter 2nd movie: ")
movies.append(mov)
mov = input("enter 3rd movie: ")
movies.append(mov)


print(movies)


#  03

movies = []
movies.append("enter 1st movie: ")
movies.append("enter 2nd movie: ")
movies.append("enter 3rd movie: ")
movies.append(mov)


#  04

movies = []
movies.append(input("enter 1st movie: "))
movies.append(input("enter 2nd movie: "))
movies.append(input("enter 3rd movie: "))

print(movies)




#   question -> 02
# WAP to check if a list contains a palindrome of elements. (Hint: use Copy() method)

# list1 = [1, 2, 1]
# list2 = [1, 2, 3]
list1 = ["m", "a", "a", "m", "p"]

copy_list1 = list1.copy()
copy_list1.reverse()

if(copy_list1 == list1):
    print("palindrome")
else:
    print("Not palindrome")



# count in Question 1

grade = ["C", "D", "A", "A", "B", "B", "A"]
grade.sort()
print(grade)

# print(grade.count("A"))
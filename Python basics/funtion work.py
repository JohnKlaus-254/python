#Q1 practice question
#
# We should create a function that ‘findsgrade’ by
# taking in marks of each subject as parameters
# calculating total from the parameters(subjects) passed
# calculating the average from the total
# using if statement to find grade
# what if I want to get total marks! and average?
# def findGrade(Math,Chem,Eng,Bio):
#     total= Math+ Chem + Eng+ Bio
#     average= total/4
#
#     if average >= 70:
#         print("Your grade is A")
#     elif average > 60:
#         print("Your grade is B")
#     elif average > 50:
#         print("Your day is C")
#     elif average > 40:
#         print("Your day is D")
#     elif average > 30:
#         print("Your day is E")
#     else:
#         print("You have failed this")
#     print('Your total is: ',total)
#     print('Your average was: ',average)
#
#
# findGrade(69,90,88,90)


# # Q2: Write a function called sum_digits that is given
# an integer num and returns the sum of the digits of num.

# def sum_digits(num):
#     tostr=str(num) #converting to string
#     sum=0#initializing sum
#     for i in tostr:#iterating
#         sum += int(i)#conversion back to integer
#
#     print(sum)
#
#     return sum
# sum_digits(18847)


# sum_digits()


#Q1(googles doc)
#Write a program which accepts a string as input to print "Yes"
# if the string is "yes", "YES" or "Yes", otherwise
# print "No".

# typed_input= input("enter the keyword 'yes': ")
# def capitalize_y(a):
#     if a == 'YES':
#         print('Yes')
#     elif a == 'yes':
#         print("Yes")
#     elif a== 'Yes':
#         print("Yes")
#     else:
#         print('NO')
#
# capitalize_y(typed_input)

#Q2:
#Implement a function that takes as input three variables,
# and returns the largest of the three.
# Do this without using the Python max () function!

# def largest(a,b,c):
#     if a>b and a>c:
#         print('a')
#     elif b>a and b>c:
#         print('b')
#     elif c>a and c>b:
#         print('c')
# largest(2893,56,62)
# largest(688,256,65552)
# largest(123,556,2)
# largest(23,663,662)

#Q3
#Write a program that takes a list of numbers
# (for example, a = [5, 10, 15, 20, 25]) and makes a new
# list of only the first and last elements of the given list.
# For practice, write this code inside a function

# def index():
#     a=[12,45,82,11,89,90]
#     print([a[0], a[-1]])
#
# index()

# Q4
#Ask the user for a number. Depending on whether the
# number is even or odd,
# print out an appropriate message to the user.


# number = input('Enter a value: ')
# number= int(number)
# def oddOrEven(a):
#
#     if a % 2==0:
#         print('its an even number')
#     else:
#         print('its an odd number')
#
# oddOrEven(number)


# Q5
#With a given tuple (1, 2, 3, 4, 5, 6, 7, 8, 9, 10),
# write a program to print the first half values in one
# line and the last half values in one line.

# def arrange():
#     a=(1,2,3,4,5,6,7,8,9,10)
#     a=list(a)
#     print(a[0:5])
#     print(a[5:10])
# arrange()

#Method 2
# def split(aTuple):
#     half =int(len(aTuple)/2)
#
#     first_half =aTuple[:half]
#     last_half =aTuple[half:]
#
#     first_half=
#PART C
# a) Create a function that takes a name and returns a greeting

# def hello():
#     a=input('enter your name: ')
#     print("hellow "+a)
# hello()

#b) Write a function that takes the base and height of a triangle and return its area

# def triArea(b, h):
#     area= 0.5*b*h
#     print(area)
#
# triArea(3,2)

#c) Create a function that finds the maximum range of a triangles third edge.

# def hypotenuse():

#d  You've got chickens (2 legs), cows (4 legs) and pigs (4 legs) on your farm.
# Return the total number of legs on your farm. (CREATE A FUNCTION

# def legs(ch, co, pi):
#     chicken=ch*2
#     cow=co*4
#     pig=pi*4
#     total = chicken+cow+pig
#     print('the total number of legs in the farm are',total)
#
# legs(2,3,5)

#e  Given a list of integers,
# return the difference between the largest and smallest integers in the list.

# def difference():
#



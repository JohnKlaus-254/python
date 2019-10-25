# FUNTIONS- this is a group of related statements that perform a task.
# syntax
# def funtionName(parameters):
#     statements
#
# def hello():#declaration of funtion
#     print('hello world')#statement
#     print('Nicklaus Githua')#statement
# hello()#calling the funtion
# hello()
# hello()#you can call a funtion multiple times


# Parameters
# def addTwoNum(a,b):
#     summ = a+b
#     print(summ)
#
# addTwoNum(90,25)
# addTwoNum(940,25)
# addTwoNum('Teresia',' Nduta')

# def Subtract(a,b):
#   print(a-b)
#
# Subtract(90,25)
# Subtract(940,785)
#
# def Multi(a,b):
#   print(a*b)
#
# Multi(90,25)
# Multi(940,785)

# def check(a):
#
#     if a< 100:
        print("{} is below 100".format(a))
    elif a==100:
        print("{} is equal to 100".format(a))
    else:
        print("{} is above 100".format(a))

check(52)

def division(b):
    if b% 2==0:
        print("divisible by 2")
    else:
        print("not divisible")

division(56)
#
#Strings
def upperCase(name):
    inde1 = name(0).upper()
    fullName = inde1 + name[1:]
    print(fullName)

def name(aName):
    print(aName.replace('Morning', 'Afternoon'))

name('Good Morning')

def addTwoNums(a,b):
    return a+b
#method one
x = addTwoNums(10,10)
print (x)

#method two
print(addTwoNums(20,10))










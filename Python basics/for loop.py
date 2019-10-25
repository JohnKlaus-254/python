# A for loop  loops over a given range
# the i  in example below represents each individual member in the range
# in range, the last value is excluded
# for i in range(100):
#     print(i)
#
# for num in range(5 ,10):#
#     print(num)
#
# for each in range(0 ,20,2):# the third value in range indicates the steps to jump/skip through the loop
#     print(each)


#house = {"utensils":["spoon", "plate", "fork"], "clohes":["beddings","jackets","umbrella", "raincoat"]}
# #print(house)
# for each in house:
#     print(house[each])
#
#
# students = ["Klaus", "Kassim", "Andrew", "Eugine"]
# for every in students:
#     every += " Kamau"
#     print(every)
#
# subjects = [34, 56, 67,34, 67,54, 22,89]
# total = 0
# for sum in subjects:
#     total += sum
# print(total)


#Questions
#write a program that prits ur name a 100 times using a while loop and a for loop
#write a prog tht outputs a 100 lines numbered 1 to 100 each with your name on it
#write a prog that uses a for loop to print the numbes 8 11 14 17 20 ....
#  up to 83 86 89
#write a program that prints the first 20 numbers and their squares and cubes.
# use while loop and for loop to solve them indipendently
#Q1
print('Q1:')
print('For loop')
name = "John Klaus"
for i in range(10):
    print(name)
print('while loop')
a=0
while a< 10:
    print('John K')
    a += 1


#Q2
print('Q2:')
name = "John K"
for i in range(10):
    print(str(i)+name)

#Q3
print('Q3:')
for each in range(8 ,89,3):
    print(each)

#while loop
c=8
while(8<=a<92):
    print(a)
    a+=3

#Q4
print('Q4:')
print('for loop')
for num in range(21):
    print(str(num)+'...'+str(num**2)+'...'+str(num**3))
print('while loop')
a=0
while a<21:
    print(str(a) + '...' + str(a ** 2) + '...' + str(a ** 3))
    a+=1


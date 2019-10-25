#A list is a collection of more than on variable
# a python list- it can hold anything no matter the datatype.

personal=["John Klaus", 23,"juja",True,10000000]
print(len(personal))
print(type(personal))
#list operations
#accessing an element in a list

students=["John","Maxwell","Casium"]

print(students[0])
#concactination
new_student = ["Nduta"]
total_students = students+ new_student
print(total_students)


total_students.append("Caxton")
print(total_students)
a= total_students.count("Caxton")
print(total_students)
print(a)
# A list can store the same element as many times as posiible
print(len(" Jake Williams     ".strip()))#this funtion removes all the extra spaces in a line
pos= total_students.index("Nduta")
print(pos)
print(total_students[1:3])

#KISS- keep it simple
#dry-dont repeat yourself
total_students.insert(0, "Caxton")
total_students.pop(3)

print(total_students)

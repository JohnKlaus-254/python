taskList = [23,"Jane",["Lesson 23", 560,{"currency":"KES"}],987,(76,"John")]

#1. determine the type of variable in tasklist using an inbiuld funtion
#2. Print KES
#3. Print 560
#4. Use a funtion to determine the length of task list
#5. change 987 to 789 without using an inbiuld method or assignment
#6. Change the name John to Jane

print('Q1:')
print(type(taskList))

print('Q2:')#KES
print(taskList [2][2]["currency"])

print('Q3:')#560
print(taskList[2][1])

taskList = [23,"Jane",["Lesson 23", 560,{"currency":"KES"}],987,(76,"John")]

print('Q4:')#Funtion length
print((len(taskList)))

print('Q5:') #change 987 to 789. convert to a string and then inverse the the string
print(str(taskList[3])[::-1])

print('Q6: a tuple cannot be changed') #change john to jane

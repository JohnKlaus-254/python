if True:
    print('True')

marks = input("What is your KCPE marks: ")
#marks = int(marks)
marks = eval(marks) # this is preferable incase the user inputs a float. you convert bcz python takes input as a string.
if marks <0 or marks>500:
    print("Your Marks are unrealistic")
else:
    if marks >= 350 and marks<= 500:
        print("Congulaculation you are Admitted")
    else:
        print("Sorry try again next year")

#Read on if-elif statements
#create a program for a leap year

avg_marks= eval(input("Average Marks: "))
if avg_marks >= 80 and avg_marks <= 100:
    print("A")
elif avg_marks >= 70:
    print("B")
elif avg_marks >= 60:
    print("C")
elif avg_marks >= 50:
    print("D")
else:
    print("You have Failed this Semester")

year = eval(input("Enter the year you intend to check: "))
if (year % 4) == 0:
    print("This is a Leap Year")
else:
    print("This isn't a Leap Year")



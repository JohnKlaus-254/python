# While loop - A while loop repeats its execution of its indented block until the condition given becomes False
#a = 0
#while a < 10:
   # print("John Klaus")
    #a += 1
    #print(a)

savedpin = "6669"
tries = 3


current = input("Enter Pin")
tries -= 1

while current != savedpin and tries > 0:
    current = input("Enter Pin Again")
    tries -= 1


if current != savedpin:
    print('card blocked, visit the bank')
else:
    print('Welcome to your Account')

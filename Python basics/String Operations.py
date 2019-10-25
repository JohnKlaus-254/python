#CONCACTINATION using a plus
#CONCACTINATION using a format
first_name= "John"
last_name = "Klaus"

full_name = first_name +' '+ last_name
print(full_name)
#a better way to do this is;
full_name = "{} {}".format(first_name, last_name)
print(full_name)

print("this man is called {} from the family of {} ".format(first_name, last_name))
#format
names ="John Klaus"
name2 = "jake williams"
name3 = "DENNIS WAWERU"

print(name2.title())

#count - counts the number of time something has been repeated
#python is case sensitive
sen="Man is to error because man did not create Man"
print(sen.lower().count("a"))
#String slicing
#left of the colon signify the starting element
#right of the coon signify the ending position but that element in that position is excluded. so to include it, add up to the next element.
print(sen[0:15])

jina = "muyani"
print(jina[1:-2])
print(jina[2::-2])

print(sen.split())

sente ="learning more string funtions"
print(sente.join())
print(sente.replace())
print(sente.index())
print(sente.find())
print(sente.center())
print(sente.isalpha())






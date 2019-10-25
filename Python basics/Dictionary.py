#A dictionary is a data structure that holds 'key' 'value' pairs
personal=["John Klaus", 23,"juja",True,10000000]
a =0
b=0.0
c=""
d=[]
e=()
f= {}# dictionary
print(type(f))

personal={"name":"John Klaus","age":22,"location":"juja","is_tall":True, "networth":10000000}
#accessing  an element
print(personal["age"])
print(personal["location"])
print(personal["name"])
print(personal)
#dict Methods
personal.copy()

personal.get("age")
print(personal)
personal.items()
personal.keys()
personal.pop()
print(personal)
personal.clear()
#we can use three types of conditions:
#1. if
#2. if-else
#3. if-elif-else

#python uses indentation to define blocks of code with : operator

a=12

if a>10:
    print("thats correct")
    print("awesome facts")
print("the end")

name=input("What is the secret identity of Batman?")
if name=="bruce wayne":
    print("thats correct")
if name=="alfred":
    print("thats not correct")
if name=="gordon":
    print("thats stupid")

food = input("What would you like to eat?\n>>")
if food in ["ice-cream", "daal-chawal","naam-sabji"]:
    print("okay, make it yourself")
if food=="pizza":
    print("okay")

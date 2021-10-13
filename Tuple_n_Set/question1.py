#WAP to add values from user in a set
#they can add any number of values in the set
#use while loop to perform this task

data=set()

while True:
    x=input("Enter a value : ")
    if not x:
        break
    data.add(x)

print(data)
#WAP to take user input to create a list
#the user should decide the size of list
#the list should be numeric
#display list values

a=int(input("Enter the size of list : "))
x=[]
for i in range(a):
    val=int(input("Enter a value : "))
    x.append(val)

print("The numbers are : ",x)

total = sum(x)
print(total)
x_max = max(x)
print(x_max)
x_min = min(x)
print(x_min)
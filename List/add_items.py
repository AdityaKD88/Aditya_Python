x=[]        #empty list
print("Enter three values : ")
for i in range(3):
    val=input("->")
    x.append(val)

x.append(10)
x.append('Helium')
x.append(True)
# x.append(1,2,3)       error
x.append(['a','b','c'])     #append list to the end of list

print(x)

x.insert(0,200)
x.insert(4,'Banana')
x.insert(-3,'Apple')
x.insert(2,[1,2,3,6])
print(x)

a = [1,2,3,4]
b = [3.0,2.1,4.8]

print(a)
print(b)
a.extend(b)
print(a)
b.extend(a)
print(b)
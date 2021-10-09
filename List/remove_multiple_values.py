x=[1,2,33,2,1,2,3,1,2,3,2,2,55,655,15,551,665,12,551,665,15,155,46]
print(x)
y=x.copy()
#remove all the 3s in this list
for i in range(x.count(3)):
    x.remove(3)
print("Removed all 3s")
print(x)

#removing all 3s with pop n index
while 3 in y:
    idx=y.index(3)
    y.pop(idx)
print(y)
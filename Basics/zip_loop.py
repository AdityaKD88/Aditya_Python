num=[12,24,36,48]
num2=[11,22,33,44]
num3=[8,16,24,32,40,48]
for i,j in zip(num,num2):
    print(i,j)

for i,j in zip(num,num2):
    print(i+j)

for i,j,k in zip(num,num2,num3):
    print(j,i,k)
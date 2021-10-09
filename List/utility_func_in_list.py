x=[1,2,33,2,1,2,3,1,2,3,2,2,55,655,15,551,665,12,551,665,15,155,46]
print(x)

print("occurence of 1 = ",x.count(1))
print("occurence of 1 = ",x.count(2))
print("occurence of 1 = ",x.count(3))
print("occurence of 1 = ",x.count(5))
print("occurence of 1 = ",x.count(15))

a = ['chicago', 'new york', 'delias']
b = [12,45,13]
c = ['Nevada', 57, 'Massouri', 58]
print(a)
a.sort()
print(a)

print(b)
b.sort(reverse=True)
print(b)
#erroe
#print(c)
#c.sort()
#print(c)

y = [1,1,12,1,1,2,2,22,2,3,3,3,3,3,]
print(y)
y.reverse()
print(y)
y.reverse()
print(y)
idx=y.index(22)
print("22 found at ",idx)
idx=y.index(2)
print("2 found at ",idx)
if 123 in y:
    idx=y.index(123)
    print("123 found at ",idx)

z=x.copy()
print(z)
print(x)
x.sort()
print(x)
print(z)

a=(1,2,3)
b=12,34,56

print(a,b)
print(type(a),type(b))

c=('Chimera','Mintour','Persues')
print(c[0])     #accesing value from index
print(c[1])
print(c[-1])

#creating tuple from existing data
name='Rahul'
nameT=tuple(name)
print(nameT)        #new variable contains tuple < CREATE

values=[1299,239,8329,1239]
values=tuple(values)
print(values)

a=12
b=23

x=a,b
print(x)
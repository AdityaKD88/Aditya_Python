'''
- comprehension -> when we want to create a list from existing list in one line
- mapping -> generate same size sequence from existing sequence
- filtering -> create a smaller sequence from existing one, using a condition
'''

'''syntax
newlist = [ operation loop-for-existinglist condition(optional) ]
'''

x=[2,3,51,2,74,567,89,109,189]
#mapping
x2 = [i**2 for i in x]
print(x)
print(x2)

#filter
x_odd = [i for i in x if i%2!=0]
print(x_odd)

x_odd_sqr = [i**2 for i in x if i%2!=0]
print(x_odd_sqr)
'''1. WAP to create a dict that contains following sequence:
1 : 1
2 : 4
3 : 9
4 : 16
...
10 : 10000
hint : use for loop, don't do this manually 
'''

num = {}
for i in range(1,101):
    num[i]=i**2
print(num)

'''2. WAP to sort a dictionary of 5 elements
you can put anything inside the dictionary
'''

# sot by keys
colors = {
    'R': 'red',
    'G': 'green',
    'B': 'blue',
    'Y': 'yellow',
    'Bl': 'black'
}
print(dict(sorted(colors.items())))
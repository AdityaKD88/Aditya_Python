'''WAP to ask the user his/her expenses on different items. Take
around 15 key and value from user and then perform sum and average
on the values.
'''
items = {}
for i in range(3):
    k = input('enter an item ->> ')
    v = int(input('enter the value ->> '))
    items[k]= v

sum=0
for i in items:
    sum=sum+items[i]

print('\nItem and expenses are : ')
for k,v in items.items():
    print(k,"=>",v,end=', ')

print("\nSum of itemsenses is : ",sum)
print("\nAverage of itemsenses is : ",sum/len(items))

'''
expences = {}
for i in range(15):
    k = input('enter a word->>')
    v = int(input('enter the meaning->>'))
    expences[k]= v
total = sum(list(expences.values()))
average = sum(list(expences.values())/len(expences))
print(f'total is {total}, average is {average}')
'''
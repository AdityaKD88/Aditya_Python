num = list(range(1,15))

for element in num:
    print(element)

words = ['this','that','wish','what','word']
for item in words:
    print(f'{item} is {len(item)} chars')

coords = [[1,2],[2,3],[4,5]]
for i in coords:
    print(i)

for i in coords:
    print(i[0],i[1])

for idx, value in enumerate(words):
    print(f'{idx} has {value}')

for i in num:
    if i%3==0:
        print(i)

for item in coords:
    for i in item:
        print(i)
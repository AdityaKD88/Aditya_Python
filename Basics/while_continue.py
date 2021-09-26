'''
we have continue keyword
which is used to skil a loop step
it can be used in for and while both
'''

i=int(input("Enter value of i : "))

while i>0:
    if i%3==0:
        i-=1
        continue
    print(i)
    i-=1

#we can easily skip continue keyword
i=int(input("Enter value of i : "))
while i>0:
    if i%3!=0:
        print(i)
    i-=1
'''Use the file from gutenburg to read and
count the words and then store the answer in a new file
like this
a  12
to  123
hi  45
this  343
Make this a one or more function program
'''
file=open('dummy.txt','r')
words=file.split()
x=dict()
for c in words:
    x[c]+=1
file.close()
for k in list(x.keys()):
    print(k, ":", x[k])
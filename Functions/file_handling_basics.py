'''
file handling basics
1. read a file - open()     r - read
2. write a file - open()    w - write
3. update a file - open()   a - append
open() function has a option to set mode of file
it returns a file object
'''

file = open('dummy.txt')
print(file.read())
file.close()

f1 = open('radiants.txt','w')
f1.write("The radiants are saviors of humanity.\n")
f1.write("They have shardplate and shardblade\n")
f1.write("To be continued")
f1.close()      #save

f2=open('dummy.txt','a')
f2.write("\nWritten by Knowledgeble person")
f2.close

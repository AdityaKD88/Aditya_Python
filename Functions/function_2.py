#count number of characters, words, punctuatuation, spaces from file
import file_function as ff

data=ff.reader('dummy.txt')
print('Number of characters are : ',len(data),'chars in file')
print('Number of words are : ',len(data.split()))
print('Number of spaces are : ',data.count(' '))

count=0 
for i in range (0, len (data)):   
    if data[i] in ('!', ',', ';', '.', '-', '?', '\''):
        count += 1;  
print ("Number of punctuation are : ",count)
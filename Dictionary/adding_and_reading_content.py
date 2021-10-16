words = {}  #dict

words['alpha'] = "number one, the starting value, or the top value"
print("User input -->")
for i in range(3):
    k=input("Enter a word : ")
    v=input("Enter the meaning : ")
    words[k]=v

#full
print(words)

#reading a particular
print(words['alpha'])
print(words.get('alpha', 'not found'))
print(words.get('beta'))
print(words.get('beta', 'not found'))
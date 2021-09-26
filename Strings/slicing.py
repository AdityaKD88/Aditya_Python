name ="Doctor Stephen Strange"

print(len(name))
print(name[3],name[4],name[5])      #noob implementation
print(name[3:6])                    #pro implementation
print(name[7:-8])
#we can skip value before colon if we want to start from beginning
#we can skip value after colon if we want to stop at the end
print(name[:6])
print(name[-7:])

#syntax for slicing
#var[startIdx : endIdx : gap]
print(name[::2])
print(name[1::2])

#reverse string
print(name[::-1])
print(name[:])
print(name[:][::-1][:5])
#WAP to find the sum of all values in a numeric list

x=[1,12,123,1234]
total=0
for i in x:
    total += i
print(x,'>> total = ',total)

#short version

total = sum(x)
print(total)
x_max = max(x)
print(x_max)
x_min = min(x)
print(x_min)

#average
x_mean = sum(x)/len(x)
print(x_mean)
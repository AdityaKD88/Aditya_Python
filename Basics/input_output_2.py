a=10
b="balls"
c=100
d="Rupees"

#printing with comma seperated values
print("Raju purchased",a,b,"for",c,d)

#contacatenation using +
print("Raju purchased " + str(a) + " " + b + " for " + str(c) + " " + d)

#printing format specifier
print("Raju purchased %d %s for %d %s" %(a,b,c,d))

#print using format() method
print("Raju purchased {} {} for {} {}".format(a,b,c,d))

#printing using f-string (from ver=3.6)
print(f"Raju purchased {a} {b} for {c} {d}")

#properties of print function
#end - handles what will be displayed after printing content (mainly used in loops)
#sep - separator symbol

print("Hi", end="gkugouy")
print("There")

print(a,b,c,d)
print(a,b,c,d, sep="XX")
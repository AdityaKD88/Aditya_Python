#python has different operators
#1. Mathematical
#2. Conditional or comparison
#3. Assignment
#4. Logical
#5. Membership
#6. Instance
#7. Walrus

#mathematical operators
a=10+3
print(a)
a=10-3
print(a)
a=10*3
print(a)
a=10/3      #division - real number
print(a)
a=10%3      #modulus - remainder
print(a)
a=10//3     #integer division - quotient
print(a)
a=10**3     #exponent
print(a)

#comparison operators
a=10
b=3
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)
print(a==b)
print(a!=b)

#assignment operators
c=15
print(c)
c+=10 #add 10 to existing value of c
print(c)
c-=10 #subtract 10 to existing value of c
print(c)
c*=10 #multiply 10 to existing value of c
print(c)
c/=10 #divide 10 to existing value of c
print(c)
c//=10
print(c)
c%=10
print(c)
c**=10
print(c)

#logicl operators - multiple expression [and, or, not]
a=5
b=15
c=10
print(a>b and a>c)
print(b>a or b>100)
print(not a>b)
print(not(a>b and a<c or a>10))

#membership operator - in [it can search a value in an iterable]

colors = ["red", "blue", "green", "purple", "yellow"]

print("red" in colors)
print("brown" in colors)
print("Green" in colors)
print(45 in colors)
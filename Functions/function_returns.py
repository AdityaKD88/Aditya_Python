def hypotenuse(a,b):
    hyp=(a**2+b**2)**.5
    return hyp

#answer can be stored
ans=hypotenuse(3,4)
print("Answer",ans)

#can be used in expression
out = hypotenuse(3,4)+hypotenuse(4,5)*5
print(out)

#can be directly printed if no0 variable is needed
print(hypotenuse(10,10))
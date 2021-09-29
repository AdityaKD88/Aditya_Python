value=input("Enter something ")

ans = value.isupper()
print("Is the value entered is upper? ",ans)

ans = value.islower()
print("Is the value entered is lower? ",ans)

ans = value.isalpha()
print("Does the value contain only alphabet? ",ans)     #only alphabets(no specical character or space)

ans = value.isnumeric()
print("Does the value contains only numbers? ",ans)

ans = value.isspace()
print("Does the value conatins only space? ",ans)

ans = value.isprintable()
print("Is the value printable on screen? ",ans)

ans = value.isdigit()
print("Does the value contains only digits? ",ans)

ans = value.isdecimal()
print("Does the value contains decimal numbers? ",ans)      # . does not comes under decimal

name="Dr. Ram Verma"

if name.startswith("Dr."):
    print("Hello Doctor")
if name.startswith("Mr."):
    print("Hello Mister")

file=input("Enter the filename")
if file.endswith(".exe"):
    print(f"{file} is application file")
elif file.endswith(".doc"):
    print(f"{file} is word file")
elif file.endswith(".pdf"):
    print(f"{file} is PDF file")
elif file.endswith(".png"):
    print(f"{file} is PNG file")
else:
    print(f"{file} is not defined")
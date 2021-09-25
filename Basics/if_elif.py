weather = input("How is the weather today =>")
if weather.lower() == "warm":
    print("put on some light clothes when you get out")
elif weather.lower() == "cold":
    print("take the jacket you")
elif weather.lower() == "rainy":
    print("wear raincoat")
elif weather.lower() == "humid":
    print("stay home")
else:
    print("try again")

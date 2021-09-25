print("You see three doors select one from them")
door=input("1 or 2 or 3")

if door=="1":
    print("you enter the room that is dark")
    print("you see to glowing eyes")
    print("What will you do?")
    ans = input("run / stand / attack")
    if ans=="run":
        print("You stumble and get hurt")
    if ans=="attack":
        print("you try to attack the gloming eyes but they are actually small candles")
    if ans=="stand":
        print("nothing appens")
if door=="2":
    print("it was a trap, you die")
if door=="3":
    print("there is wall behind the door")
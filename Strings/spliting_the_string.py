msg ="We will be seeing the horizon"

words=msg.split()
print(words)

msg2="Hi there, how are you? Where have you been? ok"
sentence=msg2.split(",")
print(sentence)

sentence=msg2.split("?")
print(sentence)

gibberish=msg2.split("a")
print(gibberish)

print(f"We found {len(words)} words in msg")
print(f"We found {len(msg2.split())} words in msg2")

msg3="Welcome to wakanda, you will have fun, just dont steal from us, or you will have no fun"

print("Normal ->",msg3.split(","))
print("Normal 2 split ->",msg3.split(",", maxsplit=2))
print("Reverse ->",msg3.rsplit(","))
print("Reverse 2 split ->",msg3.rsplit(",", maxsplit=2))

print(msg3[:18])
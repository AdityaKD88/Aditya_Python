'''
find    - better
index
'''
msg = "Once upon a time, their was a kingdom, the king was Richard"

idx=msg.find("time")
print(f"time was find at index {idx}")
idx=msg.find("queen")
print(f"time was find at index {idx}")
if idx==-1:
    print("queen was not find")

idxking=msg.find("king")
print(f"king was found at index {idxking}")

idxa=msg.find("a")
print(f"king was found at index {idxa}")
print(len(msg))
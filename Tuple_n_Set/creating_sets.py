x = ()      #empty set

x={1,2,3,1,2,3,1,2,3,1,2,3,1,2,3}
print(x)

words = {'Knights','Radiants','Shards','Blades','Armor'}
print(words)

for value in words:
    print(value,end=' ')
quote = "Life Before Death, Courage, Before Fear, Journey Before Destination"
quote_chars=set(quote.lower())
print("\n",quote_chars)
print(len(quote_chars))
content ='''Tony Stark is the wealthy son of industrialist and weapons
manufacturer Howard Stark and his wife, Maria. Tony grew up a genius
with a brilliant mind for technology and inventions and, naturally,
followed in his father’s footsteps, inheriting Stark Industries upon
his parents’ untimely death. Tony designed many weapons of war for
Stark Industries, far beyond what any other company was creating, while
living the lifestyle of a bon vivant.'''

words=content.split()
print(words)

max_freq=0
max_occ_word=''
for item in words:
    count = words.count(item)
    print(f'{item} --> {count}')
    if count>max_freq:
        max_freq=count
        max_occ_word=item

print(f'{max_occ_word} ---> {max_freq}')
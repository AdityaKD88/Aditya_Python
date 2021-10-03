from string import ascii_lowercase

content ='''
Doctor Stephen Vincent Strange M.D., Ph.D is the Sorcerer Supreme
and a Master of the Mystic Arts. Originally a brilliant,
although arrogant, neurosurgeon, Strange got into a car accident
which resulted with his hands becoming crippled. When all Western
medicine failed him, Strange embarked on a journey that led him
into Kamar-Taj where Strange had made the discovery of magic and
alternate dimensions, being trained by the Ancient One. Though
focused on healing his hands and returning into his career, Strange
learned more of the mystic arts and helped the Masters prevent
Kaecilius from merging the Earth with the Dark Dimension, but not
before witnessing the Ancient One's death. Following the demise of
their mentor, Strange became the protector of the New York Sanctum
in New York as well as the Earth's protector from any new inter-dimensional threats.
'''

num_of_a=content.count("a")
print(f"a occurs {num_of_a} times")

in_counter=content.count("in")
print(f"in occurs {in_counter} times")

#counting all alphabets

max_freq=0
most_freq_letter=""
for letter in ascii_lowercase:
    counter=content.count(letter)
    print(f"{letter} found {counter} times")
    if max_freq < counter:
        max_freq=counter
        most_freq_letter=letter

print(f"the {most_freq_letter} has highest frequency: {max_freq}")
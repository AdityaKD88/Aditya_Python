# REMOVE
# searching value - use with if condition

colors = ['yellow', 'green', 'blue', 'purple', 'pink', 'black', 'pink']
colors.remove('yellow')
print(colors)
if 'jellow' in colors:
    colors.remove('jellow')
print(colors)
if 'pink' in colors:
    colors.remove('pink')
print(colors)
# POP
# remove value by idx - if not given remove last
# the removed value can be stored in a variable
colors.pop(1)
print(colors)
separated_value=colors.pop(2)
print(colors)
print(separated_value)

colors.pop()
print(colors)

# CLEAR

colors.clear()
print(colors)
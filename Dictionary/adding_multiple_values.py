menu = {
    'Veg Manchurian' : 189.00,
    'Fried Rice' : 100.00,
    'Veg Momos' : 80.00
}

new_menu = {
    'Chicken Manchurian' : 259.00,
    'Chicken Momos' : 160.00
}
print('Before Update',menu)

menu.update(new_menu)
print('After Update',menu)

update_menu = {
    'Veg Momos' : 100,
    'Veg Chowmein' : 120.00
}

menu.update(update_menu)
print('Final Menu',menu)
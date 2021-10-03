msg ='''
Doctor Stephen Vincent Strange M.D., Ph.D is the Sorcerer Supreme and a 
Master of the Mystic Arts. Originally a brilliant, although arrogant, neurosurgeon,
Strange got into a car accident which resulted with his hands becoming crippled.
'''
print(msg)

updated_msg=msg.replace('the','wow')
print(updated_msg)

updated_msg=msg.replace(',','l')
print(updated_msg)

#remove via replace()
updated_msg=msg.replace('e','')
print(updated_msg)
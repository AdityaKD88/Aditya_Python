
student = ['billu',17,15,12,14,False,True,9393939393]

stdDict = {
    'name'       : 'billu',
    'maths'      : 17,
    'english'    : 15,
    'hindi'      : 12,
    'age'        : 14,
    'studies'    : False,
    'delinquent' : True,
    'phone'      : 9393939393
}

print(stdDict)

myinfo={
    'city' : 'lucknow',
    'state': 'UP',
    'phone': 2893128938,  # when we create 2 keys with same name in a dictionary, it will overwrite the content
    'phone': 8293892922
    }

print(myinfo)

address = dict(sno=121,street='abcd street',
location='blah blah blah',city='Lucknow',pincode=226001)

print(address)
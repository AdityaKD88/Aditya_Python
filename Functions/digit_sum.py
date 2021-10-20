import file_function as ff
def sum(number):
    s=0
    while number>0:
        digit = number % 10
        s += digit
        number //= 10
    ff.writer('num.txt',str(s))

sum(154)

'''
def sum(number):
    s=0
    for digit in str(number):
        s+=int(digit)
    ff.writer('num.txt',str(s))
sum(154)
'''
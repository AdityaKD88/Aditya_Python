def is_leap_year(year):
    if year%4==0:
        if year%100==0:
            if year%400==0:
                return True
            else:
                return False
        else:
            return True
    return False
x=int(input("Enter a year : "))
if 1900<=x<=10**5:
    print(is_leap_year(x))
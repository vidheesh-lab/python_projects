year=int(input('enter a year: '))
if(year%4==0):
    print('It is divisble by 4,so it may or may not be leap year')
    if(year%100==0):
        print('It is divisble by 100, so it may or may not be a leap year')
        if(year%400==0):
            print('It is a leap year')
        else:
            print('It is not a leap year')
    else:
        print('It is a leap year')
else:
    print('It is not a leap year')
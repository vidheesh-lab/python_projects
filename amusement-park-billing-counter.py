print('WELCOME TO PYTHON AMUSEMENT PARK')
a,b,c,d,e=200,250,300,50,150                #a=below12,b=12to18,c=above18,d=photo,e=lunch
print(f'The ticket prices are: \nFor kids(below 12 years)={a} \nFor teens(12 to 18 yrs)={b} \nFor adults(above 18yrs)={c}')
print(f'Other charges: \nPhotos={d} \nLunch={e}')
adults=int(input('Please tell the count of adults: '))
teens=int(input('Please tell the count of teens: '))
kids=int(input('Please tell the count of kids: '))
money1=a*kids
money2=b*teens
money3=c*adults
total_ticket_price=money1+money2+money3
photos=input('Do u need any photos? ')
lunch=input('Do u need any lunch? ')
if(photos=='yes'):
     count=int(input('mention the count of photos: '))
else:
     print('OK sure')
     count=0
if(lunch=='yes'):
     count1=int(input('mention the count of lunch: '))
else:
     print('OK sure')
     count1=0
money4=d*count
money5=e*count1
total=total_ticket_price+money4+money5
if(total>=1100):
     print('CONGRATS SUMMER OFFER HAS BEEN CLAIMED')
     a1=20/100
else:
     print('NO OFFERS VALID SORRY')
     a1=0
grand_total=total-(total*a1)
print('=====================YOUR BILL============================')
print('====NAME=======COUNT=======UNIT PRICE=======TOTAL')
print(f'    ADULTS     {adults}     {c}             {money3}')
print(f'    TEENS      {teens}      {b}             {money2}')
print(f'    KIDS       {kids}       {a}             {money1}')
print(f'    PHOTOS     {count}      {d}             {money4}')
print(f'    LUNCH      {count1}     {e}             {money5}')
print('===========================================================')
print(f'   TOTAL                                    {total}')
print('===========================================================')
print(f'OFFER CLAIMED: {a1}')
print('===========================================================')
print(f'                  GRAND TOTAL           {grand_total}     ')
print('===========================================================')
print(f'THANK YOU, ENJOY YOUR RIDES!!!')
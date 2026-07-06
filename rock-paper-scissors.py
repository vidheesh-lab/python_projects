print('WELCOME TO THE GAME OF ROCK, PAPER AND SCISSORS')
print('THE RULES: \n0 stands for rock \n1 stands for paper \n2 stands for scissors')
a=int(input('Enter a number: '))
if(a<=2):
    if(a==0):
        print('YOU PLAYED ROCK')
    elif(a==1):
        print('YOU PLAYED PAPER')
    else:
        print('YOU PLAYED SCISSORS')  #general
    import random
    b=random.randint(0,2)
    if(b==0):
        print('SYSTEM PLAYED ROCK')
    elif(b==1):
        print('SYSTEM PLAYED PAPER')
    else:
        print('SYSTEM PLAYED SCISSORS')
    if(a!=b):
        if(a>b):
            if(a==2 and b==0):
                print('YOU LOSE')
            else:
                print('YOU WIN')
        if(b>a):
            if(b==2 and a==0):
                print('YOU WIN')
            else:
                print('YOU LOSE')
    else:
        print('TIE')
else:
    print('invalid')
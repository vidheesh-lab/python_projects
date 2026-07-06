# Initial system variables
user_full_name = "Master Python Programmer"
masked_account = "ACT-XXXX-1994"
system_pin = "4321"

# The master currency list holding user balance codes
# 'USD' = $100, 'EUR' = $110, 'INR' = $1.20
wallet_balances = ["USD", "EUR", "INR", "USD", "INR", "INR"]

print('================ BANKING TERMINAL ===============')
security_pin=input('Enter 4-digit security pin: ')

#checking if pin is correct and generating a random number
if(security_pin==system_pin):
    import random
    random_number=random.randint(1000,9999)
    year=masked_account[-4:]
    print('--- SECURITY VERIFICATION ---')
    print(f'Welcome, {user_full_name} \nSession token: {random_number} \nAcoount year: {year}')
    usd=wallet_balances.count('USD')
    eur=wallet_balances.count('EUR')
    inr=wallet_balances.count('INR')
    total_holdings=(usd*100)+(eur*110)+(inr*1.20)
    print(f'USD holdings: {usd} units \nEUR holdings: {eur} units \nINR holdings: {inr} units')
    print(f'TOTAL WALLET VALIDATION IS ${total_holdings}')

    #adding currency to the wallet
    
    print('--- INJECT NEW CAPITAL ---')
    answer=input('Do u want to add currency? ')
    if(answer=='yes' or answer=='Yes'):
        code=input('Enter currency code: ')
        code_list=code.split(',')
        wallet_balances.extend(code_list)
        print('DEPOSIT SUCCESSFUL')
        new_length=len(wallet_balances)
        print(f'Total ledger inventory records: {new_length}')
    else:
        print('ok sure')
    

    #withdrawing the currency from the wallet
    print('--- AUTOMATED WITHDRAWAL GATE ---')
    answer1=input('Do you want to withdraw currency? ')
    if(answer1=='yes' or answer1=='Yes'):
        code1=input('Enter currency code to withdraw: ')
        if(code1 in wallet_balances):
            count=wallet_balances.count(code1)
            if(count>2):
                print('Processing high-volume withdrawal...')
                print('--- FINAL TRANSACTION RECEIPT ---')
                print(f'Token Authorisation: {random_number} \nFinal Status: SUCCESS')
            elif(count==1 or count==2):
                print('Processing standard withdrawal...')
                print('--- FINAL TRANSACTION RECEIPT ---')
                print(f'Token Authorisation: {random_number} \nFinal Status: SUCCESS')
            else:
                print('[DENIED] Insufficient specific currency reserves!')
        else:
            print('NOT VALID CURRENCY')
    else:
        print('Ok sure')
else:
    print('[CRITICAL] ACCESS DENIED: INVALID SECURITY PIN')
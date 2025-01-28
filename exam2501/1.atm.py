
 # 1.ATM SIMULATOR
def check_balance(bank_bal):
    print(f"YOUR BANK BALANCE: {bank_bal}""\n")
    return bank_bal
def deposit_money(amnt,bank_bal):
    bank_bal+=amnt
    print(f"RUPEES {amnt} IS CEREDITED""\n")
    return bank_bal

def withdraw_money(amnt,bank_bal):
    bank_bal-=amnt
    print(f"RUPEES {amnt} IS DEBITED""\n")
    return bank_bal

def switch(ch,min,bank_bal):
    if(ch==1):
        check_balance(bank_bal)
        return bank_bal
    elif(ch==2):
        amnt=int(input("ENTER DEPOSIT AMOUNT: "))
        bank_bal=deposit_money(amnt,bank_bal)
        return bank_bal
    else:
        amnt=int(input("ENTER THE WITHDRAWAL AMOUNT: "))
        if(min<(bank_bal-amnt)):
            bank_bal=withdraw_money(amnt,bank_bal)
            return bank_bal
        else:
            print("THE WITHDRAWAL IS DECLINED DUE TO CROSSING THE LIMIT OF MINIMUM BALANCE\n")
            return bank_bal
print("WELCOME TO ATM \n")
MIN_BAL=1000
bank_bal=1000
t=True
while(t):
    print("1. CHECK BALANCE \n2. DEPOSITE MONEY \n3. WITHDRAW \n4. EXIT \n")
    ch=int(input("enter the appropriate number for operation \n"))
    if(ch>4):
        print("ENTER VALID OPTION \n")
        continue
    elif(ch==4):
        break
    else:
        bank_bal=switch(ch,MIN_BAL,bank_bal)
print("THANK YOU \n")
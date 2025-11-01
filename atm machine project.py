def atm():
    balance=10000
    while True:
        print("1.check balance")
        print("2.Deposite")
        print("3.Withdraw")
        print("4.Exit")
        a=int(input("enter a password"))
        b=1234
        if(a==b):
            print("right password")
        else:
            print("wrong password")
            break    
        choice=int(input("enter your choice"))
        if choice==1:
            print("your balance is",balance)
        elif choice==2:
            amount=int(input("enter the amount you wantto deposite"))
            balance=balance+amount
            print("deposited money",amount)
        elif choice==3:
            amount=int(input("enter the amount you want to withdraw"))
            if amount<=balance:
                
                print("withdraw money",amount)
            else:
                print('insufficient money')
            balance-=amount
        elif(choice==4):
            print("thankyou")
            break
        else:
            print("invalid choice")    

atm()                

                      

class Bank:
    def __init__(self,acc_no,name,type,bal):
        self.acc_no=acc_no
        self.name=name
        self.type=type
        self.bal=bal
    def deposit(self,amt):
        if amt<=0:
            print("It should be an positive number")
        else:
            self.bal += amt
            print("Your current balance is ",self.bal)
    def withdraw(self,amt):
        if amt <= 0:
            print("It should be a positive number")
        elif amt>self.bal:
            print("Insufficient balance")
        else:
            self.bal=amt
            print("Your current balance is:",self.bal)
    def display(self):
        print(f"Account Number:{self.acc_no}")
        print(f"Account Holder:{self.name}")
        print(f"Account Type:{self.type}")
        print(f"Account Balance:{self.bal}")
no=int(input("enter the account number:"))
name=input("enter your name:")
type=input("enter the account type:")
bal=int(input("enter your balance:"))
usr1=Bank(no,name,type,bal)
while True:
    print("\n1)DEPOSIT\n2)WITHDRAWAL\n3)ACCOUNT INFORMATION\n4)EXIT\n")
    opt=int(input("Enter the option"))
    if opt==1:
        amt=int(input("Enter your amount"))
        usr1.deposit(amt)
    elif opt==2:
        amt=int(input("Enter your withdrawal amount"))
        usr1.withdraw(amt)
    elif opt==3:
        usr1.display()
    elif opt==4:
        exit(0)
    else:
        print("invalid option")
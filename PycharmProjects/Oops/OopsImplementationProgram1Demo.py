import sys
class Customer:
    '''Customer class related operation'''
    bankname='satyambank'
    def __init__(self,name,balance=0):
        self.name=name
        self.balance=balance
    def deposit(self,amount):
        self.balance=self.balance+amount
        print('After deposit balance is: ',self.balance)
    def withral(self,amount):
        if amount>self.balance:
            print('Insufficient balance')
            sys.exit()
        else:
            self.balance=self.balance-amount
            print('After withral accont balance :',self.balance)

print('WELCOME TO',Customer.bankname)
name=input('enter customer name')
c=Customer(name)
while True:
    print('d-Deposit\nw-Withral\ne-Exit')
    option=input('choose your required option')
    if option=='d' or option=='D':
        amount=float(input('enter the amount to deposit'))
        c.deposit(amount)
    elif option == 'w' or option == 'W':
        amount = float(input('enter the amount to withral'))
        c.withral(amount)

    elif option=='e' or option=='E':
        print('thanks for bankig')
        sys.exit()
    else:
        print('choose valid option')
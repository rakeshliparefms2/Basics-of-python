"""
Bank application using OOP:
"""























































































































































































































































































































































































































































































































































































































































































































































































































































































    def __init__(self,name,balance = 0.0):
        self.name = name
        self.bal = balance
    def deposit(self,amt):
        self.bal += amt
        time.sleep(2)
        print('Total Balance after credit is Rs.',self.bal)
    def withdraw(self,amt):
        self.bal -= amt
        time.sleep(2)
        print('Total Balance after debit is Rs.', self.bal)
nm = input('Enter your Name:')
b = Bank(nm)
while True:
    print('--------------------------')
    time.sleep(2)
    print('Hello',nm, 'Welcome to',Bank.bank_name)
    print('--------------------------')
    time.sleep(2)
    print('Which operation would you like to perform')
    time.sleep(3)
    print('1.Deposit\n2.Withdraw\n3.Current Balance\n4.Exit')
    time.sleep(2)
    choice = input('Enter your choice:')
    if choice == '1':
        print(nm,'you have selected Credit option')
        time.sleep(2)
        amt = float(input('Please enter amount in Rs.'))
        time.sleep(2)
        b.deposit(amt)
    elif choice == '2':
        print(nm,'you have selected Debit option')
        time.sleep(2)
        amt = float(input('Please enter amount in Rs.'))
        time.sleep(2)
        b.withdraw(amt)
    elif choice == '3':
        print(nm, 'Please wait we are fetching your current balance')
        time.sleep(2)
        print('Your Current Balance is Rs:',b.bal)
    else:
        print(nm,'Thank you for your time')
        print('Visit again...!!!!!')
        #break
        exit()
print('Do the next step....')
for i in range(4):
    print(i)

# Assignment: Create a DMart application
# Assignment: Covid19 registration application

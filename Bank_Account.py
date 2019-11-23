#This is an OOP python project to create a Bank Account
#variables are:
#first name
#last name
#account number
#starting balance
#current balance

#Methods
#withdraw
#deposit
#interaccount transfer

# Bank Account has a checkings and savings account
# Checkings Account is a bank account - it inherits the bank accout class
# Savings Account is a bank account - it inherits the bank accout class



# learning
class Bank_Account:
    #self it used to access variables within a class. It has to be the first parameter in a function
    def __init__(self, first_name, last_name, account_number,starting_balance,current_balance):
        self.first_name = first_name
        self.last_name = last_name
        self.account_number = account_number
        self.starting_balance = starting_balance
        self.current_balance = starting_balance
    def deposit(self,deposit_amount):
        self.current_balance = self.starting_balance + deposit_amount
        return self.current_balance
    def withdraw(self,withdrawal_amount):
        self.current_balance = self.starting_balance - withdrawal_amount
        return self.current_balance
    def get_current_balance(self):
        return self.current_balance

class Savings_Account(Bank_Account):
    pass

class Checkings_Account(Bank_Account):
    pass


#initiated a new bank account object
b_acount = Bank_Account("Wura","Sonubi",3432,0,0)

action = input("Would you like to make a deposit or withdraw? ")
if action == "withdraw":
    withdraw_amount = int(input("please enter the withdrawal ammount "))
    b_acount.withdraw(withdraw_amount)
elif action == "deposit":
    depo_amount = int(input("please enter the depost ammount "))
    b_acount.deposit(depo_amount)

print(f"You now have {b_acount.get_current_balance()} in your bank account")

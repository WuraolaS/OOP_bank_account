#This is an OOP python project to create a Bank Account

# Bank Account has a checkings and savings account
# Checkings Account is a bank account - it inherits the bank accout class
# Savings Account is a bank account - it inherits the bank accout class

# Bank acount attribute:
#Account number
#Starting balance
#Transactions
#Current balance

# Methods:
#Withdrawal
#deposit
#interaccount transfers
class Bank_Account:
    #init initializes the class attributes once an object is created
    #self refers to the newly created objected created from the class
    def __init__(self, account_number, starting_balance, current_balance):
        self.account_number
#         #create a new bank account
#         self.account_number = account_number
#         self.starting_balance = 0
#         self.current_balance = 0
#     # def set_starting_balance(amount):
#     #     self.starting_balance = amount
#     # def get_starting_balnce
#
#
#     def deposit(self,deposit_amount):
#         self.current_balance = self.starting_balance + self.deposit_amount
#
#     # def withdraw(self.withdrawal_amount):
#     #     self.current_balance = starting_balance - withdrawal_amount
#
#     # def deposit(deposit_amount):
#     #     current_balance = starting_balance + deposit_amount
#
#     # def get_current_balance():
#     #     return current_balance
#
# B = Bank_Account()
# #The bank account determines the starting balance
# B.account_number = 243
# # B.starting_balance = 100
# B.deposit(5)
# print(B.current_balance)

#current blocker when I try to use a method it returns this output:
# raceback (most recent call last):
#   File "Bank_Account.py", line 41, in <module>
#     B.set_starting_balance(5)
# TypeError: set_starting_balance() takes 1 positional argument but 2 were given


# learning
class Bank_Account:
    #self it used to access variables within a class. It has to be the first parameter in a function
    def __init__(self, account_number,starting_balance,current_balance):
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

#initiated a new bank account object
b_acount = Bank_Account(3432,0,0)

action = input("Would you like to make a deposit or withdraw? ")
if action == "withdraw":
    withdraw_amount = int(input("please enter the withdrawal ammount "))
    b_acount.withdraw(withdraw_amount)
elif action == "deposit":
    depo_amount = int(input("please enter the depost ammount "))
    b_acount.deposit(depo_amount)

print(f"You now have {b_acount.get_current_balance()} in your bank account")

#if I deposit 200 withdrawing 50 should return 50 hmm.
# b_acount.withdraw(50)
#print(f"{b_acount.account_number} has {b_acount.current_balance} in the account")

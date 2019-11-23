from random import randint
randint(100, 999)

class Bank_Account:
    #self it used to access variables within a class. It has to be the first parameter in a function
    #init runs everytime we create a new bank account
    def __init__(self, first_name, last_name, account_number,starting_balance,current_balance):
        self.first_name = first_name
        self.last_name = last_name
        #to scale use random generator to have this create a random 6 digit number
        self.account_number = account_number
        self.starting_balance = starting_balance
        self.current_balance = starting_balance

#methods automatically take the instance as the first argument
    #Used to collect the account details
    def get_account_info(self):
        return "first name is {} , last name is {} , account number is {}, starting balance was {}, current balance is {}".format(self.first_name, self.last_name,self.account_number,self.starting_balance,self.current_balance)

    def deposit(self,deposit_amount):
        self.current_balance = self.starting_balance + deposit_amount
        return self.current_balance

    def withdraw(self,withdrawal_amount):
        self.current_balance = self.starting_balance - withdrawal_amount
        return self.current_balance
    #def interaccount transfer
    def get_current_balance(self):
        return self.current_balance

class Savings_Account(Bank_Account):
    #interst rate is the classes attribute
     interest_rate = 0.6
    # def __init__(self, first_name, last_name, account_number,starting_balance,current_balance)

class Checkings_Account(Bank_Account):
    pass



#initiated a new bank account object
# Wuras_account = Bank_Account("Wura","Sonubi",3432,0,0)
# print(Wuras_account.account_number)
# print(Wuras_account.get_account_info())
Wuras_C_account = Checkings_Account("Wura","Sonubi",3943,0,0)
Wuras_S_account = Savings_Account("Wura","Sonubi",5882,0,0)

action = input("Hello welcome to chase, what would you like to do today: ")

if action == "checkings account info":
    print(Wuras_C_account.get_account_info())
elif action == "deposit":
    d_amount = int(input("How much would you like to deposit? "))
    account_choice = input("would you like to deposit to your savings or checkings? ")
    if account_choice == "checkings":
        Wuras_C_account.deposit(d_amount)
        print(Wuras_C_account.get_account_info())
    elif account_choice == "savings":
        Wuras_S_account.deposit(d_amount)
        print(Wuras_S_account.get_account_info())
    else:
        print("sorry can't read amount")
elif action == "withdrawal":
    w_amount = int(input("How much would you like to withdraw? "))
    account_choice = input("would you like to withdraw from your savings or checkings? ")
    if account_choice == "checkings":
        Wuras_C_account.withdraw(w_amount)
        print(Wuras_C_account.get_account_info())
    elif account_choice == "savings":
        Wuras_S_account.withdraw(w_amount)
        print(Wuras_S_account.get_account_info())
else:
    print("sorry can't help")

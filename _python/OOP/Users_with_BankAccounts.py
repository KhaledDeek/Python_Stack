class BankAccount:
    def __init__(self , int_rate ):
        self.int_rate = int_rate  
        self.account_no = 0
        self.accounts = [0,0]
    def deposit(self, amount , account_no ):
        self.accounts[account_no] += amount
        print(self.accounts)
        return self
    
    def withdraw(self, amount, account_no ):
        self.balance -= amount
        return self


class User:
    def __init__ (self , name , email):
        self.name = name 
        self.email = email 
        self.account_no = 0
        self.accounts = [0,0]
        self.account = BankAccount(int_rate= 0.02 )
    def make_deposit(self , amount ,account_no):
        self.accounts[account_no] +=amount
        return self
    def make_withdrawal(self, amount,account_no):
        self.accounts[account_no] -=amount
        return self
    def display_user_balance(self):
        for i in range(len(self.accounts)):
            print(f"Account {i} balance =" ,self.accounts[i] )
    def transfer_money(self , name , amount ,account_no):
        self.accounts[account_no] -=amount
        name.accounts[account_no] += amount
        




khaled = User("Khaled", "deek@axsos.com")
deek = User("Deek" , "khaled@axsos.com")
desperado = User("Desperado" , "desperado@axsos.com")





khaled = User("Khaled", "deek@axsos.com")
deek = User("Deek" , "khaled@axsos.com")
desperado = User("Desperado" , "desperado@axsos.com")



1#
khaled.make_deposit(100 , 0).make_deposit(100 , 1).make_deposit(100 , 1).make_withdrawal(100 , 1).display_user_balance()


2#
deek.make_deposit(100 , 0).make_deposit(250 , 1).make_withdrawal(120 , 0).make_withdrawal(130 , 1).display_user_balance()

3#
desperado.make_deposit(250 , 1).make_withdrawal(30 , 1).make_withdrawal(20 , 1).make_withdrawal(100 , 0).display_user_balance()


4#
khaled.transfer_money(desperado, 100 , 1)
khaled.display_user_balance()
desperado.display_user_balance()
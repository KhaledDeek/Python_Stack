class User:
    def __init__ (self , name , email):
        self.name = name 
        self.email = email 
        self.account_balance = 0
    def make_deposit(self , amount):
        self.account_balance += amount
        return self
    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self
    def display_user_balance(self):
        print(self.account_balance)
    def transfer_money(self , name , amount):
        self.account_balance -=amount
        name.account_balance += amount
        





khaled = User("Khaled", "deek@axsos.com")
deek = User("Deek" , "khaled@axsos.com")
desperado = User("Desperado" , "desperado@axsos.com")



1#
khaled.make_deposit(100).make_deposit(100).make_deposit(100).make_withdrawal(100).display_user_balance()


2#
deek.make_deposit(100).make_deposit(250).make_withdrawal(120).make_withdrawal(130).display_user_balance()

3#
desperado.make_deposit(250).make_withdrawal(30).make_withdrawal(20).make_withdrawal(100).display_user_balance()


4#
khaled.transfer_money(desperado, 100)
khaled.display_user_balance()
desperado.display_user_balance()
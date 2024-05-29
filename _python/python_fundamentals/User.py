class User:
    def __init__(self,name , email_address):
        self.name = name
        self.email = email_address
        self.account_balance = 0
    
    def make_deposit(self , amount):
        self.account_balance += amount
        
    def make_withdrawal(self , amount):
        self.account_balance -= amount
    
    def display_user_balance(self):
        print(self.account_balance)
    
    def transfer_money(self , amount, namex):
        self.account_balance -= amount
        namex.account_balance += amount

khaled = User("Khaled", "deek@axsos.com")
deek = User("Deek", "khaled@axsos.com")
desperado = User("Desperado", "desperado@axsos.com")


1#
khaled.make_deposit(100)
khaled.make_deposit(150)
khaled.make_deposit(250)
khaled.make_withdrawal(130)
khaled.display_user_balance()

2#
deek.make_deposit(100)
deek.make_deposit(250)
deek.make_withdrawal(120)
deek.make_withdrawal(130)
deek.display_user_balance()

3#
desperado.make_deposit(250)
desperado.make_withdrawal(30)
desperado.make_withdrawal(20)
desperado.make_withdrawal(100)
desperado.display_user_balance()



4# bonus

khaled.transfer_money(100 , desperado)
khaled.display_user_balance()
desperado.display_user_balance()

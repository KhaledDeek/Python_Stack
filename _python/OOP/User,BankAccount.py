class BankAccount:
    def __init__(self , balance , int_rate):
        self.balance = 0
        self.int_rate = 0.02
    
    def deposit(self, amount):
        self.balance += amount
        return self
    
    def withdraw(self, amount):
        self.balance -= amount
        return self
    
    def display_account_info(self):
        balance_withrate = (self.balance*self.int_rate) + self.balance
        print( self.balance , self.int_rate , balance_withrate)
        return self
    
    def yield_interest(self):
        if self.balance > 0 : 
            self.balance = (self.balance * self.int_rate) + self.balance 
            print(self.balance)
            return self
        


class User:
    def __init__(self ,name , email_address):
        self.name = name
        self.email = email_address
        self.account = BankAccount(int_rate=0.02, balance=0)
        
    
    def make_deposit(self, amount): 
        self.account.balance += amount
        return self
    def make_withdrawal(self, amount):
        self.account.balance -= amount
        return self
    def display_user_balance(self):
        print(self.account.balance)
        return self
    def transfer_money(self, other_User, amount):
        self.account.balance -= amount
        other_User.account.balance += amount
    def new_account(self,new_account_number):
        pass
        #self.account_number.append(new_account_number)
        #print(self.account_number)
        #return self.account_number


khaled = User("Khaled", "deek@axsos.com")
deek = User("Deek" , "khaled@axsos.com")
desperado = User("Desperado", "desperado@axsos.com")


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


5#
#khaled.new_account(2)
#khaled.display_user_balance([1])

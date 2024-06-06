

class BankAccount:
    def __init__(self , balance , int_rate):
        self.balance = balance
        self.int_rate = int_rate
    
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
        




khaled = BankAccount(  2000 , 0.02)
yousef = BankAccount( 1000 , 0.02)

khaled.deposit(100).deposit(150).deposit(250).withdraw(200).display_account_info()
yousef.deposit(500).deposit(200).withdraw(100).withdraw(100).withdraw(100).withdraw(200).display_account_info()



class BankAccount:
    def __init__(self , saving_account, current_account, int_rate):
        self.saving_account = 0
        self.current_account = 0
        self.int_rate = int_rate
        
    
    def deposit(self, type , amount ):
        if type == "Saving":
            self.saving_account += amount
            return self
        else:
            self.current_account +=amount
    
    def withdraw(self, type, amount):
        if type == "Saving":
            self.saving_account -= amount
            return self
        else:
            self.current_account -=amount
    
    def display_account_info(self , type):
        if type == "Saving":
            balance_withrate = (self.saving_account*self.int_rate) + self.saving_account
            print( self.saving_account , self.int_rate , balance_withrate)
            return self
        else:
            balance_withrate = (self.current_account*self.int_rate) + self.current_account
            print( self.current_account , self.int_rate , balance_withrate)
            return self
    def yield_interest(self , type ):
        if type == "Saving":
            if self.saving_account > 0 : 
                self.saving_account = (self.saving_account * self.int_rate) + self.saving_account 
                print(self.saving_account)
                return self
        else:
            self.current_account = (self.current_account * self.int_rate) + self.current_account
            print(self.current_account)
            return self 

class User:
    def __init__ (self , name , email):
        self.name = name 
        self.email = email 
        self.account = BankAccount(int_rate=0.02 , saving_account =0 , current_account=0 )
        
    def make_deposit(self , amount , type):
        if type == "Saving":
            self.account.saving_account += amount
            return self
        else: 
            self.account.current_account +=amount
            return self
    def make_withdrawal(self, amount , type ):
        if type == "Saving":
            self.account.saving_account -= amount
            return self
        else: 
            self.account.current_account -=amount
            return self
    def display_user_balance(self):
        print("Saving_Balance = " +str(self.account.saving_account) , "Current_Balance = "+str(self.account.current_account))
    def transfer_money(self , name , amount , type):
        if type == "Saving":
            self.account.saving_account -=amount
            name.account.saving_account +=amount
        else:
            self.account.current_account -=amount
            name.account.current_account += amount
        


khaled = User("Khaled", "deek@axsos.com")
deek = User("Deek" , "khaled@axsos.com")
desperado = User("Desperado" , "desperado@axsos.com")

1#
khaled.make_deposit(100 , "Saving").make_deposit(100, "Saving").make_deposit(100, "Current").make_withdrawal(20, "Current").display_user_balance()


2#
deek.make_deposit(100, "Saving").make_deposit(250, "Saving").make_withdrawal(120, "Current").make_withdrawal(70,"Current").display_user_balance()

3#
desperado.make_deposit(250, "Saving").make_withdrawal(30, "Saving").make_withdrawal(20, "Saving").make_withdrawal(100, "Saving").display_user_balance()


4#
khaled.transfer_money(desperado, 100, "Saving")
khaled.display_user_balance()
desperado.display_user_balance()





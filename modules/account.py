from .owner import Owner

class Account():
    def __init__(self, balance, owner):
        self.id = owner.owner_id()
        self.balance = None
        self.maybe = balance
        self.owner = owner.account_owner()
        if self.maybe > 0:
            self.balance = balance
        else:
            print("Balance needs to be above zero")
        
    def withdraw(self, amount):
        expected_balance = self.balance - amount
        if expected_balance > 0:
            self.balance = expected_balance
            return self.balance
        else:
            return f'Warning not enough funds to withdraw\nCurrent Balance: ${self.balance}'
    
    def deposit(self, amount):
        self.balance = self.balance + amount
        return self.balance

    def get_balance(self):
        if self.balance != None:
            return self.balance 
        else:
            return "No account exists"

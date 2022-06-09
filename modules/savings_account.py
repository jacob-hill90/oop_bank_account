from .account import Account

class SavingsAccount(Account):
    minimum_balance = 10
    withdraw_fee = 2

    def __init__(self, id, balance, open_date, owner):
        super().__init__(id, balance, open_date, owner=owner)

        if balance < self.minimum_balance:
            raise ValueError(f"Savings account needs to be at least ${self.minimum_balance}")
        
    def withdraw(self, amount):
        if self.balance - amount - self.withdraw_fee < self.minimum_balance:
            raise ValueError('Can not withdraw amount specified')

        self.balance = self.balance - amount
        return self.balance

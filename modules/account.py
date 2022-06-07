from .owner import Owner
import os
import csv

class Account():
    def __init__(self, id, balance, open_date):
        self.id = id
        self.balance = int(balance)
        self.open_date = open_date
        self.maybe = int(balance)
        
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

    def get_id(self):
        return self.id

    @classmethod
    def objects(cls):
            accounts = []
            my_path = os.path.abspath(os.path.dirname(__file__))
            path = os.path.join(my_path, "../support/accounts.csv")
            with open(path) as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    acct = Account(row[0], row[1], row[2])
                    accounts.append(acct)
            return accounts
            
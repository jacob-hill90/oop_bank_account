from .owner import Owner
import csv
import os

class Account():
    def __init__(self, id, balance, open_date, owner = None):

        if id == 666:
            raise Exception('Bad account number')
        self.id = id

        if balance < 0:
            raise ValueError("Balance needs to be a positive number")
        self.balance = balance

        self.open_date = open_date
        self.owner = owner

    def __str__(self):
        owner_name = self.owner.name if self.owner is not None else "[no name]"
        return f"This account is owned by {owner_name} and the current balance is {self.get_balance()}"
        

    def set_owner(self, owner):
        if self.owner is not None:
            raise Exception('Can not change owner once set')
        self.owner = owner
       
        
    def withdraw(self, amount):
        if self.balance - amount < 0:
            raise ValueError('Can not withdraw amount specified')
        
        self.balance = self.balance - amount
        return self.balance
    
    def deposit(self, amount):
        self.balance = self.balance + amount
        return self.balance

    def get_balance(self):
        return self.balance

    @classmethod
    def all_accounts(cls):
        accounts = []
        with open("./support/accounts.csv", 'r') as accounts_file:
            data = csv.reader(accounts_file)
            for line in data:
                id = int(line[0])
                balance = int(line[1])/ 100
                open_date = line[2]

                account = cls(id, balance, open_date)
                accounts.append(account)

        return accounts
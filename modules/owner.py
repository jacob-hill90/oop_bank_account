import os
import csv

class Owner():
    owners = []
    def __init__(self, id, first, last, street, city, state):
        self.id = id
        self.first = first
        self.last = last
        self.street = street
        self.city = city
        self.state = state
    
    def account_owner(self):
        return f'The account owner: {self.first} {self.last}'
   
    @classmethod
    def get_id(cls):
        for i in Owner.owners:
            print(i.id)

    def __str__(self):
        return self.first
   
    @classmethod
    def objects(cls):
            my_path = os.path.abspath(os.path.dirname(__file__))
            path = os.path.join(my_path, "../support/owners.csv")
            with open(path) as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    person = Owner(row[0], row[1], row[2], row[3], row[4], row[5])
                    Owner.owners.append(person)
    
            return Owner.owners


import os
import csv

class Owner():
    def __init__(self, id, first, last, street, city, state):
        self.id = id
        self.first = first
        self.last = last
        self.street = street
        self.city = city
        self.state = state
    
    def account_owner(self):
        return f'The account owner: {self.first} {self.last}'

    def owner_id(self):
        return self.id
   
    @classmethod
    def objects(cls):
            owners = []
            my_path = os.path.abspath(os.path.dirname(__file__))
            path = os.path.join(my_path, "../support/owners.csv")
            with open(path) as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    owners.append(Owner(**dict(row)))

            return owners




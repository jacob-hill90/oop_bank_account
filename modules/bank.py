from .account import Account

class Bank():
    def __init__(self):
        self.accounts = []

    def load_accounts(self):
        try:
            self.accounts = Account.all_accounts()
        except Exception as e:
            print(e)
            return None

        return self.accounts

    def find_account_by_id(self,id):
        for a in self.accounts:
            if a.id == id:
                return a
        return None
    

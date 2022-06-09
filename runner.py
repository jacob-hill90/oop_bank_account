from modules.account import Account
from modules.bank import Bank
from modules.owner import Owner

b = Bank()
accounts = b.load_accounts()
# if accounts is not None:
#     for a in accounts:
#         print(a)

a_found = b.find_account_by_id(15152)

print(a_found)


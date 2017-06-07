import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

from models import Transaction

print('transactions:')
for transaction in Transaction.select():
    print(transaction.transaction_id)

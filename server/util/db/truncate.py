import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

from models import Transaction

query = Transaction.delete()
query.execute()

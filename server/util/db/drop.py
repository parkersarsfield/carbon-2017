import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

from config import db_host, db_name, db_user
from models import Transaction
from peewee import *

db = PostgresqlDatabase(db_name, host=db_host, user=db_user)

db.connect()

db.drop_tables([Transaction])

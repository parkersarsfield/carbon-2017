import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

from config import db_host, db_name, db_password, db_user
from models import Transaction
from peewee import *

db = PostgresqlDatabase(db_name, host=db_host, password=db_password, user=db_user)

db.connect()

db.create_tables([Transaction])

from config import db_host, db_name, db_password, db_user
from peewee import *
import datetime

db = PostgresqlDatabase(db_name, autocommit=True, autorollback=True, host=db_host, password=db_password, user=db_user)

class BaseModel(Model):
    class Meta:
        database = db

class Transaction(BaseModel):
    gesture_one = CharField()
    gesture_two = CharField()
    gesture_three = CharField()
    gesture_one_status = IntegerField(default=0)
    gesture_two_status = IntegerField(default=0)
    gesture_three_status = IntegerField(default=0)
    is_complete = BooleanField(default=False)
    timestamp = DateTimeField(default=datetime.datetime.now)
    transaction_id = IntegerField(primary_key=True, unique=True)

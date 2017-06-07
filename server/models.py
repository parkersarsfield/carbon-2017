from peewee import *
import datetime

db = PostgresqlDatabase('postgres', host='localhost', user='postgres')

class BaseModel(Model):
    class Meta:
        database = db

class Transaction(BaseModel):
    gesture_one = CharField()
    gesture_two = CharField()
    gesture_three = CharField()
    is_completed = BooleanField(default=False)
    timestamp = DateTimeField(default=datetime.datetime.now)
    transaction_id = CharField(primary_key=True, unique=True)

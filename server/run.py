from models import Transaction
from datetime import datetime, timedelta
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
import random

app = Flask(__name__)

CORS(app)

@app.route('/api/authenticate', methods=['GET'])
def authenticate():
    gestures = ['left', 'right', 'fist', 'open']

    # TODO do not truncate all transactions in the beginning
    query = Transaction.delete()
    query.execute()

    # create a random group of 3 gestures
    secure_random = random.SystemRandom()

    gesture_one = secure_random.choice(gestures)
    gesture_two = secure_random.choice(gestures)
    gesture_three = secure_random.choice(gestures)

    # TODO correctly increment transaction_id
    transaction_id = 0
    transaction = Transaction.create(gesture_one=gesture_one, gesture_two=gesture_two, gesture_three=gesture_three, transaction_id=transaction_id)

    # TODO send transaction id to armband and tell armband to start listening

    return jsonify(
        gesture_one=gesture_one,
        gesture_two=gesture_two,
        gesture_three=gesture_three,
        transaction_id=transaction_id
    )

@app.route('/api/validate', methods=['PUT'])
def validate():
    result = None

    json = request.get_json(force=True)

    gesture_one = json['gesture_one']
    gesture_two = json['gesture_two']
    gesture_three = json['gesture_three']
    transaction_id = json['transaction_id']

    transaction = Transaction.get(Transaction.transaction_id == transaction_id)

    if (transaction.gesture_one == gesture_one and transaction.gesture_two == gesture_two and transaction.gesture_three == gesture_three):
        result = True
    else:
        result = False

    transaction.is_complete = result
    transaction.save()

    return jsonify(
        result=result
    )

@app.route('/api/check', methods=['GET'])
def check():
    #seconds_limit = 60
    seconds_limit = 5
    time_now = datetime.now()

    transaction_id = request.args.get('transaction_id')
    transaction_id = int(transaction_id)

    transaction = Transaction.get(Transaction.transaction_id == transaction_id)

    if (transaction.is_complete):
        transaction.delete_instance()

        return jsonify(
            status='PASS'
        )
    elif (time_now - transaction.timestamp) <= timedelta(seconds=seconds_limit):
         return jsonify(
             status='WAIT'
         )
    else:
        transaction.delete_instance()

        return jsonify(
             status='FAIL'
         )

from models import db, Transaction
from datetime import datetime, timedelta
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
import random

app = Flask(__name__)

CORS(app)

@app.route('/api/authenticate', methods=['GET'])
def authenticate():
    GESTURES = ['FIST', 'LEFT', 'OPEN', 'RIGHT']

    gesture_one = None
    gesture_two = None
    gesture_three = None

    query = Transaction.delete()
    query.execute()

    secure_random = random.SystemRandom()

    while (gesture_one == gesture_two or gesture_two == gesture_three):
        gesture_one = secure_random.choice(GESTURES)
        gesture_two = secure_random.choice(GESTURES)
        gesture_three = secure_random.choice(GESTURES)

    transaction_id = 0
    transaction = Transaction.create(gesture_one=gesture_one, gesture_two=gesture_two, gesture_three=gesture_three, transaction_id=transaction_id)

    return jsonify(
        gesture_one=gesture_one,
        gesture_two=gesture_two,
        gesture_three=gesture_three,
        transaction_id=transaction_id
    )

@app.route('/api/validate', methods=['PUT'])
def validate():
    # only validate one at a time 

    result = None

    json = request.get_json(force=True)

    current_gesture = json['current_gesture']
    gesture = json['gesture']
    transaction_id = json['transaction_id']

    transaction = Transaction.get(Transaction.transaction_id == transaction_id)

    if current_gesture == 1:
        if transaction.gesture_one == gesture:
            result = True
            transaction.gesture_one_status = 1
        elif transaction.gesture_one_status == 2:
            result = False
            transaction.gesture_one_status = 3;
        else:
            result = False
            transaction.gesture_one_status = 2
    elif current_gesture == 2:
        if transaction.gesture_two == gesture:
            result = True
            transaction.gesture_two_status = 1
        elif transaction.gesture_two_status == 2:
            result = False
            transaction.gesture_two_status = 3;
        else:
            result = False
            transaction.gesture_two_status = 2
    elif current_gesture == 3:
        if transaction.gesture_three == gesture:
            result = True
            transaction.gesture_three_status = 1
            transaction.is_complete = True
        elif transaction.gesture_three_status == 2:
            result = False
            transaction.gesture_three_status = 3;
        else:
            result = False
            transaction.gesture_three_status = 2

    transaction.save()

    return jsonify(
        result=result
    )

@app.route('/api/check', methods=['GET'])
def check():
    SECONDS_LIMIT = 60
    #SECONDS_LIMIT = 5

    fail_hard = False
    fail_soft = False
    json = None
    number_complete = 0
    time_now = datetime.now()
    transaction = None

    transaction_id = request.args.get('transaction_id')
    transaction_id = int(transaction_id)

    try:
        transaction = Transaction.get(Transaction.transaction_id == transaction_id)
    except Transaction.DoesNotExist:
        return ('', 404)

    if transaction.gesture_one_status == 1:
        number_complete = 1
    elif transaction.gesture_one_status == 2:
        fail_soft = True
    elif transaction.gesture_one_status == 3:
        fail_hard = True

    if (transaction.gesture_two_status == 1) and (not fail_soft):
        number_complete = 2
    elif transaction.gesture_two_status == 2:
        fail_soft = True
    elif transaction.gesture_two_status == 3:
        fail_hard = True

    if (transaction.gesture_three_status == 1) and (not fail_soft):
        number_complete = 3
    elif transaction.gesture_three_status == 2:
        fail_soft = True
    elif transaction.gesture_three_status == 3:
        fail_hard = True

    if fail_hard:
        json = jsonify(
            number_complete=number_complete,
            status='FAIL:HARD'
        )
    elif fail_soft:
        json = jsonify(
            number_complete=number_complete,
            status='FAIL:SOFT'
        )
    elif (transaction.is_complete):
        transaction.delete_instance()

        json = jsonify(
            number_complete=3,
            status='PASS'
        )
    elif (time_now - transaction.timestamp) <= timedelta(seconds=SECONDS_LIMIT):
         json = jsonify(
             number_complete=number_complete,
             status='WAIT'
         )
    else:
        transaction.delete_instance()

        json = jsonify(
             status='FAIL:HARD'
         )

    return json

from models import Transaction
from flask import Flask, jsonify, request
import random

gestures = ['left', 'right', 'fist', 'open']

app = Flask(__name__)

@app.route('/api/authenticate', methods=['GET'])
def initiate_authentication():
    # TODO do not truncate all transactions in the beginning
    query = Transaction.delete()
    query.execute()

    # create a random group of 3 gestures
    secure_random = random.SystemRandom()

    gesture_one = secure_random.choice(gestures)
    gesture_two = secure_random.choice(gestures)
    gesture_three = secure_random.choice(gestures)

    # create transaction id
    # TODO correctly increment transaction_id
    transaction_id = 0
    transaction = Transaction.create(gesture_one=gesture_one, gesture_two=gesture_two, gesture_three=gesture_three, transaction_id=transaction_id)

    return jsonify(
        gesture_one=gesture_one,
        gesture_two=gesture_two,
        gesture_three=gesture_three,
        transaction_id=transaction_id
    )

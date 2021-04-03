from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import or_
from os import environ
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_recycle': 299}

db = SQLAlchemy(app)

CORS(app)


class Payment(db.Model):
    __tablename__ = 'payment'

    payment_id = db.Column(db.String(100), nullable=False, primary_key=True)
    liaise_id = db.Column(db.Integer, nullable=False)
    sender_id = db.Column(db.Integer, nullable=False)
    receiver_id = db.Column(db.Integer, nullable=False)
    created = db.Column(db.DateTime, default=datetime.now())
    status = db.Column(db.String(20), nullable=False)


    def __init__(self, payment_id, liaise_id, sender_id, receiver_id, status):
        self.payment_id = payment_id
        self.liaise_id = liaise_id
        self.sender_id = sender_id
        self.receiver_id = receiver_id
        self.status = status
    
    def json(self):
        return {"payment_id": self.payment_id,
                "liaise_id": self.liaise_id,
                "sender_id": self.sender_id,
                "receiver_id": self.receiver_id,
                "created": self.created,
                "status": self.status}

# Get All Payment
@app.route("/payment")
def get_all():
    payment_list = Payment.query.all()
    if len(payment_list):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "payments": [payment.json() for payment in payment_list]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no payments."
        }
    ), 404


# Get All Payout
@app.route("/payment/payout")
def get_payout():
    payment_list = Payment.query.filter(or_(Payment.status=="confirm", Payment.status=="cancel")).all()
    if payment_list:
        return jsonify(
            {
                "code": 200,
                "payments": [payment.json() for payment in payment_list]
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no Payouts available."
        }
    ), 404


# Get a Single Payment
@app.route("/payment/payment_id/<string:payment_id>")
def find_by_payment_id(payment_id):
    payment = Payment.query.filter_by(payment_id=payment_id).first()
    if payment:
        return jsonify(
            {
                "code": 200,
                "data": payment.json()
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "Payment not found."
        }
    ), 404


# Get a Payment by Liaise ID
@app.route("/payment/liaise_id/<string:liaise_id>")
def find_by_liase_id(liaise_id):
    payment = Payment.query.filter_by(liaise_id=liaise_id).first()
    if payment:
        return jsonify(
            {
                "code": 200,
                "data": payment.json()
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "Payment not found."
        }
    ), 404

# Get All Payment by Liaise ID
@app.route("/payment/paymentByLiaiseId/<string:liaise_id>")
def get_homework_liaise_id(liaise_id):
    payment_list = Payment.query.filter_by(liaise_id=liaise_id).all()
    if payment_list:
        return jsonify(
            {
                "code": 200,
                "payments": [payment.json() for payment in payment_list]
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no Payments for this homework."
        }
    ), 404


# Submit Payment
@app.route("/payment/addPayment", methods=['POST'])
def create_payment():
    data = request.get_json()
    payment = Payment(**data)
    try:
        db.session.add(payment)
        db.session.commit()
    except:
        return jsonify(
            {
                "code": 500,
                "message": "An error occurred creating the Payment."
            }
        ), 500
    return jsonify(
        {
            "code": 201,
            "data": payment.json()
        }
    ), 201


#Update Payment Status by Payment Id
@app.route("/payment/updateStatusByPaymentId/<string:payment_id>", methods=['PUT'])
def update_status_payment(payment_id):
    try:
        payment = Payment.query.filter_by(payment_id=payment_id).first()
        if not payment:
            return jsonify(
                {
                    "code": 404,
                    "data": {
                        "payment_id": payment_id
                    },
                    "message": "Payment not found."
                }
            ), 404
        data = request.get_json()
        if data['status']:
            payment.status = data['status']
            db.session.commit()
            return jsonify(
                {
                    "code": 200,
                    "data": payment.json()
                }
            ), 200
    except Exception as e:
        return jsonify(
            {
                "code": 500,
                "data": {
                    "payment": payment_id
                },
                "message": "An error occurred while updating the payment. " + str(e)
            }
        ), 500


#Update Payment Status by Liaise Id
@app.route("/payment/updateStatusByLiaiseId/<string:liaise_id>", methods=['PUT'])
def update_status_liaise(liaise_id):
    try:
        payment = Payment.query.filter_by(liaise_id=liaise_id).first()
        if not payment:
            return jsonify(
                {
                    "code": 404,
                    "data": {
                        "liaise_id": liaise_id
                    },
                    "message": "Payment not found."
                }
            ), 404
        data = request.get_json()
        if data['status']:
            payment.status = data['status']
            db.session.commit()
            return jsonify(
                {
                    "code": 200,
                    "data": payment.json()
                }
            ), 200
    except Exception as e:
        return jsonify(
            {
                "code": 500,
                "data": {
                    "payment": liaise_id
                },
                "message": "An error occurred while updating the payment. " + str(e)
            }
        ), 500


# Delete Payment
@app.route("/payment/deletePayment/<string:payment_id>", methods=['DELETE'])
def delete_payment(payment_id):
    payment = Payment.query.filter_by(payment_id=payment_id).first()
    if payment:
        db.session.delete(payment)
        db.session.commit()
        return jsonify(
            {
                "code": 200,
                "data": {
                    "payment_id": payment_id
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "data": {
                "payment_id": payment_id
            },
            "message": "Payment not found."
        }
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5400, debug=True)
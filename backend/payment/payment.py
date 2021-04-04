from flask import Flask, request, jsonify, json
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import or_
from os import environ
from flask_cors import CORS
from datetime import datetime
import stripe



# This is your real test secret API key.
stripe.api_key = 'sk_test_51IYNsbAnXlfn6Qey2xQsssmxk06NgRtbg5Nsju1nxxhir40QVZe49xU5ZmuEdIKOGKhnPtqlPUzFVdP8UIwJBAWY002ooSpSYA'


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_recycle': 299}

db = SQLAlchemy(app)

CORS(app)


#This part will have to be modified
YOUR_DOMAIN = 'http://localhost/study_buddy/www/Testing/UI'


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
    data = json.loads(request.get_data())
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
        ), 200
    return jsonify(
        {
            "code": 404,
            "data": {
                "payment_id": payment_id
            },
            "message": "Payment not found."
        }
    ), 404



# EXTERNAL API CALLS

# Creating checkout session
@app.route('/create-checkout-session', methods=['POST'])
def create_checkout_session():
    data = json.loads(request.get_data())
    data_list = []
    data_list.append(data)
    print(data_list)
    try:
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=data_list,
            mode='payment',
            success_url=YOUR_DOMAIN + '/success' + "?session_id={CHECKOUT_SESSION_ID}",
            cancel_url=YOUR_DOMAIN + '/cancel' + "?session_id={CHECKOUT_SESSION_ID}",
        )

        # Update database with PK --> Payment ID and DateTime on top of existing data attributes to be updated

        return jsonify({'id': checkout_session.id,
                        'payment_id': checkout_session.payment_intent})
    except Exception as e:
        return jsonify(error=str(e)), 403


# On success, update status of payment to be on HOLD
@app.route('/success', methods=['GET'])
def order_success():
    session = stripe.checkout.Session.retrieve(request.args.get('session_id'))
    payment_intent = stripe.PaymentIntent.retrieve(session.payment_intent)
    payment_id = session.payment_intent

    print(session.payment_intent)

    try:
        payment = Payment.query.filter_by(payment_id=session.payment_intent).first()
        if not payment:
            return jsonify(
                {
                    "code": 404,
                    "data": {
                        "payment_id": payment_intent
                    },
                    "message": "Payment not found."
                }
            ), 404

        
        payment.status = "Hold"
        db.session.commit()

        return jsonify(
            {
                "code": 200,
                "data": {
                    "payment": payment.json(),
                    "payment_id": payment_id
                }
            }
        ), 200
    except Exception as e:
        return jsonify(
            {
                "code": 500,
                "data": {
                    "payment": payment_intent
                },
                "message": "An error occurred while updating the payment. " + str(e)
            }
        ), 500


# On Failure, update status of payment to be FAILED
@app.route('/cancel', methods=['GET'])
def order_failure():
    session = stripe.checkout.Session.retrieve(request.args.get('session_id'))
    payment_intent = stripe.PaymentIntent.retrieve(session.payment_intent)
    payment_id = session.payment_intent

    print(session.payment_intent)

    try:
        payment = Payment.query.filter_by(payment_id=session.payment_intent).first()
        if not payment:
            return jsonify(
                {
                    "code": 404,
                    "data": {
                        "payment_id": payment_intent
                    },
                    "message": "Payment not found."
                }
            ), 404

        
        payment.status = "Failed"
        db.session.commit()

        return jsonify(
            {
                "code": 200,
                "data": {
                    "payment": payment.json(),
                    "payment_id": payment_id
                }
            }
        ), 200
    except Exception as e:
        return jsonify(
            {
                "code": 500,
                "data": {
                    "payment": payment_intent
                },
                "message": "An error occurred while updating the payment. " + str(e)
            }
        ), 500






if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5400, debug=True)
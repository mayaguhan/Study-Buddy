from flask import Flask, request, jsonify
from flask_cors import CORS

import os, sys
from os import environ

import requests
from invokes import invoke_http

import amqp_setup
import pika
import json

app = Flask(__name__)
CORS(app)

user_URL = environ.get('user_URL') or "http://user:5000/user"
payment_URL = environ.get('payment_URL') or "http://payment:5400/payment"
accept_offering_URL = environ.get('accept_offering_URL') or "http://accept_offering:5300/accept_offering"
notification_URL = environ.get('notification_URL') or "http://notification:5800/notification"

# homework_id, liaise_id, tutor_id, status must be passed as JSON.
@app.route("/make_payment", methods=['POST'])
def make_payment():
    if request.is_json:
        try:
            payment = request.get_json()
            # Activate processPayment function to update Homework & Liaise
            result = processPayment(payment)
            print('\n-------------------------')
            print('\nresult: ', result)
            return jsonify(result), result['code']
        
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            ex_str = str(e) + " at " + str(exc_type) + ": " + fname + ": line " + str(exc_tb.tb_lineno)
            print(ex_str)

            return jsonify({
                "code": 500,
                "message": "make_payment.py internal error: " + ex_str
            }), 500
    
    return jsonify({
        "code": 400,
        "message": "Invalid JSON input: " +str(request.get_data())
    })


def processPayment(payment):
    payment_json = {
        "payment_id": 999999, #To Change to payment_id from Stripe API
        "liaise_id": payment['liaise_id'], 
        "sender_id": payment['student_id'], 
        "receiver_id": 100, #user_id of StudyBuddy account
        "status": "Hold"
    }
    payment_result =  invoke_http(payment_URL + '/addPayment', method='POST', json=payment_json)
    payment_code = payment_result["code"]


    # Invoking Accept Offering complex microservice
    accept_offering_json = {
        "homework_id": payment['homework_id'],
        "liaise_id": payment['liaise_id'],
        "tutor_id": payment['tutor_id'],
        "status": "Progress"
    }
    accept_offering_result =  invoke_http(accept_offering_URL + '/accept', method='POST', json=accept_offering_json)
    accept_offering_code = accept_offering_result["code"]
    homework_title = accept_offering_result['data']['homework_result']['data']['title']


    # Invoke user microservice to retrieve sender/receiver details
    student_result = invoke_http(user_URL + '/user_id/' + str(payment['student_id']), method='GET')
    student_code = student_result["code"]
    student_email = student_result['data']['email']
    student_name = student_result['data']['username']

    tutor_result = invoke_http(user_URL + '/user_id/' + str(payment['tutor_id']), method='GET')
    tutor_code = tutor_result["code"]
    tutor_email = tutor_result['data']['email']
    tutor_name = tutor_result['data']['username']


    # Invoke Notification Microservice to send email to Student
    student_email_json = {
        "receiver": student_email,
        "subject": "Acceptance of offer for " + homework_title,
        "content": "You have accepted an offer from " + tutor_name + " for " + homework_title
    }
    student_email_result = invoke_http(notification_URL + '/email', method='POST', json=student_email_json)
    student_email_code = student_email_result["code"]

    tutor_email_json = {
        "receiver": tutor_email,
        "subject": "Acceptance of offer for " + homework_title,
        "content": student_name + " has accepted your offer for " + homework_title
    }
    tutor_email_result = invoke_http(notification_URL + '/email', method='POST', json=tutor_email_json)
    tutor_email_code = tutor_email_result["code"]



    # Return update result
    return {
        "code": 201,
        "data": {
            "payment_result": payment_result,
            "accept_offering_result": accept_offering_result,
            "student_email": student_result,
            "tutor_email": tutor_result, 
            "student_email_result": student_email_result
        }
    }


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5500, debug=True)
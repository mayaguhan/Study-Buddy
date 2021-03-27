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


# homework_id, liaise_id, tutor_id, status must be passed as JSON.
@app.route("/make_payment", methods=['POST'])
def make_payment():
    if request.is_json:
        try:
            payment = request.get_json()
            print("\nReceived a request to accept payment in JSON:", payment)
            
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
    #Updating Homework Microservice, status = Progress
    # liaise_id = 
    # homework_id = 
    # student_id = payment['student_id']
    # tutor_id = 
    # offering = payment['offering']

    # Invoking Payment microservice
    payment_json = {
        "payment_id": 999999, #To Change to payment_id from Stripe API
        "liaise_id": payment['liaise_id'], 
        "sender_id": payment['student_id'], 
        "receiver_id": 100 #user_id of StudyBuddy account
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





    #Check if AMQP is setup
    # amqp_setup.check_setup()

    #Error handling
    # if payment_code not in range(200,300):
    #     #Inform error microservice
    #     print("\n-----Publishing the homework error message with routing_key=homework.error-----")
        
    #     message = json.dumps(accept_offering_result)
    #     amqp_setup.channel.basic_publish(exchange=amqp_setup.exchangename, routing_key="homework.error", body=message, properties=pika.BasicProperties(delivery_mode=2))
    #     #delivery_mode makes the message persistent
    #     print("\nHomework Error Status ({:d}) published to the RabbitMQ Exchange:".format(homework_code), homework_result)


    #     return {
    #         "code": 500,
    #         "data": {"homework_result": homework_result},
    #         "message": "Homework status update failure has been sent for error handling"
    #     }


    # ERROR HANDLING WITHOUT AMQP
    # print("Error in updating homework")
    # return {
    #     "code": 400,
    #     "data": {
    #         # "homework_result": homework_result
    #     },
    #     "message": "There has been an error in updating the homework. Error has been sent for error handling."
    # }
    





    #ERROR HANDLING WITHOUT AMQP
    # if liaise_code not in range(200,300):
    #     print("Error in updating homework")
    #     return {
    #         "code": 400,
    #         "data": {
    #             "liaise_result": liaise_result
    #         },
    #         "message": "There has been an error in updating the liaison. Error has been sent for error handling."
    #     }
    


    
    # Invoke user microservice to retrieve email
    student_result = invoke_http(user_URL + '/user_id/' + str(payment['student_id']), method='GET')
    student_code = student_result["code"]
    student_email = student_result['data']['email']

    tutor_result = invoke_http(user_URL + '/user_id/' + str(payment['tutor_id']), method='GET')
    tutor_code = tutor_result["code"]
    tutor_email = tutor_result['data']['email']


    #Error Handling
    # if tutor_code not in range(200,300):
        #Inform error microservice
        # print("\n-----Publishing the user error with routing_key=user.error-----")

        # message = json.dumps(tutor_result)
        # amqp_setup.channel.basic_publish(exchange=amqp_setup.exchangename, routing_key="user.error", body=message, properties=pika.BasicProperties(delivery_mode=2))
        #delivery_mode makes the message persistent

        # print("\nUser Error Status ({:d}) published to the RabbitMQ Exchange:".format(tutor_code), tutor_result)


        # return {
        #     "code": 500,
        #     "data": {"tutor_result": tutor_result},
        #     "message": "Tutor email retrieval failure has been sent for error handling"
        # }



    # ERROR HANDLING WITHOUT AMQP
    # if tutor_code not in range(200,300):
    #     print("Error in retrieving recipient details")
    #     return {
    #         "code": 400,
    #         "data": {
    #             "tutor_result": tutor_result
    #         },
    #         "message": "There has been an error in retrieving recipient details. Error has been sent for error handling."
    #     }
    # print(tutor_result)
    # print(tutor_result['data']['email']) #Recipient's email?


    # Invoke Notification microservice


    # Return update result
    return {
        "code": 201,
        "data": {
            #Stripe result?
            "payment_result": payment_result,
            "accept_offering_result": accept_offering_result,
            "student_email": student_email,
            "tutor_email": tutor_email
        }
    }


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5500, debug=True)
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
homework_URL = environ.get('homework_URL') or "http://homework:5100/homework"
liaise_URL = environ.get('liaise_URL') or "http://liaise:5200/liaise"
payment_URL = environ.get('payment_URL') or "http://payment:5400/payment"
notification_URL = environ.get('notification_URL') or "http://notification:5800/notification"


# homework_id, liaise_id, tutor_id, status must be passed as JSON.
@app.route("/accept_offering/accept", methods=['POST'])
def accept_offering():
    if request.is_json:
        try:
            offering = request.get_json()
            result = processAcceptance(offering)
            return jsonify(result), result['code']
        
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            ex_str = str(e) + " at " + str(exc_type) + ": " + fname + ": line " + str(exc_tb.tb_lineno)
            print(ex_str)

            return jsonify({
                "code": 500,
                "message": "accept_offering.py internal error: " + ex_str
            }), 500
    
    return jsonify({
        "code": 400,
        "message": "Invalid JSON input: " +str(request.get_data())
    })




def processAcceptance(offering):
    amqp_setup.check_setup()

    # Retrieve Liaise Id & Student Id using Payment Id
    payment_id = offering["payment_id"] #pi_1IcAwKAnXlfn6QeyBm03bBlK
    payment_result = invoke_http(payment_URL + '/payment_id/' + str(payment_id), method='GET', json=offering)
    payment_code = payment_result["code"]
    liaise_id = payment_result["data"]["liaise_id"]
    student_id = payment_result["data"]["sender_id"]

    if payment_code not in range(200,300):
        print("\n-----Publishing the Payment error message with routing_key=payment.error-----")
        message = json.dumps(payment_result)
        amqp_setup.channel.basic_publish(exchange=amqp_setup.exchangename, routing_key="payment.error", body=message, properties=pika.BasicProperties(delivery_mode=2))
        print("\nPayment Error ({:d}) published to the RabbitMQ Exchange:".format(payment_code), payment_result)
        return {
            "code": 500,
            "data": {"payment_result": payment_result},
            "message": "Payment insertion failure has been sent for error handling"
        }


    # Retrieve Homework Id & Tutor Id using Liaise Id
    liaise_result = invoke_http(liaise_URL + '/' + str(liaise_id), method='GET')
    liaise_code = liaise_result["code"]
    tutor_id = liaise_result["data"]["tutor_id"]
    homework_id = liaise_result["data"]["homework_id"]

    if liaise_code not in range(200,300):
        print("\n-----Publishing the Liaise error message with routing_key=liaise.error-----")
        message = json.dumps(liaise_result)
        amqp_setup.channel.basic_publish(exchange=amqp_setup.exchangename, routing_key="liaise.error", body=message, properties=pika.BasicProperties(delivery_mode=2))
        print("\nLiaise Error ({:d}) published to the RabbitMQ Exchange:".format(liaise_code), liaise_result)
        return {
            "code": 500,
            "data": {"liaise_result": liaise_result},
            "message": "Liaise has been sent for error handling"
        }


    # Update Homework Status = Progress
    homework_result = invoke_http(homework_URL + '/updateStatus/' + str(homework_id), method='PUT', json={"status" : "Progress"})
    homework_code = homework_result["code"]
    homework_title = homework_result['data']['title']

    if homework_code not in range(200,300):
        print("\n-----Publishing the Homework update error message with routing_key=homework.error-----")
        message = json.dumps(homework_result)
        amqp_setup.channel.basic_publish(exchange=amqp_setup.exchangename, routing_key="homework.error", body=message, properties=pika.BasicProperties(delivery_mode=2))
        print("\nHomework Error ({:d}) published to the RabbitMQ Exchange:".format(homework_code), homework_result)
        return {
            "code": 500,
            "data": {"homework_result": homework_result},
            "message": "Homework has been sent for error handling"
        }


    # Update Liaise, Accept Tutor, Reject others
    accept_json = {
        "liaise_id": liaise_id, 
        "homework_id": homework_id
    }
    liaise_update_result = invoke_http(liaise_URL + '/accept/' + str(liaise_id) + '/' + str(homework_id), method='PUT', json=accept_json)
    liaise_update_code = liaise_update_result["code"]

    if liaise_update_code not in range(200,300):
        print("\n-----Publishing the Liaise update error message with routing_key=liaise.error-----")
        message = json.dumps(liaise_update_result)
        amqp_setup.channel.basic_publish(exchange=amqp_setup.exchangename, routing_key="liaise.error", body=message, properties=pika.BasicProperties(delivery_mode=2))
        print("\nLiaise Error ({:d}) published to the RabbitMQ Exchange:".format(liaise_update_code), liaise_update_result)
        return {
            "code": 500,
            "data": {"liaise_update_result": liaise_update_result},
            "message": "Liaise has been sent for error handling"
        }


    # Invoke user microservice to retrieve student details
    student_result = invoke_http(user_URL + '/user_id/' + str(student_id), method='GET')
    student_code = student_result["code"]
    student_email = student_result['data']['email']
    student_name = student_result['data']['username']

    if student_code not in range(200,300):
        print("\n-----Publishing the Student error message with routing_key=student.error-----")
        message = json.dumps(student_result)
        amqp_setup.channel.basic_publish(exchange=amqp_setup.exchangename, routing_key="student.error", body=message, properties=pika.BasicProperties(delivery_mode=2))
        print("\nStudent Error ({:d}) published to the RabbitMQ Exchange:".format(student_code), student_result)
        return {
            "code": 500,
            "data": {"student_result": student_result},
            "message": "Student has been sent for error handling"
        }


    # Invoke user microservice to retrieve tutor details
    tutor_result = invoke_http(user_URL + '/user_id/' + str(tutor_id), method='GET')
    tutor_code = tutor_result["code"]
    tutor_email = tutor_result['data']['email']
    tutor_name = tutor_result['data']['username']

    if tutor_code not in range(200,300):
        print("\n-----Publishing the Tutor update error message with routing_key=tutor.error-----")
        message = json.dumps(tutor_result)
        amqp_setup.channel.basic_publish(exchange=amqp_setup.exchangename, routing_key="tutor.error", body=message, properties=pika.BasicProperties(delivery_mode=2))
        print("\nTutor Error ({:d}) published to the RabbitMQ Exchange:".format(tutor_code), tutor_result)
        return {
            "code": 500,
            "data": {"tutor_result": tutor_result},
            "message": "Tutor has been sent for error handling"
        }


    # Invoke Notification Microservice to send email to Student
    student_email_json = {
        "receiver": student_email,
        "subject": "Acceptance of offer for " + homework_title,
        "content": "You have accepted an offer from " + tutor_name + " for " + homework_title
    }
    student_email_result = invoke_http(notification_URL + '/email', method='POST', json=student_email_json)
    student_email_code = student_email_result["code"]

    if student_email_code not in range(200,300):
        print("\n-----Publishing the Student Email update error message with routing_key=student_email.error-----")
        message = json.dumps(student_email_result)
        amqp_setup.channel.basic_publish(exchange=amqp_setup.exchangename, routing_key="student_email.error", body=message, properties=pika.BasicProperties(delivery_mode=2))
        print("\nStudent Email Error ({:d}) published to the RabbitMQ Exchange:".format(student_email_code), student_email_result)
        return {
            "code": 500,
            "data": {"student_email_result": student_email_result},
            "message": "Student Email has been sent for error handling"
        }


    # Invoke Notification Microservice to send email to Tutor
    tutor_email_json = {
        "receiver": tutor_email,
        "subject": "Acceptance of offer for " + homework_title,
        "content": student_name + " has accepted your offer for " + homework_title
    }
    tutor_email_result = invoke_http(notification_URL + '/email', method='POST', json=tutor_email_json)
    tutor_email_code = tutor_email_result["code"]

    if tutor_email_code not in range(200,300):
        print("\n-----Publishing the Tutor Email update error message with routing_key=tutor_email.error-----")
        message = json.dumps(tutor_email_result)
        amqp_setup.channel.basic_publish(exchange=amqp_setup.exchangename, routing_key="tutor_email.error", body=message, properties=pika.BasicProperties(delivery_mode=2))
        print("\nTutor Email Error ({:d}) published to the RabbitMQ Exchange:".format(tutor_email_code), tutor_email_result)
        return {
            "code": 500,
            "data": {"tutor_email_result": tutor_email_result},
            "message": "Tutor Email has been sent for error handling"
        }



    # #Error handling
    # if homework_code not in range(200,300):
    #     #Inform error microservice
    #     print("\n-----Publishing the homework error message with routing_key=homework.error-----")
        
    #     message = json.dumps(homework_result)
    #     amqp_setup.channel.basic_publish(exchange=amqp_setup.exchangename, routing_key="homework.error", body=message, properties=pika.BasicProperties(delivery_mode=2))
    #     #delivery_mode makes the message persistent
    #     print("\nHomework Error Status ({:d}) published to the RabbitMQ Exchange:".format(homework_code), homework_result)


    #     return {
    #         "code": 500,
    #         "data": {"homework_result": homework_result},
    #         "message": "Homework status update failure has been sent for error handling"
    #     }


    #     # ERROR HANDLING WITHOUT AMQP
    #     # print("Error in updating homework")
    #     # return {
    #     #     "code": 400,
    #     #     "data": {
    #     #         "homework_result": homework_result
    #     #     },
    #     #     "message": "There has been an error in updating the homework. Error has been sent for error handling."
    #     # }
    


    # #Invoke liaise microservice to update status
    # updated_liaise_URL = liaise_URL + '/accept/' + str(liaise_id) + '/' + str(homework_id)
    # liaise_result = invoke_http(updated_liaise_URL, method='PUT', json=offering)
    # liaise_code = liaise_result["code"]


    # #Error Handling
    # if liaise_code not in range(200,300):
    #     #Inform error microservice
    #     print("\n-----Publishing the liaise error with routing_key=liaise.error-----")

    #     message = json.dumps(liaise_result)
    #     amqp_setup.channel.basic_publish(exchange=amqp_setup.exchangename, routing_key="liaise.error", body=message, properties=pika.BasicProperties(delivery_mode=2))
    #     #delivery_mode makes the message persistent

    #     print("\nLiaise Error Status ({:d}) published to the RabbitMQ Exchange:".format(liaise_code), liaise_result)


    #     return {
    #         "code": 500,
    #         "data": {"liaise_result": liaise_result},
    #         "message": "Liaise status update failure has been sent for error handling"
    #     }


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


    # Return update result
    return {
        "code": 201,
        "data": {
            "payment_result": payment_result,
            "liaise_result": liaise_result, 
            "homework_result": homework_result,
            "liaise_update_result": liaise_update_result,
            "student_result": student_result,
            "tutor_result": tutor_result
            # "student_email_result": student_email_result,
            # "tutor_email_result": tutor_email_result
        }
    }


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5300, debug=True)
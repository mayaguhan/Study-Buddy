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

homework_URL = environ.get('homework_URL') or "http://homework:5100/homework"
liaise_URL = environ.get('liaise_URL') or "http://liaise:5200/liaise"
payment_URL = environ.get('payment_URL') or" http://payment:5400/payment"


@app.route("/modify_homework/<string:action>", methods=['POST'])
def modify_homework(action):
    if request.is_json:
        try:
            homework = request.get_json()
            result = modifyHomework(homework, action)
            return jsonify(result), result['code']
        
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            ex_str = str(e) + " at " + str(exc_type) + ": " + fname + ": line " + str(exc_tb.tb_lineno)
            print(ex_str)

            return jsonify({
                "code": 500,
                "message": "modify_homework.py internal error: " + ex_str
            }), 500
    
    return jsonify({
        "code": 400,
        "message": "Invalid JSON input: " +str(request.get_data())
    })


def modifyHomework(homework, action):
    amqp_setup.check_setup()

    homework_id = homework['homework_id']
    liaise_id_result = invoke_http(liaise_URL + '/getAccepted/' + str(homework_id), method='GET')
    liaise_id_code = liaise_id_result["code"]

    if liaise_id_code not in range(200,300):
        print("\n-----Publishing the Liaise error message with routing_key=liaise.error-----")
        message = json.dumps(liaise_id_result)
        amqp_setup.channel.basic_publish(exchange=amqp_setup.exchangename, routing_key="liaise.error", body=message, properties=pika.BasicProperties(delivery_mode=2))
        print("\nLiaise Error ({:d}) published to the RabbitMQ Exchange:".format(liaise_id_code), liaise_id_result)
        return {
            "code": 500,
            "data": {"liaise_id_result": liaise_id_result},
            "message": "Liaise has been sent for error handling"
        }
    liaise_id = liaise_id_result['data']['liaise_id']


    if action == "confirm":
        # Update Homework Status = Confirm
        homework_result = invoke_http(homework_URL + '/updateStatus/' + str(homework_id), method='PUT', json={"status" : "Solve"})
        homework_code = homework_result["code"]

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


        # Update Liaise with tutor ratings & remark
        liaise_result = invoke_http(liaise_URL + '/confirmHomework/' + str(liaise_id), method='PUT', json=homework)
        liaise_code = liaise_result["code"]

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


        # Update Payment Status = Confirm
        homework["status"] = "Confirm"
        payment_result = invoke_http(payment_URL + '/updateStatusByLiaiseId/' + str(liaise_id) + '/Hold', method='PUT', json=homework)
        payment_code = payment_result["code"]
        
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

    elif action == "cancel":
        # Update Homework Status = Cancel
        homework["status"] = "Cancel"
        homework_result = invoke_http(homework_URL + '/updateStatus/' + str(homework_id), method='PUT', json=homework)
        homework_code = homework_result["code"]

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


        # Update Liaise as Rejected
        liaise_result = invoke_http(liaise_URL + '/reject', method='PUT', json=homework)
        liaise_code = liaise_result["code"]

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


        # Update Payment Status = Cancel
        payment_result = invoke_http(payment_URL + '/updateStatusByLiaiseId/' + str(liaise_id) + '/Hold', method='PUT', json=homework)
        payment_code = payment_result["code"]

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


    else:
        return {
            "code": 400,
            "message": "Invalid action executed"
        }
    


    # Return update result
    return {
        "code": 201,
        "data": {
            "liaise_id_result": liaise_id_result,
            "homework_result": homework_result,
            "liaise_result": liaise_result,
            "payment_result": payment_result
        }
    }


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5700, debug=True)
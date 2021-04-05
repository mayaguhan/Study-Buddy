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


# homework_id, liaise_id, tutor_id, status must be passed as JSON.
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
    homework_id = homework['homework_id']
    liaise_id = homework['liaise_id']
    if action == "confirm":
        print(homework)
        homework["status"] = "Solve"
        homework_result = invoke_http(homework_URL + '/updateStatus/' + str(homework_id), method='PUT', json=homework)
        homework_code = homework_result["code"]

        liaise_result = invoke_http(liaise_URL + '/confirmHomework/' + str(liaise_id), method='PUT', json=homework)
        liaise_code = liaise_result["code"]

        homework["status"] = "Hold"
        payment_result = invoke_http(payment_URL + '/updateStatusByLiaiseId/' + str(liaise_id), method='PUT', json=homework)
        payment_code = payment_result["code"]

    elif action == "cancel":
        homework["status"] = "Cancel"
        homework_result = invoke_http(homework_URL + '/updateStatus/' + str(homework_id), method='PUT', json=homework)
        homework_code = homework_result["code"]

        liaise_result = invoke_http(liaise_URL + '/reject', method='PUT', json=homework)
        liaise_code = liaise_result["code"]

        payment_result = invoke_http(payment_URL + '/updateStatusByLiaiseId/' + str(liaise_id), method='PUT', json=homework)
        payment_code = payment_result["code"]

    else:
        return {
            "code": 400,
            "message": "Invalid action executed"
        }
    

    # updated_homework_URL = homework_URL + '/' + str(homework_id)
    # homework_result = invoke_http(updated_homework_URL, method='PUT', json=homework)
    # homework_code = homework_result["code"]

    # #Check if AMQP is setup
    # amqp_setup.check_setup()

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
            "homework_result": homework_result,
            "liaise_result": liaise_result,
            "payment_result": payment_result
        }
    }


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5700, debug=True)
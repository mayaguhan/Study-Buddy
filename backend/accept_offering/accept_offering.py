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


# homework_id, liaise_id, tutor_id, status must be passed as JSON.
@app.route("/accept_offering/accept", methods=['POST'])
def accept_offering():
    if request.is_json:
        try:
            offering = request.get_json()
            print("\nReceived a request to accept offering in JSON:", offering)
            
            # Activate processAcceptance function to update Homework & Liaise
            result = processAcceptance(offering)
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
                "message": "accept_offering.py internal error: " + ex_str
            }), 500
    
    return jsonify({
        "code": 400,
        "message": "Invalid JSON input: " +str(request.get_data())
    })


def processAcceptance(offering):
    #Updating Homework Microservice, status = Progress
    print('\n-----Invoking homework microservice-----')
    homework_id = offering['homework_id']
    liaise_id = offering['liaise_id']

    updated_homework_URL = homework_URL + '/' + str(homework_id)
    homework_result = invoke_http(updated_homework_URL, method='PUT', json=offering)
    homework_code = homework_result["code"]

    #Check if AMQP is setup
    amqp_setup.check_setup()

    #Error handling
    if homework_code not in range(200,300):
        #Inform error microservice
        print("\n-----Publishing the homework error message with routing_key=homework.error-----")
        
        message = json.dumps(homework_result)
        amqp_setup.channel.basic_publish(exchange=amqp_setup.exchangename, routing_key="homework.error", body=message, properties=pika.BasicProperties(delivery_mode=2))
        #delivery_mode makes the message persistent
        print("\nHomework Error Status ({:d}) published to the RabbitMQ Exchange:".format(homework_code), homework_result)


        return {
            "code": 500,
            "data": {"homework_result": homework_result},
            "message": "Homework status update failure has been sent for error handling"
        }


        # ERROR HANDLING WITHOUT AMQP
        # print("Error in updating homework")
        # return {
        #     "code": 400,
        #     "data": {
        #         "homework_result": homework_result
        #     },
        #     "message": "There has been an error in updating the homework. Error has been sent for error handling."
        # }
    


    #Invoke liaise microservice to update status
    updated_liaise_URL = liaise_URL + '/accept/' + str(liaise_id) + '/' + str(homework_id)
    liaise_result = invoke_http(updated_liaise_URL, method='PUT', json=offering)
    liaise_code = liaise_result["code"]


    #Error Handling
    if liaise_code not in range(200,300):
        #Inform error microservice
        print("\n-----Publishing the liaise error with routing_key=liaise.error-----")

        message = json.dumps(liaise_result)
        amqp_setup.channel.basic_publish(exchange=amqp_setup.exchangename, routing_key="liaise.error", body=message, properties=pika.BasicProperties(delivery_mode=2))
        #delivery_mode makes the message persistent

        print("\nLiaise Error Status ({:d}) published to the RabbitMQ Exchange:".format(liaise_code), liaise_result)


        return {
            "code": 500,
            "data": {"liaise_result": liaise_result},
            "message": "Liaise status update failure has been sent for error handling"
        }


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
            "liaise_result": liaise_result
        }
    }




if __name__ == "__main__":
    print("This is flask " + os.path.basename(__file__) + " for placing an acceptance request...")
    app.run(host="0.0.0.0", port=5300, debug=True)
    # For our understanding
    # - debug=True will reload the program automatically if a change is detected;
    #   -- it in fact starts two instances of the same flask program, and uses one of the instances to monitor the program changes;
    # - host="0.0.0.0" allows the flask program to accept requests sent from any IP/host (in addition to localhost),
    #   -- i.e., it gives permissions to hosts with any IP to access the flask program,
    #   -- as long as the hosts can already reach the machine running the flask program along the network
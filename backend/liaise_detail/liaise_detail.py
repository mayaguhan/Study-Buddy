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



@app.route("/liaise_detail/<string:homework_id>")
def user_liaise_detail(homework_id):
    # print(liaise_id)
    if homework_id:
        try:
            # Activate retrieveLiaiseDetail function to retrieve user details for each liaise
            result = retrieveLiaiseDetail(homework_id)
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


@app.route("/liaise_detail/liaiseId/<string:liaise_id>")
def user_liaise_detail_by_liaiseId(liaise_id):
    if liaise_id:
        try:
            result = retrieveLiaiseDetailByLiaiseId(liaise_id)
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

def retrieveLiaiseDetail(homework_id):
    #Updating Homework Microservice, status = Progress
    print('\n-----Invoking homework microservice-----')
    return_list = []

    liaisons_result = invoke_http(liaise_URL + '/liaiseByHomework/' + str(homework_id), method='GET')
    liaisons_code = liaisons_result["code"]
    # print(liaisons_result["liaisons"], "\n \n")

    if len(liaisons_result["liaisons"]) > 0:
        for liaise in liaisons_result["liaisons"]:

            tutor_id = liaise["tutor_id"]
            user_result = invoke_http(user_URL + '/user_id/' + str(tutor_id), method='GET')
            user_code = user_result["code"]

            tutor_rating_result = invoke_http(liaise_URL + '/averageRating/' + str(tutor_id), method='GET')
            tutor_rating_code = tutor_rating_result["code"]

            user_result["data"]["rating"] = tutor_rating_result["average"]
            user_result["data"]["liaise_id"] = liaise["liaise_id"]
            user_result["data"]["homework_id"] = liaise["homework_id"]
            user_result["data"]["offering"] = liaise["offering"]
            user_result["data"]["status"] = liaise["status"]

            return_list.append(user_result)



    # #Check if AMQP is setup
    # amqp_setup.check_setup()

    # #Error handling
    # if liaisons_code not in range(200,300):
    #     #Inform error microservice
    #     print("\n-----Publishing the homework error message with routing_key=homework.error-----")
        
    #     message = json.dumps(liaisons_result)
    #     amqp_setup.channel.basic_publish(exchange=amqp_setup.exchangename, routing_key="homework.error", body=message, properties=pika.BasicProperties(delivery_mode=2))
    #     #delivery_mode makes the message persistent
    #     print("\nHomework Error Status ({:d}) published to the RabbitMQ Exchange:".format(liaisons_code), liaisons_result)


    #     return {
    #         "code": 500,
    #         "data": {"homework_result": liaisons_result},
    #         "message": "Homework status update failure has been sent for error handling"
    #     }


        # ERROR HANDLING WITHOUT AMQP
        # print("Error in updating homework")
        # return {
        #     "code": 400,
        #     "data": {
        #         "homework_result": homework_result
        #     },
        #     "message": "There has been an error in updating the homework. Error has been sent for error handling."
        # }
    



    #Error Handling
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
            "liaisons_result" : return_list
        }
    }


def retrieveLiaiseDetailByLiaiseId(liaise_id):
    return_list = []

    liaisons_result = invoke_http(liaise_URL + "/" + str(liaise_id), method='GET')
    liaisons_code = liaisons_result["code"]

    if len(liaisons_result["data"]) > 0:
        tutor_id = liaisons_result["data"]["tutor_id"]
        homework_id = liaisons_result["data"]["homework_id"]
        print(tutor_id, homework_id)

        user_result = invoke_http(user_URL + '/user_id/' + str(tutor_id), method='GET')
        user_code = user_result["code"]

        homework_result = invoke_http(homework_URL + '/' + str(homework_id), method='GET')
        homework_code = homework_result["code"]

        liaisons_result["data"]["tutor_username"] = user_result["data"]["username"]
        liaisons_result["data"]["tutor_contact"] = user_result["data"]["contact"]
        liaisons_result["data"]["tutor_email"] = user_result["data"]["email"]
        liaisons_result["data"]["tutor_telegram_id"] = user_result["data"]["telegram_id"]

        liaisons_result["data"]["homework_title"] = homework_result["data"]["title"]
        liaisons_result["data"]["homework_description"] = homework_result["data"]["description"]
        liaisons_result["data"]["homework_subject"] = homework_result["data"]["subject"]
        liaisons_result["data"]["homework_image"] = homework_result["data"]["image"]

        print(liaisons_result, user_result, homework_result)
        #     user_code = user_result["code"]


    # Return liaise result
    return {
        "code": 201,
        "data": liaisons_result
    }


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5600, debug=True)
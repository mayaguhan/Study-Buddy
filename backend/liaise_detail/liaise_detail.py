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


# # Get All Liaise Offerings by Homework ID
# @app.route("/liaise/liaiseByHomework/<string:homework_id>")
# def get_homework_all(homework_id):
#     liaise_list = Liaise.query.filter_by(homework_id=homework_id).all()
#     if liaise_list:
#         return jsonify(
#             {
#                 "code": 200,
#                 "liaisons": [liaise.json() for liaise in liaise_list]
#             }
#         )
#     return jsonify(
#         {
#             "code": 404,
#             "message": "There are no Liaisons for this homework."
#         }
#     ), 404

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




if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5600, debug=True)
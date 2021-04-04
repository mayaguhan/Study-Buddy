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
    return_list = []

    liaisons_result = invoke_http(liaise_URL + '/liaiseByHomework/' + str(homework_id), method='GET')
    liaisons_code = liaisons_result["code"]

    if len(liaisons_result["liaisons"]) > 0:
        for liaise in liaisons_result["liaisons"]:

            tutor_id = liaise["tutor_id"]
            tutor_result = invoke_http(user_URL + '/user_id/' + str(tutor_id), method='GET')
            tutor_code = tutor_result["code"]

            tutor_rating_result = invoke_http(liaise_URL + '/averageRating/' + str(tutor_id), method='GET')
            tutor_rating_code = tutor_rating_result["code"]


            tutor_result["data"]["rating"] = tutor_rating_result["average"]
            tutor_result["data"]["tutor_id"] = liaise["tutor_id"]
            tutor_result["data"]["liaise_id"] = liaise["liaise_id"]
            tutor_result["data"]["homework_id"] = liaise["homework_id"]
            tutor_result["data"]["offering"] = liaise["offering"]
            tutor_result["data"]["status"] = liaise["status"]

            return_list.append(tutor_result)

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

        homework_result = invoke_http(homework_URL + '/' + str(homework_id), method='GET')
        homework_code = homework_result["code"]
        student_id = homework_result["data"]["student_id"]
        liaisons_result["data"]["homework_title"] = homework_result["data"]["title"]
        liaisons_result["data"]["homework_description"] = homework_result["data"]["description"]
        liaisons_result["data"]["homework_subject"] = homework_result["data"]["subject"]
        liaisons_result["data"]["homework_image"] = homework_result["data"]["image"]
        liaisons_result["data"]["student_id"] = student_id

        tutor_result = invoke_http(user_URL + '/user_id/' + str(tutor_id), method='GET')
        tutor_code = tutor_result["code"]
        liaisons_result["data"]["tutor_username"] = tutor_result["data"]["username"]
        liaisons_result["data"]["tutor_contact"] = tutor_result["data"]["contact"]
        liaisons_result["data"]["tutor_email"] = tutor_result["data"]["email"]
        liaisons_result["data"]["tutor_telegram_id"] = tutor_result["data"]["telegram_id"]
        liaisons_result["data"]["tutor_photo"] = tutor_result["data"]["photo"]

        student_result = invoke_http(user_URL + '/user_id/' + str(student_id), method='GET')
        student_code = student_result["code"]
        liaisons_result["data"]["student_username"] = student_result["data"]["username"]
        liaisons_result["data"]["student_contact"] = student_result["data"]["contact"]
        liaisons_result["data"]["student_email"] = student_result["data"]["email"]
        liaisons_result["data"]["student_telegram_id"] = student_result["data"]["telegram_id"]
        liaisons_result["data"]["student_photo"] = student_result["data"]["photo"]


    # Return liaise result
    return {
        "code": 201,
        "data": liaisons_result
    }


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5600, debug=True)